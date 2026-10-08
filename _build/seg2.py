
# ================= HTML GENERATION =================
ASSETS = os.path.join(GH,'assets'); FIGS = os.path.join(ASSETS,'figures')
os.makedirs(FIGS, exist_ok=True); os.makedirs(os.path.join(ASSETS,'js'), exist_ok=True)

CSS = """
:root{--ink:#152936;--blue:#0f5e78;--accent:#b56c22;--bg:#f4f7f9;--card:#fff;--border:#d5e0e6;--hl:#fff2a8;--hl2:#ffe1b0}
*{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,"Segoe UI",Roboto,"Microsoft YaHei",sans-serif}
a{color:var(--blue);text-decoration:none} a:hover{text-decoration:underline}
header.site{background:linear-gradient(135deg,#123a4d,#0f5e78);color:#fff;padding:26px 5%}
header.site h1{margin:0 0 6px;font-size:25px;font-weight:650}
header.site p{margin:4px 0;max-width:1100px;opacity:.92;font-size:14px}
nav.crumbs{background:#0d3546;padding:7px 5%;font-size:13px}
nav.crumbs a{color:#bfe0ec;margin-right:6px}
main{max-width:1180px;margin:auto;padding:22px 4%}
.stats{display:flex;flex-wrap:wrap;gap:12px;margin:18px 0}
.stat{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px 18px;min-width:130px}
.stat b{display:block;font-size:26px;color:var(--blue)}
.stat span{font-size:12px;color:#4a6572}
.card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px 20px;margin:14px 0}
.badge{display:inline-block;padding:1px 9px;border-radius:11px;font-size:12px;margin:2px 3px 2px 0;border:1px solid var(--border);background:#eef4f7;color:#2b5568}
.badge.core{background:#e3f2e9;border-color:#9fcdb4;color:#1d6643}
.badge.ctx{background:#f0ecf7;border-color:#c9bce0;color:#5a4785}
.badge.contrast{background:#fdeee0;border-color:#e8b477;color:#8a4d12}
.badge.pending{background:#fdf0f0;border-color:#e5a8a8;color:#8d3434}
.badge.loc{font-family:ui-monospace,Consolas,monospace;background:#eef6fb}
mark{background:var(--hl);padding:0 2px;border-radius:2px}
mark.field{background:var(--hl2)}
blockquote.ex{border-left:4px solid var(--blue);background:#f0f7fa;margin:10px 0;padding:10px 14px;border-radius:0 8px 8px 0}
blockquote.claim{border-left:4px solid var(--accent);background:#fffaf2;margin:10px 0;padding:10px 14px;border-radius:0 8px 8px 0}
table.data{border-collapse:collapse;width:100%;font-size:13.5px}
table.data th,table.data td{border:1px solid var(--border);padding:6px 9px;text-align:left;vertical-align:top}
table.data th{background:#e9f0f4;position:sticky;top:0}
table.data tr:nth-child(even){background:#f7fafb}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0;padding:12px;background:var(--card);border:1px solid var(--border);border-radius:10px;position:sticky;top:0;z-index:5}
.filters input,.filters select{padding:6px 9px;border:1px solid #b7c8d2;border-radius:6px;font-size:13.5px}
.filters input[type=search]{flex:1;min-width:220px}
.fieldgrid{display:grid;grid-template-columns:170px 1fr;gap:0;border:1px solid var(--border);border-radius:8px;overflow:hidden;margin:10px 0}
.fieldgrid>div{padding:8px 12px;border-bottom:1px solid var(--border)}
.fieldgrid .fl{background:#f0f5f8;font-weight:600;font-size:13px}
.fieldgrid .fv{font-size:13.5px}
details{border:1px solid var(--border);border-radius:8px;background:var(--card);margin:8px 0;padding:10px 14px}
summary{cursor:pointer;font-weight:600;color:var(--blue)}
.warn{border-left:4px solid var(--accent);background:#fff8ee;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:13.5px}
.note{border-left:4px solid var(--blue);background:#eff6f9;padding:12px 16px;border-radius:0 8px 8px 0;margin:14px 0;font-size:13.5px}
img.fig{max-width:100%;border:1px solid var(--border);border-radius:8px;background:#fff;margin:8px 0}
.figcap{font-size:12.5px;color:#4a6572;margin:4px 0 18px}
.small{font-size:12.5px;color:#4a6572}
.mono{font-family:ui-monospace,Consolas,monospace;font-size:12px;word-break:break-all}
footer{border-top:1px solid var(--border);margin-top:40px;padding:16px 5%;font-size:12.5px;color:#5a7482}
h2.sec{border-bottom:2px solid var(--blue);padding-bottom:4px;margin-top:26px}
.pill{font-size:11px;padding:1px 7px;border-radius:9px;background:#dcebf1;color:#24586f;margin-left:6px}
a.pdfbtn{display:inline-block;background:#0f5e78;color:#fff !important;padding:3px 12px;border-radius:6px;font-size:12.5px;margin-top:6px}
a.pdfbtn.none{background:#9fb3bd}
"""
with open(os.path.join(ASSETS,'style.css'),'w',encoding='utf-8') as f: f.write(CSS)

JS = """
function esc(s){return (s||'').replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
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
        names=[n for n in z.namelist() if re.match(r'(artwork/)?Fig\d+\.pdf$', n)]
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
      '<link rel="stylesheet" href="'+root+'assets/style.css"></head><body data-root="'+root+'">'
      '<header class="site"><h1>AI for IVF &middot; Evidence Companion</h1>'
      '<p>Interactive evidence library for the manuscript <i>Artificial intelligence for in vitro fertilization</i> '
      '(Artificial Intelligence Review submission). Every cited work is mapped to the manuscript sections it supports, '
      'with highlighted manuscript claims, extracted fields, and source locators.</p></header>'
      '<nav class="crumbs"><a href="'+root+'index.html">Home</a> &rsaquo; '+cr+'</nav>'
      '<main>'+body+'</main>'
      '<footer>Generated '+datetime.date.today().isoformat()+' &middot; Evidence compiled by automated extraction; human verification pending '
      '&middot; PDFs mirrored only where locally held or openly licensed; otherwise DOI links.</footer>'
      '<script src="'+root+'data/papers.js"></script><script src="'+root+'assets/js/app.js"></script></body></html>')

count_pages=0
for p in papers:
    pf = p['primary']['folder']
    pdir = os.path.join(GH,'papers',pf,p['id'])
    os.makedirs(pdir, exist_ok=True)
    pdf = p['pdf']; has_pdf = pdf['status'] in ('local_copy','downloaded_oa','exists')
    pdf_link = ('<a class="pdfbtn" href="'+p['id']+'.pdf">Open PDF</a>' if has_pdf else
                ('<a class="pdfbtn none" href="'+esc(p['doi_url'])+'">PDF not mirrored &mdash; DOI link</a>' if p['doi_url'] else ''))
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
                if isinstance(val,(dict,list)): val=json.dumps(val,ensure_ascii=False)
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
        ct_html+='</table><p class="small">Full detail on <a href="../../contrasts.html">contrasts page</a>.</p>'
    body=('<div class="card"><span class="mono">'+p['id']+'</span> '+(' '.join(badges))+
      '<h2 style="margin:8px 0">'+esc(p['title'])+'</h2>'
      '<p class="small">'+esc(p['authors_short'])+' ('+str(p['year'])+'). <i>'+esc(p['venue'])+'</i>.<br>'
      'DOI: <a href="'+esc(p['doi_url'])+'">'+esc(p['doi'])+'</a> &middot; '+pdf_link+'</p>'
      '<p class="small">Cited in: '+secs_html+'</p></div>'
      '<div class="warn"><b>Verification status.</b> Evidence below is machine-extracted and AI-adjudicated; <b>author/human verification is pending</b>. '
      'Locators (e.g. '+p['id']+'-B0014) are block anchors into the archived full-text reader'+
      ((', sha256 <span class="mono">'+p['sha256'][:16]+'&hellip;</span>') if p['sha256'] else '')+'.</div>'
      +('<h3>Manuscript passages citing this work <span class="pill">highlighted = supported claim</span></h3>'+claims_html if claims_html else '<p class="small">No extractable in-text passage.</p>')
      +(('<blockquote class="ex"><b>Adjudicated scope:</b> <mark>'+esc(p['scope'])+'</mark></blockquote>') if p['scope'] else '')
      +(('<blockquote class="ex"><b>Method summary:</b> '+esc(p['method_summary'])+'</blockquote>') if p['method_summary'] else '')
      +fld+ex_html+ct_html
      +(('<h3>All archived block locators</h3><p>'+locs_html+'</p>') if p['locators'] else ''))
    with open(os.path.join(pdir,'card.html'),'w',encoding='utf-8') as f:
        f.write(page(p['id']+' — '+p['title'][:60],
                     [('Sections','../../sections.html'),(p['primary']['title'],'../../sections.html#'+pf),(p['id'],'')],
                     body, root='../../'))
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
                v=str(v).replace('|','\|')
                md.append('| **'+FLABEL[fn]+'** | '+v+' | '+' '.join(p['field_locs'].get(fn) or [])+' |')
        md.append('')
    if p['excerpts']:
        md.append('## Source-linked excerpts')
        for ex in p['excerpts']: md.append('- ['+ex.get('locator','')+'] =='+ex.get('paraphrase','')+'==')
        md.append('')
    md.append('---'); md.append('*Machine-extracted; human verification pending. == ... == marks supporting content.*')
    with open(os.path.join(pdir,'README.md'),'w',encoding='utf-8') as f: f.write('
'.join(md))
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
    with open(os.path.join(sd,'README.md'),'w',encoding='utf-8') as f: f.write('
'.join(md))
