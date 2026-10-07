# EE047 — Development and validation of deep learning based embryo selection across multiple days of transfer.

**Theilgaard Lassen, Fly Kragh, Rimestad et al. (2023).** *Scientific reports*. DOI: [10.1038/s41598-023-31136-3](https://doi.org/10.1038/s41598-023-31136-3)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE047.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Direct video encoders and shared representations
> ==The later iDAScore development study uses separate pathways for early and blastocyst-stage transfer days and treatment-level splitting. Its multicenter dataset supports internal evaluation. The v1 comparator had previously trained on some v2 test samples, giving the compared versions different exposure histories on the evaluation set [@EE047].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict embryo implantation potential for day-2, day-3 and day-5+ transfer. | EE047-B0009 |
| **Inputs** | Raw multifocal EmbryoScope time-lapse images; early model 20–84 hpi, late model 20–148 hpi. | EE047-B0008 EE047-B0009 |
| **Prediction time** | Day-specific model scores using available images through day 2, 3 or 5+; early/late windows differ. | EE047-B0009 |
| **Analysis unit** | Embryo prediction nested within IVF treatment; split grouped by treatment. | EE047-B0006 |
| **Method** | 3D-CNN day-5+ model; early implantation and direct-cleavage CNNs combined by logistic regression, day-wise calibration and 1.0–9.9 scaling. | EE047-B0009 |
| **Supervision / labels** | Known implantation fetal-heartbeat labels; discarded embryos treated as negative for training and all-embryo evaluation. | EE047-B0006 EE047-B0009 |
| **Outcome** | Separate discrimination for KID-positive versus KID-negative and versus KID-negative plus discard; calibration on KID population. | EE047-B0011 |
| **Sample sizes** | {"source_embryos": 249635, "source_treatments": 34620, "clinics": 22, "eligible_embryos": 181428, "transferred_KID": 33687, "discarded": 147741, "training_embryos": 154875, "test_embryos": 26553} | EE047-B0006 EE047-B0007 |
| **Splitting** | 85/15 treatment-level split; all embryos of a treatment kept together. Same patient across separate treatments not explicitly addressed. | EE047-B0006 |
| **Validation** | Multicenter pooled internal test AUROC/DeLong intervals and graphical calibration; independent-clinic holdout not stated in main methods. | EE047-B0011 |

## Source-linked excerpts
- [EE047-B0006] ==After exclusions, the study retained 181,428 embryos from 22 clinics, including 33,687 transferred embryos with known fetal-heartbeat outcomes and 147,741 discarded embryos.==
- [EE047-B0009] ==Separate three-dimensional CNN tracks handled cleavage and blastocyst stages, with day-specific calibration and discarded embryos sampled as negative examples.==
- [EE047-B0013] ==Transferred-embryo AUCs were 0.669, 0.621, and 0.707 for day 2, day 3, and day 5+, respectively, with lower-stage calibration ranges than day 5+.==
- [EE047-B0028] ==The authors identify internal validation as a limitation and call for external validation at new clinics and prospective clinical evaluation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*