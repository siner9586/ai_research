from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

ALLOWED_HOSTS = {
    "www.ncbi.nlm.nih.gov", "ncbi.nlm.nih.gov",
    "ftp.ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov",
}
MAX_BYTES = 150 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def https_ftp(url: str) -> str:
    if url.startswith("ftp://ftp.ncbi.nlm.nih.gov/"):
        return "https://ftp.ncbi.nlm.nih.gov/" + url.split("ftp://ftp.ncbi.nlm.nih.gov/", 1)[1]
    return url


def get_bytes(session: requests.Session, url: str) -> tuple[bytes, str, str, int]:
    host = (urlparse(url).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")
    response = session.get(url, timeout=(45, 600), allow_redirects=True)
    final_host = (urlparse(response.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    response.raise_for_status()
    data = response.content
    if len(data) > MAX_BYTES:
        raise RuntimeError("resource_too_large")
    return data, response.url, (response.headers.get("content-type") or "").lower(), response.status_code


def extract_pdf_from_tgz(data: bytes) -> tuple[bytes, str]:
    candidates: list[tuple[int, str, bytes]] = []
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        for member in tar.getmembers():
            if not member.isfile() or not member.name.lower().endswith(".pdf"):
                continue
            stream = tar.extractfile(member)
            if stream is None:
                continue
            content = stream.read()
            if content[:5] == b"%PDF-":
                candidates.append((len(content), member.name, content))
    if not candidates:
        raise RuntimeError("no_pdf_in_oa_tgz")
    candidates.sort(reverse=True)
    _, name, content = candidates[0]
    return content, name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pmcid", required=True)
    parser.add_argument("--paper-id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--doi", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-pmc-oa-recovery/1.0 (lawful OA research archive)"})
    api_url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={args.pmcid}"
    api_data, api_final_url, api_content_type, api_status = get_bytes(session, api_url)
    root = ET.fromstring(api_data)
    record = root.find(".//record")
    if record is None:
        error = root.find(".//error")
        raise RuntimeError(f"pmc_oa_record_not_found:{error.text if error is not None else api_data[:300]!r}")
    license_value = record.attrib.get("license")
    retracted = record.attrib.get("retracted")
    links = []
    for link in record.findall("link"):
        links.append({"format": link.attrib.get("format"), "href": link.attrib.get("href"), "updated": link.attrib.get("updated")})
    selected = next((item for item in links if item.get("format") == "pdf" and item.get("href")), None)
    archive_member = None
    if selected:
        resource_url = https_ftp(selected["href"])
        pdf_bytes, final_url, content_type, http_status = get_bytes(session, resource_url)
    else:
        selected = next((item for item in links if item.get("format") == "tgz" and item.get("href")), None)
        if not selected:
            raise RuntimeError(f"no_pdf_or_tgz_link:{links!r}")
        resource_url = https_ftp(selected["href"])
        tgz_bytes, final_url, content_type, http_status = get_bytes(session, resource_url)
        pdf_bytes, archive_member = extract_pdf_from_tgz(tgz_bytes)
    if pdf_bytes[:5] != b"%PDF-":
        raise RuntimeError(f"not_pdf_magic:{pdf_bytes[:20]!r}")

    file_name = re.sub(r"[^A-Za-z0-9._-]+", "_", args.paper_id) + ".pdf"
    path = args.output / file_name
    path.write_bytes(pdf_bytes)
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages[: min(12, pages)]:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(text_parts)
    title_tokens = [token for token in norm(args.title).split() if len(token) > 3]
    title_match_ratio = sum(token in norm(text) for token in title_tokens) / max(1, len(title_tokens))
    doi_match = args.doi.lower() in text.lower()
    validation_status = "verified" if pages > 0 and (doi_match or title_match_ratio >= 0.45) else "needs_manual_title_review"
    result = {
        "paper_id": args.paper_id,
        "title": args.title,
        "doi": args.doi,
        "pmcid": args.pmcid,
        "oa_api_url": api_url,
        "oa_api_final_url": api_final_url,
        "oa_api_http_status": api_status,
        "oa_api_content_type": api_content_type,
        "oa_record_license": license_value,
        "oa_record_retracted": retracted,
        "oa_links": links,
        "selected_format": selected.get("format") if selected else None,
        "selected_url": resource_url,
        "resource_final_url": final_url,
        "resource_http_status": http_status,
        "resource_content_type": content_type,
        "archive_pdf_member": archive_member,
        "size_bytes": len(pdf_bytes),
        "sha256": sha256(path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(title_match_ratio, 4),
        "validation_status": validation_status,
        "local_file": file_name,
        "code_executed": False,
    }
    (args.output / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    if validation_status != "verified":
        raise SystemExit("pdf_identity_not_verified")


if __name__ == "__main__":
    main()
