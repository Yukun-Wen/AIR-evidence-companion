# EC035 — Real-world use of an artificial intelligence-powered clinical decision support tool for ovarian stimulation.

**Bixby, Miller (2025).** *F&S reports*. DOI: [10.1016/j.xfre.2025.01.015](https://doi.org/10.1016/j.xfre.2025.01.015)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==An observational implementation study combines neighborhood-based starting-dose software with regression-based trigger support. Relative to historical controls, clinician-adjunct use is associated with lower FSH exposure and no detected difference in mean mature-oocyte yield. Matching with replacement permits repeated control patients. The historical comparison estimates the association between adjunct use and observed treatment outcomes. Neighborhood retrieval for modeling, control matching and imputation perform separate computational roles [@EC035].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Evaluate real-world adjunctive ovarian stimulation decision support. | EC035-B0006 EC035-B0010 |
| **Inputs** | Starting-dose tool:AMH,AFC,BMI; trigger tool:latest estradiol and follicle measurements. | EC035-B0007 EC035-B0008 |
| **Prediction time** | Starting dose before stimulation and trigger predictions during stimulation. | EC035-B0007 EC035-B0008 EC035-B0011 |
| **Analysis unit** | Patient treatment episode in observational implementation comparison. | EC035-B0010 EC035-B0012 |
| **Method** | Stim Assist combines KNN neighborhood dose-response curves with interpretable linear trigger/yield models. | EC035-B0007 EC035-B0008 |
| **Supervision / labels** | Previously developed models learned MII yields and hormone responses; current study evaluates outcomes without new model training. | EC035-B0007 EC035-B0008 EC035-B0013 |
| **Outcome** | MII oocyte count,starting/totalFSH dose,peakE2 and severeOHSS. | EC035-B0013 EC035-B0014 |
| **Sample sizes** | {"AI_treated_patients": 292, "matched_historical_control_records": 292, "missing_AMH_or_AFC_imputed": 49, "historical_starting_dose_training_cycles": 18591, "historical_trigger_training_cycles": 30278} | EC035-B0007 EC035-B0008 EC035-B0012 EC035-B0014 |
| **Splitting** | 2022–2023 AI-use cohort vs 2019–2022 historical controls; nearest-neighbor 1:1 matching with replacement on age,AMH,AFC. | EC035-B0010 EC035-B0012 |
| **Validation** | Single-site observational postmarket comparison with age subgroups; no randomized assignment or live-birth endpoint. | EC035-B0010 EC035-B0013 EC035-B0027 |

## Source-linked excerpts
- [EC035-B0006 to EC035-B0009 (AI software)] ==Stim Assist combines a K-nearest-neighbor starting-dose curve trained on 18,591 cycles with linear-regression trigger models trained on 30,278 cycles and provides predictions rather than mandatory recommendations.==
- [EC035-B0010 to EC035-B0013 (Design and analysis)] ==At one US clinic, 292 AI-assisted cycles from 2022-2023 were matched with replacement to historical cycles from 2019-2022 on age, AFC, and AMH; simple t tests compared MII yield and FSH use.==
- [EC035-B0014 to EC035-B0016 (Primary results and Table 1)] ==Seventeen percent of exposed patients had AMH or AFC imputed; mean MII oocytes were similar (11.17/11.18 versus 11.25), while starting and total FSH were lower in the AI period (397 versus 444 IU and 4,182 versus 4,655 IU).==
- [EC035-B0019 to EC035-B0022 (E2 and sensitivity results)] ==Trigger-day estradiol did not differ significantly, and complete-case sensitivity matching retained lower FSH use with no statistically significant MII difference.==
- [EC035-B0027 to EC035-B0031 (Outcome boundaries and limitations)] ==The study did not assess fertilization, blastocyst, euploid, live-birth, or several adverse outcomes; it was single-center, nonrandomized, historically controlled, and subject to varying physician interpretation of the tool.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*