# EE072 — An artificial intelligence model based on the proteomic profile of euploid embryos and blastocyst morphology: a preliminary study.

**Bori, Dominguez, Fernandez et al. (2021).** *Reproductive biomedicine online*. DOI: [10.1016/j.rbmo.2020.09.031](https://doi.org/10.1016/j.rbmo.2020.09.031)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Early, intermediate and late fusion
> ==Direct molecular--morphological fusion has also been evaluated for euploid embryo transfers. A preliminary multilayer-perceptron study combines 20 computed morphology variables with spent-medium protein measurements; a genetic algorithm selects network architectures. The IL-6/MMP-1 configuration attains AUC 1.0 on seven internal-test embryos and correctly classifies eight of 11 previously unused embryos in a blind test (72.7% accuracy). Both samples belong to the 55-embryo multimodal population; a separate 131-embryo donor-oocyte population supports morphology-only modeling. The design demonstrates a concrete fusion mechanism at small scale, with the blind result identifying the next target for independent replication [@EE072].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth using engineered blastocyst morphology, alone or combined with spent-medium protein measurements in euploid embryos. | EE072-H0045 EE072-H0048 EE072-H0050 |
| **Inputs** | Single blastocyst image at111.5±1.5hours plus day5 spent-culture-medium proteins for the multimodal group. Image segmentation/texture analysis produces33 variables reduced to20;92proteins are measured, with selected sets including IL-6/MMP-1. | EE072-H0050 EE072-H0065 EE072-H0068 EE072-H0070 EE072-H0090 |
| **Prediction time** | Blastocyst/day5 image and medium collection; the multimodal analysis is restricted to subsequently confirmed euploid embryos. Source states only euploid-embryo medium was analysed after single transfer, so retrospective assay timing does not establish a deployed pre-transfer test. | EE072-H0050 EE072-H0061 EE072-H0063 |
| **Analysis unit** | Embryo with single-embryo-transfer live-birth label. Donor-image and autologous-PGT-A multimodal groups have different sampling and must not be merged as one model test cohort. | EE072-H0048 EE072-H0051 EE072-H0063 |
| **Method** | Computer-vision morphology extraction with region segmentation/Hough transform; collinearity reduction; multilayer perceptron trained by back-propagation and genetic-algorithm architecture selection. Alternative morphology/protein input combinations are compared; selected architecture1 uses20morphology variables plus IL-6/MMP-1. | EE072-H0068 EE072-H0070 EE072-H0090 EE072-H0092 |
| **Supervision / labels** | Patient-reported live birth after single-embryo transfer; PGT-A confirms euploid eligibility for the autologous multimodal group rather than serving as its predicted target. | EE072-H0061 EE072-H0063 EE072-H0088 EE072-H0090 |
| **Outcome** | Positive versus negative live birth; morphology-only donor and euploid multimodal evaluations are separate. | EE072-H0045 EE072-H0063 EE072-H0088 EE072-H0090 |
| **Sample sizes** | {"donor_recipients_and_embryos": 131, "autologous_PGT_A_women_and_initial_embryos": 81, "initial_embryos_total": 212, "autologous_embryos_excluded_by_image_or_stage": 26, "analysable_images_total": 186, "analysable_multimodal_embryos": 55, "multimodal_blind_test_embryos": 11, "multimodal_development_embryos": 44, "multimodal_internal_test_embryos": 7, "proteins_assayed": 92, "spent_medium_samples_assayed": 81, "control_medium_samples": 8, "centres": 1} | EE072-H0048 EE072-H0050 EE072-H0051 EE072-H0065 EE072-H0071 EE072-H0090 EE072-H0093 EE072-H0094 |
| **Splitting** | Donor group randomly split70/15/15 for training/validation/test. Of55multimodal embryos,11reserved for blind testing; remaining44randomly split68/16/16. Isolation of preprocessing, protein/architecture selection and donor/patient groups is not fully established. | EE072-H0051 EE072-H0071 |
| **Validation** | Morphology-only donor test reports95%accuracy. Selected multimodal architecture has reported AUROC1.0 on only7internal test embryos; blind11-embryo set yields8/11correct (72.7%). No independent-centre or prospective clinical-policy evaluation is established. | EE072-H0088 EE072-H0090 EE072-H0092 EE072-H0093 EE072-H0094 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*