from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from semantic_scholar_backfill import (
    API,
    FIELDS,
    LIMIT,
    dump_json_gz,
    make_session,
    normalize_doi,
    save_json,
    utcnow,
)

TITLE_NONALNUM = re.compile(r"[^a-z0-9]+")
ARXIV_PREFIX = re.compile(r"^(?:arxiv:\s*|https?://arxiv\.org/(?:abs|pdf)/)", re.I)
ARXIV_VERSION = re.compile(r"v\d+$", re.I)


def normalize_title(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return TITLE_NONALNUM.sub("", value.casefold())


def normalize_arxiv(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = ARXIV_PREFIX.sub("", value.strip()).removesuffix(".pdf")
    return ARXIV_VERSION.sub("", text).lower() or None


def load_queries(path: Path) -> dict[str, str]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not value:
        raise ValueError("seed-rescue query file must be a non-empty JSON object")
    return {str(key): str(query) for key, query in value.items()}


def load_seeds(path: Path, year: int) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]
    return [row for row in rows if str(row.get("year") or "") == str(year)]


def normalize_paper(
    item: dict[str, Any], year: int, query_group: str, query_text: str
) -> dict[str, Any]:
    external = item.get("externalIds") or {}
    oa = item.get("openAccessPdf") or {}
    authors = [a.get("name") for a in item.get("authors") or [] if a.get("name")]
    journal = item.get("journal") or {}
    source_external_id = (
        item.get("paperId")
        or str(item.get("corpusId") or "")
        or hashlib.sha256(json.dumps(item, sort_keys=True).encode()).hexdigest()
    )
    return {
        "source_name": "Semantic Scholar",
        "discovery_layer": "gold_standard_recall_rescue",
        "source_external_id": source_external_id,
        "s2_paper_id": item.get("paperId"),
        "corpus_id": item.get("corpusId"),
        "doi_normalized": normalize_doi(external.get("DOI")),
        "arxiv_id": normalize_arxiv(external.get("ArXiv")),
        "pmid": external.get("PubMed"),
        "mag_id": external.get("MAG"),
        "openalex_id": None,
        "canonical_title": " ".join((item.get("title") or "").split()),
        "abstract": item.get("abstract"),
        "publication_date": item.get("publicationDate"),
        "publication_year": item.get("year") or year,
        "work_type": item.get("publicationTypes") or [],
        "language": None,
        "venue": item.get("venue") or journal.get("name"),
        "publisher": None,
        "authors": authors,
        "url": item.get("url"),
        "is_oa": item.get("isOpenAccess"),
        "oa_pdf_url": oa.get("url"),
        "oa_status": item.get("isOpenAccess"),
        "license": oa.get("status"),
        "citation_count": item.get("citationCount"),
        "reference_count": item.get("referenceCount"),
        "fields_of_study": item.get("fieldsOfStudy") or [],
        "s2_fields_of_study": item.get("s2FieldsOfStudy") or [],
        "external_ids": external,
        "query_groups": [query_group],
        "query_texts": [query_text],
    }


def crawl_query(
    session: Any,
    root: Path,
    year: int,
    query_group: str,
    query_text: str,
    deadline: float,
) -> dict[str, Any]:
    checkpoint = root / "checkpoints" / str(year) / f"{query_group}.json"
    prior = json.loads(checkpoint.read_text(encoding="utf-8")) if checkpoint.exists() else {}
    if prior.get("completed") and prior.get("result"):
        return prior["result"]

    token = prior.get("token")
    pages = int(prior.get("pages", 0))
    records = int(prior.get("records", 0))
    started = utcnow()
    completed = False
    error = None
    output = root / "normalized" / "semantic_scholar_rescue" / str(year) / f"{query_group}.jsonl.gz"

    while time.monotonic() < deadline:
        params: dict[str, Any] = {
            "query": query_text,
            "year": str(year),
            "fields": FIELDS,
            "limit": LIMIT,
        }
        if token:
            params["token"] = token
        response = session.get(API, params=params, timeout=(30, 180))
        if response.status_code != 200:
            error = f"http_{response.status_code}:{response.text[:500]}"
            break
        try:
            payload = response.json()
        except ValueError as exc:
            error = f"invalid_json:{exc}"
            break

        data = payload.get("data") or []
        pages += 1
        dump_json_gz(
            root
            / "raw"
            / "semantic_scholar_rescue"
            / str(year)
            / query_group
            / f"page_{pages:06d}.json.gz",
            payload,
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(output, "at", encoding="utf-8") as handle:
            for item in data:
                handle.write(
                    json.dumps(
                        normalize_paper(item, year, query_group, query_text),
                        ensure_ascii=False,
                    )
                    + "\n"
                )
        records += len(data)
        next_token = payload.get("token")
        completed = not next_token or not data
        save_json(
            checkpoint,
            {
                "token": next_token,
                "pages": pages,
                "records": records,
                "completed": completed,
                "updated_at": utcnow(),
            },
        )
        if completed:
            token = next_token or "END_NO_TOKEN"
            break
        if next_token == token:
            error = "repeated_token"
            break
        token = next_token
        time.sleep(1.2 + random.random() * 0.5)

    if not completed and not error:
        error = "workflow_deadline_reached"
    result = {
        "query_group": query_group,
        "query_text": query_text,
        "pages_completed": pages,
        "records_found": records,
        "cursor_end": token,
        "completed": completed,
        "started_at": started,
        "finished_at": utcnow(),
        "error": error,
    }
    save_json(
        checkpoint,
        {
            "token": token,
            "pages": pages,
            "records": records,
            "completed": completed,
            "result": result,
            "updated_at": utcnow(),
        },
    )
    return result


def merge_year(root: Path, year: int) -> tuple[list[dict[str, Any]], Path]:
    records: dict[str, dict[str, Any]] = {}
    folder = root / "normalized" / "semantic_scholar_rescue" / str(year)
    for path in sorted(folder.glob("R*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = (
                    item.get("doi_normalized")
                    or item.get("arxiv_id")
                    or item.get("s2_paper_id")
                    or item["source_external_id"]
                )
                if key in records:
                    records[key]["query_groups"] = sorted(
                        set(records[key]["query_groups"]) | set(item["query_groups"])
                    )
                    records[key]["query_texts"] = sorted(
                        set(records[key]["query_texts"]) | set(item["query_texts"])
                    )
                    for field in ("abstract", "oa_pdf_url", "venue", "authors"):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    output = folder / "paper_master_semantic_scholar_rescue.jsonl.gz"
    output.parent.mkdir(parents=True, exist_ok=True)
    ordered = [records[key] for key in sorted(records)]
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        for item in ordered:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    return ordered, output


def validate_seeds(
    records: list[dict[str, Any]], seeds: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    doi_index = {item.get("doi_normalized") for item in records if item.get("doi_normalized")}
    arxiv_index = {item.get("arxiv_id") for item in records if item.get("arxiv_id")}
    title_index = {
        normalize_title(item.get("canonical_title")): item for item in records if item.get("canonical_title")
    }
    rows: list[dict[str, Any]] = []
    for seed in seeds:
        doi = normalize_doi(seed.get("doi"))
        arxiv_id = normalize_arxiv(seed.get("arxiv_id"))
        title_key = normalize_title(seed.get("title"))
        method = None
        if doi and doi in doi_index:
            method = "doi"
        elif arxiv_id and arxiv_id in arxiv_index:
            method = "arxiv_id"
        elif title_key and title_key in title_index:
            method = "normalized_title"
        rows.append(
            {
                "seed_id": seed.get("seed_id"),
                "title": seed.get("title"),
                "year": seed.get("year"),
                "recovered": bool(method),
                "match_method": method,
                "layers": seed.get("layers"),
            }
        )
    return rows


def write_seed_validation(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["seed_id", "title", "year", "recovered", "match_method", "layers"]
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--queries", type=Path, required=True)
    parser.add_argument("--seeds", type=Path, required=True)
    parser.add_argument("--hours", type=float, default=5.5)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    queries = load_queries(args.queries)
    seeds = load_seeds(args.seeds, args.year)
    started = utcnow()
    deadline = time.monotonic() + args.hours * 3600
    session = make_session()
    results = []
    for query_group, query_text in queries.items():
        result = crawl_query(
            session, args.output, args.year, query_group, query_text, deadline
        )
        results.append(result)
        if result["error"] == "workflow_deadline_reached":
            break

    records, master = merge_year(args.output, args.year)
    validation = validate_seeds(records, seeds)
    validation_path = args.output / "audits" / f"seed_rescue_validation_{args.year}.csv"
    write_seed_validation(validation_path, validation)

    manifest = args.output / "manifests" / f"semantic_scholar_rescue_{args.year}_queries.csv"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = list(results[0]) if results else ["query_group"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    recovered = sum(bool(row["recovered"]) for row in validation)
    completed = len(results) == len(queries) and all(item["completed"] for item in results)
    summary = {
        "run_id": f"semantic-scholar-rescue-{args.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "Semantic Scholar",
        "discovery_layer": "gold_standard_recall_rescue",
        "year": args.year,
        "query_groups_expected": len(queries),
        "query_groups_attempted": len(results),
        "query_groups_completed": sum(bool(item["completed"]) for item in results),
        "pages_completed": sum(int(item["pages_completed"]) for item in results),
        "raw_records": sum(int(item["records_found"]) for item in results),
        "unique_records": len(records),
        "completed": completed,
        "started_at": started,
        "finished_at": utcnow(),
        "errors": [item for item in results if item["error"]],
        "master_path": str(master.relative_to(args.output)),
        "seed_validation_path": str(validation_path.relative_to(args.output)),
        "missed_seeds_expected": len(seeds),
        "missed_seeds_recovered": recovered,
        "rescue_recall": (recovered / len(seeds)) if seeds else None,
        "seed_titles_used_for_retrieval": false if False else False,
        "integrity_note": "Exact seed titles are used only for validation after topic-query retrieval.",
    }
    save_json(args.output / "completion" / f"semantic_scholar_rescue_{args.year}.json", summary)
    if not completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
