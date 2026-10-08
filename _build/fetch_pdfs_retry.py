# -*- coding: utf-8 -*-
import os, re, json, zipfile, unicodedata, time
import urllib.request, urllib.error, urllib.parse
from collections import Counter

ROOT = r'D:\KU-Assignment\IVF'
PKG  = os.path.join(ROOT, 'review2', 'AIR_Review_Package')
GH   = os.path.join(PKG, 'github')
PDFR = os.path.join(GH, 'papers')
LOG  = os.path.join(GH, '_build', 'pdf_acquisition_log.json')

with open(os.path.join(PKG,'evidence_data','citation_metadata.json'),encoding='utf-8') as f:
    META = json.load(f)
meta = {m['paper_id']: m for m in META}

with zipfile.ZipFile(os.path.join(PKG,'AIR_Source_Draft.zip')) as z:
    tex = z.read('Main_Manuscript_AIR.tex').decode('utf-8')
heads = list(re.finditer(r'\\(section|subsection|subsubsection)\*?\{([^}]*)\}', tex))
tops  = [(i,h.group(2)) for i,h in enumerate(heads) if h.group(1)=='section']
def sec_folder_for_pos(pos):
    idx = max(i for i,(k,h) in enumerate(tops) if heads[k].start()<=pos)
    t = tops[idx][1]
    return "%02d_%s"%(idx+1, re.sub(r'[^a-z0-9]+','_', t.lower()).strip('_')), t
order={}
for m in re.finditer(r'\\cite[tp]?(?:\[[^\]]*\])*\{([^}]*)\}', tex):
    for k in m.group(1).split(','):
        k=k.strip()
        if k in meta and k not in order: order[k]=m.start()
primary={k:sec_folder_for_pos(p) for k,p in order.items()}

UA={'User-Agent':'AIR-evidence (mailto:review@example.org)'}
def uget(url,timeout=45):
    return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout)
def fetch_pdf(url,dest):
    try:
        with uget(url,60) as r: data=r.read()
        if len(data)>4000 and data[:5]==b'%PDF-':
            open(dest,'wb').write(data); return True,len(data)
        return False,'not_pdf'
    except urllib.error.HTTPError as e: return False,'http_%d'%e.code
    except Exception as e: return False,str(e)[:80]
def upw(doi):
    try:
        with uget('https://api.unpaywall.org/v2/'+doi+'?email=review@example.org',30) as r:
            w=json.loads(r.read().decode('utf-8'))
        loc=w.get('best_oa_location') or {}
        return loc.get('url_for_pdf') or loc.get('url'), (w.get('oa_status') or '')
    except Exception as e: return None,'upw_err'
def epmc_pdf(doi):
    try:
        q=urllib.parse.quote('DOI:"'+doi+'"')
        with uget('https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='+q+'&format=json&resultType=core',30) as r:
            w=json.loads(r.read().decode('utf-8'))
        res=(w.get('resultList') or {}).get('result') or []
        if not res: return None
        pmcid=res[0].get('pmcid')
        return ('https://www.ncbi.nlm.nih.gov/pmc/articles/'+pmcid+'/pdf/') if pmcid else None
    except Exception: return None

log=json.load(open(LOG,encoding='utf-8'))
todo=[pid for pid,r in log.items() if r['status']=='unavailable']
print('retry',len(todo))
for i,pid in enumerate(todo):
    rec=log[pid]; m=meta[pid]; doi=m.get('doi') or ''
    folder,_=primary.get(pid,('99_uncited','Uncited'))
    pdir=os.path.join(PDFR,folder,pid); os.makedirs(pdir,exist_ok=True)
    pdf_path=os.path.join(pdir,pid+'.pdf')
    if os.path.exists(pdf_path): rec['status']='exists'; log[pid]=rec; continue
    ok=False
    if doi:
        u,oa=upw(doi)
        if u:
            ok,msg=fetch_pdf(u,pdf_path); rec['pdf_url']=u
            if ok: rec['status']='downloaded_oa'; rec['detail']='unpaywall'; rec['oa_status']=oa
    if not ok and doi:
        u=epmc_pdf(doi)
        if u:
            ok,msg=fetch_pdf(u,pdf_path)
            if ok: rec['status']='downloaded_oa'; rec['detail']='europepmc'; rec['pdf_url']=u; rec['oa_status']='oa_epmc'
    if ok: rec['bytes']=os.path.getsize(pdf_path)
    log[pid]=rec
    if i%15==0: print(i,pid,rec['status'],flush=True)
    time.sleep(0.3)
json.dump(log,open(LOG,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('DONE',Counter(v['status'] for v in log.values()))
