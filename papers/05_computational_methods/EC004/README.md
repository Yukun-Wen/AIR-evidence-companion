# EC004 — Ensemble machine learning models for sperm quality evaluation concerning success rate of clinical pregnancy in assisted reproductive techniques.

**Mehrjerd, Dehghani, Jajroudi et al. (2024).** *Scientific reports*. DOI: [10.1038/s41598-024-73326-7](https://doi.org/10.1038/s41598-024-73326-7)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational methods

**PDF:** see EC004.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Semen-derived vectors support both fertilization assessment and pregnancy prognosis. Yi compares machine-learning and logistic models using same-day semen characteristics in short-term IVF and rescue-ICSI pathways, with machine-learning partitioning incompletely specified. Mehrjerd combines routine semen variables in ensembles for pregnancy across IVF and ICSI. Metric choice changes the latter comparison: random forest has the higher AUC, while bagging has the higher accuracy. A defined threshold and treatment pathway connect these probabilities to prospective triage or sperm-selection decisions [@EC003,EC004].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy and fetal-heartbeat progression from semen quality in IVF/ICSI; separate IUI analysis. | EC004-B0003 |
| **Inputs** | Post-preparation CASA morphology, motility and sperm count. | EC004-B0034 EC004-B0041 |
| **Prediction time** | After sperm preparation before treatment outcome; this prediction time is inferred from the collection protocol. | EC004-B0034 |
| **Analysis unit** | Couple/treatment course; source uses these labels interchangeably. | EC004-B0032 |
| **Method** | Bagging, random forest, boosting, XGBoost and AdaBoost with SMOTE; RF SHAP interpretation. | EC004-B0041 EC004-B0043 |
| **Supervision / labels** | Supervised clinical-pregnancy labels from treatment records. | EC004-B0003 EC004-B0041 |
| **Outcome** | Early clinical pregnancy described as positive test or gestational sac at week 5; secondary fetal heartbeat around week 11. | EC004-B0003 |
| **Sample sizes** | {"ivf_icsi_initial": 734, "ivf_icsi_analyzed": 599, "iui_initial": 1197, "iui_analyzed": 954, "independent_patient_count": "unclear because couples/courses interchange"} | EC004-B0032 |
| **Splitting** | 80/20 train/test and 10-fold cross-validation; relationship between these schemes and timing of SMOTE are not specified. | EC004-B0041 |
| **Validation** | Internal accuracy and AUROC comparison; authors state no external validation or live-birth follow-up. | EC004-B0008 EC004-B0029 EC004-B0050 |

## Source-linked excerpts
- [EC004-B0031 to EC004-B0033] ==Data came from multiple Iranian infertility centers; after exclusions, 599 IVF/ICSI and 954 IUI courses remained, with mixed infertility etiologies and limited tabulated clinical covariates.==
- [EC004-B0040 to EC004-B0050] ==Models used only sperm morphology, motility, and count, with an 80/20 split, SMOTE for imbalance, and ten-fold cross-validation; five ensemble approaches were assessed mainly by accuracy and AUC.==
- [EC004-B0008 to EC004-B0018] ==Bagging and random forest were the strongest reported models; for IVF/ICSI, random forest had mean accuracy 0.72 and AUC 0.80, while morphology and count differed between successful and unsuccessful clinical-pregnancy groups.==
- [EC004-B0020 to EC004-B0025] ==The paper proposes sperm-count and morphology cutoffs and interprets SHAP directions, but some quantities and units are internally unclear, including a morphology cutoff reported in million per milliliter and negative effects for higher sperm parameters.==
- [EC004-B0029] ==The authors acknowledge retrospective bias, insufficient diversity, uncontrolled female age and ovarian reserve, no external validation, and lack of live-birth or other long-term outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*