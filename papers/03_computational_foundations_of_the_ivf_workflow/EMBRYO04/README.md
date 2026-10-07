# EMBRYO04 — Development of deep learning algorithms for predicting blastocyst formation and quality by time-lapse monitoring

**Liao, Zhang, Feng et al. (2021).** *Communications biology*. DOI: [10.1038/s42003-021-01937-1](https://doi.org/10.1038/s42003-021-01937-1)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods

**PDF:** see EMBRYO04.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Embryo analysis extends from static morphology to development over time. The 2025 Istanbul consensus update distinguishes grading, ranking and selection using literature, practice-survey responses and expert opinion. These terms organize tasks with separate reference standards: morphology description, developmental forecasting and ploidy classification. Representative studies show how each standard creates a different learning problem and evaluation target [@ER032,EMBRYO01,EMBRYO02,EMBRYO03,EMBRYO04,EMBRYO05].==

> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2019--2021: learned visual and temporal representations [@EMBRYO01,EMBRYO02,EMBRYO04]==

> **§ Data, reference standards and the structure of evidence** : Sequences, trajectories and multiple views
> ==Embryo studies use several sequence designs: an image encoder followed by an LSTM for blastocyst grading, spatial and temporal streams for developmental prediction, and a video encoder with recurrent processing for outcome scoring. Frame selection, observation cutoff, sequence length and alignment determine their effective inputs within the incubator recordings [@EMBRYO02,EMBRYO04,OUTCOME03].==

> **§ Computational methods** : Temporal representations: events, sequences and developmental change
> ==Temporal models encode developmental order, duration and change through events, recurrent states or frame interactions. Embryo tasks include grading, blastocyst forecasting and outcome scoring; clinical monitoring also captures treatment feedback. Event models emphasize timing, recurrent models retain history, and video encoders learn changing appearance [@EMBRYO02,EMBRYO04,OUTCOME03] [@R022].==

> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Kragh and colleagues combine a convolutional encoder over three focal planes with an LSTM over up to 30 hourly frames, padded to a fixed length, from 90 hours post-insemination to maximal expansion. Separate heads predict inner-cell-mass (ICM) and trophectoderm (TE) grades. From a corpus of 8,664 blastocysts, the 851-embryo internal test yielded ICM/TE accuracies of 65.2%/69.6%, compared with 58.0%/64.5% for the single-image CNN at 120 hours. The higher grading accuracy accompanies two coupled changes: an extended observation history and recurrent encoding. An equal-history comparison with a fixed frame encoder and training protocol can isolate the recurrent component [@EMBRYO02]. Liao separates developmental progression from appearance: a temporal stream models cell-stage sequences, a spatial stream extracts morphology, and fusion forecasts blastocyst formation and usable-blastocyst status from the first three days. Stage and forecast evaluations locate errors along this pixel-to-event-to-outcome path [@EMBRYO04].==

> **§ Computational methods** : Comparing temporal support and information paths
> ==Time alignment determines which developmental differences an encoder sees. Liao aligns early observations using pronuclear fading, whereas Kragh defines a late sequence relative to detected maximal expansion. Fixed clocks based on insemination, ICSI or capture start and event-relative clocks preserve different relationships. An encoder comparison therefore fixes the observation window, time reference and provenance of each alignment event: observed, annotated or predicted [@EMBRYO02,EMBRYO04].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Early blastocyst formation and usable-blastocyst prediction (STEM/STEM+) |  |
| **Inputs** | Time-lapse videos through day three |  |
| **Prediction time** | Day three; day-five/six morphology outcome |  |
| **Analysis unit** | embryo/video |  |
| **Method** | DenseNet201 cell/morphology features; LSTM temporal stream; gradient-boosted spatial stream; weighted ensemble |  |
| **Supervision / labels** | Embryologist cell-stage and blastocyst-quality annotations |  |
| **Outcome** | Blastocyst formation; usable blastocyst (morphology surrogate) |  |
| **Sample sizes** | [{"value": 10432, "unit": "prediction-model embryo videos", "locator": "Methods / Development of prediction models; P070"}, {"value": 2086, "unit": "validation videos", "locator": "Methods / Spatial-temporal ensemble model; P078"}] |  |
| **Splitting** | 80/20 embryo-video partition; patient disjointness not_reported_in_examined_text. |  |
| **Validation** | Single-center internal validation; ensemble weights selected and performance evaluated on the same validation set. |  |

## Source-linked excerpts
- [EMBRYO04-B0030] ==A single-centre time-lapse pipeline combined pronuclear-fading detection, cell counting and spatial-temporal models for blastocyst formation and quality prediction.==
- [EMBRYO04-B0007] ==The ensemble outperformed its component models on a random held-out embryo set, the implantation subset was small and descriptive.==
- [EMBRYO04-B0021] ==Only embryos cultured to day 5 or 6 were retained, excluding earlier transferred, frozen or discarded embryos, patient-disjoint splitting was not reported.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*