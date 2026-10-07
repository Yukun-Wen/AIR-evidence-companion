# EMBRYO05 — A non-invasive artificial intelligence approach for the prediction of human blastocyst ploidy: a retrospective model development and validation study

**Barnes, Brendel, Gao et al. (2023).** *The Lancet. Digital health*. DOI: [10.1016/s2589-7500(22)00213-8](https://doi.org/10.1016/s2589-7500(22)00213-8)

**Role:** core · contrasts C15, C16 · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Embryo analysis extends from static morphology to development over time. The 2025 Istanbul consensus update distinguishes grading, ranking and selection using literature, practice-survey responses and expert opinion. These terms organize tasks with separate reference standards: morphology description, developmental forecasting and ploidy classification. Representative studies show how each standard creates a different learning problem and evaluation target [@ER032,EMBRYO01,EMBRYO02,EMBRYO03,EMBRYO04,EMBRYO05].==

> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Feature integration fixes the earliest usable prediction time. STORK-A combines blastocyst images with maternal age and morphokinetic information, adding morphology grading in a fuller configuration. The complete predictor becomes available after its final required observation. Component acquisition times and complete-model availability therefore describe complementary aspects of the input [@EMBRYO05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2022--2023: scaled scoring and molecular endpoints [@OUTCOME03,EMBRYO05]==

> **§ Data, reference standards and the structure of evidence** : Outcome availability, selection and censoring
> ==The observation of later outcomes depends on development and clinical selection. An oocyte can fail fertilization; an embryo can arrest; a blastocyst may not undergo biopsy or transfer. The availability of ploidy, implantation and live-birth labels is therefore shaped by upstream development and clinical decisions. A model trained on one selected subset addresses a conditional population. STORK-A's PGT-A reference is observed among embryos entering the biopsy pathway. The source population, endpoint-eligible subset and final analyzed observations describe successive selections that determine the ploidy task [@EMBRYO05].==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Feature combination for ploidy prediction (image-derived and clinical features / embryo) [@EMBRYO05]==

> **§ Computational methods** : Early, intermediate and late fusion
> ==STORK-A combines blastocyst images, maternal age and morphokinetics for ploidy classification, with morphology grading added in a fuller configuration. External tests use the reduced input combination. Pairing those tests with the corresponding internal configuration evaluates population change at fixed information content. The PGT-A reference defines the target as ploidy classification in a biopsy-selected population [@EMBRYO05].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Noninvasive ploidy classification (STORK-A) |  |
| **Inputs** | 110-h image; maternal age; morphokinetics; optional morphology grade |  |
| **Prediction time** | Blastocyst stage, image at 110 h after ICSI |  |
| **Analysis unit** | embryo |  |
| **Method** | Combined machine-learning/deep-learning classifier |  |
| **Supervision / labels** | PGT-A labels |  |
| **Outcome** | Euploid versus aneuploid; additional complex-aneuploidy classifications |  |
| **Sample sizes** | [{"value": 10378, "unit": "embryos with PGT-A", "locator": "Summary / Findings"}, {"value": 1385, "unit": "patients", "locator": "Summary / Findings"}] |  |
| **Splitting** | not_reported_in_examined_text |  |
| **Validation** | Internal evaluation; WCM-ES+ and IVI Valencia independent datasets. |  |

## Source-linked excerpts
- [EMBRYO05-H0027] ==STORK-A retrospectively combined 110-hour blastocyst images, maternal age, morphokinetics and morphology for PGT-A ploidy prediction in 10,378 embryos.==
- [EMBRYO05-H0059] ==The primary data were randomly divided 70:15:15 at embryo level, the report does not state that multiple embryos from the same patient were kept in one partition.==
- [EMBRYO05-H0093] ==External accuracy was 63.4% (AUC 0.702) in WCM-ES+ and 65.7% (AUC 0.715) in IVI Valencia, lower than the primary test performance.==
- [EMBRYO05-H0103] ==Only embryos already selected for biopsy were labelled, restricting the spectrum, patent and consulting interests were disclosed.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*