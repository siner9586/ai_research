from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DOI_PREFIX = re.compile(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", re.I)
ARXIV_PREFIX = re.compile(r"^(?:arxiv:\s*|https?://arxiv\.org/(?:abs|pdf)/)", re.I)
ARXIV_VERSION = re.compile(r"v\d+$", re.I)
TITLE_NONALNUM = re.compile(r"[^a-z0-9]+")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def normalize_doi(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    return DOI_PREFIX.sub("", value).strip().lower() or None


def normalize_arxiv(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = ARXIV_PREFIX.sub("", value.strip()).removesuffix(".pdf")
    return ARXIV_VERSION.sub("", text).lower() or None


def normalize_title(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return TITLE_NONALNUM.sub("", value.casefold())


def merge_records(input_root: Path, output_path: Path) -> tuple[int, list[dict[str, Any]]]:
    records: dict[str, dict[str, Any]] = {}
    paths = sorted(input_root.rglob("paper_master_semantic_scholar_rescue.jsonl.gz"))
    for path in paths:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = (
                    item.get("doi_normalized")
                    or item.get("arxiv_id")
                    or item.get("s2_paper_id")
                    or item.get("source_external_id")
                )
                if not key:
                    key = hashlib.sha256(
                        json.dumps(item, sort_keys=True).encode("utf-8")
                    ).hexdigest()
                if key in records:
                    records[key]["query_groups"] = sorted(
                        set(records[key].get("query_groups") or [])
                        | set(item.get("query_groups") or [])
                    )
                    records[key]["query_texts"] = sorted(
                        set(records[key].get("query_texts") or [])
                        | set(item.get("query_texts") or [])
                    )
                    for field in (
                        "abstract",
                        "oa_pdf_url",
                        "venue",
                        "authors",
                        "doi_normalized",
                        "arxiv_id",
                    ):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    ordered = [records[key] for key in sorted(records)]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output_path, "wt", encoding="utf-8") as handle:
        for item in ordered:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
    return len(ordered), ordered


def load_seeds(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def validate_across_years(
    records: list[dict[str, Any]], seeds: list[dict[str, str]]
) -> list[dict[str, Any]]:
    doi_index: dict[str, dict[str, Any]] = {}
    arxiv_index: dict[str, dict[str, Any]] = {}
    title_index: dict[str, dict[str, Any]] = {}
    for record in records:
        doi = normalize_doi(record.get("doi_normalized"))
        arxiv = normalize_arxiv(record.get("arxiv_id"))
        title = normalize_title(record.get("canonical_title"))
        if doi:
            doi_index[doi] = record
        if arxiv:
            arxiv_index[arxiv] = record
        if title:
            title_index[title] = record

    rows: list[dict[str, Any]] = []
    for seed in seeds:
        doi = normalize_doi(seed.get("doi"))
        arxiv = normalize_arxiv(seed.get("arxiv_id"))
        title = normalize_title(seed.get("title"))
        match: dict[str, Any] | None = None
        method: str | None = None
        if doi and doi in doi_index:
            match = doi_index[doi]
            method = "doi"
        elif arxiv and arxiv in arxiv_index:
            match = arxiv_index[arxiv]
            method = "arxiv_id"
        elif title and title in title_index:
            match = title_index[title]
            method = "normalized_title"

        declared_year_text = str(seed.get("year") or "").strip()
        declared_year = int(declared_year_text) if declared_year_text.isdigit() else None
        matched_year_raw = match.get("publication_year") if match else None
        matched_year = int(matched_year_raw) if str(matched_year_raw or "").isdigit() else None
        rows.append(
            {
                "seed_id": seed.get("seed_id"),
                "title": seed.get("title"),
                "declared_year": declared_year,
                "matched_publication_year": matched_year,
                "year_delta": (
                    matched_year - declared_year
                    if matched_year is not None and declared_year is not None
                    else None
                ),
                "version_year_mismatch": (
                    matched_year is not None
                    and declared_year is not None
                    and matched_year != declared_year
                ),
                "recovered": match is not None,
                "match_method": method,
                "matched_s2_paper_id": match.get("s2_paper_id") if match else None,
                "matched_doi": match.get("doi_normalized") if match else None,
                "matched_arxiv_id": match.get("arxiv_id") if match else None,
                "matched_query_groups": "|".join(match.get("query_groups") or []) if match else "",
                "layers": seed.get("layers"),
            }
        )
    return rows


def write_validation(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "seed_id",
        "title",
        "declared_year",
        "matched_publication_year",
        "year_delta",
        "version_year_mismatch",
        "recovered",
        "match_method",
        "matched_s2_paper_id",
        "matched_doi",
        "matched_arxiv_id",
        "matched_query_groups",
        "layers",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seeds", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    annual_summaries = [
        load_json(path)
        for path in sorted(args.input.rglob("semantic_scholar_rescue_*.json"))
    ]
    master_path = args.output / "semantic_scholar_seed_rescue_master.jsonl.gz"
    unique_records, records = merge_records(args.input, master_path)
    seeds = load_seeds(args.seeds)
    validation = validate_across_years(records, seeds)
    validation_path = args.output / "gold_seed_rescue_validation_cross_year.csv"
    write_validation(validation_path, validation)
    expected = len(validation)
    recovered = sum(bool(row["recovered"]) for row in validation)
    version_year_mismatches = sum(bool(row["version_year_mismatch"]) for row in validation)

    all_years_completed = (
        len(annual_summaries) == 9
        and all(summary.get("completed") is True for summary in annual_summaries)
    )
    errors = [
        {"year": summary.get("year"), "errors": summary.get("errors")}
        for summary in annual_summaries
        if summary.get("errors")
    ]
    summary = {
        "run_id": f"semantic-scholar-seed-rescue-all-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "Semantic Scholar",
        "discovery_layer": "gold_standard_recall_rescue",
        "years_expected": 9,
        "years_received": len(annual_summaries),
        "years_completed": sum(summary.get("completed") is True for summary in annual_summaries),
        "query_groups_completed": sum(
            int(summary.get("query_groups_completed") or 0) for summary in annual_summaries
        ),
        "pages_completed": sum(
            int(summary.get("pages_completed") or 0) for summary in annual_summaries
        ),
        "raw_records": sum(int(summary.get("raw_records") or 0) for summary in annual_summaries),
        "unique_records": unique_records,
        "missed_gold_seeds_expected": expected,
        "missed_gold_seeds_recovered": recovered,
        "rescue_recall": (recovered / expected) if expected else None,
        "version_year_mismatches_resolved": version_year_mismatches,
        "completed": all_years_completed,
        "recall_target_passed": recovered == expected,
        "errors": errors,
        "master_file": master_path.name,
        "master_sha256": sha256_file(master_path),
        "validation_file": validation_path.name,
        "validation_sha256": sha256_file(validation_path),
        "integrity_note": "Exact seed titles were used only for post-retrieval validation; retrieval used generalizable topic queries. Cross-year DOI/arXiv/title matching prevents preprint-versus-conference publication-year differences from being misclassified as retrieval failures. MAG identifiers are preserved as mag_id and are not mapped to OpenAlex IDs.",
    }
    summary_path = args.output / "semantic_scholar_seed_rescue_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest_path = args.output / "sha256sums.txt"
    manifest_path.write_text(
        f"{sha256_file(master_path)}  {master_path.name}\n"
        f"{sha256_file(validation_path)}  {validation_path.name}\n"
        f"{sha256_file(summary_path)}  {summary_path.name}\n",
        encoding="utf-8",
    )
    if not all_years_completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
