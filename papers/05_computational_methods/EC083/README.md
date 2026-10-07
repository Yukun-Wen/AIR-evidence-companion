# EC083 — Rupture Prediction for Microscopic Oocyte Images of Piezo Intracytoplasmic Sperm Injection by Principal Component Analysis.

**Yagi, Tsuji, Morimoto et al. (2022).** *Journal of clinical medicine*. DOI: [10.3390/jcm11216546](https://doi.org/10.3390/jcm11216546)

**Role:** core · workflow: Oocyte assessment

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Comparison of spatial designs and clinical uses
> ==Texture also supports procedural forecasting. In Piezo-ICSI recordings, local binary patterns, PCA and an SVM predict membrane rupture from pre-puncture frames. Leave-one-oocyte-out evaluation keeps each oocyte's frames together, while the metric aggregates sampled frames. The result measures frame-level prediction with oocyte separation, linking pre-puncture texture to subsequent membrane behavior. Configuration-selection effects remain unresolved [@EC083].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict oocyte-membrane rupture during Piezo-ICSI. | EC083-B0005 |
| **Inputs** | One to five preceding microscopy-video frames cropped to 380×370; local binary pattern texture features. | EC083-B0007 EC083-B0032 |
| **Prediction time** | Frames preceding the first confirmed rupture-related frame; intended prediction before puncturing/rupture, exact prospective cutoff needs validation. | EC083-B0032 |
| **Analysis unit** | Oocyte/movie; several frames per oocyte. | EC083-B0005 EC083-B0033 |
| **Method** | LBP texture, PCA dimensionality 1–11 and SVM with linear, RBF, polynomial or sigmoid kernel. | EC083-B0005 EC083-B0033 EC083-B0034 |
| **Supervision / labels** | Observed membrane rupture during extension versus nonrupture. | EC083-B0005 |
| **Outcome** | Rupture classification accuracy, sensitivity and specificity. | EC083-B0005 EC083-B0034 |
| **Sample sizes** | {"oocytes": 93, "rupture": 38, "nonrupture": 55, "parameter_frame_configurations_reported": 5115, "patients": "not_reported_in_examined_source"} | EC083-B0005 EC083-B0033 |
| **Splitting** | Leave-one-oocyte-out validation excludes all frames of the held-out oocyte from training; patient grouping not described. | EC083-B0033 |
| **Validation** | Internal leave-one-oocyte-out comparison across frame counts, PCA dimensions and kernels; no external validation. | EC083-B0034 EC083-B0046 |

## Source-linked excerpts
- [EC083-B0005] ==The cohort consists of 93 clinic oocytes assigned to Piezo-ICSI in 2019, labeled as 38 rupture and 55 nonrupture oocytes.==
- [EC083-B0007] ==Each ICSI procedure was recorded as a 30-fps microscopic movie and converted into cropped frame sequences for analysis.==
- [EC083-B0033] ==Evaluation used leave-one-oocyte-out cross-validation, ensuring frames from the held-out oocyte did not enter training, but patient-level clustering was not reported.==
- [EC083-B0034] ==The best reported setting reached 91.4% accuracy with a polynomial-kernel SVM using three frames and nine principal components.==
- [EC083-B0037] ==At the selected best setting, reported sensitivity was 91.23% and specificity 91.67%.==
- [EC083-B0046] ==The authors caution that the sample is small, baseline information is uncertain, and larger studies are required.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*