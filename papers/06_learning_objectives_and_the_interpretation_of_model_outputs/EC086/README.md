# EC086 — Personal KPIs in IVF Laboratory: Are They Measurable or Distortable? A Case Study Using AI-Based Benchmarking.

**Mauchart, Wagner, Godony et al. (2025).** *Journal of clinical medicine*. DOI: [10.3390/jcm14196948](https://doi.org/10.3390/jcm14196948)

**Role:** core · workflow: Laboratory quality assurance

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Probability estimation, discrimination and calibration
> ==Case-mix-adjusted laboratory benchmarking uses predictions as a reference for observed outcomes. A random-forest study compares an embryologist's observed clinical-pregnancy rate with predicted rates. Age-related miscalibration contributes to that residual difference, alongside patient and treatment variation. Conflicting accounts of the operator's contribution to training cases add uncertainty about model exposure. Calibration and training provenance are therefore part of the operator benchmark itself [@EC086].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy for case-mix-adjusted laboratory operator benchmarking. | EC086-B0012 EC086-B0013 |
| **Inputs** | Age, BMI, FSH dose, early estradiol, indication, oocyte count and laboratory fertilization/blastocyst measures. | EC086-B0007 EC086-B0014 |
| **Prediction time** | After laboratory development indicators are available; retrospective KPI benchmarking rather than a clearly specified prospective decision time. | EC086-B0014 |
| **Analysis unit** | ICSI cycle, with pregnancy denominator restricted to cycles reaching embryo transfer. | EC086-B0006 EC086-B0015 |
| **Method** | Random forest pregnancy classifier with five-fold evaluation; strata-level calibration and observed–predicted comparisons. | EC086-B0012 EC086-B0016 |
| **Supervision / labels** | Ultrasound-confirmed gestational-sac clinical pregnancy from laboratory system. | EC086-B0006 EC086-B0012 |
| **Outcome** | Clinical pregnancy probability and expected versus observed operator/subgroup CPR; laboratory KPIs separately described. | EC086-B0008 EC086-B0013 |
| **Sample sizes** | {"institution_ICSI_cycles": 1294, "single_operator_cycles": 474, "single_operator_ET_subset": "not quantified in examined methods"} | EC086-B0006 EC086-B0012 |
| **Splitting** | Five-fold cross-validation on institutional dataset. Benchmark operator is included in development population; whether benchmark uses strictly out-of-fold predictions is unclear. | EC086-B0012 EC086-B0013 |
| **Validation** | Internal AUROC/accuracy/precision/recall plus calibration and subgroup observed–predicted analyses; no independent external evaluation. | EC086-B0013 EC086-B0016 |

## Source-linked excerpts
- [EC086-B0006] ==The benchmark analysis covered 474 ICSI cycles performed by a single senior embryologist, and CPR included only cycles reaching embryo transfer.==
- [EC086-B0012] ==The random forest was described as trained on 1294 institutional ICSI cycles and evaluated with fivefold cross-validation.==
- [EC086-B0013] ==Reported model performance was AUC 0.75, accuracy 0.78, precision 0.50, and recall 0.36.==
- [EC086-B0024] ==For patients older than 40, predicted CPR 0.18 exceeded observed CPR 0.11, and age-stratified calibration failed.==
- [EC086-B0036] ==The authors acknowledge small subgroups, a single embryologist, and absence of multi-operator or multicentre validation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*