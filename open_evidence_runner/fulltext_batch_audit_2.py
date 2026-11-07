from __future__ import annotations

import argparse
import csv
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
        "license": "CC BY 4.0",
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
    {
        "paper_id": "arxiv:2602.04003",
        "title": "When AI Persuades: Adversarial Explanation Attacks on Human Trust in AI-Assisted Decision Making",
        "doi": "10.48550/arxiv.2602.04003",
        "url": "https://arxiv.org/pdf/2602.04003v3",
        "version": "preprint-v3",
        "license": "CC BY 4.0",
    },
    {
        "paper_id": "arxiv:2603.18895",
        "title": "From Accuracy to Readiness: Metrics and Benchmarks for Human-AI Decision-Making",
        "doi": "10.48550/arxiv.2603.18895",
        "url": "https://arxiv.org/pdf/2603.18895",
        "version": "preprint",
        "license": "arXiv-hosted",
    },
    {
        "paper_id": "doi:10.1609/aaai.v40i47.41457",
        "title": "Calibrating Reliance: Addressing Misuse and Disuse in AI-Based Second-Opinion Systems for Medical Diagnosis",
        "doi": "10.1609/aaai.v40i47.41457",
        "url": "https://ojs.aaai.org/index.php/AAAI/article/download/41457/45418",
        "version": "publisher",
        "license": "AAAI open proceedings",
    },
]

ALLOWED_HOSTS = {
    "www.nature.com",
    "nature.com",
    "www.jmir.org",
    "jmir.org",
    "arxiv.org",
    "export.arxiv.org",
    "www.frontiersin.org",
    "frontiersin.org",
    "aclanthology.org",
    "www.aclanthology.org",
    "ojs.aaai.org",
}
MAX_BYTES = 100 * 1024 * 1024
REPOSITORY_PATTERN = re.compile(
    r"https?://(?:www\.)?(?:github\.com|osf\.io|zenodo\.org|huggingface\.co|figshare\.com|dataverse\.[^/\s]+|doi\.org/10\.5281/zenodo\.)/[^\s<>)\]}]+",
    re.IGNORECASE,
)
AVAILABILITY_PATTERNS = [
    re.compile(r"(?:data|code|materials?|software) availability[^\n]{0,500}", re.IGNORECASE),
    re.compile(r"(?:data|code|materials?|software) (?:are|is|were|was) available[^\n]{0,500}", re.IGNORECASE),
    re.compile(r"(?:source code|dataset|data set) (?:can be found|is available|are available)[^\n]{0,500}", re.IGNORECASE),
]


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def safe_filename(paper_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", paper_id) + ".pdf"


def is_error_page(prefix: bytes) -> bool:
    lowered = prefix[:4096].lower()
    return any(marker in lowered for marker in (b"<!doctype html", b"<html", b"access denied", b"cloudflare", b"captcha"))


def extract_text(reader: PdfReader) -> str:
    pages = len(reader.pages)
    indexes = list(range(min(8, pages)))
    if pages > 8:
        indexes.extend(range(max(8, pages - 4), pages))
    chunks: list[str] = []
    for index in sorted(set(indexes)):
        try:
            chunks.append(reader.pages[index].extract_text() or "")
        except Exception:
            continue
    return "\n".join(chunks)


def audit_one(session: requests.Session, target: dict, output: Path) -> dict:
    parsed = urlparse(target["url"])
    if parsed.scheme != "https":
        raise RuntimeError(f"non_https_url:{target['url']}")
    host = (parsed.hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")

    response = session.get(target["url"], timeout=(30, 240), allow_redirects=True, stream=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()
    content_type = (response.headers.get("content-type") or "").lower()

    path = output / safe_filename(target["paper_id"])
    total = 0
    prefix = b""
    with path.open("wb") as handle:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            if len(prefix) < 4096:
                prefix += chunk[: 4096 - len(prefix)]
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("file_too_large")
            handle.write(chunk)

    if prefix[:5] != b"%PDF-":
        path.unlink(missing_ok=True)
        if is_error_page(prefix):
            raise RuntimeError(f"html_or_access_control_page:content_type={content_type}")
        raise RuntimeError(f"not_pdf_magic:{prefix[:16]!r};content_type={content_type}")

    reader = PdfReader(str(path))
    page_count = len(reader.pages)
    if page_count < 1:
        path.unlink(missing_ok=True)
        raise RuntimeError("pdf_has_no_pages")
    text = extract_text(reader)
    normalized_text = norm(text)
    title_tokens = [token for token in norm(target["title"]).split() if len(token) > 3]
    title_ratio = sum(token in normalized_text for token in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    validation_status = "verified" if doi_match or title_ratio >= 0.55 else "needs_manual_title_review"

    repository_links = sorted({match.rstrip(".,;:") for match in REPOSITORY_PATTERN.findall(text)})
    statements: list[str] = []
    for pattern in AVAILABILITY_PATTERNS:
        for match in pattern.findall(text):
            cleaned = " ".join(match.split())
            if cleaned and cleaned not in statements:
                statements.append(cleaned[:500])

    return {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "redirect_count": len(response.history),
        "http_status": response.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": file_sha256(path),
        "page_count": page_count,
        "doi_match": doi_match,
        "title_match_ratio": round(title_ratio, 4),
        "repository_links": repository_links,
        "availability_statements": statements[:10],
        "validation_status": validation_status,
        "local_file": path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "open-evidence-fulltext-audit/2.0 (lawful open-access research archive; contact via repository)",
            "Accept": "application/pdf,text/html;q=0.8,*/*;q=0.5",
        }
    )

    results: list[dict] = []
    seen_sha: dict[str, str] = {}
    for target in TARGETS:
        try:
            result = audit_one(session, target, args.output)
            digest = result["sha256"]
            result["duplicate_of"] = seen_sha.get(digest)
            seen_sha.setdefault(digest, target["paper_id"])
            results.append(result)
        except Exception as exc:
            results.append(
                {
                    **target,
                    "validation_status": "retryable",
                    "error": f"{type(exc).__name__}:{exc}",
                }
            )

    (args.output / "fulltext_audit.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    repository_report = [
        {
            "paper_id": row["paper_id"],
            "repository_links": row.get("repository_links", []),
            "availability_statements": row.get("availability_statements", []),
            "validation_status": row["validation_status"],
        }
        for row in results
    ]
    (args.output / "repository_and_availability_audit.json").write_text(
        json.dumps(repository_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    with (args.output / "sha256_manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "paper_id",
                "local_file",
                "sha256",
                "size_bytes",
                "page_count",
                "validation_status",
                "duplicate_of",
                "final_url",
                "license",
            ],
        )
        writer.writeheader()
        for row in results:
            writer.writerow({key: row.get(key) for key in writer.fieldnames})

    verified = sum(row.get("validation_status") == "verified" for row in results)
    manual = sum(row.get("validation_status") == "needs_manual_title_review" for row in results)
    retryable = len(results) - verified - manual
    duplicates = sum(bool(row.get("duplicate_of")) for row in results)
    summary = {
        "targets": len(results),
        "verified": verified,
        "needs_manual_title_review": manual,
        "retryable": retryable,
        "duplicates": duplicates,
        "completed": True,
        "all_targets_finalized": retryable == 0 and manual == 0,
    }
    (args.output / "completion_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if verified == 0:
        raise SystemExit("No fulltext was independently verified")


if __name__ == "__main__":
    main()
