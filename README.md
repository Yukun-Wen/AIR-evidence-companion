# AI for IVF — Evidence Companion

[![Site](https://img.shields.io/badge/site-live-5b7d95)](https://yukun-wen.github.io/AIR-evidence-companion/)
[![Works](https://img.shields.io/badge/cited%20works-247-7a8b6f)](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html)
[![PDFs](https://img.shields.io/badge/mirrored%20PDFs-91-c08a5f)](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html)

**Live site:** https://yukun-wen.github.io/AIR-evidence-companion/

An interactive, reviewer-facing evidence library for the AIR manuscript submission
*Artificial intelligence for in vitro fertilization*. Every one of the **247 cited
works** is mapped to the manuscript section(s) it supports, with highlighted
manuscript claims, machine-extracted evidence fields, archived source locators,
and — where a local or open-access PDF exists — a **highlighted PDF** marking the
passages that support the manuscript's argument.

No build step or JavaScript framework is required: this is a static HTML/CSS/JS
site that also works when opened offline (`index.html`).

## For reviewers — how to navigate

1. **Start at the landing page** — corpus stats, section links, key figures.
2. **Browse by chapter** — `sections.html` groups all cited works by the
   manuscript section that first cites them.
3. **Search & filter** — `catalog.html` is a sortable, searchable table of
   all 247 works (click a column header to sort; filter by role / section /
   workflow / PDF availability / contrast participation).
4. **Interactive explorer** — on `atlas.html`, hover a stacked section bar
   for counts and click a segment to open the pre-filtered catalog.
5. **Evidence cards** — each paper's `card.html` shows the highlighted
   manuscript passage it supports, its extracted fields, and a **BibTeX**
   button that copies the citation to the clipboard.
6. **Highlighted PDFs** — for the 58 core reports with mirrored full text, the
   *Highlighted-evidence PDF* button opens the source PDF with the supporting
   sentences already marked in yellow.

## Pages

| Page | Purpose |
|---|---|
| `index.html` | Landing: corpus stats, section links, key figures |
| `az.html` | Master index — works by section, workflow group, author initial, year |
| `catalog.html` | Searchable / sortable / filterable table of all cited works |
| `claims.html` | Manuscript claim passages → citing papers (highlighted) |
| `contrasts.html` | 20 conditional within-report comparisons + delta chart |
| `sections.html` | Chapter index — papers filed by first-cited manuscript section |
| `atlas.html` | Charts, manuscript figures, and the interactive explorer |

## Repository layout

| Path | Content |
|---|---|
| `papers/<section>/<ID>/` | Per-paper folder: `README.md` evidence card, `card.html`, `<ID>.pdf`, `<ID>_highlighted.pdf` when present |
| `data/papers.js` / `.json` | Machine-readable record for every cited work |
| `assets/` | Stylesheet, `js/app.js`, generated SVG charts, manuscript figure PNGs |
| `_build/` | `build_site.py` generator, `highlight_pdfs.py`, acquisition/highlight logs |

## Highlighting conventions

| Visual cue | Meaning |
|---|---|
| Yellow `<mark>` | Manuscript passage citing the work — the claim it supports |
| Orange `mark.field` | Machine-extracted evidence field (task, inputs, method, outcome, split, validation…) |
| Blue chip `<ID>-Bxxxx` | Block locator into the archived full-text reader (sha256-pinned) |
| "Highlighted-evidence PDF" button | Source PDF with supporting sentences marked |

Excerpt blocks are AI paraphrases of source content, each tagged with its locator.
All machine-extracted fields are flagged *human verification pending*.

## Rebuilding the site

```bash
# requires Python 3.10+ with matplotlib + PyMuPDF
python _build/build_site.py      # regenerate pages, cards, charts, QA
python _build/highlight_pdfs.py  # annotate mirrored PDFs with highlight marks
```

The generator is idempotent and ends with a dead-link QA pass
(`_build/build_report.json`).

## Deploying to GitHub Pages

```bash
git init -b main && git add -A && git commit -m "evidence companion"
gh repo create AIR-evidence-companion --public --source . --push
# Settings → Pages → Deploy from a branch → main / (root)
```

## PDF & licensing policy

PDFs are mirrored **only** where a local copy already existed or an open-access
PDF was retrievable (OpenAlex / Unpaywall / Europe PMC). Works behind paywalls
are represented by their DOI link — no licensed PDFs are redistributed. The
acquisition log `_build/pdf_acquisition_log.json` records status + OA flag per
paper. See `NOTICE.md`.

## 中文说明

本文件夹是配合 AIR 投稿的"证据导航站"。`index.html` 为入口（可离线双击打开）。
所有被引文献按正文章节归入 `papers/01_* … 10_*`；每篇一个子目录，含
`README.md` 证据卡（高亮支持内容）、`card.html` 交互页与（如可获得）PDF。
高亮含义：黄色=正文引用该文的句子（即其支持的论点）；橙色=抽取的证据字段；
蓝色芯片=原文块定位码（带 sha256）。构建脚本在 `_build/`，重新生成运行
`python _build/build_site.py`。在线版见
https://yukun-wen.github.io/AIR-evidence-companion/
