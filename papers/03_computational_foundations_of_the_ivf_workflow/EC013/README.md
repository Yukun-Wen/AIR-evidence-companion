# EC013 — A preliminary study of sperm identification in microdissection testicular sperm extraction samples with deep convolutional neural networks.

**Wu, Badamjav, Reddy et al. (2021).** *Asian journal of andrology*. DOI: [10.4103/aja.aja_66_20](https://doi.org/10.4103/aja.aja_66_20)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational foundations of the IVF workflow, Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Gamete assessment spans specimens, individual cells and subsequent biological competence. Male-infertility reviews cover semen parameters, DNA integrity, retrieval prediction, ART prognosis and counseling alongside single-sperm selection and foundational CASA studies [@R035,R036,R034,R037]. Rare-sperm detection is a localization task within IVF sample preparation. A MobileNetV2/SSD study evaluates images of diluted residual micro-TESE material from patients. Object recall measures successful localization in those specimens, placing the result at the detection stage of the workflow. Patient separation is unspecified [@EC013].==

> **§ Computational methods** : Detection: selecting the object of analysis
> ==Rare-sperm search couples localization to specimen preparation and acquisition speed. MobileNetV2/SSD is evaluated on diluted residual human micro-TESE material, with image-test counts and patient grouping unresolved. An augmented-reality prototype combines YOLOv5s, DeepSORT and microscope overlays on donor sperm mixed with HepG2 cells. The physical surrogate provides a controlled setting for detector and tracker development. Clinical search performance depends on the authentic tissue setting, and end-to-end latency includes acquisition and display alongside detector runtime [@EC013,EC076].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Detect spermatozoa in residual micro-TESE microscopy images. | EC013-B0018 |
| **Inputs** | Static inverted-microscopy images of diluted prepared testicular-biopsy residual material. | EC013-B0010 EC013-B0011 |
| **Prediction time** | Immediately after micro-TESE preparation, before potential sperm retrieval/use; timing relative to use inferred from sample-processing workflow. | EC013-B0010 |
| **Analysis unit** | Image-level processing; sperm bounding boxes nested in images and patients. | EC013-B0013 EC013-B0018 |
| **Method** | ImageNet-pretrained MobileNetV2 feature extractor with single-shot detector and hard-negative mining. | EC013-B0020 EC013-B0021 |
| **Supervision / labels** | Single embryologist training bounding boxes; three-embryologist two-of-three IoU consensus for benchmark labels. | EC013-B0013 EC013-B0035 |
| **Outcome** | Sperm detection mAP at IoU 0.5, average recall and F1; no reproductive endpoint. | EC013-B0038 |
| **Sample sizes** | {"patients": 30, "images_total": 702, "benchmark_images": 110, "benchmark_sperm": 111} | EC013-B0008 EC013-B0035 |
| **Splitting** | Reported image split 80/10/10; separate benchmark described as 110 images. Patient-disjoint partition and reconciliation of test count not reported. | EC013-B0013 EC013-B0035 |
| **Validation** | Internal image benchmark versus embryologist consensus; mAP 0.741, recall 0.376 and F1 0.499. | EC013-B0035 EC013-B0038 |

## Source-linked excerpts
- [EC013-B0008] ==The dataset comprised 702 de-identified images from testicular biopsy samples of 30 patients after IRB approval and consent.==
- [EC013-B0010] ==Material was residual prepared TESE sample after micro-TESE and was explicitly more diluted and less complex than original specimens.==
- [EC013-B0035] ==Three embryologists independently labeled 110 test images with 111 sperm and a two-of-three overlap rule formed the reference boxes.==
- [EC013-B0038] ==The model's mAP, recall and F1 were 0.741, 0.376 and 0.499, compared with 0.925, 0.642 and 0.758 for embryologists.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*