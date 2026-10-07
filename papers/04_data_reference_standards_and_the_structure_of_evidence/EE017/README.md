# EE017 — Deep-learning model for embryo selection using time-lapse imaging of matched high-quality embryos.

**Boucret, Chabrun, Boguenet et al. (2025).** *Scientific reports*. DOI: [10.1038/s41598-025-10531-y](https://doi.org/10.1038/s41598-025-10531-y)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Computational methods

**PDF:** see EE017.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE015,EE017,EQF01]==

> **§ Computational methods** : Direct video encoders and shared representations
> ==Another pipeline combines YOLO cropping, SimCLR image pretraining, LSTM sequence encoding and an XGBoost pregnancy predictor. Its external tests evaluate stage encoding; cross-validation evaluates the downstream pregnancy classifier in selected good-quality transferred embryos. The staged design permits representation quality and outcome discrimination to be analyzed at their respective evaluation levels [@EE017].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict pregnancy using matched high-quality sibling embryo videos. | EE017-B0016 EE017-B0020 EE017-B0021 |
| **Inputs** | Cropped time-lapse sequences; one task additionally uses a previous sibling transfer outcome. | EE017-B0011 EE017-B0017 EE017-B0020 |
| **Prediction time** | Pre-transfer sequence assessment; paired task needs an earlier transfer outcome. | EE017-B0020 EE017-B0021 |
| **Analysis unit** | Embryo video/pair nested in patient and stimulation cohort. | EE017-B0016 EE017-B0017 EE017-B0024 |
| **Method** | SimCLR VGG16/ResNet 18, Siamese LSTM and Euclidean/XGBoost downstream prediction. | EE017-B0012 EE017-B0017 EE017-B0021 |
| **Supervision / labels** | Nearby-frame self-supervision and same/different pregnancy-outcome pair labels. | EE017-B0012 EE017-B0016 |
| **Outcome** | Fetal heartbeat five weeks after transfer. | EE017-B0009 EE017-B0042 |
| **Sample sizes** | {"initial_videos": 3419, "initial_patients": 504, "pretraining_embryos": 1580, "pretraining_patients": 460, "outcome_eligible_embryos": 829, "fine_tune_embryos": 209, "fine_tune_patients": 62, "validation_embryos": 620, "validation_patients": 312, "paired_validation_patients": 174, "single_validation_patients": 312, "external_stage_probe_frames": 1584} | EE017-B0014 EE017-B0024 |
| **Splitting** | Patient split for fine-tuning; ineligible training cases added to validation; pretraining uses all selected embryos. | EE017-B0014 EE017-B0016 EE017-B0024 |
| **Validation** | Pair bootstrap and repeated XGBoost CV; external stage probe is separate from clinical-outcome validation. | EE017-B0015 EE017-B0020 EE017-B0021 EE017-B0031 EE017-B0042 |

## Source-linked excerpts
- [EE017-B0016] ==Fine-tuning used patient-stratified training and validation, with paired embryos from cycles containing both positive and negative outcomes.==
- [EE017-B0024] ==The analysis used 1,580 embryos for pretraining, 209 for fine-tuning, and 620 in the validation cohort.==
- [EE017-B0031] ==The independent-outcome task reported AUC 0.64, F1 0.55, sensitivity 53.9%, specificity 68.1%, and Brier score 0.30.==
- [EE017-B0042] ==The authors cite small sample size, local retrospective validation, lack of live-birth outcome, and transfer-protocol assumptions as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*