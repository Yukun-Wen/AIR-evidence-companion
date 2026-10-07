# EE019 — Computer vision for automatic identification of blastocyst structures and blastocyst formation time in In-Vitro Fertilization.

**Villota, Ayensa-Jimenez, Malo et al. (2025).** *Computers in biology and medicine*. DOI: [10.1016/j.compbiomed.2025.110633](https://doi.org/10.1016/j.compbiomed.2025.110633)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE006,EE019,EQF01]==

> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Blastocyst masks can generate area trajectories for formation-time estimation. A comparison of U-Net, HRNet and related segmenters includes a small private-clinic test, where compartment performance falls relative to the public-image comparison. Its results and conclusion give conflicting timing-error summaries; segmentation overlap and event-timing error require separate records [@EE019].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Segment blastocyst structures and estimate time of expanded-blastocyst formation. | EE019-P005 EE019-P006 |
| **Inputs** | PCRM annotated static blastocyst images and independent Geri time-lapse videos from Quirónsalud Zaragoza. | EE019-P005 |
| **Prediction time** | Segmentation at blastocyst imaging; formation time retrospectively extracted from development video spanning roughly day 1–5. | EE019-P005 EE019-P006 |
| **Analysis unit** | Pixel/structure segmentation per image; formation timing per embryo video. | EE019-P005 |
| **Method** | RDU-Net replication, U-Net, HRNet and DeepLab, plus genetic-algorithm-tuned image processing; segmentation-derived area time series identifies formation. | EE019-P005 EE019-P006 |
| **Supervision / labels** | Expert ZP/TE/ICM masks and expert-annotated blastocyst-formation times. | EE019-P005 |
| **Outcome** | Structure segmentation overlap and formation-timing error, not implantation outcome prediction. | EE019-P005 EE019-P006 |
| **Sample sizes** | {"PCRM_images_reported": 249, "private_videos": 69, "private_segmentation_images": 25, "patient_count": "not_reported_in_examined_source"} | EE019-P005 |
| **Splitting** | Public 85/15 image splits and described ten-fold repeated/CV experiments; independent private center evaluated on 25 images and 69 videos. | EE019-P005 EE019-P006 |
| **Validation** | Internal split variability and independent-center segmentation/timing evaluation; selection of HRNet considers private-data generalization. | EE019-P006 EE019-P012 |

## Source-linked excerpts
- [EE019-P005] ==Training used 249 publicly annotated blastocyst images; independent evaluation used 25 labelled images and 69 time-lapse videos from another clinic.==
- [EE019-P009] ==Across architectures, HRNet provided the best overall segmentation, with a mean Dice score near 0.87 across structures.==
- [EE019-P011] ==On private data, HRNet Dice scores were 0.70, 0.76, and 0.70 for zona pellucida, trophectoderm, and inner cell mass; timing error averaged 4.87 hours.==
- [EE019-P013] ==The authors caution that domain shift and segmentation errors can affect downstream biopsy or selection decisions and restrict the current tool to research use.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*