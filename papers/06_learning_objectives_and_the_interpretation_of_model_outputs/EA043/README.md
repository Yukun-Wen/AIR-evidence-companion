# EA043 — In Vitro Fertilization (IVF) Cumulative Pregnancy Rate Prediction From Basic Patient Characteristics

**Zhang, Cui, Wang et al. (2019).** *IEEE Access*. DOI: [10.1109/access.2019.2940588](https://doi.org/10.1109/access.2019.2940588)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Learning objectives and the interpretation of model outputs

**PDF:** see EA043.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Learning objectives and the interpretation of model outputs** : Sequential outcomes and transfers until live birth
> ==Cluster-specific support-vector models estimate cumulative pregnancy from baseline characteristics. Internal patient-split evaluation reports modest discrimination and errors in cluster-level outcome curves, with comparator performance varying across analyses. The curve errors describe group-level fit for pregnancy over the specified horizon [@EA043].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict cumulative pregnancy after one, two or three oocyte-pickup cycles from initial patient characteristics. | EA043-P001 EA043-P003 |
| **Inputs** | Eleven selected baseline variables: age, BMI, infertility duration, AFC, AMH, FSH and five infertility-cause indicators. | EA043-P002 EA043-P003 |
| **Prediction time** | After initial medical examination and before actual IVF treatment. Source Day 3 is day 3 of the consultation timeline, not embryo day 3. | EA043-P001 EA043-P002 |
| **Analysis unit** | Couple/patient with cumulative outcomes across oocyte-pickup cycles. | EA043-P002 EA043-P004 |
| **Method** | Logistic-regression feature selection; k-means initialization at 30 clusters followed by log-rank merging; RBF SVM and cluster-specific SVM (C-SVM), with one-hot encoding and z normalization. | EA043-P002 EA043-P003 |
| **Supervision / labels** | Observed pregnancy by pickup-cycle number; cycle-1 pregnancy labels for feature selection, excluding first-cycle cases without transfer. | EA043-P002 EA043-P003 |
| **Outcome** | Cumulative pregnancy through cycles 1–3; the precise clinical pregnancy ascertainment definition is not reported in examined source. | EA043-P001 EA043-P004 EA043-P006 |
| **Sample sizes** | {"couples_patients": 11190, "reported_cycle_count_distribution": {"1": 9419, "2": 1432, "3": 236, "4": 59, "5": 30, "6": 7, "7": 2, "8": 2, "9": 2, "10": 0, "11": 1}, "distribution_interpretation": "Reported Cycle Statistics; these values sum to 11190 and are not treated here as cycle-specific at-risk denominators."} | EA043-P002 EA043-P003 |
| **Splitting** | Thirty random patient two-thirds training/one-third test repetitions; five-fold SVM tuning on training set. Feature-selection and normalization nesting are not established in examined description. | EA043-P003 EA043-P004 |
| **Validation** | Internal repeated held-out AUROC for cycles 1–3 and cumulative-probability RMSE; no external test or clinical utility trial reported. | EA043-P004 EA043-P005 |

## Source-linked excerpts
- [EA043-P002] ==The cohort comprised 11,190 treated couples and used only baseline age, BMI, infertility duration, ovarian-reserve markers, FSH, and infertility-cause variables.==
- [EA043-P003] ==Cycle counts fell sharply from 9,419 in cycle one to 1,432 in cycle two and 236 in cycle three, while feature selection used first-cycle pregnancy labels.==
- [EA043-P004] ==The study compared clustering, a global probabilistic SVM, and cluster-specific SVMs using a random two-thirds training and one-third test split.==
- [EA043-P005] ==Across 30 repetitions, C-SVM mean AUCs were approximately 0.69 for each of the first three cycles and its cumulative-curve RMSE was 0.0267.==
- [EA043-P006] ==The discussion proposes counseling uses and economic benefits, but the study itself evaluates only prediction metrics and not patient decisions, cost, time to pregnancy, or quality of life.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*