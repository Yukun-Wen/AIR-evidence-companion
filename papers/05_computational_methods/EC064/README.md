# EC064 — Comparative analysis of convolutional neural networks and traditional machine learning models for IVF live birth prediction: a retrospective analysis of 48514 IVF cycles and an evaluation of deployment feasibility in resource-constrained settings.

**Liu, Wang, Huang et al. (2025).** *Frontiers in endocrinology*. DOI: [10.3389/fendo.2025.1556681](https://doi.org/10.3389/fendo.2025.1556681)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC064.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==Table entry; table caption: Selected tabular prediction designs and evaluation conditions. — CNN over a reshaped tabular pseudo-image [@EC064]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth from structured fresh-IVF records and compare computational deployment. | EC064-B0005 |
| **Inputs** | Clinical EMR variables including demographics, hormones, treatment, retrieved oocytes and embryo counts; described as 42 features reshaped to a 6×7 pseudo-image. | EC064-B0011 EC064-B0014 |
| **Prediction time** | After embryo development/counts are available; exact prediction time not stated, timing inferred from post-fertilization inputs. | EC064-B0014 |
| **Analysis unit** | Fresh IVF record/cycle; text alternates patients and cycles for the same total. | EC064-B0005 EC064-B0006 |
| **Method** | Custom two-convolution CNN versus naive Bayes, RF, decision tree and feedforward NN; XGBoost feature ranking and SHAP. | EC064-B0012 EC064-B0013 EC064-B0001 |
| **Supervision / labels** | Binary EMR live-birth versus non-live-birth outcome labels. | EC064-B0028 |
| **Outcome** | Live birth; detailed gestational-age/ascertainment definition not reported in examined methods/results. | EC064-B0001 EC064-B0028 |
| **Sample sizes** | {"fresh_IVF_records": 48514, "unique_patients": "unclear: source uses both patients and cycles"} | EC064-B0005 EC064-B0006 |
| **Splitting** | Stratified random 80/20 split; five-fold cross-validation on training data. Patient-level grouping and partition underlying each results table need verification. | EC064-B0010 EC064-B0019 |
| **Validation** | Internal accuracy, precision, recall, F1 and AUROC means/SD; local CPU/GPU feasibility. External validation not reported. | EC064-B0019 EC064-B0017 |

## Source-linked excerpts
- [EC064-B0006] ==The cohort is described as 48,514 patients undergoing fresh IVF cycles at one hospital from 2009 to 2018.==
- [EC064-B0010] ==Data were randomly split 80:20 and five-fold cross-validation was performed on the training portion.==
- [EC064-B0014] ==The predictor list includes baseline, stimulation, retrieval, fertilization, and embryo-quality variables, so prediction timing is not purely pretreatment.==
- [EC064-B0039] ==Random forest AUC was 0.9734 versus 0.8899 for CNN, while both had near-one recall.==
- [EC064-B0047] ==The authors acknowledge single-center data, lack of multimodal inputs, and omitted socioeconomic factors.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*