from __future__ import annotations

import json
import logging
import os
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

from ..config import REPO_ROOT, ensure_dirs, site_config
from ..fetchers.arxiv import fetch_arxiv_categories_with_stats, mock_papers
from ..models import Paper, PaperSignal, ScoredPaper
from ..render.markdown import render_daily_markdown
from ..render.rss import build_rss
from ..render.static import build_search_index, build_sitemap
from .dedupe import dedupe_papers
from .enrich import build_signals
from .normalize import normalize_papers
from .qa import run_qa
from .score import score_papers
from .select import build_repeat_history, repeat_guard_summary, select_papers

logger = logging.getLogger(__name__)
DEFAULT_ARXIV_CATEGORIES = ["cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.MA", "cs.IR"]
PUBLISH_TIMEZONE = "Asia/Shanghai"


class FetchResolutionError(RuntimeError):
    def __init__(self, message: str, attempts: list[dict]):
        super().__init__(message)
        self.attempts = attempts


def fetch_stage(day: date, mock: bool = False) -> list[Paper]:
    papers, _stats = _fetch_stage_with_stats(day, mock=mock)
    return papers


def _fetch_stage_with_stats(day: date, mock: bool = False, fail_on_empty: bool = True) -> tuple[list[Paper], dict]:
    ensure_dirs()
    pipeline = site_config().get("pipeline", {})
    categories = pipeline.get("arxiv_categories", DEFAULT_ARXIV_CATEGORIES)
    if mock:
        mock_dt = datetime.combine(day, time.min, tzinfo=timezone.utc)
        raw_papers = [paper.model_copy(update={"published_at": mock_dt, "updated_at": mock_dt}) for paper in mock_papers()]
        stats = {
            "target": str(day),
            "categories": categories,
            "category_counts": _count_by_category(raw_papers, categories),
            "errors": {},
            "failed_categories": [],
            "successful_categories": categories,
            "total_papers": len(raw_papers),
            "all_categories_failed": False,
            "fetch_mode": "mock",
            "page_stats": {},
            "page_count": 0,
            "request_count": 0,
        }
    else:
        cached_papers = _read_existing_processed_papers(day) if os.environ.get("AI_RESEARCH_REUSE_EXISTING_SOURCE") == "1" else None
        if cached_papers:
            raw_papers = cached_papers
            stats = {
                "target": str(day),
                "categories": categories,
                "category_counts": _count_by_category(raw_papers, categories),
                "errors": {},
                "failed_categories": [],
                "successful_categories": categories,
                "total_papers": len(raw_papers),
                "all_categories_failed": False,
                "fetch_mode": "existing_processed",
                "page_stats": {},
                "page_count": 0,
                "request_count": 0,
                "partial_fetch_errors": {},
            }
        else:
            raw_papers, stats = fetch_arxiv_categories_with_stats(
                categories,
                int(pipeline.get("max_results_per_category", 80)),
                day=day,
                request_delay_seconds=float(pipeline.get("arxiv_request_delay_seconds", 3.5)),
                max_total_results=int(pipeline.get("max_total_results", 0)) or None,
            )
    papers = dedupe_papers(normalize_papers(raw_papers))
    stats["total_candidates"] = len(raw_papers)
    stats["deduped_papers"] = len(papers)
    if fail_on_empty and not papers:
        raise RuntimeError(f"No papers found for {day}; refusing to generate an empty production brief")
    if papers:
        _write(REPO_ROOT / "data" / "raw" / str(day) / "papers.json", papers)
        _write(_processed_dir(day) / "papers.json", papers)
    return papers, stats


def enrich_stage(day: date, mock: bool = False) -> dict[str, PaperSignal]:
    papers = _read_papers(day)
    signals = build_signals(papers, day, mock=mock)
    _write(_processed_dir(day) / "signals.json", list(signals.values()))
    return signals


def score_stage(day: date) -> tuple[list[ScoredPaper], list[ScoredPaper], list[ScoredPaper]]:
    pipeline = site_config().get("pipeline", {})
    papers = _read_papers(day)
    signal_rows = _read_signals(day)
    if not signal_rows:
        signal_rows = list(build_signals(papers, day, mock=False).values())
        _write(_processed_dir(day) / "signals.json", signal_rows)
    signals = {signal.arxiv_id: signal for signal in signal_rows}
    scored = score_papers(papers, signals, recent_topics=_recent_topics(day))
    repeat_guard_days = int(pipeline.get("repeat_guard_days", 30))
    repeat_history = build_repeat_history(
        day,
        days=repeat_guard_days,
        scope=str(pipeline.get("repeat_guard_scope", "featured_and_mentions")),
    )
    featured, mentions = select_papers(
        scored,
        featured_min=int(pipeline.get("featured_min", 3)),
        featured_max=int(pipeline.get("featured_max", 5)),
        mentions_min=int(pipeline.get("mentions_min", 8)),
        mentions_max=int(pipeline.get("mentions_max", 15)),
        repeat_history=repeat_history,
        repeat_guard_featured_strict=bool(pipeline.get("repeat_guard_featured_strict", True)),
    )
    guard_summary = repeat_guard_summary(scored, featured, mentions, repeat_history, repeat_guard_days)
    _write(_processed_dir(day) / "scored_papers.json", scored)
    _write(
        _processed_dir(day) / "selected_papers.json",
        {"featured": [x.model_dump(mode="json") for x in featured], "mentions": [x.model_dump(mode="json") for x in mentions]},
    )
    _write(_processed_dir(day) / "repeat_guard_summary.json", guard_summary)
    return scored, featured, mentions


def generate_stage(
    day: date,
    lang: str | None = None,
    target_date: date | None = None,
    fallback_from: date | None = None,
    publish_date: date | None = None,
) -> tuple[list[str], dict[str, str]]:
    scored = _read_scored(day)
    selected = _read_selected(day)
    featured = selected["featured"]
    mentions = selected["mentions"]
    files: list[str] = []
    slugs: dict[str, str] = {}
    langs = [lang] if lang in {"zh", "en"} else ["zh", "en"]
    for item_lang in langs:
        _remove_publication_markdown(item_lang, publish_date or day)
        rendered, slug = render_daily_markdown(
            day,
            item_lang,
            featured,
            mentions,
            scored,
            target_date=target_date or day,
            fallback_from=fallback_from,
            publish_date=publish_date or day,
        )
        files.extend(rendered)
        slugs[item_lang] = slug
    return files, slugs


def build_static_stage() -> list[str]:
    return [
        str(build_rss("zh")),
        str(build_rss("en")),
        str(build_search_index()),
        str(build_sitemap()),
    ]


def qa_stage(day: date, allow_warnings: bool = False, target_date: date | None = None, publish_date: date | None = None):
    report = run_qa(
        day,
        REPO_ROOT / "data" / "content",
        REPO_ROOT / "data" / "reports" / "qa",
        target_date=target_date,
        publish_date=publish_date,
    )
    if report.errors:
        raise RuntimeError(f"QA failed for data date {day}: {len(report.errors)} errors, {len(report.warnings)} warnings")
    return report


def run_daily(
    day: date,
    mock: bool = False,
    allow_qa_warnings: bool = False,
    fallback_days: int | None = None,
    trigger: str | None = None,
):
    pipeline = site_config().get("pipeline", {})
    fallback_days = int(pipeline.get("fallback_days", 0) if fallback_days is None else fallback_days)
    publish_date = _publication_date()
    run_report = _base_run_report(day, publish_date=publish_date, mock=mock, fallback_days=fallback_days, trigger=trigger)
    try:
        actual_day, papers, fetch_stats, attempts = _resolve_fetch_day(day, mock=mock, fallback_days=fallback_days)
        fallback_from = day if actual_day != day else None
        run_report.update({
            "actual_date": str(actual_day),
            "fallback_used": actual_day != day,
            "fallback_from": str(fallback_from) if fallback_from else None,
            "attempts": attempts,
            "categories": fetch_stats.get("categories", []),
            "category_counts": fetch_stats.get("category_counts", {}),
            "errors": fetch_stats.get("errors", {}),
            "total_candidates": fetch_stats.get("total_candidates", fetch_stats.get("total_papers", 0)),
            "deduped_papers": fetch_stats.get("deduped_papers", len(papers)),
            "fetch_mode": fetch_stats.get("fetch_mode"),
            "page_count": fetch_stats.get("page_count", 0),
            "request_count": fetch_stats.get("request_count", 0),
            "page_stats": fetch_stats.get("page_stats", {}),
            "partial_fetch_errors": fetch_stats.get("partial_fetch_errors", {}),
            "warnings": _fetch_warnings(fetch_stats, day, actual_day),
        })
        _log_run_summary("fetch", run_report)

        enrich_stage(actual_day, mock=mock)
        scored, featured, mentions = score_stage(actual_day)
        manifest = _write_candidate_manifest(
            publish_date=publish_date,
            target_date=day,
            actual_date=actual_day,
            fallback_from=fallback_from,
            mock=mock,
            fetch_stats=fetch_stats,
            papers=papers,
            scored=scored,
            featured=featured,
            mentions=mentions,
        )
        guard_summary = _read_optional_json(_processed_dir(actual_day) / "repeat_guard_summary.json", {})
        generated, slugs = generate_stage(actual_day, target_date=day, fallback_from=fallback_from, publish_date=publish_date)
        static_files = build_static_stage()

        run_report.update({
            "status": "validating",
            "candidate_count": len(scored),
            "featured": len(featured),
            "featured_count": len(featured),
            "mentions": len(mentions),
            "mentions_count": len(mentions),
            "candidate_ids": manifest["candidate_ids"],
            "featured_ids": manifest["featured_ids"],
            "mention_ids": manifest["mention_ids"],
            "selected_ids": manifest["selected_ids"],
            "candidate_manifest": manifest["manifest_file"],
            "candidate_file": manifest["candidate_file"],
            "raw_candidate_file": manifest["raw_candidate_file"],
            "processed_papers_file": manifest["processed_papers_file"],
            "selected_file": manifest["selected_file"],
            "slugs": slugs,
            "generated_files": generated + static_files + [str((REPO_ROOT / manifest["manifest_file"]).resolve())],
            **guard_summary,
        })
        _write_run_report(run_report)
        qa_report = qa_stage(actual_day, allow_warnings=allow_qa_warnings, target_date=day, publish_date=publish_date)

        run_report.update({
            "status": "success",
            "qa_passed": qa_report.passed,
            "qa_warnings": qa_report.warnings,
        })
        _write_run_report(run_report)
        _log_run_summary("complete", run_report)
        return {
            "date": str(publish_date),
            "publish_date": str(publish_date),
            "target_date": str(day),
            "actual_date": str(actual_day),
            "fallback_used": actual_day != day,
            "fallback_from": str(fallback_from) if fallback_from else None,
            "mock": mock,
            "papers": len(papers),
            "total_candidates": run_report["total_candidates"],
            "deduped_papers": run_report["deduped_papers"],
            "candidate_count": run_report["candidate_count"],
            "featured_count": run_report["featured_count"],
            "mentions_count": run_report["mentions_count"],
            "candidate_manifest": run_report["candidate_manifest"],
            "candidate_file": run_report["candidate_file"],
            "selected_file": run_report["selected_file"],
            "fetch_mode": run_report["fetch_mode"],
            "page_count": run_report["page_count"],
            "request_count": run_report["request_count"],
            "page_stats": run_report["page_stats"],
            "partial_fetch_errors": run_report["partial_fetch_errors"],
            "category_counts": run_report["category_counts"],
            "category_errors": run_report["errors"],
            "featured": len(featured),
            "mentions": len(mentions),
            "selected_ids": run_report["selected_ids"],
            "slugs": slugs,
            "qa_passed": qa_report.passed,
            "qa_warnings": qa_report.warnings,
            "generated": generated + static_files,
            "run_report": run_report["report_path"],
            "repeat_guard": guard_summary,
        }
    except Exception as exc:
        attempts = getattr(exc, "attempts", None)
        if attempts:
            run_report["attempts"] = attempts
            last_attempt = attempts[-1]
            run_report["category_counts"] = last_attempt.get("category_counts", {})
            run_report["errors"] = last_attempt.get("errors", {})
            run_report["total_candidates"] = last_attempt.get("total_candidates", 0)
            run_report["deduped_papers"] = last_attempt.get("deduped_papers", 0)
            run_report["fetch_mode"] = last_attempt.get("fetch_mode")
            run_report["page_count"] = last_attempt.get("page_count", 0)
            run_report["request_count"] = last_attempt.get("request_count", 0)
            run_report["page_stats"] = last_attempt.get("page_stats", {})
            run_report["partial_fetch_errors"] = last_attempt.get("partial_fetch_errors", {})
        run_report["status"] = "failed"
        run_report["errors"] = _append_error(run_report.get("errors", {}), "pipeline", str(exc))
        _write_run_report(run_report)
        _log_run_summary("failed", run_report)
        raise


def _read_existing_processed_papers(day: date) -> list[Paper] | None:
    path = REPO_ROOT / "data" / "processed" / str(day) / "papers.json"
    if not path.exists():
        return None
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))
        papers = [Paper(**row) for row in rows]
    except Exception as exc:
        logger.warning("Could not reuse existing processed source papers for %s: %s", day, exc)
        return None
    if not papers:
        return None
    logger.info("Reusing existing processed source papers for %s: %s papers", day, len(papers))
    return papers


def _processed_dir(day: date) -> Path:
    path = REPO_ROOT / "data" / "processed" / str(day)
    path.mkdir(parents=True, exist_ok=True)
    return path


def _reports_dir() -> Path:
    path = REPO_ROOT / "data" / "reports" / "runs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, list):
        data = [x.model_dump(mode="json") if hasattr(x, "model_dump") else x for x in data]
    elif hasattr(data, "model_dump"):
        data = data.model_dump(mode="json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _remove_publication_markdown(lang: str, publish_date: date) -> None:
    daily_dir = REPO_ROOT / "data" / "content" / lang / "daily"
    if not daily_dir.exists():
        return
    for path in daily_dir.glob(f"{publish_date}-*.md"):
        path.unlink()


def _resolve_fetch_day(day: date, mock: bool, fallback_days: int) -> tuple[date, list[Paper], dict, list[dict]]:
    if mock:
        papers, stats = _fetch_stage_with_stats(day, mock=True)
        return day, papers, stats, [_attempt_summary(day, stats)]

    attempts: list[dict] = []
    all_errors: dict[str, str] = {}
    for offset in range(max(fallback_days, 0) + 1):
        candidate_day = day - timedelta(days=offset)
        try:
            papers, stats = _fetch_stage_with_stats(candidate_day, mock=False, fail_on_empty=False)
        except Exception as exc:
            stats = {
                "target": str(candidate_day),
                "categories": site_config().get("pipeline", {}).get("arxiv_categories", DEFAULT_ARXIV_CATEGORIES),
                "category_counts": {},
                "errors": {"fetch": str(exc)},
                "total_candidates": 0,
                "deduped_papers": 0,
                "fetch_mode": None,
                "page_count": 0,
                "request_count": 0,
                "partial_fetch_errors": {},
            }
            attempts.append(_attempt_summary(candidate_day, stats, error=str(exc)))
            all_errors[str(candidate_day)] = str(exc)
            logger.warning("No usable arXiv papers for %s: %s", candidate_day, exc)
            continue
        attempts.append(_attempt_summary(candidate_day, stats))
        if stats.get("all_categories_failed"):
            messages = "; ".join(f"{key}: {value}" for key, value in stats.get("errors", {}).items())
            raise FetchResolutionError(
                "All arXiv categories failed for "
                f"{candidate_day}; not using date fallback because this is a fetch failure, "
                f"not an empty arXiv publication day. Errors: {messages}",
                attempts,
            )
        if papers:
            return candidate_day, papers, stats, attempts

    searched = ", ".join(str(day - timedelta(days=offset)) for offset in range(max(fallback_days, 0) + 1))
    detail = "; ".join(f"{attempt['date']}: {attempt.get('error') or '0 papers'}" for attempt in attempts)
    if all_errors:
        detail = detail or "; ".join(f"{key}: {value}" for key, value in all_errors.items())
    raise FetchResolutionError(
        "No real arXiv papers found for target date or fallback window; "
        f"searched {searched}. Details: {detail}",
        attempts,
    )


def _base_run_report(day: date, publish_date: date, mock: bool, fallback_days: int, trigger: str | None) -> dict:
    pipeline = site_config().get("pipeline", {})
    categories = pipeline.get("arxiv_categories", DEFAULT_ARXIV_CATEGORIES)
    repeat_guard_days = int(pipeline.get("repeat_guard_days", 30))
    return {
        "trigger": trigger or os.environ.get("GITHUB_EVENT_NAME") or "local",
        "date": str(publish_date),
        "publish_date": str(publish_date),
        "target_date": str(day),
        "actual_date": None,
        "fallback_days": fallback_days,
        "fallback_used": False,
        "fallback_from": None,
        "mock": mock,
        "categories": categories,
        "category_counts": {},
        "total_candidates": 0,
        "deduped_papers": 0,
        "candidate_count": 0,
        "featured_count": 0,
        "mentions_count": 0,
        "candidate_ids": [],
        "featured_ids": [],
        "mention_ids": [],
        "selected_ids": [],
        "candidate_manifest": None,
        "candidate_file": None,
        "raw_candidate_file": None,
        "processed_papers_file": None,
        "selected_file": None,
        "fetch_mode": None,
        "page_count": 0,
        "request_count": 0,
        "page_stats": {},
        "partial_fetch_errors": {},
        "featured": 0,
        "mentions": 0,
        "slugs": {},
        "errors": {},
        "warnings": [],
        "generated_files": [],
        "qa_passed": False,
        "qa_warnings": [],
        "repeat_guard_days": repeat_guard_days,
        "excluded_recent_duplicates_count": 0,
        "excluded_recent_duplicates": [],
        "fallback_allowed": False,
        "fallback_reason": None,
        "status": "running",
        "attempts": [],
        "report_path": str((_reports_dir() / f"{publish_date}.json").relative_to(REPO_ROOT)),
    }


def _write_candidate_manifest(
    *,
    publish_date: date,
    target_date: date,
    actual_date: date,
    fallback_from: date | None,
    mock: bool,
    fetch_stats: dict,
    papers: list[Paper],
    scored: list[ScoredPaper],
    featured: list[ScoredPaper],
    mentions: list[ScoredPaper],
) -> dict:
    paths = _candidate_source_paths(actual_date)
    manifest = {
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "publish_date": str(publish_date),
        "target_date": str(target_date),
        "actual_date": str(actual_date),
        "fallback_used": actual_date != target_date,
        "fallback_from": str(fallback_from) if fallback_from else None,
        "mock": mock,
        "fetch_mode": fetch_stats.get("fetch_mode"),
        "candidate_count": len(scored),
        "raw_candidate_count": len(papers),
        "featured_count": len(featured),
        "mentions_count": len(mentions),
        "candidate_ids": _scored_ids(scored),
        "paper_ids": _paper_ids(papers),
        "featured_ids": _scored_ids(featured),
        "mention_ids": _scored_ids(mentions),
        "selected_ids": _scored_ids(featured + mentions),
        **paths,
    }
    _write(REPO_ROOT / paths["manifest_file"], manifest)
    return manifest


def _candidate_source_paths(actual_date: date) -> dict[str, str]:
    prefix = f"data/processed/{actual_date}"
    return {
        "raw_candidate_file": f"data/raw/{actual_date}/papers.json",
        "processed_papers_file": f"{prefix}/papers.json",
        "candidate_file": f"{prefix}/scored_papers.json",
        "selected_file": f"{prefix}/selected_papers.json",
        "manifest_file": f"{prefix}/candidate_manifest.json",
    }


def _paper_ids(papers: list[Paper]) -> list[str]:
    return [paper.arxiv_id for paper in papers]


def _scored_ids(rows: list[ScoredPaper]) -> list[str]:
    return [row.paper.arxiv_id for row in rows]


def _publication_date() -> date:
    pinned = os.environ.get("AI_RESEARCH_PUBLISH_DATE")
    if pinned:
        return date.fromisoformat(pinned)
    return datetime.now(ZoneInfo(PUBLISH_TIMEZONE)).date()


def _write_run_report(report: dict) -> None:
    path = REPO_ROOT / report["report_path"]
    _write(path, report)
    _write(_reports_dir() / "last-run.json", report)


def _read_optional_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def _log_run_summary(stage: str, report: dict) -> None:
    logger.info(
        "daily_brief_%s status=%s publish_date=%s target_date=%s actual_date=%s "
        "fallback_days=%s fallback_used=%s candidates=%s deduped=%s featured=%s mentions=%s",
        stage,
        report.get("status"),
        report.get("publish_date"),
        report.get("target_date"),
        report.get("actual_date"),
        report.get("fallback_days"),
        report.get("fallback_used"),
        report.get("candidate_count") or report.get("total_candidates"),
        report.get("deduped_papers"),
        report.get("featured"),
        report.get("mentions"),
    )


def _attempt_summary(day: date, stats: dict, error: str | None = None) -> dict:
    return {
        "date": str(day),
        "category_counts": stats.get("category_counts", {}),
        "errors": stats.get("errors", {}),
        "total_candidates": stats.get("total_candidates", stats.get("total_papers", 0)),
        "deduped_papers": stats.get("deduped_papers", 0),
        "fetch_mode": stats.get("fetch_mode"),
        "page_count": stats.get("page_count", 0),
        "request_count": stats.get("request_count", 0),
        "page_stats": stats.get("page_stats", {}),
        "partial_fetch_errors": stats.get("partial_fetch_errors", {}),
        "error": error,
    }


def _fetch_warnings(stats: dict, target_day: date, actual_day: date) -> list[str]:
    warnings: list[str] = []
    if actual_day != target_day:
        warnings.append(f"Fallback used internally: target_date={target_day}, actual_date={actual_day}")
    partial_errors = stats.get("partial_fetch_errors") or {}
    if partial_errors:
        warnings.append("Partial fetch fallback used for categories: " + ", ".join(sorted(partial_errors)))
    return warnings


def _append_error(errors, key: str, message: str):
    if not isinstance(errors, dict):
        errors = {"previous": str(errors)}
    errors[key] = message
    return errors


def _count_by_category(papers: list[Paper], categories: list[str]) -> dict[str, int]:
    counts = {category: 0 for category in categories}
    for paper in papers:
        for category in paper.categories:
            if category in counts:
                counts[category] += 1
    return counts


def _read_papers(day: date) -> list[Paper]:
    data = json.loads((_processed_dir(day) / "papers.json").read_text(encoding="utf-8"))
    return [Paper(**x) for x in data]


def _read_signals(day: date) -> list[PaperSignal]:
    path = _processed_dir(day) / "signals.json"
    if not path.exists():
        return []
    return [PaperSignal(**x) for x in json.loads(path.read_text(encoding="utf-8"))]


def _read_scored(day: date) -> list[ScoredPaper]:
    return [ScoredPaper(**x) for x in json.loads((_processed_dir(day) / "scored_papers.json").read_text(encoding="utf-8"))]


def _read_selected(day: date) -> dict[str, list[ScoredPaper]]:
    data = json.loads((_processed_dir(day) / "selected_papers.json").read_text(encoding="utf-8"))
    return {"featured": [ScoredPaper(**x) for x in data.get("featured", [])], "mentions": [ScoredPaper(**x) for x in data.get("mentions", [])]}


def _recent_topics(day: date) -> list[str]:
    topics: list[str] = []
    for delta in range(1, 8):
        path = _processed_dir(day - timedelta(days=delta)) / "selected_papers.json"
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for key in ("featured", "mentions"):
            for row in data.get(key, []):
                topic = row.get("topic_slug") or row.get("topic")
                if topic:
                    topics.append(str(topic))
    return topics[-40:]
