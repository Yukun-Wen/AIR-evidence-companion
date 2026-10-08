
# ================= CHARTS =================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.edgecolor':'#9fb3bd','axes.labelcolor':'#152936',
                     'xtick.color':'#3a5563','ytick.color':'#3a5563','figure.dpi':110})
BLUE='#0f5e78'; ACC='#b56c22'; GREEN='#2e7d52'; PURP='#6a5acd'; RED='#a33'; GREY='#7d97a3'
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
ax.text(0,0,'247\nworks',ha='center',va='center',fontsize=13,fontweight='bold',color=BLUE)
savefig(fig,'corpus_composition.svg')

# 2 workflow groups
fig,ax=plt.subplots(figsize=(6.4,3.4))
names=[w['workflow_group'] for w in WF][::-1]; vals=[w['reports'] for w in WF][::-1]
ax.barh(names,vals,color=BLUE,height=.62)
for i,v in enumerate(vals): ax.text(v+.5,i,str(v),va='center',fontsize=9,color=BLUE)
ax.set_xlabel('Core empirical reports'); ax.set_xlim(0,max(vals)*1.12)
savefig(fig,'workflow_groups.svg')

# 3 year histogram
years=[p['year'] for p in papers if isinstance(p['year'],int)]
bins=range(min(years),max(years)+2)
fig,ax=plt.subplots(figsize=(6.6,3.0))
core_y=[p['year'] for p in papers if p['role']=='core' and isinstance(p['year'],int)]
ctx_y=[p['year'] for p in papers if p['role']!='core' and isinstance(p['year'],int)]
ax.hist([ctx_y,core_y],bins=bins,stacked=True,color=[PURP,BLUE],label=['Contextual','Core'],edgecolor='w')
ax.set_xlabel('Publication year'); ax.set_ylabel('Cited works'); ax.legend(frameon=False)
savefig(fig,'citations_by_year.svg')

# 4 citation density per top section (primary filing counts)
sec_counts=collections.Counter(p['primary']['folder'] for p in papers)
labels=[s['folder'].split('_',1)[0]+' '+s['title'][:34] for s in SEC_INFO]
vals=[sec_counts.get(s['folder'],0) for s in SEC_INFO]
fig,ax=plt.subplots(figsize=(6.8,3.6))
ax.bar(range(len(vals)),vals,color=[BLUE if i<8 else GREY for i in range(len(vals))])
ax.set_xticks(range(len(vals))); ax.set_xticklabels([s['folder'].split('_')[0] for s in SEC_INFO])
ax.set_ylabel('Works filed (primary)'); ax.set_xlabel('Manuscript section')
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
ax.set_xlabel('Metric value (A grey → B colored)'); ax.grid(axis='x',alpha=.25)
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
ax.imshow(M,cmap=matplotlib.colors.ListedColormap(['#eef4f7',BLUE]),aspect='auto',vmin=0,vmax=1)
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

CHARTS=[('corpus_composition.svg','Corpus composition'),('workflow_groups.svg','Core reports by IVF workflow group'),
        ('citations_by_year.svg','Cited works by publication year'),('section_filing.svg','Primary filing across manuscript sections'),
        ('contrast_deltas.svg','Conditional contrasts C01–C20 (within-report A→B)'),
        ('dataset_family_heatmap.svg','Four-dataset model-family matrix'),('resource_reuse.svg','Most-reused named resources')]
print('charts written')

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
<select id="fSec" onchange="render()"></select>
<select id="fWf" onchange="render()"></select>
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
clm='<h2>Manuscript claims → supporting papers</h2><p class="small">Each highlighted block is a verbatim manuscript passage; beneath it are the works it cites. Click an ID for that paper’s evidence card.</p>'
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
<div class="card"><h3 style="margin-top:0">Evidence highlights</h3><img class="fig" src="assets/figures/contrast_deltas.svg"><div class="figcap">Conditional contrasts: within-report A→B configuration deltas (color = direction).</div>
<img class="fig" src="assets/figures/dataset_family_heatmap.svg"><div class="figcap">Four-dataset benchmark: 15 independent model families, best representative per cell.</div></div>
<div class="warn"><b>Honesty note.</b> All extracted content is machine-derived and <b>author verification is pending</b>. Highlighted passages are manuscript text citing each work; source excerpts are paraphrases keyed to archived block locators (sha256-pinned). PDFs are mirrored only where locally held or openly licensed; otherwise the DOI link is provided.</div>
'''
with open(os.path.join(GH,'index.html'),'w',encoding='utf-8') as f:
    f.write(page('Evidence companion — AI for IVF review',[('Home','')],idx_body))
print('top pages written')
