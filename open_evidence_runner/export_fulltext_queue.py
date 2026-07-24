from __future__ import annotations

import argparse
import base64
import csv
import json
import os
from pathlib import Path
from typing import Any

import requests

AUDIENCE = "neon-open-evidence-import"
TABLES = [
    "papers",
    "screening_decisions",
    "candidate_screening_decisions",
    "files",
    "oa_locations",
    "datasets",
    "repositories",
    "drive_objects",
]


def request_oidc_token() -> tuple[str, dict[str, Any]]:
    request_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    separator = "&" if "?" in request_url else "?"
    response = requests.get(
        f"{request_url}{separator}audience={AUDIENCE}",
        headers={"Authorization": f"bearer {os.environ['ACTIONS_ID_TOKEN_REQUEST_TOKEN']}"},
        timeout=60,
    )
    response.raise_for_status()
    token = response.json()["value"]
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    claims = json.loads(base64.urlsafe_b64decode(payload))
    return token, claims


def fetch_table(session: requests.Session, endpoint: str, token: str, table: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    offset = 0
    page_size = 1000
    status_codes: list[int] = []
    while True:
        response = session.get(
            f"{endpoint.rstrip('/')}/{table}",
            params={"select": "*", "limit": page_size, "offset": offset},
            headers={"Authorization": f"Bearer {token}", "Prefer": "count=exact"},
            timeout=(30, 180),
        )
        status_codes.append(response.status_code)
        if response.status_code not in (200, 206):
            return [], {
                "table": table,
                "accessible": False,
                "status_code": response.status_code,
                "response_excerpt": response.text[:500],
                "status_codes": status_codes,
            }
        page = response.json()
        if not isinstance(page, list):
            raise RuntimeError(f"Unexpected response for {table}")
        rows.extend(page)
        if len(page) < page_size:
            break
        offset += len(page)
        if offset > 250000:
            raise RuntimeError(f"Safety row cap exceeded for {table}")
    return rows, {
        "table": table,
        "accessible": True,
        "rows": len(rows),
        "columns": sorted(rows[0]) if rows else [],
        "status_codes": status_codes,
    }


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, allow_nan=False, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    token, claims = request_oidc_token()
    workflow_ref = str(claims.get("workflow_ref", ""))
    if not workflow_ref.startswith("siner9586/ai_research/.github/workflows/open-evidence-neon-import.yml@refs/pull/"):
        raise RuntimeError("Unexpected workflow identity")

    session = requests.Session()
    diagnostics: list[dict[str, Any]] = []
    tables: dict[str, list[dict[str, Any]]] = {}
    for table in TABLES:
        rows, diagnostic = fetch_table(session, args.endpoint, token, table)
        diagnostics.append(diagnostic)
        if diagnostic.get("accessible"):
            tables[table] = rows
            write_jsonl(args.output / f"{table}.jsonl", rows)

    papers = {str(row.get("paper_id")): row for row in tables.get("papers", []) if row.get("paper_id")}
    selected: set[str] = set()
    for table in ("screening_decisions", "candidate_screening_decisions"):
        for row in tables.get(table, []):
            decision = str(row.get("final_decision") or row.get("decision") or "").lower()
            if decision in {"include", "uncertain", "pending_fulltext", "fulltext_review"}:
                paper_id = row.get("paper_id") or row.get("candidate_id")
                if paper_id and str(paper_id) in papers:
                    selected.add(str(paper_id))

    files_by_paper: dict[str, list[dict[str, Any]]] = {}
    for row in tables.get("files", []):
        if row.get("paper_id"):
            files_by_paper.setdefault(str(row["paper_id"]), []).append(row)
    oa_by_paper: dict[str, list[dict[str, Any]]] = {}
    for row in tables.get("oa_locations", []):
        if row.get("paper_id"):
            oa_by_paper.setdefault(str(row["paper_id"]), []).append(row)

    queue: list[dict[str, Any]] = []
    final_markers = {"oa_pdf_verified", "publisher_html_verified", "repository_manuscript_verified", "metadata_only", "paywalled_not_accessed", "not_found", "retracted", "access_requires_authorization"}
    for paper_id in sorted(selected):
        paper_files = files_by_paper.get(paper_id, [])
        statuses = {str(row.get("status") or row.get("validation_status") or row.get("fulltext_status") or "") for row in paper_files}
        if statuses & final_markers:
            continue
        paper = papers[paper_id]
        queue.append({
            "paper_id": paper_id,
            "title": paper.get("canonical_title") or paper.get("title"),
            "doi": paper.get("doi_normalized") or paper.get("doi"),
            "arxiv_id": paper.get("arxiv_id"),
            "pmid": paper.get("pmid"),
            "publication_year": paper.get("publication_year") or paper.get("year"),
            "existing_file_rows": paper_files,
            "oa_locations": oa_by_paper.get(paper_id, []),
        })

    pending_drive = []
    for row in tables.get("drive_objects", []):
        status = str(row.get("status") or row.get("upload_status") or "").lower()
        if status in {"pending", "retryable", "queued", "failed_transient"}:
            pending_drive.append(row)

    write_jsonl(args.output / "fulltext_queue.jsonl", queue)
    write_jsonl(args.output / "drive_pending_retryable.jsonl", pending_drive)
    summary = {
        "completed": True,
        "run_scope": "read_only_queue_export",
        "accessible_tables": [d["table"] for d in diagnostics if d.get("accessible")],
        "inaccessible_tables": [d["table"] for d in diagnostics if not d.get("accessible")],
        "selected_papers": len(selected),
        "fulltext_queue": len(queue),
        "drive_pending_retryable": len(pending_drive),
        "diagnostics": diagnostics,
        "oidc_repository": claims.get("repository"),
        "oidc_workflow_ref": workflow_ref,
    }
    (args.output / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
