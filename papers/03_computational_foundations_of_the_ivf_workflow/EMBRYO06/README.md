# EMBRYO06 — A generalized AI system for human embryo selection covering the entire IVF cycle via multi-modal contrastive learning

**Wang, Wang, Gao et al. (2024).** *Patterns (New York, N.Y.)*. DOI: [10.1016/j.patter.2024.100985](https://doi.org/10.1016/j.patter.2024.100985)

**Role:** core · contrasts C05, C06 · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Computational methods

**PDF:** see EMBRYO06.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2024: multimodal systems and randomized selection [@EMBRYO06,OUTCOME05]==

> **§ Computational methods**
> ==In the figure caption — Source-located quantitative examples for these mechanisms are presented in Table 7 STIM05,EMBRYO03,EMBRYO02,EMBRYO06==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Timestamp-aware encoding across transferred embryos (stage-specific images / transfer) [@EMBRYO06]==

> **§ Computational methods** : Direct video encoders and shared representations
> ==The later iDAScore development study uses separate pathways for early and blastocyst-stage transfer days and treatment-level splitting. Its multicenter dataset supports internal evaluation. The v1 comparator had previously trained on some v2 test samples, giving the compared versions different exposure histories on the evaluation set [@EE047]. IVFormer uses visual-temporal contrastive learning before adaptation to morphology, ploidy and live birth. Static images and videos share a developmental representation. Pretraining and fine-tuning reuse development data; evaluation patients remain separate [@EMBRYO06].==

> **§ Computational methods** : Biological alignment and hierarchical aggregation
> ==Transfer-level supervision connects the embryo representations to an observed clinical outcome. IVFormer's live-birth task combines stage-specific images using timestamp-based temporal embeddings. In an external cohort of 1,343 double-embryo transfers from 1,262 patients, metadata-only, image-only and combined models achieved AUCs of 0.734, 0.820 and 0.857; the combined estimate had a 95% CI of 0.830--0.878. The combined input-and-learner configuration has the highest point estimate for transfer-level prognosis. The observed label belongs to the embryo pair, so individual-embryo attribution and sibling ordering remain distinct targets [@EMBRYO06].==

> **§ Computational methods** : Representation reuse and adaptation across targets
> ==Wang and colleagues alternate image and video self-supervision through IVFormer's shared visual encoder, then adapt it to morphology, ploidy and live birth. Positive video pairs are augmented clips from one sequence, enforcing consistency across appearance and sampling changes. On a patient-separated internal ploidy test of 520 embryos from 356 patients, metadata-only, video-only and combined models achieved AUCs of 0.663, 0.783 and 0.811; the combined 95% CI was 0.770--0.847. The reference grouped mosaic and aneuploid embryos as non-euploid. The combined input-and-learner configuration yields the highest point estimate on this common population. A fixed-learner ablation separates modality content from the interaction mechanism used to encode it [@EMBRYO06].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Multitask embryo morphology, ploidy and live-birth prediction |  |
| **Inputs** | Static images, time-lapse videos, maternal/clinical metadata |  |
| **Prediction time** | Stage-specific morphology; blastocyst ploidy; transfer-time live birth |  |
| **Analysis unit** | image/embryo for morphology/ploidy; transfer for live birth |  |
| **Method** | IVFormer transformer with visual-temporal contrastive learning (VTCLR); supervised fine-tuning and multimodal combination |  |
| **Supervision / labels** | Self-supervised pretraining; morphology, PGT-A and live-birth labels downstream |  |
| **Outcome** | Multiple distinct morphology, genetic and clinical endpoints |  |
| **Sample sizes** | [{"value": 41279, "unit": "pretraining images", "locator": "Methods / Pre-training dataset; P106"}, {"value": 2136, "unit": "pretraining videos", "locator": "P106"}, {"value": 520, "unit": "internal PGT embryos", "locator": "Methods / Downstream tasks; P108"}, {"value": 256, "unit": "external PGT embryos", "locator": "P108"}] |  |
| **Splitting** | Development/internal 2:1; pretraining train/tune 9:1. Explicit patient-disjoint internal and external datasets (P104-P108). |  |
| **Validation** | Internal validation; external PGT and separate single-/double-transfer live-birth cohorts. |  |

## Source-linked excerpts
- [EMBRYO06-B0015] ==The multimodal development corpus contained 41,279 static images and 2,136 time-lapse videos, followed by morphology, ploidy and live-birth downstream tasks.==
- [EMBRYO06-B0054] ==Internal datasets were patient-disjoint and external Chinese cohorts included 256 PGT-A embryos and 1,831 single- or double-embryo transfers.==
- [EMBRYO06-B0025] ==Combined video and metadata achieved internal ploidy AUC 0.811, the external human comparison used 256 embryos and score-bin ranking.==
- [EMBRYO06-B0040] ==All development and external validation cohorts were Chinese, retrospective ranking analyses do not establish that using the system improves live birth.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*