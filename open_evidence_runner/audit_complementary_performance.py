from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import tarfile
from pathlib import Path

import requests

REPOSITORY = "uw-hai/Complementary-Performance"
COMMIT = "6cebab4ffd2b332ebec5e27e7632e7bf1c36ba5f"
ARCHIVE_URL = f"https://api.github.com/repos/{REPOSITORY}/tarball/{COMMIT}"
MAX_BYTES = 100 * 1024 * 1024
SENSITIVE_PATTERNS = re.compile(r"(^|_)(email|name|phone|address|ip|workerid|mturkid)($|_)", re.I)
TRIAL_HINTS = {"assignmentid", "questionid", "task", "condition", "choice", "y", "pred", "conf"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def download(out: Path) -> dict:
    response = requests.get(
        ARCHIVE_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "open-evidence-resource-audit/1.0"},
        timeout=(30, 240),
        stream=True,
        allow_redirects=True,
    )
    response.raise_for_status()
    total = 0
    with out.open("wb") as fh:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("archive_exceeds_bounded_limit")
            fh.write(chunk)
    if out.read_bytes()[:2] != b"\x1f\x8b":
        raise RuntimeError("not_gzip_archive")
    return {"requested_url": ARCHIVE_URL, "final_url": response.url, "status": response.status_code, "bytes": total}


def audit_csv(raw: bytes, path: str) -> dict:
    text = raw.decode("utf-8-sig", errors="replace")
    reader = csv.reader(io.StringIO(text))
    try:
        header = next(reader)
    except StopIteration:
        return {"path": path, "rows": 0, "columns": [], "empty": True}
    rows = 0
    for _ in reader:
        rows += 1
    normalized = [re.sub(r"[^a-z0-9]", "", col.lower()) for col in header]
    sensitive = [col for col in header if SENSITIVE_PATTERNS.search(col)]
    trial_hits = sorted(TRIAL_HINTS.intersection(normalized))
    return {
        "path": path,
        "rows": rows,
        "columns": header,
        "column_count": len(header),
        "sensitive_column_candidates": sensitive,
        "trial_schema_hits": trial_hits,
        "trial_level_candidate": len(trial_hits) >= 6,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    archive = args.output / f"Complementary-Performance-{COMMIT}.tar.gz"
    transfer = download(archive)
    members = []
    csv_audits = []
    license_files = []
    readmes = []

    with tarfile.open(archive, "r:gz") as tf:
        for member in tf.getmembers():
            if not member.isfile():
                continue
            relative = "/".join(member.name.split("/")[1:])
            members.append({"path": relative, "size": member.size})
            lower = relative.lower()
            if Path(lower).name.startswith(("license", "copying")):
                license_files.append(relative)
            if Path(lower).name.startswith("readme"):
                readmes.append(relative)
            if lower.endswith(".csv"):
                extracted = tf.extractfile(member)
                if extracted:
                    csv_audits.append(audit_csv(extracted.read(), relative))

    team_files = [x for x in csv_audits if x.get("trial_level_candidate")]
    sensitive_files = [x for x in csv_audits if x.get("sensitive_column_candidates")]
    summary = {
        "repository": REPOSITORY,
        "fixed_commit": COMMIT,
        "transfer": transfer,
        "archive_sha256": sha256(archive),
        "archive_bytes": archive.stat().st_size,
        "file_count": len(members),
        "csv_file_count": len(csv_audits),
        "license_files": license_files,
        "license_status": "not_declared" if not license_files else "license_file_present_requires_content_review",
        "readme_files": readmes,
        "trial_level_candidate_files": [x["path"] for x in team_files],
        "sensitive_column_candidate_files": [x["path"] for x in sensitive_files],
        "participant_data_status": "anonymized_trial_level_candidate" if team_files and not sensitive_files else "manual_privacy_review_required",
        "code_executed": False,
    }
    (args.output / "repository_manifest.json").write_text(json.dumps(members, indent=2), encoding="utf-8")
    (args.output / "csv_schema_audit.json").write_text(json.dumps(csv_audits, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "SHA256SUMS.txt").write_text(f"{summary['archive_sha256']}  {archive.name}\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))

    if not team_files:
        raise SystemExit("No trial-level candidate CSV was detected")


if __name__ == "__main__":
    main()
