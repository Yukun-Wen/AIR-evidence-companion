# EE066 — An artificial intelligence model (euploid prediction algorithm) can predict embryo ploidy status based on time-lapse data.

**Huang, Tan, Li et al. (2021).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-021-00864-4](https://doi.org/10.1186/s12958-021-00864-4)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE066.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==BELA derives a blastocyst score through multitask bidirectional LSTM processing, then combines it with age in logistic ploidy prediction. Its evaluation varies by age and aneuploidy contrast, with mosaics excluded [@EE026]. A multistage live-birth system also joins image and clinical information, using cohorts that include development-contributing clinics and a prospective nonrandomized selection comparison [@EE028]. Its inconsistent modality descriptions leave the exact fusion configuration uncertain. Together, these examples connect the fused output to three design choices: component inputs, clinical population and the role of the score in selection. Another ploidy model concatenates 3D-ResNet video features, manually annotated kinetics, age and embryo day. Its later cohort evaluates this feature combination under same-center temporal change. The confusion matrix and reported accuracy give inconsistent summaries of that evaluation [@EE066].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict embryo ploidy from video,morphokinetics and maternal age. | EE066-B0015 EE066-B0021 |
| **Inputs** | 64sampled frames across six developmental windows plus manually annotated kinetic parameters and patient age. | EE066-B0017 EE066-B0018 EE066-B0019 |
| **Prediction time** | Observation extends to132.5–136hpi before biopsy/cryopreservation. | EE066-B0017 |
| **Analysis unit** | Blastocyst nested within PGT cycle. | EE066-B0008 |
| **Method** | 3D-ResNet50 encoder with2048-dimensional representation,concatenation and fully connected fusion classifier. | EE066-B0018 EE066-B0021 |
| **Supervision / labels** | NGS euploid/aneuploid label; chromosome-specific mosaic thresholds; kinetic labels annotated and reviewed. | EE066-B0011 EE066-B0012 |
| **Outcome** | Euploid versus aneuploid classification. | EE066-B0011 EE066-B0021 |
| **Sample sizes** | {"initial_cycles": 469, "initial_blastocysts": 1803, "later_cycles": 155, "later_blastocysts": 523} | EE066-B0008 EE066-B0013 |
| **Splitting** | Ten subsets withD10fixedtest and rotatingD1–D9validation; later2019–2020same-center temporal validation; patient/cycle grouping unspecified. | EE066-B0013 |
| **Validation** | Internal and temporal-test AUROC; later cohort from same hospital,not independent-center validation. | EE066-B0013 EE066-B0022 |

## Source-linked excerpts
- [EE066-B0012] ==The model fused embryo images, manually marked kinetic parameters, and patient clinical information after excluding mosaics from the binary euploid/aneuploid dataset.==
- [EE066-B0013] ==Development used a fixed tenth as test data with rotating validation subsets, followed by a later December 2019-December 2020 cohort from the same center.==
- [EE066-B0025] ==Sequential additions raised AUC from 0.57 for one image to 0.80 for selected video windows plus clinical and kinetic features.==
- [EE066-B0028] ==The original confusion-matrix table reports 193/246 euploids and 175/221 aneuploids correctly classified in the later cohort.==
- [EE066-B0034] ==The authors acknowledge manual kinetic annotation, sample-size/overfitting concerns, and uncertain transportability from PGT patients to other infertility populations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*