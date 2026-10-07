# EC091 — Cervical Secretion Methylation Is Associated with the Pregnancy Outcome of Frozen-Thawed Embryo Transfer.

**Lee, Su, Do et al. (2023).** *International journal of molecular sciences*. DOI: [10.3390/ijms24021726](https://doi.org/10.3390/ijms24021726)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Cervical methylation studies use selected gene regions with RF, SVM, MLP and other classifiers to predict ongoing pregnancy around 12 weeks. Independent assay samples with separately fitted models evaluate biomarker replication [@EC090]. A related balanced FET case-control study evaluates prediction under a sampled class balance. Its day-before and transfer-day descriptions place acquisition around transfer but differ on the exact input cutoff [@EC091].==

> **§ Quantitative evidence and supported decision claims** : Biological hierarchy determines what the sample represents
> ==The cervical methylation reports illustrate a potential link: they share centers and overlapping recruitment windows, while participant overlap is unreported. The evidence records therefore preserve the shared recruitment context and classify the participant relationship as unknown. Confirmed participant links would distinguish replication from reuse for these classifiers [@EC090,EC091].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict pregnancy after FET using cervical-secretion methylation. | EC091-B0015 |
| **Inputs** | Eight qMSP regions from HOXA10, HAND2, KSR1, PPT2, PRKAG2 and ZMIZ1. | EC091-B0009 EC091-B0013 |
| **Prediction time** | Near embryo transfer; Methods says day before, Discussion says day of transfer. | EC091-B0023 EC091-B0026 |
| **Analysis unit** | Woman/cervical-secretion sample. | EC091-B0013 |
| **Method** | Ten classifiers: LR, naive Bayes, SVM, kNN, decision tree, RF, bagged trees, LightGBM, XGBoost and MLP. | EC091-B0030 |
| **Supervision / labels** | Viable intrauterine pregnancy with fetal heartbeat persisting 10 weeks after transfer (12 gestational weeks). | EC091-B0026 |
| **Outcome** | Sustained pregnancy, not live birth. | EC091-B0026 |
| **Sample sizes** | {"qMSP_case_control_women": 72, "pregnant": 36, "nonpregnant": 36, "pilot_methylome_women": 41, "GSE90060_biological_reference_women": 17} | EC091-B0010 EC091-B0011 EC091-B0013 |
| **Splitting** | Ten-fold CV stated; independent heldout test allocation not specified in examined methods. | EC091-B0030 |
| **Validation** | Internal AUROC, accuracy, F-measure, precision and recall; qMSP analysis distinct from public-data biological screening. | EC091-B0015 EC091-B0030 |

## Source-linked excerpts
- [EC091-B0013] ==The main qMSP case-control analysis included 36 pregnant and 36 nonpregnant women and eight regions across six genes.==
- [EC091-B0014] ==Only KSR1-MS02 differed significantly; single gene/region AUCs ranged 0.55-0.67.==
- [EC091-B0015] ==Across ten models, logistic regression achieved accuracy 86.67% and AUC 0.81, while the multilayer perceptron achieved AUC 0.89 with accuracy 73.33%.==
- [EC091-B0030] ==Ten algorithms were compared using tenfold cross-validation on the same small dataset.==
- [EC091-B0023] ==The authors acknowledge retrospective design, small cohort, non-euploid embryos, and sampling only at transfer.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*