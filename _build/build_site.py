# -*- coding: utf-8 -*-
"""
build_site.py — generate the reviewer-facing GitHub evidence site for the
AIR manuscript review package. Reads evidence_data/* (in package), the
manuscript .tex from AIR_Source_Draft.zip, and figures from AIR_Figure_Artwork.zip.
Emits a static HTML/JS site under github/. No network access.
"""
import os, re, json, csv, html, zipfile, unicodedata, datetime, collections

ROOT = r'D:\KU-Assignment\IVF'
PKG  = os.path.join(ROOT, 'review2', 'AIR_Review_Package')
GH   = os.path.join(PKG, 'github')
ED   = os.path.join(PKG, 'evidence_data')
BUILD= os.path.join(GH, '_build')
os.makedirs(BUILD, exist_ok=True)

def J(p):
    with open(p, encoding='utf-8') as f: return json.load(f)
def esc(s): return html.escape(str(s) if s is not None else '')

# ---------------- load evidence ----------------
META   = {m['paper_id']: m for m in J(os.path.join(ED,'citation_metadata.json'))}
MATRIX = {r['paper_id']: r for r in J(os.path.join(ED,'report_evidence_matrix.json'))}
KU     = {r['paper_id']: r for r in J(os.path.join(ED,'ku_uniform_extraction_07.json'))['records']}
CONTRA = J(os.path.join(ED,'conditional_contrasts.json'))  # list of 20
WF     = J(os.path.join(ED,'workflow_counts.json'))
REPS   = J(os.path.join(ED,'four_dataset_models','representatives.json'))
REPS   = REPS if isinstance(REPS, list) else REPS.get('rows', [])
CENSUS = list(csv.DictReader(open(os.path.join(ED,'eight_questions','resource_census.csv'),encoding='utf-8-sig')))
DUSES  = list(csv.DictReader(open(os.path.join(ED,'eight_questions','dataset_uses.csv'),encoding='utf-8-sig')))
APPR   = {r['paper_id']: r for r in J(os.path.join(PKG,'Human_Review_Package','evidence','appraisal_evidence_prefills.json'))['rows']}
FIELDNAMES = ['task','inputs','prediction_time','unit','method','supervision','outcome','sample_sizes','split','validation']
FLABEL = {'task':'Task','inputs':'Inputs','prediction_time':'Prediction time','unit':'Analysis unit',
          'method':'Method','supervision':'Supervision / labels','outcome':'Outcome',
          'sample_sizes':'Sample sizes','split':'Splitting','validation':'Validation'}
PIDRE = re.compile(r'^[A-Z]{1,8}\d{2,4}$')

# ---------------- tex: sections + claims ----------------
with zipfile.ZipFile(os.path.join(PKG,'AIR_Source_Draft.zip')) as z:
    TEX = z.read('Main_Manuscript_AIR.tex').decode('utf-8')

HEADS = list(re.finditer(r'\\(section|subsection|subsubsection)\*?\{([^}]*)\}', TEX))
TOPS  = [h for h in HEADS if h.group(1)=='section']

def slugify(s): return re.sub(r'[^a-z0-9]+','_', s.lower()).strip('_')

SEC_INFO = []
for i,h in enumerate(TOPS):
    SEC_INFO.append({'idx':i,'title':h.group(2),
                     'folder': f"{i+1:02d}_{slugify(h.group(2))}"})

def sec_of(pos):
    cur = SEC_INFO[0]
    for s in SEC_INFO:
        if TOPS[s['idx']].start() <= pos: cur = s
        else: break
    return cur

def sub_of(pos):
    """nearest heading (any level) at-or-before pos -> (title, level)"""
    best = None
    for h in HEADS:
        if h.start() <= pos: best = h
        else: break
    return (best.group(2), best.group(1)) if best else ('','section')

def clean_tex(t):
    t = re.sub(r'(?<!\\)%.*', '', t)
    for _ in range(8):
        depth=0; cut=-1
        for m in re.finditer(r'\\(begin\{|end\{[^}]*\}|begingroup|endgroup)', t):
            tok=m.group(1)
            if tok.startswith('begin'): depth+=1
            else:
                depth-=1
                if depth<0: cut=m.end(); break
        if cut<0: break
        t=t[cut:]
    ENV = '(?:longtable|sidewaystable|tabularx|tabular|figure|minipage|table|equation|align|sidewaysfigure)'
    t = re.sub(r'\\begin\{'+ENV+r'\*?\}[\s\S]*?\\end\{'+ENV+r'\*?\}', ' ', t)
    t = re.sub(r'\\begin\{'+ENV+r'[^}]*\}', ' ', t)
    t = re.sub(r'\\end\{'+ENV+r'[^}]*\}', ' ', t)
    t = re.sub(r'\\begingroup[\s\S]*?\\endgroup', ' ', t)
    t = re.sub(r'\\bgroup[\s\S]*?\\egroup', ' ', t)
    t = re.sub(r'\\(?:setlength|renewcommand|setcounter|addtocounter|newcommand|providecommand|def|let)\{[^}]*\}\{[^}]*\}', ' ', t)
    t = re.sub(r'\\(?:setlength|renewcommand|setcounter)\{[^}]*\}', ' ', t)
    t = re.sub(r'\\cite[tp]?(?:\[[^\]]*\])*\{([^}]*)\}', r'[@\1]', t)
    t = re.sub(r'\\(?:label|ref|eqref|autoref|pageref)\{[^}]*\}', '', t)
    t = re.sub(r'\\(?:textbf|textit|emph|texttt|textsc|underline)\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\(sub)*section\*?\{[^}]*\}', '', t)
    t = re.sub(r'\\(?:begin|end)\{[^}]*\}', ' ', t)
    t = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?', ' ', t)
    t = t.replace('~',' ').replace('\\%','%').replace('\\&','&').replace('\\_','_').replace('\\$','$')
    t = re.sub(r'[{}]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

CITE_RE = re.compile(r'\\cite[tp]?(?:\[[^\]]*\])*\{([^}]*)\}')
CLAIMS = collections.defaultdict(list)   # key -> [{sec, sub, text}]
first_pos = {}
par_bounds = [(m.start(), m.end()) for m in re.finditer(r'\n\s*\n', TEX)]
def context_for(pos):
    s = max((b[1] for b in par_bounds if b[1] <= pos), default=0)
    e = min((b[0] for b in par_bounds if b[0] > pos), default=len(TEX))
    return s, e

ENV_SPAN_RE = re.compile(r'\\begin\{(longtable|sidewaystable|tabularx|tabular|figure\*|figure|minipage|table)\*?\}[\s\S]*?\\end\{(?:longtable|sidewaystable|tabularx|tabular|figure\*|figure|minipage|table)\*?\}')
ENV_BLOCKS = [(m.start(), m.end()) for m in ENV_SPAN_RE.finditer(TEX)]
def in_block(pos):
    for a,b in ENV_BLOCKS:
        if a < pos < b: return a,b
    return None

ROW_SPLIT = re.compile(r'\\\\')
for m in CITE_RE.finditer(TEX):
    keys = [k.strip() for k in m.group(1).split(',') if k.strip() in META]
    if not keys: continue
    blk = in_block(m.start())
    if blk:
        a,b = blk
        env_txt = TEX[a:b]
        capm = re.search(r'\\caption\{([^}]*)\}', env_txt)
        try: env_name = re.search(r'\\begin\{([^}]*)\}', env_txt).group(1)
        except Exception: print('DBG:', repr(env_txt[:100]), 'pos', m.start()); env_name='?'
        if 'figure' in env_name or 'minipage' in env_name:
            cap = capm.group(1) if capm else ''
            # sentence in caption containing the cite
            sent=''
            for s_ in re.split(r'(?<=[.!?])\s+', cap):
                if m.group(0) in s_ or any(k in s_ for k in keys): sent=s_.strip(); break
            chunk = ('In the figure caption' + (': ' + cap if not sent else '') + ' — ' + (sent or cap)) if cap else env_txt[:600]
        else:
            capp = ('; table caption: ' + capm.group(1)) if capm else ''
            rel = m.start()-a
            rows = ROW_SPLIT.split(env_txt)
            row = ''; acc = 0
            for r_ in rows:
                acc += len(r_)+2
                if acc >= rel: row = r_; break
            cells = re.split(r'&', row)
            cite_cell = row.strip()
            for c_ in cells:
                if m.group(0) in c_: cite_cell = c_.strip(); break
            chunk = 'Table entry' + capp + ' — ' + cite_cell
    else:
        s,e = context_for(m.start())
        chunk = TEX[s:e]
    if (not blk) and len(chunk) < 350:
        s2 = max((b[1] for b in par_bounds if b[1] <= s-1), default=0)
        chunk = TEX[s2:e]
    txt = clean_tex(chunk)
    if len(txt) > 1600: txt = txt[:1600].rsplit(' ',1)[0] + ' …'
    if len(txt) < 30: continue
    sub, lvl = sub_of(m.start())
    sec = sec_of(m.start())
    for k in keys:
        first_pos.setdefault(k, m.start())
        CLAIMS[k].append({'section': sec['title'], 'sfolder': sec['folder'],
                          'subsection': sub if lvl!='section' else '',
                          'text': txt, 'keys': keys})
# dedupe claims per key
for k,v in CLAIMS.items():
    seen=set(); out=[]
    for c in v:
        sig=c['text'][:90]
        if sig in seen: continue
        seen.add(sig); out.append(c)
    CLAIMS[k]=out[:6]

def primary_section(pid):
    pos = first_pos.get(pid)
    if pos is None: return {'folder':'99_uncited','title':'Uncited'}
    return sec_of(pos)

def all_sections(pid):
    secs=[]; seen=set()
    for c in CLAIMS.get(pid,[]):
        k=(c['sfolder'],c['section'])
        if k not in seen: seen.add(k); secs.append({'folder':c['sfolder'],'title':c['section']})
    return secs or [primary_section(pid)]


def unlatex(s):
    if not s: return ''
    s = re.sub(r"\\['\"`^~=.uvcdbrtHk]{?([A-Za-z])\}?", r'\1', s)
    repl = {'\\ss':'ss','\\ae':'ae','\\AE':'AE','\\oe':'oe','\\OE':'OE','\\aa':'aa','\\o':'o','\\i':'i','\\j':'j','\\l':'l'}
    for k,v in repl.items(): s=s.replace(k,v)
    for ch in ['_','&','%','$','#','{','}']: s=s.replace(chr(92)+ch, ch)
    s = s.replace('---','\u2014').replace('--','\u2013').replace('~',' ')
    return re.sub(r'[{}]','',str(s)).strip()

# pdf availability (written by fetch_pdfs.py; may still be running)
ACQ = {}
acqp = os.path.join(BUILD,'pdf_acquisition_log.json')
if os.path.exists(acqp): ACQ = J(acqp)
HL = J(os.path.join(BUILD,'pdf_highlight_log.json')) if os.path.exists(os.path.join(BUILD,'pdf_highlight_log.json')) else {}

def pdf_status(pid):
    rec = ACQ.get(pid,{})
    st = rec.get('status','pending')
    return {'status': st, 'oa': rec.get('oa_status',''),
            'url': rec.get('pdf_url') or '', 'detail': rec.get('detail','')}

# ---------------- papers.json ----------------
papers=[]
for pid,m in META.items():
    mat = MATRIX.get(pid); ku = KU.get(pid)
    core = bool(m.get('core_empirical_report'))
    fields={}; flocs={}
    if mat:
        for f in FIELDNAMES:
            v = mat.get(f)
            if v not in (None,'',[],{}): fields[f]=v
        fe = mat.get('field_evidence') or {}
        flocs = {k:(v.get('locators') if isinstance(v,dict) else []) for k,v in fe.items()}
    elif ku:
        for f in FIELDNAMES:
            v = ku.get(f)
            if v not in (None,'',[],{}): fields[f]=v
        fe = ku.get('field_evidence') or {}
        flocs = {k:(v.get('locators') if isinstance(v,dict) else []) for k,v in fe.items()}
    ex = (mat or {}).get('source_linked_evidence') or []
    locs = (mat or {}).get('source_locators') or []
    sha  = (mat or ku or {}).get('reader_sha256') or (mat or {}).get('source_sha256','')
    wf   = (mat or {}).get('primary_workflow_group','')
    cids = m.get('contrast_ids') or []
    if isinstance(cids,str):
        try: cids=json.loads(cids)
        except Exception: cids=[]
    appr = APPR.get(pid)
    auth = m.get('authors_bibtex','')
    auth = unlatex(auth)
    auths=[a.strip() for a in re.split(r'\s+and\s+', auth) if a.strip()]
    a_short = ', '.join(a.split(',')[0] for a in auths[:3]) + (' et al.' if len(auths)>3 else '')
    papers.append({
        'id':pid,'title':unlatex(m.get('title','')),'authors_short':a_short,'authors_n':len(auths),
        'year':m.get('year'),'venue':unlatex(m.get('venue_bibtex','')),'etype':m.get('entry_type',''),
        'doi':m.get('doi',''),'doi_url':m.get('doi_url',''),
        'role':'core' if core else 'contextual',
        'contrast_ids':cids,'workflow':wf,
        'primary':primary_section(pid),'sections':all_sections(pid),
        'claims':CLAIMS.get(pid,[]),'fields':fields,'field_locs':flocs,
        'excerpts':ex,'locators':locs,'sha256':sha,
        'scope':(mat or {}).get('adjudicated_scope',''),
        'method_summary':(mat or {}).get('source_linked_method_summary',''),
        'appraisal_tool':((appr or {}).get('ai_evidence_prefill') or {}).get('suggested_tool',''),
        'human_verification':m.get('human_verification','pending'),
        'pdf':pdf_status(pid),
    })
papers.sort(key=lambda p:(p['primary']['folder'], p['id']))

os.makedirs(os.path.join(GH,'data'), exist_ok=True)
data_js = 'window.PAPERS = ' + json.dumps(papers, ensure_ascii=False) + ';'
with open(os.path.join(GH,'data','papers.js'),'w',encoding='utf-8') as f: f.write(data_js)
with open(os.path.join(GH,'data','papers.json'),'w',encoding='utf-8') as f: json.dump(papers,f,ensure_ascii=False,indent=1)
print('papers:', len(papers))
print('claims total:', sum(len(p['claims']) for p in papers))
print('papers w/o claims:', [p['id'] for p in papers if not p['claims']][:20])
print('sections:', sorted({p['primary']['folder'] for p in papers}))

# ================= HTML GENERATION =================
ASSETS = os.path.join(GH,'assets'); FIGS = os.path.join(ASSETS,'figures')
os.makedirs(FIGS, exist_ok=True); os.makedirs(os.path.join(ASSETS,'js'), exist_ok=True)

CSS = """
:root{--ink:#2e3735;--muted:#75808a;--blue:#5b7d95;--accent:#c08a5f;--bg:#f6f4f1;--panel:#efece8;--border:#ddd6cd;--hl:#f5e9bf;--hl2:#f3dcc9;--teal:#7fa8a0}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14.5px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
a{color:var(--blue);text-decoration:none;border-bottom:1px solid transparent}
a:hover{border-bottom-color:var(--blue)}
header.site{background:#fff;color:var(--ink);padding:20px 5% 14px;border-bottom:3px solid var(--blue)}
header.site h1{margin:0 0 4px;font-size:22px;font-weight:700;letter-spacing:-0.01em}
header.site p{margin:3px 0;max-width:1180px;font-size:13px;color:var(--muted)}
nav.crumbs{background:var(--panel);padding:7px 5%;font-size:12.5px;border-bottom:1px solid var(--border)}
nav.crumbs a{color:var(--blue);margin-right:5px;border:0}
main{max-width:1200px;margin:auto;padding:18px 4%}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0}
.stat{background:var(--panel);border:1px solid var(--border);border-left:3px solid var(--blue);border-radius:4px;padding:9px 15px;min-width:120px}
.stat b{display:block;font-size:23px;color:var(--blue);font-weight:700}
.stat span{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.03em}
.card{background:#fff;border:1px solid var(--border);border-radius:5px;padding:16px 20px;margin:14px 0;box-shadow:0 1px 2px rgba(16,42,67,.04)}
.card h3{margin-top:0;font-size:15.5px;color:var(--blue);border-bottom:1px solid var(--border);padding-bottom:6px}
.badge{display:inline-block;padding:1px 8px;border-radius:3px;font-size:11.5px;font-weight:600;margin:2px 3px 2px 0;border:1px solid var(--border);background:var(--panel);color:#3b5568}
.badge.core{background:#e8ecdf;border-color:#a9b894;color:#5d6b4a}
.badge.ctx{background:#eae7f0;border-color:#b8afc9;color:#6a5f8c}
.badge.contrast{background:#f4e4d6;border-color:#d9ac80;color:#8f5f33}
.badge.pending{background:#f4e3df;border-color:#d4a294;color:#8c4f42}
.badge.loc{font-family:ui-monospace,"Cascadia Code",Consolas,monospace;background:#e3e9eb;color:var(--blue)}
mark{background:var(--hl);padding:0 2px;border-radius:2px}
mark.field{background:var(--hl2)}
blockquote.ex{border-left:3px solid var(--teal);background:#eef2f0;margin:10px 0;padding:9px 14px;border-radius:0 4px 4px 0;font-size:13.5px}
blockquote.claim{border-left:3px solid var(--accent);background:#f6eee6;margin:10px 0;padding:9px 14px;border-radius:0 4px 4px 0;font-size:13.5px}
table.data{border-collapse:collapse;width:100%;font-size:13px}
table.data th,table.data td{border:1px solid var(--border);padding:6px 9px;text-align:left;vertical-align:top}
table.data th{background:var(--panel);position:sticky;top:0;font-weight:650}
table.data tr:nth-child(even){background:#f8f6f3}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;padding:11px;background:var(--panel);border:1px solid var(--border);border-radius:5px;position:sticky;top:0;z-index:5}
.filters input,.filters select{padding:6px 9px;border:1px solid #b7c8d2;border-radius:4px;font-size:13px}
.filters input[type=search]{flex:1;min-width:220px}
.fieldgrid{display:grid;grid-template-columns:175px 1fr;gap:0;border:1px solid var(--border);border-radius:5px;overflow:hidden;margin:10px 0}
.fieldgrid>div{padding:7px 12px;border-bottom:1px solid var(--border)}
.fieldgrid .fl{background:var(--panel);font-weight:600;font-size:12.5px}
.fieldgrid .fv{font-size:13px}
details{border:1px solid var(--border);border-radius:5px;background:#fff;margin:8px 0;padding:9px 14px}
summary{cursor:pointer;font-weight:600;color:var(--blue);font-size:13.5px}
.warn{border-left:3px solid var(--accent);background:#f6eee4;padding:11px 16px;border-radius:0 4px 4px 0;margin:14px 0;font-size:13px}
.note{border-left:3px solid var(--blue);background:var(--panel);padding:11px 16px;border-radius:0 4px 4px 0;margin:14px 0;font-size:13px}
img.fig{max-width:100%;border:1px solid var(--border);border-radius:4px;background:#fff;margin:6px 0}
.figcap{font-size:12px;color:var(--muted);margin:4px 0 16px;font-style:italic}
.small{font-size:12.5px;color:var(--muted)}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:11.5px;word-break:break-all}
footer{border-top:1px solid var(--border);margin-top:36px;padding:14px 5%;font-size:12px;color:var(--muted);background:var(--panel)}
h2.sec{border-bottom:2px solid var(--blue);padding-bottom:4px;margin-top:26px;font-size:18px;color:var(--blue)}
.pill{font-size:10.5px;padding:1px 7px;border-radius:9px;background:var(--panel);color:var(--blue);margin-left:6px;border:1px solid var(--border)}
a.pdfbtn{display:inline-block;background:var(--blue);color:#fff !important;padding:3px 11px;border-radius:4px;font-size:12px;margin-top:6px;border:0}
a.pdfbtn.none{background:#8fa6b3}
    .navrow{display:flex;justify-content:space-between;align-items:center;margin:8px 0 10px;font-size:12.5px}
    .navrow a{color:var(--blue);text-decoration:none;padding:3px 10px;border:1px solid var(--border);border-radius:4px;background:var(--panel)}
    .navrow a.idx{background:var(--blue);color:#fff}
    .navrow a:hover{filter:brightness(.95)}
    a.pdfbtn.hl{background:#b07c52}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:800px){.grid2{grid-template-columns:1fr}.fieldgrid{grid-template-columns:1fr}}
"""
with open(os.path.join(ASSETS,'style.css'),'w',encoding='utf-8') as f: f.write(CSS)

JS = """
function esc(s){return String(s==null?'':s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function badgeHtml(p){
  var b=[];
  b.push('<span class="badge '+(p.role=='core'?'core':'ctx')+'">'+(p.role=='core'?'Core report':'Contextual')+'</span>');
  (p.contrast_ids||[]).forEach(function(c){b.push('<span class="badge contrast">'+c+'</span>')});
  var st=p.pdf?p.pdf.status:'';
  if(st=='local_copy'||st=='downloaded_oa'||st=='exists') b.push('<span class="badge">PDF</span>'); else b.push('<span class="badge pending">no PDF</span>');
  return b.join(' ');
}
function paperLink(p){var r=(document.body.dataset.root||'');return r+'papers/'+p.primary.folder+'/'+p.id+'/card.html'}
function rowHtml(p){
  return '<tr><td><a href="'+paperLink(p)+'"><b>'+esc(p.id)+'</b></a></td>'+
  '<td>'+esc(p.title)+'</td><td>'+esc(p.authors_short)+'</td><td>'+esc(p.year||'')+'</td>'+
  '<td>'+esc(p.venue)+'</td><td>'+esc((p.sections||[]).map(function(s){return s.title}).join('; '))+'</td>'+
  '<td>'+esc(p.workflow||'')+'</td><td>'+badgeHtml(p)+'</td></tr>';
}
"""
with open(os.path.join(ASSETS,'js','app.js'),'w',encoding='utf-8') as f: f.write(JS)

FIGCAP = {}
for m in re.finditer(r'Fig(\d+)\.pdf\}.*?\\caption\{([^}]*)\}', TEX, re.S):
    FIGCAP[int(m.group(1))] = clean_tex(m.group(2))

def convert_figures():
    try:
        import fitz
    except Exception as e:
        print('figure conversion skipped:', e); return []
    out=[]
    zpath=os.path.join(PKG,'AIR_Figure_Artwork.zip')
    if not os.path.exists(zpath): return out
    with zipfile.ZipFile(zpath) as z:
        names=[n for n in z.namelist() if re.match(r'.*?/?Fig\d+\.pdf$', n)]
        for n in sorted(names, key=lambda x:int(re.search(r'\d+',os.path.basename(x)).group())):
            num=int(re.search(r'Fig(\d+)',os.path.basename(n)).group(1))
            try:
                doc=fitz.open(stream=z.read(n), filetype='pdf')
                pix=doc[0].get_pixmap(matrix=fitz.Matrix(2.4,2.4))
                pix.save(os.path.join(FIGS,'Fig%d.png'%num))
                out.append({'num':num,'file':'assets/figures/Fig%d.png'%num,'caption':FIGCAP.get(num,'')})
            except Exception as e:
                print('fig conv fail', n, e)
    return out
FIGS_OUT = convert_figures()
print('figs converted:', [f['num'] for f in FIGS_OUT])

def page(title, crumbs, body, root=''):
    cr=''.join('<a href="'+root+h+'">'+esc(t)+'</a> &rsaquo; ' for t,h in crumbs[:-1]) + (esc(crumbs[-1][0]) if crumbs else '')
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(title)+'</title>'
      '<link rel="stylesheet" href="'+root+'assets/style.css">'
      '<script src="'+root+'data/papers.js"></script><script src="'+root+'assets/js/app.js"></script></head><body data-root="'+root+'">'
      '<header class="site"><h1>AI for IVF &middot; Evidence Companion</h1>'
      '<p>Interactive evidence library for the manuscript <i>Artificial intelligence for in vitro fertilization</i> '
      '(Artificial Intelligence Review submission). Every cited work is mapped to the manuscript sections it supports, '
      'with highlighted manuscript claims, extracted fields, and source locators.</p></header>'
      '<nav class="crumbs"><a href="'+root+'index.html">Home</a> &rsaquo; '+cr+'</nav>'
      '<main>'+body+'</main>'
      '<footer>Generated '+datetime.date.today().isoformat()+' &middot; Evidence compiled by automated extraction; human verification pending '
      '&middot; PDFs mirrored only where locally held or openly licensed; otherwise DOI links.</footer>'
      '</body></html>')

count_pages=0
for _i,_p in enumerate(papers):
    if _i>0: _p['_prev']=papers[_i-1]
    if _i<len(papers)-1: _p['_next']=papers[_i+1]
for p in papers:
    pf = p['primary']['folder']
    pdir = os.path.join(GH,'papers',pf,p['id'])
    os.makedirs(pdir, exist_ok=True)
    pdf = p['pdf']; has_pdf = pdf['status'] in ('local_copy','downloaded_oa','exists')
    pdf_link = ('<a class="pdfbtn" href="'+p['id']+'.pdf">Open PDF</a>' if has_pdf else
                ('<a class="pdfbtn none" href="'+esc(p['doi_url'])+'">PDF not mirrored &mdash; DOI link</a>' if p['doi_url'] else ''))
    hl = HL.get(p['id'],{})
    if has_pdf and hl.get('annots',0)>0:
        pdf_link += ' <a class="pdfbtn hl" href="'+p['id']+'_highlighted.pdf">Highlighted-evidence PDF ('+str(hl['annots'])+' marks)</a>'
    badges=['<span class="badge '+('core' if p['role']=='core' else 'ctx')+'">'+('Core empirical report' if p['role']=='core' else 'Contextual source')+'</span>']
    for c in p['contrast_ids']: badges.append('<span class="badge contrast">contrast '+esc(c)+'</span>')
    if p['appraisal_tool']: badges.append('<span class="badge">'+esc(p['appraisal_tool'])+' prefill</span>')
    badges.append('<span class="badge pending">human verification: '+esc(p['human_verification'])+'</span>')
    secs_html=' '.join('<span class="badge">'+esc(s['title'])+'</span>' for s in p['sections'])

    claims_html=''
    for c in p['claims']:
        claims_html+=('<blockquote class="claim"><div class="small">&sect; '+esc(c['section'])+((' &mdash; '+esc(c['subsection'])) if c['subsection'] else '')+
                      '</div><mark>'+esc(c['text'])+'</mark></blockquote>')
    fld=''
    if p['fields']:
        fld='<h3>Extracted evidence fields</h3><div class="fieldgrid">'
        for fn in FIELDNAMES:
            if fn in p['fields']:
                val=p['fields'][fn]
                val=p['fields'][fn]
                if isinstance(val,dict): val=' | '.join(str(k)+': '+str(v) for k,v in val.items())
                elif isinstance(val,(list,tuple)): val='; '.join(( (str(x.get('value'))+' '+str(x.get('unit',''))+(' ['+str(x.get('locator',''))+']' if x.get('locator') else '')) if isinstance(x,dict) else str(x) ) for x in val)
                else: val=str(val)
                locs=' '.join('<span class="badge loc">'+esc(l)+'</span>' for l in (p['field_locs'].get(fn) or []))
                fld+=('<div class="fl">'+FLABEL[fn]+'<br>'+locs+'</div><div class="fv"><mark class="field">'+esc(val)+'</mark></div>')
        fld+='</div>'
    ex_html=''
    if p['excerpts']:
        ex_html='<h3>Source-linked evidence excerpts</h3>'
        for ex in p['excerpts']:
            ex_html+=('<blockquote class="ex"><span class="badge loc">'+esc(ex.get('locator',''))+'</span> <mark>'+esc(ex.get('paraphrase',''))+'</mark></blockquote>')
    locs_html=' '.join('<span class="badge loc">'+esc(l)+'</span>' for l in p['locators'])
    contr = [c for c in CONTRA if c['paper_id']==p['id']]
    ct_html=''
    if contr:
        ct_html='<h3>Conditional comparisons in this paper</h3><table class="data"><tr><th>ID</th><th>Config A</th><th>Config B</th><th>&Delta; (B&minus;A)</th><th>Metric</th><th>Population</th><th>Status</th></tr>'
        for c in contr:
            ct_html+=('<tr><td><b>'+c['contrast_id']+'</b></td><td>'+esc(c['configuration_A'])+' ('+str(c['value_A'])+')</td><td>'+esc(c['configuration_B'])+' ('+str(c['value_B'])+')</td><td>'+str(c['delta_B_minus_A'])+'</td><td>'+esc(c['metric'])+'</td><td>'+esc(c['evaluation_population'])+'</td><td>'+esc(c['comparison_status'])+'</td></tr>')
        ct_html+='</table><p class="small">Full detail on <a href=\"__ROOT__contrasts.html\">contrasts page</a>.</p>'
    _pv=p.get('_prev'); _nx=p.get('_next')
    nav_html='<div class="navrow">'+('<a href="../../'+_pv['primary']['folder']+'/'+_pv['id']+'/card.html">&larr; '+_pv['id']+'</a>' if _pv else '<span></span>')+'<a class="idx" href="../../../az.html">Index</a>'+('<a href="../../'+_nx['primary']['folder']+'/'+_nx['id']+'/card.html">'+_nx['id']+' &rarr;</a>' if _nx else '<span></span>')+'</div>'
    body=('<div class="card"><span class="mono">'+p['id']+'</span> '+(' '.join(badges))+
      '<h2 style="margin:8px 0">'+esc(p['title'])+'</h2>'
      '<p class="small">'+esc(p['authors_short'])+' ('+str(p['year'])+'). <i>'+esc(p['venue'])+'</i>.<br>'
      'DOI: <a href="'+esc(p['doi_url'])+'">'+esc(p['doi'])+'</a> &middot; '+pdf_link+'</p>'
      '<p class="small">Cited in: '+secs_html+'</p></div>'+
      nav_html+
      '<div class="warn"><b>Verification status.</b> Evidence below is machine-extracted and AI-adjudicated; <b>author/human verification is pending</b>. Locators (e.g. '+p['id']+'-B0014) are block anchors into the archived full-text reader'+
      ((', sha256 <span class="mono">'+p['sha256'][:16]+'&hellip;</span>') if p['sha256'] else '')+'.</div>'
      +('<h3>Manuscript passages citing this work <span class="pill">highlighted = supported claim</span></h3>'+claims_html if claims_html else '<p class="small">No extractable in-text passage.</p>')
      +(('<blockquote class="ex"><b>Adjudicated scope:</b> <mark>'+esc(p['scope'])+'</mark></blockquote>') if p['scope'] else '')
      +(('<blockquote class="ex"><b>Method summary:</b> '+esc(p['method_summary'])+'</blockquote>') if p['method_summary'] else '')
      +fld+ex_html+ct_html
      +(('<h3>All archived block locators</h3><p>'+locs_html+'</p>') if p['locators'] else ''))
    body = body.replace('__ROOT__','../../../')
    with open(os.path.join(pdir,'card.html'),'w',encoding='utf-8') as f:
        f.write(page(p['id']+' — '+p['title'][:60],
                     [('Sections','sections.html'),(p['primary']['title'],'sections.html#'+pf),(p['id'],'')],
                     body, root='../../../'))
    md=['# '+p['id']+' — '+p['title'],'',
        '**'+p['authors_short']+' ('+str(p['year'])+').** *'+p['venue']+'*. DOI: ['+p['doi']+']('+p['doi_url']+')','',
        '**Role:** '+p['role']+((' · contrasts '+', '.join(p['contrast_ids'])) if p['contrast_ids'] else '')+' · workflow: '+(p['workflow'] or 'n/a'),'',
        '**Cited in:** '+', '.join(s['title'] for s in p['sections']),'',
        '**PDF:** '+('see '+p['id']+'.pdf in this folder' if has_pdf else 'not mirrored - see DOI')+' | **Interactive card:** [card.html](card.html)','',
        '## Manuscript passages citing this work']
    for c in p['claims']:
        md.append('> **§ '+c['section']+'**'+((' : '+c['subsection']) if c['subsection'] else ''))
        md.append('> =='+c['text']+'==')
        md.append('')
    if p['fields']:
        md.append('## Extracted evidence fields'); md.append('| Field | Value | Locators |'); md.append('|---|---|---|')
        for fn in FIELDNAMES:
            if fn in p['fields']:
                v=p['fields'][fn]
                if isinstance(v,(dict,list)): v=json.dumps(v,ensure_ascii=False)
                v=str(v).replace('|', chr(92)+'|')
                md.append('| **'+FLABEL[fn]+'** | '+v+' | '+' '.join(p['field_locs'].get(fn) or [])+' |')
        md.append('')
    if p['excerpts']:
        md.append('## Source-linked excerpts')
        for ex in p['excerpts']: md.append('- ['+ex.get('locator','')+'] =='+ex.get('paraphrase','')+'==')
        md.append('')
    md.append('---'); md.append('*Machine-extracted; human verification pending. == ... == marks supporting content.*')
    with open(os.path.join(pdir,'README.md'),'w',encoding='utf-8') as f: f.write('\n'.join(md))
    count_pages+=1
print('card pages:', count_pages)

for s in SEC_INFO:
    sd=os.path.join(GH,'papers',s['folder']); os.makedirs(sd,exist_ok=True)
    plist=[p for p in papers if p['primary']['folder']==s['folder']]
    md=['# Section '+str(s['idx']+1)+'. '+s['title'],'',str(len(plist))+' cited work(s) primarily filed under this section.','',
        '| ID | Title | Year | Role | PDF |','|---|---|---|---|---|']
    for p in plist:
        has_pdf = p['pdf']['status'] in ('local_copy','downloaded_oa','exists')
        md.append('| ['+p['id']+']('+p['id']+'/README.md) | '+p['title'][:90].replace('|',' ')+' | '+str(p['year'])+' | '+p['role']+' | '+('yes' if has_pdf else 'DOI only')+' |')
    with open(os.path.join(sd,'README.md'),'w',encoding='utf-8') as f: f.write('\n'.join(md))


# ================= CHARTS =================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':9.5,'axes.edgecolor':'#c9c2b8','axes.labelcolor':'#3a4340','axes.linewidth':0.8,'axes.grid':False,
                     'xtick.color':'#75808a','ytick.color':'#75808a','figure.dpi':110,'axes.titlesize':10.5,'axes.titlecolor':'#4a5a55'})
BLUE='#5b7d95'; ACC='#c08a5f'; GREEN='#7a8b6f'; PURP='#8b7fa3'; RED='#a8604e'; GREY='#aeb9b3'; TEAL='#7fa8a0'; INK='#2e3735'
def tidy(ax):
    for s in ['top','right','left']:
        ax.spines[s].set_visible(False)
def savefig(fig,name):
    fig.tight_layout(); fig.savefig(os.path.join(FIGS,name),bbox_inches='tight',transparent=True)
    plt.close(fig)

# 1 corpus donut
core_n=sum(1 for p in papers if p['role']=='core'); ctx_n=len(papers)-core_n
contrast_n=len({c['paper_id'] for c in CONTRA})
fig,ax=plt.subplots(figsize=(4.6,3.4))
ax.pie([core_n-contrast_n,contrast_n,ctx_n],labels=['Core reports','Core w/ contrasts','Contextual'],
       colors=[BLUE,ACC,PURP],autopct=lambda v:str(round(v/247*100))+'%',startangle=90,
       wedgeprops=dict(width=.42,edgecolor='w'),textprops={'fontsize':9})
ax.text(0,0,'247\nworks',ha='center',va='center',fontsize=13,fontweight='bold',color=INK)
savefig(fig,'corpus_composition.svg')

# 2 workflow groups
fig,ax=plt.subplots(figsize=(6.4,3.4))
names=[w['workflow_group'] for w in WF][::-1]; vals=[w['reports'] for w in WF][::-1]
ax.barh(names,vals,color=BLUE,height=.62)
for i,v in enumerate(vals): ax.text(v+.5,i,str(v),va='center',fontsize=9,color=BLUE)
ax.set_xlabel('Core empirical reports'); ax.set_xlim(0,max(vals)*1.15); tidy(ax)
savefig(fig,'workflow_groups.svg')

# 3 year histogram
years=[p['year'] for p in papers if isinstance(p['year'],int)]
bins=range(min(years),max(years)+2)
fig,ax=plt.subplots(figsize=(6.6,3.0))
core_y=[p['year'] for p in papers if p['role']=='core' and isinstance(p['year'],int)]
ctx_y=[p['year'] for p in papers if p['role']!='core' and isinstance(p['year'],int)]
ax.hist([ctx_y,core_y],bins=bins,stacked=True,color=[PURP,BLUE],label=['Contextual','Core'],edgecolor='w')
ax.set_xlabel('Publication year'); ax.set_ylabel('Cited works'); ax.legend(frameon=False); ax.grid(axis='y',alpha=.2,color='#c9c2b8'); tidy(ax)
savefig(fig,'citations_by_year.svg')

# 4 citation density per top section (primary filing counts)
sec_counts=collections.Counter(p['primary']['folder'] for p in papers)
labels=[s['folder'].split('_',1)[0]+' '+s['title'][:34] for s in SEC_INFO]
vals=[sec_counts.get(s['folder'],0) for s in SEC_INFO]
fig,ax=plt.subplots(figsize=(6.8,3.6))
ax.bar(range(len(vals)),vals,color=[BLUE if i<8 else GREY for i in range(len(vals))])
ax.set_xticks(range(len(vals))); ax.set_xticklabels([s['folder'].split('_')[0] for s in SEC_INFO])
ax.set_ylabel('Works filed (primary)'); ax.set_xlabel('Manuscript section'); ax.grid(axis='y',alpha=.2,color='#c9c2b8'); tidy(ax)
savefig(fig,'section_filing.svg')

# 5 contrast deltas dumbbell
fig,ax=plt.subplots(figsize=(7.0,5.4))
cs=sorted(CONTRA,key=lambda c:c['contrast_id'])
for i,c in enumerate(cs):
    a,b=c['value_A'],c['value_B']
    col=GREEN if c['delta_B_minus_A']>0 else (RED if c['delta_B_minus_A']<0 else GREY)
    ax.plot([a,b],[i,i],'-',color='#c3d3da',lw=3,zorder=1)
    ax.scatter([a],[i],s=46,color=GREY,zorder=2)
    ax.scatter([b],[i],s=52,color=col,zorder=3)
    ax.text(max(a,b)+.004,i,f"Δ{c['delta_B_minus_A']:+.3f}",va='center',fontsize=8,color=col)
ax.set_yticks(range(len(cs)))
ax.set_yticklabels([c['contrast_id']+' '+c['metric']+' · '+c['paper_id'] for c in cs],fontsize=8)
ax.set_xlabel('Metric value (A grey → B colored)'); ax.grid(axis='x',alpha=.15,color='#c9c2b8'); tidy(ax)
savefig(fig,'contrast_deltas.svg')

# 6 dataset x family heatmap
fam=sorted({r['family_name'] for r in REPS})
ds=sorted({r['dataset_name'] for r in REPS})
M=[[0]*len(ds) for _ in fam]
met={}
for r in REPS:
    i=fam.index(r['family_name']); j=ds.index(r['dataset_name'])
    M[i][j]=1; met[(i,j)]=r
fig,ax=plt.subplots(figsize=(6.2,5.6))
ax.imshow(M,cmap=matplotlib.colors.ListedColormap(['#efece8',BLUE]),aspect='auto',vmin=0,vmax=1)
for (i,j),r in met.items():
    v=list(r['metrics'].values())[0] if r.get('metrics') else None
    ax.text(j,i,(r['paper_id']+'\n'+('%.3f'%v if isinstance(v,(int,float)) else '')),ha='center',va='center',fontsize=7,color='w')
ax.set_xticks(range(len(ds))); ax.set_xticklabels(ds,fontsize=9)
ax.set_yticks(range(len(fam))); ax.set_yticklabels(fam,fontsize=8)
ax.set_title('4 datasets × 15 model families — best representative per cell',fontsize=10)
savefig(fig,'dataset_family_heatmap.svg')

# 7 resource reuse
census=sorted(CENSUS,key=lambda r:int(r.get('n_total') or 0),reverse=True)[:12]
fig,ax=plt.subplots(figsize=(6.6,3.8))
ax.barh([c['display_name'] for c in census][::-1],[int(c['n_total']) for c in census][::-1],color=ACC,height=.62)
ax.set_xlabel('Report–resource uses (cited corpus)')
savefig(fig,'resource_reuse.svg')

OLD_CHARTS=[('corpus_composition.svg','Corpus composition'),('workflow_groups.svg','Core reports by IVF workflow group'),
        ('citations_by_year.svg','Cited works by publication year'),('section_filing.svg','Primary filing across manuscript sections'),
        ('contrast_deltas.svg','Conditional contrasts C01–C20 (within-report A→B)'),
        ('dataset_family_heatmap.svg','Four-dataset model-family matrix'),('resource_reuse.svg','Most-reused named resources')]
print('charts written')



# ---- additional indexing/comprehension charts ----
# A. field completeness across core reports
fig,ax=plt.subplots(figsize=(7.0,3.4))
coreps=[p for p in papers if p['role']=='core']
cov=[(fn, sum(1 for p in coreps if fn in (p['fields'] or {}))/max(1,len(coreps))*100) for fn in FIELDNAMES]
cov.sort(key=lambda x:x[1])
ax.barh([FLABEL[f] for f,_ in cov],[v for _,v in cov],color=BLUE,height=.66)
for i,(f,v) in enumerate(cov): ax.text(v+1.2,i,str(round(v))+'%',va='center',fontsize=8.5,color='#75808a')
ax.set_xlim(0,105); ax.set_xlabel('Core reports with an extracted value (%)'); ax.set_title('Evidence-field completeness across the 125 core reports'); ax.grid(axis='x',alpha=.2,color='#c9c2b8'); tidy(ax)
savefig(fig,'field_completeness.svg')

# B. papers per subsection (top 12)
fig,ax=plt.subplots(figsize=(7.2,4.2))
import collections as _c
subc=_c.Counter()
for p in papers:
    for cl in p['claims']:
        if cl.get('subsection'): subc[cl['subsection']]+=1; break
top=subc.most_common(12)[::-1]
ax.barh([t[0][:42] for t in top],[t[1] for t in top],color=ACC,height=.7)
for i,(t,v) in enumerate(top): ax.text(v+0.4,i,str(v),va='center',fontsize=8.5,color='#3a5563')
ax.set_xlabel('Works carrying a supporting claim'); ax.set_title('Density of supporting evidence by manuscript subsection'); ax.grid(axis='x',alpha=.2,color='#c9c2b8'); tidy(ax)
savefig(fig,'subsection_density.svg')


# ---- reviewer-comprehension charts ----
fig,ax=plt.subplots(figsize=(8.4,3.2))
stages=[('Title-abstract records screened',2905),('Registry full-text recommendations',389),
        ('Field-level verifications',1180),('Cited works',247),('Core empirical reports',125)]
cols=[BLUE,GREEN,ACC,TEAL,PURP]
for i,(lab,v) in enumerate(stages):
    y=len(stages)-i-0.5
    ax.barh(y,v,height=.66,color=cols[i])
    ax.text(v+18,y,f'{v:,}',va='center',fontsize=9,color=INK)
ax.set_yticks([len(stages)-i-0.5 for i in range(len(stages))])
ax.set_yticklabels([s[0] for s in stages],fontsize=9.5)
ax.set_xlim(0,3350); ax.set_ylim(0,len(stages)); ax.axis('off')
ax.set_title('From screening to cited corpus',fontsize=11,loc='left',color='#4a5a55',pad=6)
savefig(fig,'evidence_funnel.svg')

wfnames=[w['workflow_group'] for w in WF]
colnames=[w.split(' ')[0] for w in wfnames]+['Contextual']
import numpy as np
H=np.zeros((len(SEC_INFO),len(colnames)),dtype=int)
for p in papers:
    try: si=[s['folder'] for s in SEC_INFO].index(p['primary']['folder'])
    except ValueError: continue
    ci=wfnames.index(p['workflow']) if p['workflow'] in wfnames else len(wfnames)
    H[si][ci]+=1
fig,ax=plt.subplots(figsize=(8.2,4.2))
im=ax.imshow(H,cmap='cividis',aspect='auto')
mx=H.max() or 1
for i in range(H.shape[0]):
    for j in range(H.shape[1]):
        if H[i,j]>0: ax.text(j,i,str(H[i,j]),ha='center',va='center',fontsize=8,color='w' if H[i,j]>mx*0.55 else '#22404e')
ax.set_xticks(range(len(colnames))); ax.set_xticklabels(colnames,fontsize=8,rotation=28,ha='right')
ax.set_yticks(range(len(SEC_INFO))); ax.set_yticklabels([s['folder'].split('_')[0]+' '+s['title'][:26] for s in SEC_INFO],fontsize=8)
fig.colorbar(im,shrink=.7,label='papers (primary filing)')
ax.set_title('Evidence distribution: manuscript section x IVF workflow group',fontsize=11,color=BLUE)
savefig(fig,'section_workflow_heatmap.svg')

byds=collections.defaultdict(list)
for r in REPS:
    pm=r.get('primary_metric'); v=(r.get('metrics') or {}).get(pm)
    if isinstance(v,(int,float)): byds[r['dataset_name']].append((r['family_name'],v,pm,r['paper_id']))
order_ds=['HFEA','HuSHeM','SMIDS','CleavageEmbryo']
fig,axs=plt.subplots(2,2,figsize=(9.6,6.4))
for ax,d in zip(axs.flat,order_ds):
    rows=sorted(byds.get(d,[]),key=lambda x:x[1])
    for y,(fam,v,pm,pid) in enumerate(rows):
        ax.barh(y,v,height=.6,color=BLUE)
        ax.text(v,y,' %.3f - %s'%(v,pid),va='center',fontsize=7.5,color='#33505d')
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows],fontsize=8)
    ax.set_title('%s - %s'%(d, rows[0][2] if rows else ''),fontsize=9.5,color=BLUE)
    ax.set_xlim(0,max([r[1] for r in rows]+[1])*1.32); ax.grid(axis='x',alpha=.2)
fig.suptitle('Best independent-family representative per dataset (primary metric)',fontsize=11,y=1.0)
savefig(fig,'benchmark_panels.svg')

fig,ax=plt.subplots(figsize=(7.0,2.8))
prefill=118; ku_only=125-118
ax.barh(0,prefill,color=GREEN,label='PROBAST+AI evidence prefill')
ax.barh(0,ku_only,left=prefill,color=ACC,label='field extraction only (KU)')
ax.barh(1,122,color=GREY,label='metadata + citation only')
ax.text(prefill/2,0,'118 prefilled',ha='center',va='center',color='w',fontsize=8)
ax.text(prefill+ku_only/2,0,str(ku_only),ha='center',va='center',color='w',fontsize=8)
ax.text(61,1,'metadata only',ha='center',va='center',color='w',fontsize=8)
ax.set_yticks([0,1]); ax.set_yticklabels(['Core reports (n=125)','Contextual (n=122)'],fontsize=9)
ax.legend(frameon=False,fontsize=8,loc='lower right',bbox_to_anchor=(1,-0.6),ncol=3)
ax.set_title('Extraction / appraisal coverage - human verification pending on all',fontsize=10.5,color='#4a5a55')
ax.set_xlim(0,130)
savefig(fig,'verification_status.svg')

depth=[('claim passages',sum(1 for p in papers if p['claims'])),
       ('extracted fields',sum(1 for p in papers if p['fields'])),
       ('source excerpts',sum(1 for p in papers if p['excerpts'])),
       ('block locators',sum(1 for p in papers if p['locators'])),
       ('contrast roles',sum(1 for p in papers if p['contrast_ids']))]
fig,ax=plt.subplots(figsize=(6.8,2.8))
ax.barh([d[0] for d in depth][::-1],[d[1] for d in depth][::-1],color=BLUE,height=.6)
for i,(k,v) in enumerate(depth[::-1]): ax.text(v+2,i,'%d papers'%v,va='center',fontsize=8.5,color='#33505d')
ax.set_xlim(0,255); ax.set_title('How many papers carry each evidence layer',fontsize=10.5,color=BLUE)
savefig(fig,'evidence_depth.svg')

CHARTS = [('evidence_funnel.svg','Review funnel: screening to cited corpus'),
          ('section_workflow_heatmap.svg','Evidence distribution: section x workflow group'),
          ('benchmark_panels.svg','Four-dataset benchmark: best family representative'),
          ('contrast_deltas.svg','Conditional contrasts C01-C20'),
          ('corpus_composition.svg','Corpus composition'),('workflow_groups.svg','Core reports by workflow group'),
          ('citations_by_year.svg','Cited works by year'),('section_filing.svg','Primary filing across sections'),
          ('dataset_family_heatmap.svg','Dataset x model-family matrix'),('resource_reuse.svg','Most-reused resources'),
          ('verification_status.svg','Coverage vs pending verification'),
          ('field_completeness.svg','Evidence-field completeness'),('subsection_density.svg','Evidence density by subsection')]

# ================= TOP-LEVEL PAGES =================
def stats_block():
    have_pdf=sum(1 for p in papers if p['pdf']['status'] in ('local_copy','downloaded_oa','exists'))
    claims=sum(len(p['claims']) for p in papers)
    excerpts=sum(len(p['excerpts']) for p in papers)
    cards=[('247','cited works'),(str(core_n),'core reports'),(str(ctx_n),'contextual'),
           (str(len(SEC_INFO)),'manuscript sections'),(str(claims),'highlighted claim passages'),
           (str(excerpts),'source-linked excerpts'),(str(len(CONTRA)),'conditional contrasts'),
           (str(have_pdf),'PDFs mirrored')]
    return '<div class="stats">'+''.join('<div class="stat"><b>'+b+'</b><span>'+s+'</span></div>' for b,s in cards)+'</div>'

# ---- sections.html ----
sb=''
for s in SEC_INFO:
    plist=[p for p in papers if p['primary']['folder']==s['folder']]
    if not plist: continue
    sb+='<h2 class="sec" id="'+s['folder']+'">§'+str(s['idx']+1)+'. '+esc(s['title'])+' <span class="pill">'+str(len(plist))+'</span></h2>'
    n_core=sum(1 for p in plist if p['role']=='core')
    n_pdf=sum(1 for p in plist if p['pdf']['status'] in ('local_copy','downloaded_oa','exists'))
    n_ctr=len({c for p in plist for c in p['contrast_ids']})
    n_fld=sum(1 for p in plist if p['fields'])
    sb+=('<div class="stats" style="margin:8px 0">'
         '<div class="stat"><b>'+str(len(plist))+'</b><span>works</span></div>'
         '<div class="stat"><b>'+str(n_core)+'</b><span>core</span></div>'
         '<div class="stat"><b>'+str(len(plist)-n_core)+'</b><span>contextual</span></div>'
         '<div class="stat"><b>'+str(n_pdf)+'</b><span>PDF mirrored</span></div>'
         '<div class="stat"><b>'+str(n_fld)+'</b><span>field-extracted</span></div>'
         '<div class="stat"><b>'+str(n_ctr)+'</b><span>contrasts</span></div></div>')
    sb+='<table class="data"><tr><th>ID</th><th>Title</th><th>Year</th><th>Role</th><th>Badges</th></tr>'
    for p in plist:
        has_pdf = p['pdf']['status'] in ('local_copy','downloaded_oa','exists')
        sb+=('<tr><td><a href="papers/'+p['primary']['folder']+'/'+p['id']+'/card.html"><b>'+p['id']+'</b></a></td>'
             '<td>'+esc(p['title'])+'</td><td>'+str(p['year'])+'</td><td>'+p['role']+'</td>'
             '<td>'+('PDF' if has_pdf else 'DOI only')+(' · '+','.join(p['contrast_ids']) if p['contrast_ids'] else '')+'</td></tr>')
    sb+='</table>'
with open(os.path.join(GH,'sections.html'),'w',encoding='utf-8') as f:
    f.write(page('Papers by manuscript section',[('Papers by section','')],'<h2>Cited works by manuscript section</h2><p class="small">Each paper is filed under the section where it is first cited; a paper may also support other sections (shown on its card).</p>'+sb))

# ---- catalog.html ----
cat='''<h2>Evidence catalog — 247 cited works</h2>
<div class="filters">
<input type="search" id="q" placeholder="Search title, author, ID, venue, DOI…" oninput="render()">
<select id="fRole" onchange="render()"><option value="">Core + Contextual</option><option value="core">Core only</option><option value="contextual">Contextual only</option></select>
<select id="fSec" onchange="render()"><option value="">All sections</option></select>
<select id="fWf" onchange="render()"><option value="">All workflow groups</option></select>
<select id="fPdf" onchange="render()"><option value="">PDF: any</option><option value="1">mirrored</option><option value="0">DOI only</option></select>
<select id="fCtr" onchange="render()"><option value="">Any</option><option value="1">contrast papers</option></select>
</div>
<p class="small" id="cnt"></p>
<table class="data" id="tbl"><thead><tr><th>ID</th><th>Title</th><th>Authors</th><th>Year</th><th>Venue</th><th>Cited in</th><th>Workflow</th><th>Tags</th></tr></thead><tbody></tbody></table>
<script>
var P=window.PAPERS||[];
(function(){
 var sec=document.getElementById('fSec'); var secs={};
 P.forEach(function(p){(p.sections||[]).forEach(function(s){secs[s.title]=1})});
 Object.keys(secs).forEach(function(t){var o=document.createElement('option');o.value=t;o.textContent=t;sec.appendChild(o)});
 var wf=document.getElementById('fWf'); var w={};
 P.forEach(function(p){if(p.workflow)w[p.workflow]=1});
 Object.keys(w).forEach(function(t){var o=document.createElement('option');o.value=t;o.textContent=t;wf.appendChild(o)});
})();
function render(){
 var q=document.getElementById('q').value.toLowerCase();
 var fr=document.getElementById('fRole').value, fs=document.getElementById('fSec').value,
     fw=document.getElementById('fWf').value, fp=document.getElementById('fPdf').value,
     fc=document.getElementById('fCtr').value;
 var rows=P.filter(function(p){
   if(fr && p.role!=fr) return false;
   if(fs && !(p.sections||[]).some(function(s){return s.title==fs})) return false;
   if(fw && p.workflow!=fw) return false;
   var has=p.pdf&&(p.pdf.status=='local_copy'||p.pdf.status=='downloaded_oa'||p.pdf.status=='exists');
   if(fp==='1'&&!has) return false; if(fp==='0'&&has) return false;
   if(fc==='1'&&!(p.contrast_ids||[]).length) return false;
   if(q){var hay=(p.id+' '+p.title+' '+p.authors_short+' '+p.venue+' '+p.doi).toLowerCase(); if(hay.indexOf(q)<0) return false;}
   return true;
 });
 document.getElementById('cnt').textContent=rows.length+' / '+P.length+' shown';
 document.querySelector('#tbl tbody').innerHTML=rows.map(rowHtml).join('');
}
render();
</script>'''
with open(os.path.join(GH,'catalog.html'),'w',encoding='utf-8') as f:
    f.write(page('Evidence catalog',[('Catalog','')],cat))

# ---- claims.html ----
clm='<h2>Manuscript claims → supporting papers</h2><p class="small">Each highlighted block is a verbatim manuscript passage; beneath it are the works it cites. Click an ID for that paper&rsquo;s evidence card.</p>'
claim_items=[]
for p in papers:
    for c in p['claims']: claim_items.append({'p':p,'c':c})
# group by text to avoid duplicates
seen={}
for it in claim_items:
    t=it['c']['text']
    seen.setdefault(t,{'c':it['c'],'papers':[]})['papers'].append(it['p'])
ordered=sorted(seen.values(), key=lambda x:(x['c']['section']))
for grp in ordered:
    c=grp['c']
    clm+='<details><summary>'+esc(c['text'][:150])+('…' if len(c['text'])>150 else '')+'</summary>'
    clm+='<blockquote class="claim"><div class="small">§ '+esc(c['section'])+((' — '+esc(c['subsection'])) if c['subsection'] else '')+'</div><mark>'+esc(c['text'])+'</mark></blockquote>'
    clm+='<p>Cited by: '+' '.join('<a href="papers/'+p['primary']['folder']+'/'+p['id']+'/card.html"><span class="badge">'+p['id']+'</span></a>' for p in grp['papers'])+'</p></details>'
with open(os.path.join(GH,'claims.html'),'w',encoding='utf-8') as f:
    f.write(page('Claims to papers',[('Claims','')],clm))

# ---- contrasts.html ----
ct='<h2>Conditional comparisons (C01–C20)</h2><p class="small">Within-report contrasts between model configurations. Values are as extracted; statuses describe admissible interpretation.</p><img class="fig" src="assets/figures/contrast_deltas.svg"><table class="data"><tr><th>ID</th><th>Paper</th><th>Endpoint</th><th>A</th><th>B</th><th>Δ</th><th>Metric</th><th>Axis</th><th>Status</th><th>Interpretation</th></tr>'
for c in CONTRA:
    pnext=[p for p in papers if p['id']==c['paper_id']]
    link=('papers/'+pnext[0]['primary']['folder']+'/'+c['paper_id']+'/card.html') if pnext else '#'
    ct+=('<tr><td><b>'+c['contrast_id']+'</b></td><td><a href="'+link+'">'+c['paper_id']+'</a></td><td>'+esc(c['endpoint'])+'</td>'
         '<td>'+esc(c['configuration_A'])+' <b>'+str(c['value_A'])+'</b></td><td>'+esc(c['configuration_B'])+' <b>'+str(c['value_B'])+'</b></td>'
         '<td><b>'+('%+.3f'%c['delta_B_minus_A'])+'</b></td><td>'+esc(c['metric'])+'</td><td>'+esc(c['comparison_axis'])+'</td>'
         '<td>'+esc(c['comparison_status'])+'</td><td class="small">'+esc(c['interpretation'])+'</td></tr>')
ct+='</table>'
with open(os.path.join(GH,'contrasts.html'),'w',encoding='utf-8') as f:
    f.write(page('Conditional contrasts',[('Contrasts','')],ct))

# ---- atlas.html ----
at='<h2>Visualization atlas</h2>'
for fn,cap in CHARTS:
    at+='<div class="card"><img class="fig" src="assets/figures/'+fn+'"><div class="figcap">'+esc(cap)+'</div></div>'
if FIGS_OUT:
    at+='<h2 class="sec">Manuscript figures</h2>'
    for fg in FIGS_OUT:
        at+='<div class="card"><img class="fig" src="'+fg['file']+'"><div class="figcap"><b>Figure '+str(fg['num'])+'.</b> '+esc(fg['caption'][:300])+'</div></div>'
with open(os.path.join(GH,'atlas.html'),'w',encoding='utf-8') as f:
    f.write(page('Visualization atlas',[('Atlas','')],at))

# ---- index.html ----
sec_links=''.join('<li><a href="sections.html#'+s['folder']+'">§'+str(s['idx']+1)+' '+esc(s['title'])+'</a> <span class="pill">'+str(sec_counts.get(s['folder'],0))+'</span></li>' for s in SEC_INFO if sec_counts.get(s['folder'],0))
idx_body='''
<div class="note"><b>For reviewers.</b> This site organizes the <b>247 works cited</b> in the AIR manuscript by the section they support. Each paper has an evidence card showing (a) the manuscript passages it supports — highlighted; (b) extracted evidence fields; (c) source-linked excerpts with archived block locators; (d) where mirrored, a local PDF. Use <a href="catalog.html">Catalog</a> to filter; <a href="claims.html">Claims</a> to read forward from a manuscript sentence; <a href="contrasts.html">Contrasts</a> for the 20 conditional comparisons; <a href="atlas.html">Atlas</a> for figures.</div>
'''+stats_block()+'''
<div class="grid2">
<div class="card"><h3 style="margin-top:0">Corpus at a glance</h3><img class="fig" src="assets/figures/corpus_composition.svg"><img class="fig" src="assets/figures/workflow_groups.svg"></div>
<div class="card"><h3 style="margin-top:0">Papers by manuscript section</h3><ul class="toc">'''+sec_links+'''</ul>
<p><a class="pdfbtn" href="sections.html">Open chapter index</a> <a class="pdfbtn" href="catalog.html">Open catalog</a></p></div>
</div>
<div class="card"><h3 style="margin-top:0">How to read this site</h3>
<table class="data"><tr><th style="width:170px">Visual cue</th><th>Meaning</th></tr>
<tr><td><mark>yellow highlight</mark></td><td>Verbatim manuscript passage citing the work — the claim it supports</td></tr>
<tr><td><mark class="field">orange highlight</mark></td><td>Machine-extracted evidence field (task, inputs, method, split, validation…)</td></tr>
<tr><td><span class="badge loc">EMBRYO01-B0034</span></td><td>Block locator into the archived full-text reader (sha256-pinned)</td></tr>
<tr><td><span class="badge core">core</span> / <span class="badge ctx">contextual</span></td><td>Evidence layer of the cited work</td></tr>
<tr><td><span class="badge contrast">C-id</span></td><td>Paper contributes a conditional comparison (Contrasts page)</td></tr>
<tr><td><span class="badge pending">pending</span></td><td>Machine-derived; human verification pending</td></tr></table>
<p class="small"><b>Reading path:</b> 1. <a href="catalog.html">Catalog</a> filter &rarr; 2. paper card &rarr; 3. <a href="claims.html">Claims</a> &rarr; 4. <a href="contrasts.html">Contrasts</a>/<a href="atlas.html">Atlas</a>.</p></div>
<div class="card"><h3 style="margin-top:0">Evidence highlights</h3>
<img class="fig" src="assets/figures/evidence_funnel.svg">
<img class="fig" src="assets/figures/section_workflow_heatmap.svg">
<img class="fig" src="assets/figures/benchmark_panels.svg"><div class="figcap">Four-dataset benchmark: best independent-family representative per dataset.</div>
<img class="fig" src="assets/figures/contrast_deltas.svg"><div class="figcap">Conditional contrasts: within-report A&rarr;B configuration deltas.</div></div>
<div class="warn"><b>Honesty note.</b> All extracted content is machine-derived and <b>author verification is pending</b>. Highlighted passages are manuscript text citing each work; source excerpts are paraphrases keyed to archived block locators (sha256-pinned). PDFs are mirrored only where locally held or openly licensed; otherwise the DOI link is provided.</div>
'''
with open(os.path.join(GH,'index.html'),'w',encoding='utf-8') as f:
    f.write(page('Evidence companion — AI for IVF review',[],idx_body))

# ---- az.html master index ----
import collections as _col
by_sec = _col.defaultdict(list); by_wf = _col.defaultdict(list); by_etype = _col.defaultdict(list); by_auth = _col.defaultdict(list); by_year=_col.defaultdict(list)
for p in papers:
    by_sec[p['primary']['title']].append(p)
    if p.get('workflow'): by_wf[p['workflow']].append(p)
    if p.get('etype'): by_etype[p['etype']].append(p)
    a0=(p['authors_short'] or '').split(',')[0].strip()
    if a0: by_auth[a0[0].upper()].append(p)
    by_year[str(p['year'] or '?')].append(p)

def plist(rows):
    out=''
    for p in rows:
        out+=('<li><a href="papers/'+p['primary']['folder']+'/'+p['id']+'/card.html"><b>'+p['id']+'</b></a> '+esc(p['title'][:80])+' <span class="small">('+esc(str(p['year'])+' · '+p['venue'])+')</span></li>')
    return '<ul class="idxlist">'+out+'</ul>'

az='<h2>Master index</h2><p class="small">Find a cited work by manuscript section, workflow group, evidence type, first-author initial, or year. Click an ID to open its evidence card.</p>'
az+='<div class="navrow" style="justify-content:flex-start;gap:8px;flex-wrap:wrap"><a class="idx" href="catalog.html">Searchable table</a><a href="sections.html">By section</a><a href="claims.html">By claim</a><a href="contrasts.html">By contrast</a><a href="atlas.html">Charts &amp; figures</a></div>'
az+='<h3>By manuscript section</h3><div class="grid2">'
for s in SEC_INFO:
    rows=by_sec.get(s['title'],[])
    az+='<div><h4>§'+str(s['idx']+1)+' '+esc(s['title'])+' <span class="pill">'+str(len(rows))+'</span></h4>'+plist(rows)+'</div>'
az+='</div>'
az+='<h3>By workflow group</h3><div class="grid2">'
for wf,rows in sorted(by_wf.items()):
    az+='<div><h4>'+esc(wf)+' <span class="pill">'+str(len(rows))+'</span></h4>'+plist(rows)+'</div>'
az+='</div>'
az+='<h3>By first-author initial</h3>'
letters=''.join('<a href="#az'+c+'">'+c+'</a> ' for c in sorted(by_auth))
az+='<p class="small">'+letters+'</p><div class="grid2">'
for c in sorted(by_auth):
    az+='<div><h4 id="az'+c+'">'+c+' <span class="pill">'+str(len(by_auth[c]))+'</span></h4>'+plist(by_auth[c])+'</div>'
az+='</div>'
az+='<h3>By publication year</h3><div class="grid2">'
for yr,rows in sorted(by_year.items(), reverse=True):
    az+='<div><h4>'+yr+' <span class="pill">'+str(len(rows))+'</span></h4>'+plist(rows)+'</div>'
az+='</div>'
with open(os.path.join(GH,'az.html'),'w',encoding='utf-8') as f:
    f.write(page('Master index', [('Master index','')], az, root=''))

print('top pages written')


# ================= DOCS =================
readme = '''# AI for IVF — Evidence Companion (reviewer-facing)

Static evidence library for the AIR manuscript submission. Open **index.html** in any browser (works offline) or publish this folder as a GitHub Pages site.

## What is inside

| Path | Content |
|---|---|
| `index.html` | Landing page: corpus stats, section links, key figures |
| `catalog.html` | Searchable/filterable table of all 247 cited works |
| `claims.html` | Manuscript claim passages → citing papers (highlighted) |
| `contrasts.html` | 20 conditional within-report comparisons + delta chart |
| `sections.html` | Chapter index — papers filed by first-cited manuscript section |
| `az.html` | Master index — works by section, workflow group, author initial, year |
| `atlas.html` | Visualization atlas (generated charts + manuscript figures) |
| `papers/<section>/<ID>/` | Per-paper folder: `README.md` evidence card + `card.html` + `<ID>.pdf` when mirrored |
| `data/papers.js` / `.json` | Machine-readable record for every paper |
| `assets/` | CSS, JS, generated SVG charts, manuscript figure PNGs |
| `_build/` | `build_site.py` generator + `fetch_pdfs.py` / `fetch_pdfs_retry.py` + acquisition log |

## How highlighting works

- **Yellow** (`==…==` in Markdown, `<mark>` in HTML): manuscript passages citing the work — the claim it supports.
- **Orange** (`mark.field`): extracted evidence fields (task, inputs, method, outcome, split, validation…).
- **Blue chips** like `EMBRYO01-B0034`: block locators into the archived full-text reader (sha256-pinned).
- Excerpt blocks are AI paraphrases of source content, each tagged with its locator.

## PDF policy

PDFs are mirrored **only** where a local copy already existed or an open-access PDF was retrievable (OpenAlex / Unpaywall / Europe PMC). Works behind paywalls are represented by their DOI link. The acquisition log `_build/pdf_acquisition_log.json` records status + OA flag per paper. Before making this repository public, review `NOTICE.md`.

## ä¸­æ–‡è¯´æ˜Ž

## 中文说明

本文件夹是配合 AIR 投稿的"证据导航站"。`index.html` 为入口（可离线双击打开）。所有被引文献按正文章节归入 `papers/01_* ... 08_*`；每篇一个子目录，含 `README.md` 证据卡（高亮支持内容）、`card.html` 交互页与（如可获得）PDF。高亮含义见上表：黄色=正文引用该文的句子（即其支持的论点）；橙色=抽取的证据字段；蓝色芯片=原文块定位码（带 sha256）。构建脚本在 `_build/`；重新生成运行 `python _build/build_site.py`。

## Publish checklist (GitHub Pages)

1. `git init && git add . && git commit` inside this folder (or copy to a dedicated repo).
2. Push to GitHub; in **Settings → Pages**, choose *Deploy from a branch* → `main` / `/(root)`.
3. Site appears at `https://<user>.github.io/<repo>/`. No Actions/Jekyll needed.
'''
with open(os.path.join(GH,'README.md'),'w',encoding='utf-8') as f: f.write(readme)

notice='''# NOTICE — redistribution & verification status

- Article PDFs are mirrored **only** when (a) already present in the local corpus or (b) retrievable as an open-access copy (OA status recorded in `_build/pdf_acquisition_log.json`). Closed-access works are represented by DOI links only. Reviewers are responsible for confirming their institution's licence before further redistribution.
- All extracted fields, source-linked excerpts and block locators are **machine-generated and pending human verification**. They are provided to speed up checking, not as adjudicated facts.
- Manuscript passages shown are verbatim from the current draft and remain the authors' work.
- Figure PNGs under `assets/figures/Fig*.png` are the manuscript's own artwork.
'''
with open(os.path.join(GH,'NOTICE.md'),'w',encoding='utf-8') as f: f.write(notice)

with open(os.path.join(GH,'_config.yml'),'w') as f:
    f.write('# passthrough so Pages serves static files unchanged\nplugins: []\nmarkdown: kramdown\n')
with open(os.path.join(GH,'.gitignore'),'w') as f:
    f.write('.DS_Store\nThumbs.db\n__MACOSX/\n')
with open(os.path.join(GH,'.gitattributes'),'w') as f:
    f.write('* text=auto\n*.pdf binary\n*.png binary\n*.svg text\n')

# ================= QA =================
import glob
report={'papers':len(papers),'claims':sum(len(p['claims']) for p in papers),
        'card_pages':count_pages,'figs':len(FIGS_OUT),'charts':len(CHARTS),
        'pdf_status':{}}
for p in papers: report['pdf_status'][p['pdf']['status']]=report['pdf_status'].get(p['pdf']['status'],0)+1
# internal link check
bad=[]
for fp in glob.glob(os.path.join(GH,'**','*.html'),recursive=True):
    txt=open(fp,encoding='utf-8').read()
    for m in re.finditer(r'(?:href|src)="([^"#]+)"',txt):
        u=m.group(1)
        if u.startswith(('http','mailto','#')): continue
        tgt=os.path.normpath(os.path.join(os.path.dirname(fp),u))
        if not os.path.exists(tgt): bad.append({'from':os.path.relpath(fp,GH),'to':u})
    # remove stale paper folders not matching a paper's primary filing
    import shutil as _sh
    for _sec in os.listdir(os.path.join(GH,'papers')):
        _sd=os.path.join(GH,'papers',_sec)
        if not os.path.isdir(_sd): continue
        for _pid in os.listdir(_sd):
            _pp=[p for p in papers if p['id']==_pid]
            if _pp and _pp[0]['primary']['folder']!=_sec:
                _sh.rmtree(os.path.join(_sd,_pid), ignore_errors=True)
report['dead_links']=bad
report['dead_link_count']=len(bad)
json.dump(report,open(os.path.join(BUILD,'build_report.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('QA dead links:',len(bad))
for b in bad[:15]: print('  ',b)
print('REPORT',json.dumps(report['pdf_status']))

