from datetime import date
import json

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.pipeline.qa import run_qa
from ai_research_brief.pipeline.run_daily import run_daily


def test_qa_report_passes_mock_content(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    run_daily(date(2026, 6, 3), mock=True)
    report = run_qa(date(2026, 6, 3), REPO_ROOT / "data/content", REPO_ROOT / "data/reports/qa")
    assert report.passed is True
    assert report.errors == []
    payload = json.loads((REPO_ROOT / "data/reports/qa/2026-06-03.json").read_text(encoding="utf-8"))
    assert payload["passed"] is True
