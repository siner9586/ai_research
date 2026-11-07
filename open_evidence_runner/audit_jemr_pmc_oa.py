from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

PMC_ID = "PMC13214853"
PAPER_ID = "doi:10.3390/jemr19030055"
DOI = "10.3390/jemr19030055"
TITLE = "Eye-Tracking Evidence That Verifiable Explanations Support Visual Evidence Checking in AI-Assisted Chest Radiograph Interpretation"
OA_API = f"https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={PMC_ID}"
ALLOWED_HOSTS = {"www.ncbi.nlm.nih.gov", "ncbi.nlm.nih.gov", "ftp.ncbi.nlm.nih.gov"}
MAX_BYTES = 300 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def https_from_ftp(url: str) -> str:
    if url.startswith("ftp://ftp.ncbi.nlm.nih.gov/"):
        return "https://ftp.ncbi.nlm.nih.gov/" + url.split("ftp.ncbi.nlm.nih.gov/", 1)[1]
    return url


def bounded_download(session: requests.Session, url: str, path: Path) -> dict:
    url = https_from_ftp(url)
    host = (urlparse(url).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")
    path.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    with session.get(url, timeout=(30, 300), stream=True, allow_redirects=True) as response:
        final_host = (urlparse(response.url).hostname or "").lower()
        if final_host not in ALLOWED_HOSTS:
            raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
        response.raise_for_status()
        with path.open("wb") as fh:
            for chunk in response.iter_content(1024 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > MAX_BYTES:
                    raise RuntimeError("package_exceeds_limit")
                fh.write(chunk)
        return {
            "requested_url": url,
            "final_url": response.url,
            "status": response.status_code,
            "content_type": response.headers.get("content-type"),
            "bytes": total,
            "sha256": sha256(path),
        }


def validate_pdf(path: Path) -> dict:
    if path.read_bytes()[:5] != b"%PDF-":
        raise RuntimeError("not_pdf_magic")
    reader = PdfReader(str(path))
    if reader.is_encrypted:
        raise RuntimeError("encrypted_pdf")
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages[: min(12, pages)]:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            pass
    text = "\n".join(text_parts)
    tokens = [token for token in norm(TITLE).split() if len(token) > 3]
    title_ratio = sum(token in norm(text) for token in tokens) / max(1, len(tokens))
    doi_match = DOI.lower() in text.lower()
    return {
        "pages": pages,
        "title_match_ratio": round(title_ratio, 4),
        "doi_match": doi_match,
        "validation_status": "oa_pdf_verified" if pages > 0 and (doi_match or title_ratio >= 0.45) else "needs_manual_title_review",
    }


def inspect_zip(path: Path) -> dict:
    import zipfile
    if path.read_bytes()[:2] != b"PK":
        raise RuntimeError("not_zip_magic")
    with zipfile.ZipFile(path) as zf:
        members = [{"name": info.filename, "size": info.file_size, "crc": info.CRC} for info in zf.infolist()]
        bad = zf.testzip()
    return {"member_count": len(members), "members": members, "crc_error_member": bad, "validation_status": "verified" if bad is None else "corrupt"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "ExplainabilityBiasOpenEvidence/3.1 PMC-OA-audit", "Accept": "application/xml,text/xml,*/*"})

    response = session.get(OA_API, timeout=(30, 180))
    response.raise_for_status()
    api_xml = args.output / "pmc_oa_response.xml"
    api_xml.write_bytes(response.content)
    root = ET.fromstring(response.content)
    error = root.find("error")
    if error is not None:
        raise RuntimeError(f"pmc_oa_error:{error.attrib}:{error.text}")
    record = root.find("records/record")
    if record is None:
        record = root.find("record")
    if record is None:
        raise RuntimeError("pmc_oa_record_missing")
    record_info = dict(record.attrib)
    links = []
    for link in record.findall("link"):
        links.append(dict(link.attrib))
    if not links:
        raise RuntimeError("pmc_oa_links_missing")

    package_link = next((link for link in links if link.get("format") in {"tgz", "tar.gz"}), None)
    if not package_link:
        raise RuntimeError(f"pmc_oa_package_link_missing:{links}")
    package_url = package_link.get("href")
    if not package_url:
        raise RuntimeError("pmc_oa_package_href_missing")
    package_path = args.output / f"{PMC_ID}.tar.gz"
    transfer = bounded_download(session, package_url, package_path)
    if package_path.read_bytes()[:2] != b"\x1f\x8b":
        raise RuntimeError("not_gzip_tar_magic")

    extract_dir = args.output / "package"
    manifest = []
    with tarfile.open(package_path, "r:gz") as tf:
        for member in tf.getmembers():
            if not member.isfile():
                continue
            if member.name.startswith("/") or ".." in Path(member.name).parts:
                raise RuntimeError(f"unsafe_tar_member:{member.name}")
            manifest.append({"name": member.name, "size": member.size})
        tf.extractall(extract_dir, filter="data")

    pdf_results = []
    zip_results = []
    other_files = []
    for path in sorted(p for p in extract_dir.rglob("*") if p.is_file()):
        relative = str(path.relative_to(extract_dir))
        suffix = path.suffix.lower()
        base = {"relative_path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)}
        if suffix == ".pdf":
            try:
                base.update(validate_pdf(path))
            except Exception as exc:
                base.update({"validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
            pdf_results.append(base)
        elif suffix == ".zip":
            try:
                base.update(inspect_zip(path))
            except Exception as exc:
                base.update({"validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
            zip_results.append(base)
        else:
            other_files.append(base)

    verified_pdf = next((item for item in pdf_results if item.get("validation_status") == "oa_pdf_verified"), None)
    if verified_pdf is None:
        raise RuntimeError(f"verified_article_pdf_missing:{pdf_results}")

    summary = {
        "paper_id": PAPER_ID,
        "pmc_id": PMC_ID,
        "doi": DOI,
        "title": TITLE,
        "oa_api": OA_API,
        "oa_api_status": response.status_code,
        "oa_api_sha256": sha256(api_xml),
        "record": record_info,
        "links": links,
        "package_transfer": transfer,
        "package_sha256": sha256(package_path),
        "package_members": manifest,
        "pdf_results": pdf_results,
        "zip_results": zip_results,
        "other_files": other_files,
        "verified_article_pdf": verified_pdf,
        "code_executed": False,
        "completed": True,
    }
    (args.output / "completion_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    sums = []
    for path in sorted(p for p in args.output.rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt"):
        sums.append(f"{sha256(path)}  {path.relative_to(args.output)}")
    (args.output / "SHA256SUMS.txt").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print(json.dumps({"record": record_info, "links": links, "pdf_results": pdf_results, "zip_results": zip_results, "other_file_count": len(other_files)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
