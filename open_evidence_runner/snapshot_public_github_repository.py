from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import zipfile
from pathlib import Path

TARGETS = {
    "peterbhase-InterpretableNLP-ACL2020": {
        "repository": "peterbhase/InterpretableNLP-ACL2020",
        "expected_default_branch": "master",
        "linked_paper": "doi:10.18653/v1/2020.acl-main.491",
        "expected_license": "MIT",
    },
    "anoymous-518-anon-artifact": {
        "repository": "anoymous-518/anon-artifact",
        "expected_default_branch": "main",
        "linked_paper": "arxiv:2602.04003",
        "expected_license": "NO_LICENSE_FILE_FOUND",
    },
    "distillpub-post--building-blocks": {
        "repository": "distillpub/post--building-blocks",
        "expected_default_branch": "master",
        "linked_paper": "doi:10.23915/distill.00010",
        "expected_license": "CC BY 4.0 article source; verify repository files",
    },
}

MAX_ARCHIVE_BYTES = 500 * 1024 * 1024
LICENSE_NAMES = {
    "license", "license.txt", "license.md", "copying", "copying.txt",
    "copyright", "notice", "notice.txt",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(*args: str, cwd: Path | None = None) -> str:
    completed = subprocess.run(args, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return completed.stdout.strip()


def is_lfs_pointer(path: Path) -> bool:
    try:
        prefix = path.read_bytes()[:200]
    except OSError:
        return False
    return prefix.startswith(b"version https://git-lfs.github.com/spec/v1")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target-id", choices=sorted(TARGETS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    target = TARGETS[args.target_id]
    root = args.output
    clone_dir = root / "repository"
    root.mkdir(parents=True, exist_ok=True)

    clone_url = f"https://github.com/{target['repository']}.git"
    run("git", "clone", "--depth", "1", "--no-tags", clone_url, str(clone_dir))
    commit_hash = run("git", "rev-parse", "HEAD", cwd=clone_dir)
    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD", cwd=clone_dir)
    commit_time = run("git", "show", "-s", "--format=%cI", "HEAD", cwd=clone_dir)
    commit_subject = run("git", "show", "-s", "--format=%s", "HEAD", cwd=clone_dir)

    rows = []
    license_files = []
    lfs_pointers = []
    total_bytes = 0
    for path in sorted(clone_dir.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(clone_dir).as_posix()
        size = path.stat().st_size
        total_bytes += size
        digest = sha256_file(path)
        pointer = is_lfs_pointer(path)
        if pointer:
            lfs_pointers.append(relative)
        row = {"path": relative, "size_bytes": size, "sha256": digest, "git_lfs_pointer": pointer}
        rows.append(row)
        if path.name.lower() in LICENSE_NAMES:
            try:
                text = path.read_text(encoding="utf-8", errors="replace")[:30000]
            except OSError:
                text = ""
            license_files.append({"path": relative, "sha256": digest, "text_excerpt": text})

    manifest_path = root / "file_manifest.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "size_bytes", "sha256", "git_lfs_pointer"])
        writer.writeheader()
        writer.writerows(rows)

    archive_path = root / f"{args.target_id}_{commit_hash[:12]}.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for row in rows:
            path = clone_dir / row["path"]
            archive.write(path, arcname=f"{target['repository'].replace('/', '__')}/{row['path']}")
    if archive_path.stat().st_size > MAX_ARCHIVE_BYTES:
        archive_path.unlink(missing_ok=True)
        raise RuntimeError("repository_snapshot_archive_too_large")

    metadata = {
        **target,
        "target_id": args.target_id,
        "clone_url": clone_url,
        "commit_hash": commit_hash,
        "branch": branch,
        "commit_time": commit_time,
        "commit_subject": commit_subject,
        "file_count": len(rows),
        "uncompressed_bytes": total_bytes,
        "archive_file": archive_path.name,
        "archive_size_bytes": archive_path.stat().st_size,
        "archive_sha256": sha256_file(archive_path),
        "license_files": license_files,
        "license_status": "license_file_found" if license_files else "no_license_file_found",
        "lfs_pointer_count": len(lfs_pointers),
        "lfs_pointers": lfs_pointers,
        "code_executed": False,
        "completed": True,
    }
    (root / "repository_snapshot_audit.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    shutil.rmtree(clone_dir)
    print(json.dumps({key: metadata[key] for key in ("repository", "commit_hash", "file_count", "archive_size_bytes", "license_status", "lfs_pointer_count")}, indent=2))


if __name__ == "__main__":
    main()
