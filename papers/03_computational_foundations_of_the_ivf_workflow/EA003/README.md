# EA003 — Set-Valued Policy Learning

**Laura Fuentes-Vicente, Mathieu Even, Gaelle Dormion et al. (2026).** *arXiv preprint*. DOI: []()

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational foundations of the IVF workflow, Learning objectives and the interpretation of model outputs

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2026: decision-oriented evaluation [@EQF02,EA003]==

> **§ Learning objectives and the interpretation of model outputs** : Policy objectives and clinical utility
> ==where the superscript denotes the outcome under a specified selection policy. Prediction studies characterize associations under observed care; policy evaluation compares outcomes under alternative decision processes. Allocation design and follow-up determine how the observed comparison identifies the effect of changing actions. Set-valued policy learning returns a set of candidate doses. Its IVF application models follicular-yield and estradiol trade-offs under causal and noisy-label assumptions. Coverage guarantees are evaluated using synthetic data, while the IVF analysis estimates the two laboratory targets under candidate dosing strategies [@EA003].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Learn sets of candidate ovarian-stimulation gonadotropin-dose categories under uncertainty. | EA003-P004 EA003-P009 |
| **Inputs** | Baseline cycle characteristics and six ordinal observed dose categories; individual baseline feature inventory not supplied in examined text. | EA003-P009 |
| **Prediction time** | Dose-selection time before stimulation response, inferred from baseline inputs and action definition. | EA003-P009 |
| **Analysis unit** | Recorded ovarian-stimulation cycle. | EA003-P009 |
| **Method** | Greatest-lower-bound policy and noisy-label conformal policy; multi-arm causal-forest label generation and SuperLearner outcome estimation. | EA003-P005 EA003-P006 EA003-P017 EA003-P018 |
| **Supervision / labels** | Observed dose/outcome data supervise outcome models; optimal-treatment labels estimated rather than observed. | EA003-P006 EA003-P009 |
| **Outcome** | Follicular yield and estradiol,set-policy value and recommendation-set size; no measured OHSS reduction. | EA003-P009 |
| **Sample sizes** | {"ovarian_stimulation_cycles": 18538, "centers": "multiple; exact count not_reported_in_examined_source", "patients": "not_reported_in_examined_source", "dose_categories": 6} | EA003-P009 |
| **Splitting** | Framework partitions label-estimation,training and calibration sets; IVF-specific split sizes,patient grouping and site holdout not reported in examined text. | EA003-P006 EA003-P009 |
| **Validation** | Observational estimated policy-value tradeoffs across confidence/randomness parameters; synthetic coverage experiments separate from IVF application. | EA003-P009 EA003-P010 |

## Source-linked excerpts
- [EA003-P003] ==The framework assumes standard causal identification conditions of consistency, overlap, and conditional exchangeability for multiple treatments.==
- [EA003-P006] ==Synthetic experiments compare greatest-lower-bound and conformal set-valued policies across sample sizes, confidence levels, and injected-randomness levels using coverage, cardinality, and policy-value criteria.==
- [EA003-P009] ==The real IVF application contains 18,538 ovarian-stimulation cycles, six gonadotropin-dose levels, follicular yield as the primary outcome, and estradiol as a risk-related secondary outcome.==
- [EA003-P010] ==The conclusion states that the ideal randomness level required for conformal coverage remains an open question and recommends combining methods and learners rather than relying on one configuration.==
- [EA003-P018] ==For the IVF application, noisy treatment labels were generated with a multi-arm causal forest and conditional outcomes for the nonconformity score were estimated by a multi-algorithm Super Learner.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*