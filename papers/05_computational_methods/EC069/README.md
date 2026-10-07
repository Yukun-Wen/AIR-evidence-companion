# EC069 — Improved clinical pregnancy rates in natural frozen-thawed embryo transfer cycles with machine learning ovulation prediction: insights from a retrospective cohort study.

**Luz, Hourvitz, Moran et al. (2024).** *Scientific reports*. DOI: [10.1038/s41598-024-80356-8](https://doi.org/10.1038/s41598-024-80356-8)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC069.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Monitoring sequences and treatment feedback
> ==Natural-cycle transfer monitoring supplies a classification example. XGBoost predicts relative ovulation classes from hormones and ultrasound, using several derived observations per cycle. A later retrospective comparison examines pregnancy outcomes under physician timing and model-consistent timing. The two analyses address monitoring classification and timing-associated outcomes, with the cycle as the shared biological unit [@EC069].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify ovulation timing relative to latest test day to support natural FET timing. | EC069-B0046 EC069-B0048 |
| **Inputs** | Baseline characteristics plus up to two days of LH, progesterone, estradiol, follicle size and endometrial thickness; 20 selected features. | EC069-B0034 EC069-B0048 EC069-B0049 |
| **Prediction time** | Latest monitoring test day; output five relative ovulation-day classes. | EC069-B0046 |
| **Analysis unit** | Test-day instance nested within cycle and patient. | EC069-B0044 EC069-B0047 |
| **Method** | XGBoost, forward sequential feature selection, grid-search tuning and one-versus-rest calibration. | EC069-B0049 |
| **Supervision / labels** | Three-REI majority ovulation labels; separate documented follicular rupture plus LH-surge reference. | EC069-B0037 EC069-B0039 |
| **Outcome** | Relative ovulation class; retrospective clinical pregnancy by concordance with suggested transfer day. | EC069-B0046 EC069-B0041 |
| **Sample sizes** | {"REI_cycles": 500, "train_cycles": 309, "validation_cycles": 90, "test_cycles": 101, "REI_instances": 3181, "documented_cycles": 101, "documented_instances": 591, "later_pregnancy_cycles": 515} | EC069-B0038 EC069-B0041 |
| **Splitting** | Patient-ID split into train/validation/test; after tuning fit train+validation; nonoverlapping documented and later outcome cohorts. | EC069-B0047 EC069-B0049 |
| **Validation** | Accuracy and calibration against REI/documented ovulation; retrospective adjusted matched-vs-mismatched pregnancy association. | EC069-B0006 EC069-B0009 EC069-B0051 |

## Source-linked excerpts
- [EC069-B0009] ==The model achieved about 93% accuracy against both the expert-consensus and selected documented-ovulation test sets, with poorer performance in sparse later-day classes.==
- [EC069-B0015] ==Clinical pregnancy was 34.6% in matched cycles and 25.9% in mismatched cycles in the retrospective outcome cohort.==
- [EC069-B0037] ==The development dataset was split by patient and ovulation ground truth came from majority decisions by three experienced reproductive endocrinologists.==
- [EC069-B0041] ==The clinical analysis retrospectively grouped later cycles by whether physician-selected timing agreed with a model recommendation; the model did not assign treatment.==
- [EC069-B0029] ==The authors acknowledge nonrandom reference data, reliance on expert opinion, retrospective outcome analysis, and need for randomized and external validation.==
- [EC069-B0058] ==Several authors were shareholders, board members, or employees of FertilAI.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*