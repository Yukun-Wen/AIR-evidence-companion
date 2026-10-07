# EC053 — Personalized prediction of the secondary oocytes number after ovarian stimulation: A machine learning model based on clinical and genetic data.

**Zielinski, Pukszta, Mickiewicz et al. (2023).** *PLoS computational biology*. DOI: [10.1371/journal.pcbi.1011020](https://doi.org/10.1371/journal.pcbi.1011020)

**Role:** core · contrasts C10, C11 · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** see EC053.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Genetic inputs extend clinical-history representations. One study predicts MII-oocyte counts from clinical-genetic features and previous-cycle outcomes; extensive variant searches, repeated cycles and incompletely specified nesting leave selection optimism unresolved. A donor study classifies total-oocyte response using baseline, genetic and realized treatment variables in selected young donors, excluding very low responses. SHAP identifies predictive variants within this population. The studies share a pharmacogenetic motivation while defining different targets, information sets and generalization populations [@EC053,EC037].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict number of MII oocytes and evaluate incremental genetic features. | EC053-B0006 |
| **Inputs** | AMH,AFC at stimulation start,age,priorMII/prior-denuded-oocyte counts,PCOS;14-gene variants/haplotype-derived features. | EC053-B0019 EC053-B0024 EC053-B0036 |
| **Prediction time** | Baseline/start-of-stimulation with previous-cycle history; inferred from selected features, requiring genotyping availability. | EC053-B0019 EC053-B0024 |
| **Analysis unit** | IVF stimulation process nested in woman. | EC053-B0008 EC053-B0019 |
| **Method** | LightGBM100 trees,5 leaves,maxdepth 16,l 2 loss;clinical feature selection and SOM/haplotype genetic feature construction;SHAP. | EC053-B0011 EC053-B0012 EC053-B0031 EC053-B0034 |
| **Supervision / labels** | Supervised observed retrieved MII counts. | EC053-B0006 EC053-B0011 |
| **Outcome** | Continuous MII oocyte yield. | EC053-B0006 EC053-B0012 |
| **Sample sizes** | {"women": 6043, "IVF_processes": 9090, "clinical_only_group": {"women": 5779, "processes": 8574}, "genetic_group": {"women": 264, "processes": 516}} | EC053-B0008 EC053-B0019 EC053-B0021 |
| **Splitting** | Five-fold cross-validation; patient-level grouping and nested genetic-feature search not specified in B0011. | EC053-B0011 EC053-B0035 |
| **Validation** | InternalRMSE/MAE/MAPE;clinical-vsgenetic models described as trained on sameGroup 2;127 feature combinations evaluated; prospective validation requested. | EC053-B0022 EC053-B0023 EC053-B0035 EC053-B0036 EC053-B0045 |

## Source-linked excerpts
- [EC053-B0008] ==Data came from 6,043 women and 9,090 IVF processes across six Polish clinic locations, with exclusions based on gonadotropin type and AMH availability/range.==
- [EC053-B0011] ==LightGBM handled missing previous-cycle data and was evaluated with fivefold cross-validation.==
- [EC053-B0019] ==The clinical cohort contained 5,779 women/8,574 processes, while the genetic cohort contained 264 women/516 processes; first-day AFC and previous-cycle outcomes were selected predictors.==
- [EC053-B0035] ==One hundred twenty-seven combinations of engineered genetic features were tried on the same genetic cohort, and the best reduced RMSE by 0.18 oocytes.==
- [EC053-B0036] ==In the genetic cohort, adding selected genetic features improved RMSE from 3.53 to 3.35 oocytes and MAE from 2.58 to 2.48.==
- [EC053-B0045] ==The authors call for a large prospective clinical study to verify real-life concordance and performance.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*