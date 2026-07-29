from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

TARGETS = [
    {"paper_id":"doi:10.48550/arxiv.2210.08960","title":"Deceptive AI Systems That Give Explanations Are Just as Convincing as Honest AI Systems in Human-Machine Decision Making","doi":"10.48550/arxiv.2210.08960","url":"https://arxiv.org/pdf/2210.08960","version":"preprint","declared_license":None,"arxiv_id":"2210.08960"},
    {"paper_id":"doi:10.48550/arxiv.2602.01264","title":"Shades of Uncertainty: How AI Uncertainty Visualizations Affect Trust in Alzheimer's Predictions","doi":"10.48550/arxiv.2602.01264","url":"https://arxiv.org/pdf/2602.01264","version":"preprint","declared_license":None,"arxiv_id":"2602.01264"},
    {"paper_id":"doi:10.48550/arxiv.2410.03727","title":"FaithEval: Can Your Language Model Stay Faithful to Context, Even If The Moon is Made of Marshmallows","doi":"10.48550/arxiv.2410.03727","url":"https://arxiv.org/pdf/2410.03727","version":"preprint","declared_license":None,"arxiv_id":"2410.03727"},
    {"paper_id":"doi:10.48550/arxiv.2412.11298","title":"The Impact of AI Explanations on Clinicians Trust and Diagnostic Accuracy in Breast Cancer","doi":"10.48550/arxiv.2412.11298","url":"https://arxiv.org/pdf/2412.11298","version":"preprint","declared_license":None,"arxiv_id":"2412.11298"},
    {"paper_id":"doi:10.2196/66760","title":"Investigating Whether AI Will Replace Human Physicians and Understanding the Interplay of the Source of Consultation, Health-Related Stigma, and Explanations of Diagnoses on Patients Evaluations of Medical Consultations: Randomized Factorial Experiment","doi":"10.2196/66760","url":"https://www.jmir.org/2025/1/e66760/PDF","version":"publishedVersion","declared_license":"CC BY"},
    {"paper_id":"doi:10.1038/s41746-025-01958-8","title":"Comparison of SHAP and clinician friendly explanations reveals effects on clinical decision behaviour","doi":"10.1038/s41746-025-01958-8","url":"https://www.nature.com/articles/s41746-025-01958-8.pdf","version":"publishedVersion","declared_license":"CC BY-NC-ND 4.0","article_page":"https://www.nature.com/articles/s41746-025-01958-8"},
    {"paper_id":"doi:10.3390/jemr19030055","title":"Eye-Tracking Evidence That Verifiable Explanations Support Visual Evidence Checking in AI-Assisted Chest Radiograph Interpretation","doi":"10.3390/jemr19030055","url":"https://www.mdpi.com/1995-8692/19/3/55/pdf","version":"publishedVersion","declared_license":"CC BY 4.0","article_page":"https://www.mdpi.com/1995-8692/19/3/55"},
]

ALLOWED_HOSTS={
    "arxiv.org","export.arxiv.org",
    "www.jmir.org","jmir.org",
    "www.nature.com","nature.com","static-content.springer.com","media.springernature.com",
    "www.mdpi.com","mdpi.com","mdpi-res.com","www.mdpi-res.com","pub.mdpi-res.com",
}
MAX_BYTES=120*1024*1024
SUPP_EXTENSIONS={".pdf",".xlsx",".xls",".csv",".zip",".docx",".txt"}


def digest(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()


def norm(text:str)->str:
    return re.sub(r"[^a-z0-9]+"," ",text.lower()).strip()


def safe_name(value:str)->str:
    return re.sub(r"[^A-Za-z0-9._-]+","_",value).strip("_")


def arxiv_license(session:requests.Session, arxiv_id:str)->dict:
    url=f"https://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        r=session.get(url,timeout=(30,180))
        r.raise_for_status()
        root=ET.fromstring(r.content)
        ns={"atom":"http://www.w3.org/2005/Atom","arxiv":"http://arxiv.org/schemas/atom"}
        entry=root.find("atom:entry",ns)
        lic=entry.find("arxiv:license",ns).text if entry is not None and entry.find("arxiv:license",ns) is not None else None
        return {"atom_url":url,"license_url":lic,"atom_sha256":hashlib.sha256(r.content).hexdigest()}
    except Exception as exc:
        return {"atom_url":url,"error":f"{type(exc).__name__}:{exc}"}


def fetch_binary(session:requests.Session,url:str,path:Path)->dict:
    host=(urlparse(url).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowed:{host}")
    with session.get(url,timeout=(45,300),stream=True,allow_redirects=True) as r:
        final_host=(urlparse(r.url).hostname or "").lower()
        if final_host not in ALLOWED_HOSTS:
            raise RuntimeError(f"redirect_host_not_allowed:{final_host}")
        r.raise_for_status()
        total=0
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("wb") as f:
            for chunk in r.iter_content(1024*1024):
                if not chunk:
                    continue
                total+=len(chunk)
                if total>MAX_BYTES:
                    raise RuntimeError("file_exceeds_limit")
                f.write(chunk)
        return {"requested_url":url,"final_url":r.url,"http_status":r.status_code,"content_type":(r.headers.get("content-type") or "").lower(),"size_bytes":total,"sha256":digest(path)}


def validate_pdf(path:Path,target:dict)->dict:
    if path.read_bytes()[:5]!=b"%PDF-":
        raise RuntimeError(f"not_pdf_magic:{path.read_bytes()[:16]!r}")
    reader=PdfReader(str(path))
    if reader.is_encrypted:
        raise RuntimeError("encrypted_pdf")
    pages=len(reader.pages)
    text=[]
    for page in reader.pages[:min(12,pages)]:
        try:
            text.append(page.extract_text() or "")
        except Exception:
            pass
    joined="\n".join(text)
    tokens=[t for t in norm(target["title"]).split() if len(t)>3]
    ratio=sum(t in norm(joined) for t in tokens)/max(1,len(tokens))
    doi_match=target["doi"].lower() in joined.lower()
    status="oa_pdf_verified" if pages>0 and (doi_match or ratio>=0.45) else "needs_manual_title_review"
    return {"page_count":pages,"doi_match":doi_match,"title_match_ratio":round(ratio,4),"validation_status":status,"text_extracted_chars":len(joined)}


def discover_supplements(session:requests.Session,target:dict)->tuple[list[dict],dict]:
    page=target.get("article_page")
    if not page:
        return [],{"status":"not_applicable"}
    host=(urlparse(page).hostname or "").lower()
    if host not in ALLOWED_HOSTS:
        return [],{"status":"host_not_allowed"}
    try:
        r=session.get(page,timeout=(30,180),allow_redirects=True)
        r.raise_for_status()
    except Exception as exc:
        return [],{"status":"retryable","error":f"{type(exc).__name__}:{exc}"}
    final_host=(urlparse(r.url).hostname or "").lower()
    if final_host not in ALLOWED_HOSTS:
        return [],{"status":"retryable","error":f"redirect_host_not_allowed:{final_host}"}
    soup=BeautifulSoup(r.text,"html.parser")
    found=[]
    seen=set()
    for a in soup.find_all("a",href=True):
        href=urljoin(r.url,a["href"])
        text=" ".join(a.get_text(" ",strip=True).split())
        lower=(href+" "+text).lower()
        if not any(k in lower for k in ("supplement","supplementary","moesm","/s1")):
            continue
        h=(urlparse(href).hostname or "").lower()
        if h not in ALLOWED_HOSTS or href in seen:
            continue
        seen.add(href)
        found.append({"url":href,"anchor_text":text})
    return found,{"status":"completed","page_url":r.url,"page_sha256":hashlib.sha256(r.content).hexdigest(),"links_found":len(found)}


def main()->None:
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    a.output.mkdir(parents=True,exist_ok=True)
    pdf_dir=a.output/"pdfs";supp_dir=a.output/"supplements"
    session=requests.Session()
    retry=Retry(total=4,connect=4,read=4,status=3,backoff_factor=3,status_forcelist=(429,500,502,503,504),allowed_methods=frozenset({"GET","HEAD"}),raise_on_status=False)
    session.mount("https://",HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent":"ExplainabilityBiasOpenEvidence/3.0 lawful-fulltext-audit"})
    results=[];supplements=[]
    for target in TARGETS:
        item={**target}
        if target.get("arxiv_id"):
            item["arxiv_metadata"]=arxiv_license(session,target["arxiv_id"])
        filename=safe_name(target["paper_id"])+".pdf"
        path=pdf_dir/filename
        try:
            item["transfer"]=fetch_binary(session,target["url"],path)
            item.update(validate_pdf(path,target))
            item["local_file"]=str(path.relative_to(a.output))
        except Exception as exc:
            path.unlink(missing_ok=True)
            item["validation_status"]="retryable"
            item["error"]=f"{type(exc).__name__}:{exc}"
        links,page_audit=discover_supplements(session,target)
        item["supplement_discovery"]=page_audit
        for idx,link in enumerate(links,1):
            parsed=Path(urlparse(link["url"]).path)
            suffix=parsed.suffix.lower()
            if suffix not in SUPP_EXTENSIONS:
                suffix=".bin"
            out=supp_dir/(safe_name(target["paper_id"])+f"_supp_{idx:02d}"+suffix)
            row={"paper_id":target["paper_id"],**link,"local_file":str(out.relative_to(a.output))}
            try:
                row["transfer"]=fetch_binary(session,link["url"],out)
                magic=out.read_bytes()[:16]
                if out.suffix.lower()==".pdf" and magic[:5]!=b"%PDF-":
                    raise RuntimeError(f"supplement_not_pdf:{magic!r}")
                if out.suffix.lower() in {".xlsx",".zip",".docx"} and magic[:2]!=b"PK":
                    raise RuntimeError(f"supplement_not_zip_container:{magic!r}")
                row["validation_status"]="verified"
            except Exception as exc:
                out.unlink(missing_ok=True)
                row["validation_status"]="retryable"
                row["error"]=f"{type(exc).__name__}:{exc}"
            supplements.append(row)
        results.append(item)
    summary={
        "targets":len(results),
        "oa_pdf_verified":sum(r.get("validation_status")=="oa_pdf_verified" for r in results),
        "manual_review":sum(r.get("validation_status")=="needs_manual_title_review" for r in results),
        "retryable":sum(r.get("validation_status")=="retryable" for r in results),
        "supplements_discovered":len(supplements),
        "supplements_verified":sum(r.get("validation_status")=="verified" for r in supplements),
        "supplements_retryable":sum(r.get("validation_status")=="retryable" for r in supplements),
    }
    (a.output/"fulltext_audit.json").write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    (a.output/"supplement_audit.json").write_text(json.dumps(supplements,ensure_ascii=False,indent=2),encoding="utf-8")
    (a.output/"completion_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    sums=[]
    for path in sorted(x for x in a.output.rglob("*") if x.is_file() and x.name!="SHA256SUMS.txt"):
        sums.append(f"{digest(path)}  {path.relative_to(a.output)}")
    (a.output/"SHA256SUMS.txt").write_text("\n".join(sums)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    if summary["oa_pdf_verified"]==0:
        raise SystemExit("No fulltext verified")

if __name__=="__main__":
    main()
