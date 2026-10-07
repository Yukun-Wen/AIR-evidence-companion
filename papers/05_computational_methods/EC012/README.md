# EC012 — Machine-learning algorithm incorporating capacitated sperm intracellular pH predicts conventional in vitro fertilization success in normospermic patients.

**Gunderson, Puga Molina, Spies et al. (2021).** *Fertility and sterility*. DOI: [10.1016/j.fertnstert.2020.10.038](https://doi.org/10.1016/j.fertnstert.2020.10.038)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational methods, Design challenges and directions for validated AI

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Semen-derived vectors support both fertilization assessment and pregnancy prognosis. Yi compares machine-learning and logistic models using same-day semen characteristics in short-term IVF and rescue-ICSI pathways, with machine-learning partitioning incompletely specified. Mehrjerd combines routine semen variables in ensembles for pregnancy across IVF and ICSI. Metric choice changes the latter comparison: random forest has the higher AUC, while bagging has the higher accuracy. A defined threshold and treatment pathway connect these probabilities to prospective triage or sperm-selection decisions [@EC003,EC004]. A gradient-boosted model combines intracellular pH, membrane potential and clinical variables to predict conventional-IVF fertilization from leftover sperm incubated overnight. A separate model predicts sufficient sperm for ICSI in men with NOA, testing 26 later patients at the same centre [@EC012,EC019].==

> **§ Design challenges and directions for validated AI** : Isolating the contribution of a computational mechanism
> ==Table entry; table caption: Source-located limitations and studies that could address them. — Overnight assays of leftover sperm [@EC012]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict conventional IVF fertilization above two-thirds in normospermic couples. | EC012-H0160 |
| **Inputs** | Sperm intracellular pH, membrane potential, hyperactivated motility and clinical IVF covariates; ordinary semen parameters excluded. | EC012-H0161 EC012-H0335 |
| **Prediction time** | Measured after oocyte retrieval and overnight 18-hour capacitation of leftover sperm; operational pre-insemination availability was not demonstrated. | EC012-H0146 EC012-H0148 |
| **Analysis unit** | Couple/IVF cycle, with sperm-sample functional assays. | EC012-H0144 EC012-H0161 |
| **Method** | Gradient-boosted classifier with recursive feature elimination and bootstrap assessment. | EC012-H0161 EC012-H0335 |
| **Supervision / labels** | Supervised labels from observed 2PN fertilization ratio. | EC012-H0148 EC012-H0160 |
| **Outcome** | More than 0.66 normally fertilized 2PN oocytes per mature oocyte, not pregnancy or live birth. | EC012-H0160 |
| **Sample sizes** | {"couples": 76, "training_couples": 58, "test_couples": 18, "assay_reference_fertile_men": 10} | EC012-H0144 EC012-H0161 |
| **Splitting** | Random 58/18 couple split; nominal 75/25 proportions. | EC012-H0161 |
| **Validation** | Single-center internal holdout with 500 bootstrap assessments; results-text mean AUROC0.81 differs from individual Fig 3C estimate 0.831. | EC012-H0333 EC012-H0335 EC012-H0344 |

## Source-linked excerpts
- [EC012-H0144] ==Couples were in conventional IVF or split conventional-IVF/ICSI cycles; 76 of 80 contacted men consented, with ICSI-only and known male-factor cases excluded.==
- [EC012-H0160] ==The gradient-boosted target was conventional-IVF fertilization ratio above 0.66, defined using two-pronuclear zygotes per mature oocyte.==
- [EC012-H0335] ==The model used 58 couples for training and 18 for testing and reported mean accuracy 0.72 and mean AUC 0.81 after repeated bootstrap assessment.==
- [EC012-H0344] ==The authors identify cost, single-center sampling, limited patient count, and diagnostic heterogeneity as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*