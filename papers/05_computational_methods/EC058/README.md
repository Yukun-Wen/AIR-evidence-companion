# EC058 — Machine learning prediction of live birth after IVF using the morphological uterus sonographic assessment group features of adenomyosis.

**Alson, Bjornsson, Henic et al. (2026).** *Scientific reports*. DOI: [10.1038/s41598-025-31013-1](https://doi.org/10.1038/s41598-025-31013-1)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC058.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Uterine imaging provides complementary fusion designs. An endometrial study clusters ultrasound regions into habitats, derives radiomic features and combines them with clinical variables for clinical-pregnancy prediction. This structure introduces imaging information and regional organization as two components. Comparisons with clinical-only and whole-region models can separate their contributions. A prospective first-IVF/ICSI cohort uses expert MUSA ultrasound features in a pretreatment cumulative-live-birth model; adding embryo stage and frozen-transfer information post hoc yields a later-information predictor [@EC057,EC058].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth after first IVF/ICSI treatment using adenomyosis ultrasound features. | EC058-B0021 |
| **Inputs** | Age, BMI, AMH, AFC, MUSA uterine features, endometriosis findings and symptom variables. | EC058-B0012 EC058-B0013 |
| **Prediction time** | Baseline before ART for main model; exploratory embryo-stage/FET analyses use later information. | EC058-B0008 |
| **Analysis unit** | Woman/index IVF treatment including fresh and frozen transfers until birth or embryos exhausted. | EC058-B0007 EC058-B0010 |
| **Method** | Optuna-tuned XGBoost with five-fold ensemble; post-hoc bagged decision tree comparison. | EC058-B0015 EC058-B0016 EC058-B0021 |
| **Supervision / labels** | Recorded live birth of living child after >22 gestational weeks. | EC058-B0010 |
| **Outcome** | Live birth from index treatment and its available embryos; not solely first-transfer live birth. | EC058-B0010 EC058-B0021 |
| **Sample sizes** | {"women": 1037, "centers": 1} | EC058-B0007 |
| **Splitting** | Stratified random 80/20 train/test and stratified five-fold CV within training. | EC058-B0014 EC058-B0015 |
| **Validation** | Internal AUROC and accuracy; Youden threshold from CV evaluation; SHAP interpretations. | EC058-B0019 EC058-B0020 |

## Source-linked excerpts
- [EC058-B0007] ==The prospective cohort enrolled 1,037 women aged 25 to 39 undergoing their first IVF/ICSI treatment at one Swedish center.==
- [EC058-B0014] ==A stratified random 80/20 train-test split was used for internal validation.==
- [EC058-B0028] ==The primary XGBoost model achieved test accuracy 0.59 and AUC 0.66.==
- [EC058-B0045] ==The primary prediction time was before treatment; adding embryo stage and frozen transfer post hoc increased AUC to 0.75 and changed the dominant predictors.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*