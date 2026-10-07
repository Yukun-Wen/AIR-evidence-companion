# EE060 — Automatic characterization of human embryos at day 4 post-insemination from time-lapse imaging using supervised contrastive learning and inductive transfer learning techniques.

**Paya, Bori, Colomer et al. (2022).** *Computer methods and programs in biomedicine*. DOI: [10.1016/j.cmpb.2022.106895](https://doi.org/10.1016/j.cmpb.2022.106895)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Representation reuse and adaptation across targets
> ==Representation reuse learns useful features before fitting the downstream target. SimCLR combines augmented views, a shared encoder and a projection head under a contrastive objective; masked autoencoders reconstruct masked content from visible patches through a lighter decoder. View construction specifies invariance, while reconstruction specifies which missing image content the representation learns to estimate. Adapting these objectives to embryo morphology involves choosing biologically meaningful transformations and evaluating the pretrained representation on a separate downstream task [@EM025,EM026]. Supervised contrastive learning uses developmental viability labels to organize embryo-image embeddings, followed by inductive transfer to morphology-quality classification. The single-center evaluation reports a transfer-learning advantage for these developmental labels; patient grouping is unspecified [@EE060].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify embryo viability and morphology quality at day 4, with day-5 comparison. | EE060-P003 EE060-P004 |
| **Inputs** | Three adjacent focal-plane grayscale images at 90 or 115 hpi stacked as 224×224×3 input. | EE060-P003 |
| **Prediction time** | 90 hpi primary setting; independently trained 115 hpi comparator. | EE060-P003 |
| **Analysis unit** | Embryo image instance; source calls 3014/830 observations embryo cycles and separately lists patient counts. | EE060-P003 |
| **Method** | Supervised contrastive ResNet50/VGG16 encoder with projection-head variants, followed by classifier; inductive transfer from viability to quality. | EE060-P004 EE060-P005 |
| **Supervision / labels** | Viable/nonviable labels and ASEBIR morphology high A/B versus low C; exact operational viable definition is not detailed in examined Materials. | EE060-P003 |
| **Outcome** | Embryo viability category and morphology quality; no direct live-birth endpoint. | EE060-P003 EE060-P005 |
| **Sample sizes** | {"viability_embryo_cycles_reported": 3014, "viability_patients": 1289, "quality_embryo_cycles_reported": 830, "quality_patients": 559} | EE060-P003 |
| **Splitting** | 85% development/15% blind test; development split again 90/10 training/validation for both tasks. Patient grouping not specified. | EE060-P003 EE060-P004 |
| **Validation** | Internal blind test of supervised contrastive versus cross-entropy and transfer variants, accuracy/precision/sensitivity/specificity/F1/AUROC. | EE060-P005 EE060-P006 |

## Source-linked excerpts
- [EE060-P003] ==The study was a retrospective single-center ICSI cohort with 3,014 cycles from 1,289 patients for viability and 830 cycles from 559 patients for quality; labels were balanced but morphology-based and potentially discordant.==
- [EE060-P004] ==The models used three focal planes at 90 and 115 hours, with 85% assigned to development and 15% to a blind test, followed by a training/validation split within development data.==
- [EE060-P007] ==The original PDF table reports Day-4 viability accuracy/AUC of 0.8103/0.84 and Day-4 quality accuracy/AUC of 0.7500/0.77 for the proposed methods, with higher Day-5 metrics.==
- [EE060-P010] ==The authors identify the retrospective single-center design, one incubator type, need for multicenter data, and larger prospective validation as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*