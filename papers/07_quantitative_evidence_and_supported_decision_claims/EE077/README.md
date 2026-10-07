# EE077 — Consistency and objectivity of automated embryo assessments using deep neural networks.

**Bormann, Thirumalaraju, Kanakasabapathy et al. (2020).** *Fertility and sterility*. DOI: [10.1016/j.fertnstert.2019.12.004](https://doi.org/10.1016/j.fertnstert.2019.12.004)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Labels and denominators determine what a metric measures
> ==Rotation-based experiments measure sensitivity to image orientation. A CNN produces more consistent morphology and disposition outputs than participating embryologists on the examined set. This is a repeatability result under a defined input transformation. Clinical-policy evaluation extends the question from consistency of decisions to the transfer outcomes that follow them [@EE077].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Compare reproducibility of CNN embryo grades and biopsy/cryopreservation disposition with embryologists. | EE077-B0008 EE077-B0009 |
| **Inputs** | Static70hpi/113hpi images; original and90/180/270degree rotations for disposition experiment. | EE077-B0007 |
| **Prediction time** | 70hpi and113hpi morphological assessment. | EE077-B0008 |
| **Analysis unit** | Embryo image; four rotated presentations of each of56blastocysts are repeated measures. | EE077-B0008 EE077-B0009 |
| **Method** | Previously trained CNN five-class developmental-quality classifier; repeat inference and rotation tests. | EE077-B0007 |
| **Supervision / labels** | Expert morphology annotations for prior CNN training; current evaluation studies reader agreement and decision consistency. | EE077-B0007 |
| **Outcome** | Grade agreement,inter/intraobserver variability and rotation-invariant biopsy/freeze/discard decisions. | EE077-B0008 EE077-B0009 |
| **Sample sizes** | {"source_embryos": 3469, "70hpi_test_images": 748, "113hpi_test_images": 742, "rotation_embryos": 56, "rotation_presentations": 224, "embryologists_total": 10} | EE077-B0007 EE077-B0008 EE077-B0009 |
| **Splitting** | Evaluated embryos stated independent of CNN training; this report does not provide full training-partition counts. | EE077-B0007 |
| **Validation** | Coefficient of variation,ICC,Cronbach alpha and rotation consistency; no pregnancy outcome evaluation. | EE077-B0010 |

## Source-linked excerpts
- [EE077-B0007] ==The CNN was trained on 3,469 normally fertilized embryo images at 70 and 113 hours, using five classes based on blastocyst quality; evaluation embryos were independent of training.==
- [EE077-B0009] ==Ten embryologists assessed 56 blastocysts at four rotations for biopsy and cryopreservation decisions, and consistency was defined as rotation-invariant decisions.==
- [EE077-B0011] ==Grading showed high inter-embryologist variability and low single-measure absolute agreement, while the network produced identical classifications across repeated runs.==
- [EE077-B0012] ==The CNN's reported disposition consistency was 83.92%, compared with 52.14% and 57.68% average consistency for embryologists in the biopsy and cryopreservation tasks.==
- [EE077-B0016] ==The authors caution that neural-network performance is not automatically generalizable across imaging systems or datasets and depends on training data and methods.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*