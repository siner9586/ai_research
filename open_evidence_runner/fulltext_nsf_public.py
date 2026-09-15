from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGET = {
    "paper_id": "doi:10.1145/3519266",
    "title": "Effects of Explanations in AI-Assisted Decision Making: Principles and Comparisons",
    "doi": "10.1145/3519266",
    "url": "https://par.nsf.gov/servlets/purl/10434195",
    "version": "accepted_manuscript",
    "license": "CC BY 4.0",
}
ALLOWED_HOSTS = {"par.nsf.gov", "www.osti.gov", "osti.gov"}
MAX_BYTES = 100 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    result = {**TARGET}
    try:
        host = (urlparse(TARGET["url"]).hostname or "").lower()
        if host not in ALLOWED_HOSTS:
            raise RuntimeError(f"host_not_allowed:{host}")
        session = requests.Session()
        session.headers.update({"User-Agent": "open-evidence-nsf-public/1.0 (lawful public access research archive)"})
        r = session.get(TARGET["url"], timeout=(30, 240), allow_redirects=True, stream=True)
        final_host = (urlparse(r.url).hostname or "").lower()
        if final_host not in ALLOWED_HOSTS:
            raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
        r.raise_for_status()
        content_type = (r.headers.get("content-type") or "").lower()
        path = args.output / "doi_10.1145_3519266.pdf"
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
            path.unlink(missing_ok=True)
            raise RuntimeError(f"not_pdf_magic;content_type={content_type}")
        reader = PdfReader(str(path))
        pages = len(reader.pages)
        text_parts = []
        for page in reader.pages:
            try:
                text_parts.append(page.extract_text() or "")
            except Exception:
                text_parts.append("")
        text = "\n".join(text_parts)
        tokens = [t for t in norm(TARGET["title"]).split() if len(t) > 3]
        ratio = sum(t in norm(text) for t in tokens) / max(1, len(tokens))
        doi_match = TARGET["doi"].lower() in text.lower()
        license_match = "creative commons attribution international 4.0" in text.lower()
        result.update({
            "requested_url": TARGET["url"],
            "final_url": r.url,
            "http_status": r.status_code,
            "content_type": content_type,
            "size_bytes": total,
            "sha256": sha256(path),
            "page_count": pages,
            "doi_match": doi_match,
            "title_match_ratio": round(ratio, 4),
            "license_text_match": license_match,
            "local_file": path.name,
            "validation_status": "verified" if pages == 36 and doi_match and ratio >= 0.7 and license_match else "needs_manual_title_review",
        })
    except Exception as exc:
        result.update({"validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps([result], ensure_ascii=False, indent=2), encoding="utf-8")
    verified = result.get("validation_status") == "verified"
    summary = {"targets": 1, "verified": int(verified), "manual_review": int(result.get("validation_status") == "needs_manual_title_review"), "retryable": int(result.get("validation_status") == "retryable")}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if not verified:
        raise SystemExit("NSF accepted manuscript was not fully verified")


if __name__ == "__main__":
    main()
