# EE031 — Evaluation of the Clinical Efficacy and Trust in AI-Assisted Embryo Ranking: Survey-Based Prospective Study.

**Kim, Kang, Lee et al. (2024).** *Journal of medical Internet research*. DOI: [10.2196/52637](https://doi.org/10.2196/52637)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Decision benefit requires evaluation of a clinical policy
> ==Reader experiments isolate specific components of human assistance. A ranking survey constructs four-image questions with exactly one past clinical-pregnancy outcome and compares unaided with AI-assisted embryologists. This controlled task measures how assistance changes selection behavior under a known outcome distribution. Routine transfer decisions add the clinical choice set and subsequent follow-up to that interaction [@EE031].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Evaluate AI-assisted embryo ranking, agreement and trust in a reader survey. | EE031-B0014 EE031-B0021 EE031-B0022 |
| **Inputs** | Day 5 images with or without ResNet 50-derived AI scores. | EE031-B0014 EE031-B0022 |
| **Prediction time** | Historical pre-transfer images assessed in a later survey. | EE031-B0022 EE031-B0045 |
| **Analysis unit** | Embryologist response to four-image questions with one pregnancy-positive embryo. | EE031-B0014 |
| **Method** | Previously trained ResNet 50 plus repeated unaided/assisted reader assessment. | EE031-B0022 |
| **Supervision / labels** | Known clinical-pregnancy labels for images. | EE031-B0014 EE031-B0022 |
| **Outcome** | Question-level ranking accuracy and agreement; rank positions are not treatment cycles. | EE031-B0021 EE031-B0029 EE031-B0032 |
| **Sample sizes** | {"model_images": 2555, "model_train_images": 2043, "model_test_images": 512, "survey_images": 360, "questions": 90, "initial_embryologists": 34, "final_embryologists": 61, "participating_clinics": 12} | EE031-B0014 EE031-B0018 EE031-B0022 |
| **Splitting** | Model 80/20 image split with three-fold training;360 survey images from held-out 512 images. | EE031-B0019 EE031-B0022 |
| **Validation** | Unaided versus assisted reader performance and AI-only ranking; no clinical allocation experiment. | EE031-B0029 EE031-B0032 EE031-B0045 |

## Source-linked excerpts
- [EE031-B0014] ==Each of 90 questions presented four embryo images, one linked to clinical pregnancy, for ranking before and after AI scores were shown.==
- [EE031-B0022] ==The ResNet50 model was trained on 2043 images and tested on 512, with AUC 0.716 and accuracy 0.663; 360 test-set images were used in the survey.==
- [EE031-B0032] ==First-choice correct responses were 34/90 for embryologists, 45/90 with AI guidance, and 59/90 for AI alone.==
- [EE031-B0029] ==Overall interobserver kappa rose from 0.392 without AI to 0.521 with AI guidance.==
- [EE031-B0045] ==The authors acknowledge that single 2D images omit the multiple perspectives and developmental kinetics available in practice.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*