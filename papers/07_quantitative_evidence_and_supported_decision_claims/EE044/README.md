# EE044 — Comparing performance between clinics of an embryo evaluation algorithm based on time-lapse images and machine learning.

**Johansen, Parner, Kragh et al. (2023).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-023-02871-3](https://doi.org/10.1007/s10815-023-02871-3)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** see EE044.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Validation changes define the tested scope of transportability
> ==Case mix also changes clinic-level performance. An external four-clinic iDAScore evaluation standardizes AUC to a reference age distribution, reducing some between-clinic variation while retaining residual heterogeneity. The standardized result measures discrimination in a common age distribution. Calibration addresses absolute probability agreement, and within-cycle ranking addresses sibling order; each adds a distinct view of performance to this case-mix comparison [@EE044].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Compare clinic-specific iDAScore discrimination after standardizing maternal-age distributions. | EE044-B0009 EE044-B0010 |
| **Inputs** | iDAScore v1.0 based solely on time-lapse; maternal age used for evaluation standardization, not model input. | EE044-B0009 EE044-B0016 |
| **Prediction time** | Day-5/6 embryo evaluation before single transfer. | EE044-B0011 |
| **Analysis unit** | Transferred embryo/SET observation nested in treatment and clinic. | EE044-B0011 EE044-B0022 |
| **Method** | Previously trained 3D-CNN iDAScore; weighted ROC/AUC using outcome-specific age-density ratios and bootstrap. | EE044-B0009 EE044-B0017 EE044-B0018 |
| **Supervision / labels** | Observed fetal heartbeat at 6–8 weeks after transfer; no new model training in this study. | EE044-B0015 |
| **Outcome** | Fetal-heartbeat discrimination; age-standardized clinic AUC and between-clinic heterogeneity. | EE044-B0015 EE044-B0018 |
| **Sample sizes** | {"external_embryos": 4805, "external_treatments": 4086, "external_clinic_embryos": [780, 1959, 1662, 404], "reference_embryos": 666, "reference_treatments": 650} | EE044-B0021 EE044-B0022 |
| **Splitting** | External four-clinic data excluded from original training; reference age population from independent internal held-out set. | EE044-B0011 EE044-B0014 |
| **Validation** | External clinic-specific conventional and age-standardized ROC/AUC with 10,000 bootstrap repetitions and heterogeneity statistics. | EE044-B0017 EE044-B0018 |

## Source-linked excerpts
- [EE044-B0011] ==The external study population was assembled from four clinics, excluded model-training data, and was restricted to autologous single transfers with known age and fetal-heartbeat outcome.==
- [EE044-B0018] ==Outcome-specific age-density ratios were used to weight sensitivity and specificity, yielding clinic-specific standardized ROC curves and AUCs with bootstrap intervals.==
- [EE044-B0027] ==Standardized AUCs ranged from 0.60 to 0.71 and reduced estimated between-clinic variance from 0.0026 to 0.0022, while clinic 3 remained lower.==
- [EE044-B0035] ==The authors caution that sparse age ranges can destabilize the method and that findings do not necessarily generalize to donors or ages outside 21-44.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*