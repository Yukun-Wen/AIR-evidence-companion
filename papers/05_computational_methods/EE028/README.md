# EE028 — Artificial intelligence system for outcome evaluations of human in vitro fertilization-derived embryos.

**Sun, Li, Zeng et al. (2024).** *Chinese medical journal*. DOI: [10.1097/cm9.0000000000003162](https://doi.org/10.1097/cm9.0000000000003162)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE028.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==BELA derives a blastocyst score through multitask bidirectional LSTM processing, then combines it with age in logistic ploidy prediction. Its evaluation varies by age and aneuploidy contrast, with mosaics excluded [@EE026]. A multistage live-birth system also joins image and clinical information, using cohorts that include development-contributing clinics and a prospective nonrandomized selection comparison [@EE028]. Its inconsistent modality descriptions leave the exact fusion configuration uncertain. Together, these examples connect the fused output to three design choices: component inputs, clinical population and the role of the score in selection.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict morphology, blastocyst formation, ploidy and transfer-level live birth. | EE028-B0024 EE028-B0026 |
| **Inputs** | Day 1/3 images, blastocyst images, videos and clinical metadata. | EE028-B0009 EE028-B0012 EE028-B0015 EE028-B0024 |
| **Prediction time** | Task-specific Day 1/3 or blastocyst assessment before transfer. | EE028-B0009 EE028-B0012 EE028-B0021 EE028-B0024 |
| **Analysis unit** | Embryo for morphology/ploidy; transfer involving one or more embryos for live birth. | EE028-B0021 EE028-B0042 |
| **Method** | U-Net crop, ResNet 50 multitask CNN, noisy-OR fusion,3D CNN and CNN-RNN aggregation. | EE028-B0018 EE028-B0019 EE028-B0020 EE028-B0021 EE028-B0026 |
| **Supervision / labels** | Manual morphology, formation, PGT-A and live-birth labels. | EE028-B0010 EE028-B0011 EE028-B0013 EE028-B0017 |
| **Outcome** | Task-specific morphology/formation/ploidy and live birth≥28 weeks. | EE028-B0014 EE028-B0017 EE028-B0026 |
| **Sample sizes** | {"development_internal_embryos": 15602, "development_internal_patients": 5468, "morphology_train": {"patients": 3272, "embryos": 9141}, "morphology_tune": {"patients": 1071, "embryos": 3130}, "morphology_internal": {"patients": 1125, "embryos": 3331}, "external_morphology1": {"patients": 393, "embryos": 407}, "external_morphology2": {"patients": 2410, "embryos": 3192}, "livebirth_training_patients": 4537, "ploidy_videos_reported": 418, "ploidy_pilot_embryos": 145} | EE028-B0023 EE028-B0025 EE028-B0026 EE028-B0037 |
| **Splitting** | 2010–2018 development with 75/25 training/tuning;2019–2023 validation at the same two institutions. | EE028-B0023 EE028-B0025 EE028-B0026 |
| **Validation** | Internal/later-cohort AUC and prospective-described pilot; selection-rate contrasts are not randomized efficacy evidence. | EE028-B0037 EE028-B0042 EE028-B0046 EE028-B0055 |

## Source-linked excerpts
- [EE028-B0026] ==The platform comprised four modules and was evaluated using historical development data plus two later external validation cohorts.==
- [EE028-B0037] ==In a prospective pilot of 145 embryos, combined video and metadata ploidy prediction reached AUC 0.805.==
- [EE028-B0042] ==The external live-birth cohort yielded AUCs of 0.647, 0.748, and 0.769 for metadata, image, and hybrid models.==
- [EE028-B0046] ==A 280-embryo comparison reported higher live-birth rates in AI-ranked subsets than the observed day-3 and day-5 baselines, without describing randomized AI assignment.==
- [EE028-B0055] ==The authors acknowledge confinement to a Chinese population and the need for validation across diverse populations and additional exposures.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*