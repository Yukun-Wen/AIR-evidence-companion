# SPERM06 — Morphology Classification of Live Unstained Human Sperm Using Ensemble Deep Learning

**Shahali, Murshed, Spencer et al. (2024).** *Advanced Intelligent Systems*. DOI: [10.1002/aisy.202400141](https://doi.org/10.1002/aisy.202400141)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Data, reference standards and the structure of evidence, Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EC079,SPERM06]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Stained-sperm resources support comparisons of morphology labels. SMD/MSS uses modified David categories with multiple expert assessments; its evaluated task is smear-image analysis, with motile-sperm ICSI proposed as a future application. MC-HSH evaluates SCIAN expert-agreement subsets and HuSHeM, exposing the effect of annotation selection on the tested population. Augmentation expands the image material within the source donors. Resource description, annotation agreement and validation design thus capture separate properties [@EC020,EC082]. The Monash live, unstained sperm resource provides a second form of reuse: whole-cell morphology labels support classification, while a later report selects 93 normal full-agreement images and adds five-part segmentation masks. These reports share image material while changing labels and evaluated tasks [@SPERM06,EC079].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==In the figure caption: Ten documented resource links across five components. Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015 — Ten documented resource links across five components. Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015==

> **§ Computational methods** : End-to-end appearance models and transfer learning
> ==A whole-cell sperm classifier illustrates score-level ensembling. DenseNet-169, DenseNet-201, ResNet-34 and Inception-V3 each produce a normal-morphology score from an unstained cell image. A binary meta-classifier combines the four scores, learning how their predictions contribute to the final decision. The reference requires normal head, midpiece and tail morphology together. This construction expands the anatomical target beyond the head while keeping the computational roles separate: the backbones encode appearance and the meta-classifier combines their judgments [@SPERM06].==

> **§ Quantitative evidence and supported decision claims** : Labels and denominators determine what a metric measures
> ==Expert agreement also defines an evaluation population. In whole-cell sperm morphology, three experts fully agreed on 355 of 2,254 images and at least two agreed on 1,544, including the full-agreement images. Separately fitted ensembles achieved held-out accuracy of 94% under full agreement and 79% on the 309-image majority-agreement test set, with corresponding AUCs of 0.96 and 0.83. These results compare two label-defined training and evaluation populations. The images came from three donors, and random 80/20 image partitions tested new images within that acquisition cohort. Thus agreement policy and biological replication supply two distinct coordinates for interpreting the reported accuracy [@SPERM06].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Detect sperm cells and classify normal versus abnormal whole-cell morphology in live unstained human sperm images. | SPERM06-H0072 SPERM06-H0075 SPERM06-H0078 |
| **Inputs** | DIC microscopy images of unstained sperm at1000×, cropped to800×800 whole-cell images; lower-resolution copies used for robustness tests. Separate YOLOv3 detection development uses181 field images at200×/400×/600×. | SPERM06-H0075 SPERM06-H0076 SPERM06-H0103 SPERM06-H0105 |
| **Prediction time** | During ex-vivo live-sperm morphology assessment, before any hypothesized use of the assessed cell for ICSI; treatment outcome prediction is not evaluated. | SPERM06-H0068 SPERM06-H0072 SPERM06-H0096 SPERM06-H0100 |
| **Analysis unit** | Individual sperm-cell image nested in technical/biological replicate and donor; six biological/eight technical replicates arise from three donors. | SPERM06-H0075 SPERM06-H0103 SPERM06-H0105 |
| **Method** | YOLOv3 locates/crops sperm; optimized DenseNet-169, DenseNet-201, ResNet-34 and Inception-v3 base classifiers feed concatenated class-probability scores to a binary meta-classifier. Optuna selects hyperparameters; augmentation and normal-class oversampling apply to training. | SPERM06-H0078 SPERM06-H0079 SPERM06-H0109 SPERM06-H0111 |
| **Supervision / labels** | Three blinded andrology experts label head, midpiece and tail normal/abnormal. Whole cell is normal only when all three parts are normal. Full agreement, partial agreement (≥2 experts), disagreement and unlabelled subsets are retained separately. | SPERM06-H0075 SPERM06-H0076 SPERM06-H0107 |
| **Outcome** | Detection and expert-morphology classification; confidence on disagreement/unlabelled images has no independent correctness reference. Fertilization, embryo development and live birth are not measured as model endpoints. | SPERM06-H0081 SPERM06-H0083 SPERM06-H0087 SPERM06-H0091 SPERM06-H0100 |
| **Sample sizes** | {"donors": 3, "biological_replicates": 6, "technical_replicates": 8, "sperm_cell_images": 2254, "full_agreement_images": 355, "partial_agreement_images_including_full": 1544, "disagreement_images": 562, "not_labelled_images": 148, "detector_field_images": 181, "detector_training_images": 145, "detector_validation_images": 9, "detector_test_images": 27, "partial_agreement_test_images": 309} | SPERM06-H0075 SPERM06-H0076 SPERM06-H0087 SPERM06-H0103 SPERM06-H0105 SPERM06-H0107 |
| **Splitting** | Detection images randomly split145/9/27. Morphology classifiers use random80/20 image splits separately for the consensus datasets; donor/replicate grouping is not established. The full-agreement subset is nested within partial agreement and is not an independent cohort. | SPERM06-H0079 SPERM06-H0105 SPERM06-H0109 SPERM06-H0111 |
| **Validation** | Internal held-out image classification: full agreement94%accuracy and AUROC0.96; partial agreement79%accuracy and AUROC0.83. Base-model, input-resolution and confidence analyses share the underlying donor/image resource; no new-donor/centre external test is established. | SPERM06-H0081 SPERM06-H0083 SPERM06-H0085 SPERM06-H0087 SPERM06-H0089 SPERM06-H0091 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*