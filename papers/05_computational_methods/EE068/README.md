# EE068 — Evaluation of artificial intelligence using time-lapse images of IVF embryos to predict live birth.

**Sawada, Sato, Nagaya et al. (2021).** *Reproductive biomedicine online*. DOI: [10.1016/j.rbmo.2021.05.002](https://doi.org/10.1016/j.rbmo.2021.05.002)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods, Quantitative evidence and supported decision claims

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Explicit events and recurrent trajectories
> ==Framewise prediction provides a simpler temporal design. An Attention Branch Network built on ResNet56 assigns image-level live-birth scores, which are combined using larger fixed weights for later frames. The attention branch localizes image features, while the aggregation rule introduces developmental position after image encoding. This separates spatial attention from learned temporal interaction: changing the aggregation rule can be tested with the image encoder and observation window held fixed. The original study partitions embryos, keeping their images together, and evaluates the resulting embryo scores [@EE068].==

> **§ Quantitative evidence and supported decision claims** : Partitioning, model selection and generalization
> ==The Attention Branch Network study illustrates the intermediate level. Its source cohort comprises 470 transferred embryos from 175 patients treated at two clinics. Its endpoint is singleton live birth without congenital anomalies after 22 weeks. The fivefold allocation explicitly groups by embryo, with four test folds totaling 376 embryos and one fold used for tuning; AUC is 0.642 (95% CI, 0.576--0.707). These details establish embryo-level separation. Patient separation remains unreported, and the generalized estimating equation used for outcome associations addresses correlation in that analysis rather than the allocation of related embryos during model training [@EE068].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Predict live birth from embryo time-lapse images and visualize image regions contributing to the prediction. | EE068-H0054 EE068-H0055 EE068-H0058 |
| **Inputs** | Serial embryo images every10 or15minutes from IVF/ICSI until cryopreservation or fresh transfer, acquired on Primo Vision or EmbryoScope. Each image is scored individually; later images receive greater aggregation weight. | EE068-H0049 EE068-H0054 EE068-H0056 EE068-H0057 |
| **Prediction time** | After the available culture sequence and before cryopreservation/fresh transfer; sequences span varying developmental durations rather than a fixed universal prediction hour. | EE068-H0047 EE068-H0049 EE068-H0051 EE068-H0057 |
| **Analysis unit** | Embryo and image nested in patient; outcomes follow single-embryo transfers. Non-live-birth patients can contribute multiple embryos. | EE068-H0042 EE068-H0047 EE068-H0049 EE068-H0061 |
| **Method** | Attention Branch Network with ImageNet-pretrained ResNet56 feature/classification components and a10-convolution-layer attention branch. Cross-entropy trains image labels; a later-frame-weighted aggregate forms the embryo score. | EE068-H0054 EE068-H0055 EE068-H0056 EE068-H0057 EE068-H0058 |
| **Supervision / labels** | Transferred-embryo live-birth label: singleton liveborn infant without congenital anomalies after22weeks; negatives include implantation failure, biochemical pregnancy and clinical miscarriage. Image labels inherit the embryo outcome. | EE068-H0042 EE068-H0054 |
| **Outcome** | Defined live birth after single transfer and attention-map interpretation; no prospective selection-policy effect is evaluated. | EE068-H0042 EE068-H0047 EE068-H0054 |
| **Sample sizes** | {"patients": 175, "clinics": 2, "transferred_embryos": 470, "live_birth_embryos": 91, "non_live_birth_embryos": 379, "time_lapse_images": 141444, "images_per_embryo_range": [68, 727], "analysed_test_embryos": 376, "cross_validation_folds": 5} | EE068-H0042 EE068-H0049 EE068-H0060 |
| **Splitting** | Stratified five-fold partition at embryo level, not frame level. Each fold is analysed using the other four for training; four analysed folds (376embryos) form testing and one is designated tuning validation. Patient grouping and the ordering/isolation of hyperparameter tuning are unresolved. | EE068-H0060 |
| **Validation** | Internal376-embryo discrimination AUROC0.642 (95%CI0.576–0.707), with threshold0.341 selected from the evaluated ROC; sensitivity/specificity/predictive values and morphology comparison reported. GEE accounts for repeated-patient association analysis, but does not establish patient-separated training. | EE068-H0060 EE068-H0061 EE068-H0073 EE068-H0075 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*