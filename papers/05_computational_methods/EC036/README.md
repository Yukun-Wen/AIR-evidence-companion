# EC036 — A weakly-supervised follicle segmentation method in ultrasound images.

**Liu, Huang, Li et al. (2025).** *Scientific reports*. DOI: [10.1038/s41598-025-95957-0](https://doi.org/10.1038/s41598-025-95957-0)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods, Learning objectives and the interpretation of model outputs, Quantitative evidence and supported decision claims

**PDF:** see EC036.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Follicle monitoring connects image measurement to workflow. One automated ultrasound system achieved an F1 of 89% (95% CI, 88--90%) on 702 test scans from 235 patients. In a separate prospective cohort, 265 of 904 scans from 269 patients required sonographer editing (29%; 95% CI, 26--32%). F1 summarizes detection across follicles; the scan-level edit rate quantifies review workload. A weakly supervised approach instead combines convolutional features and multiple-instance learning to reduce dense annotation. FUID contributes additional training data, and the biological partition unit is unspecified [@EC033,EC036].==

> **§ Learning objectives and the interpretation of model outputs** : A task-indexed metric catalogue
> ==12 Comparing IVF methods requires a common prediction question and a specified evaluation population. Available information and labels define the question; biological hierarchy and validation define the tested population; policy evaluation measures the consequences of using the output.==

> **§ Quantitative evidence and supported decision claims** : Independent models on four selected datasets
> ==The metric vector preserves trade-offs beyond the ordering metric. In the wider configuration archive, USOVA3D's leading detection mAP and segmentation overlap come from different systems [@EC036]. On VISEM, EKF-BoT-SORT leads IDF1 whereas BoT-SORT leads MOTA [@EC077]. These examples connect the independent-model comparison to the task-specific metric catalogue in Section 6.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Weakly supervised ovarian-follicle instance segmentation. | EC036-B0015 |
| **Inputs** | Ovarian ultrasound: 2D slices from USOVA3D volumes and FUID ultrasound images. | EC036-B0029 |
| **Prediction time** | At ultrasound follicle monitoring; instantaneous segmentation, not future-event prediction. | EC036-B0003 EC036-B0015 |
| **Analysis unit** | Follicles/pixels nested in ultrasound images, volumes and cases. | EC036-B0029 |
| **Method** | WSFS CNN/FPN with detection and segmentation branches, multiple-instance box supervision; optional SAM-Med2D prompt refinement. | EC036-B0015 EC036-B0016 |
| **Supervision / labels** | Bounding boxes for weakly supervised learning; expert pixel masks used for evaluation, FUID annotated then checked by a second expert. | EC036-B0001 EC036-B0029 |
| **Outcome** | Follicle detection mAP50 and segmentation IoU/Dice. | EC036-B0030 |
| **Sample sizes** | {"USOVA3D_volumes": 35, "FUID_cases": 193, "FUID_images": 22942} | EC036-B0029 |
| **Splitting** | Exact partition sizes and patient/volume grouping not reported in examined experimental methods. FUID described as unseen validation data but later training described as combined public/private data. | EC036-B0029 EC036-B0031 EC036-B0042 |
| **Validation** | Dataset-based method/ablation comparisons; external independence of FUID cannot be established from contradictory descriptions. | EC036-B0033 EC036-B0038 EC036-B0042 |

## Source-linked excerpts
- [EC036-B0007 to EC036-B0009 (Contribution and scope)] ==The work proposes bounding-box-supervised follicle instance segmentation and introduces the FUID ultrasound dataset to reduce reliance on pixel-level masks.==
- [EC036-B0015 to EC036-B0027 (Architecture and losses)] ==WSFS combines a CSPDarknet/FPN detector with a multiple-instance-learning mask branch and can supply point, box, or mask prompts to SAM-Med2D; it is an algorithmic method rather than a clinical decision intervention.==
- [EC036-B0029 (Datasets)] ==Evaluation used 35 annotated USOVA3D volumes sliced into 2D images plus FUID, described as 193 cases and 22,942 images with two-expert pixel annotations.==
- [EC036-B0033 to EC036-B0035 (Tables 1-2)] ==WSFS+ reported mAP50 0.957, IoU 0.714, and Dice 0.83 on USOVA3D; YOLOv8x-seg had lower mAP50 but higher IoU and Dice, so superiority depends on the selected metric.==
- [EC036-B0038 to EC036-B0040 (Table 3)] ==Using the WSFS+ mask as a SAM-Med2D prompt yielded mAP50 0.967, IoU 0.724, and Dice 0.84 at much higher parameter and FLOP counts than WSFS+ alone.==
- [EC036-B0052 (Limitations)] ==The authors note no end-to-end SAM integration, a 224-pixel input limit, and insufficient robustness to extremely noisy ultrasound images.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*