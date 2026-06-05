from datetime import datetime, timezone

from ai_research_brief.fetchers import arxiv
from ai_research_brief.models import Paper
from ai_research_brief.pipeline.dedupe import dedupe_papers


def _paper(arxiv_id: str, category: str) -> Paper:
    now = datetime.now(timezone.utc)
    return Paper(
        id=arxiv_id,
        arxiv_id=arxiv_id,
        title=f"Paper {arxiv_id}",
        abstract="A test paper.",
        authors=["Ada"],
        primary_category=category,
        categories=[category],
        published_at=now,
        updated_at=now,
        abs_url=f"https://arxiv.org/abs/{arxiv_id}",
        pdf_url=f"https://arxiv.org/pdf/{arxiv_id}",
    )


def test_arxiv_query_paginates_until_limit(monkeypatch):
    calls = []

    def fake_page(_query_text, start, max_results):
        calls.append((start, max_results))
        return [_paper(f"2606.{start + index:05d}", "cs.AI") for index in range(max_results)]

    monkeypatch.setattr(arxiv, "_fetch_arxiv_query_page", fake_page)
    rows, stats = arxiv._fetch_arxiv_query_with_stats("cat:cs.AI", max_results=250, page_size=100)

    assert len(rows) == 250
    assert calls == [(0, 100), (100, 100), (200, 50)]
    assert stats["pages"] == 3
    assert stats["starts"] == [0, 100, 200]


def test_dedupe_merges_categories_for_cross_listed_papers():
    rows = [_paper("2606.00001", "cs.AI"), _paper("2606.00001", "cs.LG")]

    [merged] = dedupe_papers(rows)

    assert merged.categories == ["cs.AI", "cs.LG"]
