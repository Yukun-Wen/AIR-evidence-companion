# ER045 — Inferring simple but precise quantitative models of human oocyte and early embryo development

**Leahy, Racowsky, Needleman (2021).** *Journal of the Royal Society, Interface*. DOI: [10.1098/rsif.2021.0475](https://doi.org/10.1098/rsif.2021.0475)

**Role:** core · workflow: Oocyte–embryo development

**Cited in:** Computational methods

**PDF:** see ER045.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==A probabilistic graphical model exposes conditional structure among variables. Leahy learns a Bayesian network linking stimulation, maturation and embryo development, incorporating assumptions for missing observations and multiple transfers. The fitted relations connect the observed stimulation and developmental measurements to fetal heartbeat. The supplementary material details regression and multiple-transfer likelihoods and internal cycle-level validation; patient-grouped splitting is not established for this single-clinic cohort [@ER045].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Infer sparse quantitative models of human oocyte maturation and pre-implantation embryo development. | ER045-F001 ER045-F002 |
| **Inputs** | Clinical tabular variables: age, BMI, AMH, FSH/HMG doses, retrieved eggs, MII count, peak estradiol and day-3/day-5 embryo morphology; up to 69 recorded patient/stimulation variables. | ER045-F002 ER045-F006 ER045-F007 ER045-F009 |
| **Prediction time** | Multiple explanatory time points, not a single deployable baseline model: pre-stimulation variables, treatment response and day-3/day-5 development; heartbeat prediction after the relevant embryo assessment. | ER045-F006 ER045-F007 ER045-F009 |
| **Analysis unit** | Cycles for ovarian physiology; embryos nested in cycles for development; number of fetal heartbeats per transfer for partially identified multi-embryo outcomes. | ER045-F002 ER045-F007 ER045-F008 |
| **Method** | Bayesian nonlinear polynomial regression and conditional-correlation tests; temporally constrained DAG construction; maximum-a-posteriori Poisson-binomial likelihood for multiple transfers and Bayesian model comparison. | ER045-F002 ER045-F004 ER045-F006 ER045-F008 |
| **Supervision / labels** | Observed clinical continuous/count variables and embryo grades; observed heartbeat count supplies aggregate supervision for multi-embryo transfers; explicit missingness variables. | ER045-F002 ER045-F007 ER045-F008 |
| **Outcome** | Oocyte maturation and day-3/day-5 development; fetal heartbeat after transfer. Formal supplementary variable table defines the heartbeat variable as FH>12wk. | ER045-F007 ER045-F008 |
| **Sample sizes** | {"cycles": 7399, "oocytes": 98264, "embryos": 57827, "complete_four_variable_cycles": 4910, "day3_recorded_embryos": 55350, "also_day5_recorded": 41932, "ovarian_train_cycles_SI": 3413, "ovarian_test_cycles_SI": 1497} | ER045-F002 ER045-F007 |
| **Splitting** | Separate internal training/test sets; formal supplement identifies 3413 training and 1497 test cycles for ovarian analysis. Patient grouping and exact allocation procedure are not reported in examined main/SI methods. | ER045-F002 ER045-F006 |
| **Validation** | Held-out conditional correlations/residual-variance comparisons and heartbeat-model likelihood tests; compare 99 conditional-independence statistics with 3000 simulated datasets. No external-center validation. | ER045-F006 ER045-F007 |

## Source-linked excerpts
- [ER045-P001] ==The study analyzes 7,399 clinical IVF cycles, 98,264 oocytes and 57,827 embryos using data-driven Bayesian-network models.==
- [ER045-P002] ==For key ovarian variables, nonlinear regression and Bayesian model evidence were used, with separate train and test sets as an overfitting check.==
- [ER045-P007] ==The proposed ovarian model's 99 conditional-independence predictions were checked in train and test data and compared with 3,000 simulated datasets.==
- [ER045-P008] ==Embryo analyses modeled informative missingness and multiple transfers; fetal-heartbeat likelihood used a generative Poisson-binomial approach for cycles transferring more than one embryo.==
- [ER045-P009] ==Day-3 morphology variables added no fetal-heartbeat information after day-5 variables in the analyzed data, supporting the reported memoryless coarse-grained model.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*