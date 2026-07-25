from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGET = {
    "paper_id": "doi:10.1016/j.obhdp.2018.12.005",
    "title": "Algorithm appreciation: People prefer algorithmic to human judgment",
    "doi": "10.1016/j.obhdp.2018.12.005",
    "landing_url": "https://escholarship.org/uc/item/9v38k9m6",
    "pdf_url": "https://escholarship.org/content/qt9v38k9m6/qt9v38k9m6.pdf",
    "version": "institutional_repository_manuscript",
    "license": "CC BY-NC-ND 4.0",
}
ALLOWED_HOSTS = {"escholarship.org", "www.escholarship.org"}


def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def norm(value: str) -> str:
    return re.sub(r'[^a-z0-9]+',' ',value.lower()).strip()


def main() -> None:
    out=Path('algorithm-appreciation-fulltext')
    out.mkdir(parents=True,exist_ok=True)
    session=requests.Session()
    session.headers.update({'User-Agent':'open-evidence-fulltext-audit/3.0 lawful institutional repository'})
    landing=session.get(TARGET['landing_url'],timeout=(30,180),allow_redirects=True)
    landing.raise_for_status()
    if (urlparse(landing.url).hostname or '').lower() not in ALLOWED_HOSTS:
        raise RuntimeError('landing_redirect_host_not_allowed')
    landing_text=landing.text
    landing_checks={
        'title_match': norm(TARGET['title']) in norm(landing_text),
        'doi_match': TARGET['doi'].lower() in landing_text.lower(),
        'license_match': 'by-nc-nd' in landing_text.lower() or 'Attribution-NonCommercial-NoDerivatives' in landing_text,
    }
    if not all(landing_checks.values()):
        raise RuntimeError(f'landing_metadata_mismatch:{landing_checks}')

    response=session.get(TARGET['pdf_url'],timeout=(30,240),allow_redirects=True,stream=True)
    response.raise_for_status()
    final_host=(urlparse(response.url).hostname or '').lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f'pdf_redirect_host_not_allowed:{final_host}')
    path=out/'doi_10.1016_j.obhdp.2018.12.005.pdf'
    total=0
    with path.open('wb') as handle:
        for chunk in response.iter_content(1024*1024):
            if not chunk: continue
            total+=len(chunk)
            if total>80*1024*1024: raise RuntimeError('file_too_large')
            handle.write(chunk)
    if path.read_bytes()[:5] != b'%PDF-':
        raise RuntimeError('not_pdf_magic')
    reader=PdfReader(str(path))
    pages=len(reader.pages)
    text='\n'.join((page.extract_text() or '') for page in reader.pages[:5])
    title_tokens=[t for t in norm(TARGET['title']).split() if len(t)>3]
    title_ratio=sum(token in norm(text) for token in title_tokens)/max(1,len(title_tokens))
    doi_match=TARGET['doi'].lower() in text.lower()
    license_match='by-nc-nd' in text.lower() or 'Attribution' in text
    if not (pages>0 and doi_match and title_ratio>=0.7 and license_match):
        raise RuntimeError(f'pdf_metadata_mismatch:pages={pages},doi={doi_match},title_ratio={title_ratio},license={license_match}')
    report={
        **TARGET,
        'requested_url':TARGET['pdf_url'],
        'final_url':response.url,
        'http_status':response.status_code,
        'content_type':response.headers.get('Content-Type'),
        'size_bytes':total,
        'sha256':sha256(path),
        'page_count':pages,
        'title_match_ratio':round(title_ratio,4),
        'doi_match':doi_match,
        'license_match':license_match,
        'landing_checks':landing_checks,
        'validation_status':'verified',
        'local_file':path.name,
    }
    (out/'fulltext_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'completion_summary.json').write_text(json.dumps({'targets':1,'verified':1,'completed':True},indent=2),encoding='utf-8')
    print(json.dumps({'paper_id':report['paper_id'],'verified':True,'pages':pages,'size_bytes':total,'sha256':report['sha256']},indent=2))


if __name__=='__main__':
    main()
