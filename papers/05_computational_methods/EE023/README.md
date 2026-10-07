# EE023 — Application of a methodological framework for the development and multicenter validation of reliable artificial intelligence in embryo evaluation.

**Gilboa, Garg, Shapiro et al. (2025).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-025-01351-w](https://doi.org/10.1186/s12958-025-01351-w)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE023.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Direct video encoders and shared representations
> ==A ResNet-based time-lapse scoring study separates a blind test at contributing clinics from evaluation at seven unseen clinics. It also distinguishes transferred embryos with known fetal-heartbeat outcomes from analyses including discarded embryos assigned negative labels. Together, the tests examine two dimensions of generalization: clinic change and the population supplying outcome labels [@EE023].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Score embryos for fetal-heartbeat potential and rank across morphology range. | EE023-B0009 |
| **Inputs** | Central-plane blastocyst-stage frames from time-lapse sequence, automatically cropped. | EE023-B0008 EE023-B0012 |
| **Prediction time** | Only embryos cultured to at least105hpi; blastocyst-stage inference. | EE023-B0008 EE023-B0009 |
| **Analysis unit** | Embryo; SET-only outcome evaluation. | EE023-B0006 EE023-B0018 |
| **Method** | ResNet50 dual heads with U-Net crop/area, ResNet blastulation detector and heuristic temporal score smoothing. | EE023-B0011 EE023-B0012 EE023-B0013 EE023-B0014 |
| **Supervision / labels** | FH+/FH− for transferred embryos; discarded embryos pseudo-labeled FH− but separated by second usable/discard head. | EE023-B0011 |
| **Outcome** | 1.0–9.9 embryo score associated with ultrasound fetal heartbeat; not calibrated probability by construction. | EE023-B0009 EE023-B0014 |
| **Sample sizes** | {"development_embryos": 16935, "development_transferred": 9810, "development_discarded": 7125, "blind_test": 1708, "independent_initial": 7445, "independent_analyzed": 6246, "SET_known_outcomes": 1959, "development_clinics": 3, "independent_clinics": 7} | EE023-B0006 EE023-B0015 EE023-B0018 |
| **Splitting** | 85/15 development split; blind test patient/treatment-disjoint with clinic overlap; independent set clinic/patient/treatment-disjoint. | EE023-B0006 EE023-B0010 |
| **Validation** | AUROC and score/age/source/morphology associations, including independent7-clinic evaluation. | EE023-B0015 EE023-B0018 |

## Source-linked excerpts
- [EE023-B0006] ==The development set contained 16,935 embryos, while blind and independent validation sets represented overlapping and entirely unseen clinics, respectively.==
- [EE023-B0018] ==Clinical-outcome analysis was restricted to single-embryo transfers, yielding 1,959 embryos with known fetal-heartbeat results.==
- [EE023-B0031] ==Among embryos with known transfer outcomes, AUC was 0.630 in the test dataset and 0.659 in the independent dataset.==
- [EE023-B0042] ==The authors identify retrospective design, uncontrolled confounding, and the need for randomized prospective evaluation as major limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*