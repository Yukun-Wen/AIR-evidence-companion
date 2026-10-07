# STIM04 — Machine learning tool for predicting mature oocyte yield and trigger day from start of stimulation: towards personalized treatment

**Garg, Bellver, Bosch et al. (2025).** *Reproductive biomedicine online*. DOI: [10.1016/j.rbmo.2024.104441](https://doi.org/10.1016/j.rbmo.2024.104441)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Linked regression provides a different route from planning information to laboratory prognosis. A two-model neural pipeline first predicts the observed trigger day and then passes that estimate to an MII-yield model. Development uses 13,090 cleaned cycles from a 16-clinic network; testing uses 5,103 later cycles from the same network. Full-cohort MAEs are 1.60 days (95% CI, 1.56--1.64) and 3.75 MII oocytes (95% CI, 3.65--3.86). The first estimate characterizes agreement with recorded timing, while the second characterizes yield prediction through the linked system. For MII-yield prediction, the reported $R^2$ values of 0.88 and 0.70 belong to interquartile and outlier-removed subsets, respectively. Their narrower populations explain why those values are retained separately from the full-cohort errors [@STIM04].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict observed trigger day from stimulation onset and subsequent mature-oocyte yield using linked regression models. | STIM04-H0038 STIM04-H0043 |
| **Inputs** | Planning-time age, BMI, infertility cause, AMH, AFC, stimulation protocol and initial gonadotrophin dose are considered during feature selection; MII regression also receives predicted trigger day. Exact final feature configuration and architecture require supplements. | STIM04-H0041 STIM04-H0043 STIM04-H0053 |
| **Prediction time** | At planning/start of ovarian stimulation; trigger day is indexed to stimulation day, and MII prediction uses the first model's predicted trigger day. | STIM04-H0041 STIM04-H0043 STIM04-H0053 |
| **Analysis unit** | Ovarian-stimulation cycle, pooling donor and autologous cycles; uniqueness of patients across cycles and datasets is not established. | STIM04-H0038 STIM04-H0040 |
| **Method** | Two connected-layer deep-learning regression models implemented with TensorFlow/Keras; first predicts trigger day and its output enters the MII model. Pearson correlation guides feature selection using the primary dataset. | STIM04-H0041 STIM04-H0043 STIM04-H0045 |
| **Supervision / labels** | Historically observed duration from stimulation start to trigger and retrieved MII-oocyte count; observed trigger timing is the clinical practice label, not an experimentally established optimal action. | STIM04-H0041 STIM04-H0043 STIM04-H0045 |
| **Outcome** | Trigger day and MII-oocyte count; prediction performance rather than outcomes after assigning AI-selected treatment. | STIM04-H0043 STIM04-H0045 |
| **Sample sizes** | {"primary_2020_2022_cycles": 56490, "cleaned_development_cycles": 13090, "later_2023_validation_cycles": 5103, "clinics_in_network": 16, "development_training_percent": 80, "development_validation_percent": 15, "development_test_percent": 5, "unique_patients": "not established in examined source blocks"} | STIM04-H0038 STIM04-H0040 STIM04-H0043 |
| **Splitting** | Development cycles split 80/15/5 into training/validation/test; random allocation and patient grouping are not stated in the examined model description. Separate nonoverlapping 2023 cycles provide temporal validation in the same clinic network; patient overlap is unresolved. | STIM04-H0038 STIM04-H0043 STIM04-H0045 |
| **Validation** | The full 5,103-cycle temporal set has trigger-day MAE 1.60 days (95% CI 1.56–1.64) and MII MAE 3.75 (3.65–3.86). R² 0.88 and 0.70 refer to interquartile and outlier-removed populations respectively, not the unfiltered full set. | STIM04-H0056 STIM04-H0058 STIM04-H0062 STIM04-H0063 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*