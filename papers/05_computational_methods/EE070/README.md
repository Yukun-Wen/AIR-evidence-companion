# EE070 — End-to-end deep learning for recognition of ploidy status using time-lapse videos.

**Lee, Su, Chen et al. (2021).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-021-02228-8](https://doi.org/10.1007/s10815-021-02228-8)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Direct video encoders and shared representations
> ==Two-stream I3D processing separates image appearance from optical flow before averaging predictions. In one ploidy study, mosaics join the euploid class, and default-threshold aneuploid sensitivity is low despite moderate AUC. The result couples a motion-sensitive representation with a specific genetic label definition and highlights threshold choice as a major determinant of its classification behavior [@EE070].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify aneuploid embryos versus pooled euploid/mosaic embryos from videos. | EE070-H0203 EE070-H0211 |
| **Inputs** | Time-lapse grayscale images replicated into RGB channels and computed optical flow, sampled about every 0.5 hpi. | EE070-H0211 EE070-H0214 |
| **Prediction time** | Separate day-1, day-1–3 and day-1–5 observation windows. | EE070-H0219 |
| **Analysis unit** | Embryo video nested in PGT-A cycle and patient. | EE070-H0174 EE070-H0219 |
| **Method** | ImageNet/Kinetics-pretrained two-stream I3D with averaged RGB and optical-flow predictions. | EE070-H0203 EE070-H0211 |
| **Supervision / labels** | Day-5/6 TE-biopsy high-resolution NGS PGT-A labels; euploid and mosaic combined in negative class. | EE070-H0221 EE070-H0268 |
| **Outcome** | Aneuploid versus euploid/mosaic; not euploid versus all abnormal. | EE070-H0211 |
| **Sample sizes** | {"patients": 108, "PGT_A_cycles": 119, "embryo_videos": 690, "aneuploid": 157, "euploid": 258, "mosaic": 275, "frame_data_points": 144210} | EE070-H0174 EE070-H0268 |
| **Splitting** | Random 80/20 video split; grouping by patient/cycle not described. | EE070-H0219 |
| **Validation** | Internal AUROC, confusion metrics and quartile calibration for streams/time windows; external validation not reported. | EE070-H0221 EE070-H0247 EE070-H0252 |

## Source-linked excerpts
- [EE070-H0174] ==The cohort contained 690 videos from 108 selected patients, excluding low AMH, age over 38, severe pathology, surgical sperm retrieval, and repeated euploid-transfer failure.==
- [EE070-H0178] ==PGT-A results were divided into euploid, low mosaic, high mosaic, and aneuploid groups; the model later combined both mosaic groups with euploids.==
- [EE070-H0219] ==Videos were randomly divided 80%/20% and RGB, optical flow, and time-window settings were evaluated.==
- [EE070-H0239] ==The original results table reports fused AUCs of 0.58 for Day 1, 0.63 through Day 3, and 0.74 through Day 5.==
- [EE070-H0247] ==At the default threshold, aneuploid sensitivity was 0.333 and PPV 0.529; lowering the threshold raised recall to 0.63 but reduced PPV to 0.436.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*