# EQF02 — Trial emulation for validating the clinical efficacy of a foundational AI model in embryo selection

**Rajendran, Malmsten, Arnal et al. (2026).** *npj Digital Medicine*. DOI: [10.1038/s41746-026-02672-9](https://doi.org/10.1038/s41746-026-02672-9)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2026: decision-oriented evaluation [@EQF02,EA003]==

> **§ Quantitative evidence and supported decision claims** : Broad systems and the meaning of state of the art
> ==The FEMI follow-up compares the association between embryo scores and implantation-related outcomes through retrospective trial emulation [@EQF02]. Its high- versus low-score exposure is distinct from assigning patients to competing embryo-selection strategies. The study extends external score assessment; a prospective policy comparison addresses the patient benefit of using the model. Across the full IVF pathway, a system would also need to address stimulation, gamete handling, transfer and cumulative outcomes. The reviewed systems establish task-specific or embryology-wide capabilities within that broader problem.==

> **§ Quantitative evidence and supported decision claims** : Broad systems and the meaning of state of the art
> ==Table entry; table caption: Representative leading systems: breadth and evidence answer different questions. — FEMI, 2025; follow-up 2026 [@EQF01,EQF02]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Evaluate frozen FEMI score associations with implantation across two independent cohorts. | EQF02-P002 EQF02-P006 EQF02-P007 |
| **Inputs** | Blastocyst images and maternal age; matching and adjustment use clinical covariates. | EQF02-P002 EQF02-P006 EQF02-P007 |
| **Prediction time** | Pre-transfer embryo assessment. | EQF02-P004 EQF02-P006 |
| **Analysis unit** | Transferred embryo nested in patient and center. | EQF02-P007 |
| **Method** | Frozen FEMI with propensity matching, adjusted regressions and grouped S-learner analyses. | EQF02-P007 |
| **Supervision / labels** | Observed EMR implantation-related labels; no model retraining. | EQF02-P002 EQF02-P006 EQF02-P007 |
| **Outcome** | Composite positive gestation, gestational sac or live-birth records versus not pregnant. | EQF02-P006 |
| **Sample sizes** | {"total_embryos_derived": 4674, "WCM_embryos": 2666, "WCM_patients": 1671, "IVI_embryos": 2008, "IVI_patients": 1755, "WCM_implanted": 1797, "IVI_implanted": 1087} | EQF02-P002 |
| **Splitting** | Two cohorts stated independent of original model training; patient-grouped five-fold S-learner and clustered bootstrap. | EQF02-P002 EQF02-P006 EQF02-P007 |
| **Validation** | Independent-cohort associations, matching, calibration and score contrasts; these do not establish benefit of an assigned selection policy. | EQF02-P004 EQF02-P007 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*