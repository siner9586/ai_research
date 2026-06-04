from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.pipeline.enrich import build_signals
from ai_research_brief.pipeline.score import DIMENSIONS, score_papers
from datetime import date


def test_score_outputs_all_required_dimensions(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "mock")
    papers = mock_papers()
    signals = build_signals(papers, date(2026, 6, 3), mock=True)
    scored = score_papers(papers, signals)
    assert scored[0].total_score >= scored[-1].total_score
    assert set(DIMENSIONS).issubset(scored[0].score_breakdown)
    assert scored[0].selected_reason
    assert scored[0].topic_slug
