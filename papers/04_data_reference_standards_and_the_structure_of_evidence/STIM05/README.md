# STIM05 — Explainable artificial intelligence to identify follicles that optimize clinical outcomes during assisted conception

**Hanassab, Nelson, Akbarov et al. (2025).** *Nature communications*. DOI: [10.1038/s41467-024-55301-y](https://doi.org/10.1038/s41467-024-55301-y)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Data, reference standards and the structure of evidence, Computational methods, Quantitative evidence and supported decision claims

**PDF:** see STIM05.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Partitioning, generalization and provenance
> ==Fjeldstad explicitly partitions patients for the outcome model. Hanassab uses first treatment cycles and nested leave-one-clinic-out validation, separating hyperparameter tuning from outer-clinic evaluation. McCallum reports both random image partitions and held-out-donor experiments. These designs address distinct forms of sample novelty and retain their evaluation levels in the synthesis [@OOCYTE02,STIM05,SPERM02].==

> **§ Computational methods**
> ==In the figure caption — Source-located quantitative examples for these mechanisms are presented in Table 7 STIM05,EMBRYO03,EMBRYO02,EMBRYO06==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Tree partitions and boosted ensembles (clinical variables / cycle) [@STIM05]==

> **§ Computational methods** : Nonlinear estimators and response targets
> ==Tree-based methods partition feature space through thresholds, and ensembles combine those partitions to represent nonlinear associations and interactions. Hanassab uses histogram-based gradient boosting on cycle-level follicle-size distributions to predict laboratory counts. The mature-oocyte analysis includes 14,140 first ICSI cycles from 11 clinics. Nested leave-one-clinic-out evaluation produced a mean absolute error (MAE) of 3.60 mature metaphase-II (MII) oocytes, with an SD of 0.35 across outer folds. Each of the 11 clinic holdouts uses a retrained model, quantifying cross-clinic prediction under observed trigger decisions. Permutation importance and SHAP identify the fitted prognostic contributions, connecting follicle-size distributions to predicted yield under the observed trigger decisions [@STIM05].==

> **§ Quantitative evidence and supported decision claims**
> ==Table entry; table caption: Selected numerical evidence across IVF tasks, with evaluation units and interpretation. — Mature-oocyte count; gradient boosting [@STIM05]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Identify follicle-size contributions to retrieved oocytes and downstream development |  |
| **Inputs** | Follicle-size distributions on trigger day, separately one/two days before trigger |  |
| **Prediction time** | Trigger day or specified preceding ultrasound day |  |
| **Analysis unit** | Patient's first treatment cycle; follicle measurements aggregated within cycle |  |
| **Method** | Histogram gradient-boosting regression; permutation importance and SHAP; nested leave-one-clinic-out tuning |  |
| **Supervision / labels** | Observed laboratory outcome counts |  |
| **Outcome** | Total oocytes, MII, 2PN zygotes, high-quality blastocysts; additional progesterone/live-birth association analyses |  |
| **Sample sizes** | {"patients_and_first_cycles": 19082, "clinics": 11, "MII_ICSI_cycles": 14140, "period": "2005–2023", "countries": 2} |  |
| **Splitting** | Outer held-out clinic; nested tuning on remaining ten clinics; first cycle per patient |  |
| **Validation** | Internal-external leave-one-clinic-out cross-validation; prospective impact not tested |  |

## Source-linked excerpts
- [STIM05-B0030] ==The study analyzed 19,082 treatment-naive patients from 11 UK and Polish clinics with histogram gradient boosting and leave-one-clinic-out validation.==
- [STIM05-B0009] ==Follicles around 13–18 mm contributed most to mature-oocyte yield, while associations with downstream fertilization, blastocyst and live-birth outcomes were smaller.==
- [STIM05-B0021] ==The retrospective design, follicle-measurement variability, substantial BMI/AFC missingness and lack of prospective trigger-policy testing limit causal interpretation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*