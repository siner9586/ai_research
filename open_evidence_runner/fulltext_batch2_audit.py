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
        "paper_id": "arxiv:1801.04099",
        "title": "Trust-Aware Decision Making for Human-Robot Collaboration: Model Learning and Planning",
        "doi": "10.48550/arxiv.1801.04099",
        "url": "https://arxiv.org/pdf/1801.04099",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "arxiv:2001.07641",
        "title": "Deceptive AI Explanations: Creation and Detection",
        "doi": "10.48550/arxiv.2001.07641",
        "url": "https://arxiv.org/pdf/2001.07641",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.3389/fnhum.2018.00309",
        "title": "Learning From the Slips of Others: Neural Correlates of Trust in Automated Agents",
        "doi": "10.3389/fnhum.2018.00309",
        "url": "https://www.frontiersin.org/articles/10.3389/fnhum.2018.00309/pdf",
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "paper_id": "doi:10.3389/frobt.2021.652776",
        "title": "Adaptive Cognitive Mechanisms to Maintain Calibrated Trust and Reliance in Automation",
        "doi": "10.3389/frobt.2021.652776",
        "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.652776/pdf",
        "version": "publisher",
        "license": "CC BY",
    },
    {
        "paper_id": "doi:10.1145/3377325.3377498",
        "title": "Proxy Tasks and Subjective Measures Can Be Misleading in Evaluating Explainable AI Systems",
        "doi": "10.1145/3377325.3377498",
        "url": "https://arxiv.org/pdf/2001.08298",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.1145/3375627.3375833",
        "title": "How do I fool you? Manipulating User Trust via Misleading Black Box Explanations",
        "doi": "10.1145/3375627.3375833",
        "url": "https://arxiv.org/pdf/1911.06473",
        "version": "preprint",
        "license": "arXiv-hosted",
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
        "paper_id": "doi:10.18653/v1/2020.findings-emnlp.390",
        "title": "Leakage-Adjusted Simulatability: Can Models Generate Non-Trivial Explanations of Their Behavior in Natural Language?",
        "doi": "10.18653/v1/2020.findings-emnlp.390",
        "url": "https://aclanthology.org/2020.findings-emnlp.390.pdf",
        "version": "publisher",
        "license": "ACL Anthology open access",
    },
    {
        "paper_id": "arxiv:2006.14779",
        "title": "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance",
        "doi": "10.48550/arxiv.2006.14779",
        "url": "https://arxiv.org/pdf/2006.14779",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.31234/osf.io/d4r9t",
        "title": "Does Explainable Artificial Intelligence Improve Human Decision-Making?",
        "doi": "10.31234/osf.io/d4r9t",
        "url": "https://arxiv.org/pdf/2006.11194",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "arxiv:1909.06907",
        "title": "X-ToM: Explaining with Theory-of-Mind for Gaining Justified Human Trust",
        "doi": "10.48550/arxiv.1909.06907",
        "url": "https://arxiv.org/pdf/1909.06907",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "arxiv:1811.07901",
        "title": "On Human Predictions with Explanations and Predictions of Machine Learning Models: A Case Study on Deception Detection",
        "doi": "10.48550/arxiv.1811.07901",
        "url": "https://arxiv.org/pdf/1811.07901",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
]

ALLOWED_HOSTS = {
    "www.nature.com", "nature.com", "media.springernature.com", "static-content.springer.com",
    "www.jmir.org", "jmir.org", "asset.jmir.pub", "assets.jmir.pub",
    "arxiv.org", "export.arxiv.org",
    "www.frontiersin.org", "frontiersin.org",
    "aclanthology.org", "www.aclanthology.org",
}
MAX_BYTES = 100 * 1024 * 1024
URL_RE = re.compile(r"https?://[^\s<>()\]\[{}\"']+", re.I)
AVAILABILITY_PATTERNS = [
    re.compile(r".{0,180}\bdata availability\b.{0,500}", re.I | re.S),
    re.compile(r".{0,180}\bcode availability\b.{0,500}", re.I | re.S),
    re.compile(r".{0,180}\bavailability of data and materials\b.{0,500}", re.I | re.S),
    re.compile(r".{0,180}\bsupplementary (?:material|materials|information)\b.{0,500}", re.I | re.S),
    re.compile(r".{0,180}\bsource code\b.{0,400}", re.I | re.S),
]
REPOSITORY_DOMAINS = ("github.com", "osf.io", "zenodo.org", "huggingface.co", "figshare.com", "dataverse", "dryad")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def clean_statement(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()[:700]


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")
    r = session.get(target["url"], timeout=(30, 240), allow_redirects=True, stream=True)
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
    all_text = []
    for page in reader.pages:
        try:
            all_text.append(page.extract_text() or "")
        except Exception:
            all_text.append("")
    text = "\n".join(all_text)
    normalized_text = norm(text)
    title_tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_match_ratio = sum(t in normalized_text for t in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    statements = []
    for pattern in AVAILABILITY_PATTERNS:
        for match in pattern.finditer(text):
            value = clean_statement(match.group(0))
            if value and value not in statements:
                statements.append(value)
            if len(statements) >= 8:
                break
        if len(statements) >= 8:
            break
    repository_urls = []
    for raw_url in URL_RE.findall(text):
        url = raw_url.rstrip(".,;:)")
        host = (urlparse(url).hostname or "").lower()
        if any(domain in host for domain in REPOSITORY_DOMAINS) and url not in repository_urls:
            repository_urls.append(url)
        if len(repository_urls) >= 30:
            break
    return {
        **target,
        "requested_url": target["url"],
        "final_url": r.url,
        "requested_host": requested_host,
        "final_host": final_host,
        "http_status": r.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": sha256(path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": status,
        "local_file": path.name,
        "availability_statements": statements,
        "repository_urls": repository_urls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-fulltext-audit/2.0 (lawful OA research archive)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    availability = [
        {
            "paper_id": r["paper_id"],
            "availability_statements": r.get("availability_statements", []),
            "repository_urls": r.get("repository_urls", []),
        }
        for r in results
    ]
    (args.output / "availability_and_repository_evidence.json").write_text(
        json.dumps(availability, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    verified = sum(r.get("validation_status") == "verified" for r in results)
    review = sum(r.get("validation_status") == "needs_manual_title_review" for r in results)
    retryable = sum(r.get("validation_status") == "retryable" for r in results)
    summary = {"targets": len(results), "verified": verified, "manual_review": review, "retryable": retryable}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No fulltext was verified")


if __name__ == "__main__":
    main()
