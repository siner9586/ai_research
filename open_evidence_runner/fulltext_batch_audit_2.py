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
        "paper_id": "doi:10.1038/s41598-021-87480-9",
        "title": "Humans Rely More on Algorithms Than Social Influence as a Task Becomes More Difficult",
        "doi": "10.1038/s41598-021-87480-9",
        "url": "https://www.nature.com/articles/s41598-021-87480-9.pdf",
        "version": "publisher",
        "license": "CC BY 4.0",
    },
    {
        "paper_id": "doi:10.2196/29386",
        "title": "The Impact of Explanations on Layperson Trust in Artificial Intelligence-Driven Symptom Checker Apps: Experimental Study",
        "doi": "10.2196/29386",
        "url": "https://www.jmir.org/2021/11/e29386/PDF",
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "paper_id": "doi:10.18653/v1/2020.acl-main.491",
        "title": "Evaluating Explainable AI: Which Algorithmic Explanations Help Users Predict Model Behavior?",
        "doi": "10.18653/v1/2020.acl-main.491",
        "url": "https://aclanthology.org/2020.acl-main.491.pdf",
        "version": "publisher",
        "license": "ACL Anthology open access",
    },
    {
        "paper_id": "doi:10.3389/fnhum.2018.00309",
        "title": "Learning From the Slips of Others: Neural Correlates of Trust in Automated Agents",
        "doi": "10.3389/fnhum.2018.00309",
        "url": "https://www.frontiersin.org/articles/10.3389/fnhum.2018.00309/pdf",
        "version": "publisher",
        "license": "CC BY",
    },
]

ALLOWED_HOSTS = {
    "www.nature.com", "nature.com",
    "www.jmir.org", "jmir.org",
    "aclanthology.org", "www.aclanthology.org",
    "www.frontiersin.org", "frontiersin.org",
    "public-pages-files-2025.frontiersin.org",
}
MAX_BYTES = 80 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    host = (urlparse(target["url"]).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")
    r = session.get(target["url"], timeout=(30, 180), allow_redirects=True, stream=True)
    final_host = (urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    r.raise_for_status()
    content_type = (r.headers.get("content-type") or "").lower()
    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", target["paper_id"]) + ".pdf"
    path = out / filename
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
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    sample = []
    for page in reader.pages[: min(8, pages)]:
        try:
            sample.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(sample)
    title_tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_match_ratio = sum(t in norm(text) for t in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    return {
        **target,
        "requested_url": target["url"],
        "final_url": r.url,
        "http_status": r.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": sha256(path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": status,
        "local_file": path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-fulltext-audit/1.0 (research; lawful OA only)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    completed = sum(r.get("validation_status") == "verified" for r in results)
    summary = {"targets": len(results), "verified": completed, "retryable_or_review": len(results) - completed}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if completed == 0:
        raise SystemExit("No fulltext was verified")


if __name__ == "__main__":
    main()
