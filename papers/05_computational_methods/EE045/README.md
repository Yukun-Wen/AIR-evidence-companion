# EE045 — Delineating the heterogeneity of embryo preimplantation development using automated and accurate morphokinetic annotation.

**Zabari, Kan-Tor, Or et al. (2023).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-023-02806-y](https://doi.org/10.1007/s10815-023-02806-y)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE045.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==A ResNet18 annotation system converts frame probabilities into monotonic sequences through isotonic regression. This enforces developmental ordering, whereas an alternative postprocessing design permits reverse transitions. Annotation agreement evaluates the assigned stages; exploratory developmental clusters describe patterns in the resulting trajectories [@EE045,EE015].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Automate morphokinetic annotation and characterize developmental heterogeneity by clustering. | EE045-B0010 EE045-B0020 EE045-B0028 |
| **Inputs** | Central-plane time-lapse embryo frames sampled about every18minutes. | EE045-B0006 |
| **Prediction time** | Retrospective3–6day sequences; isotonic postprocessing uses developmental order across frames. | EE045-B0006 EE045-B0022 |
| **Analysis unit** | Frame for state classification; embryo sequence for event times and clustering. | EE045-B0006 EE045-B0010 |
| **Method** | Single-channel ResNet18,categorical cross-entropy,RAdam; isotonic regression followed by k-means of profiles. | EE045-B0013 EE045-B0022 EE045-B0028 |
| **Supervision / labels** | Trained embryologists provide event times converted to frame states; transition-near frames excluded from training. | EE045-B0006 EE045-B0010 |
| **Outcome** | 11-state probabilities,discrete morphokinetic timings and unsupervised embryo clusters. | EE045-B0011 EE045-B0019 EE045-B0028 |
| **Sample sizes** | {"resource_video_files": 67707, "manually_annotated_embryos": 20253, "centers": 4, "incubators": 11} | EE045-B0006 |
| **Splitting** | Embryo-separated20%test; remaining85/15train/validation; paragraph calls latter test but table names validation. | EE045-B0006 |
| **Validation** | Technical heldout frame/event assessment and exploratory developmental clustering; known implantation subgroup associations separate. | EE045-B0007 EE045-B0019 EE045-B0028 |

## Source-linked excerpts
- [EE045-B0006] ==The source dataset contained 67,707 videos from eleven incubators at four centers, including 20,253 manually annotated embryos with embryo-level separation of test and training material.==
- [EE045-B0032] ==Across 1918 held-out embryos, the automated states reached about 93% precision and recall, and automated versus manual event timing had R-squared 0.994.==
- [EE045-B0043] ==K-means clustering of 14,159 embryos that reached eight cells by 66 hours produced nine distinct morphokinetic groups independent of maternal-age differences.==
- [EE045-B0053] ==The authors explicitly state that prospective nonselection and randomized studies are needed before clinical implementation or benefit can be established.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*