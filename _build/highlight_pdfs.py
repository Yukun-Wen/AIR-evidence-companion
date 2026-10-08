# -*- coding: utf-8 -*-
"""Annotate mirrored paper PDFs with highlights marking the passages that
support the manuscript's extracted fields/excerpts. Produces <PID>_highlighted.pdf
in each paper folder plus pdf_highlight_log.json."""
import fitz, json, re, os, sys, time
GH = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github'
papers = json.load(open(os.path.join(GH,'data','papers.json'),encoding='utf-8'))
B = chr(92)

def norm(s): return re.sub(r'\s+',' ', s.lower()).strip()
STOP = set('the a an and or of to in for on with by is are was were be been we our their this that these those it its as at from between within during after before which who whom whose such than then when where while how what why not no nor can could may might should will would do does did have has had other each more most less least some any all few many much very also'.split())
def content_words(s):
    return [w for w in re.findall(r'[a-zA-Z]{4,}', s.lower()) if w not in STOP]

def highlight_query(doc, query, color=(1,0.85,0.2)):
    """Find sentence(s) in doc best matching query; highlight words of that
    sentence region. Returns count of annots added."""
    qwords = set(content_words(query))
    if not qwords: return 0
    added = 0
    best = []
    for pi in range(doc.page_count):
        pg = doc[pi]
        words = pg.get_text('words')  # x0,y0,x1,y1,word,block,line,word_no
        if not words: continue
        # group words into lines: key=(block_no,line_no)
        lines = {}
        for w in words:
            lines.setdefault((w[5],w[6]),[]).append(w)
        # join lines into sentence-ish spans by block
        spans = {}
        for (b,l),ws in lines.items():
            txt = ' '.join(w[4] for w in ws)
            r = fitz.Rect(ws[0][:2]+ws[-1][2:4])
            spans.setdefault(b,[]).append((r,txt))
        for b,ln_list in spans.items():
            full = ' '.join(t for _,t in ln_list)
            # split into sentences
            sents = re.split(r'(?<=[.!?;])\s+(?=[A-Z(])', full)
            # map chars to rects approx: score each line by qwords overlap
            for r,txt in ln_list:
                sw = set(content_words(txt))
                score = len(qwords & sw)
                if score >= max(3, len(qwords)//3):
                    best.append((score, pi, r, txt))
    best.sort(key=lambda x:-x[0])
    for score,pi,r,txt in best[:3]:
        pg = doc[pi]
        try:
            annot = pg.add_highlight_annot(r)
            annot.set_colors(stroke=color)
            annot.set_opacity(0.45)
            annot.update()
            added += 1
        except Exception:
            try: pg.add_highlight_annot(r).update(); added+=1
            except Exception: pass
    return added

log = {}
t0=time.time()
for p in papers:
    pid = p['id']
    st = p.get('pdf',{}).get('status','')
    if st not in ('local_copy','downloaded_oa','exists'): continue
    pf = p['primary']['folder']
    src = os.path.join(GH,'papers',pf,pid,pid+'.pdf')
    if not os.path.exists(src): continue
    queries = []
    for e in p.get('excerpts') or []:
        if e.get('paraphrase'): queries.append(e['paraphrase'])
    for fn,v in (p.get('fields') or {}).items():
        if isinstance(v,str) and len(v)>15: queries.append(v)
        elif isinstance(v,list):
            for x in v:
                if isinstance(x,dict) and x.get('value'): queries.append(str(x.get('value'))+' '+str(x.get('unit','')))
    queries = queries[:14]  # cap per paper
    try:
        doc = fitz.open(src)
    except Exception as e:
        log[pid]={'error':str(e)}; continue
    n=0
    for q in queries:
        try: n += highlight_query(doc, q)
        except Exception: pass
    out = os.path.join(GH,'papers',pf,pid,pid+'_highlighted.pdf')
    try:
        if doc.is_encrypted:
            log[pid]={'error':'encrypted','annots':0}; doc.close(); continue
        doc.save(out, garbage=3, deflate=True)
        log[pid]={'annots':n,'file':pid+'_highlighted.pdf'}
    except Exception as e:
        log[pid]={'error':'save:'+str(e),'annots':0}
    doc.close()
    if n: print(pid, 'annots', n)

json.dump(log, open(os.path.join(GH,'_build','pdf_highlight_log.json'),'w'))
print('annotated', sum(1 for v in log.values() if v.get('annots',0)>0), 'of', len(log), 'elapsed', round(time.time()-t0,1),'s')
