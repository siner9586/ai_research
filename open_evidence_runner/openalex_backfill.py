from __future__ import annotations
import argparse,csv,gzip,hashlib,json,os,random,re,time
from datetime import datetime,timezone
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API='https://api.openalex.org/works'; PER_PAGE=200
Q={
'Q01_XAI_FAITHFULNESS':['explanation faithfulness','explanation fidelity','attribution faithfulness','explanation infidelity'],
'Q02_XAI_STABILITY':['explanation stability','explanation robustness','attribution stability','attribution robustness'],
'Q03_XAI_COMPLETENESS':['explanation completeness','explanation sufficiency','explanation coverage','completeness explainable AI'],
'Q04_XAI_MECHANISTIC_ALIGNMENT':['mechanistic interpretability','mechanistic alignment','plausibility faithfulness','plausibility faithfulness gap'],
'Q05_HUMAN_AI_RELIANCE':['appropriate reliance AI','overreliance AI','underreliance AI','human AI reliance'],
'Q06_ALGORITHMIC_ADVICE':['algorithmic advice','AI advice','advice taking algorithm','artificial intelligence advice'],
'Q07_AUTOMATION_BIAS':['automation bias','error induction AI','automation induced error'],
'Q08_TRUST_CALIBRATION':['trust calibration AI','calibrated trust AI','trust in AI calibration'],
'Q09_PROFESSIONAL_DECISION':['AI assisted decision professional','AI decision support medical','AI decision support legal','AI decision support finance'],
'Q10_MANAGEMENT_ORGANIZATION':['managerial decision support AI','organizational decision support AI','management artificial intelligence decision','governance explainable AI'],
'Q11_TRANSFORMER_EXPLANATION':['Transformer explanation','BERT attribution','GPT explanation','attention rollout Transformer'],
'Q12_LLM_EXPLANATION':['large language model explanation faithfulness','LLM rationale faithfulness','large language model explanation'],
'Q13_OPEN_DATA_REPLICATION':['participant level data XAI','trial level data human AI','replication package explainable AI','open data human AI decision'],
'Q14_CHINESE_XAI':['可解释人工智能','解释忠实性','解释稳定性','解释偏差'],
'Q15_CHINESE_HUMAN_AI':['人机决策','算法建议','自动化偏差','适当依赖','信任校准']}
DOI=re.compile(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)',re.I)
SELECT='id,doi,display_name,publication_year,publication_date,type,language,authorships,primary_location,best_oa_location,open_access,abstract_inverted_index,ids,is_retracted,cited_by_count,referenced_works,related_works,topics,keywords'

def now(): return datetime.now(timezone.utc).isoformat()
def doi(v): return DOI.sub('',v).strip().lower() if isinstance(v,str) and v.strip() else None

def abstract(inv):
 if not isinstance(inv,dict): return None
 words=[]
 for w,positions in inv.items():
  for pos in positions or []: words.append((pos,w))
 return ' '.join(w for _,w in sorted(words))

def norm(x,y,q,t):
 best=x.get('best_oa_location') or {}; primary=x.get('primary_location') or {}; oa=x.get('open_access') or {}
 authors=[]
 for a in x.get('authorships') or []:
  author=(a or {}).get('author') or {}; name=author.get('display_name')
  if name: authors.append(name)
 oid=(x.get('id') or '').rsplit('/',1)[-1]
 return {'source_name':'OpenAlex','source_external_id':oid or hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest(),
 'openalex_id':oid,'doi_normalized':doi(x.get('doi')),'canonical_title':' '.join((x.get('display_name') or '').split()),
 'abstract':abstract(x.get('abstract_inverted_index')),'publication_date':x.get('publication_date'),'publication_year':x.get('publication_year') or y,
 'work_type':x.get('type'),'language':x.get('language'),'venue':((primary.get('source') or {}).get('display_name')),'publisher':((primary.get('source') or {}).get('host_organization_name')),
 'authors':authors,'landing_url':best.get('landing_page_url') or primary.get('landing_page_url'),'oa_pdf_url':best.get('pdf_url') or primary.get('pdf_url'),
 'is_oa':oa.get('is_oa'),'oa_status':oa.get('oa_status'),'license':best.get('license') or primary.get('license'),'is_retracted':x.get('is_retracted'),
 'cited_by_count':x.get('cited_by_count'),'referenced_works':x.get('referenced_works') or [],'related_works':x.get('related_works') or [],
 'topics':x.get('topics') or [],'keywords':x.get('keywords') or [],'query_groups':[q],'query_texts':[t]}

def session():
 r=Retry(total=8,connect=8,read=8,status=8,backoff_factor=1,status_forcelist=(429,500,502,503,504),allowed_methods=frozenset({'GET'}),respect_retry_after_header=True,raise_on_status=False)
 s=requests.Session(); s.mount('https://',HTTPAdapter(max_retries=r)); s.headers.update({'User-Agent':'ExplainabilityBiasOpenEvidence/1.0','Accept':'application/json'}); return s

def dumpgz(p,o):
 p.parent.mkdir(parents=True,exist_ok=True)
 with gzip.open(p,'wt',encoding='utf-8') as f: json.dump(o,f,ensure_ascii=False)
def save(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,ensure_ascii=False,indent=2),encoding='utf-8')

def crawl(s,root,y,q,t,i,deadline):
 cp=root/'checkpoints'/str(y)/q/f'{i:02d}.json'; old=json.loads(cp.read_text()) if cp.exists() else {}
 if old.get('completed'): return old['result']
 cur=old.get('cursor','*'); pages=old.get('pages',0); found=old.get('records',0); start=now(); done=False; err=None
 out=root/'normalized'/'openalex'/str(y)/q/f'{i:02d}.jsonl.gz'
 while time.monotonic()<deadline:
  end='2026-07-24' if y==2026 else f'{y}-12-31'; params={'search':t,'filter':f'from_publication_date:{y}-01-01,to_publication_date:{end}','per_page':PER_PAGE,'cursor':cur,'select':SELECT}
  if os.getenv('OPENALEX_API_KEY'): params['api_key']=os.getenv('OPENALEX_API_KEY')
  r=s.get(API,params=params,timeout=(30,120))
  if r.status_code!=200: err=f'http_{r.status_code}:{r.text[:300]}'; break
  try: p=r.json()
  except ValueError as e: err=f'invalid_json:{e}'; break
  items=p.get('results') or []; pages+=1; dumpgz(root/'raw'/'openalex'/str(y)/q/f'{i:02d}'/f'page_{pages:06d}.json.gz',p)
  out.parent.mkdir(parents=True,exist_ok=True)
  with gzip.open(out,'at',encoding='utf-8') as f:
   for x in items: f.write(json.dumps(norm(x,y,q,t),ensure_ascii=False)+'\n')
  found+=len(items); nxt=(p.get('meta') or {}).get('next_cursor'); done=not items or not nxt
  save(cp,{'cursor':nxt,'pages':pages,'records':found,'completed':done,'updated_at':now()})
  if done: cur=nxt or 'END_NO_NEXT_CURSOR'; break
  if nxt==cur: err='repeated_next_cursor'; break
  cur=nxt; time.sleep(.12+random.random()*.15)
 if not done and not err: err='workflow_deadline_reached'
 res={'query_group':q,'query_text':t,'pages_completed':pages,'records_found':found,'cursor_start':'*','cursor_end':cur,'completed':done,'started_at':start,'finished_at':now(),'error':err}
 save(cp,{'cursor':cur,'pages':pages,'records':found,'completed':done,'result':res,'updated_at':now()}); return res

def merge(root,y):
 rec={}
 for p in (root/'normalized'/'openalex'/str(y)).glob('**/[0-9][0-9].jsonl.gz'):
  with gzip.open(p,'rt',encoding='utf-8') as f:
   for line in f:
    x=json.loads(line); k=x.get('doi_normalized') or x['source_external_id']
    if k in rec:
     rec[k]['query_groups']=sorted(set(rec[k]['query_groups'])|set(x['query_groups'])); rec[k]['query_texts']=sorted(set(rec[k]['query_texts'])|set(x['query_texts']))
    else: rec[k]=x
 out=root/'normalized'/'openalex'/str(y)/'paper_master_openalex.jsonl.gz'
 with gzip.open(out,'wt',encoding='utf-8') as f:
  for k in sorted(rec): f.write(json.dumps(rec[k],ensure_ascii=False)+'\n')
 return len(rec),out

def main():
 a=argparse.ArgumentParser(); a.add_argument('--year',type=int,required=True); a.add_argument('--output',type=Path,required=True); a.add_argument('--hours',type=float,default=5.5); z=a.parse_args()
 z.output.mkdir(parents=True,exist_ok=True); started=now(); deadline=time.monotonic()+z.hours*3600; s=session(); results=[]
 for q,terms in Q.items():
  for i,t in enumerate(terms,1):
   r=crawl(s,z.output,z.year,q,t,i,deadline); results.append(r)
   if r['error']=='workflow_deadline_reached': break
  if results[-1]['error']=='workflow_deadline_reached': break
 n,master=merge(z.output,z.year); man=z.output/'manifests'/f'openalex_{z.year}_search_queries.csv'; man.parent.mkdir(parents=True,exist_ok=True)
 with man.open('w',newline='',encoding='utf-8-sig') as f: w=csv.DictWriter(f,fieldnames=list(results[0])); w.writeheader(); w.writerows(results)
 expected=sum(map(len,Q.values())); complete=len(results)==expected and all(x['completed'] for x in results)
 summary={'run_id':f'openalex-{z.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}','source':'OpenAlex','year':z.year,'subqueries_expected':expected,'subqueries_attempted':len(results),'subqueries_completed':sum(x['completed'] for x in results),'pages_completed':sum(x['pages_completed'] for x in results),'raw_records':sum(x['records_found'] for x in results),'unique_records':n,'completed':complete,'started_at':started,'finished_at':now(),'errors':[x for x in results if x['error']],'master_path':str(master.relative_to(z.output)),'manifest_path':str(man.relative_to(z.output))}
 p=z.output/'completion'/f'openalex_{z.year}_summary.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
