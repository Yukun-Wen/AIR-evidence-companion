# EE013 — Stability and reliability of artificial intelligence models in embryo selection for in vitro fertilization.

**Thirumalaraju, Kanakasabapathy, Kandula et al. (2026).** *Fertility and sterility*. DOI: [10.1016/j.fertnstert.2025.08.021](https://doi.org/10.1016/j.fertnstert.2025.08.021)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims, Design challenges and directions for validated AI

**PDF:** see EE013.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Labels and denominators determine what a metric measures
> ==Training reproducibility provides another measurable property of a selection model. A CNN study varies random seeds and finds that similar aggregate discrimination can coexist with different within-patient rankings, including at a separate centre. This experiment measures the stability of proposed ordering under repeated fitting. Reporting rank agreement alongside performance uncertainty exposes variability in the decision that users receive [@EE013].==

> **§ Design challenges and directions for validated AI** : Isolating the contribution of a computational mechanism
> ==Table entry; table caption: Source-located limitations and studies that could address them. — Similar AUC with seed-dependent sibling rankings [@EE013]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Evaluate seed-to-seed stability of live-birth-trained embryo scores and within-patient rankings. | EE013-B0004 EE013-B0008 |
| **Inputs** | Static day-5 embryo images at 110±3 h post-insemination; no PGT or grade inputs during training. | EE013-B0005 EE013-B0007 |
| **Prediction time** | Day 5 at 110±3 h after insemination. | EE013-B0005 |
| **Analysis unit** | Embryo image for prediction; patient embryo cohort for ranking; transferred embryo for observed live-birth analysis. | EE013-B0008 EE013-B0013 |
| **Method** | Fifty replicate single-instance CNNs with identical architecture/data and different random initialization seeds; Grad-CAM and t-SNE analyses. | EE013-B0001 EE013-B0008 |
| **Supervision / labels** | Known live birth/non-live birth for transferred embryos; retrospective expert grades used only for critical-error evaluation. | EE013-B0007 EE013-B0014 |
| **Outcome** | Kendall concordance, top-choice agreement with transfer, live birth among top-ranked transferred embryos, and degenerate-embryo critical errors. | EE013-B0009 EE013-B0011 EE013-B0012 EE013-B0015 |
| **Sample sizes** | {"MGH_images": 10713, "MGH_patients": 1258, "Cornell_images": 648, "Cornell_patients": 53, "ranking_patients_MGH": 92, "ranking_patients_Cornell": 49, "critical_error_patients_MGH": 83, "critical_error_patients_Cornell": 45} | EE013-B0005 EE013-B0006 EE013-B0008 EE013-B0015 |
| **Splitting** | MGH development and internal patient test cohorts; Cornell kept fully separate without retraining. Exact internal allocation deferred to supplement. | EE013-B0006 EE013-B0008 |
| **Validation** | Internal/external center stability evaluation across 50 seeds with task-specific eligible patient subsets; outcomes only known for transferred embryos. | EE013-B0008 EE013-B0013 EE013-B0015 |

## Source-linked excerpts
- [[EE013-B0005]] ==The primary data included 10,713 day-5 embryo images from 1,258 MGH patients, captured at 110 plus or minus 3 hours post-insemination.==
- [[EE013-B0006]] ==An independent Cornell dataset contained 648 images from 53 patients; centres remained separate and Cornell was evaluated without retraining.==
- [[EE013-B0008]] ==Fifty replicate models shared architecture and training data but varied random seed; within-patient embryo rankings were evaluated for 92 MGH and 49 Cornell patients with at least four embryos.==
- [[EE013-B0016]] ==Across the 50 models and 172-embryo test set, mean AUC was 60.02% with range 49.47%-71.78%, alongside wide variability in other metrics.==
- [[EE013-B0017]] ==Mean rank concordance across replicate models was low: Kendall W 0.3571 at MGH and 0.3410 at Cornell.==
- [[EE013-B0018]] ==A degenerate embryo was top-ranked despite an available blastocyst in a mean 12.41% of eligible MGH cohorts and 17.29% of Cornell cohorts, with broad seed-to-seed ranges.==
- [[EE013-B0023]] ==The authors emphasize that no definitive ground-truth total ranking exists and that conventional AUC/accuracy gives limited guidance for the clinically important ranking task.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*