from datetime import date

from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.models import BriefPaper, DailyBrief, PaperSignal, QAReport


def test_required_models_validate():
    paper = mock_papers()[0]
    signal = PaperSignal(arxiv_id=paper.arxiv_id, fields_of_study=["Computer Science"], external_ids={"ArXiv": paper.arxiv_id})
    brief_paper = BriefPaper(
        arxiv_id=paper.arxiv_id,
        title=paper.title,
        short_title=paper.title,
        original_title=paper.title,
        authors=paper.authors,
        topic="Agents",
        topic_slug="agents",
        score=10,
        abs_url=paper.abs_url,
        pdf_url=paper.pdf_url,
        why_it_matters="Grounded reason",
        problem="Grounded problem",
        method="Grounded method",
        practitioner_takeaway="Grounded takeaway",
        limitations="Preprint limitation",
        bullets=["a", "b", "c"],
    )
    brief = DailyBrief(
        date=date(2026, 6, 3),
        lang="en",
        title="Daily AI Research Brief",
        slug="2026-06-03-demo",
        overview="overview",
        trend_observation="trend",
        featured_papers=[brief_paper],
        honorable_mentions=[],
        keywords=["agent"],
        sources_path="data/content/en/daily/demo-sources.md",
    )
    report = QAReport(date=date(2026, 6, 3), passed=True, warnings=[], errors=[], checked_files=[])
    assert signal.external_ids["ArXiv"] == paper.arxiv_id
    assert brief.featured_papers[0].arxiv_id == paper.arxiv_id
    assert report.passed is True
