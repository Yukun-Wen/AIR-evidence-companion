# EE030 — Leveraging federated learning for boosting data privacy and performance in IVF embryo selection.

**Lee, Tzeng, Li et al. (2024).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-024-03148-z](https://doi.org/10.1007/s10815-024-03148-z)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods, Learning objectives and the interpretation of model outputs

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Cross-cutting attributes: explanation and distributed development
> ==A FedTree study federates boosted prediction from centrally generated image grades and clinical features, placing the distributed step after image processing. Site performance and pairwise gains vary, and the non-aneuploid label includes mosaics. The study illustrates how a federated component inherits the representations and label definitions supplied by the rest of the pipeline [@EE030].==

> **§ Learning objectives and the interpretation of model outputs** : Genetic classification and assay-defined populations
> ==Mosaic handling determines an important part of the class definition. A model combining multi-focus temporal features and clinical variables groups mosaicism below 50% with euploid embryos and retrains its PGT-SR subgroup internally. It reports patient splitting alongside conflicting analyzed-video counts. Its class definition differs from the federated study's non-aneuploid category, making the mosaic rule an explicit field for harmonizing results [@EE041,EE030].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict aneuploidy and clinical pregnancy with federated models. | EE030-H0140 EE030-H0144 |
| **Inputs** | Clinical EMR features plus12-dimensional day5 image-derived expansion/ICM/TE vector. | EE030-H0145 EE030-H0307 |
| **Prediction time** | 110hpi or day5 imaging plus available clinical features. | EE030-H0145 |
| **Analysis unit** | Embryo nested in treatment/couple for ploidy; SET cycle for pregnancy. | EE030-H0140 EE030-H0144 |
| **Method** | Multitask image grading followed by FedTree horizontal federated gradient-boosted trees; local SVM/RF/GBDT comparisons. | EE030-H0307 EE030-H0311 EE030-H0314 |
| **Supervision / labels** | PGT-A labels: aneuploid>80% mosaicism versus all others; recorded SET clinical pregnancy. | EE030-H0140 EE030-H0144 |
| **Outcome** | Aneuploid versus non-aneuploid including mosaics; separate clinical pregnancy target. | EE030-H0140 EE030-H0144 |
| **Sample sizes** | {"ploidy_embryos": 10065, "ploidy_cycles": 3760, "ploidy_couples": 2479, "ploidy_hospitals": 5, "pregnancy_embryos_cycles": 4495, "pregnancy_couples": 3704, "pregnancy_hospitals": 4} | EE030-H0140 EE030-H0144 |
| **Splitting** | Random80/20 and five-fold CV; patient grouping not reported in examined description; participating hospitals contribute training and test. | EE030-H0143 |
| **Validation** | Hospital-specific AUROC comparisons of federated/local models, confidence intervals and pairwise hospital-combination experiments. | EE030-H0314 EE030-H0315 |

## Source-linked excerpts
- [EE030-H0124] ==The two tasks used 10,065 embryo records from five hospitals for ploidy and 4495 single-embryo transfers from four hospitals for clinical pregnancy.==
- [EE030-H0313] ==FedTree kept datasets local and exchanged model updates aggregated at a federated server.==
- [EE030-H0318] ==Federated ploidy AUCs ranged from 69.39% to 73.46% across hospitals, with an average reported gain of 2.5%.==
- [EE030-H0322] ==Federated clinical-pregnancy AUCs ranged from 56.77% to 72.03%, with an average reported gain of 3.08%.==
- [EE030-H0331] ==Pairwise federation sometimes reduced performance and adding all hospitals was not always optimal.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*