# OOCYTE01 — An artificial intelligence tool predicts blastocyst development from static images of fresh mature oocytes

**Fjeldstad, Qi, Mercuri et al. (2024).** *Reproductive biomedicine online*. DOI: [10.1016/j.rbmo.2024.103842](https://doi.org/10.1016/j.rbmo.2024.103842)

**Role:** core · workflow: Oocyte assessment

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : End-to-end appearance models and transfer learning
> ==Static-oocyte forecasting combines localization, appearance learning and a later developmental label. One system crops fresh denuded MII-oocyte images with Faster R-CNN, normalizes contrast and fine-tunes ImageNet-pretrained EfficientNet-B7 models, combining four fold-trained models by soft voting. Its 7,807-image test yields blastocyst-development AUC 0.64 (95% CI, 0.62--0.65). A positive label requires a blastocyst grade of at least 1CC between days four and seven; negatives combine failed fertilization and failure to reach blastocyst by day seven. Prediction therefore starts from an already-retrieved mature oocyte and addresses its subsequent laboratory development, with image-level testing and unreported patient/retrieval grouping [@OOCYTE01].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict whether a fresh mature oocyte develops to a blastocyst after ICSI from a static oocyte image. | OOCYTE01-H0041 OOCYTE01-H0046 OOCYTE01-H0048 |
| **Inputs** | Single-plane JPEG images of fresh denuded MII oocytes under Hoffman modulation contrast at 200–400×; no age or clinical covariate is specified as a classifier input in the examined model description. | OOCYTE01-H0046 OOCYTE01-H0050 OOCYTE01-H0052 OOCYTE01-H0055 |
| **Prediction time** | At mature-oocyte imaging before the downstream fertilization/developmental label is observed; the exact image acquisition offset relative to ICSI is not uniformly specified in the examined main text. | OOCYTE01-H0041 OOCYTE01-H0046 OOCYTE01-H0048 |
| **Analysis unit** | Oocyte image nested within retrieval and patient/donor; images, retrievals and people are distinct sample levels. | OOCYTE01-H0043 OOCYTE01-H0044 OOCYTE01-H0046 OOCYTE01-H0049 |
| **Method** | Faster R-CNN crops oocytes, followed by contrast normalization/augmentation; ImageNet-pretrained EfficientNet-B7 is fine-tuned with weighted binary cross-entropy. Four training-fold models are combined by soft voting; comparator architecture selection and Bayesian hyperparameter search are described. | OOCYTE01-H0052 OOCYTE01-H0053 OOCYTE01-H0055 OOCYTE01-H0056 OOCYTE01-H0057 |
| **Supervision / labels** | Embryologist-derived blastocyst label: Gardner or modified Gardner grade ≥1CC between days4 and7 positive; failed fertilization or no blastocyst by day7 negative. | OOCYTE01-H0048 OOCYTE01-H0061 |
| **Outcome** | Blastocyst development after ICSI, with separate associations between oocyte scores and blastocyst quality; not live birth or intrinsic oocyte quality independent of sperm/laboratory effects. | OOCYTE01-H0048 OOCYTE01-H0064 OOCYTE01-H0084 |
| **Sample sizes** | {"development_images": 37133, "development_patients_and_donors": 5480, "development_retrievals": 6471, "development_clinics": 8, "training_images": 29326, "internal_test_images": 7807, "external_images": 12357, "external_patients_and_donors": 1391, "external_retrievals": 1449, "external_clinics": 2, "total_images": 49490} | OOCYTE01-H0043 OOCYTE01-H0044 OOCYTE01-H0046 OOCYTE01-H0047 OOCYTE01-H0049 OOCYTE01-H0050 |
| **Splitting** | 7,807 images set aside for testing and 29,326 for training; four-fold training/validation and soft-voting ensemble. Patient/retrieval separation across partitions is not established. Additional C1/C7 datasets are evaluated; C1 is also represented in development. | OOCYTE01-H0049 OOCYTE01-H0050 OOCYTE01-H0057 OOCYTE01-H0072 OOCYTE01-H0073 |
| **Validation** | Internal image test AUROC 0.64 (95% CI 0.62–0.65); additional 12,357-image C1/C7 evaluation AUROC 0.63 (0.62–0.64). Balanced accuracy, sensitivity, specificity and age/clinic/semen subgroups are reported. Additional new data are not wholly unseen-centre validation. | OOCYTE01-H0058 OOCYTE01-H0063 OOCYTE01-H0067 OOCYTE01-H0073 OOCYTE01-H0075 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*