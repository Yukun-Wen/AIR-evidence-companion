# EE026 — Automatic ploidy prediction and quality assessment of human blastocysts using time-lapse imaging.

**Rajendran, Brendel, Barnes et al. (2024).** *Nature communications*. DOI: [10.1038/s41467-024-51823-7](https://doi.org/10.1038/s41467-024-51823-7)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE026.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==BELA derives a blastocyst score through multitask bidirectional LSTM processing, then combines it with age in logistic ploidy prediction. Its evaluation varies by age and aneuploidy contrast, with mosaics excluded [@EE026]. A multistage live-birth system also joins image and clinical information, using cohorts that include development-contributing clinics and a prospective nonrandomized selection comparison [@EE028]. Its inconsistent modality descriptions leave the exact fusion configuration uncertain. Together, these examples connect the fused output to three design choices: component inputs, clinical population and the role of the score in selection.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict euploid versus aneuploid/complex-aneuploid status via learned blastocyst grading. | EE026-B0031 |
| **Inputs** | Day-5 time-lapse frames 96–112 hpi, maternal age, learned morphology scores. | EE026-B0031 EE026-B0033 |
| **Prediction time** | After completion of 96–112 hpi observation window, before genetic result in intended use. | EE026-B0031 |
| **Analysis unit** | Embryo time-lapse sequence; siblings treated independently in source. | EE026-B0023 |
| **Method** | BELA/STORK-V: VGG16 frame features, multitask BiLSTM grading, then logistic ploidy classifier with age. | EE026-B0031 EE026-B0033 |
| **Supervision / labels** | Embryologist blastocyst/component grades for intermediate targets; TE-biopsy NGS PGT-A for ploidy. | EE026-B0024 EE026-B0033 |
| **Outcome** | Euploid versus all aneuploid or complex aneuploid; intermediate grading MAE. | EE026-B0031 EE026-B0033 |
| **Sample sizes** | {"WCM_Embryoscope_sequences": 1998, "WCM_Embryoscope_patients": 498, "WCM_eligible_sequences": 1684, "WCM_Embryoscope_plus_sequences": 841, "Spain_sequences": 543, "Florida_sequences": 869} | EE026-B0009 EE026-B0023 EE026-B0031 |
| **Splitting** | 70/30 embryo split in eligible WCM dataset; four-fold training; independent samples regardless of parent. WCM newer-device and external Spain/Florida evaluation. | EE026-B0023 EE026-B0031 |
| **Validation** | Internal, temporal/device and external-center accuracy/AUROC/precision/recall; mosaics and missing labels/features excluded. | EE026-B0031 EE026-B0035 |

## Source-linked excerpts
- [EE026-B0008] ==The study used two WCM datasets and external datasets from Spain and Florida, with PGT-A as the ploidy reference.==
- [EE026-B0010] ==BELA combines a multitask time-lapse model-derived blastocyst score with maternal age in logistic ploidy classifiers.==
- [EE026-B0012] ==WCM AUC was 0.76 for euploid versus aneuploid and 0.826 for euploid versus complex aneuploid when maternal age was included.==
- [EE026-B0021] ==Limitations include modest training size, missing clinical covariates, subjective intermediary scores, excluded mosaics, platform variability, and dependence on time-lapse equipment.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*