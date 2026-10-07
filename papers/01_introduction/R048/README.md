# R048 — The potential, perils and pitfalls of Artificial intelligence (AI) in Assisted Reproductive Technologies (ART)

**Garg, Seifer (2026).** *Reproductive Biology and Endocrinology*. DOI: [10.1186/s12958-026-01542-z](https://doi.org/10.1186/s12958-026-01542-z)

**Role:** contextual · workflow: n/a

**Cited in:** Introduction, Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Introduction**
> ==Three properties of IVF make this distinction consequential. Information accumulates over time, so retrieval findings become available too late to support a pretreatment prediction. Observations are nested: a patient may contribute several cycles, each cycle several embryos, and each embryo many images. Labels depend on clinical choices: transferred, biopsied and discarded embryos have different outcome-observation processes. These properties enter the learning problem itself. Temporal encoders must distinguish biological development from acquisition schedules; hierarchical aggregation must match the unit being predicted; and supervision must be interpreted through the process that made a target observable. They also determine how data should be partitioned and which population a test result describes. Earlier reviews establish the importance of timing, patient-level partitioning and selection bias; this survey relates those requirements to computational choices across IVF tasks [@R016,R045,R048].==

> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Treatment variables encode patient state and clinical choice. The quantity $ E[Y A=a,X=x]$ describes an observed conditional relationship; a recommendation concerns the consequence of assigning $a$. Attribution and input perturbation characterize the fitted mapping, while assignment-aware estimation addresses the intervention. Prognosis, imitation and policy evaluation therefore retain distinct objectives even when their columns and estimators coincide [@R005,R041,R042,R030,R048].==

> **§ Computational methods** : Cross-cutting attributes: explanation and distributed development
> ==Randomization checks test whether saliency depends on learned parameters and labels. Adebayo reports method-specific failures, including differences between Guided Grad-CAM and Grad-CAM. Lee's black/matte/glass-box taxonomy and ART reviews further distinguish interpretability from predictive validity. These frameworks organize explanation evaluation around a specified target, such as model sensitivity, feature attribution or clinician understanding [@EM042,R021,R030,R048].==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*