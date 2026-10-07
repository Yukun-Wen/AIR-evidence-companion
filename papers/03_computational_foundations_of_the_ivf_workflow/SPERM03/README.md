# SPERM03 — Automatic identification of human spermatozoa with zona pellucida-binding capability using deep learning

**Leung, Mei, Lee et al. (2025).** *Human reproduction open*. DOI: [10.1093/hropen/hoaf024](https://doi.org/10.1093/hropen/hoaf024)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Morphology and function introduce different reference standards. Live-sperm imaging can be evaluated against expert appearance, while paired fluorescence provides a single-cell DNA-fragmentation target. Zona pellucida binding supplies another functional label, linked through aggregated predictions to conventional-IVF fertilization groups. Each target captures a specific property: appearance, DNA integrity or binding function [@EC002,SPERM02,SPERM03].==

> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Specimen preparation determines how an assessment can be used. Stained, air-dried cells support semen-sample assessment and investigation of insemination strategies. McCallum and colleagues similarly obtain bright-field images after staining in their experimental acquisition pipeline. Live-cell selection adds an acquisition constraint: the assessed cell must remain available for injection [@SPERM02,SPERM03].==

> **§ Data, reference standards and the structure of evidence** : Static images: acquisition is part of the input
> ==Acquisition specifies the material presented to the model. A zona-binding classifier uses Diff-Quik-stained images; a DNA-fragmentation regressor uses bright-field images acquired after staining; a live-sperm morphology system uses unstained confocal imaging. These preparations define different workflows for sample assessment and live-cell selection [@SPERM03,SPERM02,EC002].==

> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Assay-derived labels connect images to measured biological properties. McCallum links bright-field cell appearance to a continuous fluorescence-derived DNA-fragmentation measure. Leung uses experimental zona-binding categories and then examines clinical fertilization associations. Continuous molecular prediction and functional classification have distinct targets, with the latter also supporting a separate sample-level analysis [@SPERM02,SPERM03].==

> **§ Computational methods** : Functional targets and acquisition adaptation
> ==Measured function can supervise spatial appearance. Leung trains VGG13 on zona pellucida-binding labels, standardizes sperm-head images and uses CycleGAN to adapt between laboratory and clinical imaging conditions. Aggregated cell predictions are associated with conventional-IVF fertilization groups. The patient-level AUC of 0.93 covers 86 of 117 men in the high (71--100%) and low (0--40%) fertilization groups. This contrast quantifies discrimination between the selected high- and low-fertilization groups [@SPERM03].==

> **§ Quantitative evidence and supported decision claims**
> ==Table entry; table caption: Selected numerical evidence across IVF tasks, with evaluation units and interpretation. — Sperm function aggregation [@SPERM03]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify ZP-binding capability and predict risk of low IVF fertilization at sample level |  |
| **Inputs** | 1000× Diff-Quik-stained sperm images; extracted heads |  |
| **Prediction time** | Pre-treatment semen assessment; cannot reuse stained assessed cells for ICSI |  |
| **Analysis unit** | Cell classifier aggregated to semen sample/patient |  |
| **Method** | K-means extraction, CycleGAN domain harmonization, ImageNet-pretrained VGG13 binary classifier; saliency maps |  |
| **Supervision / labels** | Assay-derived ZP-bound/unbound labels; clinical IVF fertilization groups |  |
| **Outcome** | ZP-binding classification and sample-level fertilization strata |  |
| **Sample sizes** | {"development_images": 1083, "independent_test_images": 220, "clinical_validation_men": 117, "clinical_validation_images": ">33,000"} |  |
| **Splitting** | 75/25 development split plus fivefold CV; 220-image test; patient separation in development not_reported_in_examined_text |  |
| **Validation** | Independent image test and clinical sample validation in 117 men |  |

## Source-linked excerpts
- [SPERM03-B0008] ==Transfer learning classified zona-pellucida-bound versus unbound stained sperm images and linked sample-level predictions to IVF fertilization.==
- [SPERM03-B0020] ==The clinical cohort analysis reported AUC 0.93 for high versus low fertilization groups, but distributions overlapped and this was not a prospective selection trial.==
- [SPERM03-B0033] ==Positive and negative images came from different sperm sources and imaging domains, CycleGAN harmonization may preserve domain cues, and patient-disjoint splitting was not clearly established.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*