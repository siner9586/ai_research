from __future__ import annotations
import argparse,csv,gzip,json,tarfile
from pathlib import Path

def main():
 a=argparse.ArgumentParser(); a.add_argument('--input',type=Path,required=True); a.add_argument('--output',type=Path,required=True); z=a.parse_args(); z.output.mkdir(parents=True,exist_ok=True)
 summaries=[json.loads(p.read_text(encoding='utf-8')) for p in sorted(z.input.glob('**/completion/openalex_*_summary.json'))]
 rec={}
 for p in sorted(z.input.glob('**/normalized/openalex/*/paper_master_openalex.jsonl.gz')):
  with gzip.open(p,'rt',encoding='utf-8') as f:
   for line in f:
    if not line.strip(): continue
    x=json.loads(line); k=x.get('doi_normalized') or x['source_external_id']
    if k in rec:
     rec[k]['query_groups']=sorted(set(rec[k].get('query_groups',[]))|set(x.get('query_groups',[]))); rec[k]['query_texts']=sorted(set(rec[k].get('query_texts',[]))|set(x.get('query_texts',[])))
     for field in ('abstract','oa_pdf_url','landing_url','license','venue','authors'):
      if not rec[k].get(field) and x.get(field): rec[k][field]=x[field]
    else: rec[k]=x
 master=z.output/'openalex_all_paper_master.jsonl.gz'
 with gzip.open(master,'wt',encoding='utf-8') as f:
  for k in sorted(rec): f.write(json.dumps(rec[k],ensure_ascii=False)+'\n')
 manifest=z.output/'openalex_all_search_queries.csv'; paths=sorted(z.input.glob('**/manifests/openalex_*_search_queries.csv')); writer=None
 with manifest.open('w',encoding='utf-8-sig',newline='') as out:
  for p in paths:
   with p.open('r',encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f)
    if writer is None: writer=csv.DictWriter(out,fieldnames=['year']+(r.fieldnames or [])); writer.writeheader()
    year=p.stem.split('_')[1]
    for row in r: writer.writerow({'year':year,**row})
 if writer is None: manifest.write_text('year,query_group\n',encoding='utf-8')
 years=sorted({int(s['year']) for s in summaries}); expected=list(range(2018,2027))
 total={'source':'OpenAlex','years_expected':expected,'years_present':years,'year_runs_completed':sum(bool(s.get('completed')) for s in summaries),'year_runs_total':len(summaries),'subqueries_expected':sum(int(s.get('subqueries_expected',0)) for s in summaries),'subqueries_completed':sum(int(s.get('subqueries_completed',0)) for s in summaries),'pages_completed':sum(int(s.get('pages_completed',0)) for s in summaries),'raw_records':sum(int(s.get('raw_records',0)) for s in summaries),'unique_records':len(rec),'completed':years==expected and all(bool(s.get('completed')) for s in summaries),'errors':[e for s in summaries for e in s.get('errors',[])]}
 summary=z.output/'openalex_all_summary.json'; summary.write_text(json.dumps(total,ensure_ascii=False,indent=2),encoding='utf-8')
 archive=z.output/'openalex_backfill_all.tar.gz'
 with tarfile.open(archive,'w:gz') as tar:
  for p in sorted(z.input.rglob('*')):
   if p.is_file(): tar.add(p,arcname=p.relative_to(z.input))
  for p in (master,manifest,summary): tar.add(p,arcname='aggregate/'+p.name)
 print(json.dumps(total,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
