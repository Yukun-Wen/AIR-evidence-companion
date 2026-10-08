import os, re, json, sys, time, unicodedata, zipfile
import urllib.request, urllib.error
try:
    import urllib3; HAS_URLLIB3=True
except Exception: HAS_URLLIB3=False

ROOT = r'D:\KU-Assignment\IVF'
PKG  = os.path.join(ROOT, 'review2', 'AIR_Review_Package')
GH   = os.path.join(PKG, 'github')
PDFR = os.path.join(GH, 'papers')
TMPM = os.path.join(ROOT, 'tmp', 'pdf_match.json')
LOG  = os.path.join(GH, '_build', 'pdf_acquisition_log.json')
os.makedirs(os.path.join(GH,'_build'), exist_ok=True)
os.makedirs(PDFR, exist_ok=True)

def norm(s):
    s = unicodedata.normalize('NFKD', (s or '').lower())
    s = re.sub(r'[^a-z0-9 ]',' ', s)
    return re.sub(r'\s+',' ', s).strip()

# --- load metadata ---
with open(os.path.join(PKG,'evidence_data','citation_metadata.json'),encoding='utf-8') as f:
    META = json.load(f)
meta = {m['paper_id']: m for m in META}

# --- section map (primary = first citing top-level section) ---
with zipfile.ZipFile(os.path.join(PKG,'AIR_Source_Draft.zip')) as z:
    tex = z.read('Main_Manuscript_AIR.tex').decode('utf-8')
heads = list(re.finditer(r'\\(section|subsection|subsubsection)\*?\{([^}]*)\}', tex))
top_secs = [(i, h.group(2)) for i,h in enumerate(heads) if h.group(1)=='section']
def sec_folder_for_pos(pos):
    idx = max(i for i,(k,h) in enumerate(top_secs) if heads[k].start()<=pos)
    title = top_secs[idx][1]
    slug = re.sub(r'[^a-z0-9]+','_', title.lower()).strip('_')
    return f"{idx+1:02d}_{slug}", top_secs[idx][1]
sec_map = {}
order = {}
cite_re = re.compile(r'\\cite[tp]?(?:\[[^\]]*\])*\{([^}]*)\}')
for m in cite_re.finditer(tex):
    for k in m.group(1).split(','):
        k=k.strip()
        if k in meta:
            folder,title = sec_folder_for_pos(m.start())
            sec_map.setdefault(k, set()).add(folder+'|'+title)
            order.setdefault(k, m.start())
primary = {}
for k, ss in sec_map.items():
    # primary = the section containing the FIRST citation
    first_pos = order[k]
    folder,title = sec_folder_for_pos(first_pos)
    primary[k] = (folder,title)

# --- local pdf match (from earlier fuzzy pass) ---
with open(TMPM,encoding='utf-8') as f:
    PM = json.load(f)
matched = PM['matched']

UA = {'User-Agent':'AIR-review-evidence-site (mailto:review@example.org)'}
def http_get(url, timeout=45):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout)

def openalex_pdf(doi):
    """Return (pdf_url, oa_status, host) via OpenAlex."""
    try:
        with http_get('https://api.openalex.org/works/https://doi.org/'+doi, 30) as r:
            w = json.loads(r.read().decode('utf-8'))
        oa = (w.get('open_access') or {}).get('oa_status','closed')
        loc = w.get('best_oa_location') or {}
        pdf = loc.get('pdf_url') or loc.get('landing_page_url')
        if not pdf and w.get('primary_location'):
            pdf = w['primary_location'].get('pdf_url')
        return pdf, oa
    except Exception as e:
        return None, f'openalex_err:{e}'

def fetch_pdf(url, dest):
    try:
        with http_get(url, 60) as r:
            data = r.read()
        if len(data) > 4000 and data[:5] == b'%PDF-':
            with open(dest,'wb') as f: f.write(data)
            return True, len(data)
        return False, 'not_pdf_or_too_small:%d' % len(data)
    except urllib.error.HTTPError as e:
        return False, f'http_{e.code}'
    except Exception as e:
        return False, f'err:{e}'

log = {}
pids = sorted(meta.keys())
for i,pid in enumerate(pids):
    m = meta[pid]
    folder,_ = primary.get(pid, ('99_uncited','Uncited'))
    pdir = os.path.join(PDFR, folder, pid)
    os.makedirs(pdir, exist_ok=True)
    pdf_path = os.path.join(pdir, f'{pid}.pdf')
    rec = {'paper_id': pid, 'doi': m.get('doi'), 'title': m.get('title')}
    if os.path.exists(pdf_path):
        rec['status']='exists'; log[pid]=rec; continue
    # 1) local copy
    src = matched.get(pid)
    if src and os.path.exists(src):
        import shutil; shutil.copyfile(src, pdf_path)
        rec['status']='local_copy'; rec['source']=src; rec['bytes']=os.path.getsize(pdf_path)
        log[pid]=rec; continue
    # 2) openalex download
    doi = m.get('doi') or ''
    pdf_url, oa = (None,'no_doi')
    if doi:
        pdf_url, oa = openalex_pdf(doi)
    rec['oa_status']=oa; rec['pdf_url']=pdf_url
    ok,msg = (False,'no_pdf_url')
    if pdf_url:
        ok,msg = fetch_pdf(pdf_url, pdf_path)
    rec['status'] = 'downloaded_oa' if ok else 'unavailable'
    rec['detail'] = msg
    if ok: rec['bytes']=os.path.getsize(pdf_path)
    log[pid]=rec
    if i % 20 == 0:
        print(f"[{i+1}/{len(pids)}] {pid}: {rec['status']}", flush=True)
        with open(LOG,'w',encoding='utf-8') as f: json.dump(log,f,ensure_ascii=False,indent=1)
    time.sleep(0.4)

with open(LOG,'w',encoding='utf-8') as f: json.dump(log,f,ensure_ascii=False,indent=1)
from collections import Counter
print('DONE', Counter(v['status'] for v in log.values()))
