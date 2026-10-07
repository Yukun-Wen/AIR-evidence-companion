# EC052 — Predicting the number of oocytes retrieved from controlled ovarian hyperstimulation with machine learning.

**Ferrand, Boulant, He et al. (2023).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/dead163](https://doi.org/10.1093/humrep/dead163)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==A single-centre LightGBM study predicts total oocytes from pretreatment variables, starting dose and protocol, and separately regresses clinician-defined ordinal bins. Eligibility requires reaching trigger. Predictions compress both tails despite modest average-error improvement over a linear comparator. Dataset-wide comparator imputation and unspecified patient grouping complicate attribution of that improvement [@EC052].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict retrieved oocyte count, directly and as clinician-defined ordinal bins. | EC052-B0011 EC052-B0013 |
| **Inputs** | 16 pre-stimulation features selected by availability, correlation and clinical input. | EC052-B0012 |
| **Prediction time** | Before start of stimulation. | EC052-B0012 |
| **Analysis unit** | Autologous stimulation cycle; individual patient count not stated in examined methods. | EC052-B0007 EC052-B0013 |
| **Method** | LightGBM with Poisson objective for counts and Huber loss for ordinal bins; linear/logistic baselines; SHAP. | EC052-B0014 EC052-B0016 |
| **Supervision / labels** | Observed oocyte counts or clinician-defined bins supervise regression. | EC052-B0013 |
| **Outcome** | Oocytes retrieved after stimulation; two alternative binning schemes. | EC052-B0013 |
| **Sample sizes** | {"cycles": 11286, "patients": "not_reported_in_examined_source", "centers": 1} | EC052-B0007 |
| **Splitting** | 80% records training with random-search five-fold CV, remaining 20% holdout; patient grouping not specified. | EC052-B0014 EC052-B0015 |
| **Validation** | Internal MAE/MAPE, error distributions and baseline comparisons; SHAP on 1000 sampled patients. | EC052-B0015 EC052-B0016 |

## Source-linked excerpts
- [EC052-B0007] ==The retrospective cohort contained 11,286 uninterrupted autologous cycles at one French center, all ending in a trigger.==
- [EC052-B0012] ==Sixteen selected features were all collected before stimulation began.==
- [EC052-B0014] ==LightGBM directly handled missing fields; models used an 80% training set, randomized-search fivefold tuning, Poisson loss for counts, and Huber loss for clinician-defined bins.==
- [EC052-B0021] ==Held-out test MAE was 4.21 oocytes for LightGBM versus 4.36 for linear regression; binned-model gains over logistic regression were also small.==
- [EC052-B0024] ==The model underpredicted zero-oocyte and high-yield tails; 15+ oocyte cycles were 22% of observed outcomes but 11% of LightGBM predictions.==
- [EC052-B0037] ==The authors caution that the single-clinic cohort is not representative and call for multicenter and prospective clinician comparison before clinical use.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*