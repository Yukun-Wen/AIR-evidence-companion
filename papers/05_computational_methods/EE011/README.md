# EE011 — Deep learning methods to forecasting human embryo development in time-lapse videos.

**Sharma, Dorobantiu, Ali et al. (2025).** *PloS one*. DOI: [10.1371/journal.pone.0330924](https://doi.org/10.1371/journal.pone.0330924)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE011.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Direct video encoders and shared representations
> ==Forecasting future frames makes an image sequence the prediction target. An exploratory ConvLSTM study trains separate models using retrospective transfer and discard strata, then evaluates synthesized development. Its image-fidelity metrics assess the forecast appearance within those strata. Recursive forecasting extends a next-frame model over several steps; seven frames span different biological durations at different acquisition rates. Forecast evaluation therefore requires both the prediction horizon and elapsed time [@EE011].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Forecast future embryo images/development from short observed video sequences. | EE011-B0036 |
| **Inputs** | Seven-frame sequences, resized to128×128 with added image channels. | EE011-B0013 EE011-B0024 |
| **Prediction time** | Cell-stage window31–43hpi or blastocyst window90–113hpi; rolling next7 frames or recursive remainder. | EE011-B0012 EE011-B0037 |
| **Analysis unit** | Frame/subsequence nested within embryo video. | EE011-B0024 EE011-B0027 |
| **Method** | ConvLSTM FramePredictor plus annotated embryo cropper; separate transferred/discarded subgroup models. | EE011-B0019 EE011-B0020 EE011-B0034 |
| **Supervision / labels** | Next recorded image is self-supervised forecasting target; cropper supervised by manual segmentation masks. | EE011-B0024 EE011-B0034 |
| **Outcome** | Image/video similarity and developmental morphology, not implantation/live birth. | EE011-B0041 EE011-B0042 |
| **Sample sizes** | {"videos": 365, "cell_stage_videos": 220, "blastocyst_videos": 145, "heldout_cell_videos": 20, "heldout_blastocyst_videos": 15, "cropper_frames": 1994, "patients": "not_reported_in_examined_source"} | EE011-B0012 EE011-B0027 EE011-B0029 EE011-B0034 |
| **Splitting** | Heldout video groups10/10/8/7; development subsets split80/20; cropper frames drawn from all365 videos. | EE011-B0027 EE011-B0029 EE011-B0030 |
| **Validation** | PSNR,SSIM,FVD and embryo morphology inspection; technical forecasting tests. | EE011-B0041 EE011-B0042 |

## Source-linked excerpts
- [[EE011-B0012]] ==The dataset comprised 365 low-fragmentation embryo videos: 220 covering 31-43 hours post-insemination and 145 covering 90-113 hours.==
- [[EE011-B0025]] ==Four separate ConvLSTM FramePredictor models were trained for transfer versus avoid videos and for cleavage versus blastocyst-stage windows.==
- [[EE011-B0027]] ==For the cleavage-stage study, each category used 100 videos for model development and 10 independent evaluation videos.==
- [[EE011-B0046]] ==Single-next-frame evaluation reported independent post-cropping PSNR/SSIM of 25.84/0.93 for cleavage-transfer videos and 26.59/0.95 for blastocyst-transfer videos, with worse blastocyst-avoid generalization.==
- [[EE011-B0070]] ==Recursive seven-frame forecasts had grayscale distortions, blurred membranes and a mean 1-1.5-hour delay in stage transitions.==
- [[EE011-B0072]] ==Embryologists could observe developmental changes and blastulation onset, but judged noise-free predictions necessary for clinical validation.==
- [[EE011-B0080]] ==The authors attribute poor generalization for blastocyst-stage avoid videos to overfitting and limited eligible data.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*