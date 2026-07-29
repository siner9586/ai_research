from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

PAPER_ID = "doi:10.1038/s44159-026-00562-1"
TITLE = "Principles for understanding trust in artificial intelligence"
DOI = "10.1038/s44159-026-00562-1"
URL = "https://ora.ox.ac.uk/objects/uuid%3A87e57859-bd77-408b-9537-042489038ece/files/s765374052"
RECORD_URL = "https://ora.ox.ac.uk/objects/uuid%3A87e57859-bd77-408b-9537-042489038ece"
LICENSE = "CC BY"
VERSION = "accepted_manuscript"
ALLOWED_HOSTS = {"ora.ox.ac.uk"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> None:
    output = Path("ora-aam")
    output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent":"open-evidence-ora-aam/1.0 (lawful institutional repository archive)"})
    requested_host = (urlparse(URL).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise SystemExit(f"host_not_allowed:{requested_host}")
    response = session.get(URL, timeout=(45, 600), allow_redirects=True, stream=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise SystemExit(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()
    content_type = (response.headers.get("content-type") or "").lower()
    path = output / "doi_10.1038_s44159-026-00562-1_ORA_AAM.pdf"
    total = 0
    with path.open("wb") as sink:
        for chunk in response.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > 25 * 1024 * 1024:
                raise SystemExit("unexpected_file_size")
            sink.write(chunk)
    if path.read_bytes()[:5] != b"%PDF-":
        prefix = path.read_bytes()[:200]
        path.unlink(missing_ok=True)
        raise SystemExit(f"not_pdf_magic:{prefix!r};content_type={content_type}")
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    sample = []
    for page in reader.pages[:12]:
        try:
            sample.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(sample)
    tokens = [token for token in norm(TITLE).split() if len(token) > 3]
    title_match_ratio = sum(token in norm(text) for token in tokens) / max(1, len(tokens))
    doi_match = DOI in text.lower()
    status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.75) else "needs_manual_review"
    result = {
        "paper_id": PAPER_ID,
        "title": TITLE,
        "doi": DOI,
        "record_url": RECORD_URL,
        "requested_url": URL,
        "final_url": response.url,
        "http_status": response.status_code,
        "content_type": content_type,
        "version": VERSION,
        "license": LICENSE,
        "rights_basis": "ORA record states the accepted manuscript is available under the University of Oxford Open Access Publications Policy with a CC BY public copyright licence.",
        "size_bytes": total,
        "sha256": sha256(path),
        "page_count": pages,
        "title_match_ratio": round(title_match_ratio, 4),
        "doi_match": doi_match,
        "validation_status": status,
        "local_file": path.name,
        "code_executed": False,
    }
    (output / "audit.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if status != "verified":
        raise SystemExit("identity_not_verified")


if __name__ == "__main__":
    main()
