# OUTCOME01 — Machine learning predicts live-birth occurrence before in-vitro fertilization treatment

**Goyal, Kuchana, Ayyagari (2020).** *Scientific reports*. DOI: [10.1038/s41598-020-76928-z](https://doi.org/10.1038/s41598-020-76928-z)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Data, reference standards and the structure of evidence, Computational methods, Learning objectives and the interpretation of model outputs, Quantitative evidence and supported decision claims

**PDF:** see OUTCOME01.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EC063,ER037,ER039,OUTCOME01]==

> **§ Computational methods** : Nonlinear estimators and response targets
> ==Goyal compares conventional classifiers, a one-dimensional neural model and ensembles across feature subsets. Despite a pretreatment description, the features include current-cycle eggs collected and embryos transferred. Models using these variables supply post-retrieval or transfer-stage prognosis; fixed-input comparisons isolate estimator changes [@OUTCOME01].==

> **§ Learning objectives and the interpretation of model outputs** : Probability estimation, discrimination and calibration
> ==Probability prediction assigns a frequency interpretation to an outcome in a defined population at a specified information time. Formally, clinical risk is $ p_i=P_ (Y_i=1 X_i)$. Goyal's predictor includes current-cycle retrieval and transfer features, making its complete input set available after those events despite its pretreatment description [@OUTCOME01].==

> **§ Learning objectives and the interpretation of model outputs** : Probability estimation, discrimination and calibration
> ==Class balance shapes probability and precision estimates. Goyal and colleagues undersample negative records before splitting the analytical dataset, producing a sampled evaluation distribution [@OUTCOME01]. Under a prevalence change with fixed class-conditional score distributions, ROC behavior can remain unchanged while precision and the PR baseline change. Saito and Rehmsmeier's examples show why class balance accompanies metric reporting and probability transport to a clinic population [@EM027].==

> **§ Learning objectives and the interpretation of model outputs** : Matching objectives to admissible comparisons
> ==12 Table answers which metrics to report and at which unit. A useful evaluation combines task performance with uncertainty, calibration where a probability is used, and the consequence of the intended decision. For a benchmark with several metrics, the primary metric supplies an explicit ordering; the remaining metrics show trade-offs. A model is Pareto-dominated only when another is at least as good on every shared metric and strictly better on one, under the same evaluation conditions. This relation preserves competing strengths without assigning arbitrary weights to unlike outcomes.==

> **§ Quantitative evidence and supported decision claims** : Available information determines the prediction question
> ==Predictor availability defines the prediction time. Retrospective clinical tables combine information recorded before treatment, during laboratory procedures, at transfer and after follow-up. Goyal's title specifies prediction before IVF treatment, whereas its feature table includes current-cycle egg collection and embryo-transfer information. The documented input set therefore describes a later-information prediction problem, whose comparator must receive information available at the same stage [@OUTCOME01].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Registry-based live-birth prediction |  |
| **Inputs** | Age, infertility/history and current-cycle egg/embryo counts (Table 1) |  |
| **Prediction time** | Claimed pretreatment; current-cycle collected eggs and transferred embryos imply later availability. Timing mismatch requires verification. |  |
| **Analysis unit** | registry treatment record; unique patients not established |  |
| **Method** | Compared conventional ML, neural network and ensembles; random forest best reported setting |  |
| **Supervision / labels** | Registry live-birth labels; negative-class undersampling |  |
| **Outcome** | Binary live-birth occurrence |  |
| **Sample sizes** | [{"value": 141160, "unit": "balanced analytical records", "locator": "Pre-processing; P032"}, {"value": 93165, "unit": "training records", "locator": "P033"}, {"value": 47995, "unit": "validation records", "locator": "P034"}] |  |
| **Splitting** | 66/34 record split after class balancing; patient-disjointness not_reported_in_examined_text. |  |
| **Validation** | Internal held-out balanced validation. |  |

## Source-linked excerpts
- [OUTCOME01-B0013] ==The study filtered 2010–2016 HFEA registry cycles to 141,160 records for live-birth classification.==
- [OUTCOME01-B0014] ==Predictors included eggs collected, eggs mixed with partner sperm and embryos transferred, contradicting the titles before-treatment timing.==
- [OUTCOME01-B0018] ==The authors removed negative records to force equal class sizes and then randomly split records, so prevalence and possible repeat-patient leakage were not preserved.==
- [OUTCOME01-B0032] ==Random forest without feature selection had the best reported AUC of 0.846 and F1 of 0.7649, without external validation or calibration.==
- [OUTCOME01-B0017] ==The target description says values greater than one were recoded positive, leaving ambiguity about records coded exactly one live birth.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*