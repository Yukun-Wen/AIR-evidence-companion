# EC054 — Prediction of oocyte maturation rate in the GnRH antagonist flexible IVF protocol using a novel machine learning algorithm - A retrospective study.

**Houri, Gil, Danieli-Gruber et al. (2023).** *European journal of obstetrics, gynecology, and reproductive biology*. DOI: [10.1016/j.ejogrb.2023.03.022](https://doi.org/10.1016/j.ejogrb.2023.03.022)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Available information determines the prediction question
> ==The same timing audit applies to intermediate laboratory outcomes. An XGBoost study of 462 first IVF/ICSI cycles classifies high maturation as at least 80% MII among oocytes denudated for micromanipulation. Its input list and importance analysis include the number of oocytes retrieved, alongside monitoring measurements. That complete predictor becomes available after retrieval. A pre-trigger implementation would require a separately specified and evaluated predictor using only measurements acquired by that earlier decision [@EC054].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify high versus low oocyte-maturation rate in a first flexible GnRH-antagonist IVF/ICSI cycle. | EC054-H0040 EC054-H0045 |
| **Inputs** | Patient baseline and treatment variables including trigger-day/antagonist-start hormones, follicle measures, doses, demographics and the number of oocytes retrieved. The latter is explicitly a model input and an important feature. | EC054-H0045 EC054-H0058 EC054-H0059 |
| **Prediction time** | The complete evaluated input set is only available after oocyte retrieval. Baseline/pre-trigger decision-support language is inconsistent with inclusion of retrieved-oocyte count; no separately evaluated early-input-only model is established. | EC054-H0043 EC054-H0045 EC054-H0058 EC054-H0065 |
| **Analysis unit** | Woman's first IVF/ICSI cycle; one included cycle per patient in this selected cohort. | EC054-H0042 EC054-H0045 EC054-H0050 |
| **Method** | XGBoost decision-tree ensemble with feature-importance ranking. Generic neural-network wording elsewhere in the report is inconsistent with the explicit implemented XGBoost methods and is not treated as a second model. | EC054-H0046 EC054-H0056 EC054-H0058 |
| **Supervision / labels** | Maturation rate is MII count divided by the number of oocytes denuded/exposed to micromanipulation; high label≥80% versus low<80%. | EC054-H0044 EC054-H0050 |
| **Outcome** | Binary high-maturation classification; pregnancy is a descriptive group outcome rather than the learned endpoint. | EC054-H0044 EC054-H0053 EC054-H0056 EC054-H0061 |
| **Sample sizes** | {"women_first_cycles": 462, "high_maturation_at_least_80_percent": 236, "low_maturation_below_80_percent": 226, "training_percent": 80, "test_percent": 20, "centres": 1, "maximum_age_years": 38} | EC054-H0042 EC054-H0044 EC054-H0045 EC054-H0047 EC054-H0050 |
| **Splitting** | Random80/20 split of the462 first-cycle patients; exact partition counts, nested tuning and repeated evaluation are not specified in the examined methods. | EC054-H0047 |
| **Validation** | Internal holdout accuracy75% and AUROC0.78; Discussion reports95%CI0.73–0.82. ROC caption calls it the whole cohort, creating ambiguity with the held-out evaluation description. No external or prospective treatment-policy validation is established. | EC054-H0047 EC054-H0056 EC054-H0057 EC054-H0061 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*