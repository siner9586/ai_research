from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
from pathlib import Path
from urllib.parse import quote, urlparse

import pandas as pd
import requests

REPOSITORY = "SalesforceAIResearch/FaithEval"
COMMIT = "58d35840e3fbc7bf4b7672582a417b3b3a327dec"
DATASETS = [
    "Salesforce/FaithEval-counterfactual-v1.0",
    "Salesforce/FaithEval-inconsistent-v1.0",
    "Salesforce/FaithEval-unanswerable-v1.0",
]
ALLOWED_HOSTS = {"api.github.com", "github.com", "codeload.github.com", "huggingface.co", "hf.co", "cdn-lfs.hf.co", "cas-bridge.xethub.hf.co"}
MAX_FILE_BYTES = 120 * 1024 * 1024
MAX_DATASET_BYTES = 300 * 1024 * 1024
SUPPORTED = {".json", ".jsonl", ".csv", ".tsv", ".parquet"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def safe(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")


def bounded_download(session: requests.Session, url: str, path: Path) -> dict:
    host = (urlparse(url).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")
    path.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    with session.get(url, timeout=(30, 300), stream=True, allow_redirects=True) as response:
        final_host = (urlparse(response.url).hostname or "").lower()
        if final_host not in ALLOWED_HOSTS:
            raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
        response.raise_for_status()
        with path.open("wb") as fh:
            for chunk in response.iter_content(1024 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > MAX_FILE_BYTES:
                    raise RuntimeError("file_exceeds_limit")
                fh.write(chunk)
        return {"requested_url": url, "final_url": response.url, "status": response.status_code, "content_type": response.headers.get("content-type"), "bytes": total, "sha256": sha256(path)}


def inspect_table(path: Path) -> dict:
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        frame = pd.read_parquet(path)
    elif suffix == ".csv":
        frame = pd.read_csv(path, low_memory=False)
    elif suffix == ".tsv":
        frame = pd.read_csv(path, sep="\t", low_memory=False)
    elif suffix == ".jsonl":
        frame = pd.read_json(path, lines=True)
    elif suffix == ".json":
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, list):
            frame = pd.json_normalize(value)
        elif isinstance(value, dict):
            if isinstance(value.get("data"), list):
                frame = pd.json_normalize(value["data"])
            else:
                return {"json_top_level_type": "object", "top_level_keys": sorted(value.keys()), "rows": None, "columns": None}
        else:
            return {"json_top_level_type": type(value).__name__, "rows": None, "columns": None}
    else:
        return {"structural_parse": "not_supported"}
    return {
        "rows": int(len(frame)),
        "columns": int(len(frame.columns)),
        "column_names": [str(c) for c in frame.columns],
        "duplicate_rows": int(frame.astype(str).duplicated().sum()),
        "null_counts": {str(k): int(v) for k, v in frame.isna().sum().items()},
    }


def audit_repo(session: requests.Session, out: Path) -> dict:
    url = f"https://api.github.com/repos/{REPOSITORY}/tarball/{COMMIT}"
    archive = out / f"FaithEval-{COMMIT}.tar.gz"
    transfer = bounded_download(session, url, archive)
    if archive.read_bytes()[:2] != b"\x1f\x8b":
        raise RuntimeError("repo_archive_not_gzip")
    manifest = []
    license_text = None
    readme_text = None
    secret_candidates = []
    pattern = re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[=:]\s*['\"][^'\"]{8,}")
    with tarfile.open(archive, "r:gz") as tf:
        for member in tf.getmembers():
            if not member.isfile():
                continue
            relative = "/".join(member.name.split("/")[1:])
            manifest.append({"path": relative, "size": member.size})
            lower = relative.lower()
            extracted = tf.extractfile(member)
            raw = extracted.read() if extracted and member.size <= 3 * 1024 * 1024 else b""
            if Path(lower).name in {"license", "license.txt", "license.md"}:
                license_text = raw.decode("utf-8", errors="replace")
            if Path(lower).name == "readme.md":
                readme_text = raw.decode("utf-8", errors="replace")
            if raw and pattern.search(raw.decode("utf-8", errors="ignore")):
                secret_candidates.append(relative)
    (out / "github_repository_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "repository": REPOSITORY,
        "fixed_commit": COMMIT,
        "archive_transfer": transfer,
        "archive_sha256": sha256(archive),
        "file_count": len(manifest),
        "license_status": "Apache-2.0" if license_text and "Apache License" in license_text else "unknown_or_missing",
        "readme_present": readme_text is not None,
        "embedded_secret_candidates": secret_candidates,
        "code_executed": False,
    }


def audit_dataset(session: requests.Session, dataset_id: str, out: Path) -> dict:
    api_url = f"https://huggingface.co/api/datasets/{dataset_id}"
    response = session.get(api_url, timeout=(30, 180))
    response.raise_for_status()
    metadata = response.json()
    revision = metadata.get("sha")
    siblings = metadata.get("siblings") or []
    card_data = metadata.get("cardData") or {}
    root = out / safe(dataset_id)
    total = 0
    files = []
    errors = []
    for sibling in siblings:
        name = sibling.get("rfilename")
        if not name:
            continue
        suffix = Path(name).suffix.lower()
        size = sibling.get("size") if isinstance(sibling.get("size"), int) else None
        row = {"rfilename": name, "api_size": size}
        if suffix not in SUPPORTED:
            row["download_status"] = "metadata_only_unsupported_extension"
            files.append(row)
            continue
        if size and (size > MAX_FILE_BYTES or total + size > MAX_DATASET_BYTES):
            row["download_status"] = "bounded_limit_not_downloaded"
            files.append(row)
            continue
        url = f"https://huggingface.co/datasets/{dataset_id}/resolve/{revision}/{quote(name, safe='/')}?download=true"
        path = root / name
        try:
            transfer = bounded_download(session, url, path)
            total += transfer["bytes"]
            row["download_status"] = "verified"
            row["local_file"] = str(path.relative_to(out))
            row["transfer"] = transfer
            row["table_audit"] = inspect_table(path)
        except Exception as exc:
            path.unlink(missing_ok=True)
            row["download_status"] = "retryable"
            row["error"] = f"{type(exc).__name__}:{exc}"
            errors.append({"file": name, "error": row["error"]})
        files.append(row)
    metadata_path = root / "huggingface_api_metadata.json"
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    row_counts = [item.get("table_audit", {}).get("rows") for item in files if item.get("table_audit", {}).get("rows") is not None]
    return {
        "dataset_id": dataset_id,
        "revision": revision,
        "private": metadata.get("private"),
        "gated": metadata.get("gated"),
        "disabled": metadata.get("disabled"),
        "license": card_data.get("license") or metadata.get("license"),
        "file_count": len(siblings),
        "downloaded_table_files": sum(item.get("download_status") == "verified" for item in files),
        "downloaded_bytes": total,
        "row_counts": row_counts,
        "total_rows_across_files": sum(row_counts),
        "errors": errors,
        "files": files,
        "api_metadata_sha256": sha256(metadata_path),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/3.0 FaithEval-resource-audit", "Accept": "application/json,*/*"})
    repo = audit_repo(session, args.output)
    datasets = [audit_dataset(session, dataset_id, args.output / "datasets") for dataset_id in DATASETS]
    summary = {
        "repository": repo,
        "datasets": datasets,
        "dataset_count": len(datasets),
        "dataset_files_downloaded": sum(d["downloaded_table_files"] for d in datasets),
        "dataset_rows_total": sum(d["total_rows_across_files"] for d in datasets),
        "code_executed": False,
    }
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    sums = []
    for path in sorted(x for x in args.output.rglob("*") if x.is_file() and x.name != "SHA256SUMS.txt"):
        sums.append(f"{sha256(path)}  {path.relative_to(args.output)}")
    (args.output / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print(json.dumps({"repo_license": repo["license_status"], "datasets": [(d["dataset_id"], d["revision"], d["license"], d["total_rows_across_files"], len(d["errors"])) for d in datasets]}, indent=2))
    if repo["license_status"] != "Apache-2.0":
        raise SystemExit("Repository license not verified")
    if repo["embedded_secret_candidates"]:
        raise SystemExit("Potential embedded secret requires manual review")
    if not any(d["downloaded_table_files"] for d in datasets):
        raise SystemExit("No benchmark data file was downloaded and parsed")

if __name__ == "__main__":
    main()
