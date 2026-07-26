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
        "candidate_id": "doi:10.3390/bs15101370",
        "pmcid": "PMC12561693",
        "title": "Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis",
        "doi": "10.3390/bs15101370",
        "urls": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC12561693/bin/behavsci-15-01370.pdf",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12561693/bin/behavsci-15-01370.pdf",
        ],
        "license": "CC BY 4.0",
    },
    {
        "candidate_id": "doi:10.3390/bs14100964",
        "pmcid": "PMC11505338",
        "title": "Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks",
        "doi": "10.3390/bs14100964",
        "urls": [
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11505338/bin/behavsci-14-00964.pdf",
            "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11505338/bin/behavsci-14-00964.pdf",
        ],
        "license": "CC BY 4.0",
    },
]
ALLOWED_HOSTS = {"pmc.ncbi.nlm.nih.gov", "www.ncbi.nlm.nih.gov", "cdn.ncbi.nlm.nih.gov"}
MAX_BYTES = 40 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def fetch_pdf(session: requests.Session, urls: list[str], path: Path) -> dict:
    failures = []
    for url in urls:
        try:
            requested_host = (urlparse(url).hostname or "").lower()
            if requested_host not in ALLOWED_HOSTS:
                raise RuntimeError(f"host_not_allowed:{requested_host}")
            r = session.get(url, timeout=(30, 180), allow_redirects=True, stream=True)
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
            if path.read_bytes()[:5] != b"%PDF-":
                preview = path.read_bytes()[:80]
                path.unlink(missing_ok=True)
                raise RuntimeError(f"not_pdf_magic:{preview!r};content_type={content_type}")
            return {
                "requested_url": url,
                "final_url": r.url,
                "http_status": r.status_code,
                "content_type": content_type,
                "size_bytes": total,
                "prior_failures": failures,
            }
        except Exception as exc:
            failures.append({"url": url, "error": f"{type(exc).__name__}:{exc}"})
            path.unlink(missing_ok=True)
    raise RuntimeError(json.dumps(failures, ensure_ascii=False))


def audit_one(session: requests.Session, target: dict, output: Path) -> dict:
    path = output / (re.sub(r"[^A-Za-z0-9._-]+", "_", target["candidate_id"]) + ".pdf")
    transfer = fetch_pdf(session, target["urls"], path)
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            text_parts.append("")
    text = "\n".join(text_parts)
    normalized = norm(text)
    tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_ratio = sum(t in normalized for t in tokens) / max(1, len(tokens))
    doi_match = target["doi"].lower() in text.lower()
    if pages < 1 or not (doi_match or title_ratio >= 0.55):
        raise RuntimeError(f"title_or_doi_mismatch:pages={pages};ratio={title_ratio};doi={doi_match}")
    return {
        **target,
        **transfer,
        "page_count": pages,
        "sha256": sha256(path),
        "doi_match": doi_match,
        "title_match_ratio": round(title_ratio, 4),
        "validation_status": "verified",
        "version": "pmc_open_access_copy",
        "local_file": path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-pmc-fallback/1.0 (lawful OA research archive; contact via repository)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = sum(x.get("validation_status") == "verified" for x in results)
    summary = {"targets": len(results), "verified": verified, "retryable": len(results) - verified}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No PMC PDF was verified")


if __name__ == "__main__":
    main()
