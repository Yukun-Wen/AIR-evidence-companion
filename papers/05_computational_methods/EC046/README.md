# EC046 — Machine-intelligence for developing a potent signature to predict ovarian response to tailor assisted reproduction technology.

**Yan, Jin, Ding et al. (2021).** *Aging*. DOI: [10.18632/aging.203032](https://doi.org/10.18632/aging.203032)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Response classification further illustrates information timing. One study develops poor-response models before stimulation and before trigger, with realized medication and follicular response entering the latter. Its selected pre-stimulation ANN and pre-trigger random forest use different information sets; algorithms are also compared within each stage. Repeated optimization uses the reported validation set, and AUC and reclassification summaries disagree. A separate ANN/SVR count model uses trigger-day estradiol and realized treatment duration; its normalized mean-impact statistic perturbs fitted inputs by ten percent to measure model sensitivity. The later-stage models support late-cycle prediction; their predictor sets specify the information available for that use [@EC046,EC084].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict poor ovarian response before stimulation and before hCG trigger. | EC046-B0007 EC046-B0008 EC046-B0009 |
| **Inputs** | Baseline age,BMI,infertility,AMH,FSH,LH,E2,AFC,history; later model adds regimen,Gn dose/duration,trigger-dayE2 andfollicles. | EC046-B0008 EC046-B0009 |
| **Prediction time** | Two explicit stages:pre-COS and pre-hCG trigger. | EC046-B0050 |
| **Analysis unit** | Woman first IVF/ICSI treatment cycle. | EC046-B0006 |
| **Method** | LR/LASSO screening; ANN,RF,DT,XGBoost,SVM,LR compared; ANN favored pre-COS,RF pre-trigger in ResultsB0032. | EC046-B0010 EC046-B0032 |
| **Supervision / labels** | Supervised poor-response labels from oocyte retrieval/cancellation. | EC046-B0007 |
| **Outcome** | Four or fewer retrieved oocytes or cycle cancellation. | EC046-B0007 |
| **Sample sizes** | {"women_first_cycles": 1110, "poor_responders": 162, "normal_high_responders": 948} | EC046-B0006 EC046-B0026 |
| **Splitting** | Random 70/30 training/validation; validation described as used for repeated optimization as well as verification. | EC046-B0012 |
| **Validation** | Internal discrimination,calibration,C-index,NRI/IDI and reserve-marker comparisons; no multicenter validation. | EC046-B0035 EC046-B0042 EC046-B0051 |

## Source-linked excerpts
- [EC046-B0006] ==The cohort contained 1,110 women undergoing their first IVF/ICSI treatment at one center.==
- [EC046-B0007] ==Poor ovarian response was defined as retrieval of four or fewer oocytes or cycle cancellation.==
- [EC046-B0009] ==The hCG pre-trigger model added treatment regimen, cumulative gonadotropin exposure, stimulation days, trigger-day estradiol, and follicle count to baseline predictors.==
- [EC046-B0012] ==Patients were randomly divided 70/30 into training and internal validation datasets.==
- [EC046-B0032] ==Validation AUC was 0.859 for the selected pre-launch ANN and 0.903 for the selected pre-trigger random forest, versus logistic regression AUCs 0.848 and 0.883.==
- [EC046-B0051] ==The authors identify retrospective single-center design and absence of prediction for oocyte counts, embryo quality, or IVF outcomes as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*