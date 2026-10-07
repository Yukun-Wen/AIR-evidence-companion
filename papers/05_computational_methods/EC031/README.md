# EC031 — Enhanced predictive performance of artificial intelligence in individualized ovarian stimulation of in vitro fertilization: a retrospective cohort study.

**Wang, Tang, Zhou et al. (2026).** *BMC medicine*. DOI: [10.1186/s12916-026-04769-0](https://doi.org/10.1186/s12916-026-04769-0)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==The target's mathematical structure determines the learning objective. Binary response classes, oocyte counts and dose-normalized transformations use different losses and scales. An externally evaluated XGBoost framework separates baseline response-risk models from models encoding a planned stimulation regimen; enumerated regimens yield conditional predictions for the observed treatment setting. Another two-center study predicts the logarithm of retrieved-oocyte count divided by starting FSH dose alongside early OHSS risk. Its regression errors are on that transformed scale, and discrepancies among its threshold metrics remain unresolved. These examples connect target transformation and predictor timing to performance interpretation [@EC031,EC032,R041,R042].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict low/high ovarian response and rank predefined stimulation strategies. | EC031-B0009 |
| **Inputs** | Baseline demographics, history, hormones and reserve markers; strategy models additionally use protocol,FSH starting dose,recombinantFSH and LH supplementation. | EC031-B0008 EC031-B0009 |
| **Prediction time** | Before stimulation using pretreatment features and planned treatment components. | EC031-B0008 EC031-B0009 |
| **Analysis unit** | Woman first controlled-ovarian-stimulation cycle. | EC031-B0005 |
| **Method** | XGBoost selected from six algorithms; SHAP feature selection; risk and strategy submodels enumerate 83 predefined regimens. | EC031-B0009 EC031-B0010 |
| **Supervision / labels** | Supervised observed low/high-response labels; hypothetical strategies evaluated against actual physician-chosen treatment outcomes. | EC031-B0007 EC031-B0013 |
| **Outcome** | Low response<4 and high response>20 retrieved oocytes; strategy precision is retrospective classification, not causal treatment benefit. | EC031-B0007 EC031-B0013 |
| **Sample sizes** | {"derivation_screened": 12780, "external_screened": 6323, "derivation_analyzed": 12012, "external_analyzed": 5702, "derivation_LOR": 1714, "derivation_HOR": 1123, "external_LOR": 882, "external_HOR": 416} | EC031-B0005 EC031-B0021 |
| **Splitting** | Separate hospital external cohort; stratified 5-fold Bayesian tuning. Calendar periods 2017–2020 and 2018–2022 overlap. | EC031-B0005 EC031-B0010 |
| **Validation** | Internal/external discrimination, calibration/Brier, marker-only comparators, complete-case and subgroup sensitivity; no prospective treatment validation. | EC031-B0012 EC031-B0013 EC031-B0045 |

## Source-linked excerpts
- [EC031-B0005 (Study population)] ==The derivation cohort came from one Chinese tertiary hospital and the independent external cohort from another; first stimulation cycles were used, with 12,780 and 6,323 initially described and only Asian women represented.==
- [EC031-B0009 to EC031-B0013 (System design and evaluation)] ==Two risk models and two strategy models were constructed; the strategy models enumerate 83 predefined treatment combinations and act as what-if simulations, with internal/external validation and comparisons against conventional ovarian-reserve-marker models.==
- [EC031-B0023 to EC031-B0029 and Table 2] ==XGBoost submodels reported derivation AUCs of 0.89-0.95, Brier scores of 0.064-0.072, superiority over marker-only comparators, and retained external-validation AUCs described as 0.84-0.88.==
- [EC031-B0036 (Retrospective strategy evaluation)] ==The strategy models reported precision above 95%, balanced accuracy near 85-86%, and MCC of 0.76-0.80 when the observed response under the actual physician-selected treatment was used to label strategies.==
- [EC031-B0045 (Limitations)] ==The authors acknowledge two-center Han Chinese data, no cumulative live-birth linkage, no prospective validation of recommendations, institutional practice differences, and noncausal joint modeling of patient features and physician-controlled decisions.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*