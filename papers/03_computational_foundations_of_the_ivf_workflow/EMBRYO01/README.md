# EMBRYO01 — Deep learning enables robust assessment and selection of human blastocysts after in vitro fertilization

**Khosravi, Kazemi, Zhan et al. (2019).** *NPJ digital medicine*. DOI: [10.1038/s41746-019-0096-y](https://doi.org/10.1038/s41746-019-0096-y)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Learning objectives and the interpretation of model outputs

**PDF:** see EMBRYO01.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Embryo analysis extends from static morphology to development over time. The 2025 Istanbul consensus update distinguishes grading, ranking and selection using literature, practice-survey responses and expert opinion. These terms organize tasks with separate reference standards: morphology description, developmental forecasting and ploidy classification. Representative studies show how each standard creates a different learning problem and evaluation target [@ER032,EMBRYO01,EMBRYO02,EMBRYO03,EMBRYO04,EMBRYO05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2019--2021: learned visual and temporal representations [@EMBRYO01,EMBRYO02,EMBRYO04]==

> **§ Data, reference standards and the structure of evidence** : Sequences, trajectories and multiple views
> ==Multiple focal planes introduce a second form of repeated observation. They provide different optical views at approximately the same developmental time, whereas longitudinal frames provide different times. Representing spatial views and temporal samples as separate axes preserves this distinction and allows an architecture to combine either or both. This makes a focal-plane voting method distinguishable from a recurrent model even if both consume several images per embryo [@EMBRYO01,EMBRYO02].==

> **§ Learning objectives and the interpretation of model outputs**
> ==Table entry; table caption: Supervision defines the outcome that a model can learn. — Morphology [@EMBRYO01]==

> **§ Learning objectives and the interpretation of model outputs** : Developmental forecasts and surrogate targets
> ==where $x_t$ denotes the available history, $h$ the prediction horizon and $E_t$ eligibility at the decision time; the fitted model $p_ ,h$ estimates the population target $p_h$. The conditional target changes with the eligible population: all normally fertilized embryos and embryos selected for continued culture define different forecasting problems. A shared cohort can also support forecasts at several observation times. Recording the window, horizon and eligibility rule identifies the quantity each model estimates. STORK distinguishes good and poor blastocysts, treats intermediate grades separately, and examines age and pregnancy associations. Primary discrimination evaluates morphology; association analyses connect grades to patient context and later outcomes [@EMBRYO01].==

> **§ Learning objectives and the interpretation of model outputs** : Matching objectives to admissible comparisons
> ==The objective taxonomy assigns an evaluation target to each model output. Measurement assesses agreement with a reference; prognosis assesses a defined outcome distribution; ranking assesses ordering within a choice set; and policy evaluation assesses consequences of use. Aligning the biological unit, available information, target and evaluation population defines comparable evaluations; controlled training, tuning and model selection isolate the tested computational change. Added-modality comparisons vary the specified input while retaining the other evaluation conditions. Morphology-based supervision evaluates agreement with grades, while treatment-level ranking evaluates an ordering among eligible siblings [@EMBRYO01,OUTCOME04]. The output's unit and purpose connect each comparison to its appropriate reference.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Binary blastocyst morphology grading (STORK) |  |
| **Inputs** | Static images at multiple focal depths |  |
| **Prediction time** | 110 h post-insemination |  |
| **Analysis unit** | image; embryo after voting |  |
| **Method** | ImageNet-initialized Inception-v1 CNN; focal-plane majority voting |  |
| **Supervision / labels** | Embryologist morphology grades mapped to good/poor; fair grades excluded from classifier training |  |
| **Outcome** | Morphological quality; separate age-plus-quality association analysis |  |
| **Sample sizes** | [{"value": 10148, "unit": "source embryos", "locator": "Methods / Images from human blastocysts; P051"}, {"value": 12001, "unit": "selected images", "locator": "Results; P015"}, {"value": 283, "unit": "blind-test embryos", "locator": "Results; P017-P019"}] |  |
| **Splitting** | 70% images training; remainder validation/test, stated nonoverlap. Patient-level disjointness not_reported_in_examined_text (P056). |  |
| **Validation** | Internal blind test; two external-center image cohorts. |  |

## Source-linked excerpts
- [EMBRYO01-B0034] ==STORK used transfer learning on static blastocyst images from several clinics, with good and poor morphology forming training labels while fair embryos were excluded from training.==
- [EMBRYO01-B0009] ==External image-classification AUCs varied across clinics, and comparisons with embryologists used a small multi-reader set and majority-vote labels.==
- [EMBRYO01-B0027] ==Multiple focal-plane images per embryo and an image-disjoint split do not clearly establish embryo- or patient-disjoint evaluation, direct pregnancy prediction was unsuccessful.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*