# EE061 — A time-lapse embryo dataset for morphokinetic parameter prediction.

**Gomez, Feyeux, Boulant et al. (2022).** *Data in brief*. DOI: [10.1016/j.dib.2022.108258](https://doi.org/10.1016/j.dib.2022.108258)

**Role:** core · workflow: Embryo assessment and selection

**Cited in:** Data, reference standards and the structure of evidence

**PDF:** see EE061.pdf in this folder | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Data, reference standards and the structure of evidence** : Data availability and reproducible extraction
> ==12 The census identifies nine resources used by at least two empirical reports and eleven used once. The small repeat-use counts, together with the protocol differences, locate the main opportunity for cumulative benchmarking: shared releases with stable subject identifiers, labels and partitions. Additional resources in the complete census include 3D-SpermVid and its linked centerline data, which provide multifocal imaging and flagellar coordinates [@ER027,ER028]. CleavageEmbryo supplies blastomere and fragment tasks, while the Nantes descriptor explains the event-derived annotations used by subsequent models [@EE024,EE061].==

## Extracted evidence fields
| Field | Value | Locators |
|---|---|---|
| **Task** | Release time-lapse resource for16-stage morphokinetic frame classification. | EE061-B0008 EE061-B0015 |
| **Inputs** | 704 grayscale embryo videos with seven focal planes and500×500images. | EE061-B0011 |
| **Prediction time** | Development from fertilization through day5/6; annotations describe contemporaneous states. | EE061-B0014 |
| **Analysis unit** | Frame nested within embryo video. | EE061-B0006 EE061-B0011 |
| **Method** | Dataset construction and propagation of manually annotated event times to frame labels; no learned-model experiment reported. | EE061-B0008 EE061-B0009 |
| **Supervision / labels** | Experienced embryologist annotations with internal QC; prospective from2014,earlier records retrospectively checked. | EE061-B0006 EE061-B0007 |
| **Outcome** | 16morphokinetic events; viability labels deliberately withheld from release. | EE061-B0006 EE061-B0015 |
| **Sample sizes** | {"selected_videos": 704, "source_cohort_couples": 716, "images_all_planes_approx": 2400000, "selected_transfer_videos": 499, "selected_subset_patient_count": "not_reported_in_examined_source"} | EE061-B0001 EE061-B0014 EE061-B0015 |
| **Splitting** | Selected10%of videos after requiring≥6annotated phases; no model training/test split in this dataset report. | EE061-B0015 |
| **Validation** | Annotation QC and descriptive dataset statistics; model-performance validation not applicable to this report. | EE061-B0006 EE061-B0012 |

## Source-linked excerpts
- [EE061-B0002] ==The resource derives from ICSI cycles at Nantes University Hospital and is deposited at Zenodo DOI 10.5281/zenodo.6390798.==
- [EE061-B0006] ==A qualified embryologist annotated timings for 16 standardized developmental events, which serve as the reference for phase labels.==
- [EE061-B0011] ==The release contains 704 embryo folders at the central focal plane, matching annotation CSVs and six additional focal-plane archives.==
- [EE061-B0014] ==The source pool comprised 716 infertile couples treated with ICSI between 2011 and 2019 at one center, with images acquired every 10-20 minutes on an EmbryoScope system.==
- [EE061-B0015] ==Videos with fewer than six annotated phases were excluded and 10% of the remainder were randomly selected; 499 of 704 represented embryos chosen for transfer, but viability labels were withheld.==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*