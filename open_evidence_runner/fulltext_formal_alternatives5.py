from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {"paper_id":"doi:10.1038/s41598-026-59232-0","title":"HCCD-DS v2: a transparent synthetic benchmark for human-AI decision support under contextual uncertainty","doi":"10.1038/s41598-026-59232-0","url":"https://www.nature.com/articles/s41598-026-59232-0_reference.pdf","version":"accepted_manuscript","license":"Nature accepted manuscript open access"},
    {"paper_id":"doi:10.1038/s44159-026-00562-1","title":"Principles for understanding trust in artificial intelligence","doi":"10.1038/s44159-026-00562-1","url":"https://ora.ox.ac.uk/objects/uuid%3A87e57859-bd77-408b-9537-042489038ece/files/s765374052","version":"accepted_manuscript","license":"CC BY"},
    {"paper_id":"doi:10.1145/3772318.3790785","title":"Understanding the Effects of AI-Assisted Critical Thinking on Human-AI Decision Making","doi":"10.1145/3772318.3790785","url":"https://arxiv.org/pdf/2602.10222","version":"preprint","license":"CC BY-NC-ND 4.0"},
    {"paper_id":"doi:10.1145/3786326","title":"Passing the Buck to AI: How Individuals’ Decision-Making Patterns Affect Reliance on AI","doi":"10.1145/3786326","url":"https://arxiv.org/pdf/2505.01537","version":"preprint","license":"CC BY-NC-SA 4.0"},
    {"paper_id":"doi:10.1145/3742414.3794719","title":"How Do We Measure Over-Reliance? A Unified Probabilistic View","doi":"10.1145/3742414.3794719","url":"https://arxiv.org/pdf/2605.21635","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"ssrn:6845387","title":"How is Reliance on AI Measured? Mapping and Evaluating Measurement Approaches in Human-AI Interaction","doi":"","url":"https://papers.ssrn.com/sol3/Delivery.cfm/75de7aa9-0411-4582-92c5-81b0e3b7433b-MECA.pdf?abstractid=6845387&mirid=1","version":"working_paper","license":"SSRN publicly posted working paper"},
]

ALLOWED_HOSTS={"www.nature.com","nature.com","ora.ox.ac.uk","arxiv.org","export.arxiv.org","papers.ssrn.com","deliverypdf.ssrn.com"}
MAX_BYTES=120*1024*1024

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''): h.update(block)
    return h.hexdigest()

def norm(text:str)->str:
    return re.sub(r'[^a-z0-9]+',' ',text.lower()).strip()

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,required=True); args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    session=requests.Session(); session.headers.update({'User-Agent':'open-evidence-formal-alternatives/5.0 (lawful OA research archive)'})
    results=[]
    for target in TARGETS:
        try:
            host=(urlparse(target['url']).hostname or '').lower()
            if host not in ALLOWED_HOSTS: raise RuntimeError(f'host_not_allowed:{host}')
            r=session.get(target['url'],timeout=(30,240),allow_redirects=True,stream=True)
            final_host=(urlparse(r.url).hostname or '').lower()
            if final_host not in ALLOWED_HOSTS: raise RuntimeError(f'redirect_host_not_allowed:{final_host}')
            r.raise_for_status()
            content_type=(r.headers.get('content-type') or '').lower()
            filename=re.sub(r'[^A-Za-z0-9._-]+','_',target['paper_id'])+'.pdf'; path=args.output/filename
            total=0
            with path.open('wb') as f:
                for chunk in r.iter_content(1024*1024):
                    if not chunk: continue
                    total+=len(chunk)
                    if total>MAX_BYTES: raise RuntimeError('file_too_large')
                    f.write(chunk)
            if path.read_bytes()[:5]!=b'%PDF-':
                path.unlink(missing_ok=True); raise RuntimeError(f'not_pdf_magic;content_type={content_type}')
            reader=PdfReader(str(path)); pages=len(reader.pages); texts=[]
            for page in reader.pages:
                try: texts.append(page.extract_text() or '')
                except Exception: texts.append('')
            text='\n'.join(texts); nt=norm(text); tokens=[t for t in norm(target['title']).split() if len(t)>3]
            ratio=sum(t in nt for t in tokens)/max(1,len(tokens)); doi_match=bool(target['doi']) and target['doi'].lower() in text.lower()
            status='verified' if pages>0 and (doi_match or ratio>=0.45) else 'needs_manual_title_review'
            results.append({**target,'requested_url':target['url'],'final_url':r.url,'http_status':r.status_code,'content_type':content_type,'size_bytes':total,'sha256':sha256(path),'page_count':pages,'doi_match':doi_match,'title_match_ratio':round(ratio,4),'validation_status':status,'local_file':filename})
        except Exception as exc:
            results.append({**target,'validation_status':'retryable','error':f'{type(exc).__name__}:{exc}'})
    (args.output/'fulltext_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    verified=sum(r.get('validation_status')=='verified' for r in results); manual=sum(r.get('validation_status')=='needs_manual_title_review' for r in results); retryable=sum(r.get('validation_status')=='retryable' for r in results)
    summary={'targets':len(results),'verified':verified,'manual_review':manual,'retryable':retryable}
    (args.output/'completion_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8'); print(json.dumps(summary,indent=2))
    if verified==0: raise SystemExit('No lawful alternative PDF verified')

if __name__=='__main__': main()
