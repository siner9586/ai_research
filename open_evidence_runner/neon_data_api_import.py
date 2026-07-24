from __future__ import annotations

import argparse
import base64
import gzip
import json
import os
import time
import zipfile
from pathlib import Path
from typing import Any, Iterable

import requests

AUDIENCE = "neon-open-evidence-import"
TABLE = "open_evidence_import_staging"


def request_oidc_token() -> str:
    request_url = os.environ["ACTIONS_ID_TOKEN_REQUEST_URL"]
    request_token = os.environ["ACTIONS_ID_TOKEN_REQUEST_TOKEN"]
    separator = "&" if "?" in request_url else "?"
    response = requests.get(
        f"{request_url}{separator}audience={AUDIENCE}",
        headers={"Authorization": f"bearer {request_token}"},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["value"]


def decode_claims(token: str) -> dict[str, Any]:
    payload = token.split(".")[1]
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.urlsafe_b64decode(payload))


def find_master(root: Path, source: str, pattern: str | None = None) -> Path:
    if pattern:
        matches = list(root.glob(pattern))
        if matches:
            return matches[0]
        raise FileNotFoundError(f"No file matching {pattern} under {root}")
    patterns = {
        "arXiv": ["**/arxiv_all_paper_master.jsonl.gz"],
        "Semantic Scholar": ["**/semantic_scholar_all_paper_master.jsonl.gz"],
    }
    if source not in patterns:
        raise ValueError(f"A master pattern is required for source {source}")
    for candidate_pattern in patterns[source]:
        matches = list(root.glob(candidate_pattern))
        if matches:
            return matches[0]
    for archive_path in root.glob("**/*.zip"):
        try:
            with zipfile.ZipFile(archive_path) as archive:
                suffix = patterns[source][0].replace("**/", "")
                names = [name for name in archive.namelist() if name.endswith(suffix)]
                if names:
                    output = root / Path(names[0]).name
                    output.write_bytes(archive.read(names[0]))
                    return output
        except zipfile.BadZipFile:
            continue
    raise FileNotFoundError(f"No aggregate master found for {source} under {root}")


def iter_jsonl_gz(path: Path) -> Iterable[dict[str, Any]]:
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                value = json.loads(line)
                if not isinstance(value, dict):
                    raise ValueError("JSONL records must be objects")
                yield value


def source_record_id(source: str, payload: dict[str, Any]) -> str:
    if payload.get("candidate_id"):
        return str(payload["candidate_id"])
    if source == "arXiv":
        return str(payload.get("arxiv_id") or payload.get("source_external_id"))
    if source == "Semantic Scholar":
        return str(payload.get("s2_paper_id") or payload.get("source_external_id"))
    return str(payload.get("source_external_id") or payload.get("doi_normalized") or payload.get("pmid"))


def chunks(records: Iterable[dict[str, Any]], max_rows: int = 200, max_bytes: int = 2_500_000):
    batch: list[dict[str, Any]] = []
    size = 2
    for record in records:
        encoded = json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        if batch and (len(batch) >= max_rows or size + len(encoded) + 1 > max_bytes):
            yield batch
            batch = []
            size = 2
        batch.append(record)
        size += len(encoded) + 1
    if batch:
        yield batch


def post_batch(session: requests.Session, endpoint: str, token: str, rows: list[dict[str, Any]]) -> None:
    response = session.post(
        f"{endpoint}/{TABLE}?on_conflict=source_name,source_record_id",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates,return=minimal",
        },
        data=json.dumps(rows, ensure_ascii=False, separators=(",", ":")).encode("utf-8"),
        timeout=(30, 180),
    )
    if response.status_code not in (200, 201, 204):
        raise RuntimeError(f"Data API insert failed HTTP {response.status_code}: {response.text[:1000]}")


def count_source(session: requests.Session, endpoint: str, token: str, source: str) -> int:
    response = session.get(
        f"{endpoint}/{TABLE}",
        params={"source_name": f"eq.{source}", "select": "source_record_id", "limit": "1"},
        headers={
            "Authorization": f"Bearer {token}",
            "Prefer": "count=exact",
            "Range": "0-0",
        },
        timeout=(30, 120),
    )
    if response.status_code not in (200, 206):
        raise RuntimeError(f"Data API count failed HTTP {response.status_code}: {response.text[:1000]}")
    content_range = response.headers.get("Content-Range", "")
    if "/" not in content_range:
        raise RuntimeError(f"Missing exact count in Content-Range: {content_range}")
    return int(content_range.rsplit("/", 1)[1])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--master-pattern")
    parser.add_argument("--batch-id")
    args = parser.parse_args()

    token = request_oidc_token()
    claims = decode_claims(token)
    expected = {
        "aud": AUDIENCE,
        "sub": "repo:siner9586/ai_research:pull_request",
        "repository": "siner9586/ai_research",
        "repository_id": "1258287537",
    }
    for key, value in expected.items():
        if str(claims.get(key)) != value:
            raise RuntimeError(f"Unexpected OIDC claim {key}")
    workflow_ref = str(claims.get("workflow_ref", ""))
    if not workflow_ref.startswith(
        "siner9586/ai_research/.github/workflows/open-evidence-neon-import.yml@refs/pull/"
    ):
        raise RuntimeError("Unexpected workflow_ref")

    master = find_master(args.artifact_root, args.source, args.master_pattern)
    batch_id = args.batch_id or f"{args.source.lower().replace(' ', '-')}-aggregate-v1"
    session = requests.Session()
    attempted = 0
    batches = 0
    started = time.time()
    staged_rows = (
        {
            "batch_id": batch_id,
            "source_name": args.source,
            "source_record_id": source_record_id(args.source, payload),
            "payload": payload,
        }
        for payload in iter_jsonl_gz(master)
    )
    for batch in chunks(staged_rows):
        post_batch(session, args.endpoint.rstrip("/"), token, batch)
        attempted += len(batch)
        batches += 1
        if batches % 25 == 0:
            print(json.dumps({"source": args.source, "attempted": attempted, "batches": batches}))
        time.sleep(0.05)

    exact_count = count_source(session, args.endpoint.rstrip("/"), token, args.source)
    report = {
        "source": args.source,
        "batch_id": batch_id,
        "master": str(master),
        "records_attempted": attempted,
        "staging_exact_count": exact_count,
        "batches": batches,
        "elapsed_seconds": round(time.time() - started, 3),
        "oidc_repository": claims.get("repository"),
        "oidc_repository_id": claims.get("repository_id"),
        "oidc_workflow_ref": workflow_ref,
        "completed": exact_count == attempted,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if not report["completed"]:
        raise SystemExit("Staging count does not match attempted record count")


if __name__ == "__main__":
    main()
