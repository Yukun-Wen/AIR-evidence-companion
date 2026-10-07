# EE037 — Assessment of artificial intelligence model and manual morphokinetic annotation system as embryo grading methods for successful live birth prediction: a retrospective monocentric study.

**Papamentzelopoulou, Prifti, Mavrogianni et al. (2024).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-024-01198-7](https://doi.org/10.1186/s12958-024-01198-7)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** see EE037.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Decision benefit requires evaluation of a clinical policy
> ==A retrospective iDAScore/KIDScore comparison evaluates scores already used in transfer selection, with most transfers containing multiple embryos. Cycle-level birth attaches the observed outcome to the transferred group, and score-informed selection defines which embryos contribute that outcome. The report's adjusted coefficients, odds ratios and intervals are internally inconsistent, leaving the adjusted association uncertain [@EE037].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Compare iDAScore and KIDScoreD5 for live-birth prediction. | EE037-B0017 EE037-B0018 |
| **Inputs** | Raw time-lapse images for iDAScore; annotated timing and morphology for KIDScore. | EE037-B0013 EE037-B0014 EE037-B0015 |
| **Prediction time** | Blastocyst Day 5/earlyDay 6,108–148 h after insemination. | EE037-B0015 |
| **Analysis unit** | Embryo scores linked to cycle outcomes; most transfers include multiple embryos. | EE037-B0019 EE037-B0020 |
| **Method** | Frozen iDAScorev 1.2.0 and KIDScoreD5 with adjusted logistic analyses. | EE037-B0015 EE037-B0018 |
| **Supervision / labels** | Existing models evaluated against observed clinical outcomes. | EE037-B0017 EE037-B0018 |
| **Outcome** | Primary live birth; clinical pregnancy uses sac and FHB six weeks after transfer. | EE037-B0017 |
| **Sample sizes** | {"cycles": 91, "blastocysts": 429, "single_transfer_cycles": 19, "double_transfer_cycles": 70, "triple_transfer_cycles": 2} | EE037-B0019 EE037-B0020 |
| **Splitting** | Single-center retrospective cohort; no new training/test split for frozen scores. | EE037-B0018 EE037-B0042 |
| **Validation** | AUROC, selected thresholds and adjusted associations in the same cohort. | EE037-B0031 EE037-B0034 EE037-B0042 |

## Source-linked excerpts
- [EE037-B0015] ==iDAScore automatically rates full time-lapse sequences from 1 to 9.9 without patient features or manually entered morphokinetics.==
- [EE037-B0020] ==Only 19 cycles used single-embryo transfer; 70 used two embryos and two used three.==
- [EE037-B0031] ==The adjusted table reports coefficient 0.423 for KIDScore but OR 1.051 with CI 1.107-2.103, an internal numerical inconsistency confirmed in the PDF.==
- [EE037-B0034] ==Reported ROC AUC was 0.695 for KIDScore and 0.657 for iDAScore, with proposed cutoffs 7.4 and 8.3.==
- [EE037-B0042] ==The authors acknowledge retrospective design, score-based embryo selection, small sample size, good-prognosis bias, and mixed embryo-transfer counts.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*