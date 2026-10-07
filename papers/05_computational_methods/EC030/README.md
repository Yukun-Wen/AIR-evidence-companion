# EC030 — Profiling oocytes with neural networks from images and mechanical data.

**Lamont, Fropier, Abadie et al. (2023).** *Journal of the mechanical behavior of biomedical materials*. DOI: [10.1016/j.jmbbm.2022.105640](https://doi.org/10.1016/j.jmbbm.2022.105640)

**Role:** core · workflow: Oocyte assessment

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Morphometry and complementary image representations
> ==Mechanical profiling trains neural networks on simulated force responses to estimate oocyte material parameters. Human surplus-oocyte experiments examine zona properties, while simulation evaluates contour-assisted cytoplasm identifiability. The workflow uses manual calibration, and conflicting maturity descriptions leave the experimental population incompletely specified [@EC030].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Infer oocyte mechanical material parameters from indentation data; investigate contour-assisted identifiability in simulation. | EC030-P004 EC030-P012 |
| **Inputs** | Force-time/displacement responses and geometric measurements; contour inputs added for in-silico experiments. | EC030-P006 EC030-P012 EC030-P017 |
| **Prediction time** | After cumulus removal and laboratory indentation of surplus oocytes excluded from ICSI; no transfer decision evaluated. | EC030-P005 EC030-P006 |
| **Analysis unit** | Oocyte for experimental application; finite-element simulation for training. | EC030-P006 EC030-P012 |
| **Method** | Convolutional input normalization followed by four dense layers and sigmoid regression; six-parameter transient-network physical model. | EC030-P012 EC030-P013 |
| **Supervision / labels** | Known sampled finite-element material parameters supervise the inverse mapping. | EC030-P012 |
| **Outcome** | Zona-pellucida material properties and force-curve fit; cytoplasm properties not reliably recovered at shallow indentation. | EC030-P013 EC030-P014 |
| **Sample sizes** | {"human_oocytes": 9, "main_simulations": 1500, "auxiliary_simulation_training": 850, "patient_count": "not_reported_in_examined_source"} | EC030-P006 EC030-P012 EC030-P017 |
| **Splitting** | 85% simulation training and 15% validation; nine human oocytes used for empirical fitting, not clinical holdout prediction. | EC030-P013 |
| **Validation** | Simulation R-squared and experimental curve agreement after minor manual calibration; no fertilization or clinical endpoint validation. | EC030-P013 EC030-P014 |

## Source-linked excerpts
- [EC030-P004] ==The study explicitly tests human metaphase-II-stage oocytes with an ART-compatible indentation setup and proposes fitting a physical model with neural networks trained on matched finite-element simulations.==
- [EC030-P006] ==The experimental series comprised nine oocytes subjected to a 10 micrometre indentation ramp and 50-second relaxation hold, with force, displacement, and optical images collected.==
- [EC030-P013] ==Validation showed useful recovery only for three zona-pellucida parameters; the reported R-squared values were 0.76, 0.82, and 0.92, while cytoplasm-related outputs performed worse than a mean prediction.==
- [EC030-P014] ==The authors report model fits within 5% relative error for all nine oocytes after minor manual calibration and therefore focus empirical calibration on flat indentation.==
- [EC030-P020] ==The conclusion acknowledges that the small indentation depth prevented useful contour variation and limited confident prediction to zona-pellucida properties.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*