# EE048 — Towards Automation in IVF: Pre-Clinical Validation of a Deep Learning-Based Embryo Grading System during PGT-A Cycles.

**Cimadomo, Chiappetta, Innocenti et al. (2023).** *Journal of clinical medicine*. DOI: [10.3390/jcm12051806](https://doi.org/10.3390/jcm12051806)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Decision benefit requires evaluation of a clinical policy
> ==An external preclinical score evaluation uses biopsied embryos for euploidy analysis and euploid single transfers for live-birth analysis. These populations locate the score's association at two successive stages of treatment. Its sibling-ranking simulation extends evaluation to embryos with unobserved transfer outcomes through assumptions about outcome availability. The subsection population and figure caption identify the endpoint attached to each analysis despite a conflicting label in the report [@EE048].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Externally evaluate iDAScore1.0 for grading,ploidy discrimination and live birth in PGT-A cycles. | EE048-B0007 EE048-B0008 |
| **Inputs** | 128 time-lapse images from12–140hpi; no patient variables. | EE048-B0012 |
| **Prediction time** | Blastocyst-stage scoring after required time-lapse observation. | EE048-B0012 |
| **Analysis unit** | Embryo and euploid SET nested within first PGT-A patient cycle. | EE048-B0007 EE048-B0008 |
| **Method** | Previously trained3D-CNN iDAScore v1.0,used as fixed scoring system. | EE048-B0012 |
| **Supervision / labels** | Prior model training uses fetal-heartbeat outcomes and broad embryo corpus; current study supplies PGT-A,expert grades and LB reference labels. | EE048-B0012 |
| **Outcome** | Morphology association,euploidy and live birth; retrospective within-cohort ranking simulations. | EE048-B0008 EE048-B0009 |
| **Sample sizes** | {"patients_first_PGT_cycles": 1232, "biopsied_embryos": 3604, "euploid_embryos": 1443, "euploid_SETs": 808, "SET_patients": 610, "mixed_ploidy_ranking_cycles": 587, "LB_ranking_cycles": 202} | EE048-B0007 EE048-B0008 EE048-B0009 |
| **Splitting** | Entire local cohort is external preclinical validation; clinic not in18-clinic training corpus. | EE048-B0012 |
| **Validation** | ROC/AUC versus embryologists,subgroup/multivariable associations and retrospective ranking simulations. | EE048-B0008 EE048-B0013 |

## Source-linked excerpts
- [EE048-B0007] ==The external clinic included 1232 first PGT-A cycles and 3604 biopsied blastocysts, with scores generated retrospectively so they did not guide care.==
- [EE048-B0019] ==Algorithm scores were associated with chromosomal status, but euploidy discrimination was AUC 0.60 compared with 0.66 for embryologist assessment.==
- [EE048-B0021] ==Among 808 euploid single transfers, live-birth discrimination was AUC 0.66 for the algorithm and 0.64 for embryologist assessment.==
- [EE048-B0022] ==The multi-euploid ranking simulation was unevaluable in 29% of cycles because algorithm-top embryos remained untransferred, potentially biasing the comparison.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*