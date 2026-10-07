# EE008 — Federated task-adaptive learning for personalized selection of human IVF-derived embryos.

**Gao, Yang, Wang et al. (2025).** *Communications medicine*. DOI: [10.1038/s43856-025-01182-1](https://doi.org/10.1038/s43856-025-01182-1)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE008.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Cross-cutting attributes: explanation and distributed development
> ==Distributed development addresses observations held by several institutions. FedEmbryo uses task- and client-adaptive loss-ratio weighting in federated learning for morphology, blastulation and live-birth prediction. Reported external cohorts assess predictive transport, although conflicting partition descriptions make the development--evaluation separation ambiguous. The loss weighting adapts learning across clients and tasks; transport and privacy evaluations characterize the resulting distributed system [@EE008].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Federated multitask morphology assessment and multimodal live-birth prediction. | EE008-B0009 EE008-B0028 EE008-B0030 |
| **Inputs** | Day 1/3 embryo images and clinical metadata including age, hormones and uterine measures. | EE008-B0028 EE008-B0032 |
| **Prediction time** | Day 1/3 assessment and Day 5 formation prediction; exact live-birth image timing needs task-level clarification. | EE008-B0028 EE008-B0030 EE008-B0032 |
| **Analysis unit** | Image/embryo nested in patient and clinic. | EE008-B0014 |
| **Method** | FedEmbryo task/client dynamic weighting, ResNet 50 image branch and MLP clinical fusion. | EE008-B0016 EE008-B0021 EE008-B0031 EE008-B0032 |
| **Supervision / labels** | Embryologist morphology and observed live-birth labels; ambiguous annotations excluded. | EE008-B0013 EE008-B0028 EE008-B0030 |
| **Outcome** | Morphology, blastocyst formation and live infant≥24 weeks surviving≥1 month. | EE008-B0028 EE008-B0030 |
| **Sample sizes** | {"federated_training_clients": 4, "external_morphology": {"E_patients": 992, "E_images": 6090, "F_patients": 497, "F_images": 2689}, "external_livebirth": {"E_patients": 376, "E_images": 1297, "F_patients": 190, "F_images": 533}, "internal_counts": "Per-client/task patients and images detailed inB0014; do not sum across tasks as unique patients"} | EE008-B0014 EE008-B0015 |
| **Splitting** | Reported patient-based 70/20/10 splits at four clients and unseenE/F cohorts; listed counts do not consistently match ratios. | EE008-B0014 EE008-B0015 |
| **Validation** | Internal/external AUC and PCC, federated/local/centralized comparisons and multimodal ablations. | EE008-B0043 EE008-B0048 EE008-B0050 EE008-B0063 |

## Source-linked excerpts
- [[EE008-B0014]] ==Four client datasets were split 70/20/10 by patient for training, validation and testing, with separate patient and image counts for morphology and live-birth tasks.==
- [[EE008-B0015]] ==Internal client tests were supplemented by two unseen external cohorts, E and F, for both morphology and live-birth evaluation.==
- [[EE008-B0028]] ==Morphology tasks used day-1 and day-3 images and predicted pronuclear abnormality, cell count, symmetry, fragmentation and day-5 blastocyst formation.==
- [[EE008-B0030]] ==Live birth was defined as delivery after at least 24 weeks followed by infant survival for at least one month.==
- [[EE008-B0043]] ==For morphology tasks, FedEmbryo generally exceeded local and federated baselines; external AUC was 0.74 for day-5 blastocyst formation versus 0.58 for local models, while some centralized results were similar.==
- [[EE008-B0048]] ==Image-only live-birth AUC was 0.80 internally and 0.76 externally for FedEmbryo, compared with 0.73 and 0.70 for local models.==
- [[EE008-B0063]] ==The authors limit generalizability to Chinese populations and note latency/scalability concerns from synchronous federated training.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*