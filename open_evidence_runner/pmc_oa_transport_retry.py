from __future__ import annotations

import argparse
import hashlib
import json
import re
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {"candidate_id":"doi:10.3390/bs15101370","pmcid":"PMC12561693","title":"Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis","doi":"10.3390/bs15101370","license":"CC BY 4.0"},
    {"candidate_id":"doi:10.3390/bs14100964","pmcid":"PMC11505338","title":"Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks","doi":"10.3390/bs14100964","license":"CC BY 4.0"},
]
OA_API="https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id={pmcid}"
MAX_BYTES=120*1024*1024


def hfile(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()


def norm(s:str)->str: return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()


def bounded_urllib(url:str,path:Path)->dict:
    req=urllib.request.Request(url,headers={'User-Agent':'open-evidence-pmc-transport/1.0 lawful OA research'})
    total=0
    with urllib.request.urlopen(req,timeout=300) as r,path.open('wb') as f:
        while True:
            b=r.read(1024*1024)
            if not b: break
            total+=len(b)
            if total>MAX_BYTES: raise RuntimeError('file_too_large')
            f.write(b)
        return {'final_url':r.geturl(),'status':getattr(r,'status',None),'bytes':total}


def download_link(url:str,path:Path)->dict:
    attempts=[]
    candidates=[url]
    if url.startswith('ftp://'):
        candidates.append('https://'+url[len('ftp://'):])
    for candidate in candidates:
        try:
            info=bounded_urllib(candidate,path)
            return {**info,'requested_url':candidate,'prior_failures':attempts}
        except Exception as exc:
            attempts.append({'url':candidate,'error':f'{type(exc).__name__}:{exc}'})
            path.unlink(missing_ok=True)
    raise RuntimeError(json.dumps(attempts,ensure_ascii=False))


def validate_pdf(path:Path,target:dict)->dict:
    if path.read_bytes()[:5]!=b'%PDF-': raise RuntimeError('not_pdf_magic')
    r=PdfReader(str(path)); pages=len(r.pages); parts=[]
    for page in r.pages:
        try: parts.append(page.extract_text() or '')
        except Exception: parts.append('')
    text='\n'.join(parts); nt=norm(text); tokens=[t for t in norm(target['title']).split() if len(t)>3]
    ratio=sum(t in nt for t in tokens)/max(1,len(tokens)); dm=target['doi'].lower() in text.lower()
    if pages<1 or not(dm or ratio>=.55): raise RuntimeError(f'pdf_mismatch:{pages}:{ratio}:{dm}')
    return {'page_count':pages,'pdf_sha256':hfile(path),'pdf_size_bytes':path.stat().st_size,'doi_match':dm,'title_match_ratio':round(ratio,4)}


def audit(target:dict,out:Path)->dict:
    api=OA_API.format(pmcid=target['pmcid'])
    rr=requests.get(api,timeout=(20,60),headers={'User-Agent':'open-evidence-pmc-transport/1.0 lawful OA research'})
    rr.raise_for_status()
    xml_path=out/f"{target['pmcid']}_oa_api.xml"; xml_path.write_bytes(rr.content)
    root=ET.fromstring(rr.content)
    links=[{'format':x.attrib.get('format'),'href':x.attrib.get('href')} for x in root.findall('.//link') if x.attrib.get('href')]
    (out/f"{target['pmcid']}_links.json").write_text(json.dumps(links,indent=2),encoding='utf-8')
    failures=[]
    for link in sorted(links,key=lambda x:0 if (x['format'] or '').lower()=='pdf' else 1):
        fmt=(link['format'] or '').lower(); href=link['href']
        try:
            if fmt=='pdf':
                p=out/(re.sub(r'[^A-Za-z0-9._-]+','_',target['candidate_id'])+'.pdf')
                transfer=download_link(href,p); val=validate_pdf(p,target)
                return {**target,'oa_api_url':api,'oa_links':links,'selected_format':'pdf',**transfer,**val,'validation_status':'verified','local_file':p.name}
            if fmt=='tgz':
                tgz=out/f"{target['pmcid']}.tar.gz"; transfer=download_link(href,tgz)
                if tgz.read_bytes()[:2]!=b'\x1f\x8b': raise RuntimeError('not_gzip')
                pdfs=[]; manifest=[]
                with tarfile.open(tgz,'r:gz') as tf:
                    for m in tf.getmembers():
                        pp=Path(m.name)
                        if not m.isfile() or pp.is_absolute() or '..' in pp.parts: continue
                        f=tf.extractfile(m)
                        if f is None: continue
                        content=f.read(); manifest.append({'path':m.name,'size':len(content),'sha256':hashlib.sha256(content).hexdigest()})
                        if m.name.lower().endswith('.pdf') and content[:5]==b'%PDF-': pdfs.append((m.name,content))
                if not pdfs: raise RuntimeError('tgz_no_pdf')
                name,content=max(pdfs,key=lambda x:len(x[1])); p=out/(re.sub(r'[^A-Za-z0-9._-]+','_',target['candidate_id'])+'.pdf'); p.write_bytes(content)
                val=validate_pdf(p,target); (out/f"{target['pmcid']}_manifest.json").write_text(json.dumps(manifest,indent=2),encoding='utf-8')
                return {**target,'oa_api_url':api,'oa_links':links,'selected_format':'tgz','selected_member':name,'package_sha256':hfile(tgz),**transfer,**val,'validation_status':'verified','local_file':p.name}
        except Exception as exc:
            failures.append({'format':fmt,'href':href,'error':f'{type(exc).__name__}:{exc}'})
    raise RuntimeError(json.dumps(failures,ensure_ascii=False))


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    results=[]
    for t in TARGETS:
        try: results.append(audit(t,a.output))
        except Exception as exc: results.append({**t,'validation_status':'retryable','error':f'{type(exc).__name__}:{exc}'})
    (a.output/'fulltext_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    v=sum(x.get('validation_status')=='verified' for x in results); s={'targets':2,'verified':v,'retryable':2-v}; (a.output/'completion_summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8'); print(json.dumps(s))
    if v==0: raise SystemExit('No PMC transport succeeded')
if __name__=='__main__': main()
