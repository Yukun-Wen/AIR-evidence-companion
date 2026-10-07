# EE050 — The use of voting ensembles to improve the accuracy of deep neural networks as a non-invasive method to predict embryo ploidy status.

**Jiang, Kandula, Thirumalaraju et al. (2023).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-022-02707-6](https://doi.org/10.1007/s10815-022-02707-6)

**Role:** core · contrasts C14 · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Voting ensembles combine a blastocyst CNN with clinical variables through SVM and neural classifiers. One ploidy study excludes inconsistent decisions, creating a selective classifier whose accuracy is interpreted together with retained coverage. Its larger morphology-association cohort addresses a separate analysis from the CNN test [@EE050].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict embryo ploidy from images and parental clinical information. | EE050-H0121 EE050-H0122 |
| **Inputs** | Day 5 blastocyst images, maternal age, AMH, sperm quality and fertilization information. | EE050-H0122 EE050-H0123 |
| **Prediction time** | Day 5 before trophectoderm biopsy. | EE050-H0122 |
| **Analysis unit** | Embryo nested in patient. | EE050-H0119 |
| **Method** | CNN, SVM and MLP components combined by soft voting. | EE050-H0121 EE050-H0122 EE050-H0123 |
| **Supervision / labels** | PGT-derived euploid and non-euploid labels, with indeterminate results grouped as non-euploid. | EE050-H0125 |
| **Outcome** | Embryonic ploidy classification. | EE050-H0125 |
| **Sample sizes** | {"imaging_embryos": 699, "imaging_patients": 248, "independent_test_embryos_reported": 140, "manual_morphology_comparison_embryos": 6828, "euploid_imaging": 339, "aneuploid_imaging": 360} | EE050-H0119 EE050-H0125 EE050-H0126 EE050-H0129 |
| **Splitting** | 140 held-out embryos among 699; patient grouping and the text describing training denominators require clarification. | EE050-H0123 EE050-H0126 EE050-H0129 |
| **Validation** | Internal classification assessment; inconsistent-output exclusions change denominators and need verification. | EE050-H0126 EE050-H0127 EE050-H0385 |

## Source-linked excerpts
- [EE050-H0119] ==The study used EmbryoScope videos from 699 embryos belonging to 248 patients at a single center.==
- [EE050-H0126] ==The CNN was tested on a distinct 140-embryo set not used in training, with three repeated model runs.==
- [EE050-H0385] ==The image-only CNN reached 61.2% accuracy and the full ensemble with four clinical characteristics reached 71.42% on the 140-embryo test set.==
- [EE050-H0431] ==The authors note single-platform training, absent mosaic modeling, limited sample size, and substantial underrepresentation of Black and Hispanic patients.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*