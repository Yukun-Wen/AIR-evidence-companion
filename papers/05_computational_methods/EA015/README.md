# EA015 — ILETIA: An AI-enhanced method for individualized trigger-oocyte pickup interval estimation of progestin-primed ovarian stimulation protocol

**Binjian Wu, Qian Li, Zhe Kuang et al. (2025).** *arXiv preprint*. DOI: []()

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Monitoring sequences and treatment feedback
> ==ILETIA combines transformer embeddings with boosted trees to estimate trigger-to-retrieval intervals. Its labels are observed timings in cycles already meeting a retrieval-rate criterion. Temporal testing evaluates reproduction of the timing patterns in those selected cycles, giving the learned interval a clear historical reference. Applying the interval as a recommendation defines a subsequent intervention with retrieval outcomes as the relevant endpoint [@EA015].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Recommend trigger-to-retrieval interval and predict premature ovulation. | EA015-P012 EA015-P013 |
| **Inputs** | Clinical, hormonal, follicular and medication variables; ovulation model adds estimated interval and MPA dose. | EA015-P012 EA015-P013 |
| **Prediction time** | Around trigger/OPU scheduling; some post-trigger variables require availability audit. | EA015-P012 EA015-P013 |
| **Analysis unit** | Patient cycle under a progestin-primed stimulation protocol. | EA015-P012 EA015-P017 |
| **Method** | ILETIA FT-Transformer with XGBoost classification, LightGBM regression and CTGAN augmentation. | EA015-P013 EA015-P015 EA015-P017 |
| **Supervision / labels** | Observed high-yield intervals and premature-ovulation labels. | EA015-P012 EA015-P013 |
| **Outcome** | Optimal-interval regression and premature-ovulation classification. | EA015-P012 EA015-P013 |
| **Sample sizes** | {"PPOS_patients": 8730, "interval_train": 8383, "interval_temporal_test": 274, "ovulation_original_positive": 95, "ovulation_selected_negative": 400, "ovulation_train": {"real_positive": 55, "synthetic_positive": 305, "negative": 360}, "ovulation_test": {"positive": 40, "negative": 40}} | EA015-P012 EA015-P017 |
| **Splitting** | Temporal regression split; balanced ovulation test of 40 positive/40 negative cases; synthetic positives restricted to training. | EA015-P012 EA015-P017 |
| **Validation** | Internal CV and later interval test; classifier evaluated on a selected balanced test population. | EA015-P016 EA015-P017 |

## Source-linked excerpts
- [EA015-P012] ==Dataset A included only cycles with oocyte-pickup rate at least 0.75 and intervals from 2,100 to 2,280 minutes, using 8,383 earlier cases for training and 274 later cases for testing.==
- [EA015-P006] ==The temporal test-set results were macro-AUROC 0.889 for interval classification and MAE 16.70 minutes with correlation 0.747 for interval regression.==
- [EA015-P007] ==The premature-ovulation dataset used 55 original positive cases to generate 305 synthetic positives, and its held-out balanced test set yielded AUROC 0.838.==
- [EA015-P017] ==The premature-ovulation test set deliberately contained 40 events and 40 controls, while training combined 360 controls with 55 real and 305 CTGAN-generated positive cases.==
- [EA015-P034] ==The retained main performance table confirms FTXGB test accuracy 0.821, F1 0.782, AUROC 0.889, and AUPR 0.819, only modestly above some deep-tabular baselines on AUROC.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*