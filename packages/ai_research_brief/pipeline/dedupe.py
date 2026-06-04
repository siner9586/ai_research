from ..models import Paper


def dedupe_papers(papers: list[Paper]) -> list[Paper]:
    seen = {}
    for paper in papers:
        if paper.arxiv_id not in seen:
            seen[paper.arxiv_id] = paper
    return list(seen.values())
