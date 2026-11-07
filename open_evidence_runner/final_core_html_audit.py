from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests

TARGET = {
    "paper_id": "doi:10.1177/1555343418799601",
    "title": "The Role of Trust and Automation in an Intelligence Analyst Decisional Guidance Paradigm",
    "doi": "10.1177/1555343418799601",
    "url": "https://journals.sagepub.com/doi/10.1177/1555343418799601",
    "version": "publisher_html",
    "license_note": "Author note states U.S. federal government employees created the article within scope of employment; publisher rights notice retained.",
}
ALLOWED_HOSTS = {"journals.sagepub.com"}
MAX_BYTES = 8 * 1024 * 1024


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "open-evidence-html-audit/1.0 (research; lawful public page only)",
        "Accept": "text/html,application/xhtml+xml",
    })
    result = dict(TARGET)
    try:
        parsed = urlparse(TARGET["url"])
        if parsed.scheme != "https" or (parsed.hostname or "").lower() not in ALLOWED_HOSTS:
            raise RuntimeError("url_not_allowlisted")
        response = session.get(TARGET["url"], timeout=(30, 180), allow_redirects=True)
        final_host = (urlparse(response.url).hostname or "").lower()
        if final_host not in ALLOWED_HOSTS:
            raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
        response.raise_for_status()
        body = response.content
        if len(body) > MAX_BYTES:
            raise RuntimeError("html_too_large")
        content_type = (response.headers.get("content-type") or "").lower()
        if "html" not in content_type or b"<html" not in body[:8192].lower():
            raise RuntimeError(f"not_html:{content_type}")
        text = body.decode(response.encoding or "utf-8", errors="replace")
        lowered = text.lower()
        if any(marker in lowered for marker in ("captcha", "access denied", "cloudflare challenge")):
            raise RuntimeError("access_control_page")
        title_tokens = [t for t in norm(TARGET["title"]).split() if len(t) > 3]
        title_ratio = sum(t in norm(text) for t in title_tokens) / max(1, len(title_tokens))
        doi_match = TARGET["doi"] in lowered
        method_markers = all(marker in lowered for marker in ("participants", "automated aid", "trust in automation scale"))
        government_marker = "work of the u.s. federal government" in lowered or "u.s. government is authorized to reproduce" in lowered
        if not (doi_match and title_ratio >= 0.75 and method_markers):
            raise RuntimeError("page_does_not_contain_full_article_evidence")
        path = args.output / "doi_10.1177_1555343418799601.html"
        path.write_bytes(body)
        result.update({
            "final_url": response.url,
            "http_status": response.status_code,
            "content_type": content_type,
            "size_bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
            "title_match_ratio": round(title_ratio, 4),
            "doi_match": doi_match,
            "method_markers_present": method_markers,
            "government_work_marker_present": government_marker,
            "validation_status": "publisher_html_verified",
            "local_file": path.name,
        })
    except Exception as exc:
        result.update({"validation_status": "retryable", "error": f"{type(exc).__name__}:{exc}"})

    (args.output / "audit_report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    completed = result["validation_status"] == "publisher_html_verified"
    (args.output / "completion_summary.json").write_text(json.dumps({"targets": 1, "verified": int(completed), "retryable": int(not completed), "completed": completed}, indent=2), encoding="utf-8")
    if not completed:
        raise SystemExit("Publisher HTML was not verified; remains retryable")


if __name__ == "__main__":
    main()
