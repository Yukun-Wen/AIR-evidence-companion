# EE035 — A novel machine-learning framework based on early embryo morphokinetics identifies a feature signature associated with blastocyst development.

**Canosa, Licheri, Bergandi et al. (2024).** *Journal of ovarian research*. DOI: [10.1186/s13048-024-01376-6](https://doi.org/10.1186/s13048-024-01376-6)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE035.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Temporal constraints impose consistency on predicted stages. An earlier pipeline combines handcrafted and bag-of-features descriptors, local-temporal AdaBoost and Viterbi refinement. Overall frame accuracy improves, while three-cell accuracy remains 20.86%. Short-stage annotation therefore becomes a specific target for improving division-timing estimation [@EE083]. Rule extraction produces a compact description of developmental timing. One study combines manually annotated early timings with clinical variables in a six-rule signature for day-five expansion. Its small same-center validation evaluates development in selected cycles already producing a fresh day-five transfer [@EE035].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict day5 expanded-blastocyst development and extract interpretable early-embryo rules. | EE035-B0013 |
| **Inputs** | 30 candidate woman-,stimulation- and embryo-related variables including early morphokinetics; IVF lacks tPNa-related measures. | EE035-B0012 |
| **Prediction time** | After early cleavage annotation up to t8; timing inferred from last required predictor. | EE035-B0011 EE035-B0012 |
| **Analysis unit** | Embryo nested in first included cycle/woman. | EE035-B0005 |
| **Method** | EmbryoMLSelection selects12variables,extracts71rules,reduces to23using MCC,and chooses six rules by classifier AUROC; comparisons include SVM,kNN,LR,naive Bayes,RF and boosting. | EE035-B0013 EE035-B0014 EE035-B0022 EE035-B0024 |
| **Supervision / labels** | Senior embryologist assigns day5 expansion group at116±2hpi; manually annotates timing. | EE035-B0011 |
| **Outcome** | Expanded blastocyst by day5 regardless of ICM/TE grade. | EE035-B0011 |
| **Sample sizes** | {"development_embryos": 575, "development_women_cycles": 80, "expanded": 210, "not_expanded": 365, "internal_training_embryos": 403, "internal_test_embryos": 172, "validation_embryos": 81, "validation_patients": 10} | EE035-B0005 EE035-B0006 EE035-B0011 EE035-B0022 |
| **Splitting** | Development575embryos split70/30 (403/172); source describes stratified10-fold CV repeated100times against the test set. Patient grouping for this internal split is unspecified. Independent81embryos from10other patients validate selected rules. | EE035-B0022 EE035-B0025 |
| **Validation** | Internal best AdaBoost six-rule AUROC0.842; independent same-center six-rule validation reports AUROC0.842/accuracy0.81 without naming the corresponding classifier in that paragraph. | EE035-B0024 EE035-B0025 |

## Source-linked excerpts
- [EE035-B0005] ==The training cohort comprised 575 embryos from 80 selected cycles with fresh day-5 single-blastocyst transfer and normal-response characteristics.==
- [EE035-B0012] ==Thirty woman-, stimulation-, and embryo-related variables were recorded for each embryo.==
- [EE035-B0024] ==Six rules involving eight variables produced the highest internal discrimination, with AUC 0.842.==
- [EE035-B0025] ==In 81 embryos from 10 additional patients, the signature reportedly achieved AUC 0.842 and accuracy 0.81.==
- [EE035-B0034] ==The authors acknowledge restricted patients, limited sample size, manual timing annotation, and use of expansion rather than ICM/TE, ploidy, or implantation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*