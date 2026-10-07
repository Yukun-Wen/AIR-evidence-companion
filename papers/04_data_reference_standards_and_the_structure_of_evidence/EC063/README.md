# EC063 — An integrated optimization and deep learning pipeline for predicting live birth success in IVF using feature optimization and transformer-based models.

**Borji, Haick, Pohn et al. (2025).** *Computer methods and programs in biomedicine*. DOI: [10.1016/j.cmpb.2025.108979](https://doi.org/10.1016/j.cmpb.2025.108979)

**Role:** core · workflow: Transfer and patient outcomes

**Cited in:** Data, reference standards and the structure of evidence, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EC063,ER037,ER039,OUTCOME01]==

> **§ Quantitative evidence and supported decision claims** : Available information determines the prediction question
> ==Borji and colleagues combine particle-swarm feature selection with a tabular transformer for live birth. The published selected-feature table includes current-cycle embryo-transfer information and a cumulative live-birth field. Assigning these inputs to a prediction time requires distinguishing historical births from the index-cycle outcome and planned transfers from completed procedures [@EC063].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict IVF live-birth occurrence from HFEA registry features. | EC063-P003 EC063-P004 |
| **Inputs** | Clinical,history and procedural registry variables;PSOselected 38 includes transferred-embryo counts and total-livebirth variable. | EC063-P011 |
| **Prediction time** | No coherent prospective prediction moment established; selected predictors include postfertilization/transfer information and an outcome-labeled variable. | EC063-P011 |
| **Analysis unit** | Registry treatment record/cycle; patient identity description inconsistent. | EC063-P004 |
| **Method** | PCA orPSO feature reduction withRF,DT,Transformer,Tab_transformer;PSO usesLR surrogate;SHAP. | EC063-P003 EC063-P004 EC063-P008 |
| **Supervision / labels** | Supervised binary live-birth occurrence with cross-entropy. | EC063-P004 EC063-P008 |
| **Outcome** | HFEA live birth occurrence; relation of total-livebirth predictor to target needs clarification. | EC063-P004 EC063-P011 |
| **Sample sizes** | {"raw_registry_records": 665244, "analyzed_records": 115012, "initial_features": 94, "PSO_selected_features": 38} | EC063-P003 EC063-P004 EC063-P010 |
| **Splitting** | Reported 70/15/15 split and 10-fold metrics with nested tuning; text simultaneously says no patient identifiers and unique patient IDs enforce grouping. | EC063-P004 EC063-P008 EC063-P009 |
| **Validation** | Internalcrossvalidation,subgroups,perturbation/SMOTE robustness; no independent external cohort. | EC063-P008 EC063-P009 EC063-P011 |

## Source-linked excerpts
- [EC063-P001] ==Published CMPB volume 271 (2025), article 108979, DOI 10.1016/j.cmpb.2025.108979, presents AI prediction of IVF live birth.==
- [EC063-P003] ==Authors describe anonymized HFEA 2010-2018 treatment data with 665,244 records and 94 initial features, a binary live-birth target, and eight PCA/PSO classifier combinations.==
- [EC063-P004] ==The paper reports 115,012 retained subjects, a 70/15/15 split before feature selection/training, and contradictory statements about absent patient identifiers and unique patient IDs.==
- [EC063-P004] ==PSO minimizes negative logistic-regression F1 with a penalty for feature count.==
- [EC063-P006] ==The custom transformer architecture table expands a projected feature vector to a sequence of length one.==
- [EC063-P007] ==The Tab_transformer table concatenates categorical embeddings and numerical inputs, reshapes to batch by one by total dimension, and applies self-attention.==
- [EC063-P008] ==Authors describe one attention layer with four heads, feed-forward dimension 128, dropout 0.2, L2 0.01, batch 512, learning rate 1e-7, 40 epochs, and tuning within nested training folds.==
- [EC063-P009] ==Authors state that perturbations are confined to training data and that all reported evaluation metrics average ten cross-validation folds.==
- [EC063-P010] ==Table 6 reports PSO plus Tab_transformer accuracy 97.0%, precision 95.2%, recall 96.1%, F1 95.6%, and AUC 98.4%; PSO plus Transformer has higher precision and recall.==
- [EC063-P010] ==Table 6 lists PCA+RF precision 91%, recall 90%, and F1 92.4%, a reporting inconsistency under the stated binary F1 definition.==
- [EC063-P011] ==Table 7 includes embryo creation/transfer, procedural dates, and total live births conceived through IVF or DI, categorizing the latter as Outcome without establishing exclusion of the index cycle.==
- [EC063-P014] ==Table 11 ranks infertility causes and procedural dates in the SHAP analysis; text acknowledges dates can proxy cohort effects and institutional protocols.==
- [EC063-P015] ==Tables 12 and 13 report feature-removal sensitivity and comparisons with mutual information and LASSO feature selection on the internal dataset.==
- [EC063-P016] ==Table 14 reports internal 2010-2018 accuracy/AUC 97.0%/98.4% and temporal 2005-2009 accuracy/AUC 96.1%/97.2%.==
- [EC063-P016] ==Discussion prose instead assigns AUC 96.5% and 91.7% to those internal and earlier temporal cohorts, conflicting with Table 14.==
- [EC063-P017] ==Table 16 reports 2010-2016 internal accuracy/AUC 97.3%/98.9% and 2017-2018 temporal accuracy/AUC 96.5%/97.9%.==
- [EC063-P017] ==The ethics statement describes anonymized registry data and no direct human experimentation; no prospective deployment or clinical impact experiment is reported.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*