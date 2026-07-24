from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import re
from pathlib import Path
from typing import Any

JSON_FIELDS = {
    "work_type": [],
    "authors": [],
    "query_groups": [],
    "query_texts": [],
    "fields_of_study": [],
    "external_ids": {},
    "corpus_layers": [],
    "reasons": [],
    "evidence": [],
}
BOOL_FIELDS = {"is_oa", "requires_adjudication"}
INT_FIELDS = {
    "publication_year",
    "citation_count",
    "reference_count",
    "technical_score",
    "behavior_score",
    "professional_score",
    "resource_score",
    "governance_score",
}
FLOAT_FIELDS = {"confidence"}
ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def find_one(root: Path, name: str) -> Path:
    matches = list(root.rglob(name))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one {name}, found {len(matches)} under {root}")
    return matches[0]


def blank(value: Any) -> bool:
    return value is None or str(value).strip() in {"", "nan", "NaN", "None", "null"}


def parse_json(value: Any, default: Any) -> Any:
    if blank(value):
        return default
    if isinstance(value, type(default)):
        return value
    try:
        parsed = json.loads(str(value))
    except json.JSONDecodeError:
        return default
    return parsed if isinstance(parsed, type(default)) else default


def parse_bool(value: Any) -> bool | None:
    if blank(value):
        return None
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y", "t"}:
        return True
    if text in {"false", "0", "no", "n", "f"}:
        return False
    return None


def parse_int(value: Any) -> int | None:
    if blank(value):
        return None
    try:
        return int(float(str(value)))
    except ValueError:
        return None


def parse_float(value: Any) -> float | None:
    if blank(value):
        return None
    try:
        result = float(str(value))
    except ValueError:
        return None
    return result if math.isfinite(result) else None


def normalize_row(row: dict[str, Any]) -> dict[str, Any]:
    normalized: dict[str, Any] = {}
    for key, value in row.items():
        if key in JSON_FIELDS:
            normalized[key] = parse_json(value, JSON_FIELDS[key])
        elif key in BOOL_FIELDS:
            normalized[key] = parse_bool(value)
        elif key in INT_FIELDS:
            normalized[key] = parse_int(value)
        elif key in FLOAT_FIELDS:
            normalized[key] = parse_float(value)
        elif key == "publication_date":
            text = "" if blank(value) else str(value).strip()
            normalized[key] = text if ISO_DATE.fullmatch(text) else None
        else:
            normalized[key] = None if blank(value) else str(value).strip()
    return normalized


def load_csv(path: Path) -> list[dict[str, Any]]:
    with gzip.open(path, "rt", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    candidates = load_csv(find_one(args.artifact_root, "candidate_records_selected.csv.gz"))
    decisions = load_csv(find_one(args.artifact_root, "screening_decisions_selected.csv.gz"))
    decision_by_id = {str(row.get("candidate_id")): normalize_row(row) for row in decisions}
    if len(decision_by_id) != len(decisions):
        raise RuntimeError("Duplicate candidate_id in selected screening decisions")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    include = uncertain = exclude = 0
    years: dict[str, int] = {}
    with gzip.open(args.output, "wt", encoding="utf-8") as handle:
        for raw_candidate in candidates:
            candidate = normalize_row(raw_candidate)
            candidate_id = str(candidate.get("candidate_id") or "")
            decision = decision_by_id.get(candidate_id)
            if decision is None:
                raise RuntimeError(f"Missing screening decision for {candidate_id}")
            payload = {**candidate, **decision}
            payload["source_name"] = args.source
            payload["staging_batch_id"] = args.batch_id
            state = str(payload.get("decision") or "")
            if state == "include":
                include += 1
            elif state == "uncertain":
                uncertain += 1
            elif state == "exclude":
                exclude += 1
            else:
                raise RuntimeError(f"Unexpected decision {state!r} for {candidate_id}")
            year_key = str(payload.get("publication_year") or "unknown")
            years[year_key] = years.get(year_key, 0) + 1
            handle.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
            written += 1

    if written != len(candidates) or written != len(decisions):
        raise RuntimeError(
            f"Row mismatch candidates={len(candidates)} decisions={len(decisions)} written={written}"
        )
    report = {
        "source": args.source,
        "batch_id": args.batch_id,
        "records": written,
        "include": include,
        "uncertain": uncertain,
        "exclude": exclude,
        "publication_years": years,
        "output": str(args.output),
        "completed": True,
    }
    report_path = args.output.with_suffix("").with_suffix(".summary.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
