from __future__ import annotations
import argparse,hashlib,json,re,time
from pathlib import Path
import requests

UA='OpenEvidence/1.0 (research archive; lawful OA only)'
PDF_MAGIC=b'%PDF-'

def sha256(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
 return h.hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--manifest',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
 a.output.mkdir(parents=True,exist_ok=True); rows=[]
 for item in json.loads(a.manifest.read_text()):
  rec={k:item.get(k) for k in ('paper_id','title','doi','url','license')}; rec.update({'status':'failed','checked_at':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
  try:
   r=requests.get(item['url'],headers={'User-Agent':UA,'Accept':'application/pdf'},timeout=(30,180),allow_redirects=True)
   rec.update({'http_status':r.status_code,'final_url':r.url,'content_type':r.headers.get('content-type'),'bytes':len(r.content)})
   ctype=(r.headers.get('content-type') or '').lower()
   if r.status_code!=200: raise RuntimeError(f'HTTP {r.status_code}')
   if not r.content.startswith(PDF_MAGIC): raise RuntimeError('not_pdf_magic')
   if 'pdf' not in ctype and len(r.content)<10000: raise RuntimeError('unexpected_mime')
   name=re.sub(r'[^A-Za-z0-9._-]+','_',item['paper_id'])+'.pdf'; p=a.output/name; p.write_bytes(r.content)
   rec.update({'status':'verified_pdf','file_name':name,'sha256':sha256(p)})
  except Exception as e: rec['error']=repr(e)
  rows.append(rec)
 (a.output/'fulltext_audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
 (a.output/'summary.json').write_text(json.dumps({'total':len(rows),'verified':sum(x['status']=='verified_pdf' for x in rows),'failed':sum(x['status']!='verified_pdf' for x in rows),'completed':True},indent=2),encoding='utf-8')
 print(json.dumps(rows,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
