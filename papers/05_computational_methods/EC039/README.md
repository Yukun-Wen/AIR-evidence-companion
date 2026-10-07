# EC039 — Development of an AI-based support system for controlled ovarian stimulation.

**Asada, Shinohara, Yonezawa et al. (2024).** *Reproductive medicine and biology*. DOI: [10.1002/rmb2.12603](https://doi.org/10.1002/rmb2.12603)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Action imitation learns recorded decisions. A LightGBM system predicts an expert's retrieval and medication choices from monitoring visits, including low-dose hCG for supplementation of LH activity. This target differs from trigger prescribing, and drug-specific agreement differs from complete-prescription agreement. Another ANN/SVR dose model duplicates records according to proximity of realized yield to a target before splitting the expanded rows, creating possible cross-partition copies unless grouped. Its later same-centre test evaluates agreement with clinician doses. The resulting objective is outcome-weighted prescribing imitation [@EC039,EC041].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Imitate expert decisions on oocyte retrieval timing and stimulation-drug prescriptions. | EC039-B0008 EC039-B0010 |
| **Inputs** | Follicle counts/sizes, hormones, age, AMH, stimulation day, prior prescriptions and longitudinal changes/moving averages. | EC039-B0013 EC039-B0016 |
| **Prediction time** | At each stimulation monitoring visit before deciding retrieval or next prescription. | EC039-B0007 EC039-B0010 |
| **Analysis unit** | Examination/visit nested in treatment cycle and patient. | EC039-B0012 EC039-B0015 |
| **Method** | LightGBM retrieval classifier and four drug/dose classifiers; compared in pre-validation with SVM, logistic regression and deep neural network. | EC039-B0017 |
| **Supervision / labels** | Recorded expert retrieval decision and expert re-review of prescription records according to current practice. | EC039-B0012 EC039-B0015 |
| **Outcome** | Retrieval versus continued stimulation; hMG/FSH product-dose, hCG dose, cetrorelix and estradiol prescription categories. | EC039-B0011 EC039-B0012 |
| **Sample sizes** | {"source_patients": 5969, "source_cycles": 7850, "retrieval_patients": 971, "retrieval_cycles": 1068, "retrieval_exams": 1345, "retrieval_positive": 316, "prescription_patients": 374, "prescription_cycles": 434, "prescription_exams": 1397} | EC039-B0012 EC039-B0015 |
| **Splitting** | Five-fold random sample cross-validation; patient/cycle grouping not specified. | EC039-B0013 EC039-B0014 EC039-B0016 |
| **Validation** | Internal cross-validation accuracy and AUROC, multiclass one-versus-rest average AUROC; pre-validation algorithm accuracy comparison. | EC039-B0017 EC039-B0018 EC039-B0022 |

## Source-linked excerpts
- [EC039-B0007] ==The source data were longitudinal IVF records containing repeated follicle, hormone, and procedure measurements collected across visits during stimulation.==
- [EC039-B0012] ==The retrieval-decision dataset included 971 patients, 1,068 cycles, and 1,345 examinations performed by an expert physician, labeled by whether the next visit was retrieval.==
- [EC039-B0015] ==The prescription models used 1,397 examinations from 434 cycles in 374 patients after expert re-review and predicted specific hMG, hCG, cetrorelix, and estradiol choices.==
- [EC039-B0026] ==Reported cross-validated average AUC was 0.948 for the prescription system, with component AUCs from 0.914 to 0.976.==
- [EC039-B0031] ==Only 56.2% of examinations had all four prescription outputs exactly correct; drug-level agreement ignoring amount was 76.2%.==
- [EC039-B0041] ==The implemented system was limited to antagonist stimulation, and the authors called for research on other protocols.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*