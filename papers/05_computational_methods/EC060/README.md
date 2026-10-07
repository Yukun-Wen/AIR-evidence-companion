# EC060 — Machine learning-based preliminary screening tool for clinical pregnancy prediction: towards management of IVF/ICSI stages.

**Huang, Tuerganbayi, Wang et al. (2025).** *Annals of medicine*. DOI: [10.1080/07853890.2025.2582245](https://doi.org/10.1080/07853890.2025.2582245)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==Table entry; table caption: Selected tabular prediction designs and evaluation conditions. — Baseline and treatment-phase clinical-pregnancy classifiers [@EC060]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy with separate pretreatment and pre-transfer models. | EC060-B0012 EC060-B0013 EC060-B0014 |
| **Inputs** | Baseline demographics/endocrine/AFC inputs; treatment model additionally uses dosage, trigger-day measurements and embryo status. | EC060-B0013 EC060-B0014 |
| **Prediction time** | Initial consultation for baseline model; before embryo transfer for treatment model. | EC060-B0013 EC060-B0014 |
| **Analysis unit** | Woman with last recorded IVF/ICSI cycle selected when multiple cycles existed. | EC060-B0006 |
| **Method** | Univariate/lasso/multivariate selection; logistic regression, XGBoost, RF, SVM, naive Bayes and LightGBM with randomized search. | EC060-B0011 EC060-B0012 |
| **Supervision / labels** | Binary clinical pregnancy from positive pregnancy test and subsequent intrauterine gestational sac. | EC060-B0009 |
| **Outcome** | Clinical pregnancy after IVF/ICSI. | EC060-B0009 |
| **Sample sizes** | {"screened_development": 1989, "development_patients": 1062, "training": 743, "internal_validation": 319, "temporal_validation": 250, "temporal_pregnancies": 145} | EC060-B0019 EC060-B0021 |
| **Splitting** | Random 70/30 development split with ten-fold training tuning; independent later same-hospital 2022 cohort. | EC060-B0010 EC060-B0012 EC060-B0015 |
| **Validation** | Internal and temporal AUROC/AUPRC, sensitivity, specificity, F1, calibration/Brier and decision curves. | EC060-B0015 |

## Source-linked excerpts
- [EC060-B0006] ==The retrospective cohort selected the last cycle per woman and excluded cancelled, no-oocyte, failed-fertilization, and frozen-transfer cases.==
- [EC060-B0009] ==Clinical pregnancy was defined by a positive pregnancy test followed by an intrauterine gestational sac on ultrasound.==
- [EC060-B0012] ==Six algorithms were trained, with randomized hyperparameter search and ten-fold cross-validation.==
- [EC060-B0027] ==The temporal cohort table reports modest AUROCs and shows naive Bayes above XGBoost in AUROC for both model stages.==
- [EC060-B0040] ==The authors note missing male and lifestyle factors, retrospective selection bias, single-center data, fresh-transfer restriction, and limited overall performance.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*