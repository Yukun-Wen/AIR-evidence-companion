# EE012 — MAIA platform for routine clinical testing: an artificial intelligence embryo selection tool developed to assist embryologists.

**Nicolielo, Jacobs, Lourenco et al. (2025).** *Scientific reports*. DOI: [10.1038/s41598-025-17755-y](https://doi.org/10.1038/s41598-025-17755-y)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Quantitative evidence and supported decision claims

**PDF:** see EE012.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Quantitative evidence and supported decision claims** : Decision benefit requires evaluation of a clinical policy
> ==Observational human-AI studies characterize how scores enter clinical decisions. A ranking-concordance study relates embryologist experience and cohort size to agreement with a 3D-CNN score. MAIA prospectively evaluates a static-image ANN during routine multicentre single-embryo transfer, including cases selected according to AI despite embryologist disagreement. Selection is observational, with conflicting reported subgroup counts. The studies describe agreement, adoption and disagreement resolution in practice, complementing intervention comparisons of the effect of assistance on outcomes [@EE004,EE012].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict clinical pregnancy and rank blastocysts from image morphology. | EE012-B0051 EE012-B0052 EE012-B0057 |
| **Inputs** | Single best-focus blastocyst image converted into 33 mathematical features. | EE012-B0050 EE012-B0051 EE012-B0053 |
| **Prediction time** | Expanded blastocyst before transfer, mainly Day 5–6. | EE012-B0030 EE012-B0050 EE012-B0057 |
| **Analysis unit** | Embryo image/single-transfer cycle nested in patient. | EE012-B0046 EE012-B0050 |
| **Method** | MAIA multilayer perceptrons optimized with a genetic algorithm. | EE012-B0013 EE012-B0052 EE012-B0053 EE012-B0054 |
| **Supervision / labels** | Supervised clinical-pregnancy labels and backpropagation. | EE012-B0053 EE012-B0054 EE012-B0057 |
| **Outcome** | Gestational sac with fetal heartbeat. | EE012-B0057 |
| **Sample sizes** | {"development_embryos_cycles": 1015, "development_patients": 891, "learning_images": 755, "internal_validation_images": 174, "excluded_images": 86, "prospective_single_transfers_patients": 200, "prospective_embryologists": 9, "prospective_centers": 3, "elective_cases": 107, "nonelective_cases": 93} | EE012-B0046 EE012-B0050 EE012-B0056 EE012-B0028 EE012-B0029 |
| **Splitting** | 755 learning images split 70/30 for training/tuning;174 internal validation;200 later clinical cases. | EE012-B0050 EE012-B0054 EE012-B0056 |
| **Validation** | Internal and prospective observational multicenter accuracy/AUC; elective-choice subgroups. | EE012-B0017 EE012-B0026 EE012-B0029 EE012-B0040 EE012-B0056 |

## Source-linked excerpts
- [[EE012-B0046]] ==Model development used 1,015 single-transfer cycles from 891 patients across three centres, with clinical pregnancy outcomes.==
- [[EE012-B0050]] ==A single best-focus 500 by 500 pixel expanded-blastocyst image was exported; 755 images were used for learning, 174 for internal validation and 86 excluded for image/development/data problems.==
- [[EE012-B0052]] ==The model was an MLP neural-network system with genetic-algorithm architecture search using 33 automatically extracted image variables.==
- [[EE012-B0056]] ==The prospective observational evaluation involved three centres, nine embryologists and 200 routine single-embryo transfers without an intervention changing practice.==
- [[EE012-B0026]] ==Across the 200 clinical-evaluation transfers, MAIA had AUC 0.65 and accuracy 66.5%, with centre-specific accuracy from 59.1% to 69.3%.==
- [[EE012-B0029]] ==In 107 elective cases with multiple eligible embryos, the transferred embryo's outcome was predicted with AUC 0.60 and accuracy 70.1%; subgroup claims based on MAIA-versus-embryologist disagreement were observational.==
- [[EE012-B0040]] ==The paper acknowledges lower internal-validation performance, absence of a prospective double-blind randomized analysis and omission of morphokinetic and patient clinical inputs.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*