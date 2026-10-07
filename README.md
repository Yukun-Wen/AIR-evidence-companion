# AI for IVF — Evidence Companion (reviewer-facing)

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
