# EC057 — Machine learning-based endometrial ultrasound radiomics habitat analysis for predicting pregnancy outcomes after embryo transfer.

**Xie, Geng, Chen et al. (2026).** *Journal of ovarian research*. DOI: [10.1186/s13048-026-02039-4](https://doi.org/10.1186/s13048-026-02039-4)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Uterine imaging provides complementary fusion designs. An endometrial study clusters ultrasound regions into habitats, derives radiomic features and combines them with clinical variables for clinical-pregnancy prediction. This structure introduces imaging information and regional organization as two components. Comparisons with clinical-only and whole-region models can separate their contributions. A prospective first-IVF/ICSI cohort uses expert MUSA ultrasound features in a pretreatment cumulative-live-birth model; adding embryo stage and frozen-transfer information post hoc yields a later-information predictor [@EC057,EC058].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy after fresh or frozen embryo transfer using endometrial habitats. | EC057-B0007 |
| **Inputs** | Mid-sagittal transvaginal ultrasound radiomics and clinical variables including embryo stage/type; four k-means habitat regions. | EC057-B0014 EC057-B0015 EC057-B0017 |
| **Prediction time** | Ultrasound on hCG or endometrial-transformation day; transfer-related predictors require embryo type to be known. Combined prediction is pre-transfer only once these inputs are available. | EC057-B0014 EC057-B0015 |
| **Analysis unit** | Patient/embryo-transfer episode, not individual embryo. | EC057-B0009 |
| **Method** | K-means habitats; univariate, correlation and mRMR feature selection; 11 ML classifiers with grid search and SHAP. | EC057-B0017 EC057-B0018 |
| **Supervision / labels** | Clinical pregnancy labelled by gestational sac on ultrasound four weeks after transfer. | EC057-B0013 |
| **Outcome** | Clinical pregnancy, not ongoing pregnancy/live birth. | EC057-B0013 |
| **Sample sizes** | {"screened": 800, "patients": 543, "train": 380, "test": 163, "pregnant": 294, "nonpregnant": 249, "fresh_transfers": 105, "frozen_transfers": 438} | EC057-B0009 EC057-B0020 |
| **Splitting** | Random patient 70/30 split; stratified five-fold tuning on training set. Scope of feature-selection fitting is not explicitly confined to training in examined description. | EC057-B0009 EC057-B0018 |
| **Validation** | Internal held-out AUROC, accuracy, sensitivity, specificity, PPV, NPV and F1; no external validation. | EC057-B0018 EC057-B0035 |

## Source-linked excerpts
- [EC057-B0009] ==Of 800 screened transfer patients, 543 were eligible and randomly allocated 380 to training and 163 to testing.==
- [EC057-B0017] ==Four endometrial habitat subregions were derived and whole/subregion radiomics underwent statistical, correlation and mRMR feature selection.==
- [EC057-B0025] ==ExtraTrees had the leading test AUC of 0.766, ahead of logistic regression and random forest.==
- [EC057-B0035] ==The authors acknowledge single-center data, two devices, no external validation and limited sample size.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*