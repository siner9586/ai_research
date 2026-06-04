from __future__ import annotations

from datetime import date
import re

import httpx


def fetch_daily_papers(day: date, timeout: float = 8.0) -> dict[str, dict]:
    """Return HF Daily Paper signals keyed by arXiv id.

    Hugging Face has changed paper endpoints over time, so this parser accepts a
    few common payload shapes and degrades to an empty mapping on failures.
    """
    url = f"https://huggingface.co/api/daily_papers?date={day.isoformat()}"
    try:
        response = httpx.get(url, timeout=timeout, headers={"User-Agent": "frontier-paper-radar/0.1"})
        response.raise_for_status()
        payload = response.json()
    except Exception:
        return {}

    rows = payload if isinstance(payload, list) else payload.get("papers", []) if isinstance(payload, dict) else []
    signals: dict[str, dict] = {}
    for row in rows:
        paper = row.get("paper", row) if isinstance(row, dict) else {}
        text = " ".join(str(paper.get(k, "")) for k in ("id", "title", "url", "paperId"))
        match = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", text)
        if not match:
            continue
        arxiv_id = match.group(1)
        signals[arxiv_id] = {
            "hf_daily": True,
            "hf_url": paper.get("url") or row.get("url"),
            "hf_upvotes": int(row.get("upvotes") or row.get("numLikes") or paper.get("upvotes") or 0),
        }
    return signals
