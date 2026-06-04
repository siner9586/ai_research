from __future__ import annotations

import os

import httpx


def fetch_paper_signals(arxiv_ids: list[str], timeout: float = 8.0) -> dict[str, dict]:
    if not arxiv_ids:
        return {}
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    if not api_key:
        return {}

    headers = {"User-Agent": "ai-research-brief/0.1", "x-api-key": api_key}

    signals: dict[str, dict] = {}
    for arxiv_id in arxiv_ids:
        fields = "paperId,citationCount,influentialCitationCount,fieldsOfStudy,externalIds"
        url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}?fields={fields}"
        try:
            response = httpx.get(url, timeout=timeout, headers=headers)
            response.raise_for_status()
            payload = response.json()
        except Exception:
            continue
        if isinstance(payload, dict):
            signals[arxiv_id] = {
                "semantic_scholar_id": payload.get("paperId"),
                "citation_count": int(payload.get("citationCount") or 0),
                "influential_citation_count": int(payload.get("influentialCitationCount") or 0),
                "fields_of_study": payload.get("fieldsOfStudy") or [],
                "external_ids": payload.get("externalIds") or {},
            }
    return signals


def fetch_citation_counts(arxiv_ids: list[str], timeout: float = 8.0) -> dict[str, int]:
    return {key: int(value.get("citation_count") or 0) for key, value in fetch_paper_signals(arxiv_ids, timeout).items()}
