from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

MAX_BYTES = 80 * 1024 * 1024
STATEMENT_TERMS = (
    "data availability",
    "availability of data",
    "code availability",
    "data and code",
    "supplementary material",
    "supplemental material",
    "github.com",
    "osf.io",
    "zenodo",
    "huggingface.co",
)
URL_RE = re.compile(r"https?://[^\s<>\]\[(){}]+", re.I)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def load_target(config: Path, key: str) -> dict:
    targets = json.loads(config.read_text(encoding="utf-8"))
    matches = [item for item in targets if item["key"] == key]
    if len(matches) != 1:
        raise RuntimeError(f"target_key_resolution_failed:{key}:{len(matches)}")
    return matches[0]


def extract_pdf_text(reader: PdfReader) -> str:
    chunks: list[str] = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        if text:
            chunks.append(text)
    return "\n".join(chunks)


def statement_snippets(text: str) -> list[str]:
    snippets: list[str] = []
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
    for index, line in enumerate(lines):
        low = line.lower()
        if any(term in low for term in STATEMENT_TERMS):
            context = " ".join(lines[max(0, index - 1) : min(len(lines), index + 3)]).strip()
            if context and context not in snippets:
                snippets.append(context[:1000])
        if len(snippets) >= 20:
            break
    return snippets


def audit(target: dict, output: Path) -> dict:
    url = target["url"]
    parsed = urlparse(url)
    if parsed.scheme != "https":
        raise RuntimeError(f"non_https_url:{url}")
    initial_host = (parsed.hostname or "").lower()
    allowed_hosts = {host.lower() for host in target["allowed_hosts"]}
    if initial_host not in allowed_hosts:
        raise RuntimeError(f"host_not_allowed:{initial_host}")

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "open-evidence-fulltext-audit/2.0 (lawful OA research archive)",
            "Accept": "application/pdf,application/octet-stream;q=0.8,*/*;q=0.1",
        }
    )
    response = session.get(url, timeout=(30, 240), allow_redirects=True, stream=True)
    final_url = response.url
    final_host = (urlparse(final_url).hostname or "").lower()
    if final_host not in allowed_hosts:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()

    content_type = (response.headers.get("content-type") or "").lower()
    output.mkdir(parents=True, exist_ok=True)
    pdf_path = output / f"{target['key']}.pdf"
    total = 0
    with pdf_path.open("wb") as fh:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError("file_too_large")
            fh.write(chunk)

    magic = pdf_path.read_bytes()[:5]
    if magic != b"%PDF-":
        pdf_path.unlink(missing_ok=True)
        raise RuntimeError(f"not_pdf_magic:{magic!r};content_type={content_type}")

    reader = PdfReader(str(pdf_path))
    pages = len(reader.pages)
    if pages < 1:
        raise RuntimeError("empty_pdf")
    text = extract_pdf_text(reader)
    normalized_text = norm(text)
    title_tokens = [token for token in norm(target["title"]).split() if len(token) > 3]
    title_ratio = sum(token in normalized_text for token in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    title_match = title_ratio >= 0.45
    if not (doi_match or title_match):
        raise RuntimeError(f"title_doi_mismatch:title_ratio={title_ratio:.4f}")

    urls = []
    for match in URL_RE.findall(text):
        cleaned = match.rstrip(".,;:'\"")
        if cleaned not in urls:
            urls.append(cleaned)
        if len(urls) >= 100:
            break

    return {
        **target,
        "requested_url": url,
        "final_url": final_url,
        "http_status": response.status_code,
        "content_type": content_type,
        "size_bytes": total,
        "sha256": sha256(pdf_path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_ratio, 4),
        "validation_status": "verified",
        "local_file": pdf_path.name,
        "availability_statement_snippets": statement_snippets(text),
        "external_resource_urls": urls,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    target = load_target(args.config, args.key)
    target_dir = args.output / args.key
    target_dir.mkdir(parents=True, exist_ok=True)
    try:
        result = audit(target, target_dir)
    except Exception as exc:
        result = {
            **target,
            "validation_status": "retryable",
            "error": f"{type(exc).__name__}:{exc}",
        }
    audit_path = target_dir / "audit.json"
    audit_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
