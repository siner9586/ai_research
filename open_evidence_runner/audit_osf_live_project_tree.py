from __future__ import annotations

import argparse
import json
from collections import deque
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
    "fusx4": {"experiment": 1, "registration_guid": "ym3ug", "doi": "10.1038/s41598-021-87480-9"},
    "b7we5": {"experiment": 2, "registration_guid": "hyz6d", "doi": "10.1038/s41598-021-87480-9"},
    "6rjuz": {"experiment": 3, "registration_guid": "vgh9k", "doi": "10.1038/s41598-021-87480-9"},
}


def relation_href(data: dict[str, Any], name: str) -> str | None:
    relationship = (data.get("relationships") or {}).get(name) or {}
    related = (relationship.get("links") or {}).get("related") or {}
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--node-id", choices=sorted(TARGETS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.output
    raw = root / "raw_api"
    files_dir = root / "files"
    root.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/2.2 OSF-live-project-tree-audit"})
    target = TARGETS[args.node_id]
    queue = deque([args.node_id])
    seen_nodes: set[str] = set()
    nodes: list[dict[str, Any]] = []
    files: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    while queue:
        node_id = queue.popleft()
        if node_id in seen_nodes:
            continue
        seen_nodes.add(node_id)
        try:
            resource = get_json(session, f"{API}/nodes/{node_id}/")
            save_json(raw / f"node_{node_id}.json", resource)
        except Exception as exc:
            errors.append({"node_id": node_id, "stage": "node", "error": f"{type(exc).__name__}:{exc}"})
            continue
        data = resource.get("data") or {}
        attributes = data.get("attributes") or {}
        node_row = {
            "id": data.get("id"),
            "title": attributes.get("title"),
            "public": attributes.get("public"),
            "category": attributes.get("category"),
            "date_created": attributes.get("date_created"),
            "date_modified": attributes.get("date_modified"),
            "parent": relation_href(data, "parent"),
            "root": relation_href(data, "root"),
        }
        nodes.append(node_row)

        children_url = relation_href(data, "children") or f"{API}/nodes/{node_id}/children/"
        try:
            children = paginate(session, children_url, None, raw, f"children_{node_id}")
            for child in children:
                child_id = child.get("id")
                if child_id and child_id not in seen_nodes:
                    queue.append(str(child_id))
        except Exception as exc:
            errors.append({"node_id": node_id, "stage": "children", "error": f"{type(exc).__name__}:{exc}"})

        providers_url = relation_href(data, "files") or f"{API}/nodes/{node_id}/files/"
        try:
            providers = paginate(session, providers_url, None, raw, f"providers_{node_id}")
        except Exception as exc:
            errors.append({"node_id": node_id, "stage": "providers", "error": f"{type(exc).__name__}:{exc}"})
            continue
        for index, provider in enumerate(providers, start=1):
            provider_row = file_attributes(provider)
            provider_files_url = provider_row.get("files_url") or (provider.get("links") or {}).get("new_folder")
            if not provider_files_url:
                continue
            try:
                node_files = recurse_files(session, provider_files_url, None, raw, f"node_{node_id}_provider_{index:02d}")
            except Exception as exc:
                errors.append({"node_id": node_id, "stage": "file_tree", "error": f"{type(exc).__name__}:{exc}"})
                continue
            for row in node_files:
                files.append({"node_id": node_id, "node_title": attributes.get("title"), **row})

    selected = []
    total_bytes = 0
    for index, row in enumerate(files, start=1):
        if not should_download(row) or not row.get("download_url"):
            continue
        expected_size = row.get("size") if isinstance(row.get("size"), int) else 0
        if total_bytes + expected_size > MAX_TOTAL_BYTES:
            errors.append({"node_id": row.get("node_id"), "name": row.get("name"), "stage": "download", "error": "project_download_budget_exceeded"})
            continue
        output = files_dir / f"{index:04d}_{row['node_id']}_{safe_name(str(row.get('name') or row.get('id')))}"
        try:
            transfer = download(session, row["download_url"], output, None)
            audit = inspect_file(output)
        except Exception as exc:
            errors.append({"node_id": row.get("node_id"), "name": row.get("name"), "stage": "download", "error": f"{type(exc).__name__}:{exc}"})
            continue
        total_bytes += transfer["size_bytes"]
        selected.append({"osf_file": row, "local_file": str(output.relative_to(root)), "transfer": transfer, "audit": audit})

    report = {
        "target": target,
        "root_node_id": args.node_id,
        "nodes_discovered": nodes,
        "node_count": len(nodes),
        "files_discovered": len(files),
        "files_selected_and_downloaded": len(selected),
        "downloaded_bytes": total_bytes,
        "downloaded": selected,
        "errors": errors,
        "completed": True,
        "participant_level_verified": False,
        "trial_level_verified": False,
        "eligibility_note": "File-level audit completed. Participant/trial status remains false until statistical schemas and row structures are independently mapped.",
    }
    save_json(root / "osf_live_project_tree_audit.json", report)
    print(json.dumps({key: report[key] for key in ("root_node_id", "node_count", "files_discovered", "files_selected_and_downloaded", "downloaded_bytes")}, indent=2))


if __name__ == "__main__":
    main()
