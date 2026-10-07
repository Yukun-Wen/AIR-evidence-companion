# EE015 — Accurate machine learning model for human embryo morphokinetic stage detection.

**Misaghi, Cree, Knowlton (2025).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-025-03585-4](https://doi.org/10.1007/s10815-025-03585-4)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence, Computational methods

**PDF:** see EE015.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE015,EE017,EQF01]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==In the figure caption — Arrows distinguish resource extension, added annotations and empirical use ER046,ER019,ER027,ER028,EC077,EC081,EC080,EC082,EE015==

> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Liao separates developmental progression from appearance: a temporal stream models cell-stage sequences, a spatial stream extracts morphology, and fusion forecasts blastocyst formation and usable-blastocyst status from the first three days. Stage and forecast evaluations locate errors along this pixel-to-event-to-outcome path [@EMBRYO04]. An EfficientNet-V2 encoder and transformer combine elapsed-time embeddings with image features for stage classification on public videos. Label correction and postprocessing also change in its image-only comparison. Frame-, embryo- and patient-level results locate accuracy within the biological hierarchy [@EE015].==

> **§ Computational methods** : Explicit events and recurrent trajectories
> ==A ResNet18 annotation system converts frame probabilities into monotonic sequences through isotonic regression. This enforces developmental ordering, whereas an alternative postprocessing design permits reverse transitions. Annotation agreement evaluates the assigned stages; exploratory developmental clusters describe patterns in the resulting trajectories [@EE045,EE015].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify morphokinetic stage and infer transition times. | EE015-B0001 EE015-B0027 |
| **Inputs** | Static central-plane embryo image with optional elapsed time since fertilization. | EE015-B0016 EE015-B0018 |
| **Prediction time** | Contemporaneous stage across culture up to seven days; complete-video postprocessing may use sequential context. | EE015-B0018 EE015-B0027 |
| **Analysis unit** | Frame nested in embryo video. | EE015-B0010 |
| **Method** | ImageNet EfficientNetV2-L with optional time-fusion transformer and heuristic temporal postprocessing; ResNet50 baseline. | EE015-B0016 EE015-B0018 EE015-B0027 |
| **Supervision / labels** | Single embryologist event labels propagated to frames; empty-well labels reclassified with visually checked model. | EE015-B0010 EE015-B0012 |
| **Outcome** | Morphokinetic class and event timing; hatched-blastocyst class excluded from later analyses due to scarcity. | EE015-B0013 EE015-B0045 EE015-B0054 |
| **Sample sizes** | {"resource_videos": 704, "analyzed_labeled_images": 273438, "empty_images": 9734, "patients": "not_reported_in_examined_source"} | EE015-B0010 EE015-B0012 |
| **Splitting** | 70/10/20 training/validation/test described; class-level image counts reported; embryo/patient grouping not established in examined methods. | EE015-B0001 EE015-B0014 EE015-B0044 |
| **Validation** | Internal accuracy,F1,precision/recall and event-time error distributions; no external center test. | EE015-B0045 EE015-B0054 |

## Source-linked excerpts
- [EE015-B0010] ==The human IVF dataset comprised 704 EmbryoScope videos and 273,438 labelled central-plane images after file-quality filtering.==
- [EE015-B0024] ==Models were trained for 50 epochs with Adam and evaluated on a held-out test set that was not used during training.==
- [EE015-B0048] ==The two leading models achieved accuracies of 0.871 and 0.879, with the latter reaching F1 0.881.==
- [EE015-B0064] ==The authors identify subjective human labels and reliance on a single EmbryoScope device type as principal limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*