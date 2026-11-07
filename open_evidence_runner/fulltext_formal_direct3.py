from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

TARGETS = [
    {"paper_id":"arxiv:2604.01114","title":"Trust and Reliance on AI in Education: AI Literacy and Need for Cognition as Moderators","doi":"10.48550/arxiv.2604.01114","url":"https://arxiv.org/pdf/2604.01114v3","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2604.03237","title":"The Persuasion Paradox: When LLM Explanations Fail to Improve Human-AI Team Performance","doi":"10.48550/arxiv.2604.03237","url":"https://arxiv.org/pdf/2604.03237v1","version":"preprint","license":"arXiv"},
    {"paper_id":"arxiv:2604.23896","title":"From Trust to Appropriate Reliance: Measurement Constructs in Human-AI Decision-Making","doi":"10.48550/arxiv.2604.23896","url":"https://arxiv.org/pdf/2604.23896v1","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2605.31275","title":"Personalized to Persuade: The Effects of Contextualization and Warmth on Trust and Reliance in Conversational AI","doi":"10.48550/arxiv.2605.31275","url":"https://arxiv.org/pdf/2605.31275","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2606.14406","title":"Friction in AI-Assisted Clinical Decision-Making: A Case Study on The Role of Questions and What-if Scenarios","doi":"10.48550/arxiv.2606.14406","url":"https://arxiv.org/pdf/2606.14406v1","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2509.08010","title":"Measuring and mitigating overreliance is necessary for building human-compatible AI","doi":"10.48550/arxiv.2509.08010","url":"https://arxiv.org/pdf/2509.08010v2","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2302.02187","title":"Appropriate Reliance on AI Advice: Conceptualization and the Effect of Explanations","doi":"10.48550/arxiv.2302.02187","url":"https://arxiv.org/pdf/2302.02187v3","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2304.08804","title":"AI Reliance and Decision Quality: Fundamentals, Interdependence, and the Effects of Interventions","doi":"10.48550/arxiv.2304.08804","url":"https://arxiv.org/pdf/2304.08804v4","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2310.02108","title":"Towards Effective Human-AI Decision-Making: The Role of Human Learning in Appropriate Reliance on AI Advice","doi":"10.48550/arxiv.2310.02108","url":"https://arxiv.org/pdf/2310.02108v1","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:2209.11812","title":"On Explanations, Fairness, and Appropriate Reliance in Human-AI Decision-Making","doi":"10.48550/arxiv.2209.11812","url":"https://arxiv.org/pdf/2209.11812v5","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:1901.09392","title":"On the (In)fidelity and Sensitivity of Explanations","doi":"10.48550/arxiv.1901.09392","url":"https://arxiv.org/pdf/1901.09392","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"arxiv:1810.03292","title":"Sanity Checks for Saliency Maps","doi":"10.48550/arxiv.1810.03292","url":"https://arxiv.org/pdf/1810.03292","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.1109/CVPR46437.2021.00084","title":"Transformer Interpretability Beyond Attention Visualization","doi":"10.1109/CVPR46437.2021.00084","url":"https://arxiv.org/pdf/2012.09838","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.1109/ICCV48922.2021.00045","title":"Generic Attention-Model Explainability for Interpreting Bi-Modal and Encoder-Decoder Transformers","doi":"10.1109/ICCV48922.2021.00045","url":"https://arxiv.org/pdf/2103.15679","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.1162/tacl_a_00349","title":"A Primer in BERTology: What We Know About How BERT Works","doi":"10.1162/tacl_a_00349","url":"https://arxiv.org/pdf/2002.12327","version":"preprint","license":"arXiv-hosted"},
    {"paper_id":"doi:10.18653/v1/2020.acl-main.385","title":"Quantifying Attention Flow in Transformers","doi":"10.18653/v1/2020.acl-main.385","url":"https://aclanthology.org/2020.acl-main.385.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"doi:10.18653/v1/2020.acl-main.386","title":"Towards Faithfully Interpretable NLP Systems: How Should We Define and Evaluate Faithfulness?","doi":"10.18653/v1/2020.acl-main.386","url":"https://aclanthology.org/2020.acl-main.386.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"doi:10.18653/v1/2020.acl-main.408","title":"ERASER: A Benchmark to Evaluate Rationalized NLP Models","doi":"10.18653/v1/2020.acl-main.408","url":"https://aclanthology.org/2020.acl-main.408.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"doi:10.18653/v1/2020.acl-main.492","title":"Explaining Black Box Predictions and Unveiling Data Artifacts through Influence Functions","doi":"10.18653/v1/2020.acl-main.492","url":"https://aclanthology.org/2020.acl-main.492.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"doi:10.18653/v1/P19-1282","title":"Is Attention Interpretable?","doi":"10.18653/v1/P19-1282","url":"https://aclanthology.org/P19-1282.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"doi:10.18653/v1/W19-4828","title":"What Does BERT Look at? An Analysis of BERT's Attention","doi":"10.18653/v1/W19-4828","url":"https://aclanthology.org/W19-4828.pdf","version":"publisher","license":"ACL Anthology open access"},
    {"paper_id":"arxiv:1802.08129","title":"Multimodal Explanations: Justifying Decisions and Pointing to the Evidence","doi":"10.48550/arxiv.1802.08129","url":"https://openaccess.thecvf.com/content_cvpr_2018/papers/Park_Multimodal_Explanations_Justifying_CVPR_2018_paper.pdf","version":"publisher","license":"CVF open repository"},
    {"paper_id":"doi:10.1093/jamia/ocab238","title":"Trust in AI: Why We Should Be Designing for Appropriate Reliance","doi":"10.1093/jamia/ocab238","url":"https://europepmc.org/articles/PMC8714273?pdf=render","version":"repository","license":"PMC open article"},
    {"paper_id":"doi:10.1257/pandp.20181022","title":"Human Judgment and AI Pricing","doi":"10.1257/pandp.20181022","url":"https://www.nber.org/system/files/working_papers/w24284/w24284.pdf","version":"working_paper","license":"NBER working paper copyright"},
]

ALLOWED_HOSTS={"arxiv.org","export.arxiv.org","aclanthology.org","www.aclanthology.org","openaccess.thecvf.com","europepmc.org","www.europepmc.org","www.nber.org","nber.org"}
MAX_BYTES=100*1024*1024
URL_RE=re.compile(r"https?://[^\s<>()\]\[{}\"']+",re.I)
AVAILABILITY_PATTERNS=[
    re.compile(r".{0,180}\bdata availability\b.{0,700}",re.I|re.S),
    re.compile(r".{0,180}\bcode availability\b.{0,700}",re.I|re.S),
    re.compile(r".{0,180}\bavailability of data and materials\b.{0,700}",re.I|re.S),
    re.compile(r".{0,180}\bsupplementary (?:material|materials|information)\b.{0,700}",re.I|re.S),
]
REPO_DOMAINS=("github.com","osf.io","zenodo.org","huggingface.co","figshare.com","dataverse","dryad")

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def norm(text:str)->str:
    return re.sub(r"[^a-z0-9]+"," ",text.lower()).strip()

def audit_one(session:requests.Session,target:dict,out:Path)->dict:
    requested_host=(urlparse(target["url"]).hostname or "").lower()
    if requested_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{requested_host}")
    r=session.get(target["url"],timeout=(30,240),allow_redirects=True,stream=True)
    final_host=(urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
    r.raise_for_status()
    content_type=(r.headers.get("content-type") or "").lower()
    filename=re.sub(r"[^A-Za-z0-9._-]+","_",target["paper_id"])+".pdf"
    path=out/filename
    total=0
    with path.open("wb") as f:
        for chunk in r.iter_content(1024*1024):
            if not chunk: continue
            total+=len(chunk)
            if total>MAX_BYTES: raise RuntimeError("file_too_large")
            f.write(chunk)
    magic=path.read_bytes()[:5]
    if magic!=b"%PDF-":
        path.unlink(missing_ok=True)
        raise RuntimeError(f"not_pdf_magic:{magic!r};content_type={content_type}")
    reader=PdfReader(str(path))
    pages=len(reader.pages)
    texts=[]
    for page in reader.pages:
        try: texts.append(page.extract_text() or "")
        except Exception: texts.append("")
    text="\n".join(texts)
    nt=norm(text)
    title_tokens=[t for t in norm(target["title"]).split() if len(t)>3]
    title_ratio=sum(t in nt for t in title_tokens)/max(1,len(title_tokens))
    doi_match=target["doi"].lower() in text.lower()
    status="verified" if pages>0 and (doi_match or title_ratio>=0.45) else "needs_manual_title_review"
    statements=[]
    for pattern in AVAILABILITY_PATTERNS:
        for match in pattern.finditer(text):
            value=re.sub(r"\s+"," ",match.group(0)).strip()[:900]
            if value and value not in statements: statements.append(value)
            if len(statements)>=10: break
        if len(statements)>=10: break
    repo_urls=[]
    for raw in URL_RE.findall(text):
        value=raw.rstrip(".,;:)")
        host=(urlparse(value).hostname or "").lower()
        if any(d in host for d in REPO_DOMAINS) and value not in repo_urls: repo_urls.append(value)
        if len(repo_urls)>=30: break
    return {**target,"requested_url":target["url"],"final_url":r.url,"requested_host":requested_host,"final_host":final_host,"http_status":r.status_code,"content_type":content_type,"size_bytes":total,"sha256":sha256(path),"page_count":pages,"doi_match":doi_match,"title_match_ratio":round(title_ratio,4),"validation_status":status,"local_file":filename,"availability_statements":statements,"repository_urls":repo_urls}

def main()->None:
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,required=True); args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    session=requests.Session(); session.headers.update({"User-Agent":"open-evidence-formal-fulltext/3.0 (lawful OA research archive)"})
    results=[]
    for target in TARGETS:
        try: results.append(audit_one(session,target,args.output))
        except Exception as exc: results.append({**target,"validation_status":"retryable","error":f"{type(exc).__name__}:{exc}"})
    (args.output/"fulltext_audit.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    availability=[{"paper_id":r["paper_id"],"availability_statements":r.get("availability_statements",[]),"repository_urls":r.get("repository_urls",[])} for r in results]
    (args.output/"availability_and_repository_evidence.json").write_text(json.dumps(availability,ensure_ascii=False,indent=2),encoding="utf-8")
    verified=sum(r.get("validation_status")=="verified" for r in results); manual=sum(r.get("validation_status")=="needs_manual_title_review" for r in results); retryable=sum(r.get("validation_status")=="retryable" for r in results)
    summary={"targets":len(results),"verified":verified,"manual_review":manual,"retryable":retryable}
    (args.output/"completion_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))
    if verified==0: raise SystemExit("No lawful OA PDF was verified")

if __name__=="__main__": main()
