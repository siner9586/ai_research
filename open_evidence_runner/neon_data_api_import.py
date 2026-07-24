from __future__ import annotations

import argparse
import base64
import gzip
import json
import math
import os
import time
import zipfile
from pathlib import Path
from typing import Any, Iterable

import requests

AUDIENCE = "neon-open-evidence-import"
TABLE = "open_evidence_import_staging"
REPOSITORY = "siner9586/ai_research"
REPOSITORY_ID = "1258287537"


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


def validate_claims(claims: dict[str, Any], allowed_workflow: str) -> str:
    expected = {
        "aud": AUDIENCE,
        "sub": f"repo:{REPOSITORY}:pull_request",
        "repository": REPOSITORY,
        "repository_id": REPOSITORY_ID,
    }
    for key, value in expected.items():
        if str(claims.get(key)) != value:
            raise RuntimeError(f"Unexpected OIDC claim {key}")
    safe_name = Path(allowed_workflow).name
    if safe_name != allowed_workflow or not safe_name.endswith(".yml"):
        raise RuntimeError("allowed_workflow must be a YAML filename without path components")
    workflow_ref = str(claims.get("workflow_ref", ""))
    required_prefix = f"{REPOSITORY}/.github/workflows/{safe_name}@refs/pull/"
    if not workflow_ref.startswith(required_prefix):
        raise RuntimeError(
            f"Unexpected workflow_ref; required prefix {required_prefix!r}"
        )
    return workflow_ref


def json_safe(value: Any) -> Any:
    """Recursively replace non-finite floats before PostgreSQL JSONB transport."""
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    return value


def strict_json_bytes(value: Any) -> bytes:
    return json.dumps(
        json_safe(value),
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")


def find_master(root: Path, source: str, pattern: str | None = None) -> Path:
    if pattern:
        matches = list(root.glob(pattern))
        if len(matches) == 1:
            return matches[0]
        raise FileNotFoundError(f"Expected one file matching {pattern}, found {len(matches)} under {root}")
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
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"JSONL record {line_number} must be an object")
            safe = json_safe(value)
            strict_json_bytes(safe)
            yield safe


def source_record_id(source: str, payload: dict[str, Any]) -> str:
    if payload.get("candidate_id"):
        value = str(payload["candidate_id"])
    elif source == "arXiv":
        value = str(payload.get("arxiv_id") or payload.get("source_external_id") or "")
    elif source == "Semantic Scholar":
        value = str(payload.get("s2_paper_id") or payload.get("source_external_id") or "")
    else:
        value = str(
            payload.get("source_external_id")
            or payload.get("doi_normalized")
            or payload.get("pmid")
            or ""
        )
    if not value:
        raise ValueError(f"Missing stable source record identifier for {source}")
    return value


def chunks(
    records: Iterable[dict[str, Any]],
    max_rows: int = 200,
    max_bytes: int = 2_500_000,
):
    batch: list[dict[str, Any]] = []
    size = 2
    for record in records:
        encoded = strict_json_bytes(record)
        if batch and (len(batch) >= max_rows or size + len(encoded) + 1 > max_bytes):
            yield batch
            batch = []
            size = 2
        batch.append(record)
        size += len(encoded) + 1
    if batch:
        yield batch


def post_batch(
    session: requests.Session,
    endpoint: str,
    token: str,
    rows: list[dict[str, Any]],
) -> None:
    response = session.post(
        f"{endpoint}/{TABLE}?on_conflict=source_name,source_record_id",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates,return=minimal",
        },
        data=strict_json_bytes(rows),
        timeout=(30, 180),
    )
    if response.status_code not in (200, 201, 204):
        raise RuntimeError(
            f"Data API insert failed HTTP {response.status_code}: {response.text[:1000]}"
        )


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
        raise RuntimeError(
            f"Data API count failed HTTP {response.status_code}: {response.text[:1000]}"
        )
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
    parser.add_argument(
        "--allowed-workflow",
        default="open-evidence-neon-import.yml",
        help="Exact workflow filename accepted in the OIDC workflow_ref claim.",
    )
    args = parser.parse_args()

    token = request_oidc_token()
    claims = decode_claims(token)
    workflow_ref = validate_claims(claims, args.allowed_workflow)

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
            "payload": json_safe(payload),
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
        "allowed_workflow": args.allowed_workflow,
        "json_standard": "RFC8259_no_NaN_or_Infinity",
        "completed": exact_count == attempted,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, indent=2, allow_nan=False), encoding="utf-8"
    )
    print(json.dumps(report, indent=2, allow_nan=False))
    if not report["completed"]:
        raise SystemExit("Staging count does not match attempted record count")


if __name__ == "__main__":
    main()
