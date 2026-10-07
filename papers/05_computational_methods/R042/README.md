# R042 — Can machine learning models predict oocyte yield during assisted conception?: a systematic review

**Wilkinson, Gogna, Gallagher et al. (2026).** *Reproductive BioMedicine Online*. DOI: [10.1016/j.rbmo.2025.105362](https://doi.org/10.1016/j.rbmo.2025.105362)

**Role:** contextual · workflow: n/a

**Cited in:** Computational methods, Design challenges and directions for validated AI

**PDF:** not mirrored - see DOI | **Interactive card:** [card.html](card.html)

## Manuscript passages citing this work
> **§ Computational methods** : Nonlinear estimators and response targets
> ==The target's mathematical structure determines the learning objective. Binary response classes, oocyte counts and dose-normalized transformations use different losses and scales. An externally evaluated XGBoost framework separates baseline response-risk models from models encoding a planned stimulation regimen; enumerated regimens yield conditional predictions for the observed treatment setting. Another two-center study predicts the logarithm of retrieved-oocyte count divided by starting FSH dose alongside early OHSS risk. Its regression errors are on that transformed scale, and discrepancies among its threshold metrics remain unresolved. These examples connect target transformation and predictor timing to performance interpretation [@EC031,EC032,R041,R042].==

> **§ Computational methods** : Trajectory summaries and recorded-action learning
> ==Treatment variables encode patient state and clinical choice. The quantity $ E[Y A=a,X=x]$ describes an observed conditional relationship; a recommendation concerns the consequence of assigning $a$. Attribution and input perturbation characterize the fitted mapping, while assignment-aware estimation addresses the intervention. Prognosis, imitation and policy evaluation therefore retain distinct objectives even when their columns and estimators coincide [@R005,R041,R042,R030,R048].==

> **§ Design challenges and directions for validated AI** : Transporting representations and evaluating their use
> ==Treatment support connects a learning target to an intervention contrast. Imitating observed prescriptions, forecasting outcomes under usual care and estimating treatment effects define different targets. Randomized allocation or a causal design addressing assignment and confounding connects a proposed policy to its effects. For multimodal and general-purpose systems, evaluation spans preprocessing, pretraining, missing-input handling, retrieval and human interaction. Component-level tests locate technical errors; end-to-end studies measure the recommendations and decisions produced by the complete system [@R041,R042,R012].==

---
*Machine-extracted; human verification pending. == ... == marks supporting content.*