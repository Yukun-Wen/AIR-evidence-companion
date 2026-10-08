import fitz, re
p = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github\papers\03_computational_foundations_of_the_ivf_workflow\EMBRYO01\EMBRYO01.pdf'
doc = fitz.open(p)
# build sentence index per page
for pi in range(doc.page_count):
    txt = doc[pi].get_text('text')
    sents = re.split(r'(?<=[.!?])\s+', txt.replace('\n',' '))
    # find sentences mentioning transfer learning / AUC / focal
    for s in sents:
        if re.search(r'transfer learning|AUC|focal', s, re.I):
            print(f'p{pi}: {s[:110]}')
