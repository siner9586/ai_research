from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

OUT=Path('fulltext-retry-audit-4')
PDF_TARGETS=[
 {'event_id':1,'paper_id':'arxiv:1805.05447','title':'Faithfully Explaining Rankings in a News Recommender System','doi':None,'url':'https://arxiv.org/pdf/1805.05447','version':'preprint','license':'arXiv-hosted'},
 {'event_id':2,'paper_id':'arxiv:1810.02678','title':'Local Interpretable Model-agnostic Explanations of Bayesian Predictive Models via Kullback-Leibler Projections','doi':'10.48550/arxiv.1810.02678','url':'https://arxiv.org/pdf/1810.02678','version':'preprint','license':'arXiv-hosted'},
 {'event_id':3,'paper_id':'arxiv:1806.08049','title':'On the Robustness of Interpretability Methods','doi':'10.48550/arxiv.1806.08049','url':'https://arxiv.org/pdf/1806.08049','version':'preprint','license':'arXiv-hosted'},
 {'event_id':4,'paper_id':'arxiv:1806.07538','title':'Towards Robust Interpretability with Self-Explaining Neural Networks','doi':'10.48550/arxiv.1806.07538','url':'https://arxiv.org/pdf/1806.07538','version':'preprint','license':'arXiv-hosted'},
 {'event_id':5,'paper_id':'arxiv:1802.00682','title':'How do Humans Understand Explanations from Machine Learning Systems? An Evaluation of the Human-Interpretability of Explanation','doi':'10.48550/arxiv.1802.00682','url':'https://arxiv.org/pdf/1802.00682','version':'preprint','license':'arXiv-hosted'},
 {'event_id':6,'paper_id':'arxiv:1802.07814','title':'Learning to Explain: An Information-Theoretic Perspective on Model Interpretation','doi':None,'url':'https://proceedings.mlr.press/v80/chen18j/chen18j.pdf','version':'published','license':'PMLR-open'},
 {'event_id':7,'paper_id':'arxiv:1806.00069','title':'Explaining Explanations: An Overview of Interpretability of Machine Learning','doi':'10.48550/arxiv.1806.00069','url':'https://arxiv.org/pdf/1806.00069','version':'preprint','license':'arXiv-hosted'},
]
HTML_TARGET={'event_id':8,'paper_id':'doi:10.23915/distill.00010','title':'The Building Blocks of Interpretability','doi':'10.23915/distill.00010','url':'https://distill.pub/2018/building-blocks/','version':'publisher_html','license':'CC BY 4.0'}
ALLOWED={'arxiv.org','export.arxiv.org','proceedings.mlr.press','distill.pub','www.distill.pub'}
MAX=120*1024*1024


def sha(path:Path)->str:
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def norm(s:str)->str:return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def ratio(title:str,text:str)->float:
 toks=[t for t in norm(title).split() if len(t)>3]; n=norm(text)
 return sum(t in n for t in toks)/max(1,len(toks))
def safe(pid:str,suffix:str)->str:return re.sub(r'[^A-Za-z0-9._-]+','_',pid)+suffix

def fetch(session,url,accept):
 if urlparse(url).scheme!='https':raise RuntimeError('non_https')
 if (urlparse(url).hostname or '').lower() not in ALLOWED:raise RuntimeError('host_not_allowed')
 r=session.get(url,headers={'Accept':accept},timeout=(30,240),allow_redirects=True,stream=True);r.raise_for_status()
 if (urlparse(r.url).hostname or '').lower() not in ALLOWED:raise RuntimeError('redirect_host_not_allowed')
 return r

def stream(session,url,path,accept):
 r=fetch(session,url,accept);total=0;prefix=b''
 with path.open('wb') as f:
  for c in r.iter_content(1024*1024):
   if not c:continue
   if len(prefix)<256:prefix+=c[:256-len(prefix)]
   total+=len(c)
   if total>MAX:raise RuntimeError('file_too_large')
   f.write(c)
 return {'final_url':r.url,'http_status':r.status_code,'content_type':r.headers.get('Content-Type'),'size_bytes':total,'prefix':prefix,'sha256':sha(path)}

def audit_pdf(session,t):
 path=OUT/safe(t['paper_id'],'.pdf');x=stream(session,t['url'],path,'application/pdf,*/*;q=0.5')
 if x['prefix'][:5]!=b'%PDF-':raise RuntimeError(f'not_pdf:{x["prefix"][:40]!r}')
 reader=PdfReader(str(path));pages=len(reader.pages);text='\n'.join((p.extract_text() or '') for p in reader.pages[:8])
 tr=ratio(t['title'],text)
 if pages<1 or tr<0.65:raise RuntimeError(f'identity_mismatch:pages={pages},title_ratio={tr}')
 return {**t,**{k:v for k,v in x.items() if k!='prefix'},'local_file':path.name,'page_count':pages,'title_match_ratio':round(tr,4),'doi_match':bool(t['doi'] and t['doi'].lower() in text.lower()),'validation_status':'verified'}

def audit_html(session,t):
 path=OUT/safe(t['paper_id'],'.html');x=stream(session,t['url'],path,'text/html,*/*;q=0.5')
 raw=path.read_bytes();text=raw.decode('utf-8',errors='replace')
 if b'<html' not in raw[:20000].lower():raise RuntimeError('not_html')
 tr=ratio(t['title'],text);doi=t['doi'].lower() in text.lower(); license_signal=('creativecommons.org/licenses/by/4.0' in text.lower() or 'cc by 4.0' in text.lower())
 if tr<0.75 or not doi or not license_signal:raise RuntimeError(f'html_identity_mismatch:title={tr},doi={doi},license={license_signal}')
 soup=BeautifulSoup(text,'html.parser')
 repositories=sorted({a.get('href') for a in soup.find_all('a',href=True) if 'github.com/' in a.get('href','')})
 return {**t,**{k:v for k,v in x.items() if k!='prefix'},'local_file':path.name,'title_match_ratio':round(tr,4),'doi_match':doi,'license_match':license_signal,'repository_links':repositories,'validation_status':'publisher_html_verified'}

def main():
 OUT.mkdir(parents=True,exist_ok=True);s=requests.Session();s.headers.update({'User-Agent':'open-evidence-fulltext-retry/4.0 lawful official-source archive'})
 rows=[]
 for t in PDF_TARGETS:
  try:rows.append(audit_pdf(s,t))
  except Exception as e:rows.append({**t,'validation_status':'retryable','error':f'{type(e).__name__}:{e}'})
 try:rows.append(audit_html(s,HTML_TARGET))
 except Exception as e:rows.append({**HTML_TARGET,'validation_status':'retryable','error':f'{type(e).__name__}:{e}'})
 summary={'targets':8,'verified_pdf':sum(r.get('validation_status')=='verified' for r in rows),'verified_html':sum(r.get('validation_status')=='publisher_html_verified' for r in rows),'retryable':sum(r.get('validation_status')=='retryable' for r in rows),'completed':True}
 (OUT/'audit_report.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 (OUT/'completion_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
 print(json.dumps(summary,indent=2))
 if summary['verified_pdf']+summary['verified_html']==0:raise SystemExit('No retry succeeded')

if __name__=='__main__':main()
