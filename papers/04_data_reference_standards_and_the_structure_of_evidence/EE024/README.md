# EE024 — Cleavage-stage embryo segmentation using SAM-based dual branch pipeline: development and evaluation with the CleavageEmbryo dataset.

**Zhang, Shi, Yin et al. (2025).** *Bioinformatics (Oxford, England)*. DOI: [10.1093/bioinformatics/btae617](https://doi.org/10.1093/bioinformatics/btae617)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Learning objectives and the interpretation of model outputs, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE024]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==12 The census identifies nine resources used by at least two empirical reports and eleven used once. The small repeat-use counts, together with the protocol differences, locate the main opportunity for cumulative benchmarking: shared releases with stable subject identifiers, labels and partitions. Additional resources in the complete census include 3D-SpermVid and its linked centerline data, which provide multifocal imaging and flagellar coordinates [@ER027,ER028]. CleavageEmbryo supplies blastomere and fragment tasks, while the Nantes descriptor explains the event-derived annotations used by subsequent models [@EE024,EE061].==

> **§ Learning objectives and the interpretation of model outputs** : A task-indexed metric catalogue
> ==12 Comparing IVF methods requires a common prediction question and a specified evaluation population. Available information and labels define the question; biological hierarchy and validation define the tested population; policy evaluation measures the consequences of using the output.==

> **§ Quantitative evidence and supported decision claims** : Broad systems and the meaning of state of the art
> ==Table entry; table caption: Representative leading systems: breadth and evidence answer different questions. — Task-specific benchmark leaders [@OUTCOME01,EQS01,EE024]==

> **§ Quantitative evidence and supported decision claims** : Independent models on four selected datasets
> ==The grouping follows computational identity. HFEA's multilayer perceptron and nine-layer dense network form one feedforward family; hard and soft voting of the same estimators form one ensemble family. On HuSHeM and SMIDS, Swin V2, EfficientNetV2 and CoAtNet size variants each occupy one slot. The five-family comparison uses standalone backbones; the source's compound CNN--Transformer cascades remain in the configuration archive. CleavageEmbryo uses the blastomere instance-segmentation task, with automated prompts for the proposed dual-branch model. Its oracle-prompt result and ablations are outside the independent-model order [@OUTCOME01,EQS01,EE024].==

> **§ Quantitative evidence and supported decision claims** : Independent models on four selected datasets
> ==Table entry; table caption: Five independent model families on each of four selected datasets. One representative per family is ranked within the stated evaluation protocol; N counts distinct papers reporting numerical model results. — CleavageEmbryo; blastomeres; 2025 [@EE024]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Segment blastomere instances and fragment regions. | EE024-B0006 EE024-B0008 |
| **Inputs** | Cleavage-stage 800×800 frames from time-lapse videos. | EE024-B0022 EE024-B0024 |
| **Prediction time** | Cleavage-stage image assessment without a clinical prediction horizon. | EE024-B0022 EE024-B0023 |
| **Analysis unit** | Image, blastomere instance and fragment pixels. | EE024-B0022 EE024-B0024 |
| **Method** | SAM dual branch with YOLOv 8 bounding-box prompts and semantic fragment decoder. | EE024-B0008 EE024-B0011 EE024-B0014 EE024-B0016 EE024-B0051 |
| **Supervision / labels** | Four-doctor pixel annotations; ground-truth training prompts and detector prompts at inference. | EE024-B0022 EE024-B0023 EE024-B0017 |
| **Outcome** | Blastomere mAP/precision/recall/F1 and fragment Dice/Hausdorff. | EE024-B0051 EE024-B0054 |
| **Sample sizes** | {"images": 1548, "train_images": 1232, "validation_images": 316, "annotators": 4} | EE024-B0022 EE024-B0024 |
| **Splitting** | 1232 training and 316 validation images; patient/video grouping not stated. | EE024-B0022 EE024-B0024 |
| **Validation** | Within-dataset model comparison and ablations; ground-truth-box oracle kept separate. | EE024-B0051 EE024-B0054 EE024-B0064 |

## Source-linked excerpts
- [EE024-B0001] ==The study develops a SAM-based dual-branch pipeline for human cleavage-stage embryos and reports blastomere mAP 0.874 and fragment Dice 0.695; code and sample data are linked on GitHub.==
- [EE024-B0022] ==Images are frames from embryo time-lapse videos and were pixel-annotated for blastomeres and fragments by four experienced physicians at one hospital.==
- [EE024-B0024] ==The dataset contains 1,548 images and uses an image-level 1,232/316 training-validation split.==
- [EE024-B0051] ==The automated YOLOv8-prompted pipeline achieved blastomere mAP 0.874; performance rose to 0.942 when ground-truth boxes supplied the prompts, showing dependence on detection quality.==
- [EE024-B0064] ==Clinical outcomes were not recorded in the present dataset; adding later developmental stages and final outcomes is identified as future work.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*