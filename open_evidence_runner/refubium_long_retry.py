from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

from pypdf import PdfReader

URL = "https://refubium.fu-berlin.de/bitstream/handle/fub188/50614/3757451.pdf?isAllowed=y&sequence=1"
EXPECTED_MD5 = "3817930aa3de95abd904509583054ec2"
DOI = "10.1145/3757451"
TITLE = "The AI is uncertain so am I What now Navigating Shortcomings of Uncertainty Representations in Human AI Collaboration with Capability focused Guidance"
MAX_BYTES = 10 * 1024 * 1024


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def digest(path: Path, alg: str) -> str:
    h = hashlib.new(alg)
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / "doi_10.1145_3757451.pdf"
    command = [
        "curl", "--fail", "--location", "--proto", "=https", "--tlsv1.2",
        "--ipv4", "--retry", "3", "--retry-delay", "10", "--retry-all-errors",
        "--connect-timeout", "120", "--max-time", "900", "--max-filesize", str(MAX_BYTES),
        "--user-agent", "open-evidence-refubium-retry/1.0 lawful OA research",
        "--output", str(path), URL,
    ]
    result = {"url": URL, "expected_md5": EXPECTED_MD5, "license": "CC BY-SA 4.0"}
    try:
        completed = subprocess.run(command, text=True, capture_output=True, timeout=960)
        result["curl_returncode"] = completed.returncode
        result["curl_stderr"] = completed.stderr[-3000:]
        if completed.returncode != 0:
            raise RuntimeError(f"curl_failed:{completed.returncode}")
        if path.stat().st_size > MAX_BYTES:
            raise RuntimeError("file_too_large")
        if path.read_bytes()[:5] != b"%PDF-":
            raise RuntimeError("not_pdf_magic")
        md5 = digest(path, "md5")
        if md5 != EXPECTED_MD5:
            raise RuntimeError(f"md5_mismatch:{md5}")
        reader = PdfReader(str(path))
        pages = len(reader.pages)
        text_parts = []
        for page in reader.pages:
            try:
                text_parts.append(page.extract_text() or "")
            except Exception:
                text_parts.append("")
        text = "\n".join(text_parts)
        tokens = [t for t in norm(TITLE).split() if len(t) > 3]
        ratio = sum(t in norm(text) for t in tokens) / max(1, len(tokens))
        doi_match = DOI in text.lower()
        if pages < 1 or not (doi_match or ratio >= 0.65):
            raise RuntimeError(f"title_doi_mismatch:{pages}:{ratio}:{doi_match}")
        result.update({
            "validation_status": "verified",
            "size_bytes": path.stat().st_size,
            "md5": md5,
            "sha256": digest(path, "sha256"),
            "page_count": pages,
            "doi_match": doi_match,
            "title_match_ratio": round(ratio, 4),
            "local_file": path.name,
        })
    except Exception as exc:
        path.unlink(missing_ok=True)
        result.update({"validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})
    (args.output / "audit_report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    verified = result.get("validation_status") == "verified"
    (args.output / "completion_summary.json").write_text(json.dumps({"targets": 1, "verified": int(verified), "retryable": int(not verified)}, indent=2), encoding="utf-8")
    if not verified:
        raise SystemExit("Refubium PDF remains retryable")


if __name__ == "__main__":
    main()
