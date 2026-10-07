# EC090 — DNA Methylation of Window of Implantation Genes in Cervical Secretions Predicts Ongoing Pregnancy in Infertility Treatment.

**Do, Su, Chen et al. (2023).** *International journal of molecular sciences*. DOI: [10.3390/ijms24065598](https://doi.org/10.3390/ijms24065598)

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
| **Task** | Predict ongoing pregnancy from cervical-secretion WOI gene methylation. | EC090-B0036 EC090-B0039 |
| **Inputs** | Array methylation of selected WOI promoter probes; separate three-gene qMSP panel SERPINE1/SERPINE2/TAGLN2. | EC090-B0030 EC090-B0036 EC090-B0038 |
| **Prediction time** | Cervical sample collected during transfer immediately before catheter insertion. | EC090-B0030 |
| **Analysis unit** | One cervical specimen per woman undergoing embryo transfer. | EC090-B0030 |
| **Method** | Bivariate/Boruta selection then RF, naive Bayes, SVM and kNN; separately trained array and qMSP classifiers. | EC090-B0041 EC090-B0042 |
| **Supervision / labels** | Binary ongoing pregnancy from at least one viable intrauterine fetus at 12 gestational weeks. | EC090-B0030 EC090-B0039 |
| **Outcome** | Ongoing pregnancy at 12 weeks, not live birth. | EC090-B0030 |
| **Sample sizes** | {"array_women": 68, "array_pregnant": 31, "array_nonpregnant": 37, "qMSP_women": 65, "qMSP_pregnant": 30, "qMSP_nonpregnant": 35} | EC090-B0008 EC090-B0018 |
| **Splitting** | 100 repetitions of five-fold CV for model tuning/evaluation within each dataset; qMSP cohort independent biologically but classifiers retrained there. | EC090-B0038 EC090-B0042 |
| **Validation** | Repeated-CV accuracy, predictive values, sensitivity/specificity and AUROC; qMSP verifies markers rather than a locked array model. | EC090-B0016 EC090-B0021 EC090-B0042 |

## Source-linked excerpts
- [EC090-B0010] ==The discovery analysis used 68 cervical-secretion samples, 2708 promoter probes, univariate selection, Boruta refinement, and four classifiers.==
- [EC090-B0016] ==Fifteen selected DMPs yielded cross-validated AUCs 0.86-0.91 and accuracy 76.44%-85.78%.==
- [EC090-B0021] ==In 65 independent qMSP samples, three-gene models achieved AUC 0.79-0.84 and accuracy 71.46%-80.72%.==
- [EC090-B0042] ==Performance was estimated with 100 repetitions of fivefold cross-validation and default caret tuning.==
- [EC090-B0028] ==The authors identify small cohorts, non-euploid embryos, and collection immediately before transfer as major limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*