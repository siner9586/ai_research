from datetime import date
import json

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.pipeline.qa import run_qa
from ai_research_brief.pipeline.run_daily import run_daily


def test_qa_report_passes_mock_content(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    result = run_daily(date(2026, 6, 3), mock=True)
    report = run_qa(
        date.fromisoformat(result["actual_date"]),
        REPO_ROOT / "data/content",
        REPO_ROOT / "data/reports/qa",
        target_date=date.fromisoformat(result["target_date"]),
        publish_date=date.fromisoformat(result["publish_date"]),
    )
    assert report.passed is True
    assert report.errors == []
    payload = json.loads((REPO_ROOT / "data" / "reports" / "qa" / f"{result['publish_date']}.json").read_text(encoding="utf-8"))
    assert payload["passed"] is True
