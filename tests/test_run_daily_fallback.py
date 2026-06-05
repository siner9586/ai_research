from datetime import date
import json

import pytest

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.pipeline import run_daily as run_daily_module


def _empty_stats(day, categories):
    return {
        "target": str(day),
        "categories": categories,
        "category_counts": {category: 0 for category in categories},
        "errors": {},
        "failed_categories": [],
        "successful_categories": categories,
        "total_papers": 0,
        "all_categories_failed": False,
    }


def test_run_daily_falls_back_to_recent_real_arxiv_date(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    target = date(2026, 6, 5)
    actual = date(2026, 6, 4)

    def fake_fetch(categories, max_results_per_category, day=None, **_kwargs):
        if day == target:
            return [], _empty_stats(day, categories)
        papers = mock_papers()
        return papers, {
            "target": str(day),
            "categories": categories,
            "category_counts": {category: len(papers) if category == "cs.AI" else 0 for category in categories},
            "errors": {},
            "failed_categories": [],
            "successful_categories": categories,
            "total_papers": len(papers),
            "all_categories_failed": False,
        }

    monkeypatch.setattr(run_daily_module, "fetch_arxiv_categories_with_stats", fake_fetch)
    result = run_daily_module.run_daily(target, mock=False, fallback_days=1)

    assert result["target_date"] == str(target)
    assert result["actual_date"] == str(actual)
    assert result["fallback_used"] is True
    assert result["papers"] == len(mock_papers())

    report = json.loads((REPO_ROOT / "data/reports/runs/last-run.json").read_text(encoding="utf-8"))
    assert report["status"] == "success"
    assert report["fallback_from"] == str(target)
    assert report["actual_date"] == str(actual)

    sources = REPO_ROOT / "data/content/en/daily" / f"{result['slugs']['en']}-sources.md"
    text = sources.read_text(encoding="utf-8")
    assert f'target_date: "{target}"' in text
    assert f'actual_date: "{actual}"' in text
    assert f'fallback_from: "{target}"' in text


def test_run_daily_fails_when_fallback_window_has_no_real_papers(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    target = date(2026, 6, 5)

    def fake_fetch(categories, max_results_per_category, day=None, **_kwargs):
        return [], _empty_stats(day, categories)

    monkeypatch.setattr(run_daily_module, "fetch_arxiv_categories_with_stats", fake_fetch)

    with pytest.raises(RuntimeError, match="No real arXiv papers found"):
        run_daily_module.run_daily(target, mock=False, fallback_days=1)

    report = json.loads((REPO_ROOT / "data/reports/runs/last-run.json").read_text(encoding="utf-8"))
    assert report["status"] == "failed"
    assert report["target_date"] == str(target)
    assert report["actual_date"] is None
    assert report["generated_files"] == []


def test_run_daily_does_not_fallback_when_all_categories_fail(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    target = date(2026, 6, 5)

    def fake_fetch(categories, max_results_per_category, day=None, **_kwargs):
        return [], {
            "target": str(day),
            "categories": categories,
            "category_counts": {category: 0 for category in categories},
            "errors": {category: "HTTP 429 Too Many Requests" for category in categories},
            "failed_categories": categories,
            "successful_categories": [],
            "total_papers": 0,
            "all_categories_failed": True,
        }

    monkeypatch.setattr(run_daily_module, "fetch_arxiv_categories_with_stats", fake_fetch)

    with pytest.raises(RuntimeError, match="All arXiv categories failed"):
        run_daily_module.run_daily(target, mock=False, fallback_days=4)

    report = json.loads((REPO_ROOT / "data/reports/runs/last-run.json").read_text(encoding="utf-8"))
    assert report["status"] == "failed"
    assert len(report["attempts"]) == 1
    assert report["attempts"][0]["date"] == str(target)
    assert report["errors"]["pipeline"].startswith("All arXiv categories failed")
