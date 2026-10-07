# EC066 — Machine learning center-specific models show improved IVF live birth predictions over US national registry-based model.

**Yao, Nguyen, Retzloff et al. (2025).** *Nature communications*. DOI: [10.1038/s41467-025-58744-z](https://doi.org/10.1038/s41467-025-58744-z)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Learning objectives and the interpretation of model outputs, Design challenges and directions for validated AI

**PDF:** see EC066.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Probability estimation, discrimination and calibration
> ==A six-centre evaluation compares centre-specific boosted models with SART formulas in selected first cycles under age 40 that meet both models' input requirements. The evaluation concerns participating centres and uses different prediction streams: ROC-AUC derives from cross-validated responses, whereas Brier, precision-recall and threshold F1 derive from production responses. The learned-model positive label includes ongoing pregnancy, with a sensitivity analysis excluding those cases. Each metric characterizes its corresponding prediction stream and label definition. Brier quantifies overall probabilistic error; calibration analysis isolates the agreement between predicted probabilities and observed frequencies [@EC066].==

> **§ Design challenges and directions for validated AI** : Isolating the contribution of a computational mechanism
> ==Table entry; table caption: Source-located limitations and studies that could address them. — Cross-validated and production prediction streams [@EC066]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Compare center-specific pretreatment live-birth models with SART and evaluate temporal stability. | EC066-B0007 EC066-B0008 |
| **Inputs** | Pretreatment age, BMI, AMH, diagnoses, birth history and additional center-specific reserve measures. | EC066-B0044 |
| **Prediction time** | Pretreatment counseling. | EC066-B0007 EC066-B0044 |
| **Analysis unit** | IVF cycle/patient, linking fresh and frozen transfers to the retrieval cycle. | EC066-B0042 EC066-B0045 |
| **Method** | Center-specific Bernoulli gradient-boosted machines; updated MLCS versions compared with SART and age models. | EC066-B0038 EC066-B0049 |
| **Supervision / labels** | Observed live-birth or ongoing-pregnancy labels; SART handles ongoing pregnancies differently. | EC066-B0042 EC066-B0050 |
| **Outcome** | At least one live birth or ongoing pregnancy; DNMV2 removes ongoing-pregnancy cases. | EC066-B0042 EC066-B0050 EC066-B0051 |
| **Sample sizes** | {"centers": 6, "locations": 22, "states": 9, "DNMV1_first_cycles": 4645, "intro_inconsistent_count": 4635, "DNMV2_excluded_ongoing_pregnancy_fraction_approx": 0.048} | EC066-B0007 EC066-B0048 EC066-B0051 |
| **Splitting** | Internal k-fold CV and later same-center temporal testing; first-cycle DNMV comparisons; recurrent cycles weighted. | EC066-B0009 EC066-B0045 EC066-B0048 |
| **Validation** | Discrimination, Brier score, calibration, PR-AUC, F1 and temporal assessment across six centers. | EC066-B0008 EC066-B0015 EC066-B0016 |

## Source-linked excerpts
- [EC066-B0007] ==The study compared center-specific and SART pretreatment models across six geographically distributed US centers using discrimination, calibration, and error-sensitive metrics.==
- [EC066-B0015] ==Median ROC-AUC did not differ, while Brier score was statistically better for MLCS2 across the six centers.==
- [EC066-B0016] ==MLCS2 had higher median PR-AUC and higher F1 at the 50% threshold than SART.==
- [EC066-B0028] ==The authors limit inference to six US centers and state that the design cannot attribute improvement to machine learning or localization itself.==
- [EC066-B0042] ==The MLCS positive outcome label includes either live birth or documented ongoing clinical pregnancy.==
- [EC066-B0066] ==The disclosures identify commercial employment, equity, patents, and related financial interests among several authors.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*