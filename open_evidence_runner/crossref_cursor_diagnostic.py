from __future__ import annotations

import hashlib
import json
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


def run(label: str, extra: dict[str, str]) -> None:
    cursor = "*"
    seen = set()
    pages = []
    for page_number in range(1, 5):
        params = {**BASE, **extra, "cursor": cursor}
        response = requests.get(
            API,
            params=params,
            headers={"User-Agent": "ExplainabilityBiasOpenEvidence/1.0 diagnostic"},
            timeout=(30, 180),
        )
        response.raise_for_status()
        message = response.json()["message"]
        items = message.get("items") or []
        next_cursor = message.get("next-cursor")
        dois = [item.get("DOI") for item in items if item.get("DOI")]
        pages.append(
            {
                "page": page_number,
                "items": len(items),
                "cursor_in_hash": short(cursor),
                "cursor_out_hash": short(next_cursor),
                "cursor_repeated": next_cursor == cursor,
                "first_doi": dois[0] if dois else None,
                "last_doi": dois[-1] if dois else None,
                "item_fingerprint": hashlib.sha256("\n".join(dois).encode()).hexdigest()[:16],
                "fingerprint_seen_before": hashlib.sha256("\n".join(dois).encode()).hexdigest() in seen,
            }
        )
        fingerprint = hashlib.sha256("\n".join(dois).encode()).hexdigest()
        seen.add(fingerprint)
        if len(items) < 1000 or not next_cursor:
            break
        cursor = next_cursor
    print(json.dumps({"mode": label, "params": extra, "pages": pages}, indent=2))


def main() -> None:
    run("default", {})
    run("published_asc", {"sort": "published", "order": "asc"})
    run("indexed_asc", {"sort": "indexed", "order": "asc"})


if __name__ == "__main__":
    main()
