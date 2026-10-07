# EE007 — Blastulation and ploidy prediction using morphology assessment in 33,999 day-3 embryos.

**Elkhatib, Kalafat, Bayram et al. (2025).** *Scientific reports*. DOI: [10.1038/s41598-025-19898-4](https://doi.org/10.1038/s41598-025-19898-4)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** see EE007.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Developmental forecasts and surrogate targets
> ==Day-three prediction also supports composite endpoints. An XGBoost study combines morphology and age to estimate later biopsy-quality and euploid-blastocyst development. The latter target follows embryos from the day-three population through development to an assay-defined state. A cycle-level ranking comparison and cycle-based partition evaluate the ordering of that developmental potential within treatment cohorts [@EE007].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict biopsiable blastocyst and euploid-blastocyst development from day-3 embryos. | EE007-B0028 |
| **Inputs** | Final models use day-3 cell count, fragmentation and female age; wider candidate clinical set and MICE. | EE007-B0001 EE007-B0034 |
| **Prediction time** | Day 3 at 68 ±1 hours post-insemination. | EE007-B0028 |
| **Analysis unit** | Embryo nested in cycle and couple. | EE007-B0034 |
| **Method** | XGBoost classification; cycle-level embryo selection comparison. | EE007-B0035 |
| **Supervision / labels** | Biopsiable blastocyst morphology ≥BL3CC; TE-biopsy NGS ploidy for qualifying blastocysts. | EE007-B0031 EE007-B0032 EE007-B0033 |
| **Outcome** | Biopsiable blastulation and euploid blastocyst yield from day-3 embryo; not live birth. | EE007-B0028 EE007-B0038 |
| **Sample sizes** | {"day3_embryos": 33999, "cycles": 5702, "unique_couples": "not_reported_in_examined_source"} | EE007-B0001 |
| **Splitting** | Cycle-based two-fold splits; 200 repetitions for selection,1000 for final validation; text also claims different patients, requiring confirmation across repeat cycles. | EE007-B0035 EE007-B0036 EE007-B0037 |
| **Validation** | Internal AUROC, shrinkage, calibration intercept/slope, Brier and scaled cycle-level correct-call score; simple morphology comparator. | EE007-B0035 EE007-B0037 |

## Source-linked excerpts
- [[EE007-B0028]] ==The single-centre cohort used autologous cycles from 2017-2021, with morphology recorded at 68 plus or minus 1 hours post-insemination and later biopsy of eligible day-5 to day-7 blastocysts.==
- [[EE007-B0035]] ==XGBoost models used repeated two-fold cross-validation with allocation by cycle rather than embryo; the paper says training and testing involved different patients.==
- [[EE007-B0010]] ==Candidate clinical and laboratory features were examined with SHAP, but the final parsimonious models used female age, day-3 cell count and fragmentation.==
- [[EE007-B0012]] ==Validation AUCs were 0.72 for biopsiable blastocyst formation and 0.73 for euploid blastocyst prediction, with generally good but imperfect calibration.==
- [[EE007-B0015]] ==Cycle-level correct-call scores were higher for the ML models than for highest-cell-count/lowest-fragmentation selection and random selection across all three reported targets.==
- [[EE007-B0025]] ==The authors identify subjective morphology scoring and development/validation at one centre as major limitations requiring external validation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*