# EC047 — Streamlining follicular monitoring during controlled ovarian stimulation: a data-driven approach to efficient IVF care in the new era of social distancing.

**Robertson, Chmiel, Cheong (2021).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/deaa251](https://doi.org/10.1093/humrep/deaa251)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Changes, extrema and slopes compress serial observations into fixed trajectory summaries, complementing Section 5.3's full-sequence encoders [@R045]. Scan-day-specific models use evolving follicular measurements to predict clinician-selected trigger timing and a high-response proxy. Validation groups scans by cycle, with repeated-woman separation unspecified and eligibility changing by scan day. These outputs characterize prescribing patterns and proxy response at successive monitoring visits [@EC047].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict trigger day and ovarian over-response to study informative scan days. | EC047-H0111 |
| **Inputs** | Patient age, AFC and size-stratified follicle counts at the current ultrasound scan. | EC047-H0113 EC047-H0182 |
| **Prediction time** | Separate prediction on each baseline or stimulation scan day using information available that day. | EC047-H0111 EC047-H0113 |
| **Analysis unit** | Scan within cycle within woman; validation grouped by treatment cycle. | EC047-H0088 EC047-H0113 |
| **Method** | Random-forest regression and classification, each 100 trees; training-mean trigger-day baseline. | EC047-H0113 EC047-H0115 |
| **Supervision / labels** | Observed clinician-chosen trigger day and recorded over-response proxy for OHSS risk. | EC047-H0111 EC047-H0200 |
| **Outcome** | Trigger timing; high response defined in source as >18 follicles ≥11 mm on trigger day and/or 18 oocytes collected. This is an OHSS-risk proxy, not diagnosed OHSS. | EC047-H0111 |
| **Sample sizes** | {"women": 1875, "cycles_database": 2322, "ultrasound_scans": 9294, "cycles_model_figures": 2128} | EC047-H0088 EC047-H0185 |
| **Splitting** | Five-fold treatment-cycle cross-validation; mean imputation within fold; no hyperparameter tuning; patient-disjoint grouping not stated. | EC047-H0113 EC047-H0115 |
| **Validation** | Out-of-fold MSE and AUROC by scan day; tested patients differ across days because attendance differs; no external validation. | EC047-H0113 EC047-H0115 EC047-H0199 |

## Source-linked excerpts
- [EC047-H0088] ==The source comprised 9,294 scans from 2,322 cycles in 1,875 women at one center.==
- [EC047-H0113] ==Random-forest trigger-day regressors were evaluated by fivefold cross-validation at treatment-cycle level, with age missing in under 1% and mean-imputed within folds.==
- [EC047-H0119] ==After exclusions, 2,128 complete cycles from 1,731 patients were analyzed, and many patients contributed more than one cycle.==
- [EC047-H0190] ==Baseline over-response AUROC was 0.77 and exceeded 0.90 after stimulation day 5.==
- [EC047-H0200] ==The trigger target was the local multidisciplinary team's historical decision and may not have been outcome-optimal; scheduling and physician biases could influence it.==
- [EC047-H0201] ==The authors explicitly state that noninferiority of reduced monitoring cannot be inferred and call for randomized trials with live birth and OHSS outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*