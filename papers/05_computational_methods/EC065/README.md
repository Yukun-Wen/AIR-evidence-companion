# EC065 — Predictive model for live birth outcomes in single euploid frozen embryo transfers: a comparative analysis of logistic regression and machine learning approaches.

**Abdala, Kalafat, Elkhatib et al. (2025).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-025-03524-3](https://doi.org/10.1007/s10815-025-03524-3)

**Role:** core · contrasts C12 · workflow: Transfer and patient outcomes

**Cited in:** Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : From cycle records to outcome prognosis
> ==Table entry; table caption: Selected tabular prediction designs and evaluation conditions. — LR, RF, SVM and XGBoost after euploid transfer [@EC065]==

> **§ Quantitative evidence and supported decision claims** : Validation changes define the tested scope of transportability
> ==Table entry; table caption: Validation designs test different forms of generalization and use. — Patient-grouped internal [@EC065]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth in single euploid frozen embryo transfer. | EC065-H0100 |
| **Inputs** | Patient characteristics, embryo morphology and biopsy day, preparation protocol and endometrial thickness; final parsimonious variables selected. | EC065-H0132 EC065-H0187 |
| **Prediction time** | Transfer-stage prediction; candidate inputs include distance from fundus after transfer, so not a wholly pretreatment information set. | EC065-H0132 |
| **Analysis unit** | Transfer cycle nested within couple. | EC065-H0136 |
| **Method** | LR, random forest, SVM and XGBoost; parsimonious variable selection and calibration. | EC065-H0133 |
| **Supervision / labels** | Recorded live-birth labels with repeated-couple effects in association analysis. | EC065-H0102 EC065-H0132 |
| **Outcome** | Binary live birth after seFET. | EC065-H0100 |
| **Sample sizes** | {"seFET_cycles": 1979, "couples": 1459} | EC065-H0136 |
| **Splitting** | Patient-separated random 60/40 partitions repeated 2000 times; final static four-fold CV for selected LR. | EC065-H0133 |
| **Validation** | Internal AUROC/AUPRC, discrimination shrinkage, calibration intercept and slope; web calculator deployment is not external validation. | EC065-H0133 EC065-H0351 |

## Source-linked excerpts
- [EC065-H0119] ==The cohort comprised autologous single euploid FET cycles using biopsied day-5 to day-7 blastocysts in natural or hormone-replacement endometrial preparation.==
- [EC065-H0132] ==Mixed-effects regression used random intercepts to account for repeated transfers from the same couple.==
- [EC065-H0133] ==Two thousand repeated splits were allocated by patient rather than cycle, and the best model underwent four-fold cross-validation.==
- [EC065-H0351] ==LR had the best validation C-statistic and calibration, while RF, SVM, and XGBoost showed more training-to-validation shrinkage; final AUROC was 0.63.==
- [EC065-H0556] ==The authors explicitly acknowledge the lack of external validation and the final model's modest AUC.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*