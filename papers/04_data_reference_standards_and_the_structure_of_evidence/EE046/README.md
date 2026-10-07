# EE046 — An annotated human blastocyst dataset to benchmark deep learning architectures for in vitro fertilization.

**Kromp, Wagner, Balaban et al. (2023).** *Scientific data*. DOI: [10.1038/s41597-023-02182-3](https://doi.org/10.1038/s41597-023-02182-3)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Learning objectives and the interpretation of model outputs

**PDF:** see EE046.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Expert morphology is an operational reference defined by a grading system and annotators. SCIAN expert-agreement subsets select images with concordant assessments, while the annotated blastocyst benchmark retains disagreement and consensus labels. These resources support different evaluations of grading, especially for ambiguous images [@EC082,EE046].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE046,EQF01]==

> **§ Learning objectives and the interpretation of model outputs** : A task-indexed metric catalogue
> ==12 Comparing IVF methods requires a common prediction question and a specified evaluation population. Available information and labels define the question; biological hierarchy and validation define the tested population; policy evaluation measures the consequences of using the output.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Release a blastocyst dataset and benchmark Gardner grading. | EE046-B0015 EE046-B0022 |
| **Inputs** | Static blastocyst microscopy images. | EE046-B0008 |
| **Prediction time** | Blastocyst assessment before transfer or cryopreservation. | EE046-B0007 EE046-B0008 |
| **Analysis unit** | Blastocyst image linked to patient and transferred-subset outcomes. | EE046-B0006 EE046-B0009 |
| **Method** | Xception, DeiT and Swin with SWA-G weight averaging; separate grading tasks. | EE046-B0017 |
| **Supervision / labels** | Single-expert silver training labels and refined consensus gold test labels. | EE046-B0012 EE046-B0013 |
| **Outcome** | Expansion, ICM and TE grades; clinical outcomes supplied but not the benchmark target. | EE046-B0009 EE046-B0017 EE046-B0023 |
| **Sample sizes** | {"blastocysts": 2344, "patients": 837, "gold_test_images": 300, "silver_train_images_derived": 2044, "fresh_transferred_images": 752, "consortium_embryologists": 11, "routine_experts_after_filter_including_Gardner_expert": 7} | EE046-B0006 EE046-B0009 EE046-B0012 EE046-B0013 |
| **Splitting** | Class-constrained random 300-image test; remaining 2044 images for training; patient disjointness unstated. | EE046-B0012 |
| **Validation** | Fixed gold-label test accuracy, weighted precision/recall/F1 and kappa. | EE046-B0017 EE046-B0020 EE046-B0022 EE046-B0023 |

## Source-linked excerpts
- [EE046-B0006] ==The dataset contains 2,344 blastocysts from 837 patients, establishing the independent-patient denominator behind the image count.==
- [EE046-B0012] ==A senior expert labeled all images; a 300-image test set was additionally rated by an international 11-embryologist consortium, with at least five ratings per image.==
- [EE046-B0013] ==The reference process excluded five annotators with less than 0.5 accuracy against the senior expert and resolved 89 no-majority cases by re-annotation and consensus.==
- [EE046-B0015] ==The 2,344 PNG images and training, test and clinical annotation files are hosted at Figshare; the cited resource is version 3, DOI 10.6084/m9.figshare.20123153.v3.==
- [EE046-B0023] ==On the internal test set, the best expansion baseline had F1 0.84, while model F1 scores for inner-cell mass and trophectoderm were 0.52-0.65 and 0.51-0.56, below the expert averages.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*