# OOCYTE02 — Segmentation of mature human oocytes provides interpretable and improved blastocyst outcome predictions by a machine learning model

**Fjeldstad, Qi, Siddique et al. (2024).** *Scientific reports*. DOI: [10.1038/s41598-024-60901-1](https://doi.org/10.1038/s41598-024-60901-1)

**Role:** core · contrasts C01, C02, C03, C04 · workflow: Oocyte assessment

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Oocyte analysis ranges from compartment segmentation to developmental prognosis. Fjeldstad and colleagues combine segmented anatomy with clinical context to predict blastocyst development. Segmentation evaluates boundary agreement, whereas developmental prediction links those measurements to an outcome shaped jointly by oocyte, sperm and culture conditions [@OOCYTE02].==

> **§ Data, reference standards and the structure of evidence** : A hierarchy of observations
> ==Sample size has a separate meaning at each level. Fjeldstad's study reports 51,831 outcome-labelled oocyte images from 6,793 patients undergoing 8,089 ICSI cycles. Images describe computational training material, cycles describe treatment episodes, and patients define the clinical representation. Reporting all three counts makes the dependency structure explicit [@OOCYTE02].==

> **§ Data, reference standards and the structure of evidence** : Static images: acquisition is part of the input
> ==Preprocessing defines the model's observation function. Cropping suppresses background and can remove contextual cues. Resizing standardizes input dimensions and can suppress small structures. Orientation normalization simplifies the appearance distribution while changing any orientation-dependent signal. Comparing spatial methods therefore entails comparing the transformations applied to the source images. Fjeldstad's dataset combines images taken immediately before and after ICSI. The combined dataset therefore represents a mixed-time setting spanning the injection procedure. The pre-injection task is defined by images acquired before injection [@OOCYTE02].==

> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Assay-derived labels connect images to measured biological properties. McCallum links bright-field cell appearance to a continuous fluorescence-derived DNA-fragmentation measure. Leung uses experimental zona-binding categories and then examines clinical fertilization associations. Continuous molecular prediction and functional classification have distinct targets, with the latter also supporting a separate sample-level analysis [@SPERM02,SPERM03]. Developmental labels specify an endpoint and observation window. The oocyte-development study predicts subsequent blastocyst development, an outcome shaped by the oocyte, sperm and culture environment. Its discrimination measures prediction of the combined developmental outcome [@OOCYTE02].==

> **§ Data, reference standards and the structure of evidence** : Partitioning, generalization and provenance
> ==Fjeldstad explicitly partitions patients for the outcome model. Hanassab uses first treatment cycles and nested leave-one-clinic-out validation, separating hyperparameter tuning from outer-clinic evaluation. McCallum reports both random image partitions and held-out-donor experiments. These designs address distinct forms of sample novelty and retain their evaluation levels in the synthesis [@OOCYTE02,STIM05,SPERM02].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@ER044,OOCYTE02]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Segment oocyte compartments and predict blastocyst competence using interpretable morphometry |  |
| **Inputs** | Denuded human MI/MII images for segmentation; MII images plus oocyte age and cohort MII count for outcome model |  |
| **Prediction time** | Images immediately before or after ICSI; timing is mixed |  |
| **Analysis unit** | Oocyte nested in cycle/patient; compartment pixels |  |
| **Method** | FCBFormer segmentation; LightGBM morphometry classifier with SHAP; ConvFormer/LightGBM ensemble |  |
| **Supervision / labels** | Embryologist masks; blastocyst ≥1CC at days 5–7 |  |
| **Outcome** | Compartment masks; binary blastocyst development |  |
| **Sample sizes** | {"segmentation_images": 7412, "segmentation_train": 4453, "segmentation_validation": 1476, "segmentation_test": 1483, "outcome_images": 51831, "patients": 6793, "ICSI_cycles": 8089, "outcome_train": 29262, "outcome_validation": 10812, "outcome_test": 11757, "external_oocytes": 9346, "external_patients": 909} |  |
| **Splitting** | Outcome dataset explicitly patient-level ~60/20/20; segmentation patient isolation not_assessed |  |
| **Validation** | Held-out patient test; independent Spanish clinic external cohort |  |

## Source-linked excerpts
- [OOCYTE02-B0031] ==The pipeline segmented oocyte compartments and derived morphometric features from thousands of ICSI oocyte images, with patient-level development splits and external-clinic evaluation.==
- [OOCYTE02-B0008] ==Blastocyst prediction was modest: the ensemble reached about AUC 0.67 internally and 0.65 externally, rather than demonstrating treatment benefit.==
- [OOCYTE02-B0019] ==Multiple oocytes and cycles per patient create clustering concerns, and all authors reported employment, equity or founder relationships with the proprietary system developer.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*