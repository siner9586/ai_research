from __future__ import annotations
import argparse,gzip,hashlib,json,re,sqlite3,unicodedata
from pathlib import Path
import numpy as np
import pandas as pd

def norm_doi(x):
 if not isinstance(x,str) or not x.strip(): return None
 return re.sub(r'^(https?://(dx\.)?doi\.org/|doi:\s*)','',x.strip(),flags=re.I).lower()
def norm_arxiv(x):
 if not isinstance(x,str) or not x.strip(): return None
 return re.sub(r'v\d+$','',re.sub(r'^arxiv:','',x.strip().lower()))
def norm_title(x):
 if not isinstance(x,str): return ''
 return ' '.join(re.sub(r'[\W_]+',' ',unicodedata.normalize('NFKC',x).lower(),flags=re.UNICODE).split())
def read_jsonl(path):
 with gzip.open(path,'rt',encoding='utf-8') as f:
  for line in f:
   if line.strip(): yield json.loads(line)
def find(root,suffix):
 hits=list(root.rglob(suffix))
 if not hits: raise FileNotFoundError(suffix)
 return hits[0]
def key(r):
 return ('doi:'+r['doi_normalized'] if r.get('doi_normalized') else 'arxiv:'+r['arxiv_id'] if r.get('arxiv_id') else 'title:'+r['title_norm'] if r.get('title_norm') else r['source_name'].lower().replace(' ','_')+':'+str(r['source_external_id']))
def richness(r): return 10*bool(r.get('doi_normalized'))+8*bool(r.get('arxiv_id'))+6*bool(r.get('abstract'))+min(len(r.get('abstract') or '')/1000,5)+3*bool(r.get('oa_pdf_url'))
def main():
 a=argparse.ArgumentParser(); a.add_argument('--arxiv-root',type=Path,required=True); a.add_argument('--s2-root',type=Path,required=True); a.add_argument('--output',type=Path,required=True); z=a.parse_args(); z.output.mkdir(parents=True,exist_ok=True)
 rows=[]
 for p in [find(z.arxiv_root,'arxiv_all_paper_master.jsonl.gz'),find(z.s2_root,'semantic_scholar_all_paper_master.jsonl.gz')]:
  for r in read_jsonl(p):
   r['doi_normalized']=norm_doi(r.get('doi_normalized')); r['arxiv_id']=norm_arxiv(r.get('arxiv_id')); r['title_norm']=norm_title(r.get('canonical_title'))
   if r.get('source_name')=='Semantic Scholar': r['openalex_id']=None
   rows.append(r)
 groups={}
 for r in rows: groups.setdefault(key(r),[]).append(r)
 merged=[]; duplicates=[]
 for k,rs in groups.items():
  ss=sorted(rs,key=richness,reverse=True); b=dict(ss[0]); b['paper_id']=k; b['source_names']=sorted({r.get('source_name') for r in rs if r.get('source_name')}); b['query_groups']=sorted({q for r in rs for q in (r.get('query_groups') or [])}); b['query_texts']=sorted({q for r in rs for q in (r.get('query_texts') or [])}); b['duplicate_record_count']=len(rs)
  for f in ['doi_normalized','arxiv_id','s2_paper_id','pmid','abstract','canonical_title','publication_date','publication_year','venue','publisher','language','oa_pdf_url','landing_url','url','license','is_oa','oa_status','authors']:
   if not b.get(f):
    for r in ss[1:]:
     if r.get(f): b[f]=r[f]; break
  merged.append(b)
  if len(rs)>1: duplicates.append({'paper_id':k,'record_count':len(rs),'sources':json.dumps(sorted({r.get('source_name') for r in rs if r.get('source_name')}),ensure_ascii=False),'titles':json.dumps(sorted({r.get('canonical_title') or '' for r in rs}),ensure_ascii=False)})
 df=pd.DataFrame([{'paper_id':r['paper_id'],'canonical_title':r.get('canonical_title'),'abstract':r.get('abstract'),'publication_year':r.get('publication_year'),'doi_normalized':r.get('doi_normalized'),'arxiv_id':r.get('arxiv_id'),'s2_paper_id':r.get('s2_paper_id'),'source_names':json.dumps(r.get('source_names',[]),ensure_ascii=False),'query_groups':json.dumps(r.get('query_groups',[]),ensure_ascii=False),'authors':json.dumps(r.get('authors') or [],ensure_ascii=False),'venue':r.get('venue'),'oa_pdf_url':r.get('oa_pdf_url'),'landing_url':r.get('landing_url') or r.get('url'),'is_oa':r.get('is_oa'),'license':r.get('license'),'duplicate_record_count':r.get('duplicate_record_count',1)} for r in merged])
 text=df.canonical_title.fillna('')+'\n'+df.abstract.fillna('')
 pats={
 'ai':r'\b(?:ai|xai|artificial intelligence|machine learning|deep learning|neural network|neural model|transformer|bert|roberta|deberta|gpt|large language model|llm|algorithmic|automated decision|autonomous system|human[- ]ai|human[- ]robot|robotic)\b|人工智能|机器学习|深度学习|神经网络|大语言模型|人机',
 'explanation':r'\b(?:explainable|explanation|interpretability|interpretable|attribution|saliency|shap|lime|integrated gradients|counterfactual|rationale|feature importance|attention rollout|mechanistic interpretability|faithfulness|fidelity|infidelity|sensitivity[- ]?n|completeness|sufficiency|explanation uncertainty|plausibility[- ]faithfulness)\b|可解释|解释忠实|解释稳定|解释偏差|特征归因|机制可解释|反事实解释',
 'behavior':r'\b(?:appropriate reliance|overreliance|underreliance|reliance|trust calibration|calibrated trust|automation bias|advice taking|algorithmic advice|ai advice|decision switching|error correction|error induction|human[- ]ai collaboration|human[- ]ai teaming|human[- ]robot collaboration|decision support|user study|human subject|participants?|experiment|human decision|decision making)\b|适当依赖|过度依赖|信任校准|自动化偏差|算法建议|人机协同|人工复核|管理者信任',
 'domain':r'\b(?:management|managerial|organization|organizational|professional|hiring|recruitment|credit|finance|financial|bankruptcy|marketing|operations|supply chain|maintenance|healthcare|medical|clinical|legal|judicial|policing|risk|audit|governance|responsibility|accountability)\b|管理决策|招聘|信贷|金融|破产|营销|运营|供应链|医疗|司法|治理|责任|审计',
 'resource':r'\b(?:participant[- ]level data|trial[- ]level data|raw data|supplementary data|open data|dataset|data availability|code availability|materials availability|replication package|preregistration|osf|zenodo|github|hugging face|dataverse|figshare|dryad|openicpsr)\b|开放数据|参与者级数据|试次级数据|复现包|代码可用',
 'participant':r'\b(?:participants?|human subjects?|respondents?|users?|workers?|clinicians?|physicians?|judges?|managers?|professionals?)\b|参与者|受试者|用户实验|管理者|专业人员',
 'advice':r'\b(?:ai advice|algorithmic advice|recommendation|prediction|decision support|ranking|assistant|system advice)\b|算法建议|人工智能建议|决策支持|预测|排序',
 'initial':r'\b(?:initial (?:decision|judgment|answer)|final (?:decision|judgment|answer)|revise(?:d)? (?:decision|answer)|switch(?:ed)?|before and after)\b|初始判断|最终决策|修改判断|决策转换',
 'correct':r'\b(?:correct|incorrect|accuracy|error|ground truth|right answer|wrong answer|model performance)\b|正确|错误|准确率|真实标签',
 'code':r'\b(?:github|code availability|source code|repository|implementation)\b|代码|仓库'}
 b={k:text.str.contains(v,case=False,regex=True,na=False) for k,v in pats.items()}; ai,ex,be,do,rex=b['ai'],b['explanation'],b['behavior'],b['domain'],b['resource']; special=text.str.contains(r'\b(?:shap|lime|integrated gradients|attention rollout|feature importance|attribution|saliency|counterfactual explanation)\b|特征归因|反事实解释',case=False,regex=True,na=False); human=text.str.contains(r'human[- ](?:ai|robot)|人机',case=False,regex=True,na=False)
 la=ex&(ai|special); lb=be&(ai|human); lc=do&ai&(be|ex|b['advice']); ld=rex&(ai|ex|be); inc=la|lb|lc|ld; unc=(~inc)&((ai&(ex|be|do|rex))|(ex&be)); exc=~(inc|unc); decision=np.where(inc,'include',np.where(unc,'uncertain','exclude')); matrix=np.column_stack([la,lb,lc,ld]); labels=np.array(['A','B','C','D']); layers=[json.dumps(labels[x].tolist()) for x in matrix]; signals=(ai.astype(int)+ex.astype(int)+be.astype(int)+do.astype(int)+rex.astype(int)).to_numpy(); confidence=np.where(inc,np.minimum(.98,.72+.05*matrix.sum(1)+.02*signals),np.where(unc,np.minimum(.78,.52+.04*signals),np.where(signals==0,.94,.78)))
 reasons=[]; evidence=[]
 for i,d in enumerate(decision):
  ls=labels[matrix[i]].tolist(); reasons.append(json.dumps([f"Strong corpus-layer signal: {','.join(ls)}"] if d=='include' else ['Partial AI/XAI relevance; independent adjudication required'] if d=='uncertain' else ['No substantive explanation, reliance, professional-decision, or open-resource linkage under configured rules']))
  ev=[]
  if df.canonical_title.iat[i]: ev.append({'claim':'title_signal','quote_or_paraphrase':str(df.canonical_title.iat[i])[:500],'section':'title','page':None})
  if d!='exclude' and df.abstract.iat[i]: ev.append({'claim':'abstract_signal','quote_or_paraphrase':str(df.abstract.iat[i])[:500],'section':'abstract','page':None})
  evidence.append(json.dumps(ev,ensure_ascii=False))
 screen=pd.DataFrame({'paper_id':df.paper_id,'screening_stage':'title_abstract','reviewer':'deterministic_high_recall_v1','decision':decision,'corpus_layers':layers,'reasons':reasons,'exclusion_code':np.where(exc,'NO_SUBSTANTIVE_LINK',None),'human_participants':np.where(df.abstract.notna(),b['participant'],None),'ai_advice_present':np.where(df.abstract.notna(),b['advice'],None),'explanation_condition_present':np.where(df.abstract.notna(),ex,None),'initial_decision_available':np.where(df.abstract.notna(),b['initial'],None),'final_decision_available':np.where(df.abstract.notna(),b['initial'],None),'ai_correctness_available':np.where(df.abstract.notna(),b['correct'],None),'participant_level_data_available':np.where(text.str.contains(r'participant[- ]level data|参与者级数据',case=False,regex=True,na=False),True,None),'trial_level_data_available':np.where(text.str.contains(r'trial[- ]level data|试次级数据',case=False,regex=True,na=False),True,None),'code_available':np.where(b['code'],True,None),'model_available':None,'license_status':df.license.fillna('unknown'),'evidence':evidence,'confidence':np.round(confidence,3),'requires_adjudication':unc})
 master=df.merge(screen[['paper_id','decision','corpus_layers','confidence','requires_adjudication']],on='paper_id'); out=z.output
 master.to_csv(out/'paper_master_s2_arxiv_deduplicated.csv.gz',index=False,compression='gzip'); master.to_parquet(out/'paper_master_s2_arxiv_deduplicated.parquet',index=False); screen.to_csv(out/'screening_decisions_title_abstract_v1.csv.gz',index=False,compression='gzip'); screen.to_parquet(out/'screening_decisions_title_abstract_v1.parquet',index=False); pd.DataFrame(duplicates).to_csv(out/'deduplication_audit.csv.gz',index=False,compression='gzip'); pd.DataFrame(duplicates).to_parquet(out/'deduplication_audit.parquet',index=False)
 rng=np.random.default_rng(20260724); excluded=screen[screen.decision=='exclude']; audit=excluded.iloc[rng.choice(len(excluded),size=max(1,round(len(excluded)*.10)),replace=False)].sort_values('paper_id'); audit.to_csv(out/'excluded_reverse_audit_sample_10pct.csv.gz',index=False,compression='gzip'); audit.to_parquet(out/'excluded_reverse_audit_sample_10pct.parquet',index=False)
 with sqlite3.connect(out/'open_evidence_s2_arxiv.sqlite') as con: master.to_sql('paper_master',con,index=False,chunksize=1000); screen.to_sql('screening_decisions',con,index=False,chunksize=1000); pd.DataFrame(duplicates).to_sql('deduplication_audit',con,index=False,chunksize=1000); con.execute('CREATE UNIQUE INDEX ux_paper_id ON paper_master(paper_id)'); con.execute('CREATE INDEX ix_decision ON screening_decisions(decision)')
 summary={'source_records':len(rows),'deduplicated_candidates':len(master),'duplicate_groups':len(duplicates),'duplicate_records_collapsed':len(rows)-len(master),'screening_status':{k:int(v) for k,v in screen.decision.value_counts().items()},'corpus_layers':{'A':int(la.sum()),'B':int(lb.sum()),'C':int(lc.sum()),'D':int(ld.sum())},'unprocessed_candidates':0,'screening_method':'deterministic_high_recall_v1','second_review_status':'pending'}; (out/'normalization_screening_summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
if __name__=='__main__': main()
