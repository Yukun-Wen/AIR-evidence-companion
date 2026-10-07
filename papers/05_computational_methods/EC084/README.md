# EC084 — Machine Learning-Based Modeling of Ovarian Response and the Quantitative Evaluation of Comprehensive Impact Features.

**Liu, Shen, Liang et al. (2022).** *Diagnostics (Basel, Switzerland)*. DOI: [10.3390/diagnostics12020492](https://doi.org/10.3390/diagnostics12020492)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Response classification further illustrates information timing. One study develops poor-response models before stimulation and before trigger, with realized medication and follicular response entering the latter. Its selected pre-stimulation ANN and pre-trigger random forest use different information sets; algorithms are also compared within each stage. Repeated optimization uses the reported validation set, and AUC and reclassification summaries disagree. A separate ANN/SVR count model uses trigger-day estradiol and realized treatment duration; its normalized mean-impact statistic perturbs fitted inputs by ten percent to measure model sensitivity. The later-stage models support late-cycle prediction; their predictor sets specify the information available for that use [@EC046,EC084].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Regress number of oocytes retrieved and describe model feature effects. | EC084-B0005 |
| **Inputs** | 11 variables: age, infertility type/duration/cause, AFC, basal FSH, AMH, regimen, gonadotropin days/dose and trigger-day estradiol. | EC084-B0008 |
| **Prediction time** | At trigger/end of stimulation, inferred from trigger-day estradiol and completed treatment inputs. | EC084-B0008 |
| **Analysis unit** | Woman/IVF stimulation course. | EC084-B0007 |
| **Method** | Two-hidden-layer ANN (4,6 neurons) and Gaussian SVR; normalized mean-impact-value interpretation. | EC084-B0010 EC084-B0012 |
| **Supervision / labels** | Observed retrieved-oocyte count. | EC084-B0008 |
| **Outcome** | Continuous oocyte yield. | EC084-B0008 |
| **Sample sizes** | {"women": 1365, "centers": 1} | EC084-B0007 |
| **Splitting** | ANN 70% training, remainder validation/testing without stated proportions; SVR ten-fold CV. | EC084-B0011 EC084-B0012 |
| **Validation** | RMSE, correlation R and absolute-error bands; headline values include training/all-instance analysis rather than a clearly isolated common test set. | EC084-B0018 EC084-B0019 EC084-B0020 |

## Source-linked excerpts
- [EC084-B0007] ==The cohort comprised 1,365 women treated at one center, and candidate features included treatment duration, cumulative gonadotropin dose, and trigger-day estradiol.==
- [EC084-B0008] ==Eleven features selected by univariate correlation were used to predict continuous retrieved-oocyte count.==
- [EC084-B0011] ==The ANN used 70% for training with the remainder for validation/testing; split proportions and independence details for the remainder were not fully specified.==
- [EC084-B0019] ==Reported correlations between predictions and observed counts were 0.882 for ANN and 0.799 for SVR.==
- [EC084-B0031] ==The paper proposes iteratively changing dose until the model predicts a target count, using the sign of a model-derived feature-impact index.==
- [EC084-B0033] ==The authors identify single-center data and absence of oocyte/embryo quality, pregnancy, and live-birth outcomes as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*