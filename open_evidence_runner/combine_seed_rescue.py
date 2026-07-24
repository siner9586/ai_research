from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


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


def merge_records(input_root: Path, output_path: Path) -> int:
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
                    for field in ("abstract", "oa_pdf_url", "venue", "authors"):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output_path, "wt", encoding="utf-8") as handle:
        for key in sorted(records):
            handle.write(json.dumps(records[key], ensure_ascii=False) + "\n")
    return len(records)


def merge_validation(input_root: Path, output_path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(input_root.rglob("seed_rescue_validation_*.csv")):
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows.extend(dict(row) for row in csv.DictReader(handle))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["seed_id", "title", "year", "recovered", "match_method", "layers"]
    with output_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("seed_id") or ""))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    annual_summaries = [
        load_json(path)
        for path in sorted(args.input.rglob("semantic_scholar_rescue_*.json"))
    ]
    master_path = args.output / "semantic_scholar_seed_rescue_master.jsonl.gz"
    unique_records = merge_records(args.input, master_path)
    validation_path = args.output / "gold_seed_rescue_validation.csv"
    validation = merge_validation(args.input, validation_path)
    expected = len(validation)
    recovered = sum(
        str(row.get("recovered") or "").strip().lower() == "true" for row in validation
    )
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
        "completed": all_years_completed,
        "errors": errors,
        "master_file": master_path.name,
        "master_sha256": sha256_file(master_path),
        "validation_file": validation_path.name,
        "validation_sha256": sha256_file(validation_path),
        "integrity_note": "Seed titles were used only for post-retrieval validation; retrieval used generalizable topic queries. MAG identifiers are preserved as mag_id and are not mapped to OpenAlex IDs.",
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
