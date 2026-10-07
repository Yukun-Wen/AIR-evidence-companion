# EC003 — Correlation analysis of a novel artificial intelligence optical microscope-assisted semen assessment system with IVF outcomes.

**Yi, Yang, Yang et al. (2025).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-025-03453-1](https://doi.org/10.1007/s10815-025-03453-1)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Semen-derived vectors support both fertilization assessment and pregnancy prognosis. Yi compares machine-learning and logistic models using same-day semen characteristics in short-term IVF and rescue-ICSI pathways, with machine-learning partitioning incompletely specified. Mehrjerd combines routine semen variables in ensembles for pregnancy across IVF and ICSI. Metric choice changes the latter comparison: random forest has the higher AUC, while bagging has the higher accuracy. A defined threshold and treatment pathway connect these probabilities to prospective triage or sperm-selection decisions [@EC003,EC004].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict short-term IVF fertilization failure requiring rescue ICSI and examine semen/outcome associations. | EC003-P002 EC003-P003 |
| **Inputs** | 55 LensHooke X1 PRO semen measurements covering concentration, pH, motility, trajectories and morphology. | EC003-P003 |
| **Prediction time** | Semen collected on oocyte-retrieval day before short-term fertilization outcome; retrieval-day prediction. | EC003-P002 EC003-P003 |
| **Analysis unit** | IVF treatment cycle linked to a semen sample; sperm measurements aggregated within sample. | EC003-P004 |
| **Method** | Univariate screening then forward-stepwise logistic regression; random forest, XGBoost and gradient boosting ROC comparisons. | EC003-P003 EC003-P004 |
| **Supervision / labels** | Supervised binary successful short-term IVF versus fertilization failure followed by rescue ICSI, from clinical records. | EC003-P002 EC003-P003 |
| **Outcome** | Rescue-ICSI requirement; secondary fertilization, 2PN, polyspermy, blastocyst and pregnancy associations. | EC003-P003 |
| **Sample sizes** | {"cycles": 330, "successful_short_term_IVF": 281, "rescue_ICSI": 49, "patients": "unique patient count not separately established"} | EC003-P002 EC003-P004 |
| **Splitting** | not_reported_in_examined_source: methods describe model fitting and ROC comparison without train/test or resampling partition. | EC003-P003 EC003-P004 |
| **Validation** | Apparent development ROC comparisons; independent held-out or external validation not reported in examined methods. | EC003-P003 EC003-P004 |

## Source-linked excerpts
- [EC003-P002 to EC003-P003] ==The cohort included 281 cycles with successful short-term IVF and 49 requiring rescue ICSI, after exclusions for older female age, low oocyte yield or maturity, PCOS, and immune factors; the AIOM produced 55 same-day semen variables.==
- [EC003-P003 to EC003-P004] ==Significant variables were entered into forward-stepwise logistic regression, followed by random forest, XGBoost, and gradient boosting analyses assessed by ROC curves; the text does not describe a held-out external test cohort.==
- [EC003-P005 to EC003-P006] ==The rescue-ICSI group had lower concentration and motility measures, larger average head dimensions, and shorter tails; logistic regression retained immotility, mean head length, and mean tail length, while single-variable AUCs were only 0.38 to 0.65.==
- [EC003-P006 to EC003-P007] ==XGBoost achieved a reported AUC of 0.88 (95% CI 0.78-0.98), sensitivity 0.78, specificity 0.90, and accuracy 0.88; the three retained variables did not correlate significantly with mature-oocyte fertilization or 2PN rates, although head and tail length correlated with polyspermy.==
- [EC003-P007 to EC003-P008] ==The authors note limited sample size, multifactorial pregnancy outcomes, no pregnancy-rate difference between groups, and the need for large prospective studies of embryo development and assisted-reproduction outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*