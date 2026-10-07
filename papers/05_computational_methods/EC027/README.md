# EC027 — Semantic segmentation of human oocyte images using deep neural networks.

**Targosz, Przystalka, Wiaderkiewicz et al. (2021).** *Biomedical engineering online*. DOI: [10.1186/s12938-021-00864-w](https://doi.org/10.1186/s12938-021-00864-w)

**Role:** core · workflow: Oocyte assessment

**Cited in:** Computational methods

**PDF:** see EC027.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Oocyte maturity classification can use explicit anatomical intermediates. One system passes DeepLabV3Plus germinal-vesicle/polar-body masks to a SqueezeNet-inspired classifier refined by a genetic algorithm. A related study compares 71 segmentation variants and identifies poor coverage of rare small structures. Both reports contain sample-count inconsistencies and leave patient isolation unspecified. The maturity report also gives a nonstandard accuracy equation, making its stated metric definition part of the result [@EC026,EC027].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Semantic segmentation of oocyte structures and abnormalities. | EC027-B0075 |
| **Inputs** | 561×561 grayscale static light-microscopy oocyte images at ×200 magnification. | EC027-B0071 |
| **Prediction time** | After retrieval, incubation and denudation for ICSI; before injection inferred from imaging workflow. | EC027-B0070 EC027-B0071 |
| **Analysis unit** | Pixels within oocyte images; images from patients, occasionally multiple oocytes per image. | EC027-B0071 EC027-B0075 |
| **Method** | 71 variants of FCN, SegNet, U-Net and DeepLab-v3+ with transferred CNN backbones and weighted pixel loss. | EC027-B0076 EC027-B0103 |
| **Supervision / labels** | Manual image segmentation supplies structure-level pixel labels. | EC027-B0071 |
| **Outcome** | Pixel/region segmentation measured with weighted IoU, accuracy, mean IoU, boundary score and Dice. | EC027-B0027 EC027-B0033 |
| **Sample sizes** | {"patients": 60, "images_reported_total": 334, "reported_class_counts": {"MII": 236, "MI": 21, "PI": 48, "DYS": 8, "DEG": 23}, "class_count_sum": 336} | EC027-B0070 |
| **Splitting** | 80% training, 5% validation, 15% test image partition with on-the-fly augmentation; patient-disjoint grouping not specified. | EC027-B0024 |
| **Validation** | Internal test comparison ranks 71 configurations by weighted IoU; two rare structures have no test examples. External validation not reported. | EC027-B0025 EC027-B0027 EC027-B0031 |

## Source-linked excerpts
- [EC027-B0070] ==The dataset comprised 334 images of oocytes from 60 ICSI patients with explicit maturity and abnormality class counts.==
- [EC027-B0024] ==Images were divided 80/5/15 into training, validation and test subsets with on-the-fly augmentation.==
- [EC027-B0027] ==The leading DeepLab-v3-ResNet-18 variant achieved test weighted IoU 0.897 and global accuracy 0.93.==
- [EC027-B0031] ==Vacuole and fragmented-polar-body pixel detection was below 50%, and extremely rare structures could not be evaluated.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*