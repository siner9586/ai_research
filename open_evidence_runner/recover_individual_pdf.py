from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

ALLOWED_HOSTS = {
    "arxiv.org", "export.arxiv.org",
    "aclanthology.org", "www.aclanthology.org",
    "link.springer.com", "cognitiveresearchjournal.springeropen.com",
}
MAX_BYTES = 100 * 1024 * 1024


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--doi", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--license", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    requested_host = (urlparse(args.url).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise SystemExit(f"host_not_allowed:{requested_host}")

    session = requests.Session()
    session.headers.update({
        "User-Agent": "open-evidence-individual-pdf-recovery/1.0 (lawful OA archive; no access-control bypass)",
        "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.1",
    })
    response = None
    last_error = None
    for attempt in range(1, 4):
        try:
            response = session.get(args.url, stream=True, allow_redirects=True, timeout=(45, 600))
            if response.status_code in {429, 500, 502, 503, 504}:
                response.close()
                raise RuntimeError(f"retryable_http_{response.status_code}")
            response.raise_for_status()
            break
        except Exception as exc:
            last_error = exc
            if attempt < 3:
                time.sleep(2 ** attempt)
    if response is None or not response.ok:
        raise SystemExit(f"request_failed:{type(last_error).__name__}:{last_error}")

    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise SystemExit(f"redirect_host_not_allowed:{final_host}")

    file_name = re.sub(r"[^A-Za-z0-9._-]+", "_", args.paper_id) + ".pdf"
    pdf_path = args.output / file_name
    total = 0
    with pdf_path.open("wb") as sink:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise SystemExit("file_too_large")
            sink.write(chunk)

    content_type = (response.headers.get("content-type") or "").lower()
    magic = pdf_path.read_bytes()[:5]
    if magic != b"%PDF-":
        prefix = pdf_path.read_bytes()[:200]
        raise SystemExit(f"not_pdf_magic:{magic!r};content_type={content_type};prefix={prefix!r}")

    reader = PdfReader(str(pdf_path))
    pages = len(reader.pages)
    sample = []
    for page in reader.pages[: min(12, pages)]:
        try:
            sample.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(sample)
    normalized_text = norm(text)
    title_tokens = [token for token in norm(args.title).split() if len(token) > 3]
    title_match_ratio = sum(token in normalized_text for token in title_tokens) / max(1, len(title_tokens))
    doi_match = args.doi.lower() in text.lower()
    actual_sha = sha256(pdf_path)
    exact_hash_match = actual_sha == args.expected_sha256.lower()
    validation_status = "verified_exact_sha256" if exact_hash_match else (
        "verified_current_legal_version" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_review"
    )
    result = {
        "paper_id": args.paper_id,
        "title": args.title,
        "doi": args.doi,
        "requested_url": args.url,
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": actual_sha,
        "expected_sha256": args.expected_sha256.lower(),
        "exact_hash_match": exact_hash_match,
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "version": args.version,
        "license": args.license,
        "validation_status": validation_status,
        "local_file": file_name,
        "code_executed": False,
    }
    (args.output / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if validation_status == "needs_manual_review":
        raise SystemExit("pdf_identity_not_verified")


if __name__ == "__main__":
    main()
