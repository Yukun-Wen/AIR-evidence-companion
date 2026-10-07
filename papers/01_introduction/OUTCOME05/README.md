# OUTCOME05 — Deep learning versus manual morphology-based embryo selection in IVF: a randomized, double-blind noninferiority trial

**Illingworth, Venetis, Gardner et al. (2024).** *Nature medicine*. DOI: [10.1038/s41591-024-03166-5](https://doi.org/10.1038/s41591-024-03166-5)

**Role:** core · contrasts C18, C19 · workflow: Embryo assessment and selection

**Cited in:** Introduction, Computational foundations of the IVF workflow, Learning objectives and the interpretation of model outputs

**PDF:** see OUTCOME05.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Introduction**
> ==In the figure caption: Organization and quantitative motivation of the survey. (a) The corpus comprises 247 cited works: 125 core empirical reports and 122 contextual sources. (b) Tabular, spatial, temporal and multimodal or hierarchical observations motivate the method families, followed by learning objectives and conditional evidence synthesis. Arrows show the reading route. (c) The same embryo model has AUC 0.67 among 2,212 transferred embryos with known fetal-heartbeat outcomes and 0.95 in the nested 17,249-embryo test set including discarded embryos assigned negative labels OUTCOME03 — Organization and quantitative motivation of the survey. (a) The corpus comprises 247 cited works: 125 core empirical reports and 122 contextual sources. (b) Tabular, spatial, temporal and multimodal or hierarchical observations motivate the method families, followed by learning objectives and conditional evidence synthesis. Arrows show the reading route. (c) The same embryo model has AUC 0.67 among 2,212 transferred embryos with known fetal-heartbeat outcomes and 0.95 in the nested 17,249-embryo test set including discarded embryos assigned negative labels OUTCOME03==

> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Treatment outcomes connect embryo-level scores to patient-level prospects through transfer policy, the number and order of available embryos, and follow-up across transfers. Embryo-scoring studies evaluate outcome association, while a randomized comparison of AI-guided and morphology-guided selection evaluates use of the score within a clinical policy. The unit of prediction and the intervention design determine which part of this connection is measured [@OUTCOME03,OUTCOME04,OUTCOME05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2024: multimodal systems and randomized selection [@EMBRYO06,OUTCOME05]==

> **§ Learning objectives and the interpretation of model outputs**
> ==Representations encode observations; targets define predictions; losses guide fitting; evaluation criteria measure performance. One encoder can support masks, grades, PGT-A classes or probabilities, each with its own reference and population. The objective axis records the learning problem and loss, while intended use records the decision. This section follows measurement, forecasting, ranking and policy evaluation [@EMBRYO03,EMBRYO02,EMBRYO05,OUTCOME05].==

> **§ Learning objectives and the interpretation of model outputs** : Policy objectives and clinical utility
> ==The randomized iDAScore study compares AI-guided with standardized morphology-based selection for the first transfer, using clinical pregnancy as the primary endpoint. The trial did not establish noninferiority. It directly evaluates a selection policy in the enrolled participants and equipment setting. Grading assistance, counseling and cumulative ordering involve different actions and therefore define separate policy objectives [@OUTCOME05].==

> **§ Learning objectives and the interpretation of model outputs** : Matching objectives to admissible comparisons
> ==12 Table answers which metrics to report and at which unit. A useful evaluation combines task performance with uncertainty, calibration where a probability is used, and the consequence of the intended decision. For a benchmark with several metrics, the primary metric supplies an explicit ordering; the remaining metrics show trade-offs. A model is Pareto-dominated only when another is at least as good on every shared metric and strictly better on one, under the same evaluation conditions. This relation preserves competing strengths without assigning arbitrary weights to unlike outcomes.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Clinical effectiveness of AI-guided embryo selection versus morphology |  |
| **Inputs** | Time-lapse images for iDAScore; Gardner assessment comparator |  |
| **Prediction time** | Day-five selection before first fresh/frozen transfer |  |
| **Analysis unit** | randomized woman; first embryo transfer |  |
| **Method** | Multicenter double-blind randomized noninferiority trial of fixed iDAScore |  |
| **Supervision / labels** | No model training in this study |  |
| **Outcome** | Primary clinical pregnancy with heartbeat at 7-9 weeks; secondary live birth |  |
| **Sample sizes** | [{"value": 1066, "unit": "randomized patients", "locator": "Abstract; Results / Table 1"}, {"value": 533, "unit": "patients per randomized arm", "locator": "Abstract"}] |  |
| **Splitting** | 1:1 patient randomization; efficacy analyses intention-to-treat and per protocol. |  |
| **Validation** | Prospective clinical utility trial at 14 clinics. |  |

## Source-linked excerpts
- [OUTCOME05-B0033] ==This was a 14-clinic randomized, double-blind, noninferiority trial with independent safety monitoring and a prespecified 5-percentage-point margin.==
- [OUTCOME05-B0009] ==Clinical pregnancy was 46.5% with iDAScore versus 48.2% with morphology, the confidence interval crossed the noninferiority margin, so noninferiority was not demonstrated.==
- [OUTCOME05-B0010] ==Live birth was 39.8% versus 43.5% and the confidence interval included benefit and clinically relevant harm, scoring time was about tenfold shorter in a small substudy.==
- [OUTCOME05-B0027] ==The fresh-versus-freeze-all interaction and lower frozen-cycle result require caution and may reflect chance, cumulative live birth was not assessed.==
- [OUTCOME05-B0046] ==Vitrolife funded the trial, participated in design and writing, and employed shareholding inventors, data collection and analysis were performed independently.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*