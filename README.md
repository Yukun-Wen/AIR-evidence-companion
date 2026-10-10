# AI for IVF — Evidence Companion

[![Site](https://img.shields.io/badge/site-live-5b7d95)](https://yukun-wen.github.io/AIR-evidence-companion/)
[![Works](https://img.shields.io/badge/cited%20works-247-7a8b6f)](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html)
[![PDFs](https://img.shields.io/badge/mirrored%20PDFs-91-c08a5f)](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html)

**Companion site:** https://yukun-wen.github.io/AIR-evidence-companion/

---

### Abstract

This repository accompanies the manuscript *Artificial intelligence for in vitro
fertilization* (submitted to *Artificial Intelligence Review*). It provides an
interactive, openly accessible evidence library in which each of the 247 cited
works is mapped to the manuscript section it supports, annotated with the
verbatim claim passages it substantiates, enriched with machine-extracted
evidence fields, and—where redistribution is permitted—mirrored as a PDF whose
supporting passages are highlighted in situ. The resource is designed to make
the evidentiary basis of the review inspectable at the level of individual
sentences, and to serve as a reproducible record of the citation network.

*Keywords: in vitro fertilization; artificial intelligence; evidence synthesis;
citation mapping; reproducible review*

---

## 1. Rationale

Narrative reviews routinely cite hundreds of primary studies, yet the reader
typically sees only the aggregated claim. This companion inverts that
arrangement: every citation is anchored to the manuscript sentence that invokes
it, to the evidence fields extracted from the source, and to sha256-pinned
locators in the archived full text. The intent is transparency—each claim can
be traced to its source rather than taken on trust—and reusability, since the
underlying records are machine-readable (`data/papers.json`).

## 2. Content

| Resource | Description |
|---|---|
| `index.html` | Landing view: corpus statistics, section overview, key figures |
| `catalog.html` | Sortable, searchable table of all 247 cited works; BibTeX export of filtered sets |
| `claims.html` | Manuscript claim passages with their supporting citations |
| `contrasts.html` | Twenty conditional within-report comparisons (C01–C20) |
| `sections.html` | Chapter-level index of cited works |
| `atlas.html` | Generated charts, manuscript figures, interactive section × workflow explorer |
| `methods.html` | Construction pipeline, record schema, verification status |
| `az.html` | Indices by section, workflow group, first-author initial, year |
| `papers/<section>/<ID>/` | Per-work evidence card, rendered page, and mirrored/highlighted PDF where available |

## 3. Reading conventions

| Cue | Interpretation |
|---|---|
| Yellow highlight | Verbatim manuscript passage citing the work—the claim it supports |
| Orange highlight | Machine-extracted evidence field (task, inputs, method, split, validation) |
| `<ID>-Bxxxx` chip | Block locator into the archived source text, sha256-pinned |
| Highlighted-PDF button | Mirrored PDF with supporting sentences marked in situ |

Excerpts are machine-generated paraphrases; all extracted fields carry the
designation *human verification pending* and should be confirmed against the
original publication before reliance.

## 4. Reproducibility

The site is fully static (HTML/CSS/JS) and regenerates deterministically:

```bash
# Python ≥3.10, matplotlib, PyMuPDF
python _build/build_site.py      # pages, cards, charts, link QA
python _build/highlight_pdfs.py  # PDF highlight annotation
```

Each run terminates with a dead-link QA pass (`_build/build_report.json`);
PDF acquisition and highlight logs are retained under `_build/` for audit.

## 5. Data availability & licensing

Full texts are mirrored only where a local copy already existed or an
open-access version was retrievable through OpenAlex, Unpaywall, or Europe PMC;
paywalled works are represented solely by their DOI. No licensed content is
redistributed. See `NOTICE.md` and `_build/pdf_acquisition_log.json`.

## 6. Citation

If you reference this evidence companion, please cite the manuscript itself.
A BibTeX entry for each cited work can be copied from its evidence card or
exported in bulk from the catalog.

---

*Compiled by automated extraction and cross-referencing; designed for reviewer
inspection. Generated with `build_site.py`—see `methods.html` for the full
pipeline.*
