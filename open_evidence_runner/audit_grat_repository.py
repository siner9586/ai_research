from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
from pathlib import Path

import requests

REPOSITORY = "shuaibo919/g-rat"
COMMIT = "d27993218649d8bfcf54fcdabc2711e81bded3c8"
ARCHIVE_URL = f"https://api.github.com/repos/{REPOSITORY}/tarball/{COMMIT}"
MAX_BYTES = 100 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    archive = args.output / f"g-rat-{COMMIT}.tar.gz"
    response = requests.get(
        ARCHIVE_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "open-evidence-code-audit/1.0"},
        stream=True,
        allow_redirects=True,
        timeout=(30, 240),
    )
    response.raise_for_status()
    total = 0
    with archive.open("wb") as fh:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("archive_exceeds_limit")
            fh.write(chunk)
    if archive.read_bytes()[:2] != b"\x1f\x8b":
        raise RuntimeError("not_gzip_archive")

    manifest = []
    license_text = None
    readme_text = None
    scripts = []
    download_scripts = []
    source_files = []
    large_files = []
    secret_candidates = []
    secret_pattern = re.compile(r"(api[_-]?key|secret|token|password|private[_-]?key)", re.I)

    with tarfile.open(archive, "r:gz") as tf:
        for member in tf.getmembers():
            if not member.isfile():
                continue
            relative = "/".join(member.name.split("/")[1:])
            manifest.append({"path": relative, "size": member.size})
            lower = relative.lower()
            if member.size > 10 * 1024 * 1024:
                large_files.append(relative)
            if lower in {"license", "license.md", "license.txt"}:
                extracted = tf.extractfile(member)
                if extracted:
                    license_text = extracted.read().decode("utf-8", errors="replace")
            if lower == "readme.md":
                extracted = tf.extractfile(member)
                if extracted:
                    readme_text = extracted.read().decode("utf-8", errors="replace")
            if lower.endswith((".py", ".sh", ".yaml", ".yml", ".json", ".txt", ".md")):
                source_files.append(relative)
                if lower.endswith(".sh"):
                    scripts.append(relative)
                if "download" in lower and lower.endswith(".sh"):
                    download_scripts.append(relative)
                if member.size <= 2 * 1024 * 1024:
                    extracted = tf.extractfile(member)
                    if extracted:
                        text = extracted.read().decode("utf-8", errors="ignore")
                        if secret_pattern.search(text) and re.search(r"(?i)(api[_-]?key|secret|token|password)\s*[=:]\s*['\"][^'\"]{8,}", text):
                            secret_candidates.append(relative)

    requirement_match = {}
    if readme_text:
        for package in ("torch", "torchmetrics", "tqdm", "pandas", "numpy"):
            match = re.search(rf"{package}==([^\s]+)", readme_text, re.I)
            if match:
                requirement_match[package] = match.group(1)

    license_status = "MIT" if license_text and "MIT License" in license_text else "unknown_or_missing"
    summary = {
        "repository": REPOSITORY,
        "fixed_commit": COMMIT,
        "archive_url": ARCHIVE_URL,
        "final_url": response.url,
        "archive_bytes": archive.stat().st_size,
        "archive_sha256": sha256(archive),
        "file_count": len(manifest),
        "source_file_count": len(source_files),
        "shell_script_count": len(scripts),
        "download_scripts": download_scripts,
        "license_status": license_status,
        "license_file_present": license_text is not None,
        "declared_runtime": requirement_match,
        "large_files": large_files,
        "embedded_secret_candidates": secret_candidates,
        "code_executed": False,
        "reproducibility_status": "code_and_entrypoints_present_external_data_required" if readme_text and download_scripts else "manual_review_required",
    }
    (args.output / "repository_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "SHA256SUMS.txt").write_text(f"{summary['archive_sha256']}  {archive.name}\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if license_status != "MIT":
        raise SystemExit("MIT license was not verified")
    if secret_candidates:
        raise SystemExit("Potential embedded secret requires manual review")


if __name__ == "__main__":
    main()
