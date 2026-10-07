# EC059 — Development and Validation of a Combined Model Integrating Early Pregnancy Ultrasound Radiomics and Clinical Features to Predict Live Birth Following Single Vitrified-Warmed Blastocyst Transfer.

**Liu, Liu, Xu et al. (2025).** *Reproductive medicine and biology*. DOI: [10.1002/rmb2.12698](https://doi.org/10.1002/rmb2.12698)

**Role:** core · contrasts C09 · workflow: Transfer and patient outcomes

**Cited in:** Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Ultrasound timing locates the target population within pregnancy. Gestational-sac and embryonic-bud radiomics combined with clinical variables predict live birth after ultrasound confirmation of a viable singleton pregnancy four weeks after blastocyst transfer [@EC059]. A delta-radiomics study uses changes between week-six and week-eight scans in selected viable singleton pregnancies. Its combined model exceeds the clinical comparator's reported test AUC, while delta features alone do not. Both designs use post-implantation information for prognosis among pregnancies meeting the imaging criteria [@EC075].==

> **§ Quantitative evidence and supported decision claims** : Conditional comparisons across model configurations
> ==The distinction extends to prediction time. Adding clinical factors to early-pregnancy ultrasound radiomics increases live-birth AUC from 0.708 to 0.718 in a 185-cycle test set [@EC059]. Because eligibility requires an established intrauterine pregnancy four weeks after transfer, the result informs post-implantation prognosis. Together, these examples show how a numerical increment becomes interpretable once its changed component, evaluation population and intended decision are recorded.==

> **§ Quantitative evidence and supported decision claims** : Conditional comparisons across model configurations
> ==In the figure caption: Six selected conditional performance comparisons. Open and filled points denote configurations A and B, with the right column giving the arithmetic difference B - — Six selected conditional performance comparisons. Open and filled points denote configurations A and B, with the right column giving the arithmetic difference B -==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth after established early pregnancy following single vitrified-warmed blastocyst transfer. | EC059-B0009 EC059-B0016 |
| **Inputs** | Radiomics of gestational-sac longitudinal/transverse views and embryonic bud plus clinical variables;final combined age,EMT,Rad-score. | EC059-B0017 EC059-B0018 EC059-B0019 EC059-B0039 |
| **Prediction time** | Four weeks after transfer with intrauterine singleton pregnancy and fetal cardiac activity confirmed. | EC059-B0009 |
| **Analysis unit** | Single-blastocyst-transfer cycle/early pregnancy. | EC059-B0009 EC059-B0027 |
| **Method** | Radiomics fusion,Mann–Whitney/correlation/LASSO selection,nine classifiers;AdaBoost clinical/radiomics/combined models. | EC059-B0019 EC059-B0020 EC059-B0021 EC059-B0025 EC059-B0038 |
| **Supervision / labels** | Retrospectively observed live-birth labels;manual ultrasoundROIs. | EC059-B0016 EC059-B0018 |
| **Outcome** | Viable infant delivery at≥28 weeks;multiple births count asone outcome. | EC059-B0016 |
| **Sample sizes** | {"cycles": 925, "training": 740, "test": 185, "training_live_birth": 624, "test_live_birth": 156, "repeat_ROI_assessment_patients": 200} | EC059-B0018 EC059-B0027 EC059-B0029 |
| **Splitting** | Random 8:2 cycle split with 5-fold model selection; patient repeat grouping not stated. | EC059-B0025 EC059-B0027 |
| **Validation** | Internal heldout AUC,classification,calibration andDCA; no prospective/external evaluation. | EC059-B0025 EC059-B0039 EC059-B0050 |

## Source-linked excerpts
- [EC059-B0009] ==Eligibility required an intrauterine singleton pregnancy confirmed four weeks after SVBT and usable ultrasound images, while multiple early failures were excluded.==
- [EC059-B0016] ==The primary endpoint was live birth, defined as delivery of a viable infant at 28 or more weeks.==
- [EC059-B0025] ==Nine classifiers were compared with five-fold cross-validation and multiple discrimination, classification, calibration, and decision-curve metrics.==
- [EC059-B0039] ==On the held-out test set, AUCs were 0.579 for clinical features, 0.708 for radiomics, and 0.718 for the combined model.==
- [EC059-B0050] ==The authors acknowledge retrospective single-center data, limited sample size, heterogeneous ultrasound equipment, omitted predictors, and subclinical-performance test AUC.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*