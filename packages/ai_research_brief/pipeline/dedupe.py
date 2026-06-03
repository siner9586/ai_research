from ..models import Paper


def dedupe_papers(papers: list[Paper]) -> list[Paper]:
    seen = {}
    for paper in papers:
        seen[paper.arxiv_id] = paper
    return list(seen.values())
