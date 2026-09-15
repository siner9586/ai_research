from __future__ import annotations

import argparse
import json
import os
import zipfile
from pathlib import Path

from extract_remote_artifact_summary import (
    central_members,
    get_signed_url,
    locate_central_directory,
    read_member,
    remote_size,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--artifact-id", required=True)
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    location = get_signed_url(args.repository, args.artifact_id, os.environ["GITHUB_TOKEN"])
    total_size = remote_size(location)
    cd_offset, cd_size, expected_entries = locate_central_directory(location, total_size)
    members = central_members(location, cd_offset, cd_size)
    if expected_entries and len(members) != expected_entries:
        raise RuntimeError(
            f"central directory mismatch: expected {expected_entries}, got {len(members)}"
        )

    summary_suffix = f"crossref_{args.year}_summary.json"
    manifest_suffix = f"crossref_{args.year}_search_queries.csv"
    selected = [
        member
        for member in members
        if member["filename"].endswith((summary_suffix, manifest_suffix))
    ]
    if len(selected) != 2:
        raise RuntimeError(
            f"expected annual summary and manifest; found {[m['filename'] for m in selected]}"
        )

    member_sizes = {
        "artifact_id": args.artifact_id,
        "year": args.year,
        "artifact_size": total_size,
        "central_directory_entries": len(members),
        "selected_members": selected,
    }
    (args.output / f"crossref_{args.year}_artifact_member_sizes.json").write_text(
        json.dumps(member_sizes, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    compact_zip = args.output / f"crossref_{args.year}_summary_only.zip"
    with zipfile.ZipFile(compact_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in selected:
            data = read_member(location, member)
            output_name = Path(member["filename"]).name
            archive.writestr(output_name, data)
            (args.output / output_name).write_bytes(data)

    summary = json.loads((args.output / summary_suffix).read_text(encoding="utf-8"))
    if summary.get("year") != args.year:
        raise RuntimeError("year mismatch in summary")
    if summary.get("completed") is not True:
        raise RuntimeError("annual Crossref summary is not completed")
    if summary.get("subqueries_attempted") != summary.get("subqueries_expected"):
        raise RuntimeError("not all Crossref subqueries were attempted")
    if summary.get("subqueries_completed") != summary.get("subqueries_expected"):
        raise RuntimeError("not all Crossref subqueries were completed")
    if summary.get("errors"):
        raise RuntimeError(f"Crossref annual summary has errors: {summary['errors']}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
