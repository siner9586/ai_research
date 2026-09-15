from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
from pathlib import Path
from typing import Any

JSON_FIELDS = {"corpus_layers": [], "reasons": [], "evidence": []}


def blank(value: Any) -> bool:
    return value is None or str(value).strip() in {"", "nan", "NaN", "None", "null"}


def safe_float(value: Any) -> float | None:
    if blank(value):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def safe_int(value: Any) -> int | None:
    result = safe_float(value)
    return int(result) if result is not None else None


def safe_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y", "t"}


def parse_json(value: Any, default: Any) -> Any:
    if blank(value):
        return default
    try:
        parsed = json.loads(str(value))
    except json.JSONDecodeError:
        return default
    return parsed if isinstance(parsed, type(default)) else default


def find_one(root: Path, filename: str) -> Path:
    matches = list(root.rglob(filename))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one {filename}, found {len(matches)}")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--batch-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    source = find_one(args.artifact_root, "screening_decisions_independent_v2.csv.gz")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    decision_counts: dict[str, int] = {}
    reviewer_counts: dict[str, int] = {}
    with gzip.open(source, "rt", encoding="utf-8-sig", newline="") as input_handle, gzip.open(args.output, "wt", encoding="utf-8") as output_handle:
        for row in csv.DictReader(input_handle):
            candidate_id = str(row.get("candidate_id") or "").strip()
            if not candidate_id:
                raise RuntimeError("Missing candidate_id")
            decision = str(row.get("decision") or "").strip()
            if decision not in {"include", "uncertain", "exclude"}:
                raise RuntimeError(f"Unexpected decision {decision!r}")
            reviewer = str(row.get("reviewer") or "").strip()
            if not reviewer.startswith("machine-rule-v2:"):
                raise RuntimeError(f"Unexpected v2 reviewer {reviewer!r}")
            payload = {
                "candidate_id": candidate_id,
                "screening_stage": str(row.get("screening_stage") or "title_abstract_independent_rule_v2"),
                "reviewer": reviewer,
                "decision": decision,
                "corpus_layers": parse_json(row.get("corpus_layers"), []),
                "reasons": parse_json(row.get("reasons"), []),
                "exclusion_code": None if blank(row.get("exclusion_code")) else str(row.get("exclusion_code")),
                "evidence": parse_json(row.get("evidence"), []),
                "confidence": safe_float(row.get("confidence")),
                "requires_adjudication": safe_bool(row.get("requires_adjudication")),
                "technical_score": safe_int(row.get("technical_score")),
                "behavior_score": safe_int(row.get("behavior_score")),
                "professional_score": safe_int(row.get("professional_score")),
                "resource_score": safe_int(row.get("resource_score")),
                "governance_score": safe_int(row.get("governance_score")),
                "run_id": str(row.get("run_id") or "independent-screen-v2-20260724"),
                "source_artifact_layer": args.source,
            }
            # The generic OIDC importer adds the staging envelope. Emit only the
            # auditable decision payload here so it is not double-wrapped.
            output_handle.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n")
            count += 1
            decision_counts[decision] = decision_counts.get(decision, 0) + 1
            reviewer_counts[reviewer] = reviewer_counts.get(reviewer, 0) + 1

    summary = {
        "source": args.source,
        "batch_id": args.batch_id,
        "records": count,
        "decision_counts": decision_counts,
        "reviewer_counts": reviewer_counts,
        "output": str(args.output),
        "completed": True,
        "final_inclusion": False,
    }
    args.output.with_suffix("").with_suffix(".summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
