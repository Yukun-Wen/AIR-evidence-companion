# EE082 — Selecting the embryo with the highest implantation potential using a data mining based prediction model.

**Chen, De Neubourg, Debrock et al. (2016).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-016-0145-1](https://doi.org/10.1186/s12958-016-0145-1)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE082.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Morphometry and complementary image representations
> ==Computer-assisted Z-stack measurements provide an earlier morphometric pathway. Manually traced blastomere dimensions feed logistic or multivariate adaptive regression splines models, evaluated on later same-center transfers. Comparison with routine embryo selection identifies changed choices among the available embryos, whose untransferred alternatives have unobserved outcomes [@EE082].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict implantation/clinical pregnancy and compare retrospective embryo selections. | EE082-B0008 EE082-B0020 |
| **Inputs** | Day1–3Z-stack-derived blastomere count,manual diameter-based volume,fragmentation and size diversity; visual scores comparator. | EE082-B0014 EE082-B0015 EE082-B0019 |
| **Prediction time** | Day3transfer after66–71hpiassessment. | EE082-B0014 |
| **Analysis unit** | Single transferred embryo in first ART cycle/woman. | EE082-B0008 |
| **Method** | Backward-elimination LR and MARS with10-foldCV; separate standard-score and computer-assisted features. | EE082-B0025 EE082-B0026 |
| **Supervision / labels** | Clinical-pregnancy outcome after SET. | EE082-B0008 EE082-B0009 |
| **Outcome** | Clinical pregnancy/implantation and retrospective disagreement with routine top-quality selection. | EE082-B0008 EE082-B0020 |
| **Sample sizes** | {"development_SET_embryos": 871, "development_pregnancies": 288, "temporal_validation_SET": 109, "validation_pregnancies": 42, "selection_comparison_patients": 104} | EE082-B0008 EE082-B0009 EE082-B0010 |
| **Splitting** | 2008–2013development,2014same-center temporal validation; MARS10-fold trainingCV. | EE082-B0008 EE082-B0009 EE082-B0026 |
| **Validation** | Temporal AUROC for CASS/standard-score LR/MARS; separate104patient retrospective choice comparison. | EE082-B0027 EE082-B0031 |

## Source-linked excerpts
- [EE082-B0008] ==Model development used 871 imaged single transferred embryos from first ART cycles in women younger than 36, with 288 clinical pregnancies.==
- [EE082-B0015] ==The computer-assisted system used the same recorded images as visual scoring but required manual diameter outlines, from which volume, fragmentation, and size-difference measures were calculated.==
- [EE082-B0031] ==Retained Table 5 shows stable but modest validation for computer-assisted models (AUC 0.64 and 0.69) and marked degradation for standard-score models (AUC 0.55 and 0.54).==
- [EE082-B0033] ==In a retrospective set of 104 cases with multiple top-quality embryos, the prediction model selected a different embryo in 68 cases.==
- [EE082-B0043] ==The authors identify single-center data and retrospective CASS analysis as major limitations and call for a prospective randomized evaluation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*