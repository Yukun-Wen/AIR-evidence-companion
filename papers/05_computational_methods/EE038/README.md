# EE038 — BlastAssist: a deep learning pipeline to measure interpretable features of human embryos.

**Yang, Leahy, Jang et al. (2024).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/deae024](https://doi.org/10.1093/humrep/deae024)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE038.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==BlastAssist combines specialized networks to measure stages, fragmentation, pronuclei, blastomeres and blastocyst structures. These measurements support interpretable observational outcome analysis. Some reference consensuses include network votes, so the resulting agreement measures consistency with a partly algorithmic reference. Its embryo-level birth probabilities from multiple transfers are model-based allocations of the observed transfer outcomes [@EE038].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Extract interpretable embryo development measurements across preimplantation stages. | EE038-H0175 EE038-H0193 EE038-H0194 |
| **Inputs** | EmbryoScope seven-plane time-lapse images every 20 minutes through day 5; clinical annotations/outcomes for evaluation. | EE038-H0178 |
| **Prediction time** | Measurements at relevant fertilization, cleavage and blastocyst stages; summary features retrospectively computed from their complete stage windows. | EE038-H0178 EE038-H0197 |
| **Analysis unit** | Frame/embryo for technical tasks; SET cycle for implantation, transferred embryos within multi-embryo cycles for live-birth association. | EE038-H0178 EE038-H0204 |
| **Method** | Six-network BlastAssist pipeline: zona segmentation, stage classification, fragmentation, pronuclear and blastomere detection, blastocyst segmentation; Bayesian outcome association. | EE038-H0193 EE038-H0197 |
| **Supervision / labels** | Human labels; some difficult-task reference consensus includes the network itself. Clinical records provide pregnancy/live-birth endpoints. | EE038-H0200 EE038-H0207 |
| **Outcome** | Feature measurement agreement; implantation defined as β-hCG >25 IU/L and live-birth association separately. | EE038-H0175 EE038-H0302 EE038-H0304 |
| **Sample sizes** | {"embryos_processed": 32939, "images_processed": 67043973, "PN_expert_test_embryos": 207, "symmetry_test_embryos": 109, "fragmentation_test_images": 6664, "stage_test_images": 21036, "SET_implantation_cycles": 723, "live_birth_embryos": 3421, "live_birth_transfer_cycles": 1801} | EE038-H0178 EE038-H0204 EE038-H0304 |
| **Splitting** | Individual-network training/split details referred to prior papers and supplement; main-reader pipeline evaluation does not establish all train/test patient overlaps. | EE038-H0193 EE038-H0199 |
| **Validation** | Expert agreement, routine clinical-annotation comparison and retrospective outcome associations at one center; no independent external/prospective outcome evaluation. | EE038-H0200 EE038-H0204 EE038-H0304 |

## Source-linked excerpts
- [EE038-H0178] ==The dataset contained 32,939 embryos and more than 67 million images from one center, with linked annotations and outcomes.==
- [EE038-H0206] ==Fragmentation accuracy was 69.4% for the network versus a 73.8% mean across five experts, using a consensus ground truth that included the network.==
- [EE038-H0295] ==Agreement with routine annotations was 79.6% for pronuclear count and 55.4% for fragmentation, with strong timing correlations.==
- [EE038-H0301] ==Among 723 single-embryo transfers, two-cell timing and symmetry were significant, whereas several other apparent trends were not.==
- [EE038-H0314] ==The authors caution that outcome associations do not account for extensive confounding and should not alone define selection algorithms.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*