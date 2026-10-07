# SPERM02 — Deep learning-based selection of human sperm with high DNA integrity

**McCallum, Riordon, Wang et al. (2019).** *Communications biology*. DOI: [10.1038/s42003-019-0491-6](https://doi.org/10.1038/s42003-019-0491-6)

**Role:** core · workflow: Sperm assessment and retrieval

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** see SPERM02.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Morphology and function introduce different reference standards. Live-sperm imaging can be evaluated against expert appearance, while paired fluorescence provides a single-cell DNA-fragmentation target. Zona pellucida binding supplies another functional label, linked through aggregated predictions to conventional-IVF fertilization groups. Each target captures a specific property: appearance, DNA integrity or binding function [@EC002,SPERM02,SPERM03].==

> **§ Computational foundations of the IVF workflow** : Gamete assessment: detection, description and competence
> ==Specimen preparation determines how an assessment can be used. Stained, air-dried cells support semen-sample assessment and investigation of insemination strategies. McCallum and colleagues similarly obtain bright-field images after staining in their experimental acquisition pipeline. Live-cell selection adds an acquisition constraint: the assessed cell must remain available for injection [@SPERM02,SPERM03].==

> **§ Data, reference standards and the structure of evidence** : Static images: acquisition is part of the input
> ==Acquisition specifies the material presented to the model. A zona-binding classifier uses Diff-Quik-stained images; a DNA-fragmentation regressor uses bright-field images acquired after staining; a live-sperm morphology system uses unstained confocal imaging. These preparations define different workflows for sample assessment and live-cell selection [@SPERM03,SPERM02,EC002].==

> **§ Data, reference standards and the structure of evidence** : Reference standards and the meaning of a label
> ==Assay-derived labels connect images to measured biological properties. McCallum links bright-field cell appearance to a continuous fluorescence-derived DNA-fragmentation measure. Leung uses experimental zona-binding categories and then examines clinical fertilization associations. Continuous molecular prediction and functional classification have distinct targets, with the latter also supporting a separate sample-level analysis [@SPERM02,SPERM03].==

> **§ Data, reference standards and the structure of evidence** : Partitioning, generalization and provenance
> ==Fjeldstad explicitly partitions patients for the outcome model. Hanassab uses first treatment cycles and nested leave-one-clinic-out validation, separating hyperparameter tuning from outer-clinic evaluation. McCallum reports both random image partitions and held-out-donor experiments. These designs address distinct forms of sample novelty and retain their evaluation levels in the synthesis [@OOCYTE02,STIM05,SPERM02].==

> **§ Computational methods**
> ==Table entry; table caption: Computational mechanisms, representational advantages and informative comparisons. — Learned appearance encoder and prediction head (microscopy pixels / biological object) [@OOCYTE02,SPERM02]==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Rank human sperm by predicted single-cell DNA fragmentation |  |
| **Inputs** | Cropped bright-field sperm-head images acquired after acridine-orange staining in this experiment |  |
| **Prediction time** | Laboratory image assessment; proposed ICSI selection use not clinically tested |  |
| **Analysis unit** | Sperm cell nested within donor |  |
| **Method** | ImageNet-pretrained VGG16 with regression head; transfer learning |  |
| **Supervision / labels** | Continuous single-cell DFI from paired fluorescence ratio |  |
| **Outcome** | DFI regression/ranking, not IVF or live-birth outcome |  |
| **Sample sizes** | {"cells": 1064, "healthy_donors": 6} |  |
| **Splitting** | Random 60/20/20 image split plus separate leave-one-donor-out evaluation |  |
| **Validation** | Internal image holdout and held-out donor tests; later imaging batch showed limited correlation |  |

## Source-linked excerpts
- [SPERM02-B0020] ==A VGG16-based model learned DNA-fragmentation labels from 1,064 stained sperm images drawn from only six healthy donors, with random-cell and leave-one-donor tests.==
- [SPERM02-B0007] ==Predicted scores showed moderate correlation with measured fragmentation and enriched a predicted low-fragmentation subpopulation.==
- [SPERM02-B0012] ==The destructive stain, imaging drift in a later acquisition, underprediction at high fragmentation and absence of ICSI or embryo outcomes limit clinical translation.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*