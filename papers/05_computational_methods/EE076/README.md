# EE076 — Development of an artificial intelligence-based assessment model for prediction of embryo viability using static images captured by optical light microscopy during IVF.

**VerMilyea, Hall, Diakiw et al. (2020).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/deaa013](https://doi.org/10.1093/humrep/deaa013)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : End-to-end appearance models and transfer learning
> ==An eight-network ResNet/DenseNet ensemble processes whole and zona-masked blastocyst images. Blind evaluation combines contributing-clinic and unseen-clinic datasets, while embryologist comparisons use a graded subset and converted morphology thresholds. Representation ensembling and comparator construction both affect the reported contrast [@EE076].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict fetal-heartbeat embryo viability from static day-5 microscopy. | EE076-B0009 |
| **Inputs** | Standard optical-microscope day-5 image, full embryo and zona-masked versions. | EE076-B0010 EE076-B0054 |
| **Prediction time** | Day 5 before PGS biopsy or freezing. | EE076-B0010 |
| **Analysis unit** | Single-transferred embryo image with clinical pregnancy outcome; repeated patient cycles not detailed. | EE076-B0009 |
| **Method** | Life Whisperer ensemble of eight ResNet-152/DenseNet-161 models, four zona and four full-embryo branches. | EE076-B0054 EE076-B0055 EE076-B0058 |
| **Supervision / labels** | Fetal heartbeat at first ultrasound, recorded after single day-5 transfer. | EE076-B0009 EE076-B0010 |
| **Outcome** | Binary heartbeat/viability accuracy, sensitivity, specificity and score agreement with converted embryologist grades. | EE076-B0013 EE076-B0063 |
| **Sample sizes** | {"total_images": 8886, "clinics": 11, "countries": 3, "pilot_images": 5282, "pilot_training": 3892, "pilot_validation": 390, "pilot_blind_test": 1000, "pivotal_images": 3604, "pivotal_training": 1744, "pivotal_validation": 193, "pivotal_blind_test": 1667} | EE076-B0069 EE076-B0070 EE076-B0071 |
| **Splitting** | Stratified image train/validation/blind splits; pivotal blind set1 same clinics and sets2/3 entirely new clinics. | EE076-B0023 EE076-B0070 |
| **Validation** | Internal blind and external-clinic blind tests; embryologist comparisons only subsets with grades. | EE076-B0068 EE076-B0070 EE076-B0072 |

## Source-linked excerpts
- [EE076-B0009] ==The retrospective study drew consecutive single Day-5 transfers with fetal-heart outcomes from 11 clinics in the USA, Australia, and New Zealand between 2011 and 2018.==
- [EE076-B0054] ==The final system was an ensemble of eight deep networks, split between zona-masked and full-embryo models.==
- [EE076-B0070] ==The pivotal phase used 1,744 training images, 193 validation images, and 1,667 blind-test images; two blind sets came from clinics that contributed no training data.==
- [EE076-B0008] ==Retained Table II reports combined blind-test sensitivity 70.1%, specificity 60.5%, and overall accuracy 64.3%, with embryologist comparisons available for only two test sets.==
- [EE076-B0092] ==The discussion limits the model to Day-5 images, notes fetal heartbeat is not live birth, and calls for prospective assessment of real-world use.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*