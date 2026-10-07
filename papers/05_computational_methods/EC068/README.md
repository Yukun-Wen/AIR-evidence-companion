# EC068 — Construction and evaluation of machine learning-based prediction model for live birth following fresh embryo transfer in IVF/ICSI patients with polycystic ovary syndrome.

**Zhu, Huang, Chen et al. (2025).** *Journal of ovarian research*. DOI: [10.1186/s13048-025-01654-x](https://doi.org/10.1186/s13048-025-01654-x)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC068.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==Table entry; table caption: Selected tabular prediction designs and evaluation conditions. — XGBoost live-birth prediction in PCOS [@EC068]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth following fresh embryo transfer in PCOS. | EC068-B0012 |
| **Inputs** | Demographics, hormones and treatment/embryo variables; seven predictors selected by intersection of LASSO and RFE. | EC068-B0010 EC068-B0017 |
| **Prediction time** | At fresh transfer once embryo number/stage and treatment data are available; inferred from inputs. | EC068-B0010 EC068-B0014 |
| **Analysis unit** | Fresh embryo-transfer cycle in a woman with PCOS. | EC068-B0014 |
| **Method** | Decision tree, kNN, LightGBM, naive Bayes, RF, SVM and XGBoost; LASSO/RFE selection, grid search and SHAP. | EC068-B0012 EC068-B0017 |
| **Supervision / labels** | Live birth defined as delivery at ≥28 weeks with at least one specified sign of life. | EC068-B0011 |
| **Outcome** | Live birth using source-specific ≥28-week definition. | EC068-B0011 |
| **Sample sizes** | {"cycles": 1062, "live_birth_cycles": 466, "training": 743, "validation": 319, "unique_patients": "not separately reported in examined cohort description"} | EC068-B0014 |
| **Splitting** | Random 70/30 cycle split; five-fold model tuning; LASSO ten-fold selection described separately. Grouping of repeated patients and preprocessing nesting unclear. | EC068-B0012 |
| **Validation** | Internal AUROC, accuracy, precision, predictive values, F1, Brier and calibration; external validation explicitly not performed. | EC068-B0012 EC068-B0030 |

## Source-linked excerpts
- [EC068-B0005] ==The cohort was restricted to women with PCOS undergoing antagonist stimulation and fresh embryo transfer at one hospital.==
- [EC068-B0011] ==Live birth was explicitly defined as pregnancy reaching at least 28 weeks with a vital sign after delivery.==
- [EC068-B0012] ==The study used a random 7:3 split, LASSO plus RFE feature selection, grid search, five-fold cross-validation, and seven classifiers.==
- [EC068-B0019] ==Held-out XGBoost performance was AUC 0.822 with balanced sensitivity, specificity, and Brier score 0.172.==
- [EC068-B0030] ==The authors acknowledge single-center data, missing metabolic measures, and absence of external validation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*