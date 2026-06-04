from __future__ import annotations

from ..fetchers.arxiv import normalize_arxiv_id
from ..models import Paper
from ..utils.text import collapse_ws


def normalize_papers(papers: list[Paper]) -> list[Paper]:
    normalized: list[Paper] = []
    for paper in papers:
        normalized.append(
            paper.model_copy(
                update={
                    "id": normalize_arxiv_id(paper.arxiv_id),
                    "arxiv_id": normalize_arxiv_id(paper.arxiv_id),
                    "title": collapse_ws(paper.title),
                    "abstract": collapse_ws(paper.abstract),
                    "authors": [collapse_ws(author) for author in paper.authors if collapse_ws(author)],
                    "categories": list(dict.fromkeys(paper.categories)),
                }
            )
        )
    return normalized
