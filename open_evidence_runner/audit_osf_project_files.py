from __future__ import annotations

import argparse
import csv
import hashlib
import json
import mimetypes
import re
from collections import Counter, deque
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests

API_HOST = "api.osf.io"
ALLOWED_DOWNLOAD_HOSTS = {
    "files.osf.io",
    "osf.io",
    "storage.googleapis.com",
    "storage.cloud.google.com",
}
MAX_SINGLE_FILE_BYTES = 120 * 1024 * 1024
MAX_TOTAL_DOWNLOAD_BYTES = 500 * 1024 * 1024

COLUMN_GROUPS = {
    "participant_id": [r"participant", r"subject", r"worker", r"prolific", r"respondent", r"user[_ -]?id", r"^pid$"],
    "trial_id": [r"trial", r"item[_ -]?id", r"case[_ -]?id", r"stimulus", r"scenario", r"applicant"],
    "condition": [r"condition", r"treatment", r"group", r"explanation", r"accuracy[_ -]?condition"],
    "initial_decision": [r"initial", r"pre[_ -]?decision", r"decision[_ -]?before", r"first[_ -]?decision"],
    "ai_advice": [r"ai[_ -]?(advice|recommend|output|prediction)", r"algorithm[_ -]?(advice|recommend|output|prediction)", r"system[_ -]?(advice|recommend|output|prediction)"],
    "ai_correctness": [r"ai[_ -]?(correct|accuracy)", r"advice[_ -]?(correct|accuracy)", r"output[_ -]?(correct|accuracy)", r"ground[_ -]?truth"],
    "final_decision": [r"final", r"post[_ -]?decision", r"decision[_ -]?after", r"revised[_ -]?decision", r"trusting[_ -]?behavio"],
    "trust": [r"trust", r"trustworth", r"reliance", r"rely", r"confidence", r"expectation[_ -]?violation"],
    "response_time": [r"response[_ -]?time", r"duration", r"latency", r"rt$"],
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def host_allowed(host: str) -> bool:
    host = host.lower()
    return host in ALLOWED_DOWNLOAD_HOSTS or host.endswith(".osf.io") or host.endswith(".googleusercontent.com")


def get_json(session: requests.Session, url: str) -> dict:
    host = (urlparse(url).hostname or "").lower()
    if host != API_HOST:
        raise RuntimeError(f"non_osf_api_host:{host}")
    response = session.get(url, timeout=(30, 180), allow_redirects=True)
    response.raise_for_status()
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host != API_HOST:
        raise RuntimeError(f"api_redirect_host_not_allowed:{final_host}")
    return response.json()


def paginate(session: requests.Session, url: str):
    while url:
        payload = get_json(session, url)
        for item in payload.get("data", []):
            yield item
        next_link = payload.get("links", {}).get("next")
        if isinstance(next_link, dict):
            url = next_link.get("href")
        else:
            url = next_link


def related_href(relationship: dict | None) -> str | None:
    if not relationship:
        return None
    related = relationship.get("links", {}).get("related")
    if isinstance(related, dict):
        return related.get("href")
    if isinstance(related, str):
        return related
    return None


def enumerate_files(session: requests.Session, node_id: str) -> tuple[list[dict], list[dict]]:
    providers_url = f"https://api.osf.io/v2/nodes/{node_id}/files/"
    providers = list(paginate(session, providers_url))
    files: list[dict] = []
    queue: deque[tuple[str, str, str]] = deque()
    for provider in providers:
        provider_name = provider.get("attributes", {}).get("name") or provider.get("id")
        root_url = related_href(provider.get("relationships", {}).get("files"))
        if root_url:
            queue.append((provider_name, "/", root_url))
    seen_urls: set[str] = set()
    while queue:
        provider_name, parent_path, url = queue.popleft()
        if url in seen_urls:
            continue
        seen_urls.add(url)
        for item in paginate(session, url):
            attrs = item.get("attributes", {})
            kind = attrs.get("kind")
            name = attrs.get("name") or item.get("id")
            materialized = attrs.get("materialized_path") or f"{parent_path.rstrip('/')}/{name}"
            links = item.get("links", {})
            relationships = item.get("relationships", {})
            row = {
                "file_id": item.get("id"),
                "provider": provider_name,
                "kind": kind,
                "name": name,
                "materialized_path": materialized,
                "size_bytes": attrs.get("size"),
                "date_created": attrs.get("date_created"),
                "date_modified": attrs.get("date_modified"),
                "resource_type": attrs.get("resource_type"),
                "guid": attrs.get("guid"),
                "download_url": links.get("download"),
                "html_url": links.get("html"),
                "delete_url": links.get("delete"),
                "move_url": links.get("move"),
            }
            files.append(row)
            if kind == "folder":
                child_url = related_href(relationships.get("files"))
                if child_url:
                    queue.append((provider_name, materialized, child_url))
    return providers, files


def match_columns(columns: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for group, patterns in COLUMN_GROUPS.items():
        hits = []
        for col in columns:
            normalized = str(col).strip().lower()
            if any(re.search(pattern, normalized) for pattern in patterns):
                hits.append(str(col))
        result[group] = sorted(set(hits))
    return result


def inspect_table(path: Path) -> dict:
    suffix = path.suffix.lower()
    try:
        if suffix == ".csv":
            frame = pd.read_csv(path, low_memory=False)
        elif suffix in {".tsv", ".tab"}:
            frame = pd.read_csv(path, sep="\t", low_memory=False)
        elif suffix in {".xlsx", ".xlsm", ".xls"}:
            book = pd.ExcelFile(path)
            sheets = []
            total_rows = 0
            all_columns: list[str] = []
            for sheet in book.sheet_names:
                df = pd.read_excel(path, sheet_name=sheet)
                sheets.append({"sheet": sheet, "rows": int(len(df)), "columns": [str(c) for c in df.columns]})
                total_rows += len(df)
                all_columns.extend(str(c) for c in df.columns)
            return {
                "format": suffix.lstrip("."),
                "sheet_count": len(sheets),
                "sheets": sheets,
                "total_rows": int(total_rows),
                "column_matches": match_columns(all_columns),
            }
        elif suffix in {".sav", ".zsav", ".por"}:
            import pyreadstat
            frame, meta = pyreadstat.read_sav(path, metadataonly=False)
            return {
                "format": "spss",
                "rows": int(len(frame)),
                "columns": [str(c) for c in frame.columns],
                "column_labels": {str(k): str(v) for k, v in zip(meta.column_names, meta.column_labels)},
                "column_matches": match_columns([str(c) for c in frame.columns]),
            }
        else:
            return {"format": suffix.lstrip("."), "structured_table_inspected": False}
        columns = [str(c) for c in frame.columns]
        return {
            "format": suffix.lstrip("."),
            "rows": int(len(frame)),
            "columns": columns,
            "column_matches": match_columns(columns),
            "missing_fraction_by_column": {str(c): round(float(frame[c].isna().mean()), 6) for c in frame.columns},
            "unique_count_by_candidate_id_column": {
                str(c): int(frame[c].nunique(dropna=True))
                for c in frame.columns
                if c in sum(match_columns(columns).values(), []) and frame[c].nunique(dropna=True) <= max(len(frame), 1)
            },
        }
    except Exception as exc:
        return {"format": suffix.lstrip("."), "inspection_error": f"{type(exc).__name__}:{exc}"}


def inspect_text(path: Path) -> dict:
    suffix = path.suffix.lower()
    if suffix not in {".r", ".rmd", ".py", ".ipynb", ".md", ".txt", ".json", ".yml", ".yaml"}:
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()
    return {
        "text_size_chars": len(text),
        "license_mentions": sorted(set(re.findall(r"\b(?:cc[- ]by(?:[- ]sa)?(?:[- ]4\.0)?|mit license|apache[- ]2\.0|gpl[- ]?3|bsd[- ]?3)\b", lower))),
        "code_language": suffix.lstrip("."),
        "data_loading_signals": [token for token in ["read.csv", "read_csv", "read_excel", "read_sav", "readrds", "load(", "pd.read_", "haven::read"] if token in lower],
        "availability_terms": [token for token in ["data availability", "codebook", "preregistration", "materials", "analysis code"] if token in lower],
    }


def download_file(session: requests.Session, row: dict, destination: Path) -> dict:
    url = row.get("download_url")
    if not url:
        return {"download_status": "no_download_url"}
    requested_host = (urlparse(url).hostname or "").lower()
    if not host_allowed(requested_host):
        return {"download_status": "requested_host_not_allowed", "requested_host": requested_host}
    response = session.get(url, timeout=(45, 600), allow_redirects=True, stream=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if not host_allowed(final_host):
        response.close()
        return {"download_status": "redirect_host_not_allowed", "requested_host": requested_host, "final_host": final_host}
    if response.status_code != 200:
        response.close()
        return {"download_status": "http_error", "http_status": response.status_code, "final_url": response.url}
    total = 0
    with destination.open("wb") as sink:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_SINGLE_FILE_BYTES:
                response.close()
                destination.unlink(missing_ok=True)
                return {"download_status": "single_file_limit_exceeded", "bytes_seen": total}
            sink.write(chunk)
    return {
        "download_status": "downloaded",
        "requested_host": requested_host,
        "final_host": final_host,
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": (response.headers.get("content-type") or "").lower(),
        "size_bytes_downloaded": total,
        "sha256": sha256(destination),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--node-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    download_dir = args.output / "downloaded"
    download_dir.mkdir(exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-osf-file-audit/1.0 (lawful public research archive; no code execution)"})
    node_url = f"https://api.osf.io/v2/nodes/{args.node_id}/"
    node_payload = get_json(session, node_url)
    (args.output / "node.json").write_text(json.dumps(node_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    attrs = node_payload.get("data", {}).get("attributes", {})
    providers, inventory = enumerate_files(session, args.node_id)
    (args.output / "providers.json").write_text(json.dumps(providers, ensure_ascii=False, indent=2), encoding="utf-8")

    total_downloaded = 0
    audit_rows = []
    for index, row in enumerate(inventory, start=1):
        item = dict(row)
        if row.get("kind") != "file":
            audit_rows.append(item)
            continue
        declared_size = row.get("size_bytes") or 0
        if declared_size and declared_size > MAX_SINGLE_FILE_BYTES:
            item["download_status"] = "declared_single_file_limit_exceeded"
            audit_rows.append(item)
            continue
        if total_downloaded + int(declared_size or 0) > MAX_TOTAL_DOWNLOAD_BYTES:
            item["download_status"] = "total_download_budget_exceeded"
            audit_rows.append(item)
            continue
        suffix = Path(row.get("name") or "file").suffix
        local_name = f"{index:04d}_{re.sub(r'[^A-Za-z0-9._-]+', '_', row.get('name') or 'file')}"
        destination = download_dir / local_name
        download_result = download_file(session, row, destination)
        item.update(download_result)
        if download_result.get("download_status") == "downloaded":
            total_downloaded += destination.stat().st_size
            item["local_file"] = str(destination.relative_to(args.output))
            item["table_audit"] = inspect_table(destination)
            item["text_audit"] = inspect_text(destination)
        audit_rows.append(item)

    file_rows = [row for row in audit_rows if row.get("kind") == "file"]
    downloaded_rows = [row for row in file_rows if row.get("download_status") == "downloaded"]
    table_rows = [row for row in downloaded_rows if row.get("table_audit", {}).get("rows") is not None or row.get("table_audit", {}).get("total_rows") is not None]
    combined_matches: dict[str, set[str]] = {key: set() for key in COLUMN_GROUPS}
    for row in table_rows:
        matches = row.get("table_audit", {}).get("column_matches", {})
        for key, values in matches.items():
            combined_matches.setdefault(key, set()).update(values)
    participant_level_candidate = bool(combined_matches.get("participant_id"))
    trial_level_candidate = participant_level_candidate and bool(combined_matches.get("trial_id"))
    reliance_recomputable_candidate = bool(combined_matches.get("ai_advice")) and bool(combined_matches.get("ai_correctness")) and bool(combined_matches.get("final_decision"))
    switch_recomputable_candidate = reliance_recomputable_candidate and bool(combined_matches.get("initial_decision"))

    summary = {
        "node_id": args.node_id,
        "title": attrs.get("title"),
        "description": attrs.get("description"),
        "public": attrs.get("public"),
        "category": attrs.get("category"),
        "date_created": attrs.get("date_created"),
        "date_modified": attrs.get("date_modified"),
        "registration": attrs.get("registration"),
        "preprint": attrs.get("preprint"),
        "current_user_permissions": attrs.get("current_user_permissions"),
        "provider_count": len(providers),
        "inventory_objects": len(audit_rows),
        "file_count": len(file_rows),
        "downloaded_file_count": len(downloaded_rows),
        "downloaded_bytes": total_downloaded,
        "download_status_counts": dict(Counter(row.get("download_status", "not_applicable") for row in file_rows)),
        "file_extensions": dict(Counter(Path(row.get("name") or "").suffix.lower() for row in file_rows)),
        "structured_table_files": len(table_rows),
        "combined_column_matches": {key: sorted(values) for key, values in combined_matches.items()},
        "participant_level_candidate": participant_level_candidate,
        "trial_level_candidate": trial_level_candidate,
        "reliance_metrics_recomputable_candidate": reliance_recomputable_candidate,
        "right_wrong_switch_recomputable_candidate": switch_recomputable_candidate,
        "code_executed": False,
        "validation_status": "audited" if attrs.get("public") is True and file_rows else "needs_review",
        "important_note": "Candidate flags are based on field names only and require manual semantic verification before upgrading evidence status.",
    }
    (args.output / "file_inventory.json").write_text(json.dumps(audit_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (args.output / "file_manifest.csv").open("w", newline="", encoding="utf-8") as stream:
        fields = ["file_id", "provider", "kind", "name", "materialized_path", "size_bytes", "date_created", "date_modified", "download_status", "final_url", "content_type", "size_bytes_downloaded", "sha256", "local_file"]
        writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(audit_rows)
    print(json.dumps(summary, indent=2))
    if summary["validation_status"] != "audited":
        raise SystemExit("osf_project_not_fully_auditable")


if __name__ == "__main__":
    main()
