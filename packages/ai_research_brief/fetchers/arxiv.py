from datetime import datetime, timezone
import re
from urllib.parse import quote
import feedparser
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed
from ..models import Paper

def fetch_arxiv_category(category: str, max_results: int = 50) -> list[Paper]:
    try:
        return _fetch_arxiv_api(category, max_results)
    except Exception:
        return fetch_arxiv_rss_category(category, max_results)


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def _fetch_arxiv_api(category: str, max_results: int = 50) -> list[Paper]:
    query = quote(f'cat:{category}')
    url = f'https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={max_results}'
    r = httpx.get(url, timeout=30, follow_redirects=True, headers={'User-Agent':'frontier-paper-radar/0.1'})
    r.raise_for_status()
    feed = feedparser.parse(r.text)
    papers = []
    for e in feed.entries:
        arxiv_id = e.id.split('/abs/')[-1]
        cats = [t['term'] for t in getattr(e, 'tags', [])]
        papers.append(Paper(id=arxiv_id, arxiv_id=arxiv_id, title=e.title.replace('\n',' ').strip(), abstract=e.summary.replace('\n',' ').strip(), authors=[a.name for a in getattr(e,'authors',[])], primary_category=cats[0] if cats else category, categories=cats or [category], published_at=datetime(*e.published_parsed[:6], tzinfo=timezone.utc), updated_at=datetime(*e.updated_parsed[:6], tzinfo=timezone.utc), abs_url=e.id, pdf_url=e.id.replace('/abs/','/pdf/')))
    return papers


@retry(stop=stop_after_attempt(2), wait=wait_fixed(1))
def fetch_arxiv_rss_category(category: str, max_results: int = 50) -> list[Paper]:
    url = f"https://rss.arxiv.org/rss/{category}"
    r = httpx.get(url, timeout=20, follow_redirects=True, headers={"User-Agent": "frontier-paper-radar/0.1"})
    r.raise_for_status()
    feed = feedparser.parse(r.text)
    papers: list[Paper] = []
    for e in feed.entries[:max_results]:
        link = getattr(e, "link", "")
        match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", link + " " + getattr(e, "description", ""))
        if not match:
            continue
        arxiv_id = match.group(1)
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


def fetch_arxiv_categories(categories: list[str], max_results_per_category: int = 80) -> list[Paper]:
    papers: list[Paper] = []
    for category in categories:
        papers.extend(fetch_arxiv_category(category, max_results_per_category))
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


def _clean_rss_description(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"arXiv:\d{4}\.\d{4,5}v?\d*\s+Announce Type:\s+\w+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _rss_authors(entry) -> list[str]:
    value = getattr(entry, "dc_creator", "") or getattr(entry, "author", "")
    if not value:
        return []
    return [part.strip() for part in re.split(r",| and ", value) if part.strip()]
