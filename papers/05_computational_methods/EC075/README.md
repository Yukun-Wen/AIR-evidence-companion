# EC075 — An interpretable delta ultrasound radiomics model for predicting live birth outcomes in single vitrified-warmed blastocyst transfer.

**Liu, Wu, Huang et al. (2025).** *Journal of ovarian research*. DOI: [10.1186/s13048-025-01859-0](https://doi.org/10.1186/s13048-025-01859-0)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC075.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Ultrasound timing locates the target population within pregnancy. Gestational-sac and embryonic-bud radiomics combined with clinical variables predict live birth after ultrasound confirmation of a viable singleton pregnancy four weeks after blastocyst transfer [@EC059]. A delta-radiomics study uses changes between week-six and week-eight scans in selected viable singleton pregnancies. Its combined model exceeds the clinical comparator's reported test AUC, while delta features alone do not. Both designs use post-implantation information for prognosis among pregnancies meeting the imaging criteria [@EC075].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth from serial early-pregnancy ultrasound after SVBT. | EC075-B0007 |
| **Inputs** | Gestational-sac radiomics at weeks 6 and 8, concatenated with clinical variables including endometrial thickness. | EC075-B0009 EC075-B0013 EC075-B0014 |
| **Prediction time** | After gestational week 8, requiring both ultrasound scans. | EC075-B0007 EC075-B0012 |
| **Analysis unit** | Woman with established singleton intrauterine pregnancy. | EC075-B0007 EC075-B0022 |
| **Method** | Radiomics screening and LASSO; RF/SVM/LR comparisons; temporal feature fusion and SHAP. | EC075-B0013 EC075-B0014 EC075-B0016 EC075-B0019 |
| **Supervision / labels** | Observed live-birth labels and manually delineated ultrasound regions. | EC075-B0009 EC075-B0012 |
| **Outcome** | Single live infant delivered at or beyond 28 gestational weeks. | EC075-B0009 |
| **Sample sizes** | {"patients": 528, "train": 369, "test": 159, "live_births_total": 472, "live_births_train": 329, "live_births_test": 143, "ROI_repeat_cases": 200} | EC075-B0012 EC075-B0024 |
| **Splitting** | Random 70/30 patient split and five-fold LASSO tuning. | EC075-B0014 EC075-B0022 EC075-B0024 |
| **Validation** | Internal discrimination, calibration, Hosmer–Lemeshow and decision-curve analyses. | EC075-B0018 EC075-B0035 EC075-B0050 |

## Source-linked excerpts
- [EC075-B0007] ==Eligibility required confirmed intrauterine pregnancy and usable week-6 and week-8 ultrasound, while several early-loss states were excluded.==
- [EC075-B0014] ==Features underwent univariate filtering, correlation pruning, and LASSO with fivefold cross-validation before model construction.==
- [EC075-B0022] ==The 528 cases were randomly divided 70/30 into training and test groups.==
- [EC075-B0035] ==Test AUCs were 0.699 for age-only clinical data, 0.660 for delta radiomics, and 0.747 for the combined model; combined-model sensitivity was 0.476.==
- [EC075-B0050] ==The authors note retrospective, single-hospital design, class imbalance, and lack of specific imbalance correction.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*