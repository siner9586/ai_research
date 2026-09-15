from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {
        "paper_id": "doi:10.1177/1555343418799601",
        "title": "The Role of Trust and Automation in an Intelligence Analyst Decisional Guidance Paradigm",
        "doi": "10.1177/1555343418799601",
        "url": "https://journals.sagepub.com/doi/pdf/10.1177/1555343418799601",
        "license_note": "Article author note states U.S. federal government work/public domain; publisher page also displays rights and permissions information.",
    },
    {
        "paper_id": "doi:10.1177/0018720818781224",
        "title": "The Effect of Cognitive Load and Task Complexity on Automation Bias in Electronic Prescribing",
        "doi": "10.1177/0018720818781224",
        "url": "https://journals.sagepub.com/doi/pdf/10.1177/0018720818781224",
        "license_note": "Publisher-copyrighted restricted-access article; archive only if the unauthenticated endpoint lawfully serves a real PDF.",
    },
]

ALLOWED_HOSTS = {
    "journals.sagepub.com",
    "uk.sagepub.com",
    "us.sagepub.com",
    "sagepub.com",
    "static-content.springer.com",
}
MAX_BYTES = 50 * 1024 * 1024
PAYWALL_MARKERS = (
    "get full access",
    "purchase access",
    "institutional access",
    "sign in",
    "log in",
    "access options",
    "subscribe",
)


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        return {**target, "fulltext_status": "retryable", "error": f"host_not_allowed:{requested_host}"}

    try:
        response = session.get(target["url"], allow_redirects=True, stream=True, timeout=(30, 180))
    except Exception as exc:
        return {**target, "fulltext_status": "retryable", "error": f"{type(exc).__name__}:{exc}"}

    final_host = (urlparse(response.url).hostname or "").lower()
    base = {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": (response.headers.get("content-type") or "").lower(),
        "redirect_host": final_host,
    }
    if final_host not in ALLOWED_HOSTS:
        return {**base, "fulltext_status": "retryable", "error": f"redirect_host_not_allowed:{final_host}"}
    if response.status_code in {401, 402, 403}:
        return {**base, "fulltext_status": "paywalled_not_accessed", "error": f"access_status:{response.status_code}"}
    if response.status_code >= 400:
        return {**base, "fulltext_status": "retryable", "error": f"http_status:{response.status_code}"}

    chunks = []
    total = 0
    for chunk in response.iter_content(1024 * 1024):
        if not chunk:
            continue
        total += len(chunk)
        if total > MAX_BYTES:
            return {**base, "fulltext_status": "retryable", "error": "file_too_large"}
        chunks.append(chunk)
    body = b"".join(chunks)
    base["bytes_received"] = len(body)

    if body[:5] != b"%PDF-":
        html = body[:2_000_000].decode("utf-8", errors="ignore").lower()
        marker = next((m for m in PAYWALL_MARKERS if m in html), None)
        if marker:
            return {**base, "fulltext_status": "paywalled_not_accessed", "error": f"html_access_page:{marker}"}
        return {**base, "fulltext_status": "retryable", "error": f"not_pdf_magic:{body[:16]!r}"}

    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", target["paper_id"]) + ".pdf"
    path = out / filename
    path.write_bytes(body)
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages[: min(pages, 10)]:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(text_parts)
    tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_ratio = sum(t in norm(text) for t in tokens) / max(1, len(tokens))
    doi_match = target["doi"].lower() in text.lower()
    if not (doi_match or title_ratio >= 0.45):
        return {
            **base,
            "fulltext_status": "needs_manual_title_review",
            "local_file": filename,
            "sha256": hash_file(path),
            "page_count": pages,
            "title_match_ratio": round(title_ratio, 4),
            "doi_match": doi_match,
        }
    return {
        **base,
        "fulltext_status": "oa_or_publicly_served_pdf_verified",
        "local_file": filename,
        "sha256": hash_file(path),
        "page_count": pages,
        "title_match_ratio": round(title_ratio, 4),
        "doi_match": doi_match,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-sage-audit/1.0 (lawful research access; no authentication bypass)"})
    results = [audit_one(session, target, args.output) for target in TARGETS]
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    counts: dict[str, int] = {}
    for item in results:
        counts[item["fulltext_status"]] = counts.get(item["fulltext_status"], 0) + 1
    summary = {"targets": len(results), "status_counts": counts, "results": results}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
