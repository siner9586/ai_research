from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

OUTPUT=Path('fulltext-supplement-audit-3')
TARGETS=[
    {
        'paper_id':'doi:10.1145/3173574.3173677',
        'title':'Explanations as Mechanisms for Supporting Algorithmic Transparency',
        'doi':'10.1145/3173574.3173677',
        'pdf_url':'https://emileerader.com/papers/rader_chi18.pdf',
        'expected_pages':13,
        'version':'author_posted_manuscript',
        'license':'ACM author-posted copy; reuse subject to copyright notice',
        'supplement_url':'https://emileerader.com/papers/rader_chi18_supplementary_file.nb.html',
    },
    {
        'paper_id':'doi:10.1287/mnsc.2016.2643',
        'title':'Overcoming Algorithm Aversion: People Will Use Imperfect Algorithms If They Can (Even Slightly) Modify Them',
        'doi':'10.1287/mnsc.2016.2643',
        'pdf_url':'https://repository.upenn.edu/server/api/core/bitstreams/ac9f1367-c0e9-4a52-a90b-c7e30e6c4910/content',
        'expected_pages':None,
        'version':'institutional_repository_working_paper',
        'license':'repository terms; no Creative Commons license confirmed',
        'supplement_url':None,
    },
]
ALLOWED={'emileerader.com','www.emileerader.com','repository.upenn.edu'}
MAX=100*1024*1024


def sha(path:Path)->str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def norm(s:str)->str:
    return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()


def ratio(title:str,text:str)->float:
    toks=[t for t in norm(title).split() if len(t)>3]
    n=norm(text)
    return sum(t in n for t in toks)/max(1,len(toks))


def get(session:requests.Session,url:str,accept:str='*/*')->requests.Response:
    if urlparse(url).scheme!='https':raise RuntimeError('non_https')
    if (urlparse(url).hostname or '').lower() not in ALLOWED:raise RuntimeError('host_not_allowed')
    r=session.get(url,headers={'Accept':accept},timeout=(30,240),allow_redirects=True,stream=True)
    r.raise_for_status()
    if (urlparse(r.url).hostname or '').lower() not in ALLOWED:raise RuntimeError('redirect_host_not_allowed')
    return r


def download(session:requests.Session,url:str,path:Path,accept:str='*/*')->dict:
    r=get(session,url,accept)
    total=0;prefix=b''
    with path.open('wb') as f:
        for c in r.iter_content(1024*1024):
            if not c:continue
            if len(prefix)<128:prefix+=c[:128-len(prefix)]
            total+=len(c)
            if total>MAX:raise RuntimeError('file_too_large')
            f.write(c)
    return {'final_url':r.url,'status':r.status_code,'content_type':r.headers.get('Content-Type'),'size_bytes':total,'prefix':prefix,'sha256':sha(path)}


def audit_pdf(session:requests.Session,t:dict)->dict:
    name=re.sub(r'[^A-Za-z0-9._-]+','_',t['paper_id'])+'.pdf'
    path=OUTPUT/name
    x=download(session,t['pdf_url'],path,'application/pdf,*/*;q=0.5')
    if x['prefix'][:5]!=b'%PDF-':raise RuntimeError(f'not_pdf:{x["prefix"][:40]!r}')
    reader=PdfReader(str(path));pages=len(reader.pages)
    text='\n'.join((p.extract_text() or '') for p in reader.pages[:8])
    title_ratio=ratio(t['title'],text)
    doi_match=t['doi'].lower() in text.lower()
    if t['expected_pages'] is not None and pages!=t['expected_pages']:raise RuntimeError(f'page_mismatch:{pages}')
    # The UPenn working paper may omit the final journal DOI, so repository identity + strong title match is sufficient.
    if title_ratio<0.75:raise RuntimeError(f'title_mismatch:{title_ratio}')
    if t['paper_id'].startswith('doi:10.1145') and not doi_match:raise RuntimeError('doi_missing_from_author_pdf')
    return {**t,**{k:v for k,v in x.items() if k!='prefix'},'local_file':name,'page_count':pages,'title_match_ratio':round(title_ratio,4),'doi_match':doi_match,'validation_status':'verified'}


def audit_supplement(session:requests.Session,t:dict)->dict|None:
    if not t.get('supplement_url'):return None
    html_path=OUTPUT/'doi_10.1145_3173574.3173677_supplement.html'
    x=download(session,t['supplement_url'],html_path,'text/html,*/*;q=0.5')
    raw=html_path.read_bytes()
    if b'<html' not in raw[:10000].lower():raise RuntimeError('supplement_not_html')
    text=raw.decode('utf-8',errors='replace')
    if t['doi'].lower() not in text.lower() or 'Supplementary Material' not in text:raise RuntimeError('supplement_identity_mismatch')
    soup=BeautifulSoup(text,'html.parser')
    linked=[]
    for a in soup.find_all('a',href=True):
        href=urljoin(t['supplement_url'],a['href'])
        host=(urlparse(href).hostname or '').lower()
        if host in ALLOWED and (href.lower().endswith('.rmd') or 'download' in a.get_text(' ',strip=True).lower()):
            linked.append(href)
    linked=sorted(set(linked))
    downloaded=[]
    for i,href in enumerate(linked,start=1):
        suffix=Path(urlparse(href).path).suffix or '.txt'
        path=OUTPUT/f'doi_10.1145_3173574.3173677_supplement_link_{i}{suffix}'
        try:
            y=download(session,href,path,'text/plain,text/markdown,*/*;q=0.5')
            downloaded.append({'url':href,'local_file':path.name,**{k:v for k,v in y.items() if k!='prefix'}})
        except Exception as e:
            downloaded.append({'url':href,'error':f'{type(e).__name__}:{e}'})
    return {'paper_id':t['paper_id'],'supplement_url':t['supplement_url'],'local_file':html_path.name,**{k:v for k,v in x.items() if k!='prefix'},'linked_resources':downloaded,'validation_status':'verified_supplement_identity'}


def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    s=requests.Session();s.headers.update({'User-Agent':'open-evidence-fulltext-supplement-audit/3.0 lawful author and repository copies'})
    pdfs=[];supp=[];errors=[]
    for t in TARGETS:
        try:pdfs.append(audit_pdf(s,t))
        except Exception as e:errors.append({'paper_id':t['paper_id'],'stage':'pdf','error':f'{type(e).__name__}:{e}'})
        try:
            z=audit_supplement(s,t)
            if z:supp.append(z)
        except Exception as e:errors.append({'paper_id':t['paper_id'],'stage':'supplement','error':f'{type(e).__name__}:{e}'})
    report={'pdfs':pdfs,'supplements':supp,'errors':errors,'targets':len(TARGETS),'verified_pdfs':len(pdfs),'verified_supplements':len(supp),'completed':True}
    (OUTPUT/'audit_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUTPUT/'completion_summary.json').write_text(json.dumps({k:report[k] for k in ('targets','verified_pdfs','verified_supplements','completed')},indent=2),encoding='utf-8')
    print(json.dumps({k:report[k] for k in ('targets','verified_pdfs','verified_supplements','errors')},indent=2))
    if len(pdfs)!=2:raise SystemExit('Not all two open manuscripts verified')

if __name__=='__main__':main()
