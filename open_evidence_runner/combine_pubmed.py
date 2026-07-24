from __future__ import annotations

import argparse
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


def merge_masters(input_root: Path, output_path: Path) -> int:
    records: dict[str, dict[str, Any]] = {}
    for path in sorted(input_root.rglob("paper_master_pubmed.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                item = json.loads(line)
                key = item.get("pmid") or item.get("doi_normalized") or hashlib.sha256(
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
                    for field in ("abstract", "doi_normalized", "pmcid", "mesh_terms"):
                        if not records[key].get(field) and item.get(field):
                            records[key][field] = item[field]
                else:
                    records[key] = item
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output_path, "wt", encoding="utf-8") as handle:
        for key in sorted(records):
            handle.write(json.dumps(records[key], ensure_ascii=False) + "\n")
    return len(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    annual = [load_json(path) for path in sorted(args.input.rglob("pubmed_*.json"))]
    master = args.output / "pubmed_2018_2026_master.jsonl.gz"
    unique_records = merge_masters(args.input, master)
    errors = [
        {"year": item.get("year"), "errors": item.get("errors")}
        for item in annual
        if item.get("errors")
    ]
    completed = len(annual) == 9 and all(item.get("completed") is True for item in annual)
    summary = {
        "run_id": f"pubmed-all-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source": "PubMed",
        "years_expected": 9,
        "years_received": len(annual),
        "years_completed": sum(item.get("completed") is True for item in annual),
        "query_groups_completed": sum(int(item.get("query_groups_completed") or 0) for item in annual),
        "pages_completed": sum(int(item.get("pages_completed") or 0) for item in annual),
        "raw_records": sum(int(item.get("raw_records") or 0) for item in annual),
        "unique_records": unique_records,
        "completed": completed,
        "errors": errors,
        "master_file": master.name,
        "master_sha256": sha256_file(master),
        "official_end_evidence": "Every ESearch count was matched by EFetch records in yearly or automatically split monthly windows.",
    }
    summary_path = args.output / "pubmed_2018_2026_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest = args.output / "sha256sums.txt"
    manifest.write_text(
        f"{sha256_file(master)}  {master.name}\n"
        f"{sha256_file(summary_path)}  {summary_path.name}\n",
        encoding="utf-8",
    )
    if not completed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
