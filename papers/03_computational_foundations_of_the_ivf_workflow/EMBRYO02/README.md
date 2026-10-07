# EMBRYO02 — Automatic grading of human blastocysts from time-lapse imaging

**Kragh, Rimestad, Berntsen et al. (2019).** *Computers in biology and medicine*. DOI: [10.1016/j.compbiomed.2019.103494](https://doi.org/10.1016/j.compbiomed.2019.103494)

**Role:** core · contrasts C07, C08 · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** see EMBRYO02.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Embryo analysis extends from static morphology to development over time. The 2025 Istanbul consensus update distinguishes grading, ranking and selection using literature, practice-survey responses and expert opinion. These terms organize tasks with separate reference standards: morphology description, developmental forecasting and ploidy classification. Representative studies show how each standard creates a different learning problem and evaluation target [@ER032,EMBRYO01,EMBRYO02,EMBRYO03,EMBRYO04,EMBRYO05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2019--2021: learned visual and temporal representations [@EMBRYO01,EMBRYO02,EMBRYO04]==

> **§ Data, reference standards and the structure of evidence** : Sequences, trajectories and multiple views
> ==Embryo studies use several sequence designs: an image encoder followed by an LSTM for blastocyst grading, spatial and temporal streams for developmental prediction, and a video encoder with recurrent processing for outcome scoring. Frame selection, observation cutoff, sequence length and alignment determine their effective inputs within the incubator recordings [@EMBRYO02,EMBRYO04,OUTCOME03].==

> **§ Data, reference standards and the structure of evidence** : Sequences, trajectories and multiple views
> ==Multiple focal planes introduce a second form of repeated observation. They provide different optical views at approximately the same developmental time, whereas longitudinal frames provide different times. Representing spatial views and temporal samples as separate axes preserves this distinction and allows an architecture to combine either or both. This makes a focal-plane voting method distinguishable from a recurrent model even if both consume several images per embryo [@EMBRYO01,EMBRYO02].==

> **§ Computational methods**
> ==In the figure caption — Source-located quantitative examples for these mechanisms are presented in Table 7 STIM05,EMBRYO03,EMBRYO02,EMBRYO06==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Frame encoder plus recurrent memory (ordered frames / embryo) [@EMBRYO02]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Ordinal ICM and trophectoderm grading |  |
| **Inputs** | Three focal planes per time-lapse frame |  |
| **Prediction time** | Sequence from 90 h to maximal blastocyst expansion; CNN trained at embryologist annotation time |  |
| **Analysis unit** | embryo |  |
| **Method** | Xception feature encoder plus LSTM; shared representation with two ordinal classification heads |  |
| **Supervision / labels** | ICM/TE A-B-C annotations; independent majority-vote reference |  |
| **Outcome** | ICM and TE grades; secondary implantation association |  |
| **Sample sizes** | [{"value": 8664, "unit": "embryos", "locator": "Section 3, PDF pp4-5"}, {"value": 4032, "unit": "treatments", "locator": "Section 3, PDF p4"}, {"value": 851, "unit": "internal-test embryos", "locator": "Section 4, PDF p6"}, {"value": 55, "unit": "multi-annotator test embryos", "locator": "Section 3, PDF p5"}] |  |
| **Splitting** | Random 80/10/10 train/validation/test; patient-grouping not_reported_in_examined_text. |  |
| **Validation** | Four-clinic pooled development; internal test and separate multi-annotator test. |  |

## Source-linked excerpts
- [EMBRYO02-P003] ==A CNN–RNN used 30-frame blastocyst videos from 8,664 embryos across four clinics, with a random embryo split and a separate 55-embryo multi-reader comparison.==
- [EMBRYO02-P006] ==ICM and trophectoderm classification accuracy was moderate, and fetal-heart prediction AUC was 0.66 for the model versus 0.64 for humans without a significant difference.==
- [EMBRYO02-P008] ==Majority-vote morphology is an imperfect reference, no held-out clinic test was reported, and authors disclosed Vitrolife employment and stock ownership.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*