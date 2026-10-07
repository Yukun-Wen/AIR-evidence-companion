# EE027 — Deep learning pipeline reveals key moments in human embryonic development predictive of live birth after in vitro fertilization.

**Mapstone, Hunter, Brison et al. (2024).** *Biology methods & protocols*. DOI: [10.1093/biomethods/bpae052](https://doi.org/10.1093/biomethods/bpae052)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Comparing temporal support and information paths
> ==A MobileNetV2 study compares developmental image windows for outcome prediction using cycle-grouped splits. This design directly examines the value of observations acquired at different developmental stages. Its methods and discussion assign miscarriage and biochemical pregnancy inconsistently, leaving the negative-class definition ambiguous for comparison with other live-birth models [@EE027].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth from precisely timed embryo images; classify developmental stages for domain transfer. | EE027-B0012 EE027-B0018 |
| **Inputs** | Selected static frames around PN, cleavage, later divisions and final blastocyst. | EE027-B0008 EE027-B0018 |
| **Prediction time** | Separate stage-specific prediction times, from PN through final day5 frame. | EE027-B0018 |
| **Analysis unit** | Embryo within fresh ICSI transfer cycle; selected SET and unambiguous DET outcomes. | EE027-B0007 EE027-B0013 |
| **Method** | ImageNet MobileNetV2 with fixed convolutional features, optional stage-pretrained hidden layer and learned outcome head. | EE027-B0011 EE027-B0012 |
| **Supervision / labels** | Live-birth/no-pregnancy records; developmental stages manually timed. | EE027-B0007 EE027-B0011 |
| **Outcome** | Live birth versus non-success endpoint; source wording for no-pregnancy/miscarriage grouping is ambiguous. | EE027-B0007 |
| **Sample sizes** | {"embryo_videos": 700, "reported_successful": 443, "reported_unsuccessful": 257, "patients": "not_reported_in_examined_source"} | EE027-B0007 EE027-B0009 |
| **Splitting** | Cycle-grouped80/10/10 repeated split or60/20/20 fixed holdout; preserve SET/DET proportions; augment training only. | EE027-B0013 |
| **Validation** | 50 repeated runs, AUROC and embryologist-score comparison; stage/timepoint comparisons within same center. | EE027-B0015 EE027-B0016 EE027-B0018 |

## Source-linked excerpts
- [EE027-B0007] ==The dataset contained 700 fresh ICSI transfer videos with live-birth or no-pregnancy outcomes.==
- [EE027-B0013] ==Outcome-model splitting kept embryos from the same treatment cycle together to reduce leakage.==
- [EE027-B0029] ==In the 141-embryo subset, model and converted embryologist-grade AUCs were 0.726 and 0.720.==
- [EE027-B0049] ==The authors acknowledge transferred-embryo selection, single-clinic data, imperfect embryologist comparison, and omission of miscarriage outcomes.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*