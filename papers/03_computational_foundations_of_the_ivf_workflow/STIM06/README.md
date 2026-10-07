# STIM06 — Deep learning-based prediction of individualized Real-time FSH doses in GnRH agonist long protocols

**Kong, Xia, Wang et al. (2025).** *Journal of translational medicine*. DOI: [10.1186/s12967-025-06562-8](https://doi.org/10.1186/s12967-025-06562-8)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** see STIM06.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Stimulation: response prediction and treatment choice
> ==Canon and colleagues evaluated starting-dose and trigger support prospectively in 291 AI-supported patients against matched historical controls. The dose tool retrieves similar baseline cycles; the trigger tool uses current follicle measurements and estradiol. Mean mature-oocyte yield was 12.20 versus 11.24 (p=0.16). Matching allowed control reuse, and clinicians retained discretion. These outcomes characterize the combined use of starting-dose and trigger support in routine clinical decisions [@STIM01]. Kong and colleagues use accumulating hormone and follicular measurements to predict daily dose categories. A comparison with baseline-only models therefore changes the information window as well as the estimator [@STIM06].==

> **§ Computational foundations of the IVF workflow** : Stimulation: response prediction and treatment choice
> ==The supervised target then determines what personalization means computationally. Kong's dose categories represent observed prescriptions, supplemented by retrieval of similar successful cycles. Classification agreement measures reproduction of prescribing behaviour; mature-oocyte yield and complications measure the consequences of a prescribing policy. Observed action, downstream response and policy consequence define three distinct forms of supervision [@STIM06].==

> **§ Data, reference standards and the structure of evidence** : A hierarchy of observations
> ==Donation links oocyte providers to recipients; separate identifiers preserve their respective contributions to gamete characteristics and subsequent outcomes. The schema separates patient, cycle, object and image counts by partition. CTFE's reported total and partition counts disagree [@STIM06].==

> **§ Data, reference standards and the structure of evidence** : Tabular clinical data and treatment histories
> ==Longitudinal clinical data contain an additional observation process. Hormones and follicles are measured at visits, while prescriptions can be issued between or across visits. Representing every day as a dense vector generally requires a choice about absent measurements. Kong and colleagues use forward filling for dynamic monitoring data, while applying other imputation rules to static variables. The resulting sequence combines measured and carried-forward values, whose measurement times distinguish their clinical meaning [@STIM06].==

> **§ Computational methods** : Monitoring sequences and treatment feedback
> ==Clinical monitoring sequences encode measurements acquired during treatment. Kong's cross-temporal and cross-feature encoding model combines baseline attributes with serial hormones, follicles and monitoring measurements through D-TDNN-based branches. A fusion gate integrates their representations, and nearest-neighbor retrieval supplies dose recommendations from similar historical trajectories. The resulting representation supports both dose classification and case retrieval [@STIM06].==

> **§ Computational methods** : Monitoring sequences and treatment feedback
> ==CTFE uses ten-segment sliding windows for later stimulation days, aligning the input history among patients still under treatment. Its supervised target is recorded dose category, including stopping. Prescribing agreement measures how well these windows encode the clinician's next recorded action. Subsequent treatment outcomes form the endpoint for evaluating a policy that acts on those recommendations [@STIM06].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict daily FSH dose category across GnRH-agonist long-protocol stimulation |  |
| **Inputs** | Static demographics/reserve/history and dynamic hormones, endometrium, follicle monitoring |  |
| **Prediction time** | Daily during stimulation using accumulated monitoring; sliding windows after day 13 |  |
| **Analysis unit** | Patient-cycle sequence with daily decisions |  |
| **Method** | Cross-temporal/cross-feature D-TDNN encoders, fusion gate and nearest-neighbour retrieval in latent space |  |
| **Supervision / labels** | Observed physician dose categories; successful cycles defined by follicle response |  |
| **Outcome** | Dose class (stop, <80, 80–160, 160–240, >240); not live birth |  |
| **Sample sizes** | {"reported_total": 13788, "reported_training": 6761, "reported_validation": 2898, "reported_test": 4135, "period": "2018–2020", "centres": 1, "source_discrepancy": "Partitions sum to 13,794, differing from stated 13,788; requires human/source verification"} |  |
| **Splitting** | Random patient-level split; one cycle per patient explicitly retained |  |
| **Validation** | Internal held-out comparison against temporal baselines and LASSO; no prospective clinical intervention |  |

## Source-linked excerpts
- [STIM06-B0008] ==A single-centre retrospective long-protocol cohort was used to train a cross-temporal and cross-feature network to reproduce five categories of daily FSH dosing.==
- [STIM06-B0033] ==The reported CTFE accuracy was 0.7367 with weighted F1 0.7320, later-day sliding-window estimates were based on much smaller samples.==
- [STIM06-B0046] ==The endpoint was concordance with local physician prescriptions rather than optimization of oocyte, embryo, pregnancy or live-birth outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*