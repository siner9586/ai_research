from __future__ import annotations
import argparse,csv,gzip,json,tarfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument('--input',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    summaries=[json.loads(x.read_text(encoding='utf-8')) for x in sorted(a.input.glob('**/completion/arxiv_*_summary.json'))]
    records={}
    for path in sorted(a.input.glob('**/normalized/arxiv/*/paper_master_arxiv.jsonl.gz')):
        with gzip.open(path,'rt',encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                row=json.loads(line); key=row['arxiv_id']
                if key in records:
                    groups=sorted(set(records[key].get('query_groups',[]))|set(row.get('query_groups',[])))
                    queries=sorted(set(records[key].get('query_texts',[]))|set(row.get('query_texts',[])))
                    if (row.get('updated_date') or '') > (records[key].get('updated_date') or ''): records[key]=row
                    records[key]['query_groups']=groups; records[key]['query_texts']=queries
                else: records[key]=row
    master=a.output/'arxiv_all_paper_master.jsonl.gz'
    with gzip.open(master,'wt',encoding='utf-8') as f:
        for key in sorted(records): f.write(json.dumps(records[key],ensure_ascii=False)+'\n')
    manifest=a.output/'arxiv_all_search_queries.csv'; writer=None
    with manifest.open('w',encoding='utf-8-sig',newline='') as out:
        for path in sorted(a.input.glob('**/manifests/arxiv_*_search_queries.csv')):
            with path.open('r',encoding='utf-8-sig',newline='') as f:
                reader=csv.DictReader(f)
                if writer is None: writer=csv.DictWriter(out,fieldnames=['year']+(reader.fieldnames or [])); writer.writeheader()
                year=path.stem.split('_')[1]
                for row in reader: writer.writerow({'year':year,**row})
    if writer is None: manifest.write_text('year,query_group\n',encoding='utf-8')
    years=sorted({int(s['year']) for s in summaries}); expected=list(range(2018,2027))
    total={'source':'arXiv','years_expected':expected,'years_present':years,'year_runs_completed':sum(bool(s.get('completed')) for s in summaries),'year_runs_total':len(summaries),'query_groups_expected':sum(int(s.get('query_groups_expected',0)) for s in summaries),'query_groups_completed':sum(int(s.get('query_groups_completed',0)) for s in summaries),'pages_completed':sum(int(s.get('pages_completed',0)) for s in summaries),'raw_records':sum(int(s.get('raw_records',0)) for s in summaries),'unique_records':len(records),'completed':years==expected and all(bool(s.get('completed')) for s in summaries),'errors':[e for s in summaries for e in s.get('errors',[])]}
    summary=a.output/'arxiv_all_summary.json'; summary.write_text(json.dumps(total,ensure_ascii=False,indent=2),encoding='utf-8')
    archive=a.output/'arxiv_backfill_all.tar.gz'
    with tarfile.open(archive,'w:gz') as tar:
        for path in sorted(a.input.rglob('*')):
            if path.is_file(): tar.add(path,arcname=path.relative_to(a.input))
        for path in (master,manifest,summary): tar.add(path,arcname='aggregate/'+path.name)
    print(json.dumps(total,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
