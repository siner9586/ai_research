from __future__ import annotations

import hashlib
import json
import re
import tarfile
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

OUT = Path('fulltext-retry-2')
OUT.mkdir(parents=True, exist_ok=True)
UA = 'open-evidence-fulltext-retry/2.0 (research; lawful OA only)'
MAX_BYTES = 80 * 1024 * 1024

TARGETS = [
    {
        'paper_id': 'doi:10.1093/jamia/ocag082',
        'title': 'Explainability in context: calibrating appropriate trust and reliance in artificial intelligence',
        'doi': '10.1093/jamia/ocag082',
        'kind': 'pmc_oa',
        'pmcid': 'PMC13385988',
        'license': 'PMC open-access article',
    },
    {
        'paper_id': 'doi:10.1038/s44159-026-00562-1',
        'title': 'Principles for understanding trust in artificial intelligence',
        'doi': '10.1038/s44159-026-00562-1',
        'kind': 'landing_pdf',
        'landing': 'https://kar.kent.ac.uk/114030/',
        'allowed_hosts': {'kar.kent.ac.uk'},
        'license': 'CC BY 4.0 accepted manuscript',
    },
    {
        'paper_id': 'doi:10.1145/3772318.3791467',
        'title': 'Do People Appropriately Rely on AI-Advice? An Analytical Review of HCI Research on Human-AI Decision-Making',
        'doi': '10.1145/3772318.3791467',
        'kind': 'landing_pdf',
        'landing': 'https://research-portal.uu.nl/en/publications/do-people-appropriately-rely-on-ai-advice-an-analytical-review-of/',
        'allowed_hosts': {'research-portal.uu.nl', 'pure.uu.nl', 'dspace.library.uu.nl'},
        'license': 'CC BY final published version',
    },
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def norm(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', ' ', text.lower()).strip()


def save_stream(resp: requests.Response, path: Path) -> None:
    total = 0
    with path.open('wb') as f:
        for chunk in resp.iter_content(1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > MAX_BYTES:
                raise RuntimeError('file_too_large')
            f.write(chunk)


def validate_pdf(path: Path, target: dict, final_url: str, status_code: int, content_type: str) -> dict:
    magic = path.read_bytes()[:5]
    if magic != b'%PDF-':
        raise RuntimeError(f'not_pdf_magic:{magic!r}')
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    sample = []
    for page in reader.pages[:min(10, pages)]:
        try:
            sample.append(page.extract_text() or '')
        except Exception:
            pass
    text = '\n'.join(sample)
    tokens = [t for t in norm(target['title']).split() if len(t) > 3]
    ratio = sum(t in norm(text) for t in tokens) / max(1, len(tokens))
    doi_match = target['doi'].lower() in text.lower()
    status = 'verified' if pages > 0 and (doi_match or ratio >= 0.45) else 'needs_manual_title_review'
    return {
        **target,
        'final_url': final_url,
        'http_status': status_code,
        'content_type': content_type,
        'size_bytes': path.stat().st_size,
        'sha256': sha256(path),
        'page_count': pages,
        'doi_match': doi_match,
        'title_match_ratio': round(ratio, 4),
        'validation_status': status,
        'local_file': path.name,
    }


def pmc_download(session: requests.Session, target: dict, path: Path) -> tuple[str, int, str]:
    api = f"https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={target['pmcid']}"
    r = session.get(api, timeout=(30, 120))
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'xml')
    links = [x.get('href') for x in soup.find_all('link') if x.get('href')]
    pdf_links = [u for u in links if u.lower().endswith('.pdf')]
    if pdf_links:
        url = pdf_links[0].replace('ftp://', 'https://')
        p = session.get(url, timeout=(30, 180), stream=True, allow_redirects=True)
        p.raise_for_status()
        save_stream(p, path)
        return p.url, p.status_code, (p.headers.get('content-type') or '').lower()
    tgz_links = [u for u in links if '.tar.gz' in u.lower()]
    if not tgz_links:
        raise RuntimeError(f'pmc_no_oa_file_links:{links}')
    url = tgz_links[0].replace('ftp://', 'https://')
    tgz = path.with_suffix('.tar.gz')
    p = session.get(url, timeout=(30, 240), stream=True, allow_redirects=True)
    p.raise_for_status()
    save_stream(p, tgz)
    with tarfile.open(tgz, 'r:gz') as tf:
        members = [m for m in tf.getmembers() if m.isfile() and m.name.lower().endswith('.pdf')]
        if not members:
            raise RuntimeError('pmc_archive_has_no_pdf')
        member = max(members, key=lambda m: m.size)
        src = tf.extractfile(member)
        if src is None:
            raise RuntimeError('pmc_pdf_extract_failed')
        path.write_bytes(src.read())
    tgz.unlink(missing_ok=True)
    return p.url, p.status_code, 'application/pdf-from-pmc-oa-package'


def landing_download(session: requests.Session, target: dict, path: Path) -> tuple[str, int, str]:
    r = session.get(target['landing'], timeout=(30, 120), allow_redirects=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    candidates = []
    for a in soup.find_all('a', href=True):
        href = urljoin(r.url, a['href'])
        text = ' '.join(a.get_text(' ', strip=True).split()).lower()
        if '.pdf' in href.lower() or 'download' in text or 'full text' in text or 'accepted manuscript' in text or 'final published version' in text:
            candidates.append(href)
    seen = set()
    for url in candidates:
        if url in seen:
            continue
        seen.add(url)
        host = (urlparse(url).hostname or '').lower()
        if host not in target['allowed_hosts']:
            continue
        try:
            p = session.get(url, timeout=(30, 180), stream=True, allow_redirects=True)
            final_host = (urlparse(p.url).hostname or '').lower()
            if final_host not in target['allowed_hosts']:
                continue
            if p.status_code != 200:
                continue
            tmp = path.with_suffix('.part')
            save_stream(p, tmp)
            if tmp.read_bytes()[:5] == b'%PDF-':
                tmp.replace(path)
                return p.url, p.status_code, (p.headers.get('content-type') or '').lower()
            tmp.unlink(missing_ok=True)
        except Exception:
            continue
    raise RuntimeError(f'no_downloadable_pdf_found:{len(candidates)} candidates')


def main() -> None:
    session = requests.Session()
    session.headers.update({'User-Agent': UA, 'Accept': 'text/html,application/pdf,application/xml;q=0.9,*/*;q=0.5'})
    results = []
    for target in TARGETS:
        filename = re.sub(r'[^A-Za-z0-9._-]+', '_', target['paper_id']) + '.pdf'
        path = OUT / filename
        try:
            if target['kind'] == 'pmc_oa':
                final_url, status_code, content_type = pmc_download(session, target, path)
            else:
                final_url, status_code, content_type = landing_download(session, target, path)
            results.append(validate_pdf(path, target, final_url, status_code, content_type))
        except Exception as exc:
            path.unlink(missing_ok=True)
            results.append({**target, 'validation_status': 'retryable', 'error': f'{type(exc).__name__}:{exc}'})
    (OUT / 'fulltext_retry_2.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    summary = {
        'targets': len(results),
        'verified': sum(r.get('validation_status') == 'verified' for r in results),
        'manual_review': sum(r.get('validation_status') == 'needs_manual_title_review' for r in results),
        'retryable': sum(r.get('validation_status') == 'retryable' for r in results),
    }
    (OUT / 'completion_summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2))
    if summary['verified'] == 0:
        raise SystemExit('No fulltext verified')


if __name__ == '__main__':
    main()
