from __future__ import annotations

import hashlib
import json
import re
import traceback
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


def token_ratio(needle: str, haystack: str) -> float:
    tokens=[token for token in norm(needle).split() if len(token)>3]
    normalized=norm(haystack)
    return sum(token in normalized for token in tokens)/max(1,len(tokens))


def save(path: Path,value: dict) -> None:
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')


def execute(out: Path) -> dict:
    diagnostic={"target":TARGET,"stage":"start"}
    session=requests.Session()
    session.headers.update({'User-Agent':'open-evidence-fulltext-audit/3.2 lawful institutional repository','Accept':'text/html,application/pdf;q=0.9,*/*;q=0.5'})
    landing=session.get(TARGET['landing_url'],timeout=(30,180),allow_redirects=True)
    diagnostic.update({'stage':'landing_received','landing_status':landing.status_code,'landing_final_url':landing.url,'landing_content_type':landing.headers.get('Content-Type')})
    save(out/'diagnostic.json',diagnostic)
    landing.raise_for_status()
    if (urlparse(landing.url).hostname or '').lower() not in ALLOWED_HOSTS:
        raise RuntimeError('landing_redirect_host_not_allowed')
    landing_text=landing.text
    landing_title_ratio=token_ratio(TARGET['title'],landing_text)
    landing_checks={
        'title_token_ratio':round(landing_title_ratio,4),
        'title_match':landing_title_ratio>=0.7,
        'doi_match':TARGET['doi'].lower() in landing_text.lower(),
        'license_signal_observed':'by-nc-nd' in landing_text.lower() or 'attribution-noncommercial-noderivatives' in norm(landing_text),
    }
    diagnostic.update({'stage':'landing_validated','landing_checks':landing_checks})
    save(out/'diagnostic.json',diagnostic)
    if not landing_checks['title_match'] or not landing_checks['doi_match']:
        raise RuntimeError(f'landing_metadata_mismatch:{landing_checks}')

    response=session.get(TARGET['pdf_url'],timeout=(30,240),allow_redirects=True,stream=True)
    diagnostic.update({'stage':'pdf_response_received','pdf_status':response.status_code,'pdf_final_url':response.url,'pdf_content_type':response.headers.get('Content-Type')})
    save(out/'diagnostic.json',diagnostic)
    response.raise_for_status()
    final_host=(urlparse(response.url).hostname or '').lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f'pdf_redirect_host_not_allowed:{final_host}')
    path=out/'doi_10.1016_j.obhdp.2018.12.005.pdf'
    total=0
    prefix=b''
    with path.open('wb') as handle:
        for chunk in response.iter_content(1024*1024):
            if not chunk: continue
            if len(prefix)<64: prefix+=chunk[:64-len(prefix)]
            total+=len(chunk)
            if total>80*1024*1024: raise RuntimeError('file_too_large')
            handle.write(chunk)
    diagnostic.update({'stage':'pdf_downloaded','size_bytes':total,'prefix_hex':prefix.hex()})
    save(out/'diagnostic.json',diagnostic)
    if prefix[:5] != b'%PDF-':
        raise RuntimeError(f'not_pdf_magic:{prefix[:32]!r}')
    reader=PdfReader(str(path))
    pages=len(reader.pages)
    text='\n'.join((page.extract_text() or '') for page in reader.pages[:5])
    title_ratio=token_ratio(TARGET['title'],text)
    doi_match=TARGET['doi'].lower() in text.lower()
    normalized_pdf=norm(text)
    license_match=('by nc nd' in normalized_pdf or ('attribution' in normalized_pdf and 'noncommercial' in normalized_pdf and 'noderivatives' in normalized_pdf))
    pdf_checks={'pages':pages,'title_ratio':round(title_ratio,4),'doi_match':doi_match,'license_match':license_match}
    diagnostic.update({'stage':'pdf_parsed','pdf_checks':pdf_checks,'sha256':sha256(path)})
    save(out/'diagnostic.json',diagnostic)
    if not (pages>0 and doi_match and title_ratio>=0.7 and license_match):
        raise RuntimeError(f'pdf_metadata_mismatch:{pdf_checks}')
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
    save(out/'fulltext_audit.json',report)
    save(out/'completion_summary.json',{'targets':1,'verified':1,'completed':True})
    diagnostic['stage']='completed'
    save(out/'diagnostic.json',diagnostic)
    return report


def main() -> None:
    out=Path('algorithm-appreciation-fulltext')
    out.mkdir(parents=True,exist_ok=True)
    try:
        report=execute(out)
        print(json.dumps({'paper_id':report['paper_id'],'verified':True,'pages':report['page_count'],'size_bytes':report['size_bytes'],'sha256':report['sha256']},indent=2))
    except Exception as exc:
        failure={'completed':False,'error':f'{type(exc).__name__}:{exc}','traceback':traceback.format_exc(limit=8)}
        save(out/'failure.json',failure)
        print(json.dumps(failure,indent=2))
        raise


if __name__=='__main__':
    main()
