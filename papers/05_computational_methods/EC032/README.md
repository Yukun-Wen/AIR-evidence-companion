# EC032 — Integrated Prediction System for Individualized Ovarian Stimulation and Ovarian Hyperstimulation Syndrome Prevention: Algorithm Development and Validation.

**Chen, Zhao, Qiu et al. (2026).** *Journal of medical Internet research*. DOI: [10.2196/78245](https://doi.org/10.2196/78245)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==The target's mathematical structure determines the learning objective. Binary response classes, oocyte counts and dose-normalized transformations use different losses and scales. An externally evaluated XGBoost framework separates baseline response-risk models from models encoding a planned stimulation regimen; enumerated regimens yield conditional predictions for the observed treatment setting. Another two-center study predicts the logarithm of retrieved-oocyte count divided by starting FSH dose alongside early OHSS risk. Its regression errors are on that transformed scale, and discrepancies among its threshold metrics remain unresolved. These examples connect target transformation and predictor timing to performance interpretation [@EC031,EC032,R041,R042].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict retrieved-oocyte yield and early moderate-to-severe OHSS across starting FSH doses. | EC032-B0013 EC032-B0014 |
| **Inputs** | Baseline hormones, anthropometrics, biochemical measures, AFC, protocol and starting FSH; Boruta selects 17 yield and 19 OHSS predictors. | EC032-B0009 EC032-B0011 EC032-B0012 |
| **Prediction time** | Before stimulation when baseline characteristics, protocol and starting FSH dose are specified. | EC032-B0016 |
| **Analysis unit** | Patient first ovarian-stimulation cycle. | EC032-B0007 EC032-B0008 |
| **Method** | Eleven regression and eleven classification algorithms, five-fold tuning, cost-sensitive OHSS learning; selected gradient boosting regression and LightGBM classification with SHAP. | EC032-B0013 EC032-B0014 EC032-B0022 EC032-B0025 |
| **Supervision / labels** | Recorded oocyte count transformed as log(count/starting FSH); guideline-diagnosed OHSS within nine days after trigger. | EC032-B0010 EC032-B0013 |
| **Outcome** | Retrieved-oocyte yield and early moderate-to-severe OHSS; simulated dose-response curves are prediction outputs. | EC032-B0010 EC032-B0013 |
| **Sample sizes** | {"internal_patients": 6401, "external_patients": 3805, "internal_training": 5120, "internal_test": 1281, "OHSS_internal": 55, "OHSS_external": 46} | EC032-B0008 EC032-B0013 EC032-B0020 |
| **Splitting** | Random 80/20 internal patient split; training-only five-fold tuning, imputation and feature selection; separate center held out for external validation. | EC032-B0013 EC032-B0014 |
| **Validation** | Internal and external regression R²/MAE/RMSE and OHSS AUROC, PR-AUC, recall, specificity, F1, kappa and predictive values. | EC032-B0013 EC032-B0014 |

## Source-linked excerpts
- [EC032-B0007 to EC032-B0010 (Cohort and outcomes)] ==The study included first stimulation cycles of patients aged 20-40 from two centers but excluded diminished ovarian reserve and microstimulation; outcomes were number of oocytes and early moderate-to-severe OHSS within nine days of trigger.==
- [EC032-B0011 to EC032-B0017 (Model development)] ==Boruta selected features within the training data; eleven regression and eleven classification algorithms were evaluated with five-fold tuning, a held-out external cohort, cost-sensitive learning for rare OHSS, SHAP interpretation, and dose-response curves.==
- [EC032-B0020 to EC032-B0021 (Table 1)] ==The internal and external cohorts contained 6,401 and 3,805 patients, while OHSS events numbered only 55 and 46; there were large cross-center differences in stimulation protocols, FSH dose, AFC, glucose, and other measurements.==
- [EC032-B0022 to EC032-B0026 (Tables 2-3)] ==The chosen oocyte-yield regressor reported R-squared about 0.80 internally and externally; the OHSS model reported ROC-AUC 0.759 and 0.729, but very low PR-AUC values of 0.0176 and 0.0227 despite the table's threshold-specific classification metrics.==
- [EC032-B0036 to EC032-B0041 (Intended use and limitations)] ==The authors frame OHSS output as screening/risk stratification and the web tool as exploratory, acknowledge selection bias, few events, retrospective confounding, missing predictors, lack of prescriptive dosing, and lack of prospective evaluation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*