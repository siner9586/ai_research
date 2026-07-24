from __future__ import annotations
import csv,hashlib,json,re,sys,time
from pathlib import Path
from urllib.parse import urlparse
import requests

TARGETS=[
{"id":"s2:82a5a84528a7ca0409f75e2211a3b33a217e9bac","title":"Ensuring Fairness in Machine Learning to Advance Health Equity","doi":"10.7326/m18-1990","url":"https://europepmc.org/articles/PMC6594166?pdf=render","license":"GREEN"},
{"id":"s2:f9fb0ad85f903e3ecf5d4bafdf7c74f647e75f58","title":"LEMNA: Explaining Deep Learning based Security Applications","doi":"10.1145/3243734.3243792","url":"https://dl.acm.org/doi/pdf/10.1145/3243734.3243792","license":"GOLD"},
{"id":"s2:80179a17eab0f9fb6e21840f3fed96c4d75c3442","title":"Building Ethics into Artificial Intelligence","doi":"10.24963/ijcai.2018/779","url":"https://www.ijcai.org/proceedings/2018/0779.pdf","license":"GOLD"},
{"id":"s2:95362d732fa70608c2640336d17ac8ff0895e10a","title":"The fallacy of inscrutability","doi":"10.1098/rsta.2018.0084","url":"https://europepmc.org/articles/PMC6191668?pdf=render","license":"GREEN"},
{"id":"s2:b2ebf0b2895a4275bdeda0b0b2b469b83adf931f","title":"A Decision Support Algorithm for Referrals to Post-Acute Care","doi":"10.1016/j.jamda.2018.08.016","url":"https://europepmc.org/articles/PMC6541013?pdf=render","license":"GREEN"},
{"id":"s2:bc9305aa9110c2bc4db1d3f720cab19d1b37ae21","title":"From Big Data to Deep Learning: A Leap Towards Strong AI or Intelligentia Obscura","doi":"10.3390/bdcc2030016","url":"https://www.mdpi.com/2504-2289/2/3/16/pdf?version=1531832584","license":"GOLD"},
{"id":"s2:e8485732d4f8835db8122f872dda1cc37651bde5","title":"Some HCI Priorities for GDPR-Compliant Machine Learning","doi":"10.31228/osf.io/wm6yk","url":"https://doi.org/10.31228/osf.io/wm6yk","license":"GOLD"},
{"id":"s2:ec103f167d25f10ee5efc1beb0fbd4d2d3b93b48","title":"Trust in Invisible Agents","doi":"10.1162/leon_e_01657","url":"https://direct.mit.edu/leon/article-pdf/51/5/450/1578671/leon_e_01657.pdf","license":"BRONZE"},
{"id":"s2:b1c263c0ad29e0102972bb451d46d80755d4449b","title":"Supply chain risk management and artificial intelligence: state of the art and future research directions","doi":"10.1080/00207543.2018.1530476","url":"https://pure.hud.ac.uk/ws/files/14514165/2018_IJPR.pdf","license":"GREEN"},
{"id":"s2:84db9aa99d2024a73487e6343368379e2fe3640b","title":"Deep learning for natural language processing: advantages and challenges","doi":"10.1093/nsr/nwx110","url":"https://academic.oup.com/nsr/article-pdf/5/1/24/24164446/nwx110.pdf","license":"HYBRID"}
]
ALLOWED={"europepmc.org","www.ijcai.org","dl.acm.org","www.mdpi.com","doi.org","osf.io","direct.mit.edu","pure.hud.ac.uk","academic.oup.com","oup.silverchair-cdn.com","pmc.ncbi.nlm.nih.gov","ncbi.nlm.nih.gov"}

def sha(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def safe_name(x):return re.sub(r'[^A-Za-z0-9._-]+','_',x)[:120]

def main(out:Path):
 out.mkdir(parents=True,exist_ok=True); files=out/'files'; files.mkdir(exist_ok=True); rows=[]
 s=requests.Session(); s.headers.update({'User-Agent':'ExplainabilityBiasOpenEvidence/1.0 (research audit)','Accept':'application/pdf,text/html;q=0.5'})
 for t in TARGETS:
  rrow={**t,'checked_at':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
  try:
   u=urlparse(t['url']);
   if u.scheme!='https' or u.hostname not in ALLOWED: raise RuntimeError('url_not_allowlisted')
   r=s.get(t['url'],timeout=(30,120),allow_redirects=True,stream=True)
   rrow.update({'http_status':r.status_code,'final_url':r.url,'content_type':r.headers.get('content-type'),'redirect_hosts':','.join(dict.fromkeys(urlparse(x.url).hostname or '' for x in r.history+[r]))})
   hosts=[urlparse(x.url).hostname for x in r.history+[r]]
   if any(h not in ALLOWED for h in hosts): raise RuntimeError('redirect_host_not_allowlisted')
   if r.status_code!=200: raise RuntimeError(f'http_{r.status_code}')
   body=r.content; rrow['size_bytes']=len(body); rrow['magic']=body[:8].hex()
   ctype=(r.headers.get('content-type') or '').lower()
   if not body.startswith(b'%PDF'):
    text=body[:3000].decode('utf-8','ignore').lower()
    if '<html' in text or 'captcha' in text or 'cloudflare' in text or 'access denied' in text: raise RuntimeError('html_or_access_challenge_not_pdf')
    raise RuntimeError('invalid_pdf_magic')
   p=files/(safe_name(t['id'])+'.pdf'); p.write_bytes(body)
   rrow.update({'status':'verified_pdf','local_file':str(p.relative_to(out)),'sha256':sha(p)})
  except Exception as e:
   rrow.update({'status':'retryable' if any(x in str(e) for x in ['timeout','429','500','502','503','504']) else 'failed','error':str(e)})
  rows.append(rrow)
 fields=sorted({k for x in rows for k in x})
 with (out/'fulltext_audit.csv').open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 (out/'fulltext_audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 summary={'targets':len(rows),'verified':sum(x['status']=='verified_pdf' for x in rows),'retryable':sum(x['status']=='retryable' for x in rows),'failed':sum(x['status']=='failed' for x in rows),'completed':True}
 (out/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary))
if __name__=='__main__':main(Path(sys.argv[1] if len(sys.argv)>1 else 'fulltext-output'))
