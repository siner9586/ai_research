from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

import pandas as pd

PUBLIC_SALTS = {
    "exp2": "open-evidence|10.1038/s41598-021-87480-9|experiment-2|v1",
    "exp3": "open-evidence|10.1038/s41598-021-87480-9|experiment-3|v1",
}


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda:handle.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def participant_hash(value: object, salt: str) -> str:
    raw=f"{salt}|{value}".encode('utf-8')
    return hashlib.sha256(raw).hexdigest()


def find_csv(root: Path, expected: str) -> Path:
    matches=[p for p in root.rglob('*.csv') if p.name.lower()==expected.lower() or expected.lower() in p.name.lower()]
    if len(matches)!=1:
        raise RuntimeError(f'Expected one {expected}, found {len(matches)}: {matches}')
    return matches[0]


def harmonize_exp2(source: Path) -> tuple[pd.DataFrame,dict]:
    raw=pd.read_csv(source)
    required={'ResponseId','WOA','InitialConfidence','PostConfidence','InitialTime','PostTime','InitialAnswer','FinalAnswer','difficulty','CorrectAnswer','AlgoGroup','round'}
    missing=required-set(raw.columns)
    if missing: raise RuntimeError(f'exp2_missing_columns:{sorted(missing)}')
    raw=raw.reset_index(drop=True)
    out=pd.DataFrame({
        'study_id':'doi:10.1038/s41598-021-87480-9',
        'experiment_id':'s41598-021-87480-9-exp2',
        'participant_id':[participant_hash(v,PUBLIC_SALTS['exp2']) for v in raw['ResponseId']],
        'trial_id':raw.groupby('ResponseId',sort=False).cumcount()+1,
        'source_row_number':raw.index+2,
        'advice_source':raw['AlgoGroup'].map({1:'algorithm',0:'crowd'}),
        'initial_decision':raw['InitialAnswer'],
        'final_decision':raw['FinalAnswer'],
        'correct_answer':raw['CorrectAnswer'],
        'woa_raw':raw['WOA'],
        'initial_confidence':raw['InitialConfidence'],
        'final_confidence':raw['PostConfidence'],
        'initial_response_time':raw['InitialTime'],
        'final_response_time':raw['PostTime'],
        'task_difficulty':raw['difficulty'],
        'reported_round':raw['round'],
        'advice_value':pd.NA,
        'advice_correct':pd.NA,
        'advice_quality':pd.NA,
    })
    assert out['participant_id'].nunique()==raw['ResponseId'].nunique()
    assert out['woa_raw'].between(0,1,inclusive='both').all()
    metrics=(out.groupby(['advice_source','task_difficulty'],dropna=False)['woa_raw']
             .agg(['count','mean','std']).reset_index().to_dict(orient='records'))
    summary={
        'experiment_id':'s41598-021-87480-9-exp2',
        'source_sha256':sha256_file(source),
        'source_rows':len(raw),
        'participants':raw['ResponseId'].nunique(),
        'output_rows':len(out),
        'woa_min':float(out['woa_raw'].min()),
        'woa_max':float(out['woa_raw'].max()),
        'group_metrics':metrics,
        'participant_identifiers_exported':False,
        'participant_pseudonym_method':'SHA-256 with public project-specific salt; original ResponseId omitted',
        'advice_value_available':False,
        'ai_correctness_available':False,
    }
    return out,summary


def harmonize_exp3(source: Path) -> tuple[pd.DataFrame,dict]:
    raw=pd.read_csv(source)
    required={'ResponseId','WOA','InitialConf','PostConf','InitialTime','PostTime','InitialAnswer','FinalAnswer','difficulty','CorrectAnswer','AlgoGroup','Quality','Advice','round'}
    missing=required-set(raw.columns)
    if missing: raise RuntimeError(f'exp3_missing_columns:{sorted(missing)}')
    raw=raw.reset_index(drop=True)
    advice_correct=(raw['Advice']==raw['CorrectAnswer'])
    if not ((raw['Quality']==1)==advice_correct).all():
        raise RuntimeError('Quality does not exactly match advice correctness')
    out=pd.DataFrame({
        'study_id':'doi:10.1038/s41598-021-87480-9',
        'experiment_id':'s41598-021-87480-9-exp3',
        'participant_id':[participant_hash(v,PUBLIC_SALTS['exp3']) for v in raw['ResponseId']],
        'trial_id':raw.groupby('ResponseId',sort=False).cumcount()+1,
        'source_row_number':raw.index+2,
        'advice_source':raw['AlgoGroup'].map({1:'algorithm',0:'crowd'}),
        'initial_decision':raw['InitialAnswer'],
        'final_decision':raw['FinalAnswer'],
        'correct_answer':raw['CorrectAnswer'],
        'woa_raw':raw['WOA'],
        'initial_confidence':raw['InitialConf'],
        'final_confidence':raw['PostConf'],
        'initial_response_time':raw['InitialTime'],
        'final_response_time':raw['PostTime'],
        'task_difficulty':raw['difficulty'],
        'reported_round':raw['round'],
        'advice_value':raw['Advice'],
        'advice_correct':advice_correct.astype(int),
        'advice_quality':raw['Quality'],
    })
    assert out['participant_id'].nunique()==raw['ResponseId'].nunique()
    assert out['woa_raw'].between(0,1,inclusive='both').all()
    correct=out.loc[out['advice_correct']==1,'woa_raw']
    wrong=out.loc[out['advice_correct']==0,'woa_raw']
    summary={
        'experiment_id':'s41598-021-87480-9-exp3',
        'source_sha256':sha256_file(source),
        'source_rows':len(raw),
        'participants':raw['ResponseId'].nunique(),
        'output_rows':len(out),
        'woa_min':float(out['woa_raw'].min()),
        'woa_max':float(out['woa_raw'].max()),
        'correct_advice_trials':int(len(correct)),
        'wrong_advice_trials':int(len(wrong)),
        'mean_woa_correct_advice':float(correct.mean()),
        'mean_woa_wrong_advice':float(wrong.mean()),
        'continuous_underreliance':float(1-correct.mean()),
        'continuous_overreliance':float(wrong.mean()),
        'participant_identifiers_exported':False,
        'participant_pseudonym_method':'SHA-256 with public project-specific salt; original ResponseId omitted',
        'advice_value_available':True,
        'ai_correctness_available':True,
        'quality_correctness_equivalence_verified':True,
    }
    return out,summary


def write_gzip_csv(frame: pd.DataFrame,path: Path) -> str:
    path.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(path,'wt',encoding='utf-8',newline='') as handle:
        frame.to_csv(handle,index=False)
    return sha256_file(path)


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--exp2-root',type=Path,required=True)
    parser.add_argument('--exp3-root',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    exp2_source=find_csv(args.exp2_root,'Experiment2.csv')
    exp3_source=find_csv(args.exp3_root,'Experiment3.csv')
    exp2,summary2=harmonize_exp2(exp2_source)
    exp3,summary3=harmonize_exp3(exp3_source)
    out2=args.output/'s41598-021-87480-9_exp2_trial_ipd.csv.gz'
    out3=args.output/'s41598-021-87480-9_exp3_trial_ipd.csv.gz'
    summary2['output_sha256']=write_gzip_csv(exp2,out2)
    summary3['output_sha256']=write_gzip_csv(exp3,out3)
    combined=pd.concat([exp2,exp3],ignore_index=True)
    combined_path=args.output/'s41598-021-87480-9_exp2_exp3_trial_ipd.csv.gz'
    combined_sha=write_gzip_csv(combined,combined_path)
    report={
        'completed':True,
        'license_status':'source files publicly downloadable on OSF; explicit data license not confirmed',
        'ipd_use_status':'archived_and_structurally_verified; analytic use requires license determination',
        'experiments':[summary2,summary3],
        'combined_rows':len(combined),
        'combined_participants_within_experiment':summary2['participants']+summary3['participants'],
        'combined_sha256':combined_sha,
        'columns':list(combined.columns),
    }
    (args.output/'harmonization_summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'completed':True,'exp2_rows':len(exp2),'exp3_rows':len(exp3),'combined_rows':len(combined),'combined_sha256':combined_sha},indent=2))


if __name__=='__main__':
    main()
