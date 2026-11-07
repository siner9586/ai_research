from __future__ import annotations
import argparse, csv, gzip, hashlib, json, os, random, time
from datetime import datetime, timezone
from pathlib import Path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API="https://api.crossref.org/works"
ROWS=1000

def now(): return datetime.now(timezone.utc).isoformat()

def session():
    retry=Retry(total=8,connect=8,read=8,status=8,backoff_factor=1,
        status_forcelist=(429,500,502,503,504),allowed_methods=frozenset({"GET"}),
        respect_retry_after_header=True,raise_on_status=False)
    s=requests.Session(); s.mount("https://",HTTPAdapter(max_retries=retry))
    mail=os.getenv("CROSSREF_MAILTO") or os.getenv("UNPAYWALL_EMAIL")
    ua="ExplainabilityBiasOpenEvidence/2.1 targeted-retry"+(f" (mailto:{mail})" if mail else "")
    s.headers.update({"User-Agent":ua,"Accept":"application/json"})
    return s

def fingerprint(items):
    ids=[str(x.get("DOI") or x.get("URL") or hashlib.sha256(json.dumps(x,sort_keys=True).encode()).hexdigest()) for x in items]
    return hashlib.sha256("\n".join(ids).encode()).hexdigest()

def save(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding="utf-8")

def crawl(s,spec,out,deadline):
    year=int(spec["year"]); group=spec["query_group"]; idx=int(spec["term_index"]); text=spec["query_text"]
    cursor=spec["cursor"]; prior_pages=int(spec.get("prior_pages",0)); prior_records=int(spec.get("prior_records",0))
    pages=0; records=0; seen=set(); error=None; completed=False; attempts=0; started=now()
    rawdir=out/"raw"/str(year)/group/f"{idx:02d}"
    while time.monotonic()<deadline:
        end="2026-07-24" if year==2026 else f"{year}-12-31"
        try:
            r=s.get(API,params={"query.bibliographic":text,
                "filter":f"from-pub-date:{year}-01-01,until-pub-date:{end}",
                "rows":ROWS,"cursor":cursor},timeout=(30,180))
        except requests.RequestException as exc:
            error=f"network:{type(exc).__name__}:{exc}"; break
        attempts+=1
        if r.status_code!=200:
            error=f"http_{r.status_code}:{r.text[:500]}"; break
        try: payload=r.json()
        except ValueError as exc:
            error=f"invalid_json:{exc}"; break
        message=payload.get("message") or {}; items=message.get("items") or []
        fp=fingerprint(items)
        if items and fp in seen:
            error="repeated_page_content"; break
        seen.add(fp); pages+=1
        rawdir.mkdir(parents=True,exist_ok=True)
        with gzip.open(rawdir/f"page_{prior_pages+pages:06d}.json.gz","wt",encoding="utf-8") as h:
            json.dump(payload,h,ensure_ascii=False)
        records+=len(items)
        nxt=message.get("next-cursor")
        completed=len(items)<ROWS
        cursor=nxt or ("END_SHORT_PAGE" if completed else cursor)
        save(out/"checkpoints"/str(year)/group/f"{idx:02d}.json",{
            "cursor":cursor,"incremental_pages":pages,"incremental_records":records,
            "total_pages":prior_pages+pages,"total_records":prior_records+records,
            "completed":completed,"updated_at":now()})
        if completed: break
        if not nxt: error="missing_next_cursor_on_full_page"; break
        time.sleep(.3+random.random()*.3)
    if not completed and not error: error="workflow_deadline_reached"
    return {"year":year,"query_group":group,"term_index":idx,"query_text":text,
        "cursor_start":spec["cursor"],"cursor_end":cursor,"prior_pages":prior_pages,
        "prior_records":prior_records,"incremental_pages":pages,"incremental_records":records,
        "total_pages":prior_pages+pages,"total_records":prior_records+records,
        "request_attempts":attempts,"completed":completed,"error":error,
        "started_at":started,"finished_at":now(),
        "official_endpoint":API,
        "official_end_evidence":"short page (<1000 records)" if completed else None}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--year",type=int,required=True)
    ap.add_argument("--specs",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--hours",type=float,default=5.5)
    args=ap.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    specs=[x for x in json.loads(args.specs.read_text(encoding="utf-8")) if int(x["year"])==args.year]
    s=session(); deadline=time.monotonic()+args.hours*3600; results=[]
    for spec in specs:
        result=crawl(s,spec,args.output,deadline); results.append(result)
        if result["error"]=="workflow_deadline_reached": break
    completed=len(results)==len(specs) and all(x["completed"] for x in results)
    summary={"run_id":f"crossref-targeted-retry-{args.year}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}",
        "source":"Crossref","year":args.year,"targets_expected":len(specs),
        "targets_attempted":len(results),"targets_completed":sum(x["completed"] for x in results),
        "completed":completed,"results":results,
        "errors":[x for x in results if x["error"]],
        "official_completion_rule":"every targeted cursor chain ends on an official short page"}
    save(args.output/f"crossref_{args.year}_targeted_retry_summary.json",summary)
    with (args.output/f"crossref_{args.year}_targeted_retry_manifest.csv").open("w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(results[0].keys())); w.writeheader(); w.writerows(results)
    print(json.dumps(summary,ensure_ascii=False,indent=2))
    if not completed: raise SystemExit(2)

if __name__=="__main__": main()
