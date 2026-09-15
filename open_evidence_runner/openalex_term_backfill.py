from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

API = "https://api.openalex.org/works"
PER_PAGE = 200
SELECT = (
    "id,doi,display_name,publication_year,publication_date,type,language,authorships,"
    "primary_location,best_oa_location,open_access,abstract_inverted_index,ids,is_retracted,"
    "cited_by_count,referenced_works,related_works,topics,keywords"
)
DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def dump_json_gz(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False)


def normalize_doi(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    return DOI_PREFIX.sub("", value).strip().lower()


def reconstruct_abstract(index: Any) -> str | None:
    if not isinstance(index, dict):
        return None
    words: list[tuple[int, str]] = []
    for word, positions in index.items():
        for position in positions or []:
            words.append((int(position), word))
    return " ".join(word for _, word in sorted(words)) or None


def normalize(item: dict[str, Any], year: int, query_group: str, query_text: str) -> dict[str, Any]:
    best = item.get("best_oa_location") or {}
    primary = item.get("primary_location") or {}
    open_access = item.get("open_access") or {}
    authors = []
    for authorship in item.get("authorships") or []:
        author = (authorship or {}).get("author") or {}
        if author.get("display_name"):
            authors.append(author["display_name"])
    openalex_id = (item.get("id") or "").rsplit("/", 1)[-1]
    return {
        "source_name": "OpenAlex",
        "source_external_id": openalex_id
        or hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest(),
        "openalex_id": openalex_id,
        "doi_normalized": normalize_doi(item.get("doi")),
        "canonical_title": " ".join((item.get("display_name") or "").split()),
        "abstract": reconstruct_abstract(item.get("abstract_inverted_index")),
        "publication_date": item.get("publication_date"),
        "publication_year": item.get("publication_year") or year,
        "work_type": item.get("type"),
        "language": item.get("language"),
        "venue": ((primary.get("source") or {}).get("display_name")),
        "publisher": ((primary.get("source") or {}).get("host_organization_name")),
        "authors": authors,
        "source_url": best.get("landing_page_url") or primary.get("landing_page_url"),
        "oa_pdf_url": best.get("pdf_url") or primary.get("pdf_url"),
        "is_oa": open_access.get("is_oa"),
        "oa_status": open_access.get("oa_status"),
        "license": best.get("license") or primary.get("license"),
        "is_retracted": item.get("is_retracted"),
        "citation_count": item.get("cited_by_count"),
        "referenced_works": item.get("referenced_works") or [],
        "related_works": item.get("related_works") or [],
        "topics": item.get("topics") or [],
        "keywords": item.get("keywords") or [],
        "query_groups": [query_group],
        "query_texts": [query_text],
    }


def request_page(session: requests.Session, params: dict[str, Any], deadline: float) -> tuple[dict[str, Any] | None, str | None, int]:
    attempts = 0
    while attempts < 8 and time.monotonic() < deadline:
        attempts += 1
        try:
            response = session.get(API, params=params, timeout=(30, 120))
        except requests.RequestException as exc:
            error = f"network:{type(exc).__name__}:{exc}"
        else:
            if response.status_code == 200:
                try:
                    return response.json(), None, attempts
                except ValueError as exc:
                    return None, f"invalid_json:{exc}", attempts
            error = f"http_{response.status_code}:{response.text[:500]}"
            if response.status_code not in {429, 500, 502, 503, 504}:
                return None, error, attempts
            retry_after = response.headers.get("Retry-After")
            try:
                retry_seconds = float(retry_after) if retry_after else 0.0
            except ValueError:
                retry_seconds = 0.0
        delay = min(60.0, max(retry_seconds if 'retry_seconds' in locals() else 0.0, 2 ** min(attempts, 5)))
        time.sleep(delay + random.random())
    return None, error if 'error' in locals() else "deadline_reached", attempts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--term-key", required=True)
    parser.add_argument("--terms", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--hours", type=float, default=4.5)
    args = parser.parse_args()

    terms = json.loads(args.terms.read_text(encoding="utf-8"))
    if args.term_key not in terms:
        raise SystemExit(f"Unknown term key: {args.term_key}")
    spec = terms[args.term_key]
    query_group = spec["query_group"]
    query_text = spec["query_text"]
    term_index = int(spec["term_index"])
    root = args.output
    root.mkdir(parents=True, exist_ok=True)
    checkpoint = root / "checkpoints" / str(args.year) / query_group / f"{term_index:02d}.json"
    old = json.loads(checkpoint.read_text(encoding="utf-8")) if checkpoint.exists() else {}
    cursor = old.get("cursor", "*")
    pages = int(old.get("pages", 0))
    records = int(old.get("records", 0))
    output = root / "normalized" / "openalex" / str(args.year) / query_group / f"{term_index:02d}.jsonl.gz"
    deadline = time.monotonic() + args.hours * 3600
    started_at = utcnow()
    completed = bool(old.get("completed"))
    error = None
    request_attempts = 0
    session = requests.Session()
    session.headers.update({
        "User-Agent": "ExplainabilityBiasOpenEvidence/2.0 (systematic-review; mailto:open-evidence@example.invalid)",
        "Accept": "application/json",
    })

    while not completed and time.monotonic() < deadline:
        end_date = "2026-07-24" if args.year == 2026 else f"{args.year}-12-31"
        params: dict[str, Any] = {
            "search": query_text,
            "filter": f"from_publication_date:{args.year}-01-01,to_publication_date:{end_date}",
            "per_page": PER_PAGE,
            "cursor": cursor,
            "select": SELECT,
        }
        if os.getenv("OPENALEX_API_KEY"):
            params["api_key"] = os.environ["OPENALEX_API_KEY"]
        payload, request_error, attempts = request_page(session, params, deadline)
        request_attempts += attempts
        if request_error or payload is None:
            error = request_error
            break
        items = payload.get("results") or []
        pages += 1
        dump_json_gz(
            root / "raw" / "openalex" / str(args.year) / query_group / f"{term_index:02d}" / f"page_{pages:06d}.json.gz",
            payload,
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(output, "at", encoding="utf-8") as handle:
            for item in items:
                handle.write(json.dumps(normalize(item, args.year, query_group, query_text), ensure_ascii=False) + "\n")
        records += len(items)
        next_cursor = (payload.get("meta") or {}).get("next_cursor")
        completed = not items or not next_cursor
        save_json(checkpoint, {
            "term_key": args.term_key,
            "cursor": next_cursor or ("END_NO_NEXT_CURSOR" if completed else cursor),
            "pages": pages,
            "records": records,
            "completed": completed,
            "updated_at": utcnow(),
        })
        if completed:
            cursor = "END_NO_NEXT_CURSOR"
            break
        if next_cursor == cursor:
            error = "repeated_next_cursor"
            break
        cursor = next_cursor
        time.sleep(0.25 + random.random() * 0.25)

    if not completed and not error:
        error = "workflow_deadline_reached"
    summary = {
        "run_id": f"openalex-term-{args.year}-{args.term_key}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "OpenAlex",
        "year": args.year,
        "term_key": args.term_key,
        "query_group": query_group,
        "term_index": term_index,
        "query_text": query_text,
        "pages_completed": pages,
        "raw_records": records,
        "cursor_end": cursor,
        "request_attempts": request_attempts,
        "completed": completed,
        "error": error,
        "started_at": started_at,
        "finished_at": utcnow(),
        "official_endpoint": API,
        "official_end_evidence": "empty results or absent next_cursor" if completed else None,
        "normalized_file": str(output.relative_to(root)),
    }
    save_json(root / "completion" / f"openalex_{args.year}_{args.term_key}.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
