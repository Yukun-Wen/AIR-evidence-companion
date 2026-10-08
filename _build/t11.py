import fitz
p = r'D:\KU-Assignment\IVF\review2\AIR_Review_Package\github\papers\01_introduction\OUTCOME05\OUTCOME05_highlighted.pdf'
doc = fitz.open(p)
print('pages', doc.page_count)
# render a page that has annots
for pi in range(doc.page_count):
    pg=doc[pi]
    annots=list(pg.annots() or [])
    if annots:
        print('page',pi,'has',len(annots),'annots')
        pix = pg.get_pixmap(matrix=fitz.Matrix(2,2))
        pix.save(r'D:\KU-Assignment\IVF\tmp\pdf_hl.png')
        break
