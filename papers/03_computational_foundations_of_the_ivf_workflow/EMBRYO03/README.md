# EMBRYO03 — Application of convolutional neural network on early human embryo segmentation during in vitro fertilization

**Zhao, Xu, Li et al. (2021).** *Journal of cellular and molecular medicine*. DOI: [10.1111/jcmm.16288](https://doi.org/10.1111/jcmm.16288)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Computational methods, Learning objectives and the interpretation of model outputs, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Embryo analysis extends from static morphology to development over time. The 2025 Istanbul consensus update distinguishes grading, ranking and selection using literature, practice-survey responses and expert opinion. These terms organize tasks with separate reference standards: morphology description, developmental forecasting and ploidy classification. Representative studies show how each standard creates a different learning problem and evaluation target [@ER032,EMBRYO01,EMBRYO02,EMBRYO03,EMBRYO04,EMBRYO05].==

> **§ Computational methods**
> ==In the figure caption — Source-located quantitative examples for these mechanisms are presented in Table 7 STIM05,EMBRYO03,EMBRYO02,EMBRYO06==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Dense convolutional decoding to anatomical masks (microscopy pixels / image) [@EMBRYO03]==

> **§ Learning objectives and the interpretation of model outputs**
> ==Representations encode observations; targets define predictions; losses guide fitting; evaluation criteria measure performance. One encoder can support masks, grades, PGT-A classes or probabilities, each with its own reference and population. The objective axis records the learning problem and loss, while intended use records the decision. This section follows measurement, forecasting, ranking and policy evaluation [@EMBRYO03,EMBRYO02,EMBRYO05,OUTCOME05].==

> **§ Learning objectives and the interpretation of model outputs** : Measurement: spatial and ordinal agreement
> ==12 Measurement makes biological structure available downstream. Zhao learns cytoplasm, pronuclear and zona-pellucida masks from expert day-one labels, evaluates anatomical agreement and supplies structured measurements for subsequent embryo-assessment models [@EMBRYO03].==

> **§ Quantitative evidence and supported decision claims**
> ==Table entry; table caption: Selected numerical evidence across IVF tasks, with evaluation units and interpretation. — Cytoplasm segmentation [@EMBRYO03]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Cytoplasm, pronucleus and zona pellucida segmentation |  |
| **Inputs** | Day-one time-lapse images |  |
| **Prediction time** | Day one |  |
| **Analysis unit** | image/pixel; repeated images within embryos/patients |  |
| **Method** | CycleGAN enhancement followed by hierarchical fully convolutional segmentation network |  |
| **Supervision / labels** | Expert masks; normal two-pronucleus images for PN training |  |
| **Outcome** | Segmentation overlap |  |
| **Sample sizes** | [{"value": 1218, "unit": "images", "locator": "Results 3.1; P053"}, {"value": 24, "unit": "embryos", "locator": "Results 3.1; P053"}, {"value": 14, "unit": "patients", "locator": "Results 3.1; P053"}] |  |
| **Splitting** | Random five-fold partition; counts reported at image level. Embryo/patient separation not_reported_in_examined_text. |  |
| **Validation** | Internal cross-validation only in examined text. |  |

## Source-linked excerpts
- [EMBRYO03-B0007] ==The segmentation study used 1,218 images from only 24 embryos contributed by 14 patients to delineate cytoplasm, zona pellucida and pronuclei.==
- [EMBRYO03-B0029] ==Reported intersection-over-union was high for cytoplasm and lower for pronuclei and zona pellucida, supporting a technical-enabling rather than outcome-prediction use case.==
- [EMBRYO03-B0054] ==Random image-level cross-validation can place frames from the same embryo in different folds, creating severe non-independence and optimistic performance risk.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*