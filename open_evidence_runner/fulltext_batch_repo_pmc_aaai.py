from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {
        "paper_id": "doi:10.1016/j.ijhcs.2026.103775",
        "title": "Trust the Explanation or my Expectation? Effects of Output Accuracy and Explanations on Expectation Violations and Trust in AI-Supported Decisions",
        "doi": "10.1016/j.ijhcs.2026.103775",
        "url": "https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/42003/1/1-s2.0-S1071581926000509-main.pdf",
        "version": "publishedVersion",
        "license": "CC BY 4.0",
    },
    {
        "paper_id": "doi:10.1093/jamia/ocag082",
        "title": "Explainability in context: calibrating appropriate trust and reliance in artificial intelligence",
        "doi": "10.1093/jamia/ocag082",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13385988/pdf/",
        "version": "publishedVersion",
        "license": "PMC open-access article",
    },
    {
        "paper_id": "doi:10.1609/aaai.v32i1.11353",
        "title": "Building More Explainable Artificial Intelligence With Argumentation",
        "doi": "10.1609/aaai.v32i1.11353",
        "url": "https://ojs.aaai.org/index.php/AAAI/article/view/11353/11212",
        "version": "publishedVersion",
        "license": "AAAI open",
    },
]

ALLOWED_HOSTS = {
    "publikationen.sulb.uni-saarland.de",
    "pmc.ncbi.nlm.nih.gov",
    "ojs.aaai.org",
}
MAX_BYTES = 80 * 1024 * 1024


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def audit_one(session: requests.Session, target: dict, output: Path) -> dict:
    requested_host = (urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")

    response = session.get(target["url"], timeout=(30, 180), allow_redirects=True, stream=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()

    content_type = (response.headers.get("content-type") or "").lower()
    filename = re.sub(r"[^A-Za-z0-9._-]+", "_", target["paper_id"]) + ".pdf"
    path = output / filename
    total = 0
    with path.open("wb") as handle:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("file_too_large")
            handle.write(chunk)

    magic = path.read_bytes()[:5]
    if magic != b"%PDF-":
        path.unlink(missing_ok=True)
        raise RuntimeError(f"not_pdf_magic:{magic!r};content_type={content_type}")

    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages[: min(8, pages)]:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(text_parts)
    tokens = [token for token in normalize(target["title"]).split() if len(token) > 3]
    title_match_ratio = sum(token in normalize(text) for token in tokens) / max(1, len(tokens))
    doi_match = target["doi"].lower() in text.lower()
    validation_status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"

    return {
        **target,
        "requested_url": target["url"],
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": file_sha256(path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": validation_status,
        "local_file": filename,
    }


def main() -> None:
    output = Path("fulltext-repo-pmc-aaai")
    output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-fulltext-audit/1.0 (lawful OA research archive)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = sum(item.get("validation_status") == "verified" for item in results)
    summary = {"targets": len(results), "verified": verified, "retryable_or_review": len(results) - verified}
    (output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No fulltext was verified")


if __name__ == "__main__":
    main()
