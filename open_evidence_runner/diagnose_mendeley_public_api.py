from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import zipfile
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests

BASE = "https://api.data.mendeley.com"
PAGE = "https://data.mendeley.com/datasets/{dataset_id}/{version}"
MAX_BODY = 200_000
MAX_FILE = 500 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def request_record(session: requests.Session, url: str, *, redirects: bool = False) -> tuple[dict[str, Any], requests.Response | None]:
    record: dict[str, Any] = {"url": url, "allow_redirects": redirects}
    try:
        response = session.get(url, timeout=(30, 120), allow_redirects=redirects)
    except requests.RequestException as exc:
        record["error"] = f"{type(exc).__name__}:{exc}"
        return record, None
    record.update({
        "status": response.status_code,
        "content_type": response.headers.get("Content-Type"),
        "content_length": response.headers.get("Content-Length"),
        "location": response.headers.get("Location"),
        "final_url": response.url,
    })
    body = response.content[:MAX_BODY]
    try:
        value = response.json()
        record["json"] = value
    except ValueError:
        record["body_prefix"] = body.decode("utf-8", errors="replace")
    return record, response


def collect_ids(value: Any) -> set[str]:
    found: set[str] = set()
    uuid_re = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.I)
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in {"id", "dataset_id", "data_entity_id", "uuid"} and isinstance(item, str) and uuid_re.match(item):
                found.add(item)
            found.update(collect_ids(item))
    elif isinstance(value, list):
        for item in value:
            found.update(collect_ids(item))
    return found


def safe_download(session: requests.Session, url: str, output: Path) -> dict[str, Any]:
    output.parent.mkdir(parents=True, exist_ok=True)
    with session.get(url, stream=True, timeout=(30, 180), allow_redirects=True) as response:
        response.raise_for_status()
        total = 0
        with output.open("wb") as f:
            for chunk in response.iter_content(1024 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > MAX_FILE:
                    raise RuntimeError("File exceeds audit maximum")
                f.write(chunk)
    return {"requested_url": url, "final_url": response.url, "size": total, "sha256": sha256(output), "content_type": response.headers.get("Content-Type")}


def possible_file_objects(value: Any) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    if isinstance(value, list):
        for item in value:
            if isinstance(item, dict):
                output.append(item)
    elif isinstance(value, dict):
        for key in ("items", "data", "results", "files"):
            if isinstance(value.get(key), list):
                output.extend(x for x in value[key] if isinstance(x, dict))
    return output


def filename_of(item: dict[str, Any]) -> str:
    return str(item.get("filename") or item.get("name") or item.get("key") or "")


def download_url_of(item: dict[str, Any]) -> str | None:
    details = item.get("content_details") or {}
    links = item.get("links") or {}
    return details.get("download_url") or item.get("download_url") or links.get("download") or links.get("content")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--version", type=int, required=True)
    parser.add_argument("--expected", action="append", default=[])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/2.0 mendeley-public-api-diagnostic", "Accept": "application/json, */*"})

    records: list[dict[str, Any]] = []
    aliases = {args.dataset_id}
    discovery_urls = [
        f"{BASE}/datasets/{args.dataset_id}?version={args.version}",
        f"{BASE}/datasets/{args.dataset_id}/versions",
        PAGE.format(dataset_id=args.dataset_id, version=args.version),
    ]
    for url in discovery_urls:
        record, _ = request_record(session, url)
        records.append(record)
        aliases.update(collect_ids(record.get("json")))
        aliases.update(collect_ids(record.get("body_prefix")))

    file_objects: list[dict[str, Any]] = []
    for alias in sorted(aliases):
        for url in [
            f"{BASE}/datasets/publics/{alias}/files?version={args.version}&$limit=100",
            f"{BASE}/datasets/{alias}/files?version={args.version}&$limit=100",
        ]:
            record, _ = request_record(session, url)
            records.append(record)
            file_objects.extend(possible_file_objects(record.get("json")))

    downloaded: list[dict[str, Any]] = []
    expected_lower = {name.lower() for name in args.expected}
    for item in file_objects:
        filename = filename_of(item)
        if not filename or (expected_lower and filename.lower() not in expected_lower):
            continue
        url = download_url_of(item)
        file_id = item.get("id")
        candidates = [url] if url else []
        for alias in sorted(aliases):
            if file_id:
                candidates.extend([
                    f"{BASE}/datasets/publics/{alias}/files/{file_id}?version={args.version}",
                    f"{BASE}/datasets/{alias}/files/{file_id}/file_downloaded?version={args.version}",
                ])
        for candidate in [x for x in candidates if x]:
            record, response = request_record(session, candidate, redirects=False)
            records.append(record)
            final = record.get("location") or candidate
            if response is not None and response.status_code == 200 and "application/json" in str(response.headers.get("Content-Type")):
                value = record.get("json") or {}
                final = download_url_of(value) or final
            try:
                download = safe_download(session, final, args.output / "files" / Path(filename).name)
            except Exception as exc:
                records.append({"download_candidate": final, "error": f"{type(exc).__name__}:{exc}"})
                continue
            downloaded.append({"filename": filename, "file_object": item, "download": download})
            break

    # Download-all route is attempted for every known alias. A successful ZIP is
    # retained even if expected-file extraction is needed in the next revision.
    zip_results = []
    for alias in sorted(aliases):
        url = f"{BASE}/datasets/{alias}/zip/file_downloaded?version={args.version}"
        record, response = request_record(session, url, redirects=False)
        records.append(record)
        final = record.get("location")
        if not final:
            continue
        zip_path = args.output / "downloads" / f"{alias}_v{args.version}.zip"
        try:
            download = safe_download(session, final, zip_path)
            download["is_zip"] = zipfile.is_zipfile(zip_path)
            if download["is_zip"]:
                with zipfile.ZipFile(zip_path) as z:
                    download["members"] = z.namelist()
            zip_results.append(download)
        except Exception as exc:
            records.append({"download_candidate": final, "error": f"{type(exc).__name__}:{exc}"})

    report = {
        "dataset_id": args.dataset_id,
        "version": args.version,
        "expected_files": args.expected,
        "aliases": sorted(aliases),
        "api_records": records,
        "file_objects": file_objects,
        "downloaded_files": downloaded,
        "zip_results": zip_results,
        "completed": bool(downloaded),
        "generated_at_epoch": time.time(),
    }
    (args.output / "diagnostic.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"dataset_id": args.dataset_id, "aliases": sorted(aliases), "file_objects": len(file_objects), "downloaded": len(downloaded), "zip_results": len(zip_results), "completed": report["completed"]}, indent=2))


if __name__ == "__main__":
    main()
