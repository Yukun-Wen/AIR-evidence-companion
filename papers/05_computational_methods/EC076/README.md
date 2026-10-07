# EC076 — AI-Based Augmented Reality Microscope for Real-Time Sperm Detection and Tracking in Micro-TESE.

**Mohamed, Yuriko, Kawagoe et al. (2026).** *Bioengineering (Basel, Switzerland)*. DOI: [10.3390/bioengineering13010102](https://doi.org/10.3390/bioengineering13010102)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational methods, Design challenges and directions for validated AI

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Detection: selecting the object of analysis
> ==Rare-sperm search couples localization to specimen preparation and acquisition speed. MobileNetV2/SSD is evaluated on diluted residual human micro-TESE material, with image-test counts and patient grouping unresolved. An augmented-reality prototype combines YOLOv5s, DeepSORT and microscope overlays on donor sperm mixed with HepG2 cells. The physical surrogate provides a controlled setting for detector and tracker development. Clinical search performance depends on the authentic tissue setting, and end-to-end latency includes acquisition and display alongside detector runtime [@EC013,EC076].==

> **§ Design challenges and directions for validated AI** : Isolating the contribution of a computational mechanism
> ==Table entry; table caption: Source-located limitations and studies that could address them. — Donor sperm in surrogate tissue [@EC076]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Real-time sperm detection, tracking and augmented-reality display for micro-TESE support. | EC076-B0045 EC076-B0046 |
| **Inputs** | Microscopy frames/video of provisional specimens mixing human donor sperm with HepG2 cells; single-frame detection followed by tracking. | EC076-B0017 EC076-B0018 EC076-B0037 |
| **Prediction time** | During live microscope observation; contemporaneous localization and movement estimation. | EC076-B0046 |
| **Analysis unit** | Sperm boxes and trajectories within frames and videos; donor/patient independence not established. | EC076-B0088 |
| **Method** | YOLOv5s detector, DeepSORT tracking and SD-CLIP head localization for velocity display. | EC076-B0045 EC076-B0067 EC076-B0069 |
| **Supervision / labels** | Manually annotated frames sampled every five frames. | EC076-B0088 |
| **Outcome** | Detection precision/recall/F1/AP, inference time, tracking and AR alignment; no fertilization endpoint. | EC076-B0073 EC076-B0099 EC076-B0106 |
| **Sample sizes** | {"videos": 19, "reported_train_validation_test_allocation": [12, 2, 5], "comparison_images": 32, "donors": "not_reported_in_examined_source"} | EC076-B0088 EC076-B0099 |
| **Splitting** | Source reports 19 videos and allocation 12/2/5, but wording says “for each video”; exact frame/video partition needs clarification. | EC076-B0088 |
| **Validation** | Internal test detection curves, 32-image comparison and qualitative tracking/latency demonstration. | EC076-B0096 EC076-B0099 EC076-B0106 |

## Source-linked excerpts
- [EC076-B0018] ==The experimental mixture combined anonymized healthy-donor human sperm suspension with HepG2 cells.==
- [EC076-B0088] ==Nineteen videos were sampled and allocated by video as 12 training, 2 validation and 5 test videos.==
- [EC076-B0099] ==On 32 microscope images, YOLOv5 achieved precision 0.81, recall 0.52, F1 0.64 and 31 ms runtime.==
- [EC076-B0114] ==The estimated end-to-end delay was camera-transfer time plus approximately 212 ms, exceeding the nominal 200 ms requirement even before transfer time.==
- [EC076-B0121] ==The authors explicitly state HepG2 cells replaced authentic clinical micro-TESE samples and that real-sample validation remains future work.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*