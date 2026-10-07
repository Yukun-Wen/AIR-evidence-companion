# EE081 — Fitting the data from embryo implantation prediction: Learning from label proportions.

**Hernandez-Gonzalez, Inza, Crisol-Ortiz et al. (2018).** *Statistical methods in medical research*. DOI: [10.1177/0962280216651098](https://doi.org/10.1177/0962280216651098)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE081.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Biological alignment and hierarchical aggregation
> ==Learning from label proportions links uncertain instance outcomes to an observed group count. Bayesian classifiers treat a transfer as a bag with a known implantation count, retaining uncertainty in individual embryo outcomes. The reserved evaluation cohort contains all-or-none implantation bags, placing evaluation on transfers whose group outcome resolves every member's label. Conflicting ambiguous-embryo counts leave the size of the weakly labeled training population uncertain [@EE081].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict individual embryo implantation while retaining partially successful multiple-embryo transfers for training. | EE081-P003 |
| **Inputs** | 26 cycle/patient/stimulation features and 14 oocyte/embryo morphology features. | EE081-P004 |
| **Prediction time** | Before day-2 transfer after morphology assessment; inferred from the stated transfer workflow. | EE081-P004 |
| **Analysis unit** | Embryo within a transfer-cycle bag; cycle-level implanted counts constrain unknown individual labels. | EE081-P003 EE081-P007 |
| **Method** | Learning from label proportions with EM for naive Bayes, tree-augmented naive Bayes and 2-dependence Bayesian classifiers; equal-frequency three-bin discretization and feature selection. | EE081-P005 EE081-P006 EE081-P007 |
| **Supervision / labels** | Exact labels for all-success/all-failure transfers; only implanted label proportions for partially successful transfers. | EE081-P003 EE081-P007 |
| **Outcome** | Implantation label as reported; pregnancy test at 14 days after transfer. Detailed independent confirmation of each implanted count is not reported in examined methods. | EE081-P004 EE081-P007 |
| **Sample sizes** | {"development_patients": 330, "development_embryos": 696, "full_bag_cycles": 256, "full_bag_embryos": 519, "partial_bag_cycles": 74, "partial_bag_embryos_prose": 117, "partial_bag_embryos_table_and_total": 177, "reserved_cycles": 134, "reserved_embryos": 253, "reserved_implanted": 45, "reserved_failed": 208} | EE081-P003 EE081-P004 EE081-P007 |
| **Splitting** | Leave-one-full-bag-out internal validation, retaining other bags for training; consecutive exclusive same-center August 2014–June 2015 reserved full-bag dataset. Feature ranking on labelled full bags is described as a preprocessing step rather than fold-nested. | EE081-P007 |
| **Validation** | Internal bag-held-out and later same-center test evaluation; precision, recall and F1 compare LLP with supervised models that exclude ambiguous transfers. | EE081-P007 EE081-P010 |

## Source-linked excerpts
- [EE081-P003] ==The authors map each transfer cycle to a bag whose known label proportion is the number of implanted embryos, allowing ambiguous individual fates to contribute to training.==
- [EE081-P004] ==The development data included 330 consecutive cycles, 696 embryos, and 117 embryos from cycles in which only a subset implanted and individual identities were unknown.==
- [EE081-P007] ==Evaluation used leave-one-full-bag-out validation and a temporally later reserved set of 134 cycles and 253 embryos, all from full bags.==
- [EE081-P010] ==Retained Table 3 shows the reserved-set LLP naive-Bayes model with embryo-plus-cycle features reached recall 0.69, precision 0.43, and F1 0.53.==
- [EE081-P012] ==The authors explicitly acknowledge that repeating cycle features for all embryos in a cycle breaks the i.i.d. assumption and suggest relational modeling as future work.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*