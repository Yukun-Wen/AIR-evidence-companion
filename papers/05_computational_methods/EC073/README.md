# EC073 — Can biomarkers identified from the uterine fluid transcriptome be used to establish a noninvasive endometrial receptivity prediction tool? A proof-of-concept study.

**He, Wu, Zou et al. (2023).** *Reproductive biology and endocrinology : RB&E*. DOI: [10.1186/s12958-023-01070-0](https://doi.org/10.1186/s12958-023-01070-0)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** see EC073.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Molecular models use distinct forms of supervision. A uterine-fluid random forest classifies receptive stage from repeated transcriptomic specimens, while a small transfer follow-up records pregnancy and birth as separate outcomes [@EC073]. An IVM/ICSI study fits methylation-based conception classifiers and compares transcriptomic pathways for cross-omics corroboration. Feature selection precedes the described split, creating a route for optimistic classifier evaluation [@EC074]. The first design connects molecular state to a stage label; the second connects methylation to conception and examines related biological pathways.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify endometrial receptive stage from uterine-fluid transcriptomics and relate calls to transfer outcome. | EC073-B0006 EC073-B0016 |
| **Inputs** | RNA-seq expression of 87 RF-selected markers plus three hub genes from uterine fluid. | EC073-B0013 EC073-B0023 |
| **Prediction time** | Development samples at LH+5,+7,+9 in preceding natural cycle; validation sample on blastocyst-transfer day before transfer. | EC073-B0011 |
| **Analysis unit** | Uterine-fluid specimen nested in woman, three time points per development woman. | EC073-B0018 EC073-B0019 |
| **Method** | Differential-expression/WGCNA discovery and random-forest three-class nirsERT. | EC073-B0014 EC073-B0015 EC073-B0016 |
| **Supervision / labels** | Pre/receptive/post labels tied to sampling times in women who subsequently conceived; normal receptivity selected by successful intrauterine pregnancy. | EC073-B0006 EC073-B0011 |
| **Outcome** | Receptive-stage classification; secondary association with intrauterine pregnancy and live birth in small transfer cohort. | EC073-B0016 EC073-B0024 |
| **Sample sizes** | {"recruited_development": 69, "development_women": 48, "collected_development_samples": 144, "sequenced_development_samples": 140, "validation_women": 22, "validation_successfully_sequenced": 21} | EC073-B0018 EC073-B0019 EC073-B0020 EC073-B0024 |
| **Splitting** | Ten-fold cross-validation of development expression profiles; woman-level grouping not stated; later 22-woman transfer cohort, 21 successful assays. | EC073-B0016 EC073-B0023 EC073-B0024 |
| **Validation** | Internal stage accuracy/sensitivity/specificity/PPV/NPV; observational association of predicted WOI with pregnancy/live birth in later same-center cohort. | EC073-B0016 EC073-B0024 |

## Source-linked excerpts
- [EC073-B0006] ==Training eligibility required successful intrauterine pregnancy after the first embryo transfer and constrained age, BMI, ovarian reserve, and infertility factors.==
- [EC073-B0016] ==Markers were selected from pairwise receptive-stage contrasts and entered into a random-forest classifier evaluated by 10-fold cross-validation.==
- [EC073-B0023] ==The 87 selected markers plus three hub genes yielded mean accuracy 93.0%, specificity 95.9%, and sensitivity 90.0%.==
- [EC073-B0024] ==In 22 transfer patients, 13 of 18 predicted normal-WOI patients had live birth, none of three predicted displaced-WOI patients conceived, and one assay failed.==
- [EC073-B0031] ==The authors state the assay was not ready for clinical use and that a randomized trial is needed to test whether guided transfer improves outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*