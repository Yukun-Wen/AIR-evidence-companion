# R045 — From static snapshots to longitudinal trajectories: artificial intelligence in women’s reproductive and ovarian health

**Liu, Liu, Zhao et al. (2026).** *Frontiers in Endocrinology*. DOI: [10.3389/fendo.2026.1893963](https://doi.org/10.3389/fendo.2026.1893963)

**Role:** contextual · workflow: n/a

**Cited in:** Introduction, Computational methods, Design challenges and directions for validated AI

**PDF:** see R045.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Introduction**
> ==Three properties of IVF make this distinction consequential. Information accumulates over time, so retrieval findings become available too late to support a pretreatment prediction. Observations are nested: a patient may contribute several cycles, each cycle several embryos, and each embryo many images. Labels depend on clinical choices: transferred, biopsied and discarded embryos have different outcome-observation processes. These properties enter the learning problem itself. Temporal encoders must distinguish biological development from acquisition schedules; hierarchical aggregation must match the unit being predicted; and supervision must be interpreted through the process that made a target observable. They also determine how data should be partitioned and which population a test result describes. Earlier reviews establish the importance of timing, patient-level partitioning and selection bias; this survey relates those requirements to computational choices across IVF tasks [@R016,R045,R048].==

> **§ Introduction**
> ==Table entry; table caption: Selected review precedents and the scope of this synthesis. — [@R045]==

> **§ Computational methods** : Fixed-vector representations: clinical records and structured measurements
> ==Let $ I_i(t)$ denote the information available for case $i$ at decision time $t$. A tabular predictor is $ y_i,t=f_ ( ( I_i(t)))$: $ $ constructs the vector and $f_ $ learns its relation to a target. Moving from pretreatment counseling to post-retrieval prognosis changes the information set and eligible population, even if the estimator stays fixed. Timing restrictions in stimulation reviews and temporal-representation distinctions in longitudinal reviews support separating these choices [@R041,R045].==

> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Changes, extrema and slopes compress serial observations into fixed trajectory summaries, complementing Section 5.3's full-sequence encoders [@R045]. Scan-day-specific models use evolving follicular measurements to predict clinician-selected trigger timing and a high-response proxy. Validation groups scans by cycle, with repeated-woman separation unspecified and eligibility changing by scan day. These outputs characterize prescribing patterns and proxy response at successive monitoring visits [@EC047].==

> **§ Design challenges and directions for validated AI**
> ==12 The taxonomy motivates three priorities: isolate representation value, preserve evaluation populations and connect workflow gains to patient outcomes. Building on partitioning, calibration and implementation research, the following designs test these priorities [@OUTCOME03,OUTCOME05,R005,R016,R045,R049].==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*