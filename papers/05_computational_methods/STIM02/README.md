# STIM02 — An interpretable machine learning model for individualized gonadotrophin starting dose selection during ovarian stimulation

**Fanton, Nutting, Rothman et al. (2022).** *Reproductive biomedicine online*. DOI: [10.1016/j.rbmo.2022.07.010](https://doi.org/10.1016/j.rbmo.2022.07.010)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Record construction and local estimation
> ==A related retrospective dose model makes the neighborhood construction explicit. It selects 100 neighbors using Manhattan distance over normalized age, BMI, AMH and AFC, then fits a constrained second-order polynomial to their observed starting-dose/MII-yield relationship. The KNN count predictor achieves MAE 3.79 MII oocytes and $R^2=0.45$ under fivefold cross-validation across 18,591 noncancelled autologous cycles from three clinics. Prediction and dose interpretation are separate steps: the local curve describes the treatment experience of similar cases, while propensity-matched comparisons relate model-defined dose groups to observed laboratory outcomes [@STIM02].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict mature-oocyte yield and construct individualized starting-FSH dose-response curves from similar historical cycles. | STIM02-H0035 STIM02-H0046 STIM02-H0048 |
| **Inputs** | Baseline age, BMI, AMH and AFC for patient-similarity retrieval; starting FSH and observed MII yield of neighboring cycles for quadratic dose-response fitting. AMH/AFC square-root transformed and inputs standardized. | STIM02-H0046 STIM02-H0048 STIM02-H0049 |
| **Prediction time** | Before ovarian stimulation for starting-dose support, using baseline patient measurements and historical neighbors; the evaluated dose contrasts are retrospective. | STIM02-H0032 STIM02-H0035 STIM02-H0046 |
| **Analysis unit** | Autologous non-cancelled retrieval cycle; repeated cycles may belong to one patient. Reported cycle counts are not unique-patient counts. | STIM02-H0040 STIM02-H0044 |
| **Method** | K-nearest-neighbor regression with K=100 and Manhattan distance; constrained second-order polynomial fits MII yield against starting FSH among neighbors. Curve shape identifies dose-responsive/flat-responsive groups; logistic propensity matching compares observed dose categories. | STIM02-H0046 STIM02-H0048 STIM02-H0053 STIM02-H0055 STIM02-H0057 |
| **Supervision / labels** | Recorded MII-oocyte counts train the KNN model; observed starting-FSH/MII pairs form the dose curves. Usable blastocysts are transferred plus frozen blastocysts. | STIM02-H0044 STIM02-H0046 STIM02-H0048 |
| **Outcome** | MII-oocyte count is the primary model target; retrospective comparisons additionally report 2PN embryos, usable blastocysts, starting FSH and total FSH. Retrieval-specific cumulative live birth is not directly linked and was only estimated under an explicit FET-linkage assumption. | STIM02-H0044 STIM02-H0053 STIM02-H0077 |
| **Sample sizes** | {"retrieval_cycles": 18591, "clinics": 3, "site1_cycles": 1229, "site2_cycles": 11233, "site3_cycles": 6129, "nearest_neighbors_per_curve": 100, "dose_responsive_matched_records_per_group": 2061, "unique_patients": "not established in examined source blocks"} | STIM02-H0040 STIM02-H0044 STIM02-H0055 STIM02-H0062 |
| **Splitting** | Five-fold cross-validation across all cycles for KNN prediction; patient-grouped folds and training-only standardization/tuning isolation are not established. Retrospective dose comparisons use the historical data with propensity matching. | STIM02-H0046 STIM02-H0051 STIM02-H0053 |
| **Validation** | Internal cross-validation: MAE 3.79 MII oocytes and R² 0.45. Propensity-matched observed-dose contrasts are separate observational analyses; no held-out clinic, temporal cohort or assigned treatment-policy evaluation is established in the examined methods. | STIM02-H0046 STIM02-H0053 STIM02-H0055 STIM02-H0061 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*