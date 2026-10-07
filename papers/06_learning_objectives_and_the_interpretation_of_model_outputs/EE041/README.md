# EE041 — Knowledge-embedded spatio-temporal analysis for euploidy embryos identification in couples with chromosomal rearrangements.

**Chen, Xie, Cai et al. (2024).** *Chinese medical journal*. DOI: [10.1097/cm9.0000000000002803](https://doi.org/10.1097/cm9.0000000000002803)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Genetic classification and assay-defined populations
> ==Mosaic handling determines an important part of the class definition. A model combining multi-focus temporal features and clinical variables groups mosaicism below 50% with euploid embryos and retrains its PGT-SR subgroup internally. It reports patient splitting alongside conflicting analyzed-video counts. Its class definition differs from the federated study's non-aneuploid category, making the mosaic rule an explicit field for harmonizing results [@EE041,EE030].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict blastocyst formation and euploidy in PGT-A/PGT-SR embryos. | EE041-B0011 EE041-B0017 |
| **Inputs** | Seven-focal-plane time-lapse frames plus selected parental clinical/chromosomal indicators. | EE041-B0017 EE041-B0019 |
| **Prediction time** | Formation predictions at days2–4; ploidy fusion uses video sampled up to168h,not early day3-only inference. | EE041-B0019 EE041-B0023 |
| **Analysis unit** | Embryo/blastocyst nested within patient/cycle. | EE041-B0021 |
| **Method** | AMSNet ResNet50 with multi-focus attention and temporal shift; AMCFNet clinical attention/MLP and MUTAN fusion. | EE041-B0011 EE041-B0016 EE041-B0017 |
| **Supervision / labels** | Observed blastulation and biopsy SNP-array/NGS labels; <50%mosaic labeled euploid. | EE041-B0010 EE041-B0021 |
| **Outcome** | Blastocyst formation and euploid-versus-aneuploid category; includes low-level mosaics in euploid label. | EE041-B0010 EE041-B0023 |
| **Sample sizes** | {"couples": 355, "cycles": 368, "formation_embryos": 2855, "blastocysts": 1965, "ploidy_blastocysts": 1422, "PGT_A": 589, "PGT_SR": 833} | EE041-B0021 |
| **Splitting** | Patient random60/20/20 split; reported n1719/568/568 and854/284/284 are embryo counts; PGT-SR retraining80/20. | EE041-B0019 |
| **Validation** | Internal heldout AUROC and matched-data video-model comparisons; PGT-SR subgroup evaluation. | EE041-B0020 EE041-B0023 |

## Source-linked excerpts
- [EE041-B0006] ==The study retrospectively collected time-lapse videos, clinical data, and PGT results from 368 cycles at one center.==
- [EE041-B0010] ==PGT labels classified mosaics below 50% as euploid and numerical abnormalities or higher mosaics as aneuploid.==
- [EE041-B0019] ==Patients, rather than embryos, were reportedly split 60/20/20 for the main tasks, while the PGT-SR subgroup used an 80/20 retraining/test split.==
- [EE041-B0023] ==Blastocyst-prediction AUC increased from 0.764 at day 2 to 0.881 at day 4.==
- [EE041-B0027] ==Seven-focus AMCFNet achieved AUC 0.729 among 833 PGT-SR blastocysts with a 67.59% aneuploid rate.==
- [EE041-B0035] ==The authors acknowledge retrospective selection bias, enrollment bias, and single-center limitations.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*