# EC037 — Pharmacogenetic analysis using artificial intelligence (AI) to identify polymorphisms associated with sub-optimal ovarian response and hyper-response.

**Ortiz, Lledo, Luque et al. (2025).** *Journal of assisted reproduction and genetics*. DOI: [10.1007/s10815-025-03471-z](https://doi.org/10.1007/s10815-025-03471-z)

**Role:** core · workflow: Stimulation and monitoring

**Cited in:** Computational methods

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==Genetic inputs extend clinical-history representations. One study predicts MII-oocyte counts from clinical-genetic features and previous-cycle outcomes; extensive variant searches, repeated cycles and incompletely specified nesting leave selection optimism unresolved. A donor study classifies total-oocyte response using baseline, genetic and realized treatment variables in selected young donors, excluding very low responses. SHAP identifies predictive variants within this population. The studies share a pharmacogenetic motivation while defining different targets, information sets and generalization populations [@EC053,EC037].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Classify ovarian response as sub-optimal, normal or hyper-response and assess pharmacogenetic predictors. | EC037-H0334 |
| **Inputs** | Donor age, BMI, AFC, protocol, stimulation duration and gonadotropin type/dose plus 19 polymorphisms. | EC037-H0358 EC037-H0365 |
| **Prediction time** | Includes completed stimulation duration and dose; pre-stimulation availability of all inputs is not established. | EC037-H0358 |
| **Analysis unit** | First stimulation cycle per oocyte donor. | EC037-H0358 |
| **Method** | SVM, kNN, RF, multilayer perceptron and XGBoost; MICE-CART imputation and SHAP. | EC037-H0339 EC037-H0343 EC037-H0349 |
| **Supervision / labels** | Supervised categories derived from retrieved oocyte count: 4–9, 10–20, >20. | EC037-H0334 |
| **Outcome** | Ovarian response category at retrieval. | EC037-H0334 |
| **Sample sizes** | {"donors_first_cycles": 495, "response_percentages": {"normal": 57.58, "hyper": 27.27, "suboptimal": 15.15}} | EC037-H0358 EC037-H0359 |
| **Splitting** | Random 80/20 split and five-fold hyperparameter CV; class balancing described before training, nesting not fully resolved. | EC037-H0341 EC037-H0344 |
| **Validation** | Internal test macro AUROC, mean sensitivity/specificity and accuracy; no separate-center validation in examined results. | EC037-H0345 EC037-H0368 |

## Source-linked excerpts
- [EC037-H0103] ==The study analyzed 495 first ovarian stimulations in healthy oocyte donors aged 18-35 and recorded clinical, stimulation, and candidate-polymorphism data.==
- [EC037-H0333] ==Predictors combined donor characteristics, observed ovarian-stimulation variables, and genotypes selected from prior literature.==
- [EC037-H0339] ==The authors reported 0.06% missing data and MICE imputation using classification trees.==
- [EC037-H0368] ==On the held-out 20% test data, random forest was the best of five classifiers, with macro AUC 0.822, mean sensitivity 0.603, mean specificity 0.802, and accuracy 0.603.==
- [EC037-H0410] ==Six variants appeared among the ten leading random-forest predictors, but only two sub-optimal-response associations and one hyper-response association were statistically significant in the follow-up multivariable regression.==
- [EC037-H0189] ==Cancelled low-response cycles and stimulations yielding fewer than four oocytes were excluded, so the analysis omits the lowest-response portion of the intended clinical spectrum.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*