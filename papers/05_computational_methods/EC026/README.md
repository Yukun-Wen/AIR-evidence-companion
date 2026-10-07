# EC026 — Human oocytes image classification method based on deep neural networks.

**Targosz, Myszor, Mrugacz (2023).** *Biomedical engineering online*. DOI: [10.1186/s12938-023-01153-4](https://doi.org/10.1186/s12938-023-01153-4)

**Role:** core · workflow: Oocyte assessment

**Cited in:** Computational methods

**PDF:** see EC026.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Oocyte maturity classification can use explicit anatomical intermediates. One system passes DeepLabV3Plus germinal-vesicle/polar-body masks to a SqueezeNet-inspired classifier refined by a genetic algorithm. A related study compares 71 segmentation variants and identifies poor coverage of rare small structures. Both reports contain sample-count inconsistencies and leave patient isolation unspecified. The maturity report also gives a nonstandard accuracy equation, making its stated metric definition part of the result [@EC026,EC027].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify human oocyte meiotic maturity and segment polar-body/germinal-vesicle structures. | EC026-B0027 EC026-B0028 |
| **Inputs** | Denuded oocyte microscopic images; automatically predicted FPB/GV masks feed the maturity classifier. | EC026-B0028 EC026-B0031 |
| **Prediction time** | After retrieval,2–5 h incubation and denudation, before ICSI; timing follows the acquisition procedure. | EC026-B0031 |
| **Analysis unit** | Oocyte image; multiple oocytes can occur in an original microscopy image. | EC026-B0031 EC026-B0037 |
| **Method** | DeepLabV3Plus segmentation followed by SqueezeNet-inspired CNN refined using genetic architecture search. | EC026-B0005 EC026-B0029 |
| **Supervision / labels** | Manual segmented oocyte structures and PI/MI/MII labels; cross-entropy optimization. | EC026-B0030 EC026-B0031 |
| **Outcome** | PI/MI/MII classification and region segmentation, not subsequent embryo or birth outcome. | EC026-B0001 EC026-B0027 |
| **Sample sizes** | {"patients": 100, "oocyte_images": 766, "MII": 663, "MI": 44, "PI": 59, "reported_segmentation_split": {"train": 657, "validation": 15, "test": 91}, "split_arithmetic_issue": "657+15+91=763; listed training class counts total660, not657"} | EC026-B0031 EC026-B0037 |
| **Splitting** | Stratified repeated image subsampling; default 3 repetitions and final classifier 10; patient grouping not specified. | EC026-B0037 EC026-B0038 EC026-B0039 |
| **Validation** | Internal repeated random validation; automatic masks evaluated separately from ideal manual masks; author-defined mean accuracy has Eq 4 ambiguity. | EC026-B0016 EC026-B0038 EC026-B0041 |

## Source-linked excerpts
- [EC026-B0031] ==The dataset contained 766 oocyte images from 100 hormonally stimulated ICSI patients, with 663 MII, 44 MI and 59 PI images.==
- [EC026-B0037] ==Repeated splits assigned 657 images to training, 15 to validation and 91 to testing for the segmentation network.==
- [EC026-B0021] ==Using DeepLab-generated masks, mean accuracy was 0.964 on validation and 0.957 on test images.==
- [EC026-B0024] ==Poor image quality, insufficient denudation, focus and indistinct structure boundaries explained observed misclassifications.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*