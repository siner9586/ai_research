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
        "paper_id": "doi:10.18653/v1/N19-1357",
        "title": "Attention is not Explanation",
        "doi": "10.18653/v1/N19-1357",
        "url": "https://aclanthology.org/N19-1357.pdf",
        "version": "publishedVersion",
        "license": "ACL open",
    },
    {
        "paper_id": "doi:10.18653/v1/D19-1002",
        "title": "Attention is not not Explanation",
        "doi": "10.18653/v1/D19-1002",
        "url": "https://aclanthology.org/D19-1002.pdf",
        "version": "publishedVersion",
        "license": "ACL open",
    },
    {
        "paper_id": "doi:10.18653/v1/P19-1452",
        "title": "BERT Rediscovers the Classical NLP Pipeline",
        "doi": "10.18653/v1/P19-1452",
        "url": "https://aclanthology.org/P19-1452.pdf",
        "version": "publishedVersion",
        "license": "ACL open",
    },
    {
        "paper_id": "doi:10.18653/v1/D18-1128",
        "title": "Do Explanations Make VQA Models More Predictable to a Human?",
        "doi": "10.18653/v1/D18-1128",
        "url": "https://aclanthology.org/D18-1128.pdf",
        "version": "publishedVersion",
        "license": "ACL open",
    },
    {
        "paper_id": "doi:10.1186/s41235-026-00707-z",
        "title": "AI-augmented decision-making in face matching: comparing concurrent and non-concurrent advice presentation",
        "doi": "10.1186/s41235-026-00707-z",
        "url": "https://link.springer.com/content/pdf/10.1186/s41235-026-00707-z.pdf",
        "version": "publishedVersion",
        "license": "publisher OA",
    },
]

ALLOWED_HOSTS = {"aclanthology.org", "www.aclanthology.org", "link.springer.com", "springer.com"}
MAX_BYTES = 80 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
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
    path = out / filename
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
    tokens = [token for token in norm(target["title"]).split() if len(token) > 3]
    title_match_ratio = sum(token in norm(text) for token in tokens) / max(1, len(tokens))
    doi_match = target["doi"].lower() in text.lower()
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
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": validation_status,
        "local_file": filename,
    }


def main() -> None:
    out = Path("fulltext-acl-springer")
    out.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-fulltext-audit/1.0 (lawful OA research archive)"})

    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, out))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})

    (out / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = sum(item.get("validation_status") == "verified" for item in results)
    summary = {"targets": len(results), "verified": verified, "retryable_or_review": len(results) - verified}
    (out / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No fulltext was verified")


if __name__ == "__main__":
    main()
