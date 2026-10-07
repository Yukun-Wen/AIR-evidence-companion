# EE052 — Application of machine learning to predict aneuploidy and mosaicism in embryos from in vitro fertilization cycles.

**Ortiz, Morales, Lledo et al. (2022).** *AJOG global reports*. DOI: [10.1016/j.xagr.2022.100103](https://doi.org/10.1016/j.xagr.2022.100103)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Genetic classification and assay-defined populations
> ==A multiclass model of aneuploidy and mosaicism includes testing technique among the predictors of mosaicism, making assay practice part of the learned classification. Its confusion matrices and adjacent accuracy summaries disagree. This example links assay-specific predictors to two levels of interpretation: the genetic class being learned and the contingency table used to measure agreement with it [@EE052].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict multiclass embryo aneuploidy patterns and mosaicism patterns. | EE052-B0035 |
| **Inputs** | 29 candidate general, parental, couple, IVF and embryo variables, including biopsy day/quality and PGT technology. | EE052-B0033 EE052-B0034 |
| **Prediction time** | At blastocyst biopsy/day-5–7 information availability; exact frozen predictor set before PGT result requires confirmation from supplement. | EE052-B0025 EE052-B0034 |
| **Analysis unit** | Embryo nested within IVF cycle/couple. | EE052-B0021 |
| **Method** | Sixteen supervised classifiers compared; final random forest with tuning, class balancing and OOB evaluation. | EE052-B0037 EE052-B0040 |
| **Supervision / labels** | aCGH/NGS PGT-A; <25% abnormal cell line euploid, 25–50% mosaic, >50% aneuploid. | EE052-B0027 EE052-B0028 EE052-B0029 |
| **Outcome** | Four aneuploidy classes and four mosaicism classes (none, whole, segmental, both). | EE052-B0035 |
| **Sample sizes** | {"embryos": 6989, "IVF_cycles": 2476, "aCGH_embryos": 2335, "NGS_embryos": 4654, "unique_patients": "not_reported_in_examined_source"} | EE052-B0021 EE052-B0027 |
| **Splitting** | Random 80/20 data-frame split with five-fold selection; final full-database RF ten-fold tuning and OOB error. Patient/cycle grouping not described. | EE052-B0038 EE052-B0040 |
| **Validation** | Internal log loss/accuracy/AUC/sensitivity/specificity with micro/macro ROC; no independent external test described. | EE052-B0038 EE052-B0041 |

## Source-linked excerpts
- [EE052-B0021] ==The observational retrospective cohort included 6989 embryos from 2476 PGT-A cycles collected over 2013-2020.==
- [EE052-B0037] ==Sixteen supervised classification algorithms spanning regression, neural networks, support-vector, tree, ensemble, Bayesian, and discriminant methods were compared.==
- [EE052-B0058] ==The final Random Forest models had AUCs of 0.792 and 0.776, while mean sensitivity and accuracy remained approximately 0.54-0.56.==
- [EE052-B0064] ==PGT-A diagnostic technique was the most important mosaicism predictor, followed by embryo quality and biopsy day, whereas maternal age was less dominant than for aneuploidy.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*