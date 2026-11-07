from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

TARGETS = [
    {"id":"arxiv:1907.12652","title":"How model accuracy and explanation fidelity influence user trust","doi":"10.48550/arXiv.1907.12652","url":"https://arxiv.org/pdf/1907.12652v1","license":"arXiv-hosted"},
    {"id":"doi:10.1145/3301275.3302308","title":"I can do better than your AI: expertise and explanations","doi":"10.1145/3301275.3302308","url":"https://dl.acm.org/doi/pdf/10.1145/3301275.3302308","license":"publisher-OA-location-to-verify"},
    {"id":"doi:10.1016/j.jelectrocard.2019.08.006","title":"SPICED-ACS: Study of the potential impact of a computer-generated ECG diagnostic algorithmic certainty index in STEMI diagnosis: Towards transparent AI","doi":"10.1016/j.jelectrocard.2019.08.006","url":"https://pure.ulster.ac.uk/files/77282994/Accepted_author_manuscript_PDF.pdf","license":"institutional-manuscript"},
    {"id":"doi:10.1007/s41649-019-00096-0","title":"AI-Assisted Decision-making in Healthcare","doi":"10.1007/s41649-019-00096-0","url":"https://link.springer.com/content/pdf/10.1007/s41649-019-00096-0.pdf","license":"publisher-OA-location-to-verify"},
    {"id":"doi:10.1136/bmjhci-2019-100081","title":"Human factors challenges for the safe use of artificial intelligence in patient care","doi":"10.1136/bmjhci-2019-100081","url":"https://informatics.bmj.com/content/bmjhci/26/1/e100081.full.pdf","license":"publisher-OA-location-to-verify"},
    {"id":"doi:10.1007/978-3-030-29726-8_3","title":"New Frontiers in Explainable AI: Understanding the GI to Interpret the GO","doi":"10.1007/978-3-030-29726-8_3","url":"https://inria.hal.science/hal-02520038/file/485369_1_En_3_Chapter.pdf","license":"institutional-manuscript"},
    {"id":"doi:10.1016/j.future.2019.07.059","title":"Predicting supply chain risks using machine learning: The trade-off between performance and interpretability","doi":"10.1016/j.future.2019.07.059","url":"https://eprints.keele.ac.uk/id/eprint/8139/1/2019_FGCS_accepted.pdf","license":"institutional-manuscript"},
    {"id":"arxiv:1911.13073","title":"Attributional Robustness Training using Input-Gradient Spatial Alignment","doi":"10.48550/arXiv.1911.13073","url":"https://arxiv.org/pdf/1911.13073v4","license":"arXiv-hosted"},
    {"id":"doi:10.1007/s10994-020-05901-8","title":"A Decision-Theoretic Approach for Model Interpretability in Bayesian Framework","doi":"10.1007/s10994-020-05901-8","url":"https://arxiv.org/pdf/1910.09358v2","license":"arXiv-hosted"},
    {"id":"arxiv:1907.12669","title":"The Challenge of Imputation in Explainable Artificial Intelligence Models","doi":"10.48550/arXiv.1907.12669","url":"https://arxiv.org/pdf/1907.12669v1","license":"arXiv-hosted"},
]

ALLOWED_HOSTS = {
    "arxiv.org", "export.arxiv.org", "dl.acm.org", "pure.ulster.ac.uk",
    "link.springer.com", "informatics.bmj.com", "inria.hal.science",
    "hal.science", "eprints.keele.ac.uk", "keele-repository.worktribe.com",
    "deliverypdf.ssrn.com", "link.springer.com"
}
MAX_BYTES = 80 * 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_name(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", value)[:140]


def main(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    files_dir = output_dir / "files"
    files_dir.mkdir(exist_ok=True)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "ExplainabilityBiasOpenEvidence/1.0 (lawful research archive)",
        "Accept": "application/pdf,text/html;q=0.4",
    })
    rows = []
    for target in TARGETS:
        record = {**target, "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        try:
            parsed = urlparse(target["url"])
            if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
                raise RuntimeError("url_not_allowlisted")
            response = session.get(target["url"], timeout=(30, 180), allow_redirects=True, stream=True)
            chain = list(response.history) + [response]
            hosts = [urlparse(item.url).hostname or "" for item in chain]
            record.update({
                "http_status": response.status_code,
                "final_url": response.url,
                "content_type": response.headers.get("content-type"),
                "redirect_hosts": ",".join(dict.fromkeys(hosts)),
            })
            if any(host not in ALLOWED_HOSTS for host in hosts):
                raise RuntimeError("redirect_host_not_allowlisted")
            if response.status_code != 200:
                raise RuntimeError(f"http_{response.status_code}")
            content = bytearray()
            for chunk in response.iter_content(1024 * 1024):
                if not chunk:
                    continue
                content.extend(chunk)
                if len(content) > MAX_BYTES:
                    raise RuntimeError("file_exceeds_size_limit")
            body = bytes(content)
            record["size_bytes"] = len(body)
            record["magic"] = body[:8].hex()
            if not body.startswith(b"%PDF"):
                text = body[:5000].decode("utf-8", "ignore").lower()
                if any(marker in text for marker in ("<html", "captcha", "cloudflare", "access denied", "just a moment")):
                    raise RuntimeError("html_or_access_challenge_not_pdf")
                raise RuntimeError("invalid_pdf_magic")
            file_path = files_dir / f"{safe_name(target['id'])}.pdf"
            file_path.write_bytes(body)
            record.update({
                "status": "verified_pdf",
                "local_file": str(file_path.relative_to(output_dir)),
                "sha256": sha256_file(file_path),
            })
        except Exception as exc:
            error = str(exc)
            retryable_markers = ("timeout", "429", "500", "502", "503", "504", "connection", "temporarily")
            record.update({
                "status": "retryable" if any(marker in error.lower() for marker in retryable_markers) else "failed",
                "error": error,
            })
        rows.append(record)
    fields = sorted({key for row in rows for key in row})
    with (output_dir / "fulltext_audit.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    (output_dir / "fulltext_audit.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {
        "targets": len(rows),
        "verified": sum(row.get("status") == "verified_pdf" for row in rows),
        "retryable": sum(row.get("status") == "retryable" for row in rows),
        "failed": sum(row.get("status") == "failed" for row in rows),
        "completed": True,
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary))


if __name__ == "__main__":
    main(Path(sys.argv[1] if len(sys.argv) > 1 else "fulltext-output"))
