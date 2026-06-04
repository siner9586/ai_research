from datetime import date
import json

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.pipeline.run_daily import run_daily


def test_mock_run_generates_content_without_keys(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    result = run_daily(date(2026, 6, 3), mock=True)
    assert result["qa_passed"] is True
    assert result["featured"] >= 3
    assert result["mentions"] >= 8
    rows = json.loads((REPO_ROOT / "apps/web/public/search-index.json").read_text(encoding="utf-8"))
    assert {"title", "date", "lang", "url", "summary", "tags", "topics", "authors", "content_excerpt"}.issubset(rows[0])
