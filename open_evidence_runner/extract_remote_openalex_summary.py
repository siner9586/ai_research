from __future__ import annotations
import argparse, binascii, json, os, re, struct, zipfile, zlib
from pathlib import Path
import requests
EOCD=b'PK\x05\x06'; ZIP64_LOCATOR=b'PK\x06\x07'; ZIP64_EOCD=b'PK\x06\x06'; CENTRAL=b'PK\x01\x02'; LOCAL=b'PK\x03\x04'
def signed(repo,aid,tok):
 r=requests.get(f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}/zip',headers={'Authorization':f'Bearer {tok}','Accept':'application/vnd.github+json'},allow_redirects=False,timeout=60); r.raise_for_status(); return r.headers['Location']
def rr(url,a,b):
 r=requests.get(url,headers={'Range':f'bytes={a}-{b}','Accept-Encoding':'identity'},timeout=(30,180));
 if r.status_code!=206: raise RuntimeError(f'range_http_{r.status_code}')
 d=r.content
 if len(d)!=b-a+1: raise RuntimeError('short_range')
 return d
def size(url):
 r=requests.get(url,headers={'Range':'bytes=0-0','Accept-Encoding':'identity'},timeout=(30,120));
 if r.status_code!=206: raise RuntimeError(f'no_range_{r.status_code}')
 m=re.search(r'/(\d+)$',r.headers.get('Content-Range','')); return int(m.group(1)) if m else (_ for _ in ()).throw(RuntimeError('no_size'))
def zip64(extra,u,c,o):
 p=0
 while p+4<=len(extra):
  hid,n=struct.unpack_from('<HH',extra,p); p+=4; x=extra[p:p+n]; p+=n
  if hid!=1: continue
  q=0
  if u==0xffffffff: u=struct.unpack_from('<Q',x,q)[0]; q+=8
  if c==0xffffffff: c=struct.unpack_from('<Q',x,q)[0]; q+=8
  if o==0xffffffff: o=struct.unpack_from('<Q',x,q)[0]
  break
 return u,c,o
def central(url,total):
 n=min(total,1048576); start=total-n; tail=rr(url,start,total-1); i=tail.rfind(EOCD)
 if i<0: raise RuntimeError('no_eocd')
 absolute=start+i; vals=struct.unpack_from('<4s4H2LH',tail,i); entries,cs,co=vals[4],vals[5],vals[6]
 if entries!=0xffff and cs!=0xffffffff and co!=0xffffffff: return co,cs,entries
 loc=rr(url,absolute-20,absolute-1); sig,_,zoff,_=struct.unpack('<4sLQL',loc)
 if sig!=ZIP64_LOCATOR: raise RuntimeError('no_zip64_locator')
 h=rr(url,zoff,zoff+55); v=struct.unpack_from('<4sQ2H2L4Q',h,0)
 if v[0]!=ZIP64_EOCD: raise RuntimeError('bad_zip64')
 return int(v[-1]),int(v[-2]),int(v[-3])
def members(url,off,n):
 d=rr(url,off,off+n-1); out=[]; p=0
 while p+46<=len(d):
  if d[p:p+4]!=CENTRAL: raise RuntimeError('bad_central')
  flags=struct.unpack_from('<H',d,p+8)[0]; method=struct.unpack_from('<H',d,p+10)[0]; crc=struct.unpack_from('<L',d,p+16)[0]; c=struct.unpack_from('<L',d,p+20)[0]; u=struct.unpack_from('<L',d,p+24)[0]; nl=struct.unpack_from('<H',d,p+28)[0]; el=struct.unpack_from('<H',d,p+30)[0]; cl=struct.unpack_from('<H',d,p+32)[0]; lo=struct.unpack_from('<L',d,p+42)[0]; ns=p+46; name=d[ns:ns+nl].decode('utf-8' if flags&0x800 else 'cp437'); extra=d[ns+nl:ns+nl+el]; u,c,lo=zip64(extra,u,c,lo); out.append({'filename':name,'method':method,'crc':crc,'compress_size':int(c),'file_size':int(u),'local_offset':int(lo)}); p=ns+nl+el+cl
 return out
def read(url,m):
 o=m['local_offset']; h=rr(url,o,o+29)
 if h[:4]!=LOCAL: raise RuntimeError('bad_local')
 nl=struct.unpack_from('<H',h,26)[0]; el=struct.unpack_from('<H',h,28)[0]; s=o+30+nl+el; raw=rr(url,s,s+m['compress_size']-1); data=raw if m['method']==0 else zlib.decompress(raw,-15)
 if len(data)!=m['file_size'] or (binascii.crc32(data)&0xffffffff)!=m['crc']: raise RuntimeError('member_integrity')
 return data
def main():
 a=argparse.ArgumentParser(); a.add_argument('--repository',required=True); a.add_argument('--artifact-id',required=True); a.add_argument('--output',type=Path,required=True); x=a.parse_args(); x.output.mkdir(parents=True,exist_ok=True)
 url=signed(x.repository,x.artifact_id,os.environ['GITHUB_TOKEN']); total=size(url); off,n,e=central(url,total); ms=members(url,off,n)
 interesting=[m for m in ms if m['filename'].endswith(('openalex_all_summary.json','openalex_all_search_queries.csv'))]
 if len(interesting)!=2: raise RuntimeError(f'expected_two:{[m["filename"] for m in interesting]}')
 (x.output/'openalex_artifact_member_sizes.json').write_text(json.dumps(interesting,indent=2),encoding='utf-8')
 with zipfile.ZipFile(x.output/'openalex-summary-only.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for m in interesting:
   d=read(url,m); z.writestr(Path(m['filename']).name,d)
   if m['filename'].endswith('openalex_all_summary.json'):
    s=json.loads(d); (x.output/'openalex_all_summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps(s,ensure_ascii=False,indent=2))
 print(json.dumps({'artifact_size':total,'entries':len(ms),'expected_entries':e},indent=2))
if __name__=='__main__': main()
