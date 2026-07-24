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
        "paper_id": "doi:10.1038/s41598-026-34983-y",
        "title": "Examining human reliance on artificial intelligence in decision making",
        "doi": "10.1038/s41598-026-34983-y",
        "url": "https://www.nature.com/articles/s41598-026-34983-y.pdf",
        "version": "publisher",
        "license": "CC BY 4.0",
    },
    {
        "paper_id": "doi:10.1145/3449287",
        "title": "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making",
        "doi": "10.1145/3449287",
        "url": "https://arxiv.org/pdf/2102.09692",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.1145/3706598.3714020",
        "title": "Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies",
        "doi": "10.1145/3706598.3714020",
        "url": "https://arxiv.org/pdf/2502.08554",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.1145/3742413.3789136",
        "title": "Adjust for Trust: Mitigating Trust-Induced Inappropriate Reliance on AI Assistance",
        "doi": "10.1145/3742413.3789136",
        "url": "https://arxiv.org/pdf/2502.13321v2",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
]

ALLOWED_HOSTS = {"www.nature.com", "nature.com", "arxiv.org", "export.arxiv.org"}
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
