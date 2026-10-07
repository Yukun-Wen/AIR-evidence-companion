# EE029 — Beyond black-box models: explainable AI for embryo ploidy prediction and patient-centric consultation.

**Luong, Ho, Hwu et al. (2024).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-024-03178-7](https://doi.org/10.1007/s10815-024-03178-7)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Cross-cutting attributes: explanation and distributed development
> ==Explanation and distributed training describe how a model is inspected and developed. SHAP assigns additive contributions under specified properties and missing-feature assumptions, with interpretation affected by correlated inputs. LIME fits a local proximity-weighted surrogate; Grad-CAM uses target-score gradients to weight feature maps for coarse localization. Together they expose feature contributions, local decision behavior and spatial sensitivity of the fitted predictor [@EM039,EM040,EM041]. An IVF ploidy classifier applies SHAP and LIME to random-forest predictions, combining global attribution with local consultation explanations. An earlier-year holdout evaluates temporal discrimination at the same center. The design pairs predictive testing with two views of the variables driving the fitted model [@EE029].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict blastocyst ploidy using interpretable tabular embryo and parental data. | EE029-H0145 EE029-H0159 |
| **Inputs** | Morphokinetic features, numeric Gardner/NEQsi morphology on day 5 and biopsy day, and 11 clinical variables. | EE029-H0130 EE029-H0157 EE029-H0159 |
| **Prediction time** | After day-5/biopsy-day morphology and morphokinetic events are available; before PGT-A result intended, timing inferred from variables. | EE029-H0157 |
| **Analysis unit** | Embryo nested in cycle and couple. | EE029-H0145 EE029-H0183 |
| **Method** | RF, LDA, logistic regression, SVM, AdaBoost and LightGBM; selected RF with SHAP and LIME. | EE029-H0179 EE029-H0180 |
| **Supervision / labels** | PGT-A euploid/aneuploid status; mosaics and insufficient DNA excluded. | EE029-H0146 EE029-H0159 |
| **Outcome** | Binary ploidy for high-, low- and all-grade blastocysts. | EE029-H0159 |
| **Sample sizes** | {"screened_embryos": 3448, "screened_patients": 820, "eligible_embryos": 1908, "eligible_couples_reported": 584, "eligible_cycles_reported": 699, "development_embryos_2021_2022": 1471, "earlier_temporal_test_2020": 437, "high_grade_development": 1107, "low_grade_development": 364} | EE029-H0145 EE029-H0146 EE029-H0183 |
| **Splitting** | 2021–2022 development with separate 80/20 embryo splits per grade group; five-fold RF grid search; 2020 same-center temporal test labelled external by authors. | EE029-H0146 EE029-H0179 EE029-H0238 |
| **Validation** | Internal and earlier-year same-center AUROC/accuracy with selected threshold; no geographically external center cohort. | EE029-H0238 EE029-H0239 |

## Source-linked excerpts
- [EE029-H0145] ==The retrospective cohort contained 3448 embryos from 820 patients at one Taipei center before eligibility filtering.==
- [EE029-H0146] ==After exclusions, 1908 embryos remained; 437 embryos from 2020 were held out and 1471 embryos from 2021-2022 were used for training.==
- [EE029-H0239] ==The final random forest achieved AUC 0.808 internally and AUC 0.750 on the held-out temporal cohort.==
- [EE029-H0259] ==The authors acknowledge euploid/aneuploid class imbalance and its potential effect on training.==
- [EE029-H0261] ==Mosaic embryos were excluded because laboratory reporting and labeling were not sufficiently standardized.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*