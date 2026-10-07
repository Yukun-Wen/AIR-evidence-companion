# EE059 — Development of an artificial intelligence model for predicting the likelihood of human embryo euploidy based on blastocyst images from multiple imaging systems during IVF.

**Diakiw, Hall, VerMilyea et al. (2022).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/deac131](https://doi.org/10.1093/humrep/deac131)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : End-to-end appearance models and transfer learning
> ==Static-image ensembles also predict PGT-A labels. A multiclinic study uses model-based data cleansing during development and reports cleansed and uncleansed blind tests. Cleansing changes population composition and class prevalence. Keeping both results identifies performance in the filtered set and the broader unfiltered population [@EE059].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict euploidy and assess cohort-ranking utility. | EE059-B0005 EE059-B0011 EE059-B0013 |
| **Inputs** | Single static blastocyst images. | EE059-B0005 EE059-B0017 EE059-B0057 EE059-B0058 |
| **Prediction time** | Day 5 before biopsy or transfer; additional analyses include Day 6/7. | EE059-B0005 |
| **Analysis unit** | Embryo image nested in patient and treatment cycle. | EE059-B0011 EE059-B0023 |
| **Method** | Life Whisperer Genetics CNN ensemble, knowledge distillation and uncertainty-based data cleansing. | EE059-B0017 EE059-B0019 EE059-B0021 EE059-B0022 EE059-B0024 EE059-B0026 |
| **Supervision / labels** | PGT-A euploid/non-euploid labels. | EE059-B0005 EE059-B0024 |
| **Outcome** | Ploidy prediction and simulated cohort selection. | EE059-B0008 EE059-B0046 |
| **Sample sizes** | {"initial_day5_images": 5050, "patients": 2438, "cycles": 2485, "cleansed_training_images": 3174, "cleansed_validation_images": 300, "blind_test_uncleansed": 1001, "blind_test_cleansed": 786, "external_India": {"images": 178, "patients": 31}, "external_Spain": {"images": 182, "patients": 63}, "external_Malaysia": {"images": 141, "patients": 65}} | EE059-B0022 EE059-B0023 EE059-B0055 EE059-B0057 EE059-B0058 |
| **Splitting** | Cleansed 3174 training/300 validation images; unfiltered 1001-image test, with 786 retained by filtering; additional external cohorts. | EE059-B0021 EE059-B0022 EE059-B0055 |
| **Validation** | Internal filtered and unfiltered AUC plus external observational cohorts and 100000 simulated selection cohorts. | EE059-B0011 EE059-B0022 EE059-B0044 EE059-B0055 EE059-B0057 EE059-B0058 |

## Source-linked excerpts
- [EE059-B0005] ==The study linked optical microscopy images from IVF embryos to PGT-A outcomes; Day-5 images were used for model development and prospectively collected data were reserved for double-blind evaluation.==
- [EE059-B0022] ==UDC produced cleansed training, validation, and test subsets and the authors explicitly note that prospective real-world sets were not cleansed.==
- [EE059-B0044] ==The uncleansed blind test achieved 65.3% accuracy, 74.6% sensitivity, 48.6% specificity, MCC 0.235, and ROC AUC 0.68; cleansing raised performance but was acknowledged as non-representative of routine use.==
- [EE059-B0048] ==In simulated cohorts the AI ranked a euploid embryo first in 82.4% of cohorts and exceeded random and two Gardner-based rankings.==
- [EE059-B0057] ==A prospectively collected Spanish GERI set yielded 65.4% accuracy, 97.3% sensitivity, and MCC 0.219, illustrating generalization with limited specificity.==
- [EE059-B0074] ==The conflict disclosure reports ownership, employment, patents, stock options, and an advisory role connected to the commercial technology.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*