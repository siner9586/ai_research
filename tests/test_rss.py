from datetime import date

from ai_research_brief.config import REPO_ROOT
from ai_research_brief.pipeline.run_daily import run_daily


def test_rss_contains_required_item_fields(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    run_daily(date(2026, 6, 3), mock=True)
    xml = (REPO_ROOT / "apps/web/public/zh/feed.xml").read_text(encoding="utf-8")
    assert "<item>" in xml
    assert "<guid>" in xml
    assert "<pubDate>" in xml
    assert "<description>" in xml
    assert "<language>zh</language>" in xml
    assert "<content>" in xml
