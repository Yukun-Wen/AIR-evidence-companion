# EC088 — Bioinformatic Analysis of Complex In Vitro Fertilization Data and Predictive Model Design Based on Machine Learning: The Age Paradox in Reproductive Health.

**Lantzi, Papakonstantinou, Vlachakis (2025).** *Biology*. DOI: [10.3390/biology14050556](https://doi.org/10.3390/biology14050556)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==ANN/SVM live-birth models simulate transfer strategies through predictions conditional on historical treatment choices [@EC070]. A large historical ART analysis evaluates full-cycle and pre-cycle models using predominantly IVF and some donor-insemination records. Its narrative and model tables disagree on the processed denominator; repeated attempts also require patient-level accounting. Age associations are conditioned by the treatment-selection process represented in these records [@EC088].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Describe registry trends and predict live-birth occurrence with full and pre-cycle feature sets. | EC088-B0036 EC088-B0039 EC088-B0065 EC088-B0074 |
| **Inputs** | Thirty full-cycle or 18 author-designated pre-cycle registry variables. | EC088-B0039 EC088-B0067 EC088-B0077 |
| **Prediction time** | Full-cycle and intended pre-cycle models; availability of the total-livebirth predictor needs checking. | EC088-B0067 EC088-B0077 |
| **Analysis unit** | HFEA treatment record; descriptive corpus includes IVF and donor insemination. | EC088-B0036 EC088-B0050 |
| **Method** | AutoML comprehensive autopilot with 59 candidate models per feature set; AUC optimization and SHAP. | EC088-B0042 EC088-B0065 EC088-B0074 |
| **Supervision / labels** | Observed live-birth occurrence labels. | EC088-B0065 EC088-B0074 |
| **Outcome** | Registry live-birth occurrence, separate from the historical survival-style descriptive analysis. | EC088-B0064 EC088-B0065 |
| **Sample sizes** | {"historical_descriptive_attempts": 1546070, "processed_prediction_records": 665244, "full_features": 30, "precycle_features": 18, "candidate_models_each": 59, "sample_scope_ambiguity": "Methods50,000-row setting versus Results100%/64% usage"} | EC088-B0036 EC088-B0039 EC088-B0042 EC088-B0065 EC088-B0074 |
| **Splitting** | Stratified CV plus 20% holdout; patient grouping and exact fold count unclear. | EC088-B0042 |
| **Validation** | Internal model comparison and lift/discrimination plots; no independent intervention evaluation. | EC088-B0069 EC088-B0070 EC088-B0098 |

## Source-linked excerpts
- [EC088-B0036] ==The source registry covered 1,546,070 fertility-treatment attempts from 1991-2018.==
- [EC088-B0039] ==Modeling used 665,244 post-wrangling cases from 2010-2018 and created 30-feature complete and 18-feature pre-cycle datasets.==
- [EC088-B0042] ==The platform used stratified cross-validation and a 20% holdout, with automated selection among multiple model types.==
- [EC088-B0067] ==Embryos transferred had normalized importance 100% in the full model, with age second at 24.84%.==
- [EC088-B0077] ==Age was the most important pre-cycle feature, followed by the reason for producing embryos or storing eggs.==
- [EC088-B0098] ==The discussion acknowledges the need for continuing testing, validation, retraining, and bias control before clinical use.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*