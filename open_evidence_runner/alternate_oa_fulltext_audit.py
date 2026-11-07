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

TARGETS = [
    {
        "paper_id": "doi:10.1145/3757451",
        "title": "The AI is uncertain, so am I. What now? Navigating Shortcomings of Uncertainty Representations in Human-AI Collaboration with Capability-focused Guidance",
        "doi": "10.1145/3757451",
        "url": "https://refubium.fu-berlin.de/bitstream/handle/fub188/50614/3757451.pdf?isAllowed=y&sequence=1",
        "version": "institutional_repository_manuscript",
        "license": "CC BY-SA 4.0",
        "source": "Refubium",
    },
    {
        "paper_id": "doi:10.3390/bs14100964",
        "title": "Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks",
        "doi": "10.3390/bs14100964",
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11505338/fullTextPDF",
        "version": "published_version",
        "license": "CC BY 4.0",
        "source": "Europe PMC",
    },
    {
        "paper_id": "doi:10.3390/bs15101370",
        "title": "Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis",
        "doi": "10.3390/bs15101370",
        "url": "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12561693/fullTextPDF",
        "version": "published_version",
        "license": "CC BY 4.0",
        "source": "Europe PMC",
    },
    {
        "paper_id": "doi:10.1016/j.chbah.2023.100009",
        "title": "Choosing between human and algorithmic advisors: The role of responsibility sharing",
        "doi": "10.1016/j.chbah.2023.100009",
        "url": "https://www.researchsquare.com/article/rs-2324206/v1.pdf",
        "version": "preprint",
        "license": "CC BY 4.0",
        "source": "Research Square",
        "alternate_doi": "10.21203/rs.3.rs-2324206/v1",
    },
    {
        "paper_id": "doi:10.1609/aaai.v38i16.29783",
        "title": "Learning Robust Rationales for Model Explainability: A Guidance-Based Approach",
        "doi": "10.1609/aaai.v38i16.29783",
        "url": "https://ojs.aaai.org/index.php/AAAI/article/download/29783/31352",
        "version": "published_version",
        "license": "AAAI open access",
        "source": "AAAI",
    },
]

ALLOWED_HOSTS = {
    "refubium.fu-berlin.de",
    "www.ebi.ac.uk",
    "ebi.ac.uk",
    "www.researchsquare.com",
    "researchsquare.com",
    "assets-eu.researchsquare.com",
    "assets.researchsquare.com",
    "ojs.aaai.org",
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


def safe_filename(paper_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", paper_id) + ".pdf"


def request_with_retry(session: requests.Session, url: str) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            response = session.get(url, stream=True, allow_redirects=True, timeout=(45, 600))
            if response.status_code in {429, 500, 502, 503, 504}:
                response.close()
                raise RuntimeError(f"retryable_http_{response.status_code}")
            response.raise_for_status()
            return response
        except Exception as exc:
            last_error = exc
            if attempt < 3:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"request_failed_after_3_attempts:{type(last_error).__name__}:{last_error}")


def audit_one(session: requests.Session, target: dict, output: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")
    response = request_with_retry(session, target["url"])
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    content_type = (response.headers.get("content-type") or "").lower()
    path = output / safe_filename(target["paper_id"])
    total = 0
    with path.open("wb") as sink:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("file_too_large")
            sink.write(chunk)
    magic = path.read_bytes()[:5]
    if magic != b"%PDF-":
        prefix = path.read_bytes()[:160]
        path.unlink(missing_ok=True)
        raise RuntimeError(f"not_pdf_magic:{magic!r};content_type={content_type};prefix={prefix!r}")
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages[: min(12, pages)]:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(text_parts)
    normalized = norm(text)
    title_tokens = [token for token in norm(target["title"]).split() if len(token) > 3]
    title_match_ratio = sum(token in normalized for token in title_tokens) / max(1, len(title_tokens))
    identifiers = [target["doi"].lower()]
    if target.get("alternate_doi"):
        identifiers.append(target["alternate_doi"].lower())
    doi_match = any(identifier in text.lower() for identifier in identifiers)
    validation_status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    return {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": sha256(path),
        "page_count": pages,
        "doi_or_alternate_doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": validation_status,
        "local_file": path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "open-evidence-alternate-oa/1.0 (lawful research archive; no access-control bypass)",
        "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.1",
    })
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    verified = sum(item.get("validation_status") == "verified" for item in results)
    manual = sum(item.get("validation_status") == "needs_manual_title_review" for item in results)
    retryable = len(results) - verified - manual
    summary = {"targets": len(results), "verified": verified, "manual_review": manual, "retryable": retryable}
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("no_alternate_oa_fulltext_verified")


if __name__ == "__main__":
    main()
