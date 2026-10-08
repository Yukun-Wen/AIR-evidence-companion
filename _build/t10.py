import fitz, json, os
GH=r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github'
log = json.load(open(GH+'\\_build\\pdf_highlight_log.json'))
papers = {p['id']:p for p in json.load(open(GH+'\\data\\papers.json',encoding='utf-8'))}
zero = [k for k,v in log.items() if not v.get('annots')]
print('zero annot:', len(zero))
for pid in zero[:6]:
    p=papers[pid]; src=GH+'\\papers\\'+p['primary']['folder']+'\\'+pid+'\\'+pid+'.pdf'
    if not os.path.exists(src): print(pid,'no file'); continue
    d=fitz.open(src)
    txt=d[0].get_text('text')
    print(pid, 'pages',d.page_count,'textlen p0',len(txt),'img-only' if len(txt)<200 else '')
    d.close()
