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

TARGETS = [
    {
        "candidate_id": "doi:10.3390/bs15101370",
        "pmcid": "PMC12561693",
        "title": "Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis",
        "doi": "10.3390/bs15101370",
        "license": "CC BY 4.0",
    },
    {
        "candidate_id": "doi:10.3390/bs14100964",
        "pmcid": "PMC11505338",
        "title": "Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks",
        "doi": "10.3390/bs14100964",
        "license": "CC BY 4.0",
    },
]
OA_API = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmcid}"
ALLOWED_HOSTS = {"www.ncbi.nlm.nih.gov", "ftp.ncbi.nlm.nih.gov"}
MAX_PACKAGE_BYTES = 120 * 1024 * 1024


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def safe_member(member: tarfile.TarInfo) -> bool:
    p = Path(member.name)
    return not p.is_absolute() and ".." not in p.parts and member.isfile()


def get_oa_package_url(session: requests.Session, pmcid: str) -> tuple[str, str]:
    api_url = OA_API.format(pmcid=pmcid)
    r = session.get(api_url, timeout=(20, 60))
    r.raise_for_status()
    if (urlparse(r.url).hostname or "").lower() not in ALLOWED_HOSTS:
        raise RuntimeError("oa_api_redirect_not_allowed")
    root = ET.fromstring(r.content)
    error = root.find("error")
    if error is not None:
        raise RuntimeError(f"oa_api_error:{''.join(error.itertext()).strip()}")
    links = root.findall(".//link")
    selected = None
    for link in links:
        if (link.attrib.get("format") or "").lower() == "tgz":
            selected = link.attrib.get("href")
            break
    if not selected:
        raise RuntimeError("oa_api_no_tgz_link")
    if selected.startswith("ftp://"):
        selected = "https://" + selected[len("ftp://"):]
    if (urlparse(selected).hostname or "").lower() != "ftp.ncbi.nlm.nih.gov":
        raise RuntimeError(f"oa_package_host_not_allowed:{selected}")
    return api_url, selected


def download(session: requests.Session, url: str, path: Path) -> dict:
    r = session.get(url, timeout=(30, 300), stream=True, allow_redirects=True)
    r.raise_for_status()
    final_host = (urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"package_redirect_not_allowed:{final_host}")
    total = 0
    with path.open("wb") as f:
        for chunk in r.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_PACKAGE_BYTES:
                raise RuntimeError("oa_package_too_large")
            f.write(chunk)
    if path.read_bytes()[:2] != b"\x1f\x8b":
        raise RuntimeError("oa_package_not_gzip")
    return {"package_final_url": r.url, "package_http_status": r.status_code, "package_bytes": total, "package_sha256": hash_file(path)}


def audit_one(session: requests.Session, target: dict, out: Path) -> dict:
    api_url, package_url = get_oa_package_url(session, target["pmcid"])
    package_path = out / f"{target['pmcid']}.tar.gz"
    transfer = download(session, package_url, package_path)
    candidates: list[tuple[tarfile.TarInfo, bytes]] = []
    manifest = []
    with tarfile.open(package_path, "r:gz") as tf:
        for member in tf.getmembers():
            if not safe_member(member):
                continue
            extracted = tf.extractfile(member)
            if extracted is None:
                continue
            content = extracted.read()
            manifest.append({"path": member.name, "size": len(content), "sha256": hashlib.sha256(content).hexdigest()})
            if member.name.lower().endswith(".pdf") and content[:5] == b"%PDF-":
                candidates.append((member, content))
    if not candidates:
        raise RuntimeError("oa_package_contains_no_pdf")
    best = max(candidates, key=lambda item: len(item[1]))
    pdf_path = out / (re.sub(r"[^A-Za-z0-9._-]+", "_", target["candidate_id"]) + ".pdf")
    pdf_path.write_bytes(best[1])
    reader = PdfReader(str(pdf_path))
    pages = len(reader.pages)
    text_parts = []
    for page in reader.pages:
        try:
            text_parts.append(page.extract_text() or "")
        except Exception:
            text_parts.append("")
    text = "\n".join(text_parts)
    normalized = norm(text)
    title_tokens = [t for t in norm(target["title"]).split() if len(t) > 3]
    ratio = sum(t in normalized for t in title_tokens) / max(1, len(title_tokens))
    doi_match = target["doi"].lower() in text.lower()
    if pages < 1 or not (doi_match or ratio >= 0.55):
        raise RuntimeError(f"oa_package_pdf_mismatch:pages={pages};ratio={ratio};doi={doi_match}")
    manifest_path = out / f"{target['pmcid']}_package_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        **target,
        "oa_api_url": api_url,
        "oa_package_url": package_url,
        **transfer,
        "package_pdf_member": best[0].name,
        "package_file_count": len(manifest),
        "pdf_size_bytes": pdf_path.stat().st_size,
        "pdf_sha256": hash_file(pdf_path),
        "page_count": pages,
        "doi_match": doi_match,
        "title_match_ratio": round(ratio, 4),
        "validation_status": "verified",
        "version": "pmc_oa_package_copy",
        "local_file": pdf_path.name,
        "manifest_file": manifest_path.name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "open-evidence-pmc-oa-package/1.0 (lawful OA research archive)"})
    results = []
    for target in TARGETS:
        try:
            results.append(audit_one(session, target, args.output))
        except Exception as exc:
            results.append({**target, "validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "fulltext_audit.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = sum(r.get("validation_status") == "verified" for r in results)
    summary = {"targets": len(results), "verified": verified, "retryable": len(results) - verified}
    (args.output / "completion_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if verified == 0:
        raise SystemExit("No official PMC OA package produced a verified PDF")


if __name__ == "__main__":
    main()
