from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

import requests

TARGETS = [
    {"resource_type":"dataset","resource_id":"qanta-challenge/qanta25-gamedata","relation":"linked_research_dataset","paper_id":"doi:10.18653/v1/2026.findings-acl.422"},
    {"resource_type":"model","resource_id":"google/gemma-3-4b-it","relation":"third_party_model_dependency","paper_id":"arxiv:2602.04003"},
    {"resource_type":"model","resource_id":"meta-llama/Llama-3.3-70B-Instruct","relation":"third_party_model_dependency","paper_id":"arxiv:2602.04003"},
    {"resource_type":"model","resource_id":"mistralai/Mistral-7B-Instruct-v0.3","relation":"third_party_model_dependency","paper_id":"arxiv:2602.04003"},
]


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda:handle.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    out=Path('huggingface-resource-audit')
    raw=out/'raw_api'
    out.mkdir(parents=True,exist_ok=True)
    raw.mkdir(parents=True,exist_ok=True)
    session=requests.Session()
    session.headers.update({'User-Agent':'open-evidence-huggingface-audit/1.0 metadata-only research audit','Accept':'application/json'})
    results=[]
    file_rows=[]
    for target in TARGETS:
        plural='datasets' if target['resource_type']=='dataset' else 'models'
        url=f"https://huggingface.co/api/{plural}/{target['resource_id']}"
        response=session.get(url,timeout=(30,180),allow_redirects=True)
        row={**target,'api_url':url,'http_status':response.status_code,'completed':False}
        if response.status_code!=200:
            row['error']=f'HTTP {response.status_code}: {response.text[:500]}'
            results.append(row)
            continue
        data=response.json()
        raw_path=raw/f"{target['resource_type']}__{target['resource_id'].replace('/','__')}.json"
        raw_path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
        card=data.get('cardData') or {}
        siblings=data.get('siblings') or []
        license_value=card.get('license') or data.get('license')
        if isinstance(license_value,list):
            licenses=license_value
        elif license_value:
            licenses=[str(license_value)]
        else:
            licenses=[]
        for sibling in siblings:
            lfs=sibling.get('lfs') or {}
            file_rows.append({
                'resource_type':target['resource_type'],
                'resource_id':target['resource_id'],
                'revision':data.get('sha'),
                'path':sibling.get('rfilename'),
                'size_bytes':sibling.get('size') or lfs.get('size'),
                'blob_id':sibling.get('blobId'),
                'lfs_sha256':lfs.get('sha256'),
                'lfs_pointer_size':lfs.get('pointerSize'),
            })
        row.update({
            'canonical_id':data.get('id') or data.get('modelId'),
            'revision':data.get('sha'),
            'last_modified':data.get('lastModified'),
            'private':data.get('private'),
            'gated':data.get('gated'),
            'disabled':data.get('disabled'),
            'licenses':licenses,
            'license_status':'declared' if licenses else 'not_declared_in_api_card_data',
            'file_count':len(siblings),
            'downloads':data.get('downloads'),
            'likes':data.get('likes'),
            'raw_api_file':str(raw_path.relative_to(out)),
            'raw_api_sha256':sha256_file(raw_path),
            'binary_files_downloaded':False,
            'completed':True,
        })
        results.append(row)
    (out/'resource_audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    with (out/'file_manifest.csv').open('w',encoding='utf-8',newline='') as handle:
        fields=['resource_type','resource_id','revision','path','size_bytes','blob_id','lfs_sha256','lfs_pointer_size']
        writer=csv.DictWriter(handle,fieldnames=fields)
        writer.writeheader(); writer.writerows(file_rows)
    summary={
        'targets':len(TARGETS),
        'completed':sum(bool(row.get('completed')) for row in results),
        'failed':sum(not bool(row.get('completed')) for row in results),
        'file_manifest_rows':len(file_rows),
        'binary_files_downloaded':False,
        'research_dataset_targets':1,
        'third_party_model_dependencies':3,
    }
    (out/'completion_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))
    if summary['completed']==0:
        raise SystemExit('No Hugging Face resource metadata was retrieved')


if __name__=='__main__':
    main()
