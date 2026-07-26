from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests

TARGETS = [
    {"candidate_id":"doi:10.3390/bs15101370","pmcid":"PMC12561693","title":"Trust Formation, Error Impact, and Repair in Human-AI Financial Advisory: A Dynamic Behavioral Analysis","doi":"10.3390/bs15101370","license":"CC BY 4.0"},
    {"candidate_id":"doi:10.3390/bs14100964","pmcid":"PMC11505338","title":"Trust Dynamics in Financial Decision Making: Behavioral Responses to AI and Human Expert Advice Following Structural Breaks","doi":"10.3390/bs14100964","license":"CC BY 4.0"},
]
URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
ALLOWED_HOSTS={"www.ebi.ac.uk"}
MAX_BYTES=30*1024*1024
XLINK="{http://www.w3.org/1999/xlink}href"


def norm(s:str)->str: return re.sub(r"[^a-z0-9]+"," ",s.lower()).strip()


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    session=requests.Session(); session.headers.update({'User-Agent':'open-evidence-europe-pmc/1.0 lawful OA research archive','Accept':'application/xml,text/xml'})
    results=[]
    for target in TARGETS:
        try:
            url=URL.format(pmcid=target['pmcid']); r=session.get(url,timeout=(30,180),allow_redirects=True)
            r.raise_for_status(); host=(urlparse(r.url).hostname or '').lower()
            if host not in ALLOWED_HOSTS: raise RuntimeError(f'redirect_host_not_allowed:{host}')
            content=r.content
            if len(content)>MAX_BYTES: raise RuntimeError('xml_too_large')
            if not content.lstrip().startswith(b'<?xml') and not content.lstrip().startswith(b'<article'): raise RuntimeError('not_jats_xml_magic')
            root=ET.fromstring(content)
            article=root if root.tag.endswith('article') else root.find('.//article')
            if article is None: raise RuntimeError('article_element_missing')
            title_el=article.find('.//article-title'); title=' '.join(''.join(title_el.itertext()).split()) if title_el is not None else ''
            title_tokens=[x for x in norm(target['title']).split() if len(x)>3]; ratio=sum(x in norm(title) for x in title_tokens)/max(1,len(title_tokens))
            ids=[''.join(x.itertext()).strip().lower() for x in article.findall('.//article-id')]
            doi_match=target['doi'].lower() in ids or target['doi'].lower() in content.decode('utf-8','ignore').lower()
            body=article.find('.//body'); body_text=' '.join(''.join(body.itertext()).split()) if body is not None else ''
            if ratio<0.75 or not doi_match or len(body_text)<3000: raise RuntimeError(f'fulltext_validation_failed:ratio={ratio};doi={doi_match};body={len(body_text)}')
            lic=' '.join(''.join(x.itertext()).split() for x in article.findall('.//license-p'))
            supp=[]
            for x in article.findall('.//supplementary-material')+article.findall('.//supplement'):
                href=x.attrib.get(XLINK) or x.attrib.get('href'); label=' '.join(''.join(x.itertext()).split())[:500]
                if href or label: supp.append({'href':href,'label':label})
            path=a.output/(re.sub(r'[^A-Za-z0-9._-]+','_',target['candidate_id'])+'.xml'); path.write_bytes(content)
            result={**target,'requested_url':url,'final_url':r.url,'http_status':r.status_code,'content_type':r.headers.get('content-type'),'size_bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'title_match_ratio':round(ratio,4),'doi_match':doi_match,'body_character_count':len(body_text),'license_text':lic[:1500],'supplementary_links':supp,'validation_status':'europe_pmc_fulltext_xml_verified','local_file':path.name}
            results.append(result)
        except Exception as exc:
            results.append({**target,'validation_status':'retryable','error':f'{type(exc).__name__}:{exc}'})
    (a.output/'fulltext_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    v=sum(x.get('validation_status')=='europe_pmc_fulltext_xml_verified' for x in results); s={'targets':2,'verified':v,'retryable':2-v}; (a.output/'completion_summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8'); print(json.dumps(s))
    if v==0: raise SystemExit('No Europe PMC XML verified')
if __name__=='__main__': main()
