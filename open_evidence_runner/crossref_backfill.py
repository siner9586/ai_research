from __future__ import annotations
import argparse,csv,gzip,hashlib,json,os,random,re,time
from datetime import datetime,timezone
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API='https://api.crossref.org/works'; ROWS=1000
Q={
'Q01_XAI_FAITHFULNESS':['"explanation faithfulness"','"explanation fidelity"','"attribution faithfulness"','"explanation infidelity"'],
'Q02_XAI_STABILITY':['"explanation stability"','"explanation robustness"','"attribution stability"','"attribution robustness"'],
'Q03_XAI_COMPLETENESS':['"explanation completeness"','"explanation sufficiency"','"explanation coverage"','completeness "explainable AI"'],
'Q04_XAI_MECHANISTIC_ALIGNMENT':['"mechanistic interpretability"','"mechanistic alignment"','"plausibility faithfulness"','"plausibility-faithfulness gap"'],
'Q05_HUMAN_AI_RELIANCE':['"appropriate reliance" AI','overreliance AI','underreliance AI','"human AI reliance"'],
'Q06_ALGORITHMIC_ADVICE':['"algorithmic advice"','"AI advice"','"advice taking" algorithm','"artificial intelligence advice"'],
'Q07_AUTOMATION_BIAS':['"automation bias"','"error induction" AI','"automation-induced error"'],
'Q08_TRUST_CALIBRATION':['"trust calibration" AI','"calibrated trust" AI','"trust in AI" calibration'],
'Q09_PROFESSIONAL_DECISION':['"AI-assisted decision" professional','"AI decision support" medical','"AI decision support" legal','"AI decision support" finance'],
'Q10_MANAGEMENT_ORGANIZATION':['managerial "decision support" AI','organizational "decision support" AI','management "artificial intelligence" decision','governance explainable AI'],
'Q11_TRANSFORMER_EXPLANATION':['Transformer explanation','BERT attribution','GPT explanation','"attention rollout" Transformer'],
'Q12_LLM_EXPLANATION':['"large language model" "explanation faithfulness"','LLM rationale faithfulness','"large language model" explanation'],
'Q13_OPEN_DATA_REPLICATION':['"participant-level data" XAI','"trial-level data" "human AI"','"replication package" explainable AI','"open data" "human AI decision"'],
'Q14_CHINESE_XAI':['可解释人工智能','解释忠实性','解释稳定性','解释偏差'],
'Q15_CHINESE_HUMAN_AI':['人机决策','算法建议','自动化偏差','适当依赖','信任校准']}
DOI=re.compile(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)',re.I)

def now(): return datetime.now(timezone.utc).isoformat()
def doi(v): return DOI.sub('',v).strip().lower() if isinstance(v,str) and v.strip() else None
def first(v): return v[0] if isinstance(v,list) and v else None

def pubdate(x):
 for k in ('published-online','published-print','published','issued','created'):
  p=first((x.get(k) or {}).get('date-parts'))
  if p:
   return f"{int(p[0]):04d}-{int(p[1]) if len(p)>1 else 1:02d}-{int(p[2]) if len(p)>2 else 1:02d}"
 return None

def norm(x,y,q,t):
 d=doi(x.get('DOI')); title=first(x.get('title')) or ''
 return {'source_name':'Crossref','source_external_id':d or x.get('URL') or hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest(),
 'doi_normalized':d,'canonical_title':' '.join(str(title).split()),'abstract':x.get('abstract'),'publication_date':pubdate(x),
 'publication_year':y,'work_type':x.get('type'),'language':x.get('language'),'venue':first(x.get('container-title')),
 'publisher':x.get('publisher'),'authors':[' '.join(filter(None,[a.get('given'),a.get('family')])).strip() for a in x.get('author') or []],
 'url':x.get('URL'),'licenses':x.get('license') or [],'links':x.get('link') or [],'reference_count':x.get('reference-count'),
 'is_referenced_by_count':x.get('is-referenced-by-count'),'relation':x.get('relation'),'query_groups':[q],'query_texts':[t]}

def session():
 r=Retry(total=8,connect=8,read=8,status=8,backoff_factor=1,status_forcelist=(429,500,502,503,504),allowed_methods=frozenset({'GET'}),respect_retry_after_header=True,raise_on_status=False)
 s=requests.Session(); s.mount('https://',HTTPAdapter(max_retries=r))
 mail=os.getenv('CROSSREF_MAILTO') or os.getenv('UNPAYWALL_EMAIL'); ua='ExplainabilityBiasOpenEvidence/1.0'+(f' (mailto:{mail})' if mail else '')
 s.headers.update({'User-Agent':ua,'Accept':'application/json'}); return s

def dumpgz(p,o):
 p.parent.mkdir(parents=True,exist_ok=True)
 with gzip.open(p,'wt',encoding='utf-8') as f: json.dump(o,f,ensure_ascii=False)

def checkpoint(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,ensure_ascii=False,indent=2),encoding='utf-8')

def crawl(s,root,y,q,t,i,deadline):
 cp=root/'checkpoints'/str(y)/q/f'{i:02d}.json'; old=json.loads(cp.read_text()) if cp.exists() else {}
 if old.get('completed'): return old['result']
 cur=old.get('cursor','*'); pages=old.get('pages',0); found=old.get('records',0); start=now(); err=None; done=False
 out=root/'normalized'/'crossref'/str(y)/q/f'{i:02d}.jsonl.gz'
 while time.monotonic()<deadline:
  end='2026-07-24' if y==2026 else f'{y}-12-31'
  r=s.get(API,params={'query.bibliographic':t,'filter':f'from-pub-date:{y}-01-01,until-pub-date:{end}','rows':ROWS,'cursor':cur},timeout=(30,120))
  if r.status_code!=200: err=f'http_{r.status_code}:{r.text[:300]}'; break
  try: p=r.json()
  except ValueError as e: err=f'invalid_json:{e}'; break
  m=p.get('message') or {}; items=m.get('items') or []; pages+=1
  dumpgz(root/'raw'/'crossref'/str(y)/q/f'{i:02d}'/f'page_{pages:06d}.json.gz',p)
  out.parent.mkdir(parents=True,exist_ok=True)
  with gzip.open(out,'at',encoding='utf-8') as f:
   for x in items: f.write(json.dumps(norm(x,y,q,t),ensure_ascii=False)+'\n')
  found+=len(items); nxt=m.get('next-cursor'); done=len(items)<ROWS
  checkpoint(cp,{'cursor':nxt,'pages':pages,'records':found,'completed':done,'updated_at':now()})
  if done: cur=nxt or 'END_SHORT_PAGE'; break
  if not nxt or nxt==cur: err='missing_or_repeated_next_cursor'; break
  cur=nxt; time.sleep(.15+random.random()*.2)
 if not done and not err: err='workflow_deadline_reached'
 res={'query_group':q,'query_text':t,'pages_completed':pages,'records_found':found,'cursor_start':'*','cursor_end':cur,'completed':done,'started_at':start,'finished_at':now(),'error':err}
 checkpoint(cp,{'cursor':cur,'pages':pages,'records':found,'completed':done,'result':res,'updated_at':now()}); return res

def merge(root,y):
 rec={}
 for p in (root/'normalized'/'crossref'/str(y)).glob('**/[0-9][0-9].jsonl.gz'):
  with gzip.open(p,'rt',encoding='utf-8') as f:
   for line in f:
    x=json.loads(line); k=x.get('doi_normalized') or x['source_external_id']
    if k in rec:
     rec[k]['query_groups']=sorted(set(rec[k]['query_groups'])|set(x['query_groups'])); rec[k]['query_texts']=sorted(set(rec[k]['query_texts'])|set(x['query_texts']))
    else: rec[k]=x
 out=root/'normalized'/'crossref'/str(y)/'paper_master_crossref.jsonl.gz'
 with gzip.open(out,'wt',encoding='utf-8') as f:
  for k in sorted(rec): f.write(json.dumps(rec[k],ensure_ascii=False)+'\n')
 return len(rec),out

def main():
 a=argparse.ArgumentParser(); a.add_argument('--year',type=int,required=True); a.add_argument('--output',type=Path,required=True); a.add_argument('--hours',type=float,default=5.5); z=a.parse_args()
 z.output.mkdir(parents=True,exist_ok=True); started=now(); dl=time.monotonic()+z.hours*3600; s=session(); results=[]
 for q,terms in Q.items():
  for i,t in enumerate(terms,1):
   r=crawl(s,z.output,z.year,q,t,i,dl); results.append(r)
   if r['error']=='workflow_deadline_reached': break
  if results[-1]['error']=='workflow_deadline_reached': break
 n,master=merge(z.output,z.year); man=z.output/'manifests'/f'crossref_{z.year}_search_queries.csv'; man.parent.mkdir(parents=True,exist_ok=True)
 with man.open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(results[0])); w.writeheader(); w.writerows(results)
 expected=sum(map(len,Q.values())); complete=len(results)==expected and all(x['completed'] for x in results)
 summary={'run_id':f'crossref-{z.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}','source':'Crossref','year':z.year,'subqueries_expected':expected,'subqueries_attempted':len(results),'subqueries_completed':sum(x['completed'] for x in results),'pages_completed':sum(x['pages_completed'] for x in results),'raw_records':sum(x['records_found'] for x in results),'unique_records':n,'completed':complete,'started_at':started,'finished_at':now(),'errors':[x for x in results if x['error']],'master_path':str(master.relative_to(z.output)),'manifest_path':str(man.relative_to(z.output))}
 p=z.output/'completion'/f'crossref_{z.year}_summary.json'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
