# EC033 — An artificial intelligence platform for automated measurement and count estimation of ovarian follicles during ovarian stimulation and IVF: a multicenter study.

**Wygocki, Zapala, Ulfig et al. (2026).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-025-03777-y](https://doi.org/10.1007/s10815-025-03777-y)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** see EC033.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Segmentation: constructing anatomical intermediates
> ==Follicle monitoring connects image measurement to workflow. One automated ultrasound system achieved an F1 of 89% (95% CI, 88--90%) on 702 test scans from 235 patients. In a separate prospective cohort, 265 of 904 scans from 269 patients required sonographer editing (29%; 95% CI, 26--32%). F1 summarizes detection across follicles; the scan-level edit rate quantifies review workload. A weakly supervised approach instead combines convolutional features and multiple-instance learning to reduce dense annotation. FUID contributes additional training data, and the biological partition unit is unspecified [@EC033,EC036].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Automated follicle detection, diameter measurement and counting in stimulation ultrasound scans. | EC033-B0005 EC033-B0016 |
| **Inputs** | Unprepared 2D transvaginal cine loops and smaller 3D ultrasound subset from multiple devices. | EC033-B0005 EC033-B0016 |
| **Prediction time** | Baseline stimulation day 1 and monitoring days 7–11; contemporaneous measurement. | EC033-B0012 EC033-B0023 |
| **Analysis unit** | Follicle/frame nested in scan, examination and patient. | EC033-B0013 EC033-B0017 |
| **Method** | Custom end-to-end deep-learning follicle recognition; detailed architecture delegated to supplement. | EC033-B0016 |
| **Supervision / labels** | Trained-annotator boxes verified by specialists; independent three-expert consensus test references blinded to AI. | EC033-B0017 EC033-B0018 EC033-B0019 |
| **Outcome** | Follicle detection/count/size, agreement and annotation time; prospective edit burden. | EC033-B0023 EC033-B0025 EC033-B0049 |
| **Sample sizes** | {"retrospective_patients": 1689, "retrospective_scans": 5508, "training_patients": 1372, "training_scans": 4399, "validation_patients": 55, "validation_scans": 305, "test_patients": 235, "test_scans": 702, "consensus_patients": 27, "consensus_scans": 102, "prospective_patients": 269, "prospective_scans": 904} | EC033-B0010 EC033-B0011 EC033-B0013 EC033-B0015 |
| **Splitting** | Patient subsets for training, threshold/hyperparameter validation, test and consensus test; multicenter/device data, center holdout allocation not specified here. | EC033-B0006 EC033-B0010 EC033-B0011 EC033-B0012 |
| **Validation** | Retrospective precision/recall/F1, count MAE/MAPE and agreement; scan-bootstrap intervals; prospective PACS workflow/edit evaluation. | EC033-B0025 EC033-B0027 EC033-B0028 EC033-B0049 |

## Source-linked excerpts
- [EC033-B0005 to EC033-B0015 (Datasets and design)] ==The retrospective corpus comprised 5,508 scans from 1,689 patients across international IVF clinics, with separate train/validation, independent test, and 102-scan three-expert consensus subsets; a prospective PACS-integrated cohort included 904 scans from 269 patients.==
- [EC033-B0017 to EC033-B0020 (Reference annotations)] ==Retrospective annotations were specialist-reviewed; the consensus subset used three independently annotating IVF sonographers who reconciled disagreements without seeing AI predictions, creating a stronger but still human-perception-based reference.==
- [EC033-B0033 to EC033-B0035 (Table 3)] ==For follicles at least 10 mm, model precision, recall, and F1 were 98.2%, 88.9%, and 93.3%; for all follicles recall fell to 68.9%, and for follicles under 10 mm it was 60.8%, lower than the expert average.==
- [EC033-B0039 and EC033-B0043 to EC033-B0045 (Count, size, device results)] ==Large-follicle count agreement was high, baseline antral-follicle count had larger error, diameter MAE versus experts averaged 0.74 mm, and independent-test performance was reported as stable across five ultrasound systems.==
- [EC033-B0046 to EC033-B0049 (Workflow results)] ==On 25 consensus scans AI-assisted review reduced annotation time, while in the prospective workflow 29% of scans needed at least one edit and 3.57% of follicles were edited; this cohort was explicitly designed for usability rather than clinical outcomes.==
- [EC033-B0061 and EC033-B0070 (Limitations and conflicts)] ==The paper acknowledges consensus ground truth and attention biases and weaker performance on small, irregular, or poor-quality follicles; several authors are employees or an owner of the company commercializing the system.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*