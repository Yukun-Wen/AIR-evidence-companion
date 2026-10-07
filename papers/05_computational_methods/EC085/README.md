# EC085 — Machine Learning-Based Prediction of IVF Outcomes: The Central Role of Female Preprocedural Factors.

**Bereczki, Bukva, Vedelek et al. (2025).** *Biomedicines*. DOI: [10.3390/biomedicines13112768](https://doi.org/10.3390/biomedicines13112768)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==12 Baseline availability and population eligibility jointly define prognosis. A nine-feature XGBoost clinical-pregnancy model uses preprocedural variables in women reaching successful retrieval and tests a later cohort at the same centre. Its predictive-value summaries disagree with the confusion counts [@EC085]. A normal-TSH study compares RF, SVM and boosting with within-cycle predictors, reporting low sensitivity and high specificity for live birth. The prediction target is live birth within the normal-TSH population [@EC087].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy from preprocedural couple characteristics. | EC085-B0006 EC085-B0044 |
| **Inputs** | Female/male age, AMH, BMI, FSH, LH, sperm concentration/motility and infertility duration. | EC085-B0012 |
| **Prediction time** | Baseline first-visit counseling intended. | EC085-B0022 EC085-B0044 |
| **Analysis unit** | IVF/ICSI cycle with successful retrieval; repeated-patient grouping not specified. | EC085-B0042 EC085-B0044 |
| **Method** | XGBoost, gain-based feature reduction, training-only SMOTE and five-fold tuning. | EC085-B0046 EC085-B0047 EC085-B0049 |
| **Supervision / labels** | Clinical pregnancy positive/negative labels. | EC085-B0044 |
| **Outcome** | Gestational sac at 7 weeks, including ectopic pregnancies; not live birth. | EC085-B0044 |
| **Sample sizes** | {"reported_primary_IVF_ICSI_cycles": 1243, "reported_initial_observations": 1422, "later_validation_cycles": 92, "later_successful": 29, "later_unsuccessful": 63} | EC085-B0042 EC085-B0043 EC085-B0044 EC085-B0022 |
| **Splitting** | Stratified 80/20 split, five-fold training CV and locked same-center temporal validation. | EC085-B0043 EC085-B0044 EC085-B0047 EC085-B0051 |
| **Validation** | Internal discrimination and later 92-cycle confusion-matrix assessment without refitting. | EC085-B0013 EC085-B0021 EC085-B0022 EC085-B0051 |

## Source-linked excerpts
- [EC085-B0042] ==The retrospective primary cohort comprised 1243 IVF/ICSI cycles with successful oocyte retrieval at one centre.==
- [EC085-B0044] ==The binary endpoint was clinical pregnancy defined by a gestational sac at seven weeks; data were split 80/20.==
- [EC085-B0046] ==SMOTE was applied only to the training data to address class imbalance.==
- [EC085-B0013] ==The nine-feature test model achieved AUC 0.876, accuracy 81.67%, sensitivity 75.64%, and specificity 84.39%.==
- [EC085-B0022] ==The locked model's later same-centre cohort accuracy was 78.3%, with sensitivity 68.9% and specificity 82.5%.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*