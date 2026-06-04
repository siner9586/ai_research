from ai_research_brief.fetchers.arxiv import mock_papers
from ai_research_brief.pipeline.dedupe import dedupe_papers


def test_dedupe_arxiv_id_keeps_one_copy():
    papers = mock_papers()
    assert len(dedupe_papers(papers + papers)) == len(papers)
