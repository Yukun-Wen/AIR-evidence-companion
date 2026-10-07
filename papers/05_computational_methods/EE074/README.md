# EE074 — Novel and conventional embryo parameters as input data for artificial neural networks: an artificial intelligence model applied for prediction of the implantation potential.

**Bori, Paya, Alegre et al. (2020).** *Fertility and sterility*. DOI: [10.1016/j.fertnstert.2020.08.023](https://doi.org/10.1016/j.fertnstert.2020.08.023)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==An earlier multilayer-perceptron study adds manually measured expansion and trophectoderm dynamics to conventional timings. The internal comparison evaluates this richer feature set for fetal-heart implantation in donor-oocyte recipients. Missing measurements require preprocessing, linking the representation's biological detail to its practical availability [@EE074].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict implantation using conventional and novel morphokinetic features. | EE074-P008 EE074-P009 |
| **Inputs** | Pronuclear movement, diameters, ICM area, trophoblast cell cycles and conventional timings. | EE074-P007 EE074-P008 |
| **Prediction time** | After observing the relevant pre-transfer developmental events. | EE074-P007 EE074-P008 |
| **Analysis unit** | Embryo/single fresh transfer from donor-oocyte recipients. | EE074-P006 EE074-P007 |
| **Method** | Four MLP variants with two hidden layers of 15 neurons. | EE074-P008 EE074-P009 |
| **Supervision / labels** | Observed implantation with fetal heartbeat. | EE074-P007 EE074-P009 |
| **Outcome** | Gestational sac and fetal heartbeat at 8 weeks. | EE074-P007 |
| **Sample sizes** | {"eligible_treatments_before_timelapse": 8832, "timelapse_treatments": 845, "single_fresh_transferred_embryos": 637, "ANN_input_embryos_after_missingness": 451, "pronuclear_measurement_embryos": 505, "blastocyst_diameter_embryos": 451, "ICM_area_embryos": 477, "trophectoderm_cycle_embryos": 360} | EE074-P006 EE074-P007 EE074-P008 |
| **Splitting** | 451 ANN cases;85% learning and 15% blind test, with five-fold training validation. | EE074-P008 EE074-P009 |
| **Validation** | Internal ANN discrimination and feature analysis; no independent external cohort. | EE074-P009 EE074-P026 |

## Source-linked excerpts
- [EE074-P006] ==The study was a retrospective single-center analysis of oocyte-donation recipients undergoing ICSI without PGT; 637 fresh single transfers were included from 845 time-lapse cycles.==
- [EE074-P008] ==The investigators defined five novel morphodynamic measurements, with feature-specific analyzable sample sizes reduced by darkness, bubbles, or out-of-focus images.==
- [EE074-P009] ==After preprocessing, 451 embryos were split 85% for learning and 15% for a blind test, with five-fold cross-validation applied to the learning portion.==
- [EE074-P026] ==Retained Table 2 reports the combined ANN3 as AUC 0.77, sensitivity 0.82, specificity 0.67, and accuracy 0.76, exceeding the conventional-only model's AUC of 0.64.==
- [EE074-P013] ==The authors acknowledge inter-observer annotation variability, difficult three-dimensional events, and the retrospective design as limits on generalizability.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*