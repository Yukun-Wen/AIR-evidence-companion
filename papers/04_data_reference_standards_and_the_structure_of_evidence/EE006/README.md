# EE006 — MiMics-Net: A Multimodal Interaction Network for Blastocyst Component Segmentation.

**Haider, Arsalan, Cho (2026).** *Diagnostics (Basel, Switzerland)*. DOI: [10.3390/diagnostics16040631](https://doi.org/10.3390/diagnostics16040631)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Computational methods

**PDF:** see EE006.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Expert morphology is an operational reference defined by a grading system and annotators. SCIAN expert-agreement subsets select images with concordant assessments, while the annotated blastocyst benchmark retains disagreement and consensus labels. These resources support different evaluations of grading, especially for ambiguous images [@EC082,EE046]. Segmentation labels introduce boundary and size uncertainty. Different anatomical compartments occupy different fractions of an image; errors in a thin boundary or rare region can be hidden by an aggregate overlap score. Component-specific metrics and the annotation-selected population therefore belong in the evidence record [@EC079,EE006].==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE006,EE019,EQF01]==

> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==A live-sperm study segments head, acrosome, nucleus, neck and tail, with different architectures leading by compartment. The small evaluation subset contains only normal, expert-agreed specimens; training/validation allocation is unspecified. These compartment-level results describe the structures available downstream [@EC079]. MiMics-Net derives intensity, local-binary-pattern and Gabor-orientation channels from one microscopy image. Parallel grouped convolutions and pointwise fusion precede spatial refinement. This image-derived fusion is evaluated through blastocyst pixel segmentation, component errors and synthetic-noise tests [@EE006].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Segment blastocyst components in static microscopy images. | EE006-B0012 |
| **Inputs** | PCRM Hoffman images; intensity, LBP texture and Gabor orientation derived from the same image. | EE006-B0011 EE006-B0012 |
| **Prediction time** | At blastocyst imaging; contemporaneous component segmentation, exact post-insemination hour not specified. | EE006-B0011 EE006-B0012 |
| **Analysis unit** | Pixels and component masks nested in blastocyst images; patient IDs/counts not supplied. | EE006-B0011 |
| **Method** | From-scratch MiMics-Net with multimodal-derived feature stem, grouped paths, skip connections and lightweight decoder; 0.65 million parameters. | EE006-B0012 EE006-B0015 EE006-B0017 |
| **Supervision / labels** | Expert embryologist pixel labels; generalized Dice training loss for five classes. | EE006-B0011 EE006-B0018 |
| **Outcome** | Jaccard and Dice of blastocyst component masks; no validated grade or pregnancy outcome. | EE006-B0020 EE006-B0021 |
| **Sample sizes** | {"original_images": 235, "training_images": 200, "test_images": 35, "augmented_training_images_reported": 3200, "patients": "not_reported_in_examined_source"} | EE006-B0011 EE006-B0019 |
| **Splitting** | Dataset-provider 200/35 image split; separate validation subset for confidence threshold not fully specified. | EE006-B0011 EE006-B0019 |
| **Validation** | Internal public-benchmark image test with comparative segmentation scores and confidence flag; multicenter validation left to future work. | EE006-B0016 EE006-B0020 EE006-B0030 |

## Source-linked excerpts
- [[EE006-B0011]] ==The dataset contains 235 human blastocyst images collected at a Canadian reproductive centre, with expert pixel annotations; the provider's 200-image training and 35-image test split was used.==
- [[EE006-B0012]] ==MiMics-Net combines photometric intensity, local-binary-pattern texture and Gabor orientation inputs and produces pixel labels for blastocyst components.==
- [[EE006-B0018]] ==The network was trained from scratch with generalized Dice loss and Adam; augmentation addressed class imbalance and expanded the training images.==
- [[EE006-B0021]] ==Testing compared pixel-level Jaccard and Dice results with several prior segmentation architectures; direct XML table inspection showed mean Jaccard 0.879, mean Dice 0.9343 and 0.65 million parameters for MiMics-Net.==
- [[EE006-B0023]] ==The authors show a compromised case and attribute failures to weak texture, ambiguous boundaries and poor illumination.==
- [[EE006-B0030]] ==The conclusion calls for multicentre validation across microscopes and protocols and notes that Gardner-grade preservation cannot be tested without expert grading labels.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*