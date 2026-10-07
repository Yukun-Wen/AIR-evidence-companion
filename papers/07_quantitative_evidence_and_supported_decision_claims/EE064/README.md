# EE064 — Using deep learning to predict the outcome of live birth from more than 10,000 embryo data.

**Huang, Zheng, Ma et al. (2022).** *BMC pregnancy and childbirth*. DOI: [10.1186/s12884-021-04373-5](https://doi.org/10.1186/s12884-021-04373-5)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** see EE064.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Labels and denominators determine what a metric measures
> ==A separate ResNet-like live-birth study combines failed transfers and discarded embryos in its negative class, making its AUC a measure of separation in that mixed label population. Conflicting cross-validation fold totals and analyzed counts leave the evaluation denominator uncertain [@EE064].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live-birth-labelled embryo outcome from blastocyst images. | EE064-B0015 |
| **Inputs** | Time-lapse-derived static embryo frames captured 105–125 h after fertilization, resized to 224×224. | EE064-B0019 EE064-B0035 |
| **Prediction time** | 105–125 h post-fertilization, blastocyst stage; not full early-development video. | EE064-B0035 |
| **Analysis unit** | Embryo image/sample nested in treatment; number of frames per embryo unclear. | EE064-B0010 EE064-B0019 |
| **Method** | Custom deep residual CNN, seven convolution modules plus dense layers, binary cross-entropy; trained from scratch with positive oversampling. | EE064-B0016 EE064-B0018 EE064-B0021 |
| **Supervision / labels** | Live birth confirmed by parental telephone follow-up; negative class also includes discarded abnormal, failed-fertilization and aneuploid embryos. | EE064-B0011 EE064-B0014 |
| **Outcome** | Composite negative versus live birth; distinguish from live birth discrimination only among transferred embryos. | EE064-B0011 |
| **Sample sizes** | {"source_embryos": 33738, "eligible_embryos_text": 15434, "five_fold_table_counts": [3812, 3812, 3811, 3811, 3811], "five_fold_table_sum": 19057, "time_lapse_cycles": 5913, "fresh_cycles_included": 3382, "frozen_transfer_cycles_included": 3270} | EE064-B0008 EE064-B0010 EE064-B0020 EE064-B0025 |
| **Splitting** | Random 5:1:1 train/validation/test and separate stratified five-fold evaluation; augmentation after split; patient grouping not described. | EE064-B0019 EE064-B0024 |
| **Validation** | Internal five-fold and holdout AUROC; no external validation reported. | EE064-B0027 EE064-B0029 EE064-B0030 |

## Source-linked excerpts
- [EE064-B0010] ==Of 33,738 embryos, pending stored embryos were excluded and 15,434 positive/negative samples were used, restricted to single-blastocyst transfer records plus discarded embryos in the labeled pool.==
- [EE064-B0011] ==The original table defines negatives as failed live birth or embryos discarded for abnormal fertilization, grossly abnormal morphology, or PGT-detected aneuploidy, unlike the positive live-birth-after-transfer class.==
- [EE064-B0024] ==Evaluation used random 5:1:1 train/validation/test splitting and five-fold cross-validation; patient-grouped separation is not stated.==
- [EE064-B0029] ==The five-fold analysis reported a mean AUC of 0.968, with individual folds from 0.960 to 0.976.==
- [EE064-B0036] ==The authors acknowledge that live birth depends on patient and treatment variables absent from the model and that their cohort was young with favorable ovarian reserve.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*