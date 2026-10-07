# EE042 — Using Unlabeled Information of Embryo Siblings from the Same Cohort Cycle to Enhance In Vitro Fertilization Implantation Prediction.

**Tzukerman, Rotem, Shapiro et al. (2023).** *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. DOI: [10.1002/advs.202207711](https://doi.org/10.1002/advs.202207711)

**Role:** core · contrasts C13 · workflow: Embryo assessment and selection

**Cited in:** Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Biological alignment and hierarchical aggregation
> ==Sibling information enters through explicit cohort summaries. One XGBoost pipeline combines embryo descriptors and a VGG16-derived score with features from untransferred siblings. Cohort-separated comparisons examine the contribution of shared context to between-cycle prognosis. Image-containing models use a smaller evaluated subset, so the available image population is part of the comparison design [@EE042].==

> **§ Quantitative evidence and supported decision claims** : Conditional comparisons across model configurations
> ==Configuration contrasts also depend on the predicted unit. IVFormer's video-only and combined video--metadata configurations achieve ploidy AUCs of 0.783 and 0.811 on 520 internal-test embryos. Its image-only and combined image--metadata configurations achieve live-birth AUCs of 0.820 and 0.857 in an external cohort of 1,343 double-embryo transfers, where the outcome belongs to the transferred group [@EMBRYO06]. Sibling information supplies another form of context: on a 155-embryo test subset, a model using images, morphology, timing and age achieves implantation AUC 0.727, increasing to 0.800 when sibling-cohort features are included [@EE042]. These comparisons locate the measured difference in the complete input-and-model configuration and identify the biological level at which it is evaluated.==

> **§ Quantitative evidence and supported decision claims** : Conditional comparisons across model configurations
> ==In the figure caption: Six selected conditional performance comparisons. Open and filled points denote configurations A and B, with the right column giving the arithmetic difference B - — Six selected conditional performance comparisons. Open and filled points denote configurations A and B, with the right column giving the arithmetic difference B -==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Test whether untransferred sibling information improves implantation prediction. | EE042-B0013 |
| **Inputs** | Morphology, morphokinetics, oocyte age, optional VGG16 score and 17 cohort-derived features. | EE042-B0013 EE042-B0041 EE042-B0043 |
| **Prediction time** | Blastocyst transfer assessment with sibling-development information. | EE042-B0030 EE042-B0031 |
| **Analysis unit** | Transferred embryo nested in stimulation cohort. | EE042-B0008 EE042-B0013 |
| **Method** | XGBoost feature-set comparisons and VGG16 image feature extraction. | EE042-B0033 EE042-B0041 EE042-B0043 |
| **Supervision / labels** | Transferred embryo outcomes; untransferred siblings contribute unlabeled features. | EE042-B0028 EE042-B0031 |
| **Outcome** | Gestational sac around 7 weeks; double transfers included only when all or none implant. | EE042-B0031 |
| **Sample sizes** | {"transferred_embryos": 2089, "IVF_cohorts": 1605, "positive_transferred": 1176, "negative_transferred": 913, "untransferred_siblings": 14105, "morphology_subset": 1936, "image_subset": 772, "test_morphology": 388, "test_morphokinetics": 418, "test_image": 155} | EE042-B0008 EE042-B0014 |
| **Splitting** | 80/20 split preserving positive/negative cohort ratios; repeated splits and ten-fold CNN prediction; patient grouping unclear. | EE042-B0014 EE042-B0042 EE042-B0043 |
| **Validation** | Paired feature-set AUROC comparisons and ten partition replications at one center. | EE042-B0014 EE042-B0029 EE042-B0043 |

## Source-linked excerpts
- [EE042-B0008] ==The dataset comprised 2089 transferred blastocysts from 1605 cycles, with 1176 implanted, 913 non-implanted, and 14,105 non-transferred siblings.==
- [EE042-B0013] ==Paired implantation models were trained with and without 17 cohort features across morphology, morphokinetic, and combined feature settings.==
- [EE042-B0014] ==Retained performance results show consistent AUC gains, including 0.727 to 0.800 for the most comprehensive image-plus-clinical-feature model.==
- [EE042-B0033] ==Manual morphokinetic annotations had 5-10% missingness for most events and about 20% for morula and blastulation timing, addressed with expert rules and imputation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*