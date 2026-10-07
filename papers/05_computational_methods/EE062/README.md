# EE062 — A novel system based on artificial intelligence for predicting blastocyst viability and visualizing the explanation.

**Enatsu, Miyatsuka, An et al. (2022).** *Reproductive medicine and biology*. DOI: [10.1002/rmb2.12443](https://doi.org/10.1002/rmb2.12443)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE062.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==FiTTE supplies ResNet18-derived image information and clinical variables to a random forest. The image-only model uses a holdout evaluation, whereas the complete-covariate ensemble uses cross-validation; their AUC difference is nonsignificant [@EE062]. The reported comparison thus combines an input change with an evaluation-design change. A shared set of patients and partitions would make the information contribution measurable, and transport testing would characterize its stability across settings.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict pregnancy and live birth directly from embryo images and compare clinical fusion. | EE062-B0007 EE062-B0012 |
| **Inputs** | Blastocyst images, optionally combined with maternal and clinical variables. | EE062-B0007 EE062-B0008 EE062-B0014 |
| **Prediction time** | Blastocyst assessment before transfer; exact availability of each clinical input needs verification. | EE062-B0008 EE062-B0010 |
| **Analysis unit** | Embryo image linked to patient. | EE062-B0007 EE062-B0014 |
| **Method** | FiTTE ResNet 18 and optional random-forest clinical fusion. | EE062-B0014 EE062-B0015 |
| **Supervision / labels** | Observed clinical-pregnancy and live-birth labels. | EE062-B0010 EE062-B0012 EE062-B0014 |
| **Outcome** | Clinical pregnancy requires positive hCG and intrauterine fetal heartbeat; live birth is a separate target. | EE062-B0010 EE062-B0012 |
| **Sample sizes** | {"images": 19342, "patients": 9961, "image_development_cycles": 17984, "clinical_complete_test_subset": 1358, "clinical_pregnancy_positive": 7717, "livebirth_cycles": 10643, "livebirth_train": 9091, "livebirth_test": 1552, "ensemble_train_example": 1223, "ensemble_test_example": 135} | EE062-B0007 EE062-B0008 EE062-B0014 EE062-B0016 |
| **Splitting** | 17984 image-development observations split 90/10;1358 clinical-complete holdout cases for pregnancy fusion; separate live-birth split. | EE062-B0014 EE062-B0016 |
| **Validation** | Internal image and combined-model comparison; ten-fold analysis of the clinical-complete subset. | EE062-B0012 EE062-B0016 EE062-B0019 EE062-B0031 |

## Source-linked excerpts
- [EE062-B0007] ==The retrospective cohort comprised 19,342 static Day-5 blastocyst images from 9,961 IVF patients at one clinic.==
- [EE062-B0014] ==ResNet18 processed embryo images; 17,984 cycles were used for training and 1,358 for testing, while the smaller ensemble required 10-fold cross-validation.==
- [EE062-B0019] ==Clinical-pregnancy accuracy increased from 59.8% for the Gardner control to 62.7% for images and 65.2% for the ensemble, with AUCs 0.68 and 0.71 and no significant ensemble-versus-image AUC difference.==
- [EE062-B0031] ==The authors identify static images, a mainly Japanese population, retrospective non-randomized design, limited sample size, and human transfer selection as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*