from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

PDF_TARGETS = [
    {"paper_id":"doi:10.1007/s44163-026-01219-x","title":"Building trustworthy Artificial Intelligence through transparency explainability uncertainty and trust calibration","doi":"10.1007/s44163-026-01219-x","urls":["https://link.springer.com/content/pdf/10.1007/s44163-026-01219-x.pdf"],"version":"publisher","license":"Open access"},
    {"paper_id":"doi:10.1016/j.chbr.2026.101021","title":"How cultural cognition affects trust and perceived quality of AI explanations","doi":"10.1016/j.chbr.2026.101021","urls":["https://www.sciencedirect.com/science/article/pii/S2451958826000953/pdfft?isDTMRedir=true&download=true"],"version":"publisher","license":"Creative Commons open access"},
    {"paper_id":"doi:10.1016/j.chbr.2026.101024","title":"Trust behavior in AI emerges from distrust in humans: A machine learning study on decision-making guidance","doi":"10.1016/j.chbr.2026.101024","urls":["https://www.sciencedirect.com/science/article/pii/S2451958826000989/pdfft?isDTMRedir=true&download=true"],"version":"publisher","license":"CC BY"},
    {"paper_id":"doi:10.1016/j.ijhcs.2026.103775","title":"Trust the Explanation or my Expectation? Effects of Output Accuracy and Explanations on Expectation Violations and Trust in AI-Supported Decisions","doi":"10.1016/j.ijhcs.2026.103775","urls":["https://www.sciencedirect.com/science/article/pii/S1071581926000509/pdfft?isDTMRedir=true&download=true"],"version":"publisher","license":"publisher open access"},
    {"paper_id":"doi:10.1038/s41598-026-59232-0","title":"HCCD-DS v2: a transparent synthetic benchmark for human-AI decision support under contextual uncertainty","doi":"10.1038/s41598-026-59232-0","urls":["https://www.nature.com/articles/s41598-026-59232-0.pdf"],"version":"publisher","license":"CC BY 4.0"},
    {"paper_id":"doi:10.1080/00140139.2026.2634115","title":"Effects of AI explanations on trust and reliance: a study in job shop scheduling","doi":"10.1080/00140139.2026.2634115","urls":["https://www.tandfonline.com/doi/pdf/10.1080/00140139.2026.2634115?download=true"],"version":"publisher","license":"CC BY 4.0"},
    {"paper_id":"doi:10.1080/0144929X.2026.2662402","title":"Aligning explanations with human values: context-sensitive trust calibration in AI decision systems","doi":"10.1080/0144929X.2026.2662402","urls":["https://www.tandfonline.com/doi/pdf/10.1080/0144929X.2026.2662402?download=true"],"version":"publisher","license":"publisher open access"},
    {"paper_id":"doi:10.1145/3772318.3790632","title":"Guided Reflection in AI-Assisted Decision-Making: Effects on AI Overreliance and Decision Accuracy","doi":"10.1145/3772318.3790632","urls":["https://dl.acm.org/doi/pdf/10.1145/3772318.3790632"],"version":"publisher","license":"CC BY 4.0"},
    {"paper_id":"doi:10.1145/3772318.3791467","title":"Do People Appropriately Rely on AI-Advice? An Analytical Review of HCI Research on Human-AI Decision-Making","doi":"10.1145/3772318.3791467","urls":["https://research-portal.uu.nl/files/291643452/3772318.3791467.pdf"],"version":"institutional_repository","license":"CC BY"},
    {"paper_id":"doi:10.1145/3772363.3798555","title":"Understanding the Affordances of Control in AI Reasoning for Human-AI Decision-Making","doi":"10.1145/3772363.3798555","urls":["https://dl.acm.org/doi/pdf/10.1145/3772363.3798555"],"version":"publisher","license":"CC BY 4.0"},
    {"paper_id":"doi:10.1145/3772363.3798834","title":"Understanding Interactive Model Engagement for Appropriate Reliance: An Exploration of AI-Assisted Decision Support in Customer Classification","doi":"10.1145/3772363.3798834","urls":["https://dl.acm.org/doi/pdf/10.1145/3772363.3798834"],"version":"publisher","license":"publisher-page-open"},
    {"paper_id":"doi:10.1145/3772363.3798835","title":"Trust to Reliance: Measurement Constructs for Human-AI Appropriate Reliance","doi":"10.1145/3772363.3798835","urls":["https://dl.acm.org/doi/pdf/10.1145/3772363.3798835"],"version":"publisher","license":"publisher-page-open"},
    {"paper_id":"ssrn:6845387","title":"How is Reliance on AI Measured? Mapping and Evaluating Measurement Approaches in Human-AI Interaction","doi":"","urls":["https://papers.ssrn.com/sol3/Delivery.cfm/6845387.pdf?abstractid=6845387"],"version":"working_paper","license":"SSRN publicly posted working paper"},
    {"paper_id":"doi:10.1038/s41597-025-04664-y","title":"A benchmarking framework and dataset for learning to defer in human-AI decision-making","doi":"10.1038/s41597-025-04664-y","urls":["https://www.nature.com/articles/s41597-025-04664-y.pdf"],"version":"publisher","license":"Nature open access"},
    {"paper_id":"doi:10.1038/s41746-025-02023-0","title":"The human factor in explainable artificial intelligence: clinician variability in trust, reliance, and performance","doi":"10.1038/s41746-025-02023-0","urls":["https://www.nature.com/articles/s41746-025-02023-0.pdf"],"version":"publisher","license":"Nature open access"},
    {"paper_id":"doi:10.1609/aaai.v32i1.11353","title":"Building More Explainable Artificial Intelligence With Argumentation","doi":"10.1609/aaai.v32i1.11353","urls":["https://ojs.aaai.org/index.php/AAAI/article/download/11353/11212"],"version":"publisher","license":"AAAI open proceedings"},
]

HTML_TARGETS = [
    {"paper_id":"doi:10.1093/jamia/ocag082","title":"Explainability in context: calibrating appropriate trust and reliance in artificial intelligence","doi":"10.1093/jamia/ocag082","url":"https://academic.oup.com/jamia/article/33/8/1554/8694719","version":"publisher_html","license":"CC BY-NC 4.0"},
    {"paper_id":"doi:10.23915/distill.00010","title":"The Building Blocks of Interpretability","doi":"10.23915/distill.00010","url":"https://distill.pub/2018/building-blocks/","version":"publisher_html","license":"CC BY 4.0"},
]

ALLOWED_HOSTS={
    "link.springer.com","static-content.springer.com","media.springernature.com","www.nature.com","nature.com",
    "www.sciencedirect.com","sciencedirect.com","pdf.sciencedirectassets.com","ars.els-cdn.com",
    "www.tandfonline.com","tandfonline.com","www.tandf.co.uk",
    "dl.acm.org","delivery.acm.org","research-portal.uu.nl",
    "papers.ssrn.com","deliverypdf.ssrn.com",
    "ojs.aaai.org","academic.oup.com","distill.pub","www.distill.pub",
}
MAX_BYTES=120*1024*1024
URL_RE=re.compile(r"https?://[^\s<>()\]\[{}\"']+",re.I)
AVAILABILITY_PATTERNS=[
    re.compile(r".{0,180}\bdata availability\b.{0,800}",re.I|re.S),
    re.compile(r".{0,180}\bcode availability\b.{0,800}",re.I|re.S),
    re.compile(r".{0,180}\bavailability of data and materials\b.{0,800}",re.I|re.S),
    re.compile(r".{0,180}\bsupplementary (?:material|materials|information)\b.{0,800}",re.I|re.S),
]
REPO_DOMAINS=("github.com","osf.io","zenodo.org","huggingface.co","figshare.com","dataverse","dryad")

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()

def norm(text:str)->str:
    return re.sub(r"[^a-z0-9]+"," ",text.lower()).strip()

def extract_evidence(text:str)->tuple[list[str],list[str]]:
    statements=[]
    for pattern in AVAILABILITY_PATTERNS:
        for match in pattern.finditer(text):
            value=re.sub(r"\s+"," ",match.group(0)).strip()[:1000]
            if value and value not in statements: statements.append(value)
            if len(statements)>=10: break
        if len(statements)>=10: break
    repo_urls=[]
    for raw in URL_RE.findall(text):
        value=raw.rstrip(".,;:)")
        host=(urlparse(value).hostname or "").lower()
        if any(d in host for d in REPO_DOMAINS) and value not in repo_urls: repo_urls.append(value)
        if len(repo_urls)>=30: break
    return statements,repo_urls

def get_checked(session:requests.Session,url:str,stream:bool=True)->requests.Response:
    requested_host=(urlparse(url).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS: raise RuntimeError(f"host_not_allowed:{requested_host}")
    r=session.get(url,timeout=(30,240),allow_redirects=True,stream=stream)
    final_host=(urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS: raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    r.raise_for_status()
    return r

def audit_pdf(session:requests.Session,target:dict,out:Path)->dict:
    filename=re.sub(r"[^A-Za-z0-9._-]+","_",target["paper_id"])+".pdf"; path=out/filename
    attempts=[]; response=None
    for url in target["urls"]:
        try: response=get_checked(session,url,True); break
        except Exception as exc: attempts.append({"url":url,"error":f"{type(exc).__name__}:{exc}"})
    if response is None: raise RuntimeError(json.dumps(attempts,ensure_ascii=False))
    total=0
    with path.open("wb") as f:
        for chunk in response.iter_content(1024*1024):
            if not chunk: continue
            total+=len(chunk)
            if total>MAX_BYTES: raise RuntimeError("file_too_large")
            f.write(chunk)
    content_type=(response.headers.get("content-type") or "").lower()
    if path.read_bytes()[:5]!=b"%PDF-":
        path.unlink(missing_ok=True); raise RuntimeError(f"not_pdf_magic;content_type={content_type}")
    reader=PdfReader(str(path)); pages=len(reader.pages); texts=[]
    for page in reader.pages:
        try: texts.append(page.extract_text() or "")
        except Exception: texts.append("")
    text="\n".join(texts); nt=norm(text); tokens=[t for t in norm(target["title"]).split() if len(t)>3]
    ratio=sum(t in nt for t in tokens)/max(1,len(tokens)); doi_match=bool(target["doi"]) and target["doi"].lower() in text.lower()
    status="verified" if pages>0 and (doi_match or ratio>=0.45) else "needs_manual_title_review"
    statements,repos=extract_evidence(text)
    return {**target,"requested_url":target["urls"][0],"final_url":response.url,"http_status":response.status_code,"content_type":content_type,"size_bytes":total,"sha256":sha256(path),"page_count":pages,"doi_match":doi_match,"title_match_ratio":round(ratio,4),"validation_status":status,"local_file":filename,"attempt_failures_before_success":attempts,"availability_statements":statements,"repository_urls":repos,"file_kind":"pdf"}

def audit_html(session:requests.Session,target:dict,out:Path)->dict:
    r=get_checked(session,target["url"],False); data=r.content
    if len(data)>MAX_BYTES: raise RuntimeError("html_too_large")
    content_type=(r.headers.get("content-type") or "").lower()
    if "html" not in content_type and b"<html" not in data[:5000].lower(): raise RuntimeError(f"not_html:{content_type}")
    text=re.sub(r"<script.*?</script>|<style.*?</style>"," ",data.decode(r.encoding or "utf-8",errors="replace"),flags=re.I|re.S)
    plain=re.sub(r"<[^>]+>"," ",text); plain=re.sub(r"\s+"," ",plain)
    tokens=[t for t in norm(target["title"]).split() if len(t)>3]; ratio=sum(t in norm(plain) for t in tokens)/max(1,len(tokens)); doi_match=target["doi"].lower() in plain.lower()
    status="publisher_html_verified" if (doi_match or ratio>=0.6) and len(plain)>5000 else "needs_manual_title_review"
    filename=re.sub(r"[^A-Za-z0-9._-]+","_",target["paper_id"])+".html"; path=out/filename; path.write_bytes(data)
    statements,repos=extract_evidence(plain)
    return {**target,"requested_url":target["url"],"final_url":r.url,"http_status":r.status_code,"content_type":content_type,"size_bytes":len(data),"sha256":sha256(path),"doi_match":doi_match,"title_match_ratio":round(ratio,4),"validation_status":status,"local_file":filename,"availability_statements":statements,"repository_urls":repos,"file_kind":"html"}

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,required=True); args=parser.parse_args(); args.output.mkdir(parents=True,exist_ok=True)
    session=requests.Session(); session.headers.update({"User-Agent":"open-evidence-formal-publisher/4.0 (lawful OA research archive)"})
    results=[]
    for t in PDF_TARGETS:
        try: results.append(audit_pdf(session,t,args.output))
        except Exception as exc: results.append({**t,"file_kind":"pdf","validation_status":"retryable","error":f"{type(exc).__name__}:{exc}"})
    for t in HTML_TARGETS:
        try: results.append(audit_html(session,t,args.output))
        except Exception as exc: results.append({**t,"file_kind":"html","validation_status":"retryable","error":f"{type(exc).__name__}:{exc}"})
    (args.output/"fulltext_audit.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    (args.output/"availability_and_repository_evidence.json").write_text(json.dumps([{"paper_id":r["paper_id"],"availability_statements":r.get("availability_statements",[]),"repository_urls":r.get("repository_urls",[])} for r in results],ensure_ascii=False,indent=2),encoding="utf-8")
    verified=sum(r.get("validation_status") in {"verified","publisher_html_verified"} for r in results); manual=sum(r.get("validation_status")=="needs_manual_title_review" for r in results); retryable=sum(r.get("validation_status")=="retryable" for r in results)
    summary={"targets":len(results),"verified":verified,"manual_review":manual,"retryable":retryable,"pdf_targets":len(PDF_TARGETS),"html_targets":len(HTML_TARGETS)}
    (args.output/"completion_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8"); print(json.dumps(summary,indent=2))
    if verified==0: raise SystemExit("No lawful fulltext verified")

if __name__=="__main__": main()
