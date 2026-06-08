from datetime import date, datetime, time, timezone
from email.utils import parsedate_to_datetime
import logging
import re
import time as time_module
from urllib.parse import quote
import feedparser
import httpx
from tenacity import RetryError, retry, stop_after_attempt, wait_exponential
from ..models import Paper
from ..utils.http import DEFAULT_USER_AGENT

logger = logging.getLogger(__name__)
ARXIV_PAGE_SIZE = 100
ARXIV_API_TIMEOUT = 45
ARXIV_API_ATTEMPTS = 5
ARXIV_RATE_LIMIT_MAX_SLEEP = 240


def fetch_arxiv_category(category: str, max_results: int = 50, day: date | None = None) -> list[Paper]:
    try:
        papers, _stats = _fetch_arxiv_api_with_stats(category, max_results, day)
        return papers
    except Exception:
        rows = fetch_arxiv_rss_category(category, max_results)
        return _filter_by_day(rows, day) if day is not None else rows


def _fetch_arxiv_api(category: str, max_results: int = 50, day: date | None = None) -> list[Paper]:
    papers, _stats = _fetch_arxiv_api_with_stats(category, max_results, day)
    return papers


def _fetch_arxiv_api_with_stats(
    category: str,
    max_results: int = 50,
    day: date | None = None,
    request_delay_seconds: float = 0.0,
) -> tuple[list[Paper], dict]:
    query_text = f"cat:{category}"
    if day:
        stamp = day.strftime("%Y%m%d")
        query_text += f" AND submittedDate:[{stamp}0000 TO {stamp}2359]"
    return _fetch_arxiv_query_with_stats(query_text, max_results=max_results, request_delay_seconds=request_delay_seconds)


def _fetch_arxiv_combined_api(categories: list[str], max_results: int = 1000, day: date | None = None) -> list[Paper]:
    papers, _stats = _fetch_arxiv_combined_api_with_stats(categories, max_results, day)
    return papers


def _fetch_arxiv_combined_api_with_stats(
    categories: list[str],
    max_results: int = 1000,
    day: date | None = None,
    request_delay_seconds: float = 0.0,
) -> tuple[list[Paper], dict]:
    category_query = " OR ".join(f"cat:{category}" for category in categories)
    query_text = f"({category_query})"
    if day:
        stamp = day.strftime("%Y%m%d")
        query_text += f" AND submittedDate:[{stamp}0000 TO {stamp}2359]"
    return _fetch_arxiv_query_with_stats(query_text, max_results=max_results, request_delay_seconds=request_delay_seconds)


def _fetch_arxiv_query(query_text: str, max_results: int = 50) -> list[Paper]:
    papers, _stats = _fetch_arxiv_query_with_stats(query_text, max_results=max_results)
    return papers


def _fetch_arxiv_query_with_stats(
    query_text: str,
    max_results: int = 50,
    page_size: int = ARXIV_PAGE_SIZE,
    request_delay_seconds: float = 0.0,
) -> tuple[list[Paper], dict]:
    max_results = max(int(max_results), 0)
    page_size = max(1, min(int(page_size), ARXIV_PAGE_SIZE, max_results or ARXIV_PAGE_SIZE))
    papers: list[Paper] = []
    page_lengths: list[int] = []
    starts: list[int] = []
    page_error = ""
    if max_results == 0:
        return [], {"pages": 0, "requests": 0, "page_lengths": [], "starts": []}

    start = 0
    while start < max_results:
        current_page_size = min(page_size, max_results - start)
        try:
            rows = _fetch_arxiv_query_page(query_text, start=start, max_results=current_page_size)
        except Exception as exc:
            if not papers:
                raise
            page_error = _format_fetch_error(exc)
            logger.warning("Partial arXiv page fetch failed at start=%s: %s", start, page_error)
            break
        papers.extend(rows)
        page_lengths.append(len(rows))
        starts.append(start)
        if len(rows) < current_page_size:
            break
        start += current_page_size
        if request_delay_seconds > 0:
            time_module.sleep(request_delay_seconds)
    return papers, {
        "pages": len(page_lengths),
        "requests": len(page_lengths),
        "page_lengths": page_lengths,
        "starts": starts,
        "max_results": max_results,
        "page_size": page_size,
        "partial": bool(page_error),
        "page_error": page_error,
    }


def _fetch_arxiv_query_page(query_text: str, start: int, max_results: int) -> list[Paper]:
    query = quote(query_text)
    url = f"https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&start={start}&max_results={max_results}"
    last_error: Exception | None = None
    for attempt in range(1, ARXIV_API_ATTEMPTS + 1):
        try:
            r = httpx.get(url, timeout=ARXIV_API_TIMEOUT, follow_redirects=True, headers={"User-Agent": DEFAULT_USER_AGENT})
            if r.status_code == 429:
                delay = _retry_after_seconds(r, attempt)
                logger.warning("arXiv API rate limited start=%s max_results=%s attempt=%s/%s; sleeping %.0fs", start, max_results, attempt, ARXIV_API_ATTEMPTS, delay)
                time_module.sleep(delay)
                continue
            r.raise_for_status()
            feed = feedparser.parse(r.text)
            return [_entry_to_paper(e) for e in feed.entries]
        except Exception as exc:
            last_error = exc
            if attempt >= ARXIV_API_ATTEMPTS:
                break
            delay = min(ARXIV_RATE_LIMIT_MAX_SLEEP, 10 * attempt)
            logger.warning("arXiv API fetch failed start=%s max_results=%s attempt=%s/%s: %s; sleeping %.0fs", start, max_results, attempt, ARXIV_API_ATTEMPTS, _format_fetch_error(exc), delay)
            time_module.sleep(delay)
    if last_error is not None:
        raise last_error
    raise RuntimeError("arXiv API returned HTTP 429 Too Many Requests after retries")


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=2, max=20))
def fetch_arxiv_rss_category(category: str, max_results: int = 50) -> list[Paper]:
    url = f"https://rss.arxiv.org/rss/{category}"
    r = httpx.get(url, timeout=30, follow_redirects=True, headers={"User-Agent": DEFAULT_USER_AGENT})
    r.raise_for_status()
    feed = feedparser.parse(r.text)
    papers: list[Paper] = []
    for e in feed.entries[:max_results]:
        link = getattr(e, "link", "")
        match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", link + " " + getattr(e, "description", ""))
        if not match:
            continue
        arxiv_id = normalize_arxiv_id(match.group(1))
        published = getattr(e, "published_parsed", None) or getattr(e, "updated_parsed", None)
        dt = datetime(*published[:6], tzinfo=timezone.utc) if published else datetime.now(timezone.utc)
        abstract = _clean_rss_description(getattr(e, "description", ""))
        papers.append(Paper(
            id=arxiv_id,
            arxiv_id=arxiv_id,
            title=getattr(e, "title", "").replace("\n", " ").strip(),
            abstract=abstract,
            authors=_rss_authors(e),
            primary_category=category,
            categories=[category],
            published_at=dt,
            updated_at=dt,
            abs_url=f"https://arxiv.org/abs/{arxiv_id}",
            pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
        ))
    return papers


def fetch_arxiv_categories_with_stats(
    categories: list[str],
    max_results_per_category: int = 250,
    day: date | None = None,
    request_delay_seconds: float = 6.0,
    max_total_results: int | None = None,
) -> tuple[list[Paper], dict]:
    papers: list[Paper] = []
    errors: dict[str, str] = {}
    category_counts: dict[str, int] = {category: 0 for category in categories}
    page_stats: dict[str, dict] = {}
    target = str(day) if day else "latest"

    combined_error = ""
    if categories and day is not None:
        try:
            combined_limit = max_total_results or max(max_results_per_category * len(categories), 1000)
            papers, combined_stats = _fetch_arxiv_combined_api_with_stats(
                categories,
                max_results=combined_limit,
                day=day,
                request_delay_seconds=request_delay_seconds,
            )
            category_counts = _count_by_category(papers, categories)
            stats = {
                "target": target,
                "categories": categories,
                "category_counts": category_counts,
                "errors": {},
                "failed_categories": [],
                "successful_categories": [category for category in categories if category_counts.get(category, 0) > 0],
                "total_papers": len(papers),
                "all_categories_failed": False,
                "fetch_mode": "combined_query",
                "max_total_results": combined_limit,
                "page_stats": {"combined_query": combined_stats},
                "page_count": combined_stats.get("pages", 0),
                "request_count": combined_stats.get("requests", 0),
                "partial_fetch_errors": _page_errors({"combined_query": combined_stats}),
            }
            return papers, stats
        except Exception as exc:
            combined_error = _format_fetch_error(exc)
            logger.warning("Combined arXiv fetch failed for %s on %s: %s", categories, target, combined_error)
            if _is_rate_limit_error(combined_error):
                rss_papers, rss_stats = _fetch_categories_from_rss(categories, max_results_per_category, day, request_delay_seconds, max_total_results)
                if rss_papers:
                    rss_stats["errors"]["combined_query"] = combined_error
                    rss_stats["fallback_from"] = "combined_query_rate_limit"
                    return rss_papers, rss_stats
                errors.update(rss_stats.get("errors", {}))
                page_stats.update(rss_stats.get("page_stats", {}))

    for index, category in enumerate(categories):
        failed = False
        try:
            rows, stats_for_category = _fetch_arxiv_api_with_stats(
                category,
                max_results_per_category,
                day=day,
                request_delay_seconds=request_delay_seconds,
            )
            page_stats[category] = stats_for_category
        except Exception as exc:
            message = _format_fetch_error(exc)
            errors[category] = message
            category_counts[category] = 0
            logger.warning("arXiv fetch failed for %s on %s: %s", category, target, message)
            rows = []
            failed = True
            if _is_rate_limit_error(message) and not papers:
                break
        if not rows and not failed:
            logger.info("arXiv returned no papers for %s on %s", category, target)
        category_counts[category] = len(rows)
        papers.extend(rows)
        if index < len(categories) - 1 and request_delay_seconds > 0:
            time_module.sleep(request_delay_seconds)
        if max_total_results and len(papers) >= max_total_results:
            papers = papers[:max_total_results]
            break

    if combined_error:
        errors["combined_query"] = combined_error
    if errors:
        error_messages = [f"{category}: {message}" for category, message in errors.items()]
        logger.warning("Partial arXiv category failures: %s", "; ".join(error_messages))
    stats = {
        "target": target,
        "categories": categories,
        "category_counts": category_counts,
        "errors": errors,
        "failed_categories": sorted(category for category in errors if category in categories),
        "successful_categories": [category for category in categories if category_counts.get(category, 0) > 0],
        "total_papers": len(papers),
        "all_categories_failed": bool(categories) and not papers and bool(errors),
        "fetch_mode": "per_category",
        "max_total_results": max_total_results,
        "page_stats": page_stats,
        "page_count": sum(stats.get("pages", 0) for stats in page_stats.values()),
        "request_count": sum(stats.get("requests", 0) for stats in page_stats.values()),
        "partial_fetch_errors": _page_errors(page_stats),
    }
    return papers, stats


def _fetch_categories_from_rss(
    categories: list[str],
    max_results_per_category: int,
    day: date | None,
    request_delay_seconds: float,
    max_total_results: int | None,
) -> tuple[list[Paper], dict]:
    papers: list[Paper] = []
    errors: dict[str, str] = {}
    category_counts: dict[str, int] = {category: 0 for category in categories}
    page_stats: dict[str, dict] = {}
    for index, category in enumerate(categories):
        try:
            rows = fetch_arxiv_rss_category(category, min(max_results_per_category, 80))
            if day:
                rows = _filter_by_day(rows, day)
            category_counts[category] = len(rows)
            page_stats[category] = {"pages": 1, "requests": 1, "page_lengths": [len(rows)], "starts": [0], "source": "rss"}
            papers.extend(rows)
        except Exception as exc:
            errors[category] = _format_fetch_error(exc)
            page_stats[category] = {"pages": 0, "requests": 1, "page_lengths": [], "starts": [], "source": "rss", "page_error": errors[category]}
        if max_total_results and len(papers) >= max_total_results:
            papers = papers[:max_total_results]
            break
        if index < len(categories) - 1 and request_delay_seconds > 0:
            time_module.sleep(request_delay_seconds)
    stats = {
        "target": str(day) if day else "latest",
        "categories": categories,
        "category_counts": category_counts,
        "errors": errors,
        "failed_categories": sorted(errors),
        "successful_categories": [category for category in categories if category_counts.get(category, 0) > 0],
        "total_papers": len(papers),
        "all_categories_failed": bool(categories) and not papers and bool(errors),
        "fetch_mode": "rss_fallback",
        "max_total_results": max_total_results,
        "page_stats": page_stats,
        "page_count": sum(stats.get("pages", 0) for stats in page_stats.values()),
        "request_count": sum(stats.get("requests", 0) for stats in page_stats.values()),
        "partial_fetch_errors": _page_errors(page_stats),
    }
    return papers, stats


def fetch_arxiv_categories(categories: list[str], max_results_per_category: int = 250, day: date | None = None) -> list[Paper]:
    papers, stats = fetch_arxiv_categories_with_stats(categories, max_results_per_category, day=day)
    if stats["all_categories_failed"]:
        messages = [f"{category}: {message}" for category, message in stats["errors"].items()]
        raise RuntimeError("All arXiv category fetches failed: " + "; ".join(messages))
    return papers


def mock_papers() -> list[Paper]:
    now = datetime.now(timezone.utc)
    rows = [
        ('2606.00001', 'Self Evolving Agents for Tool Use Skills', 'Agents learn reusable tool use skills through iterative self improvement, unit tests, execution feedback, and evaluation. OpenAI and Stanford are mentioned as comparison contexts.', ['Alice Chen', 'Bob Smith'], 'cs.AI'),
        ('2606.00002', 'Efficient Long Context Inference with Cache Compression', 'A systems method reduces memory and latency during long context model inference while preserving code reasoning accuracy.', ['Carol Li'], 'cs.LG'),
        ('2606.00003', 'RAG Evaluation under Noisy Retrieval', 'A benchmark studies retrieval augmented generation reliability under noisy evidence, missing citations, and adversarial documents.', ['Dan Wang'], 'cs.IR'),
        ('2606.00004', 'Multimodal Safety Evaluation for Vision Language Models', 'A safety evaluation suite measures multimodal models across risky visual prompts, jailbreak attempts, and alignment failures.', ['Eva Green'], 'cs.CV'),
        ('2606.00005', 'Code Model Repair with Execution Feedback', 'Code models improve patch generation through execution feedback loops, repository tests, and API-aware repair.', ['Frank Moore'], 'cs.CL'),
        ('2606.00006', 'Robotics Policies with Memory Grounded Planning', 'Embodied robot policies use memory, visual observations, and planning to improve manipulation and navigation.', ['Grace Kim'], 'cs.RO'),
        ('2606.00007', 'Synthetic Data Curation for Post Training', 'A data pipeline selects synthetic instruction data for fine-tuning and post-training with quality filters.', ['Henry Liu'], 'cs.LG'),
        ('2606.00008', 'Mechanistic Attribution for Factual Editing', 'An interpretability method localizes representations involved in factual editing and model memory.', ['Ivy Park'], 'cs.CL'),
        ('2606.00009', 'Open Speech Agent Benchmark', 'A benchmark evaluates speech and audio agents that call tools, transcribe speech, and reason over sound.', ['Jack Sun'], 'cs.SD'),
        ('2606.00010', 'Video Diffusion Models Need Temporal Tests', 'A video generation evaluation suite probes temporal consistency, motion realism, and causal order.', ['Kai Zhao'], 'cs.CV'),
        ('2606.00011', 'Serving Quantized Models with Adaptive Batching', 'A deployment system improves throughput for quantized language models using adaptive batching and cache-aware scheduling.', ['Lina Ortiz'], 'cs.DC'),
        ('2606.00012', 'Preference Optimization for Safer Tool Agents', 'Post-training with preference optimization reduces harmful tool calls and improves auditability.', ['Mona Singh'], 'cs.AI'),
        ('2606.00013', 'Database Native Retrieval for Enterprise RAG', 'A retrieval architecture routes queries to native database, graph, and vector indexes instead of flattening all sources.', ['Nate Brown'], 'cs.IR'),
        ('2606.00014', 'Chart Understanding for Vision Language Models', 'A vision-language benchmark measures chart, table, and document understanding in multimodal models.', ['Olivia Martin'], 'cs.CV'),
        ('2606.00015', 'Agentic 3D Modeling through Code Execution', 'A code intelligence benchmark tests agents that generate executable scripts for procedural 3D modeling.', ['Paul Davis'], 'cs.CL'),
        ('2606.00016', 'Training Data Deduplication for Foundation Models', 'A data engineering workflow removes near duplicates and measures downstream benchmark contamination.', ['Qian Wu'], 'cs.LG'),
        ('2606.00017', 'Red Teaming Open Source LLM Guardrails', 'A safety study evaluates jailbreak resistance, guardrail routing, and risk classification for open-source models.', ['Rita Gomez'], 'cs.AI'),
        ('2606.00018', 'Low Rank Adapters as Model Memory Probes', 'A training analysis uses LoRA adapters to estimate memorization capacity and decide when full fine-tuning is needed.', ['Sam Taylor'], 'cs.LG'),
    ]
    return [Paper(id=i, arxiv_id=i, title=t, abstract=a, authors=au, primary_category=c, categories=[c], published_at=now, updated_at=now, abs_url=f'https://arxiv.org/abs/{i}', pdf_url=f'https://arxiv.org/pdf/{i}') for i,t,a,au,c in rows]


def _entry_to_paper(e) -> Paper:
    arxiv_id = normalize_arxiv_id(e.id.split("/abs/")[-1])
    cats = [t["term"] for t in getattr(e, "tags", [])]
    published = datetime(*e.published_parsed[:6], tzinfo=timezone.utc)
    updated = datetime(*e.updated_parsed[:6], tzinfo=timezone.utc)
    return Paper(
        id=arxiv_id,
        arxiv_id=arxiv_id,
        title=e.title.replace("\n", " ").strip(),
        abstract=e.summary.replace("\n", " ").strip(),
        authors=[a.name for a in getattr(e, "authors", [])],
        primary_category=cats[0] if cats else "cs.AI",
        categories=cats or ["cs.AI"],
        published_at=published,
        updated_at=updated,
        abs_url=f"https://arxiv.org/abs/{arxiv_id}",
        pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
    )


def _filter_by_day(papers: list[Paper], day: date | None) -> list[Paper]:
    if day is None:
        return papers
    return [paper for paper in papers if paper.published_at.date() == day or paper.updated_at.date() == day]


def _retry_after_seconds(response: httpx.Response, attempt: int) -> float:
    value = response.headers.get("Retry-After")
    if value:
        try:
            return min(ARXIV_RATE_LIMIT_MAX_SLEEP, max(30.0, float(value)))
        except ValueError:
            try:
                dt = parsedate_to_datetime(value)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return min(ARXIV_RATE_LIMIT_MAX_SLEEP, max(30.0, (dt - datetime.now(timezone.utc)).total_seconds()))
            except Exception:
                pass
    return min(ARXIV_RATE_LIMIT_MAX_SLEEP, 45.0 * attempt)


def _is_rate_limit_error(message: str) -> bool:
    return "429" in message or "Too Many Requests" in message


def _count_by_category(papers: list[Paper], categories: list[str]) -> dict[str, int]:
    counts = {category: 0 for category in categories}
    for paper in papers:
        for category in paper.categories:
            if category in counts:
                counts[category] += 1
                break
    return counts


def _page_errors(page_stats: dict[str, dict]) -> dict[str, str]:
    return {
        key: str(value.get("page_error"))
        for key, value in page_stats.items()
        if value.get("page_error")
    }


def _clean_rss_description(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"arXiv:\d{4}\.\d{4,5}v?\d*\s+Announce Type:\s+\w+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _rss_authors(entry) -> list[str]:
    value = getattr(entry, "dc_creator", "") or getattr(entry, "author", "")
    if not value:
        return []
    return [part.strip() for part in re.split(r",| and ", value) if part.strip()]


def normalize_arxiv_id(value: str) -> str:
    value = value.strip().split("/")[-1]
    return re.sub(r"v\d+$", "", value)


def _format_fetch_error(exc: Exception) -> str:
    if isinstance(exc, RetryError):
        inner = exc.last_attempt.exception()
        if inner is not None:
            exc = inner
    if isinstance(exc, httpx.HTTPStatusError):
        request = exc.request
        response = exc.response
        return f"HTTP {response.status_code} {response.reason_phrase} for {request.url}"
    return f"{type(exc).__name__}: {exc}"


def date_window(day: date) -> tuple[datetime, datetime]:
    return (
        datetime.combine(day, time.min, tzinfo=timezone.utc),
        datetime.combine(day, time.max, tzinfo=timezone.utc),
    )
