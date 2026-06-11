from datetime import date
import json

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.pipeline.run_daily import run_daily


def test_mock_run_generates_content_without_keys(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.setenv("AI_RESEARCH_PUBLISH_DATE", "2026-06-03")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = run_daily(date(2026, 6, 3), mock=True)
    assert result["qa_passed"] is True
    assert result["papers"] >= 3
    assert result["generated"]
    rows = json.loads((REPO_ROOT / "apps/web/public/search-index.json").read_text(encoding="utf-8"))
    assert {"title", "date", "lang", "url", "summary", "tags", "topics", "authors", "content_excerpt"}.issubset(rows[0])
    assert {row["type"] for row in rows if row["date"] == "2026-06-03" and row["lang"] == "zh"} == {"brief", "sources"}
    report = json.loads((REPO_ROOT / "data/reports/runs/last-run.json").read_text(encoding="utf-8"))
    assert report["candidate_manifest"].endswith("candidate_manifest-2026-06-03.json")
    assert (REPO_ROOT / report["candidate_manifest"]).exists()
    assert (REPO_ROOT / "data/processed/2026-06-03/candidate_manifest.json").exists()
