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
        "candidate_id": "doi:10.2196/78757",
        "title": "Stakeholder Criteria for Trust in Artificial Intelligence-Based Computer Perception Tools in Health Care: Qualitative Interview Study",
        "doi": "10.2196/78757",
        "urls": ["https://www.jmir.org/2025/1/e78757/PDF"],
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "candidate_id": "doi:10.1145/3757451",
        "title": "The AI is uncertain, so am I. What now? Navigating Shortcomings of Uncertainty Representations in Human-AI Collaboration with Capability-focused Guidance",
        "doi": "10.1145/3757451",
        "urls": ["https://refubium.fu-berlin.de/bitstream/handle/fub188/50614/3757451.pdf?isAllowed=y&sequence=1"],
        "version": "institutional_repository",
        "license": "CC BY-SA",
    },
    {
        "candidate_id": "doi:10.1016/j.landig.2025.100912",
        "title": "The impact of artificial intelligence-driven decision support on uncertain antimicrobial prescribing: a randomised, multimethod study",
        "doi": "10.1016/j.landig.2025.100912",
        "urls": [
            "https://www.thelancet.com/action/showPdf?pii=S2589-7500%2825%2900094-9",
            "https://www.sciencedirect.com/science/article/pii/S2589750025000949/pdfft?isDTMRedir=true&download=true",
        ],
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "candidate_id": "doi:10.3390/bs15101370",
        "title": "Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis",
        "doi": "10.3390/bs15101370",
        "urls": ["https://www.mdpi.com/2076-328X/15/10/1370/pdf"],
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "candidate_id": "doi:10.3390/bs14100964",
        "title": "Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks",
        "doi": "10.3390/bs14100964",
        "urls": ["https://www.mdpi.com/2076-328X/14/10/964/pdf"],
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "candidate_id": "doi:10.2196/47031",
        "title": "Trust in and Acceptance of Artificial Intelligence Applications in Medicine: Mixed Methods Study",
        "doi": "10.2196/47031",
        "urls": [
            "https://humanfactors.jmir.org/2024/1/e47031/PDF",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC10831593/bin/humanfactors_v11i1e47031.pdf",
        ],
        "version": "publisher",
        "license": "CC BY",
    },
]

ALLOWED_HOSTS = {
    "www.jmir.org", "jmir.org", "humanfactors.jmir.org", "asset.jmir.pub", "assets.jmir.pub",
    "refubium.fu-berlin.de",
    "www.thelancet.com", "thelancet.com", "www.sciencedirect.com", "sciencedirect.com",
    "www.mdpi.com", "mdpi.com", "mdpi-res.com",
    "pmc.ncbi.nlm.nih.gov", "ftp.ncbi.nlm.nih.gov",
}
MAX_BYTES = 100 * 1024 * 1024
URL_RE = re.compile(r"https?://[^\s<>()\]\[{}\"']+", re.I)
AVAILABILITY_PATTERNS = [
    re.compile(r".{0,180}\bdata availability\b.{0,700}", re.I | re.S),
    re.compile(r".{0,180}\bcode availability\b.{0,700}", re.I | re.S),
    re.compile(r".{0,180}\bavailability of data and materials\b.{0,700}", re.I | re.S),
    re.compile(r".{0,180}\bsupplementary (?:material|materials|information)\b.{0,700}", re.I | re.S),
]
REPO_DOMAINS = ("github.com", "osf.io", "zenodo.org", "huggingface.co", "figshare.com", "dataverse", "dryad")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def download_one(session: requests.Session, url: str, path: Path) -> dict:
    requested_host = (urlparse(url).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")
    r = session.get(url, timeout=(30, 240), allow_redirects=True, stream=True)
    final_host = (urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    r.raise_for_status()
    content_type = (r.headers.get("content-type") or "").lower()
    total = 0
    with path.open("wb") as f:
        for chunk in r.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("file_too_large")
            f.write(chunk)
    magic = path.read_bytes()[:5]
    if magic != b"%PDF-":
        path.unlink(missing_ok=True)
        raise RuntimeError(f"not_pdf_magic:{magic!r};content_type={content_type}")
    return {
        "requested_url": url,
        "final_url": r.url,
        "requested_host": requested_host,
        "final_host": final_host,
        "http_status": r.status_code,
        "content_type": content_type,
        "size_bytes": total,
    }


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", target["candidate_id"]) + ".pdf"
    path = out / filename
    attempts = []
    transfer = None
    for url in target["urls"]:
        try:
            transfer = download_one(session, url, path)
            break
        except Exception as exc:
            attempts.append({"url": url, "error": f"{type(exc).__name__}:{exc}"})
            path.unlink(missing_ok=True)
    if transfer is None:
        raise RuntimeError(json.dumps(attempts, ensure_ascii=False))
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    page_text = []
    for page in reader.pages:
        try:
            page_text.append(page.extract_text() or "")
        except Exception:
            page_text.append("")
    text = "\n".join(page_text)
    normalized_text = norm(text)
    title_tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_match_ratio = sum(t in normalized_text for t in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    statements = []
    for pattern in AVAILABILITY_PATTERNS:
        for match in pattern.finditer(text):
            value = re.sub(r"\s+", " ", match.group(0)).strip()[:900]
            if value and value not in statements:
                statements.append(value)
            if len(statements) >= 10:
                break
        if len(statements) >= 10:
            break
    repository_urls = []
    for raw_url in URL_RE.findall(text):
        value = raw_url.rstrip(".,;:)")
        host = (urlparse(value).hostname or "").lower()
        if any(domain in host for domain in REPO_DOMAINS) and value not in repository_urls:
            repository_urls.append(value)
        if len(repository_urls) >= 30:
            break
    return {
        **target,
        **transfer,
        "attempt_failures_before_success": attempts,
        "page_count": pages,
        "sha256": sha256(path),
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": status,
        "local_file": filename,
        "availability_statements": statements,
        "repository_urls": repository_urls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-behavior-fulltext/1.0 (lawful OA research archive)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = sum(r.get("validation_status") == "verified" for r in results)
    manual = sum(r.get("validation_status") == "needs_manual_title_review" for r in results)
    retryable = sum(r.get("validation_status") == "retryable" for r in results)
    summary = {"targets": len(results), "verified": verified, "manual_review": manual, "retryable": retryable}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No lawful OA PDF was verified")


if __name__ == "__main__":
    main()
