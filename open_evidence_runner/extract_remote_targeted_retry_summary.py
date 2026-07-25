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

    url = get_signed_url(args.repository, args.artifact_id, os.environ["GITHUB_TOKEN"])
    size = remote_size(url)
    cd_offset, cd_size, expected_entries = locate_central_directory(url, size)
    members = central_members(url, cd_offset, cd_size)
    if expected_entries and len(members) != expected_entries:
        raise RuntimeError(f"central directory entry mismatch: expected {expected_entries}, got {len(members)}")

    suffixes = (
        f"crossref_{args.year}_targeted_retry_summary.json",
        f"crossref_{args.year}_targeted_retry_manifest.csv",
    )
    selected = [m for m in members if m["filename"].endswith(suffixes)]
    if len(selected) != 2:
        raise RuntimeError(f"expected targeted retry summary and manifest, found {[m['filename'] for m in selected]}")

    member_meta = args.output / f"crossref_{args.year}_targeted_retry_members.json"
    member_meta.write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding="utf-8")
    output_zip = args.output / f"crossref-{args.year}-targeted-retry-summary-only.zip"
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in selected:
            data = read_member(url, member)
            name = Path(member["filename"]).name
            archive.writestr(name, data)
            (args.output / name).write_bytes(data)
            if name.endswith("_summary.json"):
                print(json.dumps(json.loads(data), ensure_ascii=False, indent=2))
    print(json.dumps({"artifact_size": size, "selected_members": selected}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
