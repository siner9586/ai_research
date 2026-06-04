import json
from datetime import date
from pathlib import Path
from ..config import REPO_ROOT, ensure_dirs, site_config
from ..fetchers.arxiv import mock_papers, fetch_arxiv_categories
from ..render.markdown import render_daily_markdown
from ..render.rss import build_rss
from ..render.static import build_search_index, build_sitemap
from .dedupe import dedupe_papers
from .enrich import build_signals
from .score import score_papers
from .select import select_papers
from .qa import run_qa


def _write(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, list):
        data = [x.model_dump(mode='json') if hasattr(x, 'model_dump') else x for x in data]
    elif hasattr(data, 'model_dump'):
        data = data.model_dump(mode='json')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def run_daily(day: date, mock: bool = False):
    ensure_dirs()
    pipeline = site_config().get("pipeline", {})
    papers = mock_papers() if mock else fetch_arxiv_categories(
        pipeline.get("arxiv_categories", ["cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.MA", "cs.IR"]),
        int(pipeline.get("max_results_per_category", 80)),
    )
    papers = dedupe_papers(papers)
    signals = build_signals(papers, day, mock=mock)
    scored = score_papers(papers, signals)
    featured, mentions = select_papers(
        scored,
        featured_min=int(pipeline.get("featured_min", 3)),
        featured_max=int(pipeline.get("featured_max", 5)),
        mentions_min=int(pipeline.get("mentions_min", 8)),
        mentions_max=int(pipeline.get("mentions_max", 12)),
    )
    processed = REPO_ROOT / 'data' / 'processed' / str(day)
    _write(REPO_ROOT / 'data' / 'raw' / str(day) / 'papers.json', papers)
    _write(processed / 'papers.json', papers)
    _write(processed / 'signals.json', list(signals.values()))
    _write(processed / 'scored_papers.json', scored)
    _write(processed / 'selected_papers.json', {'featured': [x.model_dump(mode='json') for x in featured], 'mentions': [x.model_dump(mode='json') for x in mentions]})
    files = []
    slugs = {}
    for lang in ("zh", "en"):
        rendered, slug = render_daily_markdown(day, lang, featured, mentions, scored)
        files += rendered
        slugs[lang] = slug
    static_files = [
        str(build_rss("zh")),
        str(build_rss("en")),
        str(build_search_index()),
        str(build_sitemap()),
    ]
    report = run_qa(day, REPO_ROOT / 'data' / 'content', REPO_ROOT / 'data' / 'reports' / 'qa')
    return {
        'date': str(day),
        'mock': mock,
        'papers': len(papers),
        'featured': len(featured),
        'mentions': len(mentions),
        'slugs': slugs,
        'qa_passed': report.passed,
        'generated': files + static_files,
    }
