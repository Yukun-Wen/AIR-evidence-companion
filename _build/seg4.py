
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

## 中文说明

本文件夹是配合 AIR 投稿的“证据导航站”。`index.html` 为入口（可离线双击打开）。所有被引文献按正文章节归入 `papers/01_* … 08_*`；每篇一个子目录，含 `README.md` 证据卡（高亮支持内容）、`card.html` 交互页与（如可获得）PDF。高亮含义见上表。构建脚本在 `_build/`；重新生成运行 `python _build/build_site.py`。

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
report['dead_links']=bad
report['dead_link_count']=len(bad)
json.dump(report,open(os.path.join(BUILD,'build_report.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('QA dead links:',len(bad))
for b in bad[:15]: print('  ',b)
print('REPORT',json.dumps(report['pdf_status']))
