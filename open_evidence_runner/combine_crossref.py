from __future__ import annotations

import argparse
import csv
import gzip
import json
import tarfile
from pathlib import Path
from typing import Any


def merge_record(existing: dict[str, Any], row: dict[str, Any]) -> None:
    for field in ("query_groups", "query_texts"):
        existing[field] = sorted(set(existing.get(field, [])) | set(row.get(field, [])))
    for field in ("abstract", "licenses", "links", "venue", "publisher", "authors", "publication_date"):
        if not existing.get(field) and row.get(field):
            existing[field] = row[field]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    summaries = []
    for path in sorted(args.input.glob("**/completion/crossref_*_summary.json")):
        summaries.append(json.loads(path.read_text(encoding="utf-8")))

    records: dict[str, dict[str, Any]] = {}
    for path in sorted(args.input.glob("**/normalized/crossref/*/paper_master_crossref.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                row = json.loads(line)
                key = row.get("doi_normalized") or row.get("source_external_id")
                if key in records:
                    merge_record(records[key], row)
                else:
                    records[key] = row

    master_jsonl = args.output / "crossref_all_paper_master.jsonl.gz"
    with gzip.open(master_jsonl, "wt", encoding="utf-8") as f:
        for key in sorted(records):
            f.write(json.dumps(records[key], ensure_ascii=False) + "\n")

    master_csv = args.output / "crossref_all_paper_master.csv.gz"
    fields = [
        "source_name", "source_external_id", "doi_normalized", "canonical_title", "publication_date",
        "publication_year", "work_type", "language", "venue", "publisher", "authors", "url",
        "reference_count", "is_referenced_by_count", "query_groups", "query_texts",
    ]
    with gzip.open(master_csv, "wt", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for key in sorted(records):
            row = records[key]
            writer.writerow({field: json.dumps(row.get(field), ensure_ascii=False) if isinstance(row.get(field), (list, dict)) else row.get(field) for field in fields})

    combined_manifest = args.output / "crossref_all_search_queries.csv"
    manifest_paths = sorted(args.input.glob("**/manifests/crossref_*_search_queries.csv"))
    wrote_header = False
    with combined_manifest.open("w", encoding="utf-8-sig", newline="") as out:
        writer = None
        for path in manifest_paths:
            with path.open("r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                if writer is None:
                    writer = csv.DictWriter(out, fieldnames=["year"] + (reader.fieldnames or []))
                    writer.writeheader()
                    wrote_header = True
                year = path.stem.split("_")[1]
                for row in reader:
                    writer.writerow({"year": year, **row})
    if not wrote_header:
        combined_manifest.write_text("year,query_group\n", encoding="utf-8")

    expected_years = list(range(2018, 2027))
    years_present = sorted({int(s["year"]) for s in summaries})
    all_complete = years_present == expected_years and all(bool(s.get("completed")) for s in summaries)
    total = {
        "source": "Crossref",
        "years_expected": expected_years,
        "years_present": years_present,
        "year_runs_completed": sum(bool(s.get("completed")) for s in summaries),
        "year_runs_total": len(summaries),
        "subqueries_expected": sum(int(s.get("subqueries_expected", 0)) for s in summaries),
        "subqueries_completed": sum(int(s.get("subqueries_completed", 0)) for s in summaries),
        "pages_completed": sum(int(s.get("pages_completed", 0)) for s in summaries),
        "raw_records": sum(int(s.get("raw_records", 0)) for s in summaries),
        "unique_records": len(records),
        "completed": all_complete,
        "errors": [e for s in summaries for e in s.get("errors", [])],
    }
    (args.output / "crossref_all_summary.json").write_text(json.dumps(total, ensure_ascii=False, indent=2), encoding="utf-8")

    archive = args.output / "crossref_backfill_all.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        for path in sorted(args.input.rglob("*")):
            if path.is_file():
                tar.add(path, arcname=path.relative_to(args.input))
        for path in (master_jsonl, master_csv, combined_manifest, args.output / "crossref_all_summary.json"):
            tar.add(path, arcname=f"aggregate/{path.name}")
    print(json.dumps(total, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
