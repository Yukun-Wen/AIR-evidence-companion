# EE080 — Deep learning as a predictive tool for fetal heart pregnancy following time-lapse incubation and blastocyst transfer.

**Tran, Cooke, Illingworth et al. (2019).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/dez064](https://doi.org/10.1093/humrep/dez064)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Labels and denominators determine what a metric measures
> ==IVY also learns directly from videos using failed-transfer and discard-derived negatives. Laboratory hold-out evaluates transport across laboratories, while the mixed negative class defines the target being transported. Recording both dimensions distinguishes generalization to a new setting from prognosis among embryos with observed transfer outcomes [@EE080].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict embryo viability directly from time-lapse sequences. | EE080-B0013 EE080-B0016 |
| **Inputs** | Unannotated embryo-development videos. | EE080-B0012 EE080-B0016 |
| **Prediction time** | Before transfer/discard after available video sequence. | EE080-B0007 EE080-B0009 |
| **Analysis unit** | Embryo nested in cycle, patient and laboratory. | EE080-B0010 EE080-B0013 |
| **Method** | IVY deep video network trained from random initialization. | EE080-B0016 EE080-B0017 EE080-B0018 |
| **Supervision / labels** | Fetal heartbeat positives; negatives combine failed transfer and discarded abnormal or poor-quality embryos. | EE080-B0014 |
| **Outcome** | Composite viability label, not exclusively transferred-embryo pregnancy. | EE080-B0013 EE080-B0014 |
| **Sample sizes** | {"binary_labeled_embryos": 8836, "treatment_cycles": 1835, "patients": 1648, "laboratories": 8, "countries": 4, "fold_sizes": [1767, 1767, 1767, 1767, 1768]} | EE080-B0007 EE080-B0010 EE080-B0013 EE080-B0027 |
| **Splitting** | 8836 embryos assessed with 80/20 partitions and five folds; additional leave-one-laboratory-out validation across eight labs. | EE080-B0015 EE080-B0021 EE080-B0022 |
| **Validation** | Internal and laboratory-held-out AUROC; heterogeneous negative labels affect interpretation. | EE080-B0027 EE080-B0028 |

## Source-linked excerpts
- [EE080-B0009] ==The dataset included all embryos cultured in participating time-lapse incubators, including abnormal, aneuploid, discarded, fresh, frozen, and donor-oocyte embryos.==
- [EE080-B0014] ==The negative class combined failed transferred embryos with embryos discarded for abnormal fertilization, gross morphology, or PGT-detected aneuploidy.==
- [EE080-B0021] ==Five-fold stratified cross-validation randomly partitioned the entire labeled dataset and reported the mean AUC across five training-test runs.==
- [EE080-B0027] ==Retained Table III reports fold AUCs from 0.92 to 0.94 and a mean AUC of 0.93.==
- [EE080-B0039] ==The discussion states that embryo ranking is unlikely to alter cumulative pregnancy probability from a cohort, though it could shorten time to pregnancy by selecting the most promising embryo first.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*