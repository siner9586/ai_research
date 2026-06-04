from __future__ import annotations

import os

import httpx


def fetch_citation_counts(arxiv_ids: list[str], timeout: float = 8.0) -> dict[str, int]:
    if not arxiv_ids:
        return {}

    headers = {"User-Agent": "frontier-paper-radar/0.1"}
    if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
        headers["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]

    counts: dict[str, int] = {}
    for arxiv_id in arxiv_ids:
        url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields=citationCount"
        try:
            response = httpx.get(url, timeout=timeout, headers=headers)
            response.raise_for_status()
            payload = response.json()
        except Exception:
            continue
        if isinstance(payload, dict) and isinstance(payload.get("citationCount"), int):
            counts[arxiv_id] = payload["citationCount"]
    return counts
