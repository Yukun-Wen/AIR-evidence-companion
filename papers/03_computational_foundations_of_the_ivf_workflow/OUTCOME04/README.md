# OUTCOME04 — Correlation between an annotation-free embryo scoring system based on deep learning and live birth/neonatal outcomes after single vitrified-warmed blastocyst transfer: a single-centre, large-cohort retrospective study

**Ueno, Berntsen, Ito et al. (2022).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-022-02562-5](https://doi.org/10.1007/s10815-022-02562-5)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Learning objectives and the interpretation of model outputs

**PDF:** see OUTCOME04.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Embryo evaluation and treatment outcomes
> ==Treatment outcomes connect embryo-level scores to patient-level prospects through transfer policy, the number and order of available embryos, and follow-up across transfers. Embryo-scoring studies evaluate outcome association, while a randomized comparison of AI-guided and morphology-guided selection evaluates use of the score within a clinical policy. The unit of prediction and the intervention design determine which part of this connection is measured [@OUTCOME03,OUTCOME04,OUTCOME05].==

> **§ Data, reference standards and the structure of evidence** : Partitioning, generalization and provenance
> ==Fjeldstad explicitly partitions patients for the outcome model. Hanassab uses first treatment cycles and nested leave-one-clinic-out validation, separating hyperparameter tuning from outer-clinic evaluation. McCallum reports both random image partitions and held-out-donor experiments. These designs address distinct forms of sample novelty and retain their evaluation levels in the synthesis [@OOCYTE02,STIM05,SPERM02]. Centre novelty and temporal novelty are separate. Ueno and colleagues evaluate a later cohort at a clinic that contributed to model training. This tests temporal change within a familiar centre; external evaluation of a fixed model tests transport to a new clinic [@OUTCOME04].==

> **§ Learning objectives and the interpretation of model outputs**
> ==Table entry; table caption: Supervision defines the outcome that a model can learn. — Live birth [@OUTCOME04]==

> **§ Learning objectives and the interpretation of model outputs** : Probability estimation, discrimination and calibration
> ==Patient-level discrimination and within-treatment ordering use different variation in the predictors. Ueno and colleagues discuss maternal age as an example: it can improve population discrimination while remaining constant among embryos from one treatment. Probability estimation and sibling ranking therefore form separate objective categories even when they use the same numerical score [@OUTCOME04].==

> **§ Learning objectives and the interpretation of model outputs** : Ranking within the treatment decision set
> ==The additive illustration $s_cj=a_c+b_cj$ separates an embryo-independent treatment term $a_c$ from a sibling-varying term $b_cj$. Changing $a_c$ changes between-treatment separation and leaves sibling order unchanged. Ueno and colleagues discuss this distinction for age-adjusted scores [@OUTCOME04]. Shared patient context can also interact with embryo-specific features: in $s_cj=w(u_c)^ x_cj$, context $u_c$ changes the weights applied to each embryo's features. These interactions provide a mechanism for context-sensitive sibling ordering, evaluated through comparisons within the treatment choice set.==

> **§ Learning objectives and the interpretation of model outputs** : Matching objectives to admissible comparisons
> ==The objective taxonomy assigns an evaluation target to each model output. Measurement assesses agreement with a reference; prognosis assesses a defined outcome distribution; ranking assesses ordering within a choice set; and policy evaluation assesses consequences of use. Aligning the biological unit, available information, target and evaluation population defines comparable evaluations; controlled training, tuning and model selection isolate the tested computational change. Added-modality comparisons vary the specified input while retaining the other evaluation conditions. Morphology-based supervision evaluates agreement with grades, while treatment-level ranking evaluates an ordering among eligible siblings [@EMBRYO01,OUTCOME04]. The output's unit and purpose connect each comparison to its appropriate reference.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Temporal evaluation of iDAScore for live birth and neonatal outcomes |  |
| **Inputs** | Time-lapse sequence; maternal and other covariates for association adjustment |  |
| **Prediction time** | Embryo culture at least 112 h; before vitrification/transfer |  |
| **Analysis unit** | one patient, one single vitrified-warmed blastocyst transfer |  |
| **Method** | Fixed iDAScore v1.0 evaluated by ROC and multivariable logistic regression |  |
| **Supervision / labels** | No new image model trained; outcome association with observed follow-up |  |
| **Outcome** | Live birth, miscarriage and neonatal characteristics |  |
| **Sample sizes** | [{"value": 3010, "unit": "patients and transfers", "locator": "Methods / Patients; P022"}] |  |
| **Splitting** | No retraining split; later cohort than model-training data from the same contributing clinic. |  |
| **Validation** | Temporal external evaluation at a training-contributing center; not geographic center-independent validation. |  |

## Source-linked excerpts
- [OUTCOME04-B0007] ==The temporal validation included 3,010 one-patient/one-cycle single vitrified-warmed blastocyst transfers from one Japanese centre.==
- [OUTCOME04-B0022] ==Higher retrospective iDAScore was associated with live birth (AUC 0.700 overall) after adjustment, the transferred embryo had been selected by existing practice.==
- [OUTCOME04-B0024] ==No neonatal association was detected among 752 singleton deliveries, which does not establish safety for rare outcomes or AI-guided selection.==
- [OUTCOME04-B0032] ==Minimal stimulation, ICSI-only, freeze-all practice, single-centre design and retrospective selection limit transportability, randomized testing was recommended.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*