# AI for IVF — Evidence Companion

> An interactive, reviewer-facing evidence library for the AIR manuscript *Artificial
> intelligence for in vitro fertilization* — every cited work is mapped to the
> section it supports, with highlighted claims, extracted fields, and source-linked PDFs.

**🔗 Live site → https://yukun-wen.github.io/AIR-evidence-companion/**

[![Site](https://img.shields.io/badge/site-live-5b7d95)](https://yukun-wen.github.io/AIR-evidence-companion/)
[![Works](https://img.shields.io/badge/cited%20works-247-7a8b6f)](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html)
[![PDFs](https://img.shields.io/badge/mirrored%20PDFs-91-c08a5f)](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html)

---

## ⚡ 30-second overview

| | |
|---|---|
| **What** | Evidence companion for a review manuscript — 247 cited works, organized by section |
| **Why** | Lets a reviewer trace *every citation* back to its supporting claim, fields, and source |
| **How** | Static site (HTML/CSS/JS) — no build step, works offline from `index.html` |
| **Contents** | Searchable catalog · evidence cards · highlighted PDFs · charts · methods |

---

## 🗺️ Quick navigation

| I want to… | Go to |
|---|---|
| See the big picture | [`index.html`](https://yukun-wen.github.io/AIR-evidence-companion/) |
| Find a specific paper | [`catalog.html`](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html) |
| Read what a claim cites | [`claims.html`](https://yukun-wen.github.io/AIR-evidence-companion/claims.html) |
| Compare two configurations | [`contrasts.html`](https://yukun-wen.github.io/AIR-evidence-companion/contrasts.html) |
| Browse by chapter | [`sections.html`](https://yukun-wen.github.io/AIR-evidence-companion/sections.html) |
| See charts & figures | [`atlas.html`](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html) |
| Check provenance / rebuild | [`methods.html`](https://yukun-wen.github.io/AIR-evidence-companion/methods.html) |
| Alphabetical / year index | [`az.html`](https://yukun-wen.github.io/AIR-evidence-companion/az.html) |

---

## 🧭 For reviewers

1. **Start** at the landing page — corpus stats and key figures.
2. **Catalog** — sortable, searchable table of all 247 works (`/` focuses search, headers sort).
3. **Evidence cards** — each paper's `card.html` shows the highlighted claim it supports,
   extracted fields, a **BibTeX** copy button, and a **DOI** link.
4. **Highlighted PDFs** — for mirrored core reports, *Highlighted-evidence PDF* opens the
   source with the supporting sentences already marked.
5. **Atlas** — hover a stacked bar for counts; click to open the pre-filtered catalog.

---

## 🔍 Highlighting legend

| Cue | Meaning |
|---|---|
| 🟨 Yellow `<mark>` | Manuscript passage citing the work — the claim it supports |
| 🟧 Orange `mark.field` | Machine-extracted evidence field (task, method, split, validation…) |
| 🔵 `<ID>-Bxxxx` chip | Block locator into the archived source text (sha256-pinned) |
| 📄 Highlighted-PDF button | Source PDF with supporting sentences marked |

*Excerpts are AI paraphrases of source content; all machine-derived fields are*
`*human verification pending`*.

---

## 📂 Repository layout

| Path | Content |
|---|---|
| `papers/<section>/<ID>/` | `README.md` evidence card · `card.html` · `<ID>.pdf` · `<ID>_highlighted.pdf` |
| `data/papers.js` / `.json` | Machine-readable record for every cited work |
| `assets/` | Stylesheet · `js/app.js` · generated SVG charts · manuscript figure PNGs |
| `_build/` | `build_site.py` generator · `highlight_pdfs.py` · acquisition/highlight logs |

---

## 🛠️ Rebuild

```bash
# Python 3.10+ · matplotlib · PyMuPDF
python _build/build_site.py      # regenerate pages, cards, charts, QA
python _build/highlight_pdfs.py  # annotate mirrored PDFs with highlight marks
```

Idempotent; ends with a dead-link QA pass (`_build/build_report.json`).

---

## 📜 PDF & licensing

PDFs are mirrored **only** where a local copy existed or an open-access version was
retrievable (OpenAlex / Unpaywall / Europe PMC). Paywalled works are represented by
their DOI link — no licensed PDFs are redistributed.
See [`NOTICE.md`](NOTICE.md) and `_build/pdf_acquisition_log.json`.

---

## 🚢 Deploy

```bash
git init -b main && git add -A && git commit -m "evidence companion"
gh repo create AIR-evidence-companion --public --source . --push
# Settings → Pages → Deploy from a branch → main / (root)
```
