# OUTCOME03 — Robust and generalizable embryo selection based on artificial intelligence and time-lapse image sequences

**Berntsen, Rimestad, Lassen et al. (2022).** *PloS one*. DOI: [10.1371/journal.pone.0262661](https://doi.org/10.1371/journal.pone.0262661)

**Role:** core · contrasts C17 · workflow: Embryo assessment and selection

**Cited in:** Introduction, Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence

**PDF:** see OUTCOME03.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Introduction**
> ==A method's evaluation must preserve that connection. In one embryo-selection study, the same model obtained an area under the receiver operating characteristic curve (AUC) of 0.67 among transferred embryos with known fetal-heartbeat outcomes and 0.95 when the evaluation also included discarded embryos treated as negative examples [@OUTCOME03]. These values measure discrimination under different population and label definitions. Selecting among transferable sibling embryos defines a further, within-cycle ranking task. The example illustrates a recurring difficulty in interpreting IVF AI: a change in performance can arise from the computational method, the information supplied to it or the question posed by the evaluation. Distinguishing these sources of change is essential to identifying useful methodological progress.==

> **§ Introduction**
> ==In the figure caption — (c) The same embryo model has AUC 0.67 among 2,212 transferred embryos with known fetal-heartbeat outcomes and 0.95 in the nested 17,249-embryo test set including discarded embryos assigned negative labels OUTCOME03==

> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Treatment outcomes connect embryo-level scores to patient-level prospects through transfer policy, the number and order of available embryos, and follow-up across transfers. Embryo-scoring studies evaluate outcome association, while a randomized comparison of AI-guided and morphology-guided selection evaluates use of the score within a clinical policy. The unit of prediction and the intervention design determine which part of this connection is measured [@OUTCOME03,OUTCOME04,OUTCOME05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2022--2023: scaled scoring and molecular endpoints [@OUTCOME03,EMBRYO05]==

> **§ Data, reference standards and the structure of evidence** : Sequences, trajectories and multiple views
> ==Embryo studies use several sequence designs: an image encoder followed by an LSTM for blastocyst grading, spatial and temporal streams for developmental prediction, and a video encoder with recurrent processing for outcome scoring. Frame selection, observation cutoff, sequence length and alignment determine their effective inputs within the incubator recordings [@EMBRYO02,EMBRYO04,OUTCOME03].==

> **§ Data, reference standards and the structure of evidence** : Outcome availability, selection and censoring
> ==An untransferred embryo has an unobserved implantation or live-birth outcome under the current treatment history. The iDAScore development study evaluates transferred embryos and an expanded population in which discarded embryos receive proxy-negative labels. The first analysis uses observed transfer outcomes; the second adds clinical deselection to the target construction [@OUTCOME03].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Embryo fetal-heartbeat scoring (iDAScore v1.0) |  |
| **Inputs** | Time-lapse image sequences |  |
| **Prediction time** | Sequence spans 12-140 h post-insemination; variable endpoint at 108-140 h |  |
| **Analysis unit** | embryo |  |
| **Method** | I3D convolutional video encoder plus bidirectional LSTM; auxiliary discard head |  |
| **Supervision / labels** | Observed fetal heartbeat; discarded embryos pseudo-labelled negative |  |
| **Outcome** | Fetal heartbeat; distinguish KID-only from KID-plus-discard evaluation |  |
| **Sample sizes** | [{"value": 115832, "unit": "development/evaluation embryos", "locator": "Methods / Description of data; PLOS lines199-200"}, {"value": 14644, "unit": "transferred KID embryos", "locator": "same section"}, {"value": 17249, "unit": "test embryos", "locator": "Results / Final model"}, {"value": 2212, "unit": "test KID embryos", "locator": "Results / Final model"}] |  |
| **Splitting** | 85/15 random individual-embryo split across treatments and clinics; training cross-validation for hyperparameters. |  |
| **Validation** | Internal held-out embryos; leave-one-clinic-out retraining, not a single locked-model external test. |  |

## Source-linked excerpts
- [OUTCOME03-B0017] ==The 115,832-embryo dataset was randomly split by embryo despite a mean of 5.7 embryos per cycle, so patient/cycle separation was not ensured for the main test.==
- [OUTCOME03-B0024] ==A stronger leave-one-clinic-out analysis trained 12 models and evaluated clinics with more than 250 transferred embryos.==
- [OUTCOME03-B0032] ==AUC was 0.67 for transferred embryos with known outcomes but 0.95 for all embryos after adding manually discarded embryos as pseudo-negatives.==
- [OUTCOME03-B0055] ==Clinical selection mechanisms were heterogeneous and incompletely recorded, Vitrolife funded data collection and employed several authors.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*