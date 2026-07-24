from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import requests

API = "https://api.crossref.org/works"
BASE = {
    "query.bibliographic": '"explanation fidelity"',
    "filter": "from-pub-date:2018-01-01,until-pub-date:2018-12-31",
    "rows": 1000,
}


def short(value: str | None) -> str | None:
    if not value:
        return None
    return hashlib.sha256(value.encode()).hexdigest()[:16]


def run(label: str, extra: dict[str, str]) -> dict:
    cursor = "*"
    seen = set()
    pages = []
    error = None
    for page_number in range(1, 5):
        try:
            params = {**BASE, **extra, "cursor": cursor}
            response = requests.get(
                API,
                params=params,
                headers={"User-Agent": "ExplainabilityBiasOpenEvidence/1.0 diagnostic"},
                timeout=(30, 180),
            )
            if response.status_code != 200:
                error = {
                    "page": page_number,
                    "status_code": response.status_code,
                    "response_excerpt": response.text[:500],
                }
                break
            message = response.json()["message"]
            items = message.get("items") or []
            next_cursor = message.get("next-cursor")
            dois = [item.get("DOI") for item in items if item.get("DOI")]
            fingerprint = hashlib.sha256("\n".join(dois).encode()).hexdigest()
            pages.append(
                {
                    "page": page_number,
                    "items": len(items),
                    "cursor_in_hash": short(cursor),
                    "cursor_out_hash": short(next_cursor),
                    "cursor_repeated": next_cursor == cursor,
                    "first_doi": dois[0] if dois else None,
                    "last_doi": dois[-1] if dois else None,
                    "item_fingerprint": fingerprint[:16],
                    "fingerprint_seen_before": fingerprint in seen,
                }
            )
            seen.add(fingerprint)
            if len(items) < 1000 or not next_cursor:
                break
            cursor = next_cursor
            time.sleep(1.0)
        except Exception as exc:
            error = {"page": page_number, "exception": type(exc).__name__, "message": str(exc)[:500]}
            break
    return {"mode": label, "params": extra, "pages": pages, "error": error}


def main() -> None:
    results = [
        run("default", {}),
        run("published_asc", {"sort": "published", "order": "asc"}),
        run("indexed_asc", {"sort": "indexed", "order": "asc"}),
    ]
    Path("crossref_cursor_diagnostic.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
