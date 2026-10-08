# -*- coding: utf-8 -*-
import os, re, json, zipfile, time
import urllib.request, urllib.error, urllib.parse
from collections import Counter
ROOT=r'D:\KU-Assignment\IVF'; PKG=os.path.join(ROOT,'review2','AIR_Review_Package')
GH=os.path.join(PKG,'github'); PDFR=os.path.join(GH,'papers')
LOG=os.path.join(GH,'_build','pdf_acquisition_log.json')
meta={m['paper_id']:m for m in json.load(open(PKG+'\\evidence_data\\citation_metadata.json',encoding='utf-8'))}
with zipfile.ZipFile(PKG+'\\AIR_Source_Draft.zip') as z: tex=z.read('Main_Manuscript_AIR.tex').decode('utf-8')
heads=list(re.finditer(r'\\(section|subsection|subsubsection)\*?\{([^}]*)\}',tex))
tops=[(i,h.group(2)) for i,h in enumerate(heads) if h.group(1)=='section']
def fold(pos):
    idx=max(i for i,(k,h) in enumerate(tops) if heads[k].start()<=pos)
    return "%02d_%s"%(idx+1,re.sub(r'[^a-z0-9]+','_',tops[idx][1].lower()).strip('_')),tops[idx][1]
order={}
for m in re.finditer(r'\\cite[tp]?(?:\[[^\]]*\])*\{([^}]*)\}',tex):
    for k in m.group(1).split(','):
        k=k.strip()
        if k in meta and k not in order: order[k]=m.start()
primary={k:fold(p) for k,p in order.items()}
UA={'User-Agent':'AIR-evidence'}
def uget(u,t=40): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t)
def fpdf(u,d):
    try:
        with uget(u,60) as r: data=r.read()
        if len(data)>4000 and data[:5]==b'%PDF-': open(d,'wb').write(data); return True
    except Exception: return False
    return False
log=json.load(open(LOG,encoding='utf-8'))
todo=[p for p,r in log.items() if r['status']=='unavailable']
print('s2 retry',len(todo))
done=0
for pid in todo:
    rec=log[pid]; doi=(meta[pid].get('doi') or '')
    if not doi: continue
    f,_=primary.get(pid,('99_uncited','Uncited'))
    pd=os.path.join(PDFR,f,pid); os.makedirs(pd,exist_ok=True)
    dest=os.path.join(pd,pid+'.pdf')
    if os.path.exists(dest): rec['status']='exists'; log[pid]=rec; continue
    try:
        with uget('https://api.semanticscholar.org/graph/v1/paper/DOI:'+urllib.parse.quote(doi)+'?fields=openAccessPdf',30) as r:
            w=json.loads(r.read().decode('utf-8'))
        u=(w.get('openAccessPdf') or {}).get('url')
    except Exception: u=None
    if u and fpdf(u,dest):
        rec['status']='downloaded_oa'; rec['detail']='semanticscholar'; rec['pdf_url']=u
        rec['bytes']=os.path.getsize(dest); done+=1
    log[pid]=rec
    time.sleep(1.1)
json.dump(log,open(LOG,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('extra downloaded:',done)
print('DONE',Counter(v['status'] for v in log.values()))
