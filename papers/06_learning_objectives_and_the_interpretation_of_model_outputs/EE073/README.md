# EE073 — Performance of a deep learning based neural network in the selection of human blastocysts for implantation.

**Bormann, Kanakasabapathy, Thirumalaraju et al. (2020).** *eLife*. DOI: [10.7554/elife.55301](https://doi.org/10.7554/elife.55301)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** see EE073.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Ranking within the treatment decision set
> ==An Xception system combines morphology-class probabilities through genetic-algorithm weights for cohort ranking, while a separate network predicts implantation. Observed transfer outcomes are available for a subset of the retrospectively selected embryos. Its evaluation consequently comprises morphology concordance, ranking with partial outcome verification and a separate euploid-embryo outcome test [@EE073].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Rank highest-quality embryo per cohort and separately classify implantation potential. | EE073-B0025 EE073-B0027 |
| **Inputs** | Single static embryo image at113±0.05hpi,cropped to remove identifiers. | EE073-B0024 |
| **Prediction time** | 113hpi blastocyst-stage observation. | EE073-B0024 |
| **Analysis unit** | Embryo and patient-specific embryo cohort. | EE073-B0024 EE073-B0027 |
| **Method** | CNN morphology/implantation classifiers; genetic algorithm optimizes weights on five-class logits for ranking. | EE073-B0025 EE073-B0028 |
| **Supervision / labels** | Senior embryologist morphology classes; separate ultrasound implantation labels. | EE073-B0024 EE073-B0025 |
| **Outcome** | Best morphology selection and implantation verified around6weeks after transfer. | EE073-B0025 EE073-B0026 |
| **Sample sizes** | {"source_videos": 3469, "source_patients": 543, "classification_images": 2440, "training_images": 1188, "validation_images": 510, "test_images": 742, "test_patients": 97, "implantation_training_images": 281, "euploid_reader_comparison_embryos": 97, "reader_embryologists": 15} | EE073-B0024 EE073-B0026 |
| **Splitting** | Independent nonoverlapping morphology test; embryo cohort overlap excluded; paragraph also says100patients for ranking compared with97reported test. | EE073-B0026 EE073-B0027 |
| **Validation** | Same-center heldout grading/ranking and human comparison;97euploid test described as capable of implantation,so75.26%cannot be interpreted as balanced diagnostic accuracy. | EE073-B0001 EE073-B0026 |

## Source-linked excerpts
- [EE073-B0006] ==The quality-ranking network used 2,440 static images at 113 hours and was evaluated in 97 independent patient cohorts, while a separate implantation network was constructed.==
- [EE073-B0014] ==Among 97 selected cohort embryos, only 44 initially had known implantation outcomes; the algorithm's observed implantation success among those was 59.1%.==
- [EE073-B0018] ==On 97 transferred euploid embryos, the CNN achieved 75.25% accuracy versus an average 67.35% for 15 embryologists from five centers.==
- [EE073-B0026] ==The implantation model was trained on 281 known-outcome images, and the independent morphology test comprised 742 embryos from 97 patients.==
- [EE073-B0023] ==The authors state that randomized controlled trials are required before routine clinical adoption.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*