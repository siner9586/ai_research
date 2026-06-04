from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

from ..config import REPO_ROOT, ensure_dirs, site_config
from ..fetchers.arxiv import fetch_arxiv_categories, mock_papers
from ..models import Paper, PaperSignal, ScoredPaper
from ..render.markdown import render_daily_markdown
from ..render.rss import build_rss
from ..render.static import build_search_index, build_sitemap
from .dedupe import dedupe_papers
from .enrich import build_signals
from .normalize import normalize_papers
from .qa import run_qa
from .score import score_papers
from .select import select_papers


def fetch_stage(day: date, mock: bool = False) -> list[Paper]:
    ensure_dirs()
    pipeline = site_config().get("pipeline", {})
    if mock:
        papers = mock_papers()
    else:
        papers = fetch_arxiv_categories(
            pipeline.get("arxiv_categories", ["cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.MA", "cs.IR"]),
            int(pipeline.get("max_results_per_category", 80)),
            day=day,
        )
    papers = dedupe_papers(normalize_papers(papers))
    if not papers:
        raise RuntimeError(f"No papers found for {day}; refusing to generate an empty production brief")
    _write(REPO_ROOT / "data" / "raw" / str(day) / "papers.json", papers)
    _write(_processed_dir(day) / "papers.json", papers)
    return papers


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
    featured, mentions = select_papers(
        scored,
        featured_min=int(pipeline.get("featured_min", 3)),
        featured_max=int(pipeline.get("featured_max", 5)),
        mentions_min=int(pipeline.get("mentions_min", 8)),
        mentions_max=int(pipeline.get("mentions_max", 15)),
    )
    _write(_processed_dir(day) / "scored_papers.json", scored)
    _write(
        _processed_dir(day) / "selected_papers.json",
        {"featured": [x.model_dump(mode="json") for x in featured], "mentions": [x.model_dump(mode="json") for x in mentions]},
    )
    return scored, featured, mentions


def generate_stage(day: date, lang: str | None = None) -> tuple[list[str], dict[str, str]]:
    scored = _read_scored(day)
    selected = _read_selected(day)
    featured = selected["featured"]
    mentions = selected["mentions"]
    files: list[str] = []
    slugs: dict[str, str] = {}
    langs = [lang] if lang in {"zh", "en"} else ["zh", "en"]
    for item_lang in langs:
        rendered, slug = render_daily_markdown(day, item_lang, featured, mentions, scored)
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


def qa_stage(day: date, allow_warnings: bool = False):
    report = run_qa(day, REPO_ROOT / "data" / "content", REPO_ROOT / "data" / "reports" / "qa")
    if report.errors:
        raise RuntimeError(f"QA failed for {day}: {len(report.errors)} errors, {len(report.warnings)} warnings")
    return report


def run_daily(day: date, mock: bool = False, allow_qa_warnings: bool = False):
    papers = fetch_stage(day, mock=mock)
    enrich_stage(day, mock=mock)
    scored, featured, mentions = score_stage(day)
    generated, slugs = generate_stage(day)
    static_files = build_static_stage()
    report = qa_stage(day, allow_warnings=allow_qa_warnings)
    return {
        "date": str(day),
        "mock": mock,
        "papers": len(papers),
        "featured": len(featured),
        "mentions": len(mentions),
        "slugs": slugs,
        "qa_passed": report.passed,
        "qa_warnings": report.warnings,
        "generated": generated + static_files,
    }


def _processed_dir(day: date) -> Path:
    path = REPO_ROOT / "data" / "processed" / str(day)
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, list):
        data = [x.model_dump(mode="json") if hasattr(x, "model_dump") else x for x in data]
    elif hasattr(data, "model_dump"):
        data = data.model_dump(mode="json")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_json(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"Missing required pipeline artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _read_papers(day: date) -> list[Paper]:
    return [Paper.model_validate(row) for row in _read_json(_processed_dir(day) / "papers.json")]


def _read_signals(day: date) -> list[PaperSignal]:
    path = _processed_dir(day) / "signals.json"
    if not path.exists():
        return []
    return [PaperSignal.model_validate(row) for row in _read_json(path)]


def _read_scored(day: date) -> list[ScoredPaper]:
    return [ScoredPaper.model_validate(row) for row in _read_json(_processed_dir(day) / "scored_papers.json")]


def _read_selected(day: date) -> dict[str, list[ScoredPaper]]:
    payload = _read_json(_processed_dir(day) / "selected_papers.json")
    return {
        "featured": [ScoredPaper.model_validate(row) for row in payload.get("featured", [])],
        "mentions": [ScoredPaper.model_validate(row) for row in payload.get("mentions", [])],
    }


def _recent_topics(day: date) -> set[str]:
    topics: set[str] = set()
    for offset in range(1, 8):
        path = REPO_ROOT / "data" / "processed" / str(day - timedelta(days=offset)) / "selected_papers.json"
        if not path.exists():
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for row in payload.get("featured", []):
            topic = row.get("topic_slug")
            if topic:
                topics.add(topic)
    return topics
