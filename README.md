# AI for IVF — Evidence Companion

[![site](https://img.shields.io/badge/site-live-5b7d95)](https://yukun-wen.github.io/AIR-evidence-companion/)
[![works](https://img.shields.io/badge/cited%20works-247-7a8b6f)](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html)
[![sections](https://img.shields.io/badge/sections-8-7fa8a0)](https://yukun-wen.github.io/AIR-evidence-companion/sections.html)
[![contrasts](https://img.shields.io/badge/contrasts-20-c08a5f)](https://yukun-wen.github.io/AIR-evidence-companion/contrasts.html)
[![PDFs](https://img.shields.io/badge/mirrored%20PDFs-91-8b7fa3)](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html)
[![license](https://img.shields.io/badge/license-CC--BY--4.0-aeb9b3)](NOTICE.md)

**Companion site → https://yukun-wen.github.io/AIR-evidence-companion/**

---

## Abstract

This repository accompanies the manuscript *Artificial intelligence for in vitro
fertilization* (submitted to *Artificial Intelligence Review*). It is an
interactive, openly accessible evidence library in which each of the **247 cited
works** is mapped to the manuscript section it supports, annotated with the
verbatim claim passages it substantiates, enriched with machine-extracted
evidence fields, and—where redistribution is permitted—mirrored as a PDF whose
supporting passages are highlighted in situ. The resource is designed to make
the evidentiary basis of the review inspectable at the level of individual
sentences, and to serve as a reproducible record of the citation network.

*Keywords — in vitro fertilization · artificial intelligence · evidence
synthesis · citation mapping · reproducible review*

[Overview](#overview) · [Contents](#2-contents) · [Reading conventions](#3-reading-conventions) · [Reproducibility](#4-reproducibility) · [Data](#5-data-availability--licensing) · [Citation](#6-citation)

---

## Overview

Narrative reviews routinely cite hundreds of primary studies, yet the reader
typically sees only the aggregated claim. This companion inverts that
arrangement: **every citation is anchored** to the manuscript sentence that
invokes it, to the evidence fields extracted from the source, and to a
sha256-pinned locator in the archived full text. Each claim can therefore be
traced back to its source rather than taken on trust.

| | |
|---|---|
| **Corpus** | [247 cited works](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html) · [125 core reports](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html) · [122 contextual](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html) |
| **Structure** | [10 manuscript sections](https://yukun-wen.github.io/AIR-evidence-companion/sections.html) · [7 workflow groups](https://yukun-wen.github.io/AIR-evidence-companion/az.html) |
| **Analysis** | [20 conditional contrasts](https://yukun-wen.github.io/AIR-evidence-companion/contrasts.html) · [12 charts](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html) |
| **Full text** | [91 mirrored PDFs](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html) · 58 with in-situ highlight marks |
| **Format** | Static site — no build step; works offline from `index.html` |


## 1. Design

The library is organized around four linked views of the same corpus:

- **Forward —** `claims.html` reads *from* a manuscript sentence *to* the works
  it cites; each passage is shown verbatim in context.
- **Backward —** each paper's `card.html` shows the claim(s) it supports, its
  extracted fields, and its locators, so a work can be evaluated in place.
- **Cross-cut —** `catalog.html` exposes the whole record as a sortable,
  searchable table with BibTeX export of any filtered subset.
- **Synthetic —** `atlas.html` and `contrasts.html` aggregate the corpus into
  charts and the 20 conditional within-report comparisons.

## 2. Contents

| Resource | Contents |
|---|---|
| [`index.html`](https://yukun-wen.github.io/AIR-evidence-companion) | Corpus statistics, section links, key figures |
| [`catalog.html`](https://yukun-wen.github.io/AIR-evidence-companion/catalog.html) | Sortable / searchable table; `/` focuses search; bulk BibTeX export |
| [`claims.html`](https://yukun-wen.github.io/AIR-evidence-companion/claims.html) | Claim passages → supporting citations |
| [`contrasts.html`](https://yukun-wen.github.io/AIR-evidence-companion/contrasts.html) | 20 conditional within-report comparisons (C01–C20) |
| [`sections.html`](https://yukun-wen.github.io/AIR-evidence-companion/sections.html) | Chapter-level index of cited works |
| [`atlas.html`](https://yukun-wen.github.io/AIR-evidence-companion/atlas.html) | Charts, manuscript figures, interactive section × workflow explorer |
| [`methods.html`](https://yukun-wen.github.io/AIR-evidence-companion/methods.html) | Construction pipeline, record schema, verification status |
| [`az.html`](https://yukun-wen.github.io/AIR-evidence-companion/az.html) | Indices by section, workflow group, author initial, year |
| `papers/<section>/<ID>/` | Evidence card, rendered page, mirrored + highlighted PDF |

## 3. Reading conventions

| Cue | Interpretation |
|---|---|
| Yellow `<mark>` | Verbatim manuscript passage citing the work — the claim it supports |
| Orange `mark.field` | Machine-extracted evidence field (task, inputs, method, split, validation) |
| `<ID>-Bxxxx` | Block locator into the archived source text, sha256-pinned |
| *Highlighted-PDF* button | Mirrored PDF with supporting sentences marked in situ |
| *human verification pending* | Machine-derived; confirm against the original before reliance |

<details>
<summary><b>Corpus composition</b> — counts by role, workflow and section (expand)</summary>

| Dimension | Count |
|---|---|
| Cited works | 247 |
| Core empirical reports | 125 |
| Contextual sources | 122 |
| Mirrored PDFs | 91 |
| PDFs with highlight marks | 58 |
| Conditional contrasts | 20 |
| Manuscript sections | 10 |
| Machine-readable records | `data/papers.json` |

</details>

## 4. Reproducibility

The site is fully static and regenerates deterministically:

```bash
# Python ≥3.10 · matplotlib · PyMuPDF
python _build/build_site.py      # pages, cards, charts, link QA
python _build/highlight_pdfs.py  # PDF highlight annotation
```

Each run ends with a dead-link QA pass (`_build/build_report.json`);
acquisition and highlight logs are kept under `_build/` for audit.

### Benchmarks

**Most-used datasets** (verified use counts)

| Resource | Open access | Reports | References |
|---|---|---|---|
| HFEA registry | [On request](https://www.hfea.gov.uk/about-us/data-research/) | 4 | [OUTCOME01](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/OUTCOME01/card.html), [EC063](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC063/card.html), [ER037](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/ER037/card.html), [ER039](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/ER039/card.html) |
| PCRM/SFU HMC | [On request](https://doi.org/10.1109/TBME.2017.2759665) | 3 | [EE006](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE006/card.html), [EE019](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE019/card.html), [EQF01](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/EQF01/card.html) |
| HuSHeM | [Open](https://doi.org/10.17632/tt3yj2pf38.1) | 3 | [EC080](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC080/card.html), [EC082](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC082/card.html), [EQS01](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EQS01/card.html) |
| Nantes/Gomez 704 | [Open](https://doi.org/10.5281/zenodo.6390798) | 3 | [EE015](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE015/card.html), [EE017](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE017/card.html), [EQF01](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/EQF01/card.html) |
| VISEM | [Open](https://doi.org/10.5281/zenodo.2640506) | 3 | [EC077](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC077/card.html), [EC081](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC081/card.html), [ER046](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/ER046/card.html) |
| Kromp blastocysts | [Open](https://doi.org/10.6084/m9.figshare.20123153.v3) | 2 | [EE046](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE046/card.html), [EQF01](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/EQF01/card.html) |
| Monash live sperm | [Open](https://doi.org/10.26180/25621500.v1) | 2 | [SPERM06](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/SPERM06/card.html), [EC079](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC079/card.html) |
| Oocytor (human) | [Open](https://doi.org/10.5281/zenodo.6502830) | 2 | [ER044](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/ER044/card.html), [OOCYTE02](https://yukun-wen.github.io/AIR-evidence-companion/papers/03_computational_foundations_of_the_ivf_workflow/OOCYTE02/card.html) |
| SMIDS | [Open](https://doi.org/10.17632/6xvdhc9fyb.1) | 2 | [EC080](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EC080/card.html), [EQS01](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EQS01/card.html) |
| CleavageEmbryo | [On request](https://zenodo.org/records/12602738) | 1 | [EE024](https://yukun-wen.github.io/AIR-evidence-companion/papers/04_data_reference_standards_and_the_structure_of_evidence/EE024/card.html) |

**Common evaluation metrics** (distinct reports reporting each)

| Metric | Reports |
|---|---|
| AUROC | 4 |
| Precision | 4 |
| Recall | 4 |
| Accuracy | 3 |
| F1 | 3 |
| Accuracy % | 3 |
| Dice | 2 |
| Mean Jaccard | 2 |
| Mean Dice | 2 |
| mAP@0.5 | 2 |
| Precision* | 1 |
| Recall* | 1 |

**Leading configurations — top-5 datasets** (within-report rank; metric in heading)

<details><summary><b>Hi-LabSpermMorpho</b> — 18-class sperm morphology classification · Accuracy %</summary>

| # | Model | Accuracy % | Report |
|---|---|---|---|
| 1 | Soft voting: EfficientNetV2-S + V2-M + V2-L | 67.7 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |
| 2 | V2-S + V2-M + V2-L originalfeatures / SVM+MLP-A+RF | 67.36 | — | EC078 |
| 3 | V2-S + V2-M + V2-L originalfeatures / SVM+RF | 67.22 | — | EC078 |
| 4 | V2-S + V2-M + V2-L originalfeatures / MLP-A+RF | 67.0 | — | EC078 |
| 5 | Soft voting: EfficientNetV2-S + EfficientNetV2-M | 66.86 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |
| 6 | EfficientNetV2-S + V2-M + V2-L originalfeatures / RF | 66.64 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |
| 7 | Soft voting: EfficientNetV2-M + EfficientNetV2-L | 66.59 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |
| 8 | Soft voting: EfficientNetV2-S + EfficientNetV2-L | 66.42 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |
| 9 | V2-S + V2-M + V2-L originalfeatures / SVM+MLP-A | 66.31 | — | EC078 |
| 10 | EfficientNetV2-S + V2-M + V2-L reducedfeatures / MLP-A | 66.16 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EC078 |

</details>

<details><summary><b>HFEA registry</b> — binary live-birth occurrence · Accuracy</summary>

| # | Model | Accuracy | Report |
|---|---|---|---|
| — | PSO + TabTransformer | 0.97 | [TabTransformer](https://github.com/lucidrains/tab-transformer-pytorch) | EC063 |
| — | PSO + Transformer | 0.963 | — | EC063 |
| — | PCA + TabTransformer | 0.941 | [TabTransformer](https://github.com/lucidrains/tab-transformer-pytorch) | EC063 |
| — | PCA + Transformer | 0.925 | — | EC063 |
| — | PSO + RF | 0.905 | — | EC063 |
| — | PCA + RF | 0.902 | — | EC063 |
| — | PCA + decision tree | 0.898 | — | EC063 |
| — | PSO + decision tree | 0.889 | — | EC063 |

</details>

<details><summary><b>CleavageEmbryo</b> — blastomere instance segmentation · mAP</summary>

| # | Model | mAP | Report |
|---|---|---|---|
| 1 | SAM dual branch + YOLOv8 | 0.874 | [SAM](https://github.com/facebookresearch/segment-anything) | EE024 |
| 2 | SOLOv2 | 0.764 | [SOLOv2](https://github.com/WXinlong/SOLO) | EE024 |
| 3 | RTMDet | 0.756 | [MMDet](https://github.com/open-mmlab/mmdetection) | EE024 |
| 4 | DONet | 0.75 | — | EE024 |
| 5 | Cascade MaskRCNN | 0.745 | [MMDet](https://github.com/open-mmlab/mmdetection) | EE024 |
| 6 | GAInS | 0.723 | — | EE024 |
| 7 | Mask2Former | 0.708 | [Mask2Former](https://github.com/facebookresearch/Mask2Former) | EE024 |
| 8 | Mask Scoring RCNN | 0.672 | [MMDet](https://github.com/open-mmlab/mmdetection) | EE024 |
| 9 | YOLACT | 0.643 | [YOLACT](https://github.com/dbolya/yolact) | EE024 |
| 10 | SAM auto | 0.002 | [SAM](https://github.com/facebookresearch/segment-anything) | EE024 |

</details>

<details><summary><b>HuSHeM</b> — four-class morphology · Accuracy %</summary>

| # | Model | Accuracy % | Report |
|---|---|---|---|
| 1 | BEiT-B | 93.52 | [BEiT](https://github.com/microsoft/unilm/tree/master/beit2) | EQS01 |
| 2 | Swin-V2-L | 90.9 | [Swin-V2](https://github.com/microsoft/Swin-Transformer) | EQS01 |
| 3 | Swin-V2-T | 90.83 | [Swin-V2](https://github.com/microsoft/Swin-Transformer) | EQS01 |
| 4 | Eff-V2-S | 90.43 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 5 | Eff-V2-L | 89.99 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 6 | Custom CNN + BEiT-B | 89.97 | [BEiT](https://github.com/microsoft/unilm/tree/master/beit2) | EQS01 |
| 7 | Eff-V2-S + BEiT-B | 89.56 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 8 | Eff-V2-S + Swin-V2-L | 88.59 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 9 | CoAtNet-1 | 88.55 | [paper](https://arxiv.org/abs/2106.04803) | EQS01 |
| 10 | CoAtNet-0 | 86.79 | [paper](https://arxiv.org/abs/2106.04803) | EQS01 |

</details>

<details><summary><b>SMIDS</b> — three-class morphology/non-sperm · Accuracy %</summary>

| # | Model | Accuracy % | Report |
|---|---|---|---|
| 1 | BEiT-B | 92.5 | [BEiT](https://github.com/microsoft/unilm/tree/master/beit2) | EQS01 |
| 2 | Swin-V2-L | 91.67 | [Swin-V2](https://github.com/microsoft/Swin-Transformer) | EQS01 |
| 3 | Custom CNN + BEiT-B | 91.57 | [BEiT](https://github.com/microsoft/unilm/tree/master/beit2) | EQS01 |
| 4 | Eff-V2-S + Swin-V2-L | 91.17 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 5 | Eff-V2-S | 91.13 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 5 | Swin-V2-T | 91.13 | [Swin-V2](https://github.com/microsoft/Swin-Transformer) | EQS01 |
| 7 | CoAtNet-1 | 91.07 | [paper](https://arxiv.org/abs/2106.04803) | EQS01 |
| 7 | Eff-V2-L | 91.07 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |
| 9 | CoAtNet-0 | 90.73 | [paper](https://arxiv.org/abs/2106.04803) | EQS01 |
| 10 | Eff-V2-S + BEiT-B | 90.67 | [EfficientNetV2](https://github.com/google/automl/tree/master/efficientnetv2) | EQS01 |

</details>

> Ranks are within a single report and protocol — not a global leaderboard.

## 5. Data availability & licensing

Full texts are mirrored only where a local copy already existed or an
open-access version was retrievable via OpenAlex, Unpaywall, or Europe PMC;
paywalled works are represented solely by their DOI — no licensed content is
redistributed. See `NOTICE.md` and `_build/pdf_acquisition_log.json`.

## 6. Citation

If you use this companion, please cite the manuscript it accompanies. A BibTeX
entry for every cited work can be copied from its card, or a filtered set can
be exported in bulk from `catalog.html`.

---

*Compiled by automated extraction and cross-referencing for reviewer inspection.
Pipeline documented at [`methods.html`](https://yukun-wen.github.io/AIR-evidence-companion/methods.html).*
