# EC041 — Prediction model of gonadotropin starting dose and its clinical application in controlled ovarian stimulation.

**Hua, Zhe, Jing et al. (2022).** *BMC pregnancy and childbirth*. DOI: [10.1186/s12884-022-05152-6](https://doi.org/10.1186/s12884-022-05152-6)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** see EC041.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Action imitation learns recorded decisions. A LightGBM system predicts an expert's retrieval and medication choices from monitoring visits, including low-dose hCG for supplementation of LH activity. This target differs from trigger prescribing, and drug-specific agreement differs from complete-prescription agreement. Another ANN/SVR dose model duplicates records according to proximity of realized yield to a target before splitting the expanded rows, creating possible cross-partition copies unless grouped. Its later same-centre test evaluates agreement with clinician doses. The resulting objective is outcome-weighted prescribing imitation [@EC039,EC041].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict gonadotropin starting dose from patient characteristics with response-weighted historical training. | EC041-B0008 EC041-B0009 |
| **Inputs** | Age, infertility type/duration, BMI, AFC, basal FSH/E2/LH/AMH and treatment scheme. | EC041-B0056 |
| **Prediction time** | Before gonadotropin initiation; timing inferred from starting-dose decision and baseline inputs. | EC041-B0055 EC041-B0056 |
| **Analysis unit** | Woman in first oocyte-retrieval cycle. | EC041-B0006 |
| **Method** | ANN with three hidden layers of 5,4,5 nodes and Gaussian-kernel SVR; retrieved-oocyte-dependent weights implemented by repeating original samples. | EC041-B0008 EC041-B0011 EC041-B0012 EC041-B0022 EC041-B0034 |
| **Supervision / labels** | Historical clinician-selected starting dose is regression target; oocyte count informs sample weighting. | EC041-B0011 EC041-B0057 |
| **Outcome** | Dose prediction error and correlation; later patient comparison to clinician dose. | EC041-B0013 EC041-B0057 |
| **Sample sizes** | {"development_unique_women": 1555, "response_weighted_records_after_repetition": 4037, "ann_training_weighted_records": 2826, "ann_validation_weighted_records": 686, "ann_test_weighted_records": 525, "later_application_patients": 81} | EC041-B0006 EC041-B0022 EC041-B0024 EC041-B0033 |
| **Splitting** | Original1555samples expanded by repeating each sample according to response weight, then4037records partitioned2826/686/525 (70/17/13) for ANN; SVR80/20. Grouping repeated copies by original woman is not stated. | EC041-B0011 EC041-B0012 EC041-B0022 EC041-B0033 |
| **Validation** | RMSE/R on internal sets; 81 later same-center patients for dose agreement, mean absolute error 14.08 units. | EC041-B0013 EC041-B0024 EC041-B0057 |

## Source-linked excerpts
- [EC041-B0006] ==The development cohort comprised 1,555 women undergoing their first IVF/ICSI oocyte-retrieval cycle at one center.==
- [EC041-B0022] ==Outcome-based weighting duplicated each original patient record up to a rounded weight, expanding 1,555 patients into 4,037 modeling rows before splitting.==
- [EC041-B0036] ==The ANN reported test RMSE 34.21 IU and correlation R 0.942 for predicting the historical starting dose.==
- [EC041-B0057] ==In 81 later patients, model-recommended dose differed from clinician dose by a mean absolute 14.08 IU.==
- [EC041-B0067] ==The authors explicitly acknowledge there was no direct evidence, and no reported percentage, that model use moved retrieved-oocyte counts toward 16.==
- [EC041-B0069] ==Future work was proposed to compare outcomes with versus without the model, confirming that such clinical-benefit evidence was not supplied here.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*