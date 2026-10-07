# EE058 — Development of a dynamic machine learning algorithm to predict clinical pregnancy and live birth rate with embryo morphokinetics.

**Yang, Peavey, Kaskar et al. (2022).** *F&S reports*. DOI: [10.1016/j.xfre.2022.04.004](https://doi.org/10.1016/j.xfre.2022.04.004)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Fixed morphokinetic summaries make temporal information available to conventional classifiers. A small study compares regression, trees and ensembles using manually annotated timing variables. Test discrimination is substantially lower than training discrimination, and the cluster comparison is nonsignificant. The training--test gap identifies feature stability and developmental-group reproducibility as central properties of this compact representation [@EE058].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy and live birth from embryo morphokinetic times. | EE058-B0013 EE058-B0016 |
| **Inputs** | Manually annotated PN fading through blastocyst times,reduced for collinearity to six timepoints. | EE058-B0011 EE058-B0013 |
| **Prediction time** | After blastocyst formation,prior to fresh/frozen transfer; inferred from latest required timing. | EE058-B0011 |
| **Analysis unit** | Transferred embryo,with concordant-outcome double transfers included. | EE058-B0005 EE058-B0013 |
| **Method** | LR,XGBoost,decision tree and RF (Yang-Peavey); separate k-means exploration. | EE058-B0013 EE058-B0015 |
| **Supervision / labels** | Clinical fetal heartbeat at6–7weeks and recorded live birth labels. | EE058-B0005 EE058-B0012 |
| **Outcome** | Separate pregnancy and live-birth predictions. | EE058-B0016 |
| **Sample sizes** | {"surveyed_embryos": 479, "analyzed_embryos": 367, "patients": "not_reported_in_examined_source"} | EE058-B0016 |
| **Splitting** | Random70/30 embryo split; patient/cycle grouping not stated. | EE058-B0013 |
| **Validation** | Internal AUROC and sensitivity/specificity; test pregnancyAUROC0.69,livebirth0.64. | EE058-B0014 EE058-B0016 |

## Source-linked excerpts
- [EE058-B0005] ==The retrospective single-center cohort included transferred blastocysts with complete annotations and excluded discordant-outcome double transfers.==
- [EE058-B0013] ==Embryos were randomly divided 70/30, and six morphokinetic time points remained after manual collinearity trimming for model comparison.==
- [EE058-B0016] ==Random Forest clinical-pregnancy AUC declined from 0.91 in training to 0.69 in testing, while live-birth AUC declined from 0.85 to 0.64.==
- [EE058-B0021] ==The authors identify morphology-based transfer selection, repeated patients, donor embryos, and heterogeneous laboratory and transfer practices as limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*