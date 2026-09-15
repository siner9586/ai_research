from __future__ import annotations

import argparse
import csv
import hashlib
import json
import tarfile
from pathlib import Path
from urllib.parse import urlparse

import requests

MAX_BYTES = 800 * 1024 * 1024
ALLOWED_HOSTS = {"codeload.github.com"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--expected-license", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    owner, name = args.repository.split("/", 1)
    args.output.mkdir(parents=True, exist_ok=True)
    safe_name = args.repository.replace("/", "__")
    archive = args.output / f"{safe_name}_{args.commit[:12]}.tar.gz"
    url = f"https://codeload.github.com/{owner}/{name}/tar.gz/{args.commit}"
    host = (urlparse(url).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise SystemExit(f"host_not_allowed:{host}")

    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-fixed-snapshot/1.0 (lawful public repository archive)"})
    response = session.get(url, stream=True, timeout=(30, 600), allow_redirects=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise SystemExit(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()
    total = 0
    with archive.open("wb") as out:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise SystemExit("archive_too_large")
            out.write(chunk)

    manifest_rows = []
    license_members = []
    total_uncompressed = 0
    with tarfile.open(archive, "r:gz") as tar:
        members = tar.getmembers()
        for member in members:
            if not member.isfile():
                continue
            total_uncompressed += member.size
            basename = Path(member.name).name.lower()
            row = {"path": member.name, "size_bytes": member.size}
            manifest_rows.append(row)
            if basename in {"license", "license.txt", "license.md", "copying", "notice"}:
                extracted = tar.extractfile(member)
                if extracted is not None:
                    content = extracted.read()
                    license_members.append({
                        "path": member.name,
                        "size_bytes": len(content),
                        "sha256": hashlib.sha256(content).hexdigest(),
                    })

    with (args.output / "file_manifest.csv").open("w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=["path", "size_bytes"])
        writer.writeheader()
        writer.writerows(manifest_rows)

    summary = {
        "repository": args.repository,
        "commit": args.commit,
        "requested_url": url,
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": response.headers.get("content-type"),
        "archive_file": archive.name,
        "archive_size_bytes": total,
        "archive_sha256": sha256_file(archive),
        "file_count": len(manifest_rows),
        "total_uncompressed_bytes": total_uncompressed,
        "expected_license": args.expected_license,
        "license_members": license_members,
        "code_executed": False,
        "validation_status": "verified_fixed_commit_snapshot" if manifest_rows else "invalid_empty_archive",
    }
    (args.output / "snapshot_audit.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if not manifest_rows:
        raise SystemExit("empty_archive")


if __name__ == "__main__":
    main()
