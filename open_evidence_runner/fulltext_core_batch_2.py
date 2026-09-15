from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path
from urllib.parse import urlparse
import requests
from pypdf import PdfReader
TARGETS=[
{"paper_id":"doi:10.1038/s41598-021-87480-9","title":"Humans Rely More on Algorithms Than Social Influence as a Task Becomes More Difficult","doi":"10.1038/s41598-021-87480-9","url":"https://www.nature.com/articles/s41598-021-87480-9.pdf","version":"publisher","license":"CC BY 4.0"},
{"paper_id":"doi:10.2196/29386","title":"The Impact of Explanations on Layperson Trust in Artificial Intelligence-Driven Symptom Checker Apps: Experimental Study","doi":"10.2196/29386","url":"https://www.jmir.org/2021/11/e29386/PDF","version":"publisher","license":"CC BY"},
{"paper_id":"arxiv:1801.04099","title":"Trust-Aware Decision Making for Human-Robot Collaboration: Model Learning and Planning","doi":"10.48550/arxiv.1801.04099","url":"https://arxiv.org/pdf/1801.04099","version":"preprint","license":"arXiv-hosted"},
{"paper_id":"arxiv:2001.07641","title":"Deceptive AI Explanations: Creation and Detection","doi":"10.48550/arxiv.2001.07641","url":"https://arxiv.org/pdf/2001.07641","version":"preprint","license":"arXiv-hosted"},
{"paper_id":"doi:10.3389/fnhum.2018.00309","title":"Learning From the Slips of Others: Neural Correlates of Trust in Automated Agents","doi":"10.3389/fnhum.2018.00309","url":"https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2018.00309/pdf","version":"publisher","license":"CC BY"},
{"paper_id":"doi:10.1145/3377325.3377498","title":"Proxy Tasks and Subjective Measures Can Be Misleading in Evaluating Explainable AI Systems","doi":"10.1145/3377325.3377498","url":"https://arxiv.org/pdf/2001.08298","version":"preprint","license":"arXiv-hosted"},
{"paper_id":"doi:10.1145/3375627.3375833","title":"How do I fool you? Manipulating User Trust via Misleading Black Box Explanations","doi":"10.1145/3375627.3375833","url":"https://arxiv.org/pdf/1911.06473","version":"preprint","license":"arXiv-hosted"},
{"paper_id":"doi:10.18653/v1/2020.acl-main.491","title":"Evaluating Explainable AI: Which Algorithmic Explanations Help Users Predict Model Behavior?","doi":"10.18653/v1/2020.acl-main.491","url":"https://aclanthology.org/2020.acl-main.491.pdf","version":"publisher","license":"ACL open"}
]
ALLOWED={"www.nature.com","nature.com","www.jmir.org","jmir.org","arxiv.org","export.arxiv.org","www.frontiersin.org","frontiersin.org","aclanthology.org"}
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
def digest(p):
 h=hashlib.sha256();
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''): h.update(b)
 return h.hexdigest()
def one(sess,t,out):
 host=(urlparse(t['url']).hostname or '').lower()
 if host not in ALLOWED: raise RuntimeError('host_not_allowed:'+host)
 r=sess.get(t['url'],timeout=(30,180),allow_redirects=True,stream=True)
 final=(urlparse(r.url).hostname or '').lower()
 if final not in ALLOWED: raise RuntimeError('redirect_host_not_allowed:'+final)
 r.raise_for_status(); name=re.sub(r'[^A-Za-z0-9._-]+','_',t['paper_id'])+'.pdf'; p=out/name; n=0
 with p.open('wb') as f:
  for c in r.iter_content(1048576):
   if not c: continue
   n+=len(c)
   if n>80*1024*1024: raise RuntimeError('file_too_large')
   f.write(c)
 if p.read_bytes()[:5]!=b'%PDF-': p.unlink(missing_ok=True); raise RuntimeError('not_pdf_magic')
 rd=PdfReader(str(p)); pages=len(rd.pages); text='\n'.join((pg.extract_text() or '') for pg in rd.pages[:min(8,pages)])
 toks=[x for x in norm(t['title']).split() if len(x)>3]; ratio=sum(x in norm(text) for x in toks)/max(1,len(toks)); dm=t['doi'].lower() in text.lower()
 status='verified' if pages and (dm or ratio>=.45) else 'needs_manual_title_review'
 return {**t,"requested_url":t['url'],"final_url":r.url,"http_status":r.status_code,"content_type":r.headers.get('content-type',''),"size_bytes":n,"sha256":digest(p),"page_count":pages,"doi_match":dm,"title_match_ratio":round(ratio,4),"validation_status":status,"local_file":name}
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
 s=requests.Session(); s.headers['User-Agent']='open-evidence-fulltext-audit/2.0 lawful OA research'
 rows=[]
 for t in TARGETS:
  try: rows.append(one(s,t,a.output))
  except Exception as e: rows.append({**t,"validation_status":"retryable","error":f'{type(e).__name__}:{e}'})
 (a.output/'fulltext_audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)); v=sum(x.get('validation_status')=='verified' for x in rows); (a.output/'completion_summary.json').write_text(json.dumps({"targets":len(rows),"verified":v,"retryable_or_review":len(rows)-v},indent=2)); print(v)
if __name__=='__main__': main()
