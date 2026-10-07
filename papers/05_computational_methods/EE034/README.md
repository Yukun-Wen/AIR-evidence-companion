# EE034 — Generative artificial intelligence to produce high-fidelity blastocyst-stage embryo images.

**Cao, Derhaag, Coonen et al. (2024).** *Human reproduction (Oxford, England)*. DOI: [10.1093/humrep/deae064](https://doi.org/10.1093/humrep/deae064)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Computational methods

**PDF:** see EE034.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Representation reuse and adaptation across targets
> ==StyleGAN3 supplies an image-synthesis example: blastocyst frames from a small set of public embryo videos train a generator evaluated by image-distribution metrics and a visual discrimination task. Human discrimination is near chance in that task. Anatomical validation, memorization analysis and downstream augmentation experiments address complementary properties of the synthesized images [@EE034].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Generate realistic synthetic blastocyst-stage images. | EE034-B0005 |
| **Inputs** | 972 Fordham time-lapse frames at 110–120 hpi, resized to 256×256; optional FFHQ pretrained weights and augmentation. | EE034-B0006 EE034-B0013 |
| **Prediction time** | Not a prognostic timestamp; target appearance represents blastocyst-stage 110–120 hpi frames. | EE034-B0006 |
| **Analysis unit** | Image/frame; independent embryo/patient counts not specified in examined methods. | EE034-B0006 EE034-B0017 |
| **Method** | Five StyleGAN3 configurations comparing random initialization, face pretraining, augmentation and translation/rotation equivariance. | EE034-B0013 |
| **Supervision / labels** | Adversarial real-versus-generated image signal; no reproductive outcome supervision. | EE034-B0008 EE034-B0012 |
| **Outcome** | FID/KID image-distribution similarity and human real/fake judgments. | EE034-B0014 EE034-B0017 |
| **Sample sizes** | {"training_images": 972, "Turing_test_real_images": 50, "Turing_test_generated_images": 50, "evaluators": 60, "embryologists": 25, "lab_technicians": 15, "nonexperts": 20} | EE034-B0006 EE034-B0017 |
| **Splitting** | Training image corpus used as real-image reference; Turing-test real images randomly sampled from training data. No embryo-disjoint held-out generation assessment reported. | EE034-B0006 EE034-B0017 |
| **Validation** | FID/KID configuration comparison and 60-rater visual Turing test; no downstream predictive-data augmentation validation. | EE034-B0014 EE034-B0017 EE034-B0018 |

## Source-linked excerpts
- [EE034-B0006] ==The training set consisted of 972 frames sampled from 136 blastocyst time-lapse videos and resized to 256x256 pixels.==
- [EE034-B0017] ==Sixty evaluators classified 50 real and 50 synthetic images without knowing the class distribution.==
- [EE034-B0025] ==The best model reached FID 15.2 and KID 0.004 at 5000 iterations; participant accuracy was near chance, with group differences in accuracy and sensitivity.==
- [EE034-B0027] ==Experts often recognized four generated images as fake because of bubbles, dots, internal artifacts, or distorted hatched cells.==
- [EE034-B0033] ==The authors identify stage restriction, limited diversity, low resolution, and absent downstream or clinical validation as future-work needs.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*