# EC074 — Multi-Omics Analysis and Machine Learning Prediction Model for Pregnancy Outcomes After Intracytoplasmic Sperm Injection- in vitro Fertilization.

**Chen, Chen, Mai (2022).** *Frontiers in public health*. DOI: [10.3389/fpubh.2022.924539](https://doi.org/10.3389/fpubh.2022.924539)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Molecular models use distinct forms of supervision. A uterine-fluid random forest classifies receptive stage from repeated transcriptomic specimens, while a small transfer follow-up records pregnancy and birth as separate outcomes [@EC073]. An IVM/ICSI study fits methylation-based conception classifiers and compares transcriptomic pathways for cross-omics corroboration. Feature selection precedes the described split, creating a route for optimistic classifier evaluation [@EC074]. The first design connects molecular state to a stage label; the second connects methylation to conception and examines related biological pathways.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy after ICSI-IVF from cumulus-cell methylation. | EC074-B0011 |
| **Inputs** | GSE144664 methylation profiles; 32 selected DMGs/BioGRID-related genes; GSE113239 transcriptomics for pathway corroboration. | EC074-B0009 EC074-B0014 |
| **Prediction time** | Cumulus-cell sampling around oocyte treatment; exact prospective prediction time not reported in examined source. | EC074-B0009 EC074-B0017 |
| **Analysis unit** | Cumulus-cell sample; source labels initial methylation groups as IVM-conceived/unconceived. | EC074-B0009 |
| **Method** | RBF SVM, random forest (25 estimators) and L2 logistic regression; hybrid biological/differential-methylation selection. | EC074-B0012 EC074-B0016 |
| **Supervision / labels** | Pregnant versus nonpregnant source-dataset labels. | EC074-B0009 EC074-B0011 |
| **Outcome** | Clinical pregnancy classification; pathway overlap is separate biological analysis. | EC074-B0011 |
| **Sample sizes** | {"methylation_samples": 24, "methylation_pregnant": 12, "methylation_nonpregnant": 12, "transcriptomic_women_samples": 10} | EC074-B0009 EC074-B0017 |
| **Splitting** | 50/50 methylation train/test split; feature selection appears described before splitting, nesting unspecified. | EC074-B0016 |
| **Validation** | Internal test ROC/AUC; transcriptomics pathway corroboration is not external predictive validation. | EC074-B0015 EC074-B0016 EC074-B0017 |

## Source-linked excerpts
- [EC074-B0009] ==The methylation dataset comprised 12 conceived and 12 unconceived IVM/ICSI-IVF cumulus-cell samples.==
- [EC074-B0016] ==Thirty-two selected genes were modeled with a single 50/50 train-test split.==
- [EC074-B0023] ==Reported AUCs were 0.94 for SVM, 0.88 for random forest, and 0.97 for logistic regression.==
- [EC074-B0027] ==A separate transcriptomic dataset yielded 190 differentially expressed genes and overlapping pathways, rather than an external prediction test.==
- [EC074-B0044] ==The authors identify the small sample and absence of validation in similar datasets as principal limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*