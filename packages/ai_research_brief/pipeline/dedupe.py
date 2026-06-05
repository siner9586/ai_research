from ..models import Paper


def dedupe_papers(papers: list[Paper]) -> list[Paper]:
    seen: dict[str, Paper] = {}
    for paper in papers:
        if paper.arxiv_id not in seen:
            seen[paper.arxiv_id] = paper
            continue
        existing = seen[paper.arxiv_id]
        merged_categories = list(dict.fromkeys([*existing.categories, *paper.categories]))
        seen[paper.arxiv_id] = existing.model_copy(update={"categories": merged_categories})
    return list(seen.values())
