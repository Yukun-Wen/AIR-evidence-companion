# EQF01 — A foundational model for in vitro fertilization trained on 18 million time-lapse images

**Rajendran, Rehani, Phu et al. (2025).** *Nature Communications*. DOI: [10.1038/s41467-025-61116-2](https://doi.org/10.1038/s41467-025-61116-2)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational foundations of the IVF workflow, Data, reference standards and the structure of evidence, Computational methods, Quantitative evidence and supported decision claims, Conclusion

**PDF:** see EQF01.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational foundations of the IVF workflow** : Technical development: from specific predictors to reusable representations
> ==Table entry; table caption: Selected technical milestones and the evaluation questions they introduced. — 2025: reusable embryo representations [@EQF01]==

> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==Table entry; table caption: Ten frequently used named resources in the 247-work cited corpus. Uses count distinct empirical reports, separating core IVF and contextual evidence. — [@EE015,EE017,EQF01]==

> **§ Computational methods** : Comparison of spatial designs and clinical uses
> ==FEMI changes the role of pretraining from generic initialization to a reusable embryo representation. Its ViT masked autoencoder is initialized on ImageNet and further trained on 17,968,959 embryo images before adaptation to six downstream tasks. The shared representation allows one pretraining strategy to support several heads and objectives; task-specific fine-tuning remains part of each evaluated system. Image-level pretraining partitions and the inclusion of named downstream data resources make the relationship between pretraining and evaluation objects important to reconstruct. The source does not establish that every downstream test embryo was absent from self-supervised exposure. This defines an independence question for representation transfer, separate from supervised test-label use [@EQF01].==

> **§ Quantitative evidence and supported decision claims** : Broad systems and the meaning of state of the art
> ==Among the systems examined here, FEMI provides the broadest explicitly demonstrated embryo-representation programme: one pretrained backbone is adapted to six embryology tasks. Its scale and reuse make it a central methodological reference for current embryo AI [@EQF01]. IVFormer supplies a complementary example of task-specific multimodal prediction, while iDAScore provides randomized evidence about a deployed selection policy. Table makes these forms of progress directly visible.==

> **§ Quantitative evidence and supported decision claims** : Broad systems and the meaning of state of the art
> ==Table entry; table caption: Representative leading systems: breadth and evidence answer different questions. — FEMI, 2025; follow-up 2026 [@EQF01,EQF02]==

> **§ Conclusion**
> ==The technical trajectory extends from task-specific predictors to reusable representations. FEMI demonstrates adaptation across six embryology tasks; IVFormer illustrates multimodal prediction; and iDAScore links scoring to a randomized evaluation of a selection policy [@EQF01,EMBRYO06,OUTCOME05]. The next advances require shared patient-linked benchmarks, matched information and tuning, fixed-model transport tests, and prospective evaluation of selection or treatment policies. Together, these designs test whether a computational advance transfers to the biological population and clinical decision for which it was developed.==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Six downstream families:ploidy,quality scores,component segmentation,witnessing,blastulation time and developmental stage. | EQF01-P003 |
| **Inputs** | Embryo images/videos; maternal age added to ploidy variants; input format/task-specific. | EQF01-P003 EQF01-P013 |
| **Prediction time** | Ploidy110hpiimage or96–112hpivideo; blastulation-time prediction72hpi; witnessing96/112hpi; other tasks stage-specific. | EQF01-P003 EQF01-P013 |
| **Analysis unit** | Pretraining image; downstream embryo,image,pair or component depending on task. | EQF01-P003 EQF01-P006 EQF01-P013 |
| **Method** | ImageNet-initialized ViT-MAE further pretrained onIVFimages; task heads,attention BiLSTM video aggregation,UNETRdecoders and FaceNettriplet framework. | EQF01-P003 EQF01-P013 |
| **Supervision / labels** | Masked-image self-supervision; downstreamPGT-A,expert quality/timing/stage labels,segmentation masks and embryo-identity pairs. | EQF01-P003 EQF01-P006 EQF01-P013 |
| **Outcome** | Ploidy,expert scores,component masks,identity,blastulation-time offset and12-stage ordinal output; no live-birth task. | EQF01-P003 EQF01-P013 |
| **Sample sizes** | {"pretraining_images": 17968959, "euploid_vs_aneuploid_embryos": 6285, "euploid_vs_complex_aneuploid": 4436, "SFU_segmentation_embryos": 274, "stage_images": 78000, "WCM_quality_embryos": 1798, "Florida_quality_embryos": 869, "patient_count": "not_reported_in_examined_source"} | EQF01-P003 EQF01-P006 EQF01-P013 |
| **Splitting** | Image-level80/20SSLsplit; task datasets typically25%heldout embryo/test and4-fold development; task-specific external cohorts may contribute toSSLpretraining. | EQF01-P003 EQF01-P006 |
| **Validation** | Task-specificAUROC,MAE,Dice,F1,top1/top2accuracy,QWKandSpearman; shared model splits but domain-pretraining independence not established. | EQF01-P003 EQF01-P006 EQF01-P014 |

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*