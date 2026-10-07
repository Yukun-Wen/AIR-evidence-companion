# R016 — Embryo selection with artificial intelligence: how to evaluate and compare methods?

**Kragh, Karstoft (2021).** *Journal of Assisted Reproduction and Genetics*. DOI: [10.1007/s10815-021-02254-6](https://doi.org/10.1007/s10815-021-02254-6)

**Role:** contextual · workflow: n/a

**Cited in:** Introduction, Computational methods

**PDF:** see R016.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Introduction**
> ==Three properties of IVF make this distinction consequential. Information accumulates over time, so retrieval findings become available too late to support a pretreatment prediction. Observations are nested: a patient may contribute several cycles, each cycle several embryos, and each embryo many images. Labels depend on clinical choices: transferred, biopsied and discarded embryos have different outcome-observation processes. These properties enter the learning problem itself. Temporal encoders must distinguish biological development from acquisition schedules; hierarchical aggregation must match the unit being predicted; and supervision must be interpreted through the process that made a target observable. They also determine how data should be partitioned and which population a test result describes. Earlier reviews establish the importance of timing, patient-level partitioning and selection bias; this survey relates those requirements to computational choices across IVF tasks [@R016,R045,R048].==

> **§ Introduction**
> ==Specialized reviews supply complementary technical and evaluative foundations. Earlier accounts examine ART prediction, laboratory algorithm selection, visual tasks, hardware and workflows [@ER001,ER003,ER002,ER005]. Microscopy, andrology, time-lapse and governance perspectives clarify acquisition conditions and implementation context, including distinctions between human and animal evidence or stained and live cells [@ER009,ER014,ER010,ER015]. Focused syntheses compare AI with embryologists, examine ploidy prediction, map time-lapse deep learning, and assess stimulation prediction, sperm selection and semen analysis [@R019,R024,R025,R032,R039,R041]. Ranking, probability estimation, calibration, explainability and implementation readiness likewise have substantial precedents [@R016,R030,R049]. Together, these accounts establish the clinical coverage and major evaluation concerns. Our focus is the relationship between them: how a computational mechanism acts on available observations, what its supervision identifies and which comparison can establish its contribution.==

> **§ Introduction**
> ==The comparison schema builds on existing evidence tables. Gao and colleagues' Table S1 records modality, input, stage, task, performance, sample and study [@R012]. Ouyang and Wei group methods by shared datasets and tabulate public resources; Lorimer and colleagues connect model inputs to predicted outcomes; Hu and colleagues record stage, device, inputs, sample size and validation [@R028,R014,R015]. We link those study descriptors to result-specific input-availability cutoffs, biological units, partitions, calibration and documented cohort relationships. Focused reviews supply complementary validation criteria [@R025,R041,R016]. The resulting records distinguish reuse of a named resource from reuse of participants or a held-out partition, and separate a richer input set from a change in the computational mechanism. These distinctions turn a performance catalogue into an explanation of what each comparison establishes.==

> **§ Introduction**
> ==Table entry; table caption: Selected review precedents and the scope of this synthesis. — [@R016]==

> **§ Computational methods** : Record construction and local estimation
> ==Let $ I_i(t)$ denote the information available for case $i$ at decision time $t$. A tabular predictor is $ y_i,t=f_ ( ( I_i(t)))$: $ $ constructs the vector and $f_ $ learns its relation to a target. Moving from pretreatment counseling to post-retrieval prognosis changes the information set and eligible population, even if the estimator stays fixed. Timing restrictions in stimulation reviews and temporal-representation distinctions in longitudinal reviews support separating these choices [@R041,R045]. The row defines the observational unit: patient, cycle or embryo. Embryo rows can repeat patient and cycle variables, connecting related predictions. Specifying input and partition units separately preserves this hierarchy during evaluation [@R016].==

> **§ Computational methods** : From cycle records to outcome prognosis
> ==Fixed-vector learning suits available clinical measurements. Local models preserve neighborhood experience, ensembles learn interactions, and graphical models expose conditional structure. Fixing inputs, targets and populations isolates estimator comparisons; later-period and different-clinic tests assess distinct changes. Spatial and temporal encoders learn structure that fixed summaries may discard [@R016,R027,R029].==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*