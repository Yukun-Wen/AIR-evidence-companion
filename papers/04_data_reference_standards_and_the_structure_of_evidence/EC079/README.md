# EC079 — Deep Learning Models for Multi-Part Morphological Segmentation and Evaluation of Live Unstained Human Sperm.

**Lei, Saadat, Hassani et al. (2025).** *Sensors (Basel, Switzerland)*. DOI: [10.3390/s25103093](https://doi.org/10.3390/s25103093)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Data, reference standards and the structure of evidence, Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Expert morphology is an operational reference defined by a grading system and annotators. SCIAN expert-agreement subsets select images with concordant assessments, while the annotated blastocyst benchmark retains disagreement and consensus labels. These resources support different evaluations of grading, especially for ambiguous images [@EC082,EE046]. Segmentation labels introduce boundary and size uncertainty. Different anatomical compartments occupy different fractions of an image; errors in a thin boundary or rare region can be hidden by an aggregate overlap score. Component-specific metrics and the annotation-selected population therefore belong in the evidence record [@EC079,EE006].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EC079,SPERM06]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Stained-sperm resources support comparisons of morphology labels. SMD/MSS uses modified David categories with multiple expert assessments; its evaluated task is smear-image analysis, with motile-sperm ICSI proposed as a future application. MC-HSH evaluates SCIAN expert-agreement subsets and HuSHeM, exposing the effect of annotation selection on the tested population. Augmentation expands the image material within the source donors. Resource description, annotation agreement and validation design thus capture separate properties [@EC020,EC082]. The Monash live, unstained sperm resource provides a second form of reuse: whole-cell morphology labels support classification, while a later report selects 93 normal full-agreement images and adds five-part segmentation masks. These reports share image material while changing labels and evaluated tasks [@SPERM06,EC079].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==In the figure caption: Ten documented resource links across five components. Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015 — Ten documented resource links across five components. Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015==

> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Formally, a segmentation system produces a mask $M=g_ (I)$ from image $I$. A structured predictor estimates $ y=h_ ( (M),z)$, where $ $ computes morphometric descriptors and $z$ contains available clinical covariates. This factorization supports two linked assessments: anatomical mask agreement and the predictive value of the derived measurements. Downstream evaluation tests how changes in segmentation affect the final target. A live-sperm study segments head, acrosome, nucleus, neck and tail, with different architectures leading by compartment. The small evaluation subset contains only normal, expert-agreed specimens; training/validation allocation is unspecified. These compartment-level results describe the structures available downstream [@EC079].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Segment five parts of live unstained human sperm. | EC079-B0006 EC079-B0015 |
| **Inputs** | Images with head, acrosome, nucleus, midpiece and tail masks. | EC079-B0015 |
| **Prediction time** | Laboratory microscopy; exact clinical selection timestamp not specified. | EC079-B0006 EC079-B0015 |
| **Analysis unit** | Sperm image and region pixels. | EC079-B0015 EC079-B0022 |
| **Method** | Mask R-CNN, U-Net, YOLOv 8 and YOLO11. | EC079-B0025 |
| **Supervision / labels** | Expert masks from images unanimously judged morphologically normal. | EC079-B0015 |
| **Outcome** | Pixel segmentation metrics, not reproductive outcomes. | EC079-B0022 EC079-B0023 |
| **Sample sizes** | {"normal_sperm_images": 93, "expert_morphologists": 3, "patient_donor_count": "not reported in dataset paragraph"} | EC079-B0015 |
| **Splitting** | Source reports 20% training and 80% validation; donor grouping not stated. | EC079-B0015 |
| **Validation** | Internal fixed-split mean IoU, Dice, precision, recall and F1. | EC079-B0022 EC079-B0023 EC079-B0025 EC079-B0041 |

## Source-linked excerpts
- [EC079-B0002] ==The introduction identifies manual sperm selection as an operator-dependent step in ICSI and motivates automated assistance.==
- [EC079-B0006] ==The stated objective is segmentation of live unstained human sperm parts to improve CASA and sperm selection in ICSI.==
- [EC079-B0015] ==The reused dataset subset contains 93 images of normal live unstained sperm with full agreement from three experts, and the paper reports a 20% training/80% validation image split.==
- [EC079-B0029] ==For acrosome segmentation, mean IoU ranged from 69.20% for U-Net to 76.41% for Mask R-CNN.==
- [EC079-B0035] ==Tail segmentation reversed the ranking seen for compact structures, with U-Net best and Mask R-CNN worst.==
- [EC079-B0041] ==The authors acknowledge that the 93-image resource and cross-dataset differences limit robustness and call for larger datasets and cross-validation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*