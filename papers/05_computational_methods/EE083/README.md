# EE083 — Automated embryo stage classification in time-lapse microscopy video of early human embryo development.

**Wang, Moussavi, Lorenzen (2013).** *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2013*. DOI: [10.1007/978-3-642-40763-5_57](https://doi.org/10.1007/978-3-642-40763-5_57)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE083.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Temporal constraints impose consistency on predicted stages. An earlier pipeline combines handcrafted and bag-of-features descriptors, local-temporal AdaBoost and Viterbi refinement. Overall frame accuracy improves, while three-cell accuracy remains 20.86%. Short-stage annotation therefore becomes a specific target for improving division-timing estimation [@EE083].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Detect early embryo cell stages and division timings in time-lapse videos. | EE083-P002 EE083-P007 |
| **Inputs** | Dark-field Eeva videos with handcrafted image features and bag-of-features representations. | EE083-P002 EE083-P006 |
| **Prediction time** | First two days after fertilization. | EE083-P002 EE083-P006 |
| **Analysis unit** | Video frames and embryo sequences. | EE083-P006 EE083-P007 |
| **Method** | AdaBoost local classifiers followed by Viterbi sequence optimization. | EE083-P002 |
| **Supervision / labels** | Two-expert cell-stage annotations; disagreement frames excluded. | EE083-P006 |
| **Outcome** | Cell-stage accuracy and cell-division timing precision/recall. | EE083-P006 EE083-P007 |
| **Sample sizes** | {"embryo_videos": 716, "training_videos": 327, "test_videos": 389, "frames_per_video_retained": 500, "expert_annotators": 2} | EE083-P006 |
| **Splitting** | 327 training and 389 test videos; training divided for classifier levels; patient grouping not stated. | EE083-P006 |
| **Validation** | Held-out video frame and timing evaluation against each expert and their average. | EE083-P006 EE083-P007 EE083-P008 |

## Source-linked excerpts
- [EE083-P002] ==The method uses a three-level pipeline: per-frame and local-temporal AdaBoost classification followed by Viterbi sequence refinement, avoiding explicit cell tracking.==
- [EE083-P006] ==Two experts annotated 716 Eeva videos; 327 videos trained the system and 389 formed the test set, with disagreements excluded from training.==
- [EE083-P001] ==The abstract reports evaluation on 389 human embryo videos and an overall stage-classification accuracy of 87.92%.==
- [EE083-P007] ==The confusion matrix shows three-cell frames were frequently classified as two-cell or four-or-more-cell, consistent with sparse three-cell training examples.==
- [EE083-P008] ==The conclusion limits the demonstrated task to embryo-stage classification and proposes future work on quality predictors using extracted timings.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*