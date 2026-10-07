# EC070 — Clinical data-based modeling of IVF live birth outcome and its application.

**Liu, Liang, Yang et al. (2024).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-024-01253-3](https://doi.org/10.1186/s12958-024-01253-3)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==ANN/SVM live-birth models simulate transfer strategies through predictions conditional on historical treatment choices [@EC070]. A large historical ART analysis evaluates full-cycle and pre-cycle models using predominantly IVF and some donor-insemination records. Its narrative and model tables disagree on the processed denominator; repeated attempts also require patient-level accounting. Age associations are conditioned by the treatment-selection process represented in these records [@EC088].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth and compare candidate embryo-transfer strategies. | EC070-B0009 EC070-B0010 |
| **Inputs** | Age, ovarian sensitivity index, COS regimen, starting gonadotropin dose, trigger-day endometrium/progesterone and transfer strategy. | EC070-B0025 |
| **Prediction time** | Transfer planning after stimulation/retrieval; timing inferred from the selected variables. | EC070-B0007 EC070-B0025 |
| **Analysis unit** | Woman/fresh IVF cycle, with one or two embryos transferred. | EC070-B0005 EC070-B0006 |
| **Method** | ANN and Gaussian-kernel SVM; SVM selected after hyperparameter tuning. | EC070-B0010 EC070-B0011 EC070-B0012 |
| **Supervision / labels** | Supervised observed live-birth labels. | EC070-B0006 EC070-B0009 |
| **Outcome** | Live delivery at 28 weeks with infant survival for at least one month. | EC070-B0006 |
| **Sample sizes** | {"development_women": 1405, "SVM_training": 1124, "SVM_test": 281, "application_cohort_reported_results": 82, "application_cohort_flow_description": 81} | EC070-B0005 EC070-B0009 EC070-B0031 EC070-B0038 |
| **Splitting** | ANN70/17/13 split selected after testing many ratios; SVM80/20 split uses a different test set. | EC070-B0011 EC070-B0012 EC070-B0031 |
| **Validation** | Internal holdout plus small new application cohort; classification metrics and observational strategy comparisons. | EC070-B0034 EC070-B0038 EC070-B0055 |

## Source-linked excerpts
- [EC070-B0005] ==The model-development cohort comprised 1405 women undergoing IVF/ICSI at one reproductive centre.==
- [EC070-B0011] ==ANN data were split 70/17/13, and the authors selected the split after trying dozens of percentage combinations.==
- [EC070-B0031] ==The SVM used 1124 training and 281 test cases and achieved test AUC 0.854.==
- [EC070-B0038] ==In 82 later clinical cases, the model reported AUC 0.862, precision 90.57%, sensitivity 75.00%, and accuracy 74.39%.==
- [EC070-B0055] ==The discussion acknowledges that historical two-embryo-transfer preferences bias the learned recommendations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*