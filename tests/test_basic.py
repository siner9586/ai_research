from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.pipeline.dedupe import dedupe_papers
from ai_research_brief.pipeline.run_daily import run_daily
from ai_research_brief.utils.slug import slugify
from datetime import date


def test_slug():
    assert slugify('Self Evolving Agents') == 'self-evolving-agents'


def test_mock_papers():
    assert len(mock_papers()) >= 3


def test_dedupe():
    p = mock_papers()
    assert len(dedupe_papers(p + p)) == len(p)


def test_run_daily():
    r = run_daily(date(2026, 6, 3), mock=True)
    assert r['qa_passed'] is True
    assert r['featured'] >= 3
