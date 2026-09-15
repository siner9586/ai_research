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
        raise ValueError(path)
    return value


def merge_year(input_root: Path, output_root: Path, year: int) -> tuple[int, Path]:
    records: dict[str, dict[str, Any]] = {}
    paths = sorted(input_root.rglob(f"normalized/openalex/{year}/**/*.jsonl.gz"))
    for path in paths:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = item.get("doi_normalized") or item.get("openalex_id") or item["source_external_id"]
                if key in records:
                    current = records[key]
                    current["query_groups"] = sorted(set(current.get("query_groups") or []) | set(item.get("query_groups") or []))
                    current["query_texts"] = sorted(set(current.get("query_texts") or []) | set(item.get("query_texts") or []))
                    if len(item.get("abstract") or "") > len(current.get("abstract") or ""):
                        current["abstract"] = item.get("abstract")
                    if not current.get("oa_pdf_url") and item.get("oa_pdf_url"):
                        current["oa_pdf_url"] = item["oa_pdf_url"]
                else:
                    records[key] = item
    output = output_root / "normalized" / "openalex" / str(year) / "paper_master_openalex.jsonl.gz"
    output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        for key in sorted(records):
            handle.write(json.dumps(records[key], ensure_ascii=False) + "\n")
    return len(records), output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--terms", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    terms = json.loads(args.terms.read_text(encoding="utf-8"))
    expected = 9 * len(terms)
    summary_paths = sorted(args.input.rglob("completion/openalex_*.json"))
    summaries = [load_json(path) for path in summary_paths]
    keys = {(int(item["year"]), item["term_key"]) for item in summaries}
    duplicates = len(summaries) - len(keys)
    missing = [
        {"year": year, "term_key": term_key}
        for year in range(2018, 2027)
        for term_key in terms
        if (year, term_key) not in keys
    ]
    errors = [item for item in summaries if not item.get("completed") or item.get("error")]

    year_rows = []
    master_paths = []
    for year in range(2018, 2027):
        unique_records, master = merge_year(args.input, args.output, year)
        master_paths.append(master)
        year_items = [item for item in summaries if int(item["year"]) == year]
        year_rows.append({
            "year": year,
            "terms_expected": len(terms),
            "terms_received": len(year_items),
            "terms_completed": sum(item.get("completed") is True for item in year_items),
            "pages_completed": sum(int(item.get("pages_completed") or 0) for item in year_items),
            "raw_records": sum(int(item.get("raw_records") or 0) for item in year_items),
            "unique_records": unique_records,
            "errors": sum(bool(item.get("error")) for item in year_items),
            "master_file": str(master.relative_to(args.output)),
            "master_sha256": sha256_file(master),
        })

    manifest = args.output / "openalex_term_manifest.csv"
    with manifest.open("w", newline="", encoding="utf-8-sig") as handle:
        fields = ["year", "term_key", "query_group", "term_index", "query_text", "pages_completed", "raw_records", "cursor_end", "request_attempts", "completed", "error", "started_at", "finished_at"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in sorted(summaries, key=lambda x: (int(x["year"]), x["term_key"])):
            writer.writerow({field: item.get(field) for field in fields})

    completed = len(summaries) == expected and not duplicates and not missing and not errors
    aggregate = {
        "run_id": f"openalex-term-all-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "OpenAlex",
        "execution_design": "year_by_individual_topic_term",
        "years_expected": 9,
        "terms_per_year": len(terms),
        "subqueries_expected": expected,
        "subqueries_received": len(summaries),
        "subqueries_completed": sum(item.get("completed") is True for item in summaries),
        "pages_completed": sum(int(item.get("pages_completed") or 0) for item in summaries),
        "raw_records": sum(int(item.get("raw_records") or 0) for item in summaries),
        "annual_unique_records_sum": sum(row["unique_records"] for row in year_rows),
        "duplicates_in_summaries": duplicates,
        "missing_subqueries": missing,
        "errors": errors,
        "completed": completed,
        "official_end_requirement": "Every term must end with empty results or absent next_cursor.",
        "years": year_rows,
        "manifest_file": manifest.name,
    }
    summary_path = args.output / "openalex_2018_2026_term_summary.json"
    summary_path.write_text(json.dumps(aggregate, ensure_ascii=False, indent=2), encoding="utf-8")
    checksum = args.output / "sha256sums.txt"
    files = master_paths + [manifest, summary_path]
    checksum.write_text("".join(f"{sha256_file(path)}  {path.relative_to(args.output)}\n" for path in files), encoding="utf-8")
    print(json.dumps(aggregate, ensure_ascii=False, indent=2))
    if not completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
