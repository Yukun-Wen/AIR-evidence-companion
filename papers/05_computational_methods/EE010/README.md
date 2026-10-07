# EE010 — Embryo selection at the cleavage stage using Raman spectroscopy of day 3 culture medium and machine learning: a preliminary study.

**Cao, Xiong, Lu et al. (2025).** *Frontiers in endocrinology*. DOI: [10.3389/fendo.2025.1608318](https://doi.org/10.3389/fendo.2025.1608318)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE010.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Single-source molecular predictors establish baselines for added-modality evaluation. Fusion joins measurements within a predictor; agreement between separate analyses supplies biological corroboration. A preliminary day-three spent-medium Raman study combines spectral classifiers for later embryo morphology. Repeated spectra are tested by sample, with couple grouping unspecified; preprocessing and feature selection construct the developmental representation [@EE010,R012].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict extended-culture blastocyst quality/usability from day-3 spent culture medium. | EE010-B0007 EE010-B0008 |
| **Inputs** | Raman spectra of spent day-3 medium; 30–40 spectra sampled per medium specimen. | EE010-B0010 EE010-B0011 |
| **Prediction time** | Day 3, after culture-medium collection and before day-5/6 extended-culture outcome. | EE010-B0010 |
| **Analysis unit** | Spectra nested in medium sample/embryo nested in couple. | EE010-B0007 EE010-B0023 |
| **Method** | Twelve classifiers including MLP/ANN/GRU, GB, kNN, RF, SVM, discriminant and logistic models; SMOTE, four-model stacking and sample majority vote. | EE010-B0021 |
| **Supervision / labels** | Known day-5/6 morphology: good blastocyst, non-good but useful blastocyst, or clinically non-useful embryo. | EE010-B0009 EE010-B0021 |
| **Outcome** | Three extended-culture morphology/usability classes, not implantation/pregnancy. | EE010-B0009 |
| **Sample sizes** | {"couples": 78, "medium_samples": 172, "good_blastocyst": 58, "nongood_useful": 25, "nonuseful": 89, "spectra_per_sample": "30–40"} | EE010-B0007 EE010-B0023 |
| **Splitting** | Random 80/20 split within each sample-outcome group; five-fold tuning for traditional ML. Patient/couple grouping not specified. | EE010-B0007 EE010-B0021 |
| **Validation** | Internal prediction-set spectrum and sample accuracy/sensitivity/specificity and class ROC; aggregation via mode of spectra. | EE010-B0021 |

## Source-linked excerpts
- [[EE010-B0007]] ==The study used 172 day-3 spent-media samples divided into three later developmental-outcome groups and randomly allocated 80% of samples per group to training and the remainder to prediction.==
- [[EE010-B0009]] ==Labels were based on day-5/day-6 morphology: good blastocyst, non-good but clinically useful blastocyst, or clinically non-useful embryo.==
- [[EE010-B0021]] ==Twelve deep and conventional models were evaluated, traditional models used five-fold cross-validation, the training set used SMOTE, and the four best models were stacked with sample-level mode aggregation across spectra.==
- [[EE010-B0023]] ==The 172 samples came from 78 couples, with multiple day-3 embryos and samples per couple in this favorable-prognosis cohort.==
- [[EE010-B0033]] ==The stacked MLP/ANN/GRU/LDA model correctly classified 33 of 35 held-out samples, for overall accuracy 0.94, sensitivity 0.93 and specificity 0.97.==
- [[EE010-B0040]] ==The authors cite small sample size, uncertain cross-laboratory transportability, absence of a randomized clinical-outcome trial and omission of day-5 versus day-6 developmental speed.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*