# EC038 — A deep learning approach to understanding controlled ovarian stimulation and in vitro fertilization dynamics.

**Wang, Liu, Zhang et al. (2025).** *Scientific reports*. DOI: [10.1038/s41598-025-92186-3](https://doi.org/10.1038/s41598-025-92186-3)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Monitoring sequences and treatment feedback
> ==The Edwards framework uses a Transformer encoder and masked-language pretraining for stimulation records, with a rule-augmented extension. Information timing defines three tasks: visit-level treatment prediction uses current monitoring results plus history; future monitoring forecasts use earlier visits; and laboratory-outcome classification consumes records through trigger. Evaluation also varies by development phase, with a temporal holdout in one phase and repeated random splits on outcome-selected subsets in another. The resulting evidence describes treatment-label agreement and classification of binned laboratory rates for the corresponding inputs and partitions [@EC038].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict monitoring-visit treatment/hormone/follicle categories and final MII,2PN,blastulation rates. | EC038-B0021 EC038-B0022 |
| **Inputs** | Tokenized longitudinal visits including day,treatment,hormones,follicles and age,BMI,menstrual-cycle length. | EC038-B0021 |
| **Prediction time** | Next-visit hormones/follicles from preceding visits; current treatment from preceding visits plus current tests; final rates from visits through trigger. | EC038-B0022 |
| **Analysis unit** | IVF cycle with repeated monitoring visits nested in patients. | EC038-B0021 |
| **Method** | Edwards BERT-like Transformer encoder,masked-token pretraining,task-specific heads; Edwards-Pro integrates knowledge-based treatment rules. | EC038-B0024 EC038-B0025 EC038-B0027 |
| **Supervision / labels** | Self-supervised masking followed by supervised observed categorical treatment,monitoring and laboratory outcomes. | EC038-B0024 EC038-B0025 |
| **Outcome** | Binned monitoring/treatment variables and MII,2PN,blastulation rates, not live birth. | EC038-B0021 EC038-B0022 |
| **Sample sizes** | {"cycles": 30552, "patients": 12460, "MII_outcome_cycles": 8920, "fertilization_blastocyst_outcome_cycles": 6750} | EC038-B0021 EC038-B0022 |
| **Splitting** | PhaseII uses 10×10-fold random 9:1 train/validation; patient grouping not explicit; outcome data excluded from pretraining. | EC038-B0022 |
| **Validation** | Internal repeated validation with AP,AUROC,top 2 metrics and tabular/Seq 2Seq comparators; no independent-center evaluation identified in these methods. | EC038-B0013 EC038-B0022 EC038-B0025 |

## Source-linked excerpts
- [EC038-B0007 to EC038-B0008 (Model and data)] ==Edwards is a Transformer-encoder model using 123 categorized IVF elements; training used 30,552 cycles and 239,047 visits from 2013-2021, with a later 1,804-cycle/8,364-visit set from 2022 for Phase I validation.==
- [EC038-B0009 to EC038-B0011 (Tasks and evaluation)] ==Phase I predicts next-visit treatment plans, hormones, and follicle measurements from truncated prior sequences, while Phase II predicts binned MII, 2PN, and blastulation rates; baselines include conventional ML and LSTM Seq2Seq.==
- [EC038-B0012 and Tables 5-6] ==Sequential models generally outperformed traditional baselines on Phase I metrics, but severe label imbalance made some apparently high scores misleading, as illustrated by AdaBoost predicting only the dominant follitropin class.==
- [EC038-B0013 and Table 7] ==For Phase II, Edwards reported average precision of 82.9 for MII-rate class, 72.0 for 2PN-rate class, and 66.7 for blastulation-rate class, above Seq2Seq values of 78.8, 67.5, and 62.8.==
- [EC038-B0021 to EC038-B0022 (Datasets and leakage control)] ==The single-center dataset includes multiple cycles per patient; Phase I uses temporally truncated inputs, while Phase II uses 8,920 cycles for MII and 6,750 for 2PN/blastocyst outcomes with repeated random 9:1 cross-validation rather than a held-out external center.==
- [EC038-B0023 to EC038-B0027 (Model design and integration)] ==Continuous clinical values were discretized using expert-defined bins, the model was pretrained with masked-token prediction, and Edwards-Pro adds a previous knowledge-based decision system to generate candidate treatment portfolios and predicted next-visit responses.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*