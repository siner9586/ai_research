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
    {"paper_id":"doi:10.1038/s41598-021-87480-9","title":"Humans Rely More on Algorithms Than Social Influence as a Task Becomes More Difficult","doi":"10.1038/s41598-021-87480-9","url":"https://www.nature.com/articles/s41598-021-87480-9.pdf","version":"publisher","license":"CC BY 4.0"},
    {"paper_id":"doi:10.2196/29386","title":"The Impact of Explanations on Layperson Trust in Artificial Intelligence-Driven Symptom Checker Apps: Experimental Study","doi":"10.2196/29386","url":"https://www.jmir.org/2021/11/e29386/PDF","version":"publisher","license":"CC BY"},
    {"paper_id":"arxiv:1801.04099","title":"Trust-Aware Decision Making for Human-Robot Collaboration: Model Learning and Planning","doi":"10.48550/arxiv.1801.04099","url":"https://arxiv.org/pdf/1801.04099","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2001.07641","title":"Deceptive AI Explanations: Creation and Detection","doi":"10.48550/arxiv.2001.07641","url":"https://arxiv.org/pdf/2001.07641","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.3389/fnhum.2018.00309","title":"Learning From the Slips of Others: Neural Correlates of Trust in Automated Agents","doi":"10.3389/fnhum.2018.00309","url":"https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2018.00309/pdf","version":"publisher","license":"CC BY"},
    {"paper_id":"doi:10.1145/3377325.3377498","title":"Proxy Tasks and Subjective Measures Can Be Misleading in Evaluating Explainable AI Systems","doi":"10.1145/3377325.3377498","url":"https://arxiv.org/pdf/2001.08298","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.1145/3375627.3375833","title":"How do I fool you? Manipulating User Trust via Misleading Black Box Explanations","doi":"10.1145/3375627.3375833","url":"https://arxiv.org/pdf/1911.06473","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.18653/v1/2020.acl-main.491","title":"Evaluating Explainable AI: Which Algorithmic Explanations Help Users Predict Model Behavior?","doi":"10.18653/v1/2020.acl-main.491","url":"https://aclanthology.org/2020.acl-main.491.pdf","version":"publisher","license":"ACL Anthology open"},
    {"paper_id":"doi:10.18653/v1/2020.findings-emnlp.390","title":"Leakage-Adjusted Simulatability: Can Models Generate Non-Trivial Explanations of Their Behavior in Natural Language?","doi":"10.18653/v1/2020.findings-emnlp.390","url":"https://aclanthology.org/2020.findings-emnlp.390.pdf","version":"publisher","license":"ACL Anthology open"},
    {"paper_id":"arxiv:2006.14779","title":"Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance","doi":"10.48550/arxiv.2006.14779","url":"https://arxiv.org/pdf/2006.14779","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.31234/osf.io/d4r9t","title":"Does Explainable Artificial Intelligence Improve Human Decision-Making?","doi":"10.31234/osf.io/d4r9t","url":"https://arxiv.org/pdf/2006.11194","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:1909.06907","title":"X-ToM: Explaining with Theory-of-Mind for Gaining Justified Human Trust","doi":"10.48550/arxiv.1909.06907","url":"https://arxiv.org/pdf/1909.06907","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:1811.07901","title":"On Human Predictions with Explanations and Predictions of Machine Learning Models: A Case Study on Deception Detection","doi":"10.48550/arxiv.1811.07901","url":"https://arxiv.org/pdf/1811.07901","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.3389/frobt.2021.652776","title":"Adaptive Cognitive Mechanisms to Maintain Calibrated Trust and Reliance in Automation","doi":"10.3389/frobt.2021.652776","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.652776/pdf","version":"publisher","license":"CC BY"},
]

ALLOWED_HOSTS = {
    "www.nature.com", "nature.com", "www.jmir.org", "jmir.org",
    "arxiv.org", "export.arxiv.org", "aclanthology.org", "www.aclanthology.org",
    "www.frontiersin.org", "frontiersin.org"
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


def filename_for(paper_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", paper_id) + ".pdf"


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")
    response = session.get(target["url"], timeout=(30, 240), allow_redirects=True, stream=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()
    content_type = (response.headers.get("content-type") or "").lower()
    path = out / filename_for(target["paper_id"])
    total = 0
    with path.open("wb") as f:
        for chunk in response.iter_content(1024 * 1024):
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
    extracted = []
    for page in reader.pages[: min(10, pages)]:
        try:
            extracted.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(extracted)
    normalized_text = norm(text)
    title_tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    title_match_ratio = sum(token in normalized_text for token in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    return {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "http_status": response.status_code,
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
    session.headers.update({"User-Agent":"open-evidence-fulltext-audit/2.0 (lawful OA research archive)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status":"retryable", "error":f"{type(exc).__name__}:{exc}"})
    verified = sum(r.get("validation_status") == "verified" for r in results)
    review = sum(r.get("validation_status") == "needs_manual_title_review" for r in results)
    retryable = len(results) - verified - review
    summary = {"targets":len(results), "verified":verified, "manual_review":review, "retryable":retryable}
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No fulltext was verified")


if __name__ == "__main__":
    main()
