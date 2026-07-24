from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {"paper_id":"acl:D18-1128","title":"Do Explanations Make VQA Models More Predictable to a Human?","url":"https://aclanthology.org/D18-1128.pdf","expected_pages":7,"license":"ACL Anthology open access"},
    {"paper_id":"acl:N19-1357","title":"Attention is not Explanation","url":"https://aclanthology.org/N19-1357.pdf","expected_pages":14,"license":"ACL Anthology open access"},
    {"paper_id":"acl:D19-1002","title":"Attention is not not Explanation","url":"https://aclanthology.org/D19-1002.pdf","expected_pages":10,"license":"ACL Anthology open access"},
    {"paper_id":"acl:P19-1452","title":"BERT Rediscovers the Classical NLP Pipeline","url":"https://aclanthology.org/P19-1452.pdf","expected_pages":9,"license":"ACL Anthology open access"},
    {"paper_id":"arxiv:2606.06081","title":"A Framework for Measuring Appropriate Reliance on Set-Valued AI Advice","url":"https://arxiv.org/pdf/2606.06081","expected_pages":13,"license":"arXiv open preprint; license to verify from metadata/PDF"},
]
ALLOWED={"aclanthology.org","arxiv.org","export.arxiv.org"}

def sha256(path: Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def norm(s:str)->set[str]:
    return set(re.findall(r"[a-z0-9]+",s.lower()))

def main(out:Path):
    out.mkdir(parents=True,exist_ok=True)
    sess=requests.Session(); sess.headers.update({"User-Agent":"OpenEvidenceArchive/1.0 (research audit)"})
    rows=[]
    for t in TARGETS:
        row=dict(t); row.update(status="retryable",error=None)
        try:
            u=urlparse(t['url'])
            if u.scheme!='https' or u.hostname not in ALLOWED: raise RuntimeError('protocol_or_domain_not_allowed')
            r=sess.get(t['url'],timeout=(30,180),allow_redirects=True)
            row['http_status']=r.status_code; row['final_url']=r.url; row['content_type']=r.headers.get('content-type','')
            fu=urlparse(r.url)
            if fu.scheme!='https' or fu.hostname not in ALLOWED: raise RuntimeError('redirect_domain_not_allowed')
            r.raise_for_status()
            data=r.content
            if not data.startswith(b'%PDF-'): raise RuntimeError('pdf_magic_missing')
            if b'<html' in data[:4096].lower(): raise RuntimeError('html_error_page')
            path=out/(t['paper_id'].replace(':','_')+'.pdf'); path.write_bytes(data)
            reader=PdfReader(str(path)); pages=len(reader.pages)
            text=' '.join((p.extract_text() or '') for p in reader.pages[:3])
            overlap=len(norm(t['title']) & norm(text))/max(1,len(norm(t['title'])))
            row.update(status='downloaded_verified',sha256=sha256(path),size_bytes=path.stat().st_size,pages=pages,title_token_overlap=round(overlap,4),file_name=path.name)
            if pages<=0 or overlap<0.35: raise RuntimeError('title_or_page_validation_failed')
            if t.get('expected_pages') and abs(pages-t['expected_pages'])>2: row['page_count_warning']=True
        except Exception as e:
            row['status']='retryable'; row['error']=f'{type(e).__name__}: {e}'
        rows.append(row)
    (out/'fulltext_archive_manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'completion_summary.json').write_text(json.dumps({"total":len(rows),"verified":sum(r['status']=='downloaded_verified' for r in rows),"retryable":sum(r['status']=='retryable' for r in rows),"completed":all(r['status']=='downloaded_verified' for r in rows)},indent=2),encoding='utf-8')
    if not all(r['status']=='downloaded_verified' for r in rows): sys.exit(2)

if __name__=='__main__': main(Path(sys.argv[1] if len(sys.argv)>1 else 'fulltext-output'))
