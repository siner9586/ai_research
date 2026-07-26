from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

TARGETS = [
    {
        "paper_id": "doi:10.1145/3757451",
        "title": "The AI is uncertain, so am I. What now? Navigating Shortcomings of Uncertainty Representations in Human-AI Collaboration with Capability-focused Guidance",
        "doi": "10.1145/3757451",
        "url": "https://refubium.fu-berlin.de/bitstream/handle/fub188/50614/3757451.pdf?isAllowed=y&save=y&sequence=1",
        "version": "repository_copy",
        "license": "CC BY-SA 4.0",
    },
    {
        "paper_id": "doi:10.1016/j.landig.2025.100912",
        "title": "The impact of artificial intelligence-driven decision support on uncertain antimicrobial prescribing: a randomised, multimethod study",
        "doi": "10.1016/j.landig.2025.100912",
        "url": "https://www.thelancet.com/action/showPdf?pii=S2589-7500%2825%2900094-9",
        "version": "publishedVersion",
        "license": "Creative Commons open access",
    },
    {
        "paper_id": "doi:10.1016/j.chbah.2023.100009",
        "title": "Choosing between human and algorithmic advisors: The role of responsibility sharing",
        "doi": "10.1016/j.chbah.2023.100009",
        "url": "https://assets-eu.researchsquare.com/files/rs-2324206/v1/3698756e-934e-41fe-b621-147be00da96d.pdf?c=1675837808",
        "version": "preprint",
        "license": "CC BY 4.0",
    },
    {
        "paper_id": "doi:10.1609/aaai.v38i16.29783",
        "title": "Learning Robust Rationales for Model Explainability: A Guidance-Based Approach",
        "doi": "10.1609/aaai.v38i16.29783",
        "url": "https://ojs.aaai.org/index.php/AAAI/article/view/29783/31352",
        "version": "publishedVersion",
        "license": "AAAI open access",
    },
]

ALLOWED_HOSTS = {
    "refubium.fu-berlin.de",
    "www.thelancet.com",
    "thelancet.com",
    "assets-eu.researchsquare.com",
    "ojs.aaai.org",
    "aaai.org",
}
MAX_BYTES = 100 * 1024 * 1024
PAYWALL_MARKERS = ("get access", "purchase", "institutional access", "sign in", "enable javascript")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def audit_one(session: requests.Session, target: dict, output: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        return {**target, "fulltext_status": "retryable", "error": f"host_not_allowed:{requested_host}"}
    try:
        response = session.get(target["url"], timeout=(90, 300), stream=True, allow_redirects=True)
    except Exception as exc:
        return {**target, "fulltext_status": "retryable", "error": f"{type(exc).__name__}:{exc}"}
    final_host = (urlparse(response.url).hostname or "").lower()
    base = {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": (response.headers.get("content-type") or "").lower(),
        "final_host": final_host,
    }
    if final_host not in ALLOWED_HOSTS:
        return {**base, "fulltext_status": "retryable", "error": f"redirect_host_not_allowed:{final_host}"}
    if response.status_code in {401, 402, 403, 429}:
        return {**base, "fulltext_status": "retryable", "error": f"access_or_rate_status:{response.status_code}"}
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
        marker = next((marker for marker in PAYWALL_MARKERS if marker in html), None)
        return {**base, "fulltext_status": "retryable", "error": f"not_pdf_magic:{body[:16]!r};marker={marker}"}
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", target["paper_id"]) + ".pdf"
    path = output / name
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
    title_tokens = [token for token in norm(target["title"]).split() if len(token) > 3]
    title_ratio = sum(token in norm(text) for token in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    status = "oa_pdf_verified" if pages > 0 and (doi_match or title_ratio >= 0.45) else "needs_manual_title_review"
    return {
        **base,
        "fulltext_status": status,
        "local_file": name,
        "size_bytes": len(body),
        "sha256": sha256(path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_ratio, 4),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    retry = Retry(total=3, connect=3, read=3, status=2, backoff_factor=3, status_forcelist=(429, 500, 502, 503, 504), allowed_methods=frozenset({"GET", "HEAD"}), raise_on_status=False)
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "open-evidence-priority-fulltext/1.1 (lawful OA research audit)"})
    results = [audit_one(session, target, args.output) for target in TARGETS]
    counts: dict[str, int] = {}
    for result in results:
        counts[result["fulltext_status"]] = counts.get(result["fulltext_status"], 0) + 1
    summary = {"targets": len(results), "status_counts": counts, "results": results}
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if counts.get("oa_pdf_verified", 0) == 0:
        raise SystemExit("No PDF was verified")


if __name__ == "__main__":
    main()
