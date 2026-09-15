from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import requests

from audit_osf_public_files import (
    API,
    MAX_TOTAL_BYTES,
    download,
    file_attributes,
    inspect_file,
    paginate,
    recurse_files,
    safe_name,
    save_json,
    should_download,
)

TARGETS = {
    "ym3ug": {"experiment": 1, "doi": "10.1038/s41598-021-87480-9"},
    "hyz6d": {"experiment": 2, "doi": "10.1038/s41598-021-87480-9"},
    "vgh9k": {"experiment": 3, "doi": "10.1038/s41598-021-87480-9"},
}


def relation_href(resource: dict[str, Any], name: str) -> str | None:
    relationship = ((resource.get("data") or {}).get("relationships") or {}).get(name) or {}
    links = relationship.get("links") or {}
    related = links.get("related") or {}
    if isinstance(related, dict):
        return related.get("href")
    if isinstance(related, str):
        return related
    return None


def get_json(session: requests.Session, url: str) -> dict[str, Any]:
    response = session.get(url, timeout=(30, 180), headers={"Accept": "application/vnd.api+json, application/json"})
    response.raise_for_status()
    value = response.json()
    if not isinstance(value, dict):
        raise RuntimeError(f"Expected object from {url}")
    return value


def resolve_resource(session: requests.Session, guid: str, raw: Path) -> tuple[str, dict[str, Any]]:
    diagnostic: dict[str, Any] = {"guid": guid, "attempts": []}
    endpoints = [
        f"{API}/guids/{guid}/",
        f"{API}/nodes/{guid}/",
        f"{API}/registrations/{guid}/",
        f"{API}/preprints/{guid}/",
    ]
    for endpoint in endpoints:
        try:
            response = session.get(endpoint, timeout=(30, 180), headers={"Accept": "application/vnd.api+json, application/json"})
            diagnostic["attempts"].append({"url": endpoint, "status": response.status_code, "content_type": response.headers.get("Content-Type")})
            if response.status_code >= 400:
                continue
            value = response.json()
            save_json(raw / f"resolve_{len(diagnostic['attempts']):02d}.json", value)
            if endpoint.endswith(f"/guids/{guid}/"):
                referent = relation_href(value, "referent")
                if referent:
                    resource = get_json(session, referent)
                    save_json(raw / "resolved_referent.json", resource)
                    save_json(raw / "resolution_diagnostic.json", diagnostic)
                    return referent, resource
            else:
                save_json(raw / "resolution_diagnostic.json", diagnostic)
                return endpoint, value
        except Exception as exc:
            diagnostic["attempts"].append({"url": endpoint, "error": f"{type(exc).__name__}:{exc}"})
    save_json(raw / "resolution_diagnostic.json", diagnostic)
    raise RuntimeError("OSF GUID could not be resolved as guid, node, registration, or preprint")


def files_provider_url(resource: dict[str, Any]) -> str | None:
    direct = relation_href(resource, "files")
    if direct:
        return direct
    for relation in ("registered_from", "root", "node"):
        related = relation_href(resource, relation)
        if not related:
            continue
        try:
            linked = get_json(requests.Session(), related)
        except Exception:
            continue
        direct = relation_href(linked, "files")
        if direct:
            return direct
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--guid", choices=sorted(TARGETS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.output
    raw = root / "raw_api"
    files_dir = root / "files"
    root.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/2.1 OSF-GUID-audit"})
    report: dict[str, Any] = {
        "guid": args.guid,
        "target": TARGETS[args.guid],
        "completed": False,
        "files_discovered": 0,
        "files_downloaded": 0,
        "participant_level_verified": False,
        "trial_level_verified": False,
        "errors": [],
    }
    try:
        resource_url, resource = resolve_resource(session, args.guid, raw)
        data = resource.get("data") or {}
        report["resource_url"] = resource_url
        report["resource_type"] = data.get("type")
        report["resource_id"] = data.get("id")
        report["title"] = (data.get("attributes") or {}).get("title")
        providers_url = files_provider_url(resource)
        if not providers_url:
            raise RuntimeError("Resolved OSF resource did not expose a files relationship")
        providers = paginate(session, providers_url, None, raw, "providers")
        all_files: list[dict[str, Any]] = []
        for index, provider in enumerate(providers, start=1):
            row = file_attributes(provider)
            provider_files_url = row.get("files_url") or (provider.get("links") or {}).get("new_folder")
            if provider_files_url:
                all_files.extend(recurse_files(session, provider_files_url, None, raw, f"provider_{index:02d}"))
        report["providers"] = len(providers)
        report["files_discovered"] = len(all_files)

        downloaded = []
        total = 0
        for index, row in enumerate(all_files, start=1):
            if not should_download(row) or not row.get("download_url"):
                continue
            expected_size = row.get("size") if isinstance(row.get("size"), int) else 0
            if total + expected_size > MAX_TOTAL_BYTES:
                report["errors"].append({"name": row.get("name"), "error": "project_download_budget_exceeded"})
                continue
            output = files_dir / f"{index:04d}_{safe_name(str(row.get('name') or row.get('id')))}"
            try:
                transfer = download(session, row["download_url"], output, None)
                audit = inspect_file(output)
            except Exception as exc:
                report["errors"].append({"name": row.get("name"), "error": f"{type(exc).__name__}:{exc}"})
                continue
            total += transfer["size_bytes"]
            downloaded.append({"osf_file": row, "local_file": str(output.relative_to(root)), "transfer": transfer, "audit": audit})
        report["downloaded"] = downloaded
        report["files_downloaded"] = len(downloaded)
        report["downloaded_bytes"] = total
        report["completed"] = True
        report["status"] = "files_audited" if downloaded else "resolved_no_selected_files"
    except Exception as exc:
        report["status"] = "retryable_or_access_limited"
        report["errors"].append({"error": f"{type(exc).__name__}:{exc}"})
    save_json(root / "osf_guid_audit.json", report)
    print(json.dumps({key: report.get(key) for key in ("guid", "resource_type", "status", "files_discovered", "files_downloaded")}, indent=2))


if __name__ == "__main__":
    main()
