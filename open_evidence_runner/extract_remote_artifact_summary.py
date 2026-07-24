from __future__ import annotations

import argparse
import json
import os
import zipfile
from pathlib import Path

import requests
from remotezip import RemoteZip


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--artifact-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    token = os.environ["GITHUB_TOKEN"]
    api_url = f"https://api.github.com/repos/{args.repository}/actions/artifacts/{args.artifact_id}/zip"
    response = requests.get(
        api_url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"},
        allow_redirects=False,
        timeout=60,
    )
    response.raise_for_status()
    location = response.headers["Location"]
    args.output.mkdir(parents=True, exist_ok=True)

    selected_suffixes = (
        "aggregate/crossref_all_summary.json",
        "aggregate/crossref_all_search_queries.csv",
    )
    metadata = []
    with RemoteZip(location) as archive:
        infos = archive.infolist()
        for info in infos:
            if info.filename.endswith(
                (
                    "crossref_all_summary.json",
                    "crossref_all_search_queries.csv",
                    "crossref_all_paper_master.jsonl.gz",
                    "crossref_all_paper_master.csv.gz",
                )
            ):
                metadata.append(
                    {
                        "filename": info.filename,
                        "file_size": info.file_size,
                        "compress_size": info.compress_size,
                        "crc": info.CRC,
                    }
                )
        output_zip = args.output / "crossref-summary-only.zip"
        with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
            for info in infos:
                if info.filename.endswith(selected_suffixes):
                    data = archive.read(info.filename)
                    out.writestr(Path(info.filename).name, data)
                    if info.filename.endswith("crossref_all_summary.json"):
                        summary = json.loads(data)
                        (args.output / "crossref_all_summary.json").write_text(
                            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
                        )
                        print(json.dumps(summary, ensure_ascii=False, indent=2))
        (args.output / "crossref_artifact_member_sizes.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps({"selected_members": metadata}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
