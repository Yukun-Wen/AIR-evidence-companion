# EC087 — The Influence of Pre-IVF Day 2 TSH Levels on Treatment Success and Obstetric Outcomes: A Retrospective Single-Center Analysis with Machine Learning-Based Data Evaluation.

**Nadasdi, Vedelek, Bereczki et al. (2025).** *Journal of clinical medicine*. DOI: [10.3390/jcm14134407](https://doi.org/10.3390/jcm14134407)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==12 Baseline availability and population eligibility jointly define prognosis. A nine-feature XGBoost clinical-pregnancy model uses preprocedural variables in women reaching successful retrieval and tests a later cohort at the same centre. Its predictive-value summaries disagree with the confusion counts [@EC085]. A normal-TSH study compares RF, SVM and boosting with within-cycle predictors, reporting low sensitivity and high specificity for live birth. The prediction target is live birth within the normal-TSH population [@EC087].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy and live birth while assessing baseline TSH/BMI associations. | EC087-B0003 |
| **Inputs** | 40 maternal, paternal, hormonal and procedural dimensions, including embryo score and transfer-day endometrium. | EC087-B0004 |
| **Prediction time** | Main model available at transfer, inferred from procedural predictors; baseline TSH alone measured day 2/3. | EC087-B0004 EC087-B0006 |
| **Analysis unit** | Woman undergoing IVF/ICSI. | EC087-B0013 |
| **Method** | SVM, RF, XGBoost with search/CV tuning, standardization and SMOTE; feature-importance/SHAP analysis. | EC087-B0011 EC087-B0012 |
| **Supervision / labels** | Clinical pregnancy at seven gestational weeks by intrauterine sac; recorded live birth. | EC087-B0004 |
| **Outcome** | Separate clinical-pregnancy and live-birth classifications. | EC087-B0004 |
| **Sample sizes** | {"initial_women": 1086, "analyzed_women": 996, "excluded_ectopic": 18, "excluded_missed_abortion": 22, "excluded_TSH": 50} | EC087-B0013 |
| **Splitting** | Random 80/20 for RF/XGBoost and 70/30 for SVM; RF five-fold and XGBoost ten-fold tuning; 50 SVM random states. | EC087-B0011 EC087-B0012 |
| **Validation** | Internal accuracy/AUROC and feature effects; authors explicitly note absence of independent-cohort testing. | EC087-B0001 EC087-B0037 |

## Source-linked excerpts
- [EC087-B0004] ==The study restricted inclusion to TSH 0.3-4.0 mIU/L and did not stratify thyroid autoimmunity or levothyroxine use.==
- [EC087-B0012] ==RF/XGBoost used 80/20 random splits and SVM 70/30, with SMOTE and standardization in preprocessing.==
- [EC087-B0013] ==Among 996 analyzed patients, pregnancy and live-birth rates did not differ significantly across TSH quartiles.==
- [EC087-B0021] ==RF/XGBoost AUCs were 0.76/0.74 for pregnancy and 0.67/0.61 for live birth; live-birth sensitivities were 11.11% and 8.33%.==
- [EC087-B0037] ==The authors cite retrospective design, unmeasured thyroid disease details, and absent independent testing as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*