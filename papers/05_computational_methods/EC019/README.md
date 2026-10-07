# EC019 — A Machine Learning Approach for the Prediction of Testicular Sperm Extraction in Nonobstructive Azoospermia: Algorithm Development and Validation Study.

**Bachelot, Dhombres, Sermondade et al. (2023).** *Journal of medical Internet research*. DOI: [10.2196/44047](https://doi.org/10.2196/44047)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Semen-derived vectors support both fertilization assessment and pregnancy prognosis. Yi compares machine-learning and logistic models using same-day semen characteristics in short-term IVF and rescue-ICSI pathways, with machine-learning partitioning incompletely specified. Mehrjerd combines routine semen variables in ensembles for pregnancy across IVF and ICSI. Metric choice changes the latter comparison: random forest has the higher AUC, while bagging has the higher accuracy. A defined threshold and treatment pathway connect these probabilities to prospective triage or sperm-selection decisions [@EC003,EC004]. A gradient-boosted model combines intracellular pH, membrane potential and clinical variables to predict conventional-IVF fertilization from leftover sperm incubated overnight. A separate model predicts sufficient sperm for ICSI in men with NOA, testing 26 later patients at the same centre [@EC012,EC019].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict whether TESE retrieves sufficient sperm for ICSI in nonobstructive azoospermia. | EC019-B0014 |
| **Inputs** | 16 preoperative variables: age, BMI, smoking, five hormones, karyotype, Y microdeletion and six urogenital-history variables. | EC019-B0013 |
| **Prediction time** | Preoperative TESE assessment. | EC019-B0013 |
| **Analysis unit** | Individual male patient undergoing conventional or micro-TESE. | EC019-B0009 |
| **Method** | LR, naive Bayes, kNN, SVM, RF, gradient-boosted trees, XGBoost and ANN; missing-value handling and random-search tuning. | EC019-B0016 |
| **Supervision / labels** | Binary surgical-specimen examination label; positive requires enough sperm for ICSI. | EC019-B0014 |
| **Outcome** | Sufficient sperm retrieval, not pregnancy or live birth. | EC019-B0014 |
| **Sample sizes** | {"patients": 201, "retrospective_development": 175, "development_positive": 104, "development_negative": 71, "prospective_temporal_test": 26, "test_positive": 13, "test_negative": 13} | EC019-B0021 EC019-B0023 |
| **Splitting** | Same-center temporal split; development repeated 5-fold CV (10 iterations); 26 later prospectively collected patients used as test cohort. | EC019-B0017 EC019-B0023 |
| **Validation** | Sensitivity, specificity, accuracy and AUROC at 0.5 threshold; temporal validation at same institution, not independent-center validation. | EC019-B0018 EC019-B0025 |

## Source-linked excerpts
- [EC019-B0009] ==The study included 201 NOA patients undergoing conventional TESE or micro-TESE at one hospital.==
- [EC019-B0014] ==A positive target required enough spermatozoa from the surgical specimen for ICSI.==
- [EC019-B0025] ==The same-center temporal test table reports random-forest AUC 0.90, accuracy 84.6%, sensitivity 100% and specificity 69.2%.==
- [EC019-B0034] ==The authors flag monocentric design, mixed surgical procedures and operator/site-dependent target variability.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*