# EC061 — Predictive models for live birth outcomes following fresh embryo transfer in assisted reproductive technologies using machine learning.

**Wu, Wang, Liu et al. (2025).** *Journal of translational medicine*. DOI: [10.1186/s12967-025-07045-6](https://doi.org/10.1186/s12967-025-07045-6)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC061.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==Table entry; table caption: Selected tabular prediction designs and evaluation conditions. — RF live-birth prediction with 55 selected variables [@EC061]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth after fresh cleavage-stage embryo transfer. | EC061-B0006 |
| **Inputs** | 75 clinical predictors reduced to 55, including embryo grades/counts, fertilization outcomes, treatment and baseline variables. | EC061-B0014 EC061-B0015 |
| **Prediction time** | At or after selection of embryos for fresh transfer, inferred from transfer-day and embryo-quality inputs. | EC061-B0015 |
| **Analysis unit** | Fresh-transfer record; unique patient count not established. | EC061-B0012 |
| **Method** | RF, XGBoost, GBM, AdaBoost, LightGBM and ANN; missForest imputation and five-fold grid search. | EC061-B0007 EC061-B0008 |
| **Supervision / labels** | Recorded fully tracked live-birth versus non-live-birth outcomes. | EC061-B0012 EC061-B0014 |
| **Outcome** | Binary live birth following fresh transfer. | EC061-B0014 |
| **Sample sizes** | {"initial_records": 51047, "analyzed_records": 11728, "live_birth": 3971, "no_live_birth": 7757} | EC061-B0012 EC061-B0014 |
| **Splitting** | 60/40,70/30 and 80/20 record splits with five-fold CV within training; patient grouping not stated. | EC061-B0016 |
| **Validation** | Internal AUROC and classification metrics, calibration curves and Brier scores; subgroup/perturbation sensitivity analyses. | EC061-B0008 EC061-B0018 |

## Source-linked excerpts
- [EC061-B0012] ==Filtering reduced 51,047 records to 11,728 tracked fresh cleavage-stage transfer records, and missing values were imputed with missForest.==
- [EC061-B0016] ==The authors compared three random train-test ratios and reported RF and XGBoost above 0.8 AUC only at the 80% training ratio.==
- [EC061-B0020] ==At the emphasized 80:20 split, RF test AUC was 0.807 and XGBoost AUC was 0.804, with lower accuracy and sensitivity than AUC alone suggests.==
- [EC061-B0021] ==Subgroup discrimination and sensitivity varied materially, including lower AUC for two good-quality embryos and low sensitivity in younger women.==
- [EC061-B0034] ==The authors acknowledge single-center generalizability limits, subjective morphology grading, and restriction to cleavage-stage fresh transfers.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*