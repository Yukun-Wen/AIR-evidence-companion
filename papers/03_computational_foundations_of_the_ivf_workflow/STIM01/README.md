# STIM01 — Optimizing oocyte yield utilizing a machine learning model for dose and trigger decisions, a multi-center, prospective study

**Canon, Leibner, Fanton et al. (2024).** *Scientific reports*. DOI: [10.1038/s41598-024-69165-1](https://doi.org/10.1038/s41598-024-69165-1)

**Role:** core · contrasts C20 · workflow: Stimulation and monitoring

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** see STIM01.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Stimulation: response prediction and treatment choice
> ==Canon and colleagues evaluated starting-dose and trigger support prospectively in 291 AI-supported patients against matched historical controls. The dose tool retrieves similar baseline cycles; the trigger tool uses current follicle measurements and estradiol. Mean mature-oocyte yield was 12.20 versus 11.24 (p=0.16). Matching allowed control reuse, and clinicians retained discretion. These outcomes characterize the combined use of starting-dose and trigger support in routine clinical decisions [@STIM01].==

> **§ Data, reference standards and the structure of evidence** : Tabular clinical data and treatment histories
> ==Canon's starting-dose model uses age, BMI, AMH and AFC to identify similar historical patients and construct a local dose-response curve. Scaling, missing-value handling and the reference population determine the meaning of similarity. The index patient's feature vector and the historical retrieval library jointly specify the recommendation mechanism [@STIM01].==

> **§ Computational methods** : Record construction and local estimation
> ==Local similarity retrieves comparable historical cases. Canon's starting-dose tool uses age, BMI, AMH and AFC to select neighbors, then fits a polynomial relating starting FSH dose to mature-oocyte yield. Its trigger tool models current follicles and estradiol linearly. Their combined prospective comparison with historical controls evaluates clinician-adjunct use [@STIM01].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | FSH starting-dose and trigger-timing decision support |  |
| **Inputs** | Baseline age, BMI, AMH, AFC; monitoring follicle-size distribution and estradiol |  |
| **Prediction time** | Before initial FSH prescription; monitoring visits from stimulation day 7 |  |
| **Analysis unit** | Patient/cycle |  |
| **Method** | 100-neighbour retrieval plus polynomial dose-response curve; interpretable linear regression trigger models |  |
| **Supervision / labels** | Historical dose/outcome observations; this study evaluates an existing deployed model |  |
| **Outcome** | MII and total oocytes, total FSH; safety and clinician agreement |  |
| **Sample sizes** | {"prospective_patients": 291, "centres": 2, "physicians": 4, "matching": "1:1 historical matching with replacement; Table 1 reports 291 matched control records, not necessarily 291 distinct control patients", "matched_control_records": 291} |  |
| **Splitting** | No new model training; LILY data excluded from model training/testing |  |
| **Validation** | Prospective observational evaluation, December 2022–April 2023, versus historical same-physician controls September 2021–September 2022 |  |

## Source-linked excerpts
- [STIM01-B0005] ==A prospective observational evaluation compared Stim Assist-supported dose and trigger decisions in 291 patients with propensity-matched historical controls.==
- [STIM01-B0019] ==The primary mature-oocyte and total-FSH comparisons were not statistically significant, a selected trigger-concordant subgroup was also reported.==
- [STIM01-B0029] ==The paper identifies the nonrandomized historical comparison and residual confounding as limitations and discloses commercial relationships.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*