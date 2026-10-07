# EC077 — Robust Real-Time Sperm Tracking with Identity Reassignment Using Extended Kalman Filtering.

**Hassani, Saadat, Lei (2025).** *Sensors (Basel, Switzerland)*. DOI: [10.3390/s25247539](https://doi.org/10.3390/s25247539)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Data, reference standards and the structure of evidence, Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EC077,EC081,ER046]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==In the figure caption — Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015==

> **§ Computational methods** : Comparing temporal support and information paths
> ==Tracking represents identity through motion. A YOLO11, BoT-SORT and extended-Kalman-filter pipeline improves reported identity measures on reused VISEM data while lowering MOTA relative to its comparator [@EC077]. Association quality and overall tracking accuracy therefore favor different designs in this comparison. Unspecified donor/video separation and inconsistent derived motility values restrict its interpretation to the reported tracking measures.==

> **§ Quantitative evidence and supported decision claims** : Independent models on four selected datasets
> ==The metric vector preserves trade-offs beyond the ordering metric. In the wider configuration archive, USOVA3D's leading detection mAP and segmentation overlap come from different systems [@EC036]. On VISEM, EKF-BoT-SORT leads IDF1 whereas BoT-SORT leads MOTA [@EC077]. These examples connect the independent-model comparison to the task-specific metric catalogue in Section 6.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Track sperm and reassign fragmented identities across microscopy frames. | EC077-B0001 EC077-B0078 |
| **Inputs** | VISEM microscopy video frames and YOLO11m detections. | EC077-B0015 EC077-B0119 |
| **Prediction time** | Online frame-by-frame tracking; no future clinical outcome prediction. | EC077-B0090 |
| **Analysis unit** | Sperm trajectory/identity nested within video. | EC077-B0122 |
| **Method** | YOLO11m detection, BoT-SORT tracking and nonlinear EKF identity verification; ByteTrack/DeepSORT comparators. | EC077-B0015 EC077-B0022 EC077-B0078 |
| **Supervision / labels** | Annotated VISEM video detections train YOLO; tracking reference identities used for evaluation. | EC077-B0022 EC077-B0122 |
| **Outcome** | IDF1, identity switches, MOT accuracy/precision, track duration and count inflation. | EC077-B0132 EC077-B0138 |
| **Sample sizes** | {"resource_videos": 85, "evaluated_video_count": "not_reported_in_examined_source", "reported_sequence_ground_truth_ids": 34, "patient_count": "not_reported_in_examined_source"} | EC077-B0119 EC077-B0122 |
| **Splitting** | Validation-selected detector checkpoint; explicit train/validation/test video IDs and partition sizes not reported in examined source. | EC077-B0022 EC077-B0119 |
| **Validation** | Within-VISEM tracking comparisons and sensitivity analysis; no external cohort or fertility endpoint. | EC077-B0119 EC077-B0132 |

## Source-linked excerpts
- [EC077-B0003] ==The paper describes single-sperm selection, immobilization, aspiration, and injection as operator-dependent ICSI steps, establishing a direct laboratory-workflow connection.==
- [EC077-B0011] ==The empirical resource is the public VISEM collection of live human sperm microscopy videos, recorded at 37 degrees Celsius and 400x magnification.==
- [EC077-B0022] ==YOLO11 was trained for 300 epochs on annotated VISEM videos with validation-loss early stopping, but the exact video/donor partition is not reported.==
- [EC077-B0119] ==Evaluation reused the 85-video VISEM dataset and compared EKF-BoT-SORT with BoT-SORT, ByteTrack, and DeepSORT using MOT metrics.==
- [EC077-B0132] ==EKF-BoT-SORT achieved IDF1 84.84%, 132 ID switches, MOTA 41.80%, precision 87.95%, and recall 90.77% in the reported comparison.==
- [EC077-B0176] ==The authors report degraded reliability above roughly 60-70 sperm per 640 x 480 frame because longer occlusions create identity ambiguity.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*