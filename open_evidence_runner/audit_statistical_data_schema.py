from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any

import pyreadstat

ID_PATTERN = re.compile(r"(participant|subject|prolific|worker|respondent|response.?id|^id$)", re.I)
INITIAL_PATTERN = re.compile(r"(initial|first|before|pre[_ -]?advice|estimate.?1|judg(e)?ment.?1)", re.I)
ADVICE_PATTERN = re.compile(r"(advice|algorithm|computer|model|forecast|recommend|machine|human.?advisor)", re.I)
FINAL_PATTERN = re.compile(r"(final|second|after|post[_ -]?advice|estimate.?2|judg(e)?ment.?2|revised)", re.I)
OUTCOME_PATTERN = re.compile(r"(correct|accuracy|error|truth|actual|outcome|ground.?truth|score)", re.I)
TRUST_PATTERN = re.compile(r"(trust|confidence|reliance|rely|use.?advice|weight.?of.?advice|woa)", re.I)
CONDITION_PATTERN = re.compile(r"(condition|treatment|group|random|advisor.?type|algorithm.?condition)", re.I)


def matches(columns: list[str], pattern: re.Pattern[str]) -> list[str]:
    return [column for column in columns if pattern.search(column)]


def read_file(path: Path) -> tuple[Any, Any]:
    suffix = path.suffix.lower()
    if suffix == ".sav":
        return pyreadstat.read_sav(path, apply_value_formats=False)
    if suffix == ".dta":
        return pyreadstat.read_dta(path, apply_value_formats=False)
    raise ValueError(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    files = sorted(
        path for path in args.artifact_root.rglob("*")
        if path.is_file() and path.suffix.lower() in {".sav", ".dta"}
    )
    if not files:
        raise RuntimeError("No SAV or DTA files found")

    reports = []
    summary_rows = []
    for path in files:
        try:
            frame, meta = read_file(path)
        except Exception as exc:
            reports.append({"file": str(path.relative_to(args.artifact_root)), "read_error": f"{type(exc).__name__}:{exc}"})
            continue
        columns = [str(column) for column in frame.columns]
        id_fields = matches(columns, ID_PATTERN)
        initial_fields = matches(columns, INITIAL_PATTERN)
        advice_fields = matches(columns, ADVICE_PATTERN)
        final_fields = matches(columns, FINAL_PATTERN)
        outcome_fields = matches(columns, OUTCOME_PATTERN)
        trust_fields = matches(columns, TRUST_PATTERN)
        condition_fields = matches(columns, CONDITION_PATTERN)
        duplicate_rows = int(frame.duplicated().sum())
        completely_empty_columns = [str(column) for column in frame.columns if frame[column].isna().all()]
        report = {
            "file": str(path.relative_to(args.artifact_root)),
            "format": path.suffix.lower().lstrip("."),
            "rows": int(frame.shape[0]),
            "columns": int(frame.shape[1]),
            "column_names": columns,
            "column_labels": dict(zip(columns, [None if value is None else str(value) for value in (meta.column_labels or [])])),
            "id_fields": id_fields,
            "initial_decision_fields": initial_fields,
            "advice_fields": advice_fields,
            "final_decision_fields": final_fields,
            "outcome_fields": outcome_fields,
            "trust_or_reliance_fields": trust_fields,
            "condition_fields": condition_fields,
            "duplicate_full_rows": duplicate_rows,
            "completely_empty_columns": completely_empty_columns,
            "participant_level_candidate": bool(id_fields) and frame.shape[0] > 0,
            "direct_pre_advice_post_advice_candidate": bool(initial_fields and advice_fields and final_fields),
            "behavioral_reliance_candidate": bool(advice_fields and (final_fields or trust_fields or outcome_fields)),
            "value_labels": {
                str(variable): {str(key): str(value) for key, value in mapping.items()}
                for variable, mapping in (meta.variable_value_labels or {}).items()
            },
            "privacy_boundary": "No participant cell values are exported by this schema audit.",
        }
        reports.append(report)
        summary_rows.append({
            "file": report["file"],
            "rows": report["rows"],
            "columns": report["columns"],
            "participant_level_candidate": report["participant_level_candidate"],
            "direct_pre_advice_post_advice_candidate": report["direct_pre_advice_post_advice_candidate"],
            "behavioral_reliance_candidate": report["behavioral_reliance_candidate"],
            "id_field_count": len(id_fields),
            "initial_field_count": len(initial_fields),
            "advice_field_count": len(advice_fields),
            "final_field_count": len(final_fields),
            "outcome_field_count": len(outcome_fields),
            "trust_field_count": len(trust_fields),
            "condition_field_count": len(condition_fields),
        })

    readable = [item for item in reports if not item.get("read_error")]
    summary = {
        "statistical_files_found": len(files),
        "statistical_files_readable": len(readable),
        "total_rows_across_files": sum(int(item.get("rows") or 0) for item in readable),
        "participant_level_candidate_files": sum(bool(item.get("participant_level_candidate")) for item in readable),
        "direct_pre_advice_post_advice_candidate_files": sum(bool(item.get("direct_pre_advice_post_advice_candidate")) for item in readable),
        "behavioral_reliance_candidate_files": sum(bool(item.get("behavioral_reliance_candidate")) for item in readable),
        "read_errors": [item for item in reports if item.get("read_error")],
        "completed": len(readable) == len(files),
        "final_ipd_decision": "pending study-specific mapping and duplicate-sample audit",
    }
    (args.output / "statistical_schema_audit.json").write_text(
        json.dumps({"summary": summary, "files": reports}, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    with (args.output / "statistical_schema_summary.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        fields = list(summary_rows[0])
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary_rows)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not summary["completed"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
