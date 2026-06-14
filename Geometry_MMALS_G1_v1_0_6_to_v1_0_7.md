diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/ARTIFACT_MANIFEST.md /mnt/data/geometry-mmalls-g1-v103/ARTIFACT_MANIFEST.md
--- /mnt/data/geometry-mmalls-g1-v102/ARTIFACT_MANIFEST.md	2026-06-13 22:35:49.797416451 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/ARTIFACT_MANIFEST.md	2026-06-13 22:41:20.824607721 +0000
@@ -1,36 +1,32 @@
-# Geometry-MMALS G1 v1.0.1 Artifact Manifest
-
-Release-audit patch generated after critical review.
+# Geometry-MMALS G1 v1.0.3 Artifact Manifest
 
 ## Scientific status
 
-Accepted package claim: C0 pipeline validity only.
+Accepted claim: C0 implementation and protocol correction only.
 
-C1-C5 are specified as future experimental claims and require real per-seed runs, frozen gates, hardened baselines and claim manifests.
+C1-C6 remain unqualified until frozen-gate, multi-seed, controlled runs are
+archived.
 
 ## Main artifacts
 
-- `paper/Geometry_MMALS_G1_Article.pdf` - compiled article, v1.0.1, 31 pages.
-- `paper/main.tex` - LaTeX source.
-- `paper/references.bib` - bibliography.
-- `notebooks/Geometry_MMALS_G1_Colab.ipynb` - Colab-ready scaffold, explicitly labeled as G1-A supervised/grounded for angle loss.
-- `src/geometry_mmalls/` - executable scaffold.
-- `docs/CLAIMS_AND_GATES.md` - numeric pilot gates and non-claims.
-- `docs/NOTATION_BRIDGE.md` - MMALS-TPUT to Geometry-G1 notation bridge.
-- `docs/STATUS.md` - current claim status.
-
-## Validation performed
-
-- `pytest -q`: 12 tests passed.
-- `scripts/run_synthetic_smoke.py`: synthetic metric smoke completed.
-- LaTeX compiled to PDF with bibliography using pdfTeX + BibTeX.
-- PDF rendered to 31 PNG pages for visual inspection.
-
-## Key patch items
-
-- C0-only status clarified.
-- Notebook leakage risk annotated: G1-A supervised/grounded variant.
-- Fisher-Rao simplex utilities hardened near boundaries.
-- Dual memory stubs added for reconstructive audit and synthetic functional memory.
-- TPUT/G1 notation mismatch addressed.
-- Numeric gates added for CSR, ablation locality, kNN preservation, stress and seed counts.
+- `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
+- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
+- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md`
+- `src/geometry_mmalls/data.py` with `MultiAngleMNIST`
+- `src/geometry_mmalls/geometry.py` with `paired_route_geometry_loss`
+- `src/geometry_mmalls/metrics.py` with source-block and centroid metrics
+- `configs/rotated_mnist_g1.yaml` with paired-protocol settings
+- `docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch`
+
+## Core correction
+
+v1.0.2 used a single factor value inside each geometry batch. v1.0.3 uses
+same-source cross-angle views and evaluates geometry inside source blocks.
+
+## Validation performed during package generation
+
+- Notebook JSON and Python syntax validation.
+- Unit test suite: 16 tests passed.
+- Same-source multi-angle dataset smoke using locally available MNIST data.
+- Paired route-loss forward/backward smoke.
+- PDF render verification.
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/CHANGELOG.md /mnt/data/geometry-mmalls-g1-v103/CHANGELOG.md
--- /mnt/data/geometry-mmalls-g1-v102/CHANGELOG.md	2026-06-13 22:34:05.450448345 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/CHANGELOG.md	2026-06-13 22:34:10.733858272 +0000
@@ -1,5 +1,18 @@
 # Changelog
 
+## v1.0.3 - Cross-angle paired protocol correction
+
+- Replaced single-angle geometry batches with same-source multi-angle batches.
+- Added `MultiAngleMNIST` and a stable square-root-simplex paired geometry loss.
+- Preserved the continual sequence while using only previously seen angles as geometry anchors.
+- Added source identifiers to traces and source-block bootstrap metrics.
+- Replaced global pairwise significance and tie-fragile kNN evidence with paired-source and centroid geometry.
+- Added held-out interpolation accuracy, NLL, context interpolation and route interpolation controls.
+- Added staged accuracy matrices and trained-angle forgetting estimates.
+- Added signed causal route-direction probes with matched-norm orthogonal controls.
+- Added strict package version and git-SHA recording.
+- Kept C1-C6 explicitly unqualified pending multi-seed runs and hardened baselines.
+
 ## v1.0.2 - Numerical-stability and Colab execution patch
 
 - Fixed NaN gradients in `route_geodesic_loss` for identical or nearly identical routes.
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/CITATION.cff /mnt/data/geometry-mmalls-g1-v103/CITATION.cff
--- /mnt/data/geometry-mmalls-g1-v102/CITATION.cff	2026-06-13 18:02:36.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/CITATION.cff	2026-06-13 22:41:20.824176153 +0000
@@ -6,7 +6,7 @@
   - family-names: Harbonnier
     given-names: Guillaume
     orcid: ""
-version: 1.0.0
+version: 1.0.3
 date-released: 2026-06-13
 repository-code: "https://github.com/gharbonnier78/geometry-mmalls-g1"
 license: MIT
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/README.md /mnt/data/geometry-mmalls-g1-v103/README.md
--- /mnt/data/geometry-mmalls-g1-v102/README.md	2026-06-13 22:35:49.583612574 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/README.md	2026-06-13 22:41:20.823648385 +0000
@@ -4,7 +4,7 @@
 
 Geometry-MMALS G1 is a research specification and implementation scaffold for testing whether MMALS learns a meaningful internal geometry of representations, inferred contexts, routes, host transformations, synthesis states, and memory transport.
 
-> **Status:** research protocol and executable scaffold, patched as v1.0.1 after release audit. The repository currently supports a **C0 pipeline-validity claim only**. It does **not** claim that the proposed G1 experiments have succeeded. Included smoke outputs are synthetic and validate only the software and metric flow. C2+ claims require real runs, fixed numeric gates, seed reports, and hardened baselines.
+> **Status:** v1.0.3 protocol-correction release. The repository currently supports a **C0 implementation and protocol-validity claim only**. It does **not** claim that the G1 geometry gates have succeeded. C1-C6 require frozen thresholds, multi-seed runs, matched controls, archived manifests and hardened baselines.
 
 ## Why this repository exists
 
@@ -41,6 +41,16 @@
 
 No quantum-computing or quantum-advantage claim is made here.
 
+## v1.0.3 primary notebook
+
+`notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
+
+This protocol correction replaces the v1.0.2 single-angle geometry batch with
+same-source cross-angle views. It adds source-block metrics, held-out
+interpolation controls, staged forgetting evaluation and signed causal
+controls. The release remains a protocol implementation and does not claim that
+C1-C6 have passed.
+
 ## Repository map
 
 ```text
@@ -56,7 +66,9 @@
 ```
 
 
-## Release-audit patch v1.0.1
+## Numerical-stability patch v1.0.2
+
+The v1.0.2 patch fixes the uniform-route NaN gradient in the Fisher-Rao geodesic loss, adds a regression gate, finite-value checks, and a stabilized causal tangent probe.
 
 This patch addresses the main methodological risks identified during package review:
 
@@ -97,7 +109,7 @@
 
 ### Run in Colab
 
-Open `notebooks/Geometry_MMALS_G1_Colab.ipynb`. After publishing this folder, change the repository URL in the first setup cell if the GitHub location differs from:
+Open `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`. The first setup cell verifies package version `1.0.3` and records the active git commit SHA. After publishing this folder, change the repository URL only if the GitHub location differs from:
 
 ```text
 https://github.com/gharbonnier78/geometry-mmalls-g1
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/configs/rotated_mnist_g1.yaml /mnt/data/geometry-mmalls-g1-v103/configs/rotated_mnist_g1.yaml
--- /mnt/data/geometry-mmalls-g1-v102/configs/rotated_mnist_g1.yaml	2026-06-13 18:04:56.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/configs/rotated_mnist_g1.yaml	2026-06-13 22:34:10.731082948 +0000
@@ -38,6 +38,10 @@
   memory_reconstruction: 0.05
   route_bandwidth_degrees: 20.0
   route_far_margin: 0.35
+  paired_route_far_margin: 0.20
+  paired_route_far_weight: 0.25
+  paired_route_match_weight: 0.50
+  classification_anchor_replay: 0.0
 
 memory:
   reconstructive_examples_per_context: 128
@@ -53,3 +57,15 @@
   noise_std: 0.025
   drift_std: 0.04
   seed: 7
+
+paired_protocol:
+  primary_variant: paired_geometry
+  compared_variants: [no_geometry, paired_geometry]
+  development_source_limit: 512
+  development_test_source_limit: 256
+  full_source_limit: 6000
+  source_batch_size: 64
+  geometry_uses_seen_angles_only: true
+  classification_uses_current_angle_only: true
+  source_block_bootstrap: true
+  interpolation_angles_never_train: true
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/CLAIMS_AND_GATES.md /mnt/data/geometry-mmalls-g1-v103/docs/CLAIMS_AND_GATES.md
--- /mnt/data/geometry-mmalls-g1-v102/docs/CLAIMS_AND_GATES.md	2026-06-13 19:35:51.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/docs/CLAIMS_AND_GATES.md	2026-06-13 22:34:10.736372190 +0000
@@ -110,3 +110,18 @@
 - universal intelligence;
 - consciousness;
 - domain-general manifold discovery from a single synthetic benchmark.
+
+
+## v1.0.3 measurement policy amendment
+
+For RotatedMNIST G1 qualification:
+
+- distance-order and stress statistics must be computed inside same-source
+  cross-angle blocks and summarized across source images;
+- factor-centroid geometry must be reported as a complementary tie-free view;
+- uncertainty must use source-block bootstrap or permutation;
+- ordinary pairwise p-values over all sample pairs are descriptive only;
+- ordinary sample-level kNN is not a primary gate when the reference factor has
+  large tied neighborhoods;
+- a geometry-trained model must be compared with the same architecture without
+  paired geometry regularization.
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/EXPERIMENT_PROTOCOL.md /mnt/data/geometry-mmalls-g1-v103/docs/EXPERIMENT_PROTOCOL.md
--- /mnt/data/geometry-mmalls-g1-v102/docs/EXPERIMENT_PROTOCOL.md	2026-06-13 18:03:33.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/docs/EXPERIMENT_PROTOCOL.md	2026-06-13 22:34:10.735601667 +0000
@@ -16,6 +16,25 @@
 - continual stages: one declared sequence and its reversed control;
 - seeds: at least five for qualification, three only for development smoke runs.
 
+
+## 2.1 Cross-angle paired batch requirement (v1.0.3)
+
+A geometry loss is valid only when the optimization unit contains at least two
+distinct factor values. The primary G1-A protocol therefore groups several
+rotated views of the same MNIST source image in one batch item.
+
+At continual stage `t`, the paired geometry branch may use only angles already
+seen in stages `0..t`. Held-out interpolation and extrapolation angles remain
+excluded from training and model selection.
+
+Classification loss is applied to the current angle by default. Previous-angle
+views are geometry anchors, not automatically classification replay. Any
+classification replay must be declared as a separate ablation.
+
+Primary geometry statistics are computed inside source-image blocks and then
+bootstrapped across source images. Global all-pairs p-values and ordinary kNN
+over massively tied angle distances are not accepted as primary evidence.
+
 ## 3. Model boundary
 
 The primary experiment freezes a declared sensory encoder after a reference pretraining stage. This separates:
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/STATUS.md /mnt/data/geometry-mmalls-g1-v103/docs/STATUS.md
--- /mnt/data/geometry-mmalls-g1-v102/docs/STATUS.md	2026-06-13 22:00:06.426398376 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/docs/STATUS.md	2026-06-13 22:34:10.734661764 +0000
@@ -1,17 +1,22 @@
-# Current scientific status
+# Status
 
-Geometry-MMALS G1 v1.0.2 is a specification plus executable scaffold.
+## Current release: v1.0.3 protocol correction
 
-Accepted package claim: **C0 pipeline validity only**.
+The accepted claim remains **C0 pipeline and protocol implementation only**.
 
-Not yet claimed:
+v1.0.2 repaired numerical stability but its development run used one angle per
+geometry batch. Therefore the loss never observed cross-angle pairs and the run
+was non-diagnostic for grounded angular geometry.
 
-- C1 grounded descriptive geometry on real RotatedMNIST traces;
-- C2 predictive interpolation;
-- C3 reproducible host specialization;
-- C4 causal latent direction;
-- C5 continual geometric transport;
-- G2 energy-guided routing;
-- G3 phase-aware or quantum-inspired routing.
+v1.0.3 introduces a same-source cross-angle paired protocol. It is designed to
+make C1-C4 measurable, but no gate is considered passed until the notebook is
+run with frozen thresholds, multiple seeds, matched controls and archived
+results.
 
-A future experimental release must include real run manifests, per-seed CSVs, bootstrap confidence intervals, baseline sweeps, and a claim manifest tying every statement to artifacts.
+The primary notebook is:
+
+`notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
+
+The archived change report is:
+
+`docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch /mnt/data/geometry-mmalls-g1-v103/docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch
--- /mnt/data/geometry-mmalls-g1-v102/docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch	1970-01-01 00:00:00.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch	2026-06-13 22:41:21.054423803 +0000
@@ -0,0 +1,267 @@
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/ARTIFACT_MANIFEST.md /mnt/data/geometry-mmalls-g1-v103/ARTIFACT_MANIFEST.md
+--- /mnt/data/geometry-mmalls-g1-v102/ARTIFACT_MANIFEST.md	2026-06-13 22:35:49.797416451 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/ARTIFACT_MANIFEST.md	2026-06-13 22:41:20.824607721 +0000
+@@ -1,36 +1,32 @@
+-# Geometry-MMALS G1 v1.0.1 Artifact Manifest
+-
+-Release-audit patch generated after critical review.
++# Geometry-MMALS G1 v1.0.3 Artifact Manifest
+ 
+ ## Scientific status
+ 
+-Accepted package claim: C0 pipeline validity only.
++Accepted claim: C0 implementation and protocol correction only.
+ 
+-C1-C5 are specified as future experimental claims and require real per-seed runs, frozen gates, hardened baselines and claim manifests.
++C1-C6 remain unqualified until frozen-gate, multi-seed, controlled runs are
++archived.
+ 
+ ## Main artifacts
+ 
+-- `paper/Geometry_MMALS_G1_Article.pdf` - compiled article, v1.0.1, 31 pages.
+-- `paper/main.tex` - LaTeX source.
+-- `paper/references.bib` - bibliography.
+-- `notebooks/Geometry_MMALS_G1_Colab.ipynb` - Colab-ready scaffold, explicitly labeled as G1-A supervised/grounded for angle loss.
+-- `src/geometry_mmalls/` - executable scaffold.
+-- `docs/CLAIMS_AND_GATES.md` - numeric pilot gates and non-claims.
+-- `docs/NOTATION_BRIDGE.md` - MMALS-TPUT to Geometry-G1 notation bridge.
+-- `docs/STATUS.md` - current claim status.
+-
+-## Validation performed
+-
+-- `pytest -q`: 12 tests passed.
+-- `scripts/run_synthetic_smoke.py`: synthetic metric smoke completed.
+-- LaTeX compiled to PDF with bibliography using pdfTeX + BibTeX.
+-- PDF rendered to 31 PNG pages for visual inspection.
+-
+-## Key patch items
+-
+-- C0-only status clarified.
+-- Notebook leakage risk annotated: G1-A supervised/grounded variant.
+-- Fisher-Rao simplex utilities hardened near boundaries.
+-- Dual memory stubs added for reconstructive audit and synthetic functional memory.
+-- TPUT/G1 notation mismatch addressed.
+-- Numeric gates added for CSR, ablation locality, kNN preservation, stress and seed counts.
++- `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
++- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
++- `docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md`
++- `src/geometry_mmalls/data.py` with `MultiAngleMNIST`
++- `src/geometry_mmalls/geometry.py` with `paired_route_geometry_loss`
++- `src/geometry_mmalls/metrics.py` with source-block and centroid metrics
++- `configs/rotated_mnist_g1.yaml` with paired-protocol settings
++- `docs/changes/Geometry_MMALS_G1_v1_0_2_to_v1_0_3.patch`
++
++## Core correction
++
++v1.0.2 used a single factor value inside each geometry batch. v1.0.3 uses
++same-source cross-angle views and evaluates geometry inside source blocks.
++
++## Validation performed during package generation
++
++- Notebook JSON and Python syntax validation.
++- Unit test suite: 16 tests passed.
++- Same-source multi-angle dataset smoke using locally available MNIST data.
++- Paired route-loss forward/backward smoke.
++- PDF render verification.
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/CHANGELOG.md /mnt/data/geometry-mmalls-g1-v103/CHANGELOG.md
+--- /mnt/data/geometry-mmalls-g1-v102/CHANGELOG.md	2026-06-13 22:34:05.450448345 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/CHANGELOG.md	2026-06-13 22:34:10.733858272 +0000
+@@ -1,5 +1,18 @@
+ # Changelog
+ 
++## v1.0.3 - Cross-angle paired protocol correction
++
++- Replaced single-angle geometry batches with same-source multi-angle batches.
++- Added `MultiAngleMNIST` and a stable square-root-simplex paired geometry loss.
++- Preserved the continual sequence while using only previously seen angles as geometry anchors.
++- Added source identifiers to traces and source-block bootstrap metrics.
++- Replaced global pairwise significance and tie-fragile kNN evidence with paired-source and centroid geometry.
++- Added held-out interpolation accuracy, NLL, context interpolation and route interpolation controls.
++- Added staged accuracy matrices and trained-angle forgetting estimates.
++- Added signed causal route-direction probes with matched-norm orthogonal controls.
++- Added strict package version and git-SHA recording.
++- Kept C1-C6 explicitly unqualified pending multi-seed runs and hardened baselines.
++
+ ## v1.0.2 - Numerical-stability and Colab execution patch
+ 
+ - Fixed NaN gradients in `route_geodesic_loss` for identical or nearly identical routes.
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/CITATION.cff /mnt/data/geometry-mmalls-g1-v103/CITATION.cff
+--- /mnt/data/geometry-mmalls-g1-v102/CITATION.cff	2026-06-13 18:02:36.000000000 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/CITATION.cff	2026-06-13 22:41:20.824176153 +0000
+@@ -6,7 +6,7 @@
+   - family-names: Harbonnier
+     given-names: Guillaume
+     orcid: ""
+-version: 1.0.0
++version: 1.0.3
+ date-released: 2026-06-13
+ repository-code: "https://github.com/gharbonnier78/geometry-mmalls-g1"
+ license: MIT
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/README.md /mnt/data/geometry-mmalls-g1-v103/README.md
+--- /mnt/data/geometry-mmalls-g1-v102/README.md	2026-06-13 22:35:49.583612574 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/README.md	2026-06-13 22:41:20.823648385 +0000
+@@ -4,7 +4,7 @@
+ 
+ Geometry-MMALS G1 is a research specification and implementation scaffold for testing whether MMALS learns a meaningful internal geometry of representations, inferred contexts, routes, host transformations, synthesis states, and memory transport.
+ 
+-> **Status:** research protocol and executable scaffold, patched as v1.0.1 after release audit. The repository currently supports a **C0 pipeline-validity claim only**. It does **not** claim that the proposed G1 experiments have succeeded. Included smoke outputs are synthetic and validate only the software and metric flow. C2+ claims require real runs, fixed numeric gates, seed reports, and hardened baselines.
++> **Status:** v1.0.3 protocol-correction release. The repository currently supports a **C0 implementation and protocol-validity claim only**. It does **not** claim that the G1 geometry gates have succeeded. C1-C6 require frozen thresholds, multi-seed runs, matched controls, archived manifests and hardened baselines.
+ 
+ ## Why this repository exists
+ 
+@@ -41,6 +41,16 @@
+ 
+ No quantum-computing or quantum-advantage claim is made here.
+ 
++## v1.0.3 primary notebook
++
++`notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
++
++This protocol correction replaces the v1.0.2 single-angle geometry batch with
++same-source cross-angle views. It adds source-block metrics, held-out
++interpolation controls, staged forgetting evaluation and signed causal
++controls. The release remains a protocol implementation and does not claim that
++C1-C6 have passed.
++
+ ## Repository map
+ 
+ ```text
+@@ -56,7 +66,9 @@
+ ```
+ 
+ 
+-## Release-audit patch v1.0.1
++## Numerical-stability patch v1.0.2
++
++The v1.0.2 patch fixes the uniform-route NaN gradient in the Fisher-Rao geodesic loss, adds a regression gate, finite-value checks, and a stabilized causal tangent probe.
+ 
+ This patch addresses the main methodological risks identified during package review:
+ 
+@@ -97,7 +109,7 @@
+ 
+ ### Run in Colab
+ 
+-Open `notebooks/Geometry_MMALS_G1_Colab.ipynb`. After publishing this folder, change the repository URL in the first setup cell if the GitHub location differs from:
++Open `notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`. The first setup cell verifies package version `1.0.3` and records the active git commit SHA. After publishing this folder, change the repository URL only if the GitHub location differs from:
+ 
+ ```text
+ https://github.com/gharbonnier78/geometry-mmalls-g1
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/configs/rotated_mnist_g1.yaml /mnt/data/geometry-mmalls-g1-v103/configs/rotated_mnist_g1.yaml
+--- /mnt/data/geometry-mmalls-g1-v102/configs/rotated_mnist_g1.yaml	2026-06-13 18:04:56.000000000 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/configs/rotated_mnist_g1.yaml	2026-06-13 22:34:10.731082948 +0000
+@@ -38,6 +38,10 @@
+   memory_reconstruction: 0.05
+   route_bandwidth_degrees: 20.0
+   route_far_margin: 0.35
++  paired_route_far_margin: 0.20
++  paired_route_far_weight: 0.25
++  paired_route_match_weight: 0.50
++  classification_anchor_replay: 0.0
+ 
+ memory:
+   reconstructive_examples_per_context: 128
+@@ -53,3 +57,15 @@
+   noise_std: 0.025
+   drift_std: 0.04
+   seed: 7
++
++paired_protocol:
++  primary_variant: paired_geometry
++  compared_variants: [no_geometry, paired_geometry]
++  development_source_limit: 512
++  development_test_source_limit: 256
++  full_source_limit: 6000
++  source_batch_size: 64
++  geometry_uses_seen_angles_only: true
++  classification_uses_current_angle_only: true
++  source_block_bootstrap: true
++  interpolation_angles_never_train: true
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/CLAIMS_AND_GATES.md /mnt/data/geometry-mmalls-g1-v103/docs/CLAIMS_AND_GATES.md
+--- /mnt/data/geometry-mmalls-g1-v102/docs/CLAIMS_AND_GATES.md	2026-06-13 19:35:51.000000000 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/docs/CLAIMS_AND_GATES.md	2026-06-13 22:34:10.736372190 +0000
+@@ -110,3 +110,18 @@
+ - universal intelligence;
+ - consciousness;
+ - domain-general manifold discovery from a single synthetic benchmark.
++
++
++## v1.0.3 measurement policy amendment
++
++For RotatedMNIST G1 qualification:
++
++- distance-order and stress statistics must be computed inside same-source
++  cross-angle blocks and summarized across source images;
++- factor-centroid geometry must be reported as a complementary tie-free view;
++- uncertainty must use source-block bootstrap or permutation;
++- ordinary pairwise p-values over all sample pairs are descriptive only;
++- ordinary sample-level kNN is not a primary gate when the reference factor has
++  large tied neighborhoods;
++- a geometry-trained model must be compared with the same architecture without
++  paired geometry regularization.
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/EXPERIMENT_PROTOCOL.md /mnt/data/geometry-mmalls-g1-v103/docs/EXPERIMENT_PROTOCOL.md
+--- /mnt/data/geometry-mmalls-g1-v102/docs/EXPERIMENT_PROTOCOL.md	2026-06-13 18:03:33.000000000 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/docs/EXPERIMENT_PROTOCOL.md	2026-06-13 22:34:10.735601667 +0000
+@@ -16,6 +16,25 @@
+ - continual stages: one declared sequence and its reversed control;
+ - seeds: at least five for qualification, three only for development smoke runs.
+ 
++
++## 2.1 Cross-angle paired batch requirement (v1.0.3)
++
++A geometry loss is valid only when the optimization unit contains at least two
++distinct factor values. The primary G1-A protocol therefore groups several
++rotated views of the same MNIST source image in one batch item.
++
++At continual stage `t`, the paired geometry branch may use only angles already
++seen in stages `0..t`. Held-out interpolation and extrapolation angles remain
++excluded from training and model selection.
++
++Classification loss is applied to the current angle by default. Previous-angle
++views are geometry anchors, not automatically classification replay. Any
++classification replay must be declared as a separate ablation.
++
++Primary geometry statistics are computed inside source-image blocks and then
++bootstrapped across source images. Global all-pairs p-values and ordinary kNN
++over massively tied angle distances are not accepted as primary evidence.
++
+ ## 3. Model boundary
+ 
+ The primary experiment freezes a declared sensory encoder after a reference pretraining stage. This separates:
+diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/STATUS.md /mnt/data/geometry-mmalls-g1-v103/docs/STATUS.md
+--- /mnt/data/geometry-mmalls-g1-v102/docs/STATUS.md	2026-06-13 22:00:06.426398376 +0000
++++ /mnt/data/geometry-mmalls-g1-v103/docs/STATUS.md	2026-06-13 22:34:10.734661764 +0000
+@@ -1,17 +1,22 @@
+-# Current scientific status
++# Status
+ 
+-Geometry-MMALS G1 v1.0.2 is a specification plus executable scaffold.
++## Current release: v1.0.3 protocol correction
+ 
+-Accepted package claim: **C0 pipeline validity only**.
++The accepted claim remains **C0 pipeline and protocol implementation only**.
+ 
+-Not yet claimed:
++v1.0.2 repaired numerical stability but its development run used one angle per
++geometry batch. Therefore the loss never observed cross-angle pairs and the run
++was non-diagnostic for grounded angular geometry.
+ 
+-- C1 grounded descriptive geometry on real RotatedMNIST traces;
+-- C2 predictive interpolation;
+-- C3 reproducible host specialization;
+-- C4 causal latent direction;
+-- C5 continual geometric transport;
+-- G2 energy-guided routing;
+-- G3 phase-aware or quantum-inspired routing.
++v1.0.3 introduces a same-source cross-angle paired protocol. It is designed to
++make C1-C4 measurable, but no gate is considered passed until the notebook is
++run with frozen thresholds, multiple seeds, matched controls and archived
++results.
+ 
+-A future experimental release must include real run manifests, per-seed CSVs, bootstrap confidence intervals, baseline sweeps, and a claim manifest tying every statement to artifacts.
++The primary notebook is:
++
++`notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`
++
++The archived change report is:
++
++`docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md /mnt/data/geometry-mmalls-g1-v103/docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md
--- /mnt/data/geometry-mmalls-g1-v102/docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md	1970-01-01 00:00:00.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md	2026-06-13 22:34:10.819802107 +0000
@@ -0,0 +1,76 @@
+# Geometry-MMALS G1 v1.0.3
+## Cross-Angle Paired Geometry Protocol Correction Report
+
+**Date:** 2026-06-13  
+**Status:** protocol release; C0 only; C1-C6 remain unqualified.
+
+### Executive conclusion
+
+v1.0.2 repaired the Fisher-Rao numerical singularity and produced finite traces,
+but its geometry loss was applied inside fixed-angle batches. Every factor value
+inside a batch was identical, so the loss could not learn or test an ordered
+cross-angle geometry. v1.0.3 changes the optimization and measurement unit to
+the same source image observed at several angles.
+
+### Version history
+
+- v1.0.0: functional geometry specification and falsification ladder.
+- v1.0.1: claim gates, audit patch, notation bridge and memory stubs.
+- v1.0.2: numerical stability, finite guards and Colab execution.
+- v1.0.3: cross-angle paired protocol and source-block measurement.
+
+### v1.0.2 development evidence
+
+The finite development run reported distance-order correlations close to zero:
+sensory -0.0334, context -0.0383, route 0.0272 and synthesis 0.0118. These values
+do not support C1. They are not considered a decisive falsification because the
+training loss never compared different angles.
+
+Host ablations suggested two useful general hosts and two nearly inactive hosts,
+not yet localized, reproducible host specialization.
+
+The tangent probe showed symmetric route sensitivity in absolute norm, but it
+did not establish a signed angle-specific causal effect.
+
+### v1.0.3 scientific corrections
+
+1. Same-source cross-angle batches.
+2. Geometry anchors restricted to angles already seen in the continual sequence.
+3. Classification applied to the current angle by default.
+4. Stable square-root-simplex chordal loss for optimization.
+5. Fisher-Rao retained for evaluation.
+6. Source indices retained in traces.
+7. Source-block bootstrap instead of all-pairs p-values.
+8. Factor-centroid geometry instead of tie-fragile sample kNN.
+9. Held-out context and route interpolation controls.
+10. Staged accuracy and forgetting.
+11. Signed causal route projection with orthogonal controls.
+12. Package version and git SHA in every run manifest.
+
+### Mathematical protocol
+
+For source image x_i and seen angles u_1,...,u_A, the model produces routes
+r_i,a. The loss is:
+
+L_pair = L_local + lambda_far L_far + lambda_match L_match.
+
+Distances are optimized in square-root simplex coordinates. This distance is
+monotonic with the Fisher-Rao route distance but avoids arccos instability.
+
+### Claim discipline
+
+The new notebook makes C1-C4 measurable. It does not make them true. C5 still
+requires explicit memory transport and dual-memory experiments. C6 requires
+tuned baselines and secondary-dataset replication.
+
+### GitHub placement
+
+- notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb
+- docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf
+- docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md
+- configs/rotated_mnist_g1.yaml
+- src/geometry_mmalls/data.py
+- src/geometry_mmalls/geometry.py
+- src/geometry_mmalls/metrics.py
+- tests/test_geometry.py
+- tests/test_metrics.py
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/notebooks/Geometry_MMALS_G1_Colab.ipynb /mnt/data/geometry-mmalls-g1-v103/notebooks/Geometry_MMALS_G1_Colab.ipynb
--- /mnt/data/geometry-mmalls-g1-v102/notebooks/Geometry_MMALS_G1_Colab.ipynb	2026-06-13 22:00:04.801596642 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/notebooks/Geometry_MMALS_G1_Colab.ipynb	2026-06-13 22:34:10.804720402 +0000
@@ -2,76 +2,108 @@
  "cells": [
   {
    "cell_type": "markdown",
-   "id": "245c126d",
-   "metadata": {
-    "id": "245c126d"
-   },
+   "id": "8a907534",
+   "metadata": {},
    "source": [
-    "# Geometry-MMALS G1 - Grounded Functional Geometry\n",
+    "# Geometry-MMALS G1 v1.0.3\n",
+    "## Cross-Angle Paired Functional Geometry\n",
     "\n",
-    "Colab-ready scaffold for the controlled RotatedMNIST experiment. It separates the frozen sensory geometry from context, route, host and synthesis geometry.\n",
-    "\n",
-    "> **Status:** implementation scaffold, not a qualified G1 result. No quantum advantage is claimed.\n",
+    "**Scientific status:** protocol implementation and development experiment.  \n",
+    "**Accepted claim:** C0 pipeline/protocol integrity only.  \n",
+    "**Not claimed:** C1-C6 qualification, quantum advantage, backward transfer, or domain-general geometry.\n",
+    "\n",
+    "This notebook corrects the main scientific limitation of v1.0.2: each geometry\n",
+    "batch previously contained one fixed angle, so the geometry loss never observed\n",
+    "two distinct context values. v1.0.3 groups multiple rotated views of the **same\n",
+    "source image**, making route-distance versus angle-distance a real trainable and\n",
+    "measurable relation."
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "802b2927",
+   "metadata": {},
+   "source": [
+    "## Research history and change tracking\n",
     "\n",
-    "**v1.0.2 numerical-stability patch:** fixes the Fisher-Rao route-loss NaN gradient observed in the v1.0.1 development run, adds finite-value guards and stabilizes the causal tangent probe. C1-C5 remain unqualified.\n"
+    "| Version | Question | Outcome |\n",
+    "|---|---|---|\n",
+    "| v1.0.0 | Can functional MMALS geometry be specified and falsified? | Article, protocol and C0 scaffold created. |\n",
+    "| v1.0.1 | Can release claims, gates, memory stubs and notation be audited? | C0-only status and pilot gates formalized. |\n",
+    "| v1.0.2 | Can the Fisher-Rao route loss and Colab pipeline run without NaNs? | Numerical stability passed; finite traces obtained. |\n",
+    "| **v1.0.3** | Does the optimization unit actually contain cross-angle evidence? | Same-source paired protocol introduced. |\n",
+    "\n",
+    "### Tracked changes\n",
+    "\n",
+    "- **CHG-103-01:** same-source multi-angle data primitive.\n",
+    "- **CHG-103-02:** paired square-root-simplex geometry loss.\n",
+    "- **CHG-103-03:** continual stages use only angles already seen.\n",
+    "- **CHG-103-04:** source index retained in every trace.\n",
+    "- **CHG-103-05:** source-block bootstrap and factor-centroid metrics.\n",
+    "- **CHG-103-06:** held-out interpolation accuracy, NLL and route/context interpolation.\n",
+    "- **CHG-103-07:** staged accuracy matrix and forgetting.\n",
+    "- **CHG-103-08:** signed tangent effect with matched orthogonal controls.\n",
+    "- **CHG-103-09:** package version and git SHA recorded in the manifest.\n",
+    "- **CHG-103-10:** explicit non-claims and qualification checklist."
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "15521e44",
-   "metadata": {
-    "id": "15521e44"
-   },
+   "id": "3a5e636a",
+   "metadata": {},
    "source": [
-    "## 0. Setup\n",
+    "## Why the v1.0.2 run was non-diagnostic\n",
+    "\n",
+    "The v1.0.2 training loop used one `FixedAngleMNIST` loader at a time. Inside a\n",
+    "batch, every factor value was identical:\n",
+    "\n",
+    "\\[\n",
+    "u_1=u_2=\\cdots=u_B.\n",
+    "\\]\n",
+    "\n",
+    "The route loss could enforce within-angle consistency, but it could not learn an\n",
+    "ordered relation among `-60, -30, 0, 30, 60` degrees. Global all-sample\n",
+    "pairwise metrics also mixed digit identity with rotation and produced\n",
+    "dependence-inflated p-values and tie-fragile kNN scores.\n",
+    "\n",
+    "v1.0.3 changes the optimization and measurement unit to:\n",
+    "\n",
+    "> one source image observed under several declared angles.\n",
     "\n",
-    "The default clone URL assumes publication under `gharbonnier78/geometry-mmalls-g1`. In a local session, skip the clone and run `pip install -e .`."
+    "This is a stronger test of geometry, while still remaining a supervised\n",
+    "grounded G1-A variant."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "82122a76",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "82122a76",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385914987,
-     "user_tz": 300,
-     "elapsed": 17975,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "80f2114d-419e-4941-aec8-d78e6f407638"
-   },
+   "id": "8b75803d",
+   "metadata": {},
    "outputs": [],
    "source": [
     "import os\n",
     "import sys\n",
     "import shutil\n",
-    "import importlib\n",
     "import subprocess\n",
+    "import importlib\n",
+    "import importlib.metadata\n",
     "from pathlib import Path\n",
     "\n",
     "REPO_URL = \"https://github.com/gharbonnier78/geometry-mmalls-g1.git\"\n",
     "REPO_DIR = Path(\"/content/geometry-mmalls-g1\")\n",
     "SRC_DIR = REPO_DIR / \"src\"\n",
+    "EXPECTED_VERSION = \"1.0.3\"\n",
+    "FORCE_REFRESH = True\n",
+    "STRICT_VERSION = True\n",
     "\n",
-    "# Set FORCE_REFRESH=True after the v1.0.2 package is pushed to GitHub.\n",
-    "FORCE_REFRESH = False\n",
     "if FORCE_REFRESH and REPO_DIR.exists():\n",
     "    shutil.rmtree(REPO_DIR)\n",
     "\n",
     "if not REPO_DIR.exists():\n",
-    "    subprocess.run([\"git\", \"clone\", REPO_URL, str(REPO_DIR)], check=True)\n",
-    "\n",
-    "assert (REPO_DIR / \"pyproject.toml\").exists(), f\"Missing pyproject.toml in {REPO_DIR}\"\n",
-    "assert (SRC_DIR / \"geometry_mmalls\" / \"__init__.py\").exists(), \"Missing geometry_mmalls package\"\n",
+    "    subprocess.run(\n",
+    "        [\"git\", \"clone\", \"--depth\", \"1\", REPO_URL, str(REPO_DIR)],\n",
+    "        check=True,\n",
+    "    )\n",
     "\n",
     "os.chdir(REPO_DIR)\n",
     "subprocess.run(\n",
@@ -85,883 +117,1145 @@
     "importlib.invalidate_caches()\n",
     "\n",
     "import geometry_mmalls\n",
+    "\n",
+    "package_version = importlib.metadata.version(\"geometry-mmalls-g1\")\n",
+    "git_sha = subprocess.check_output(\n",
+    "    [\"git\", \"rev-parse\", \"HEAD\"], cwd=REPO_DIR, text=True\n",
+    ").strip()\n",
+    "\n",
     "print(\"Python:\", sys.executable)\n",
-    "print(\"Repository:\", REPO_DIR)\n",
-    "print(\"geometry_mmalls:\", geometry_mmalls.__file__)\n"
+    "print(\"Package:\", geometry_mmalls.__file__)\n",
+    "print(\"Package version:\", package_version)\n",
+    "print(\"Git SHA:\", git_sha)\n",
+    "\n",
+    "if package_version != EXPECTED_VERSION:\n",
+    "    message = (\n",
+    "        f\"Expected geometry-mmalls-g1 {EXPECTED_VERSION}, got {package_version}. \"\n",
+    "        \"Push the v1.0.3 package or install the supplied v1.0.3 ZIP before running.\"\n",
+    "    )\n",
+    "    if STRICT_VERSION:\n",
+    "        raise RuntimeError(message)\n",
+    "    print(\"WARNING:\", message)"
    ]
   },
   {
    "cell_type": "code",
-   "source": [
-    "from pathlib import Path\n",
-    "import geometry_mmalls\n",
-    "\n",
-    "loaded_from = Path(geometry_mmalls.__file__).resolve()\n",
-    "expected_root = Path(\"/content/geometry-mmalls-g1/src/geometry_mmalls\").resolve()\n",
-    "assert expected_root in loaded_from.parents or loaded_from.parent == expected_root, (\n",
-    "    f\"Wrong geometry_mmalls package loaded: {loaded_from}\"\n",
-    ")\n",
-    "print(\"Canonical Geometry-G1 package verified:\", loaded_from)\n"
-   ],
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "x9Z96Pxn3yGj",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385932172,
-     "user_tz": 300,
-     "elapsed": 17180,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "28f554c7-b337-472b-b01f-c6f22476a3fb"
-   },
-   "id": "x9Z96Pxn3yGj",
-   "execution_count": null,
-   "outputs": []
-  },
-  {
-   "cell_type": "code",
    "execution_count": null,
-   "id": "904dd9e8",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "904dd9e8",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385944983,
-     "user_tz": 300,
-     "elapsed": 12822,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "a01024a2-8ca4-45b7-96ff-f8452d6c4a24"
-   },
+   "id": "29b0450f",
+   "metadata": {},
    "outputs": [],
    "source": [
     "from pathlib import Path\n",
-    "import copy, json, random, time\n",
-    "import numpy as np, pandas as pd, torch, yaml\n",
+    "import copy\n",
+    "import json\n",
+    "import math\n",
+    "import random\n",
+    "import time\n",
+    "\n",
+    "import numpy as np\n",
+    "import pandas as pd\n",
+    "import torch\n",
     "import torch.nn.functional as F\n",
+    "import yaml\n",
     "from torch.utils.data import DataLoader, Subset\n",
-    "from geometry_mmalls.data import FixedAngleMNIST\n",
-    "from geometry_mmalls.geometry import normalized_stress, pairwise_fisher_rao\n",
+    "from torchvision.datasets import MNIST\n",
+    "\n",
+    "from geometry_mmalls.data import FixedAngleMNIST, MultiAngleMNIST\n",
+    "from geometry_mmalls.geometry import (\n",
+    "    fisher_rao_distance,\n",
+    "    paired_route_geometry_loss,\n",
+    ")\n",
     "from geometry_mmalls.metrics import (\n",
-    "    distance_order_correlation,\n",
-    "    euclidean_distance_matrix,\n",
-    "    neighborhood_preservation,\n",
-    "    pairwise_factor_distance,\n",
+    "    bootstrap_mean_ci,\n",
+    "    centroid_geometry_scores,\n",
+    "    grouped_geometry_scores,\n",
     ")\n",
     "from geometry_mmalls.model import GeometryMMALS, SmallConvEncoder\n",
     "\n",
+    "config = yaml.safe_load(Path(\"configs/rotated_mnist_g1.yaml\").read_text())\n",
     "\n",
-    "def route_geodesic_loss(\n",
-    "    routes: torch.Tensor,\n",
-    "    factor: torch.Tensor,\n",
-    "    bandwidth: float = 20.0,\n",
-    "    margin: float = 0.35,\n",
-    "    far_weight: float = 0.25,\n",
-    "    eps: float = 1e-8,\n",
-    ") -> torch.Tensor:\n",
-    "    \"\"\"Numerically stable G1-A Fisher-Rao route loss.\n",
-    "\n",
-    "    The diagonal is masked before arccos and the affinity is clamped with a\n",
-    "    dtype-aware epsilon. This prevents the v1.0.1 finite-forward/NaN-backward\n",
-    "    failure when routes are identical or nearly identical.\n",
-    "    \"\"\"\n",
-    "    if routes.ndim != 2:\n",
-    "        raise ValueError(\"routes must have shape [batch, hosts]\")\n",
-    "    factor = factor.reshape(-1).to(routes.device, routes.dtype)\n",
-    "    if factor.shape[0] != routes.shape[0]:\n",
-    "        raise ValueError(\"factor and routes must have the same batch length\")\n",
-    "\n",
-    "    p = routes.clamp_min(eps)\n",
-    "    p = p / p.sum(dim=-1, keepdim=True)\n",
-    "    roots = torch.sqrt(p)\n",
-    "    affinity = roots @ roots.T\n",
-    "    eye = torch.eye(routes.shape[0], dtype=torch.bool, device=routes.device)\n",
-    "    safe_eps = max(float(eps), 32.0 * torch.finfo(routes.dtype).eps)\n",
-    "    affinity = affinity.masked_fill(eye, 0.0)\n",
-    "    affinity = torch.clamp(affinity, safe_eps, 1.0 - safe_eps)\n",
-    "    d_route = 2.0 * torch.arccos(affinity)\n",
-    "    d_route = d_route.masked_fill(eye, 0.0)\n",
-    "\n",
-    "    d_factor = torch.abs(factor[:, None] - factor[None, :])\n",
-    "    near_w = torch.exp(-torch.square(d_factor / max(float(bandwidth), eps)))\n",
-    "    near_w = near_w.masked_fill(eye, 0.0)\n",
-    "    smooth = (near_w * torch.square(d_route)).sum() / near_w.sum().clamp_min(eps)\n",
-    "\n",
-    "    far_mask = (d_factor >= float(bandwidth)) & (~eye)\n",
-    "    if torch.any(far_mask):\n",
-    "        far_penalty = torch.relu(float(margin) - d_route[far_mask]).square().mean()\n",
-    "    else:\n",
-    "        far_penalty = torch.zeros((), dtype=routes.dtype, device=routes.device)\n",
-    "    return smooth + float(far_weight) * far_penalty\n",
+    "RUN_MODE = \"development\"  # \"development\" or \"qualification\"\n",
+    "SEED = 0\n",
+    "METHODS = [\"no_geometry\", \"paired_geometry\"]\n",
+    "DEVICE = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n",
+    "\n",
+    "random.seed(SEED)\n",
+    "np.random.seed(SEED)\n",
+    "torch.manual_seed(SEED)\n",
+    "if torch.cuda.is_available():\n",
+    "    torch.cuda.manual_seed_all(SEED)\n",
     "\n",
+    "train_angles = list(map(float, config[\"data\"][\"train_angles\"]))\n",
+    "interp_angles = list(map(float, config[\"data\"][\"interpolation_angles\"]))\n",
+    "extra_angles = list(map(float, config[\"data\"][\"extrapolation_angles\"]))\n",
+    "all_eval_angles = train_angles + interp_angles + extra_angles\n",
+    "\n",
+    "if RUN_MODE == \"development\":\n",
+    "    TRAIN_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"development_source_limit\"])\n",
+    "    TEST_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"development_test_source_limit\"])\n",
+    "    SENSORY_EPOCHS = 2\n",
+    "    STAGE_EPOCHS = 2\n",
+    "    BOOTSTRAP_SAMPLES = 500\n",
+    "else:\n",
+    "    TRAIN_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"full_source_limit\"])\n",
+    "    TEST_SOURCE_LIMIT = 2000\n",
+    "    SENSORY_EPOCHS = int(config[\"training\"][\"sensory_pretrain_epochs\"])\n",
+    "    STAGE_EPOCHS = int(config[\"training\"][\"stage_epochs\"])\n",
+    "    BOOTSTRAP_SAMPLES = int(config[\"metrics\"][\"bootstrap_samples\"])\n",
+    "\n",
+    "SOURCE_BATCH_SIZE = int(config[\"paired_protocol\"][\"source_batch_size\"])\n",
+    "print({\n",
+    "    \"run_mode\": RUN_MODE,\n",
+    "    \"device\": str(DEVICE),\n",
+    "    \"methods\": METHODS,\n",
+    "    \"train_source_limit\": TRAIN_SOURCE_LIMIT,\n",
+    "    \"test_source_limit\": TEST_SOURCE_LIMIT,\n",
+    "})"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "cd9af3db",
+   "metadata": {},
+   "source": [
+    "## 1. Numerical and structural self-test\n",
     "\n",
-    "# Regression gate: v1.0.1 failed here because arccos received affinity == 1.\n",
-    "_probe_logits = torch.zeros(16, 4, requires_grad=True)\n",
+    "The training loss uses chordal distance in square-root simplex coordinates.\n",
+    "This is monotonic with Fisher-Rao distance but avoids the derivative singularity\n",
+    "of `arccos` during optimization. Fisher-Rao remains the evaluation distance."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "c4dcf34b",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "_probe_logits = torch.randn(8, 5, 4, requires_grad=True)\n",
     "_probe_routes = torch.softmax(_probe_logits, dim=-1)\n",
-    "_probe_factor = torch.linspace(-60, 60, 16)\n",
-    "_probe_loss = route_geodesic_loss(_probe_routes, _probe_factor)\n",
+    "_probe_angles = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])\n",
+    "_probe_loss = paired_route_geometry_loss(_probe_routes, _probe_angles)\n",
     "_probe_loss.backward()\n",
-    "assert torch.isfinite(_probe_loss)\n",
-    "assert _probe_logits.grad is not None and torch.isfinite(_probe_logits.grad).all()\n",
-    "print(\"Stable route-geodesic backward gate: PASS\")\n",
     "\n",
-    "config = yaml.safe_load(Path('configs/rotated_mnist_g1.yaml').read_text())\n",
-    "RUN_FULL, SEED = False, 0\n",
-    "DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n",
-    "random.seed(SEED); np.random.seed(SEED); torch.manual_seed(SEED)\n",
-    "if torch.cuda.is_available():\n",
-    "    torch.cuda.manual_seed_all(SEED)\n",
-    "print(DEVICE, config['data'])\n"
+    "assert torch.isfinite(_probe_loss)\n",
+    "assert _probe_logits.grad is not None\n",
+    "assert torch.isfinite(_probe_logits.grad).all()\n",
+    "print(\"Paired route-geometry backward gate: PASS\", float(_probe_loss.detach()))"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "4f74ab77",
-   "metadata": {
-    "id": "4f74ab77"
-   },
+   "id": "26694811",
+   "metadata": {},
    "source": [
-    "## 1. Controlled data protocol\n",
+    "## 2. Controlled source split\n",
     "\n",
-    "The true angle is retained for evaluation and declared geometry losses, but is never passed to the deployable router. Interpolation angles remain outside training and model selection."
+    "The same source indices are used at every angle. Interpolation and extrapolation\n",
+    "angles are never included in training. The split is deterministic and recorded."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "63d4fd0d",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "63d4fd0d",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385947201,
-     "user_tz": 300,
-     "elapsed": 1845,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "f2bec9db-b614-45ec-cdfe-c1018e241059"
-   },
+   "id": "c4235471",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "root = Path(config['data']['root'])\n",
-    "train_angles = list(map(float, config['data']['train_angles']))\n",
-    "interp_angles = list(map(float, config['data']['interpolation_angles']))\n",
-    "limit = None if RUN_FULL else 2000\n",
+    "root = Path(config[\"data\"][\"root\"])\n",
+    "base_train = MNIST(root=str(root), train=True, download=True)\n",
+    "base_test = MNIST(root=str(root), train=False, download=True)\n",
+    "\n",
+    "rng = np.random.default_rng(SEED)\n",
+    "train_indices = rng.permutation(len(base_train))[:TRAIN_SOURCE_LIMIT].tolist()\n",
+    "test_indices = rng.permutation(len(base_test))[:TEST_SOURCE_LIMIT].tolist()\n",
     "\n",
-    "def loader(angle, train, shuffle):\n",
+    "def fixed_loader(angle, train, indices, shuffle):\n",
     "    ds = FixedAngleMNIST(root, angle=angle, train=train, download=True)\n",
-    "    if limit: ds = Subset(ds, range(min(limit, len(ds))))\n",
-    "    return DataLoader(ds, batch_size=128, shuffle=shuffle, num_workers=0)\n",
+    "    ds = Subset(ds, indices)\n",
+    "    return DataLoader(\n",
+    "        ds,\n",
+    "        batch_size=128,\n",
+    "        shuffle=shuffle,\n",
+    "        num_workers=0,\n",
+    "    )\n",
     "\n",
-    "train_loaders = {a: loader(a, True, True) for a in train_angles}\n",
-    "test_loaders = {a: loader(a, False, False) for a in train_angles}\n",
-    "interp_loaders = {a: loader(a, False, False) for a in interp_angles}"
+    "def multi_loader(angles, train, indices, shuffle):\n",
+    "    ds = MultiAngleMNIST(\n",
+    "        root,\n",
+    "        angles=angles,\n",
+    "        train=train,\n",
+    "        indices=indices,\n",
+    "        download=True,\n",
+    "    )\n",
+    "    return DataLoader(\n",
+    "        ds,\n",
+    "        batch_size=SOURCE_BATCH_SIZE,\n",
+    "        shuffle=shuffle,\n",
+    "        num_workers=0,\n",
+    "    )\n",
+    "\n",
+    "split_manifest = {\n",
+    "    \"seed\": SEED,\n",
+    "    \"train_source_count\": len(train_indices),\n",
+    "    \"test_source_count\": len(test_indices),\n",
+    "    \"train_index_checksum\": int(np.sum(train_indices)),\n",
+    "    \"test_index_checksum\": int(np.sum(test_indices)),\n",
+    "}\n",
+    "split_manifest"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "1e7be274",
-   "metadata": {
-    "id": "1e7be274"
-   },
+   "id": "da478339",
+   "metadata": {},
    "source": [
-    "## 2. Pretrain and freeze the sensory grove\n",
+    "## 3. Pretrain and freeze the sensory grove\n",
     "\n",
-    "This boundary prevents geometry already learned by perception from being attributed automatically to MMALS."
+    "The frozen encoder is a control boundary. Geometry already present in `z0` is\n",
+    "reported alongside context, route and synthesis geometry."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "29c7fa74",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "29c7fa74",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385954841,
-     "user_tz": 300,
-     "elapsed": 7638,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "a2fdb6bb-ec54-4501-c5cd-d2ae4ab6d163"
-   },
+   "id": "28aaac70",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "latent_dim = int(config['model']['latent_dim'])\n",
+    "latent_dim = int(config[\"model\"][\"latent_dim\"])\n",
     "encoder = SmallConvEncoder(latent_dim).to(DEVICE)\n",
-    "head = torch.nn.Linear(latent_dim, 10).to(DEVICE)\n",
-    "opt = torch.optim.AdamW(\n",
-    "    list(encoder.parameters()) + list(head.parameters()),\n",
-    "    lr=float(config['training']['learning_rate']),\n",
-    "    weight_decay=float(config['training']['weight_decay']),\n",
+    "sensory_head = torch.nn.Linear(latent_dim, 10).to(DEVICE)\n",
+    "sensory_optimizer = torch.optim.AdamW(\n",
+    "    list(encoder.parameters()) + list(sensory_head.parameters()),\n",
+    "    lr=float(config[\"training\"][\"learning_rate\"]),\n",
+    "    weight_decay=float(config[\"training\"][\"weight_decay\"]),\n",
     ")\n",
     "\n",
-    "sensory_epochs = int(config['training']['sensory_pretrain_epochs']) if RUN_FULL else 2\n",
     "sensory_history = []\n",
-    "for epoch in range(sensory_epochs):\n",
-    "    encoder.train(); total = correct = 0; epoch_loss = 0.0\n",
-    "    for x, y, _, _ in train_loaders[0.0]:\n",
+    "sensory_loader = fixed_loader(0.0, True, train_indices, True)\n",
+    "\n",
+    "for epoch in range(SENSORY_EPOCHS):\n",
+    "    encoder.train()\n",
+    "    total = correct = 0\n",
+    "    loss_sum = 0.0\n",
+    "    for x, y, _, _ in sensory_loader:\n",
     "        x, y = x.to(DEVICE), y.to(DEVICE)\n",
-    "        logits = head(encoder(x))\n",
+    "        logits = sensory_head(encoder(x))\n",
     "        loss = F.cross_entropy(logits, y)\n",
     "        if not torch.isfinite(loss):\n",
     "            raise FloatingPointError(\"Non-finite sensory loss\")\n",
-    "        opt.zero_grad(set_to_none=True)\n",
+    "        sensory_optimizer.zero_grad(set_to_none=True)\n",
     "        loss.backward()\n",
-    "        torch.nn.utils.clip_grad_norm_(list(encoder.parameters()) + list(head.parameters()), 5.0)\n",
-    "        opt.step()\n",
-    "        total += y.numel(); correct += (logits.argmax(1) == y).sum().item()\n",
-    "        epoch_loss += float(loss.detach()) * y.numel()\n",
-    "    row = {'epoch': epoch, 'loss': epoch_loss/total, 'accuracy': correct/total}\n",
+    "        torch.nn.utils.clip_grad_norm_(\n",
+    "            list(encoder.parameters()) + list(sensory_head.parameters()), 5.0\n",
+    "        )\n",
+    "        sensory_optimizer.step()\n",
+    "        total += y.numel()\n",
+    "        correct += (logits.argmax(1) == y).sum().item()\n",
+    "        loss_sum += float(loss.detach()) * y.numel()\n",
+    "    row = {\n",
+    "        \"epoch\": epoch,\n",
+    "        \"loss\": loss_sum / total,\n",
+    "        \"accuracy\": correct / total,\n",
+    "    }\n",
     "    sensory_history.append(row)\n",
     "    print(row)\n",
     "\n",
-    "sensory_state = copy.deepcopy(encoder.state_dict())\n"
+    "sensory_state = copy.deepcopy(encoder.state_dict())"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "a618eeb3",
-   "metadata": {
-    "id": "a618eeb3"
-   },
+   "id": "5045b0a5",
+   "metadata": {},
    "source": [
-    "## 3. MMALS route-host model and visible G1 losses"
+    "## 4. Continual training variants\n",
+    "\n",
+    "### `no_geometry`\n",
+    "Same architecture and sequential angle schedule, but no paired route geometry.\n",
+    "\n",
+    "### `paired_geometry`\n",
+    "At stage `t`, each source is rendered at all angles already seen in stages\n",
+    "`0..t`. Classification loss is applied to the current angle only. Previous\n",
+    "views are geometry anchors. This is not claimed as a replay-free continual\n",
+    "learning method; it is a controlled G1-A geometry test."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "0be3120b",
-   "metadata": {
-    "id": "0be3120b",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385954883,
-     "user_tz": 300,
-     "elapsed": 21,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    }
-   },
+   "id": "260d8c0c",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "encoder.load_state_dict(sensory_state)\n",
-    "model = GeometryMMALS(\n",
-    "    encoder, latent_dim=latent_dim,\n",
-    "    context_dim=int(config['model']['context_dim']),\n",
-    "    num_hosts=int(config['model']['num_hosts']),\n",
-    "    host_hidden_dim=int(config['model']['host_hidden_dim']),\n",
-    "    freeze_encoder=True,\n",
-    ").to(DEVICE)\n",
-    "opt = torch.optim.AdamW(\n",
-    "    [p for p in model.parameters() if p.requires_grad],\n",
-    "    lr=float(config['training']['learning_rate']),\n",
-    "    weight_decay=float(config['training']['weight_decay']),\n",
-    ")\n",
-    "\n",
-    "\n",
-    "def diversity(host_outputs):\n",
+    "def host_diversity(host_outputs):\n",
     "    h = F.normalize(host_outputs, dim=-1)\n",
-    "    sim = torch.einsum('bhd,bjd->bhj', h, h)\n",
+    "    sim = torch.einsum(\"bhd,bjd->bhj\", h, h)\n",
     "    mask = ~torch.eye(sim.shape[-1], dtype=torch.bool, device=sim.device)\n",
     "    return sim[:, mask].square().mean()\n",
     "\n",
-    "\n",
-    "def assert_finite_trace(tr, where):\n",
+    "def assert_finite_trace(trace, where):\n",
     "    tensors = {\n",
-    "        'z0': tr.z0,\n",
-    "        'context': tr.context,\n",
-    "        'route': tr.route,\n",
-    "        'host_outputs': tr.host_outputs,\n",
-    "        'z_mm': tr.z_mm,\n",
-    "        'logits': tr.logits,\n",
+    "        \"z0\": trace.z0,\n",
+    "        \"context\": trace.context,\n",
+    "        \"route\": trace.route,\n",
+    "        \"host_outputs\": trace.host_outputs,\n",
+    "        \"z_mm\": trace.z_mm,\n",
+    "        \"logits\": trace.logits,\n",
     "    }\n",
     "    bad = [name for name, value in tensors.items() if not torch.isfinite(value).all()]\n",
     "    if bad:\n",
     "        raise FloatingPointError(f\"Non-finite tensors at {where}: {bad}\")\n",
     "\n",
+    "@torch.no_grad()\n",
+    "def evaluate_model(model, angles, stage, method):\n",
+    "    rows = []\n",
+    "    model.eval()\n",
+    "    for angle in angles:\n",
+    "        loader = fixed_loader(angle, False, test_indices, False)\n",
+    "        total = correct = 0\n",
+    "        nll_sum = 0.0\n",
+    "        for x, y, _, _ in loader:\n",
+    "            x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "            trace = model(x)\n",
+    "            assert_finite_trace(trace, f\"eval method={method}, angle={angle}\")\n",
+    "            nll = F.cross_entropy(trace.logits, y, reduction=\"sum\")\n",
+    "            total += y.numel()\n",
+    "            correct += (trace.logits.argmax(1) == y).sum().item()\n",
+    "            nll_sum += float(nll)\n",
+    "        rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"stage\": stage,\n",
+    "            \"angle\": angle,\n",
+    "            \"angle_type\": (\n",
+    "                \"train\" if angle in train_angles\n",
+    "                else \"interpolation\" if angle in interp_angles\n",
+    "                else \"extrapolation\"\n",
+    "            ),\n",
+    "            \"accuracy\": correct / total,\n",
+    "            \"nll\": nll_sum / total,\n",
+    "        })\n",
+    "    return rows\n",
+    "\n",
+    "def build_model():\n",
+    "    local_encoder = SmallConvEncoder(latent_dim).to(DEVICE)\n",
+    "    local_encoder.load_state_dict(sensory_state)\n",
+    "    return GeometryMMALS(\n",
+    "        local_encoder,\n",
+    "        latent_dim=latent_dim,\n",
+    "        context_dim=int(config[\"model\"][\"context_dim\"]),\n",
+    "        num_hosts=int(config[\"model\"][\"num_hosts\"]),\n",
+    "        host_hidden_dim=int(config[\"model\"][\"host_hidden_dim\"]),\n",
+    "        freeze_encoder=True,\n",
+    "    ).to(DEVICE)\n",
+    "\n",
+    "def train_method(method):\n",
+    "    model = build_model()\n",
+    "    optimizer = torch.optim.AdamW(\n",
+    "        [p for p in model.parameters() if p.requires_grad],\n",
+    "        lr=float(config[\"training\"][\"learning_rate\"]),\n",
+    "        weight_decay=float(config[\"training\"][\"weight_decay\"]),\n",
+    "    )\n",
+    "    stage_rows = []\n",
+    "    evaluation_rows = []\n",
     "\n",
-    "def train_stage(angle, epochs=1):\n",
-    "    model.train()\n",
-    "    totals = {'loss': 0.0, 'ce': 0.0, 'geo': 0.0, 'diversity': 0.0, 'samples': 0}\n",
-    "    for epoch in range(epochs):\n",
-    "        for batch_id, (x, y, u, _) in enumerate(train_loaders[angle]):\n",
-    "            x, y, u = x.to(DEVICE), y.to(DEVICE), u.to(DEVICE)\n",
-    "            tr = model(x)\n",
-    "            assert_finite_trace(tr, f\"angle={angle}, epoch={epoch}, batch={batch_id}, forward\")\n",
-    "            ce = F.cross_entropy(tr.logits, y)\n",
-    "            # G1-A supervised/grounded variant: u shapes the declared geometry\n",
-    "            # loss only. It is never passed to the deployable router.\n",
-    "            geo = route_geodesic_loss(\n",
-    "                tr.route,\n",
-    "                u,\n",
-    "                bandwidth=float(config['losses']['route_bandwidth_degrees']),\n",
-    "                margin=float(config['losses']['route_far_margin']),\n",
-    "            )\n",
-    "            div = diversity(tr.host_outputs)\n",
-    "            loss = (\n",
-    "                float(config['losses']['classification']) * ce\n",
-    "                + float(config['losses']['route_geometry']) * geo\n",
-    "                + float(config['losses']['host_functional_diversity']) * div\n",
-    "            )\n",
-    "            if not torch.isfinite(torch.stack([ce, geo, div, loss])).all():\n",
-    "                raise FloatingPointError(\n",
-    "                    f\"Non-finite loss at angle={angle}, epoch={epoch}, batch={batch_id}: \"\n",
-    "                    f\"ce={ce.item()}, geo={geo.item()}, diversity={div.item()}, loss={loss.item()}\"\n",
+    "    for stage, current_angle in enumerate(train_angles):\n",
+    "        seen_angles = train_angles[: stage + 1]\n",
+    "        totals = {\"samples\": 0, \"loss\": 0.0, \"ce\": 0.0, \"geo\": 0.0, \"div\": 0.0}\n",
+    "\n",
+    "        if method == \"paired_geometry\":\n",
+    "            loader = multi_loader(seen_angles, True, train_indices, True)\n",
+    "        else:\n",
+    "            loader = fixed_loader(current_angle, True, train_indices, True)\n",
+    "\n",
+    "        model.train()\n",
+    "        for epoch in range(STAGE_EPOCHS):\n",
+    "            for batch_id, batch in enumerate(loader):\n",
+    "                if method == \"paired_geometry\":\n",
+    "                    views, y, factors, _ = batch\n",
+    "                    batch_size, angle_count = views.shape[:2]\n",
+    "                    flat_views = views.reshape(-1, *views.shape[2:]).to(DEVICE)\n",
+    "                    y = y.to(DEVICE)\n",
+    "                    factors = factors.to(DEVICE)\n",
+    "\n",
+    "                    trace = model(flat_views)\n",
+    "                    assert_finite_trace(\n",
+    "                        trace,\n",
+    "                        f\"{method}, stage={stage}, epoch={epoch}, batch={batch_id}\",\n",
+    "                    )\n",
+    "                    logits = trace.logits.reshape(batch_size, angle_count, -1)\n",
+    "                    routes = trace.route.reshape(batch_size, angle_count, -1)\n",
+    "                    hosts = trace.host_outputs.reshape(\n",
+    "                        batch_size, angle_count, trace.host_outputs.shape[1], -1\n",
+    "                    )\n",
+    "\n",
+    "                    current_index = angle_count - 1\n",
+    "                    ce = F.cross_entropy(logits[:, current_index], y)\n",
+    "                    geo = paired_route_geometry_loss(\n",
+    "                        routes,\n",
+    "                        factors,\n",
+    "                        bandwidth=float(config[\"losses\"][\"route_bandwidth_degrees\"]),\n",
+    "                        far_margin=float(config[\"losses\"][\"paired_route_far_margin\"]),\n",
+    "                        far_weight=float(config[\"losses\"][\"paired_route_far_weight\"]),\n",
+    "                        match_weight=float(config[\"losses\"][\"paired_route_match_weight\"]),\n",
+    "                    )\n",
+    "                    div = host_diversity(hosts[:, current_index])\n",
+    "                    sample_count = batch_size\n",
+    "                else:\n",
+    "                    x, y, _, _ = batch\n",
+    "                    x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "                    trace = model(x)\n",
+    "                    assert_finite_trace(\n",
+    "                        trace,\n",
+    "                        f\"{method}, stage={stage}, epoch={epoch}, batch={batch_id}\",\n",
+    "                    )\n",
+    "                    ce = F.cross_entropy(trace.logits, y)\n",
+    "                    geo = trace.route.sum() * 0.0\n",
+    "                    div = host_diversity(trace.host_outputs)\n",
+    "                    sample_count = y.numel()\n",
+    "\n",
+    "                loss = (\n",
+    "                    float(config[\"losses\"][\"classification\"]) * ce\n",
+    "                    + float(config[\"losses\"][\"route_geometry\"]) * geo\n",
+    "                    + float(config[\"losses\"][\"host_functional_diversity\"]) * div\n",
     "                )\n",
-    "            opt.zero_grad(set_to_none=True)\n",
-    "            loss.backward()\n",
-    "            grad_norm = torch.nn.utils.clip_grad_norm_(\n",
-    "                [p for p in model.parameters() if p.requires_grad], 5.0\n",
-    "            )\n",
-    "            if not torch.isfinite(torch.as_tensor(grad_norm)):\n",
-    "                raise FloatingPointError(f\"Non-finite gradient norm at angle={angle}, batch={batch_id}\")\n",
-    "            opt.step()\n",
-    "\n",
-    "            n = y.numel()\n",
-    "            totals['samples'] += n\n",
-    "            totals['loss'] += float(loss.detach()) * n\n",
-    "            totals['ce'] += float(ce.detach()) * n\n",
-    "            totals['geo'] += float(geo.detach()) * n\n",
-    "            totals['diversity'] += float(div.detach()) * n\n",
+    "                if not torch.isfinite(torch.stack([ce, geo, div, loss])).all():\n",
+    "                    raise FloatingPointError(\n",
+    "                        f\"Non-finite loss in {method}, stage={stage}: \"\n",
+    "                        f\"ce={ce.item()}, geo={geo.item()}, div={div.item()}\"\n",
+    "                    )\n",
+    "\n",
+    "                optimizer.zero_grad(set_to_none=True)\n",
+    "                loss.backward()\n",
+    "                grad_norm = torch.nn.utils.clip_grad_norm_(\n",
+    "                    [p for p in model.parameters() if p.requires_grad], 5.0\n",
+    "                )\n",
+    "                if not torch.isfinite(torch.as_tensor(grad_norm)):\n",
+    "                    raise FloatingPointError(\"Non-finite gradient norm\")\n",
+    "                optimizer.step()\n",
+    "\n",
+    "                totals[\"samples\"] += sample_count\n",
+    "                totals[\"loss\"] += float(loss.detach()) * sample_count\n",
+    "                totals[\"ce\"] += float(ce.detach()) * sample_count\n",
+    "                totals[\"geo\"] += float(geo.detach()) * sample_count\n",
+    "                totals[\"div\"] += float(div.detach()) * sample_count\n",
+    "\n",
+    "        count = max(totals.pop(\"samples\"), 1)\n",
+    "        stage_row = {\n",
+    "            \"method\": method,\n",
+    "            \"stage\": stage,\n",
+    "            \"current_angle\": current_angle,\n",
+    "            \"seen_angles\": json.dumps(seen_angles),\n",
+    "            **{key: value / count for key, value in totals.items()},\n",
+    "        }\n",
+    "        stage_rows.append(stage_row)\n",
+    "        print(stage_row)\n",
+    "        evaluation_rows.extend(evaluate_model(model, all_eval_angles, stage, method))\n",
     "\n",
-    "    n = max(totals.pop('samples'), 1)\n",
-    "    return {'angle': angle, **{k: v/n for k, v in totals.items()}}\n"
+    "    return model, pd.DataFrame(stage_rows), pd.DataFrame(evaluation_rows)"
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "73a475d5",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "models = {}\n",
+    "stage_tables = []\n",
+    "evaluation_tables = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    print(\"\\n=== TRAINING\", method, \"===\")\n",
+    "    model, stage_df, evaluation_df = train_method(method)\n",
+    "    models[method] = model\n",
+    "    stage_tables.append(stage_df)\n",
+    "    evaluation_tables.append(evaluation_df)\n",
+    "\n",
+    "stage_df = pd.concat(stage_tables, ignore_index=True)\n",
+    "evaluation_df = pd.concat(evaluation_tables, ignore_index=True)\n",
+    "stage_df"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "2d39a3dc",
-   "metadata": {
-    "id": "2d39a3dc"
-   },
+   "id": "a9bcb97b",
+   "metadata": {},
    "source": [
-    "## 4. Continual sequence\n",
+    "## 5. Staged accuracy and forgetting\n",
     "\n",
-    "For qualification, add hardened EWC, replay, sparse-MoE, oracle-angle diagnostic and joint upper-bound comparisons with equal validation budgets."
+    "Forgetting is computed only on trained angles. Held-out angles are evaluated for\n",
+    "interpolation and extrapolation but are never considered learned tasks."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "712c3faa",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "712c3faa",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385963319,
-     "user_tz": 300,
-     "elapsed": 8434,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "6fae5e44-52a0-46ab-9486-9eff9b74d425"
-   },
+   "id": "632e380a",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "stage_logs, checkpoints = [], {}\n",
-    "stage_epochs = int(config['training']['stage_epochs']) if RUN_FULL else 2\n",
-    "for angle in train_angles:\n",
-    "    row = train_stage(angle, stage_epochs)\n",
-    "    stage_logs.append(row)\n",
-    "    checkpoints[angle] = copy.deepcopy(model.state_dict())\n",
-    "    print(row)\n",
-    "stage_logs\n"
+    "def forgetting_table(evaluation):\n",
+    "    rows = []\n",
+    "    final_stage = int(evaluation.stage.max())\n",
+    "    for method in evaluation.method.unique():\n",
+    "        sub = evaluation[\n",
+    "            (evaluation.method == method)\n",
+    "            & (evaluation.angle_type == \"train\")\n",
+    "        ]\n",
+    "        for angle in train_angles:\n",
+    "            angle_rows = sub[sub.angle == angle].sort_values(\"stage\")\n",
+    "            seen_stage = train_angles.index(angle)\n",
+    "            angle_rows = angle_rows[angle_rows.stage >= seen_stage]\n",
+    "            best = float(angle_rows.accuracy.max())\n",
+    "            final = float(angle_rows[angle_rows.stage == final_stage].accuracy.iloc[0])\n",
+    "            rows.append({\n",
+    "                \"method\": method,\n",
+    "                \"angle\": angle,\n",
+    "                \"best_accuracy\": best,\n",
+    "                \"final_accuracy\": final,\n",
+    "                \"forgetting\": best - final,\n",
+    "            })\n",
+    "    return pd.DataFrame(rows)\n",
+    "\n",
+    "forgetting_df = forgetting_table(evaluation_df)\n",
+    "forgetting_df.groupby(\"method\").forgetting.mean()"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "cfebdc12",
-   "metadata": {
-    "id": "cfebdc12"
-   },
+   "id": "e1772809",
+   "metadata": {},
    "source": [
-    "## 5. Trace collection and geometry evidence"
+    "## 6. Same-source paired trace collection\n",
+    "\n",
+    "Every row retains `source_index`. Primary geometry scores are computed within\n",
+    "each source block, then bootstrapped across source images."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "7b5122dc",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "7b5122dc",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385966566,
-     "user_tz": 300,
-     "elapsed": 3255,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "db495443-b8d6-4ab0-8395-be72f3c77ef3"
-   },
+   "id": "4448e068",
+   "metadata": {},
    "outputs": [],
    "source": [
     "@torch.no_grad()\n",
-    "def collect(loaders, max_batches=3):\n",
-    "    model.eval(); rows=[]\n",
-    "    for angle, dl in loaders.items():\n",
-    "        for b, (x, y, u, idx) in enumerate(dl):\n",
-    "            if max_batches is not None and b >= max_batches:\n",
-    "                break\n",
-    "            tr = model(x.to(DEVICE))\n",
-    "            assert_finite_trace(tr, f\"collect angle={angle}, batch={b}\")\n",
-    "            for i in range(len(y)):\n",
-    "                rows.append(dict(\n",
-    "                    angle=float(u[i]),\n",
-    "                    label=int(y[i]),\n",
-    "                    prediction=int(tr.logits[i].argmax()),\n",
-    "                    z0=tr.z0[i].cpu().numpy(),\n",
-    "                    context=tr.context[i].cpu().numpy(),\n",
-    "                    route=tr.route[i].cpu().numpy(),\n",
-    "                    z_mm=tr.z_mm[i].cpu().numpy(),\n",
-    "                    hosts=tr.host_outputs[i].cpu().numpy(),\n",
-    "                ))\n",
+    "def collect_paired_trace(model, method, angles, source_indices):\n",
+    "    model.eval()\n",
+    "    rows = []\n",
+    "    loader = multi_loader(angles, False, source_indices, False)\n",
+    "    for views, labels, factors, source_ids in loader:\n",
+    "        batch_size, angle_count = views.shape[:2]\n",
+    "        flat = views.reshape(-1, *views.shape[2:]).to(DEVICE)\n",
+    "        trace = model(flat)\n",
+    "        assert_finite_trace(trace, f\"paired trace {method}\")\n",
+    "\n",
+    "        z0 = trace.z0.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        context = trace.context.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        route = trace.route.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        z_mm = trace.z_mm.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        logits = trace.logits.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        hosts = trace.host_outputs.reshape(\n",
+    "            batch_size, angle_count, trace.host_outputs.shape[1], -1\n",
+    "        ).cpu().numpy()\n",
+    "\n",
+    "        for b in range(batch_size):\n",
+    "            for a in range(angle_count):\n",
+    "                rows.append({\n",
+    "                    \"method\": method,\n",
+    "                    \"source_index\": int(source_ids[b]),\n",
+    "                    \"label\": int(labels[b]),\n",
+    "                    \"angle\": float(factors[b, a]),\n",
+    "                    \"prediction\": int(np.argmax(logits[b, a])),\n",
+    "                    \"z0\": z0[b, a],\n",
+    "                    \"context\": context[b, a],\n",
+    "                    \"route\": route[b, a],\n",
+    "                    \"z_mm\": z_mm[b, a],\n",
+    "                    \"hosts\": hosts[b, a],\n",
+    "                })\n",
     "    return pd.DataFrame(rows)\n",
     "\n",
-    "trace = collect({**test_loaders, **interp_loaders}, None if RUN_FULL else 3)\n",
-    "assert len(trace) > 0\n",
-    "print(\"trace rows:\", len(trace))\n"
+    "trace_tables = []\n",
+    "for method, model in models.items():\n",
+    "    trace_tables.append(\n",
+    "        collect_paired_trace(model, method, all_eval_angles, test_indices)\n",
+    "    )\n",
+    "trace_df = pd.concat(trace_tables, ignore_index=True)\n",
+    "print(\"paired trace rows:\", len(trace_df))"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "a8319242",
+   "metadata": {},
+   "source": [
+    "## 7. Source-block and centroid geometry\n",
+    "\n",
+    "Primary uncertainty is block-bootstrap over source images. Factor-centroid\n",
+    "geometry is reported as a complementary tie-free view. No global all-pairs\n",
+    "p-value is used as evidence."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "fc9649ab",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/",
-     "height": 175
-    },
-    "id": "fc9649ab",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385979201,
-     "user_tz": 300,
-     "elapsed": 12627,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "91049af2-996b-41d7-bbe9-edd57877d029"
-   },
-   "outputs": [],
-   "source": [
-    "stack = lambda name: np.stack(trace[name].to_numpy())\n",
-    "for name in ['z0', 'context', 'route', 'z_mm']:\n",
-    "    assert np.isfinite(stack(name)).all(), f\"Non-finite values in trace space: {name}\"\n",
-    "\n",
-    "du = pairwise_factor_distance(trace.angle.to_numpy())\n",
-    "spaces = {\n",
-    "    'sensory': euclidean_distance_matrix(stack('z0')),\n",
-    "    'context': euclidean_distance_matrix(stack('context')),\n",
-    "    'route': pairwise_fisher_rao(stack('route')),\n",
-    "    'synthesis': euclidean_distance_matrix(stack('z_mm')),\n",
-    "}\n",
-    "rows = []\n",
-    "for name, d in spaces.items():\n",
-    "    assert np.isfinite(d).all(), f\"Non-finite distance matrix: {name}\"\n",
-    "    rho, p = distance_order_correlation(du, d)\n",
-    "    rows.append(dict(\n",
-    "        space=name,\n",
-    "        rho=rho,\n",
-    "        p_value=p,\n",
-    "        stress=normalized_stress(du, d),\n",
-    "        knn=neighborhood_preservation(du, d, k=5),\n",
-    "        status='development_not_qualified',\n",
-    "    ))\n",
-    "geometry_df = pd.DataFrame(rows)\n",
-    "geometry_df\n"
+   "id": "cfb140f7",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def stack_column(frame, name):\n",
+    "    return np.stack(frame[name].to_numpy())\n",
+    "\n",
+    "geometry_rows = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    sub = trace_df[trace_df.method == method]\n",
+    "    factors = sub.angle.to_numpy(float)\n",
+    "    groups = sub.source_index.to_numpy()\n",
+    "\n",
+    "    spaces = {\n",
+    "        \"sensory\": (\"euclidean\", stack_column(sub, \"z0\")),\n",
+    "        \"context\": (\"euclidean\", stack_column(sub, \"context\")),\n",
+    "        \"route\": (\"fisher_rao\", stack_column(sub, \"route\")),\n",
+    "        \"synthesis\": (\"euclidean\", stack_column(sub, \"z_mm\")),\n",
+    "    }\n",
+    "\n",
+    "    for space, (metric, reps) in spaces.items():\n",
+    "        grouped = grouped_geometry_scores(\n",
+    "            factors,\n",
+    "            reps,\n",
+    "            groups,\n",
+    "            metric=metric,\n",
+    "        )\n",
+    "        rho_mean, rho_low, rho_high = bootstrap_mean_ci(\n",
+    "            grouped[\"rho\"],\n",
+    "            samples=BOOTSTRAP_SAMPLES,\n",
+    "            seed=SEED,\n",
+    "        )\n",
+    "        stress_mean, stress_low, stress_high = bootstrap_mean_ci(\n",
+    "            grouped[\"stress\"],\n",
+    "            samples=BOOTSTRAP_SAMPLES,\n",
+    "            seed=SEED + 1,\n",
+    "        )\n",
+    "        centroid = centroid_geometry_scores(\n",
+    "            factors,\n",
+    "            reps,\n",
+    "            metric=metric,\n",
+    "        )\n",
+    "        geometry_rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"space\": space,\n",
+    "            \"source_rho_mean\": rho_mean,\n",
+    "            \"source_rho_ci_low\": rho_low,\n",
+    "            \"source_rho_ci_high\": rho_high,\n",
+    "            \"source_stress_mean\": stress_mean,\n",
+    "            \"source_stress_ci_low\": stress_low,\n",
+    "            \"source_stress_ci_high\": stress_high,\n",
+    "            \"centroid_rho\": centroid[\"rho\"],\n",
+    "            \"centroid_stress\": centroid[\"stress\"],\n",
+    "            \"source_blocks\": len(grouped[\"rho\"]),\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "\n",
+    "geometry_df = pd.DataFrame(geometry_rows)\n",
+    "geometry_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "6ffa3d0e",
+   "metadata": {},
+   "source": [
+    "## 8. Held-out interpolation controls\n",
+    "\n",
+    "The model is evaluated on held-out angles for accuracy and NLL. Context\n",
+    "centroids are compared with linear interpolation between neighboring trained\n",
+    "centroids. Route centroids are interpolated in square-root simplex coordinates\n",
+    "and compared with a nearest-trained-route control."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "ff6b2c7b",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def centroid_by_angle(frame, column):\n",
+    "    return {\n",
+    "        float(angle): np.stack(group[column].to_numpy()).mean(axis=0)\n",
+    "        for angle, group in frame.groupby(\"angle\")\n",
+    "    }\n",
+    "\n",
+    "def linear_neighbors(angle, trained):\n",
+    "    lower = max(value for value in trained if value < angle)\n",
+    "    upper = min(value for value in trained if value > angle)\n",
+    "    alpha = (angle - lower) / (upper - lower)\n",
+    "    return lower, upper, alpha\n",
+    "\n",
+    "interpolation_rows = []\n",
+    "final_stage = int(evaluation_df.stage.max())\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    final_eval = evaluation_df[\n",
+    "        (evaluation_df.method == method)\n",
+    "        & (evaluation_df.stage == final_stage)\n",
+    "        & (evaluation_df.angle_type == \"interpolation\")\n",
+    "    ]\n",
+    "    sub = trace_df[trace_df.method == method]\n",
+    "    context_centroids = centroid_by_angle(sub, \"context\")\n",
+    "    route_centroids = centroid_by_angle(sub, \"route\")\n",
+    "\n",
+    "    for row in final_eval.itertuples():\n",
+    "        angle = float(row.angle)\n",
+    "        lower, upper, alpha = linear_neighbors(angle, train_angles)\n",
+    "\n",
+    "        c_pred = (\n",
+    "            (1.0 - alpha) * context_centroids[lower]\n",
+    "            + alpha * context_centroids[upper]\n",
+    "        )\n",
+    "        context_error = float(np.linalg.norm(context_centroids[angle] - c_pred))\n",
+    "\n",
+    "        p_low = route_centroids[lower]\n",
+    "        p_high = route_centroids[upper]\n",
+    "        root_pred = (\n",
+    "            (1.0 - alpha) * np.sqrt(np.clip(p_low, 1e-12, None))\n",
+    "            + alpha * np.sqrt(np.clip(p_high, 1e-12, None))\n",
+    "        )\n",
+    "        p_pred = np.square(root_pred)\n",
+    "        p_pred = p_pred / p_pred.sum()\n",
+    "\n",
+    "        actual = route_centroids[angle]\n",
+    "        route_interp_error = fisher_rao_distance(actual, p_pred)\n",
+    "        nearest_error = min(\n",
+    "            fisher_rao_distance(actual, p_low),\n",
+    "            fisher_rao_distance(actual, p_high),\n",
+    "        )\n",
+    "\n",
+    "        interpolation_rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"angle\": angle,\n",
+    "            \"accuracy\": float(row.accuracy),\n",
+    "            \"nll\": float(row.nll),\n",
+    "            \"context_interpolation_error\": context_error,\n",
+    "            \"route_interpolation_error\": route_interp_error,\n",
+    "            \"nearest_route_error\": nearest_error,\n",
+    "            \"route_interpolation_beats_nearest\": route_interp_error < nearest_error,\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "\n",
+    "interpolation_df = pd.DataFrame(interpolation_rows)\n",
+    "interpolation_df"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "a5bd6ff5",
-   "metadata": {
-    "id": "a5bd6ff5"
-   },
-   "source": [
-    "## 6. Host ablation evidence\n",
-    "\n",
-    "A host is not specialized merely because it receives route mass. Measure the loss of true-class evidence when it is removed and the remaining route is renormalized."
+   "id": "1bbf8d0f",
+   "metadata": {},
+   "source": [
+    "## 9. Host ablation bundle\n",
+    "\n",
+    "Ablation is summarized by mean, median and positive-contribution fraction.\n",
+    "Route mass alone is not interpreted as specialization."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "80559935",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/",
-     "height": 238
-    },
-    "id": "80559935",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781385980211,
-     "user_tz": 300,
-     "elapsed": 995,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "e1a878fc-f8ab-48c7-fbf1-3e600745b68f"
-   },
+   "id": "666da235",
+   "metadata": {},
    "outputs": [],
    "source": [
     "@torch.no_grad()\n",
-    "def ablations(loaders, max_batches=2):\n",
-    "    model.eval(); rows=[]\n",
-    "    for angle, dl in loaders.items():\n",
-    "        for b, (x, y, _, _) in enumerate(dl):\n",
-    "            if b >= max_batches:\n",
-    "                break\n",
+    "def host_ablation_table(model, method, angles, source_indices):\n",
+    "    model.eval()\n",
+    "    rows = []\n",
+    "    for angle in angles:\n",
+    "        loader = fixed_loader(angle, False, source_indices, False)\n",
+    "        for x, y, _, source_id in loader:\n",
     "            x, y = x.to(DEVICE), y.to(DEVICE)\n",
-    "            tr = model(x)\n",
-    "            assert_finite_trace(tr, f\"ablation angle={angle}, batch={b}\")\n",
-    "            base = F.log_softmax(tr.logits, -1).gather(1, y[:, None]).squeeze(1)\n",
-    "            for h in range(tr.route.shape[1]):\n",
-    "                r = tr.route.clone()\n",
-    "                r[:, h] = 0\n",
-    "                r = r / r.sum(1, keepdim=True).clamp_min(1e-8)\n",
-    "                z = torch.einsum('bh,bhd->bd', r, tr.host_outputs)\n",
-    "                out = model.classifier(model.synthesis_norm(z))\n",
-    "                impact = base - F.log_softmax(out, -1).gather(1, y[:, None]).squeeze(1)\n",
-    "                if not torch.isfinite(impact).all():\n",
-    "                    raise FloatingPointError(f\"Non-finite ablation impact: angle={angle}, host={h}\")\n",
-    "                rows += [\n",
-    "                    dict(angle=angle, host=h, ablation_impact=float(v), status='development_not_qualified')\n",
-    "                    for v in impact.cpu()\n",
-    "                ]\n",
-    "    return pd.DataFrame(rows)\n",
+    "            trace = model(x)\n",
+    "            base = F.log_softmax(trace.logits, -1).gather(\n",
+    "                1, y[:, None]\n",
+    "            ).squeeze(1)\n",
+    "            for host in range(trace.route.shape[1]):\n",
+    "                route = trace.route.clone()\n",
+    "                route[:, host] = 0.0\n",
+    "                route = route / route.sum(1, keepdim=True).clamp_min(1e-8)\n",
+    "                z = torch.einsum(\"bh,bhd->bd\", route, trace.host_outputs)\n",
+    "                logits = model.classifier(model.synthesis_norm(z))\n",
+    "                ablated = F.log_softmax(logits, -1).gather(\n",
+    "                    1, y[:, None]\n",
+    "                ).squeeze(1)\n",
+    "                impact = (base - ablated).detach().cpu().numpy()\n",
+    "                for idx, value in enumerate(impact):\n",
+    "                    rows.append({\n",
+    "                        \"method\": method,\n",
+    "                        \"angle\": angle,\n",
+    "                        \"source_index\": int(source_id[idx]),\n",
+    "                        \"host\": host,\n",
+    "                        \"ablation_impact\": float(value),\n",
+    "                    })\n",
+    "    raw = pd.DataFrame(rows)\n",
+    "    summary = (\n",
+    "        raw.groupby([\"method\", \"angle\", \"host\"])\n",
+    "        .ablation_impact\n",
+    "        .agg(\n",
+    "            mean=\"mean\",\n",
+    "            median=\"median\",\n",
+    "            positive_fraction=lambda values: float(np.mean(values > 0)),\n",
+    "            count=\"count\",\n",
+    "        )\n",
+    "        .reset_index()\n",
+    "    )\n",
+    "    return raw, summary\n",
+    "\n",
+    "ablation_raw_tables = []\n",
+    "ablation_summary_tables = []\n",
+    "for method, model in models.items():\n",
+    "    raw, summary = host_ablation_table(\n",
+    "        model,\n",
+    "        method,\n",
+    "        train_angles + interp_angles,\n",
+    "        test_indices,\n",
+    "    )\n",
+    "    ablation_raw_tables.append(raw)\n",
+    "    ablation_summary_tables.append(summary)\n",
     "\n",
-    "ablation_df = ablations(test_loaders)\n",
-    "ablation_df.groupby(['angle', 'host']).ablation_impact.mean().unstack()\n"
+    "ablation_raw_df = pd.concat(ablation_raw_tables, ignore_index=True)\n",
+    "ablation_summary_df = pd.concat(ablation_summary_tables, ignore_index=True)\n",
+    "ablation_summary_df.head()"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "08e65a55",
-   "metadata": {
-    "id": "08e65a55"
-   },
+   "id": "527ca86f",
+   "metadata": {},
    "source": [
-    "## 7. Minimal causal tangent probe\n",
+    "## 10. Signed causal route-direction probe\n",
     "\n",
-    "The qualified experiment must add matched-norm orthogonal controls, bootstrap confidence intervals and identity-preservation gates."
+    "The probe estimates a context direction associated with increasing angle and a\n",
+    "route direction from route centroids. It reports a **signed** projection of the\n",
+    "route change and compares it with matched-norm context directions orthogonal to\n",
+    "the angle tangent.\n",
+    "\n",
+    "This remains development evidence. Qualification requires bootstrap confidence\n",
+    "intervals, class-identity gates and replication across seeds."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "a98270eb",
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/",
-     "height": 356
-    },
-    "id": "a98270eb",
-    "executionInfo": {
-     "status": "error",
-     "timestamp": 1781385980401,
-     "user_tz": 300,
-     "elapsed": 185,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "b2157059-f04d-4110-e6f6-79ee0186b66e"
-   },
+   "id": "ac786437",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "trained = trace[trace.angle.isin(train_angles)]\n",
-    "Cmat = np.stack(trained.context).astype(np.float64)\n",
-    "y = trained.angle.to_numpy(float)\n",
-    "assert np.isfinite(Cmat).all() and np.isfinite(y).all()\n",
-    "\n",
-    "X = Cmat - Cmat.mean(0, keepdims=True)\n",
-    "y0 = y - y.mean()\n",
-    "ridge = 1e-6 * max(np.trace(X.T @ X) / max(X.shape[1], 1), 1.0)\n",
-    "tangent = np.linalg.solve(X.T @ X + ridge*np.eye(X.shape[1]), X.T @ y0)\n",
-    "tangent_norm = np.linalg.norm(tangent)\n",
-    "if not np.isfinite(tangent_norm) or tangent_norm < 1e-12:\n",
-    "    raise FloatingPointError(\"Causal tangent is undefined or degenerate\")\n",
-    "tangent /= tangent_norm\n",
+    "def orthogonal_directions(tangent, count, seed):\n",
+    "    rng = np.random.default_rng(seed)\n",
+    "    directions = []\n",
+    "    for _ in range(count):\n",
+    "        vector = rng.normal(size=tangent.shape)\n",
+    "        vector = vector - np.dot(vector, tangent) * tangent\n",
+    "        norm = np.linalg.norm(vector)\n",
+    "        if norm > 1e-12:\n",
+    "            directions.append(vector / norm)\n",
+    "    return directions\n",
     "\n",
     "@torch.no_grad()\n",
-    "def reroute(z0, c):\n",
-    "    return torch.softmax(model.router(torch.cat([z0, c], -1)), -1)\n",
+    "def causal_probe(model, method, trace, probe_angle=15.0, scales=(-2, -1, 0, 1, 2)):\n",
+    "    trained = trace[trace.angle.isin(train_angles)]\n",
+    "    contexts = stack_column(trained, \"context\").astype(np.float64)\n",
+    "    angles = trained.angle.to_numpy(float)\n",
+    "\n",
+    "    x = contexts - contexts.mean(0, keepdims=True)\n",
+    "    y = angles - angles.mean()\n",
+    "    ridge = 1e-6 * max(np.trace(x.T @ x) / max(x.shape[1], 1), 1.0)\n",
+    "    tangent = np.linalg.solve(\n",
+    "        x.T @ x + ridge * np.eye(x.shape[1]),\n",
+    "        x.T @ y,\n",
+    "    )\n",
+    "    tangent = tangent / max(np.linalg.norm(tangent), 1e-12)\n",
     "\n",
-    "x = next(iter(interp_loaders[15.0]))[0].to(DEVICE)\n",
-    "tr = model(x)\n",
-    "assert_finite_trace(tr, \"causal probe\")\n",
-    "t = torch.tensor(tangent, dtype=tr.context.dtype, device=DEVICE)\n",
-    "causal_probe_df = pd.DataFrame([\n",
-    "    {\n",
-    "        'scale': s,\n",
-    "        'route_shift': float(torch.linalg.vector_norm(\n",
-    "            reroute(tr.z0, tr.context + s*t) - tr.route,\n",
-    "            dim=1,\n",
-    "        ).mean()),\n",
-    "        'status': 'development_not_qualified',\n",
-    "    }\n",
-    "    for s in [-2, -1, 0, 1, 2]\n",
-    "])\n",
-    "causal_probe_df\n"
+    "    route_centroids = centroid_by_angle(trained, \"route\")\n",
+    "    route_matrix = np.stack([\n",
+    "        np.sqrt(np.clip(route_centroids[angle], 1e-12, None))\n",
+    "        for angle in train_angles\n",
+    "    ])\n",
+    "    centered_angles = np.asarray(train_angles) - np.mean(train_angles)\n",
+    "    route_centered = route_matrix - route_matrix.mean(0, keepdims=True)\n",
+    "    route_direction = (\n",
+    "        centered_angles[:, None] * route_centered\n",
+    "    ).sum(axis=0) / max(np.sum(centered_angles ** 2), 1e-12)\n",
+    "    route_direction = route_direction / max(np.linalg.norm(route_direction), 1e-12)\n",
+    "\n",
+    "    orthogonals = orthogonal_directions(tangent, count=8, seed=SEED + 9)\n",
+    "    loader = fixed_loader(probe_angle, False, test_indices, False)\n",
+    "    x_batch, y_batch, _, _ = next(iter(loader))\n",
+    "    x_batch, y_batch = x_batch.to(DEVICE), y_batch.to(DEVICE)\n",
+    "    base = model(x_batch)\n",
+    "    base_logp = F.log_softmax(base.logits, -1).gather(1, y_batch[:, None]).squeeze(1)\n",
+    "\n",
+    "    tangent_tensor = torch.tensor(tangent, dtype=base.context.dtype, device=DEVICE)\n",
+    "    route_dir_tensor = torch.tensor(\n",
+    "        route_direction, dtype=base.route.dtype, device=DEVICE\n",
+    "    )\n",
+    "\n",
+    "    rows = []\n",
+    "    for scale in scales:\n",
+    "        new_context = base.context + float(scale) * tangent_tensor\n",
+    "        new_route = torch.softmax(\n",
+    "            model.router(torch.cat([base.z0, new_context], dim=-1)),\n",
+    "            dim=-1,\n",
+    "        )\n",
+    "        delta_root = torch.sqrt(new_route.clamp_min(1e-12)) - torch.sqrt(\n",
+    "            base.route.clamp_min(1e-12)\n",
+    "        )\n",
+    "        signed_effect = float(\n",
+    "            (delta_root * route_dir_tensor).sum(dim=1).mean().detach().cpu()\n",
+    "        )\n",
+    "\n",
+    "        z = torch.einsum(\"bh,bhd->bd\", new_route, base.host_outputs)\n",
+    "        logits = model.classifier(model.synthesis_norm(z))\n",
+    "        new_logp = F.log_softmax(logits, -1).gather(1, y_batch[:, None]).squeeze(1)\n",
+    "        identity_drop = float((base_logp - new_logp).mean().detach().cpu())\n",
+    "\n",
+    "        orth_effects = []\n",
+    "        for direction in orthogonals:\n",
+    "            direction_tensor = torch.tensor(\n",
+    "                direction, dtype=base.context.dtype, device=DEVICE\n",
+    "            )\n",
+    "            c_orth = base.context + float(scale) * direction_tensor\n",
+    "            r_orth = torch.softmax(\n",
+    "                model.router(torch.cat([base.z0, c_orth], dim=-1)),\n",
+    "                dim=-1,\n",
+    "            )\n",
+    "            delta_orth = torch.sqrt(r_orth.clamp_min(1e-12)) - torch.sqrt(\n",
+    "                base.route.clamp_min(1e-12)\n",
+    "            )\n",
+    "            orth_effects.append(\n",
+    "                float(\n",
+    "                    torch.abs(\n",
+    "                        (delta_orth * route_dir_tensor).sum(dim=1)\n",
+    "                    ).mean().detach().cpu()\n",
+    "                )\n",
+    "            )\n",
+    "\n",
+    "        orth_mean = float(np.mean(orth_effects)) if orth_effects else float(\"nan\")\n",
+    "        csr = abs(signed_effect) / max(orth_mean, 1e-12) if scale != 0 else 0.0\n",
+    "        rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"probe_angle\": probe_angle,\n",
+    "            \"scale\": scale,\n",
+    "            \"signed_route_effect\": signed_effect,\n",
+    "            \"orthogonal_abs_effect_mean\": orth_mean,\n",
+    "            \"causal_specificity_ratio\": csr,\n",
+    "            \"class_log_prob_drop\": identity_drop,\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "    return pd.DataFrame(rows)\n",
+    "\n",
+    "causal_tables = []\n",
+    "for method, model in models.items():\n",
+    "    causal_tables.append(\n",
+    "        causal_probe(\n",
+    "            model,\n",
+    "            method,\n",
+    "            trace_df[trace_df.method == method],\n",
+    "        )\n",
+    "    )\n",
+    "causal_df = pd.concat(causal_tables, ignore_index=True)\n",
+    "causal_df"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "968d7c03",
-   "metadata": {
-    "id": "968d7c03"
-   },
+   "id": "f83a28c6",
+   "metadata": {},
    "source": [
-    "## 8. Export with epistemic status"
+    "## 11. Development gate summary\n",
+    "\n",
+    "The notebook computes measurements needed for C1-C4, but it does not\n",
+    "automatically convert a development run into a claim. A gate may be marked\n",
+    "`candidate_pass` only after frozen thresholds, multi-seed aggregation and all\n",
+    "required controls are present."
    ]
   },
   {
    "cell_type": "code",
    "execution_count": null,
-   "id": "e018523d",
-   "metadata": {
-    "id": "e018523d",
-    "executionInfo": {
-     "status": "aborted",
-     "timestamp": 1781385980438,
-     "user_tz": 300,
-     "elapsed": 83497,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    }
-   },
+   "id": "3ae29bb8",
+   "metadata": {},
    "outputs": [],
    "source": [
-    "out = Path('results/per_seed/dev_seed_0')\n",
-    "out.mkdir(parents=True, exist_ok=True)\n",
-    "geometry_df.to_csv(out/'geometry_metrics.csv', index=False)\n",
-    "ablation_df.to_csv(out/'host_ablation.csv', index=False)\n",
-    "causal_probe_df.to_csv(out/'causal_probe.csv', index=False)\n",
-    "pd.DataFrame(stage_logs).to_csv(out/'stage_logs.csv', index=False)\n",
-    "pd.DataFrame(sensory_history).to_csv(out/'sensory_history.csv', index=False)\n",
-    "(out/'run_manifest.json').write_text(json.dumps({\n",
-    "    'status': 'development_not_qualified',\n",
-    "    'notebook_version': '1.0.2',\n",
-    "    'seed': SEED,\n",
-    "    'run_full': RUN_FULL,\n",
-    "    'device': str(DEVICE),\n",
-    "    'timestamp': time.time(),\n",
-    "    'warning': 'Not a qualified G1 result.',\n",
-    "}, indent=2))\n",
-    "print(out.resolve())\n"
+    "gate_rows = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    route_row = geometry_df[\n",
+    "        (geometry_df.method == method) & (geometry_df.space == \"route\")\n",
+    "    ].iloc[0]\n",
+    "    interp = interpolation_df[interpolation_df.method == method]\n",
+    "    forgetting = forgetting_df[forgetting_df.method == method]\n",
+    "\n",
+    "    gate_rows.append({\n",
+    "        \"method\": method,\n",
+    "        \"C1_route_source_rho\": route_row.source_rho_mean,\n",
+    "        \"C1_route_rho_ci_low\": route_row.source_rho_ci_low,\n",
+    "        \"C1_route_centroid_rho\": route_row.centroid_rho,\n",
+    "        \"C2_mean_interpolation_accuracy\": interp.accuracy.mean(),\n",
+    "        \"C2_route_interp_win_fraction\": interp.route_interpolation_beats_nearest.mean(),\n",
+    "        \"mean_trained_angle_forgetting\": forgetting.forgetting.mean(),\n",
+    "        \"qualification_status\": \"not_qualified\",\n",
+    "    })\n",
+    "\n",
+    "gate_summary_df = pd.DataFrame(gate_rows)\n",
+    "gate_summary_df"
    ]
   },
   {
    "cell_type": "markdown",
-   "id": "99337a0b",
-   "metadata": {
-    "id": "99337a0b"
-   },
+   "id": "d24cb3e3",
+   "metadata": {},
    "source": [
-    "## 9. Before publication and optional PDF export\n",
-    "\n",
-    "Implement transport memory, dual-memory qualification, cross-seed host-role matching, compute accounting, confidence intervals, baseline hardening and secondary-dataset replication. Follow `docs/CLAIMS_AND_GATES.md`.\n",
+    "## 12. Export and immutable manifest\n",
     "\n",
-    "The cells below are optional. Save the notebook to Drive or upload it to `/content` before running the PDF export.\n"
+    "All exported tables retain epistemic status. The manifest records the package\n",
+    "version, git SHA, split checksums, compared methods and notebook history."
    ]
   },
   {
    "cell_type": "code",
-   "source": [
-    "# Optional Drive mount. Skip when the notebook already exists under /content.\n",
-    "try:\n",
-    "    from google.colab import drive\n",
-    "    drive.mount('/content/drive')\n",
-    "except Exception as exc:\n",
-    "    print(\"Drive mount skipped:\", exc)\n"
-   ],
-   "metadata": {
-    "id": "G2fyKbQy-e8n"
-   },
-   "id": "G2fyKbQy-e8n",
    "execution_count": null,
-   "outputs": []
+   "id": "64a24fcc",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "output_root = Path(\"results/v1_0_3\") / f\"seed_{SEED}\"\n",
+    "output_root.mkdir(parents=True, exist_ok=True)\n",
+    "\n",
+    "stage_df.to_csv(output_root / \"stage_logs.csv\", index=False)\n",
+    "evaluation_df.to_csv(output_root / \"staged_evaluation.csv\", index=False)\n",
+    "forgetting_df.to_csv(output_root / \"forgetting.csv\", index=False)\n",
+    "geometry_df.to_csv(output_root / \"paired_geometry_metrics.csv\", index=False)\n",
+    "interpolation_df.to_csv(output_root / \"interpolation_metrics.csv\", index=False)\n",
+    "ablation_summary_df.to_csv(output_root / \"host_ablation_summary.csv\", index=False)\n",
+    "ablation_raw_df.to_csv(output_root / \"host_ablation_raw.csv\", index=False)\n",
+    "causal_df.to_csv(output_root / \"causal_probe.csv\", index=False)\n",
+    "gate_summary_df.to_csv(output_root / \"development_gate_summary.csv\", index=False)\n",
+    "pd.DataFrame(sensory_history).to_csv(output_root / \"sensory_history.csv\", index=False)\n",
+    "\n",
+    "run_manifest = {\n",
+    "    \"status\": \"development_not_qualified\",\n",
+    "    \"notebook_version\": \"1.0.3\",\n",
+    "    \"package_version\": package_version,\n",
+    "    \"git_sha\": git_sha,\n",
+    "    \"run_mode\": RUN_MODE,\n",
+    "    \"seed\": SEED,\n",
+    "    \"device\": str(DEVICE),\n",
+    "    \"methods\": METHODS,\n",
+    "    \"train_angles\": train_angles,\n",
+    "    \"interpolation_angles\": interp_angles,\n",
+    "    \"extrapolation_angles\": extra_angles,\n",
+    "    \"split_manifest\": split_manifest,\n",
+    "    \"tracked_changes\": [f\"CHG-103-{index:02d}\" for index in range(1, 11)],\n",
+    "    \"warning\": (\n",
+    "        \"This archive implements the corrected paired protocol. \"\n",
+    "        \"It is not a qualified C1-C6 result.\"\n",
+    "    ),\n",
+    "    \"timestamp\": time.time(),\n",
+    "}\n",
+    "(output_root / \"run_manifest.json\").write_text(\n",
+    "    json.dumps(run_manifest, indent=2),\n",
+    "    encoding=\"utf-8\",\n",
+    ")\n",
+    "print(\"Exported to:\", output_root.resolve())"
+   ]
   },
   {
-   "cell_type": "code",
+   "cell_type": "markdown",
+   "id": "3decc6cb",
+   "metadata": {},
    "source": [
-    "# Optional one-time LaTeX installation for nbconvert PDF export.\n",
-    "import shutil, subprocess, sys\n",
-    "if shutil.which(\"xelatex\") is None:\n",
-    "    subprocess.run(\n",
-    "        [\"apt-get\", \"update\"],\n",
-    "        check=True,\n",
-    "        stdout=subprocess.DEVNULL,\n",
-    "    )\n",
-    "    subprocess.run(\n",
-    "        [\"apt-get\", \"install\", \"-y\", \"texlive-xetex\", \"texlive-latex-extra\", \"pandoc\"],\n",
-    "        check=True,\n",
-    "    )\n",
-    "else:\n",
-    "    print(\"xelatex already installed:\", shutil.which(\"xelatex\"))\n"
-   ],
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "pqovNflx98W0",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781387575498,
-     "user_tz": 300,
-     "elapsed": 95378,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "e1f7d293-03df-4671-d6ea-fb9a523de41d"
-   },
-   "id": "pqovNflx98W0",
-   "execution_count": null,
-   "outputs": []
+    "## 13. Qualification checklist\n",
+    "\n",
+    "Before any C1-C6 claim:\n",
+    "\n",
+    "1. Freeze gates before qualification runs.\n",
+    "2. Run at least five seeds for pilot qualification and ten for final evidence.\n",
+    "3. Validate `no_geometry` and `paired_geometry` with equal budgets.\n",
+    "4. Add tuned EWC, replay, sparse-MoE, oracle-angle and joint upper-bound controls.\n",
+    "5. Report source-block confidence intervals and failed seeds.\n",
+    "6. Confirm interpolation angles never enter training or checkpoint selection.\n",
+    "7. Add role matching across seeds for host specialization.\n",
+    "8. Add memory-transport and dual-memory experiments before C5.\n",
+    "9. Replicate on a secondary controlled factor or dataset.\n",
+    "10. Archive notebook, CSVs, manifest, environment and commit SHA."
+   ]
   },
   {
-   "cell_type": "code",
+   "cell_type": "markdown",
+   "id": "85d78746",
+   "metadata": {},
    "source": [
-    "from pathlib import Path\n",
+    "## 14. Optional PDF export\n",
     "\n",
-    "patterns = [\n",
-    "    \"Geometry_MMALS_G1_Colab_v1_0_2*.ipynb\",\n",
-    "    \"Geometry_MMALS_G1_Colab_v1_0_1*.ipynb\",\n",
-    "]\n",
-    "candidates = []\n",
-    "for pattern in patterns:\n",
-    "    candidates.extend(Path('/content').glob(pattern))\n",
-    "    drive_root = Path('/content/drive/MyDrive')\n",
-    "    if drive_root.exists():\n",
-    "        candidates.extend(drive_root.rglob(pattern))\n",
-    "\n",
-    "# Deduplicate and prefer the newest file.\n",
-    "candidates = sorted({p.resolve() for p in candidates if p.is_file()}, key=lambda p: p.stat().st_mtime, reverse=True)\n",
-    "if not candidates:\n",
-    "    raise FileNotFoundError(\n",
-    "        \"Notebook file not found. Save a copy to Drive or upload the .ipynb to /content, then rerun this cell.\"\n",
-    "    )\n",
-    "notebook_path = candidates[0]\n",
-    "print(\"Notebook selected for export:\", notebook_path)\n"
-   ],
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "jeb5hbv6-ApC",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781387575565,
-     "user_tz": 300,
-     "elapsed": 75,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "36803f7f-1721-48ba-c181-2fb8feac567f"
-   },
-   "id": "jeb5hbv6-ApC",
-   "execution_count": null,
-   "outputs": []
+    "The GitHub archive contains a separate protocol correction report under\n",
+    "`docs/reports/`. Notebook PDF export is optional and should not replace the raw\n",
+    "`.ipynb`, CSV tables or manifest."
+   ]
   },
   {
    "cell_type": "code",
-   "source": [
-    "import subprocess, sys\n",
-    "from pathlib import Path\n",
-    "\n",
-    "output_dir = Path('/content/pdf_export')\n",
-    "output_dir.mkdir(parents=True, exist_ok=True)\n",
-    "cmd = [\n",
-    "    sys.executable, '-m', 'jupyter', 'nbconvert',\n",
-    "    '--to', 'pdf',\n",
-    "    str(notebook_path),\n",
-    "    '--output-dir', str(output_dir),\n",
-    "    '--PDFExporter.latex_command=xelatex',\n",
-    "    '--PDFExporter.latex_command={filename}',\n",
-    "    '--PDFExporter.latex_command=-interaction=nonstopmode',\n",
-    "    '--PDFExporter.latex_count=3',\n",
-    "]\n",
-    "print(' '.join(cmd))\n",
-    "subprocess.run(cmd, check=True)\n",
-    "print(\"PDF export directory:\", output_dir)\n"
-   ],
-   "metadata": {
-    "colab": {
-     "base_uri": "https://localhost:8080/"
-    },
-    "id": "DRLLBRtI-E1D",
-    "executionInfo": {
-     "status": "ok",
-     "timestamp": 1781387587843,
-     "user_tz": 300,
-     "elapsed": 12275,
-     "user": {
-      "displayName": "Guillaume Harbonnier",
-      "userId": "03965805495763048025"
-     }
-    },
-    "outputId": "abc30a9e-4c49-4279-b7a1-95077654969d"
-   },
-   "id": "DRLLBRtI-E1D",
    "execution_count": null,
-   "outputs": []
+   "id": "fba381b1",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "# Optional: save/upload this notebook first, then run.\n",
+    "# The command passes each list-valued latex argument separately.\n",
+    "#\n",
+    "# import subprocess, sys\n",
+    "# from pathlib import Path\n",
+    "#\n",
+    "# notebook_path = Path(\"/content/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb\")\n",
+    "# output_dir = Path(\"/content/pdf_export\")\n",
+    "# output_dir.mkdir(parents=True, exist_ok=True)\n",
+    "# subprocess.run([\n",
+    "#     sys.executable, \"-m\", \"jupyter\", \"nbconvert\",\n",
+    "#     \"--to\", \"pdf\",\n",
+    "#     str(notebook_path),\n",
+    "#     \"--output-dir\", str(output_dir),\n",
+    "#     \"--PDFExporter.latex_command=xelatex\",\n",
+    "#     \"--PDFExporter.latex_command={filename}\",\n",
+    "#     \"--PDFExporter.latex_command=-interaction=nonstopmode\",\n",
+    "#     \"--PDFExporter.latex_count=3\",\n",
+    "# ], check=True)"
+   ]
   }
  ],
  "metadata": {
   "colab": {
+   "name": "Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb",
    "provenance": []
   },
+  "geometry_mmalls": {
+   "status": "development_not_qualified",
+   "tracked_changes": [
+    "CHG-103-01",
+    "CHG-103-02",
+    "CHG-103-03",
+    "CHG-103-04",
+    "CHG-103-05",
+    "CHG-103-06",
+    "CHG-103-07",
+    "CHG-103-08",
+    "CHG-103-09",
+    "CHG-103-10"
+   ],
+   "version": "1.0.3"
+  },
   "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
@@ -974,4 +1268,4 @@
  },
  "nbformat": 4,
  "nbformat_minor": 5
-}
\ No newline at end of file
+}
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb /mnt/data/geometry-mmalls-g1-v103/notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb
--- /mnt/data/geometry-mmalls-g1-v102/notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb	1970-01-01 00:00:00.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb	2026-06-13 22:34:10.804720402 +0000
@@ -0,0 +1,1271 @@
+{
+ "cells": [
+  {
+   "cell_type": "markdown",
+   "id": "8a907534",
+   "metadata": {},
+   "source": [
+    "# Geometry-MMALS G1 v1.0.3\n",
+    "## Cross-Angle Paired Functional Geometry\n",
+    "\n",
+    "**Scientific status:** protocol implementation and development experiment.  \n",
+    "**Accepted claim:** C0 pipeline/protocol integrity only.  \n",
+    "**Not claimed:** C1-C6 qualification, quantum advantage, backward transfer, or domain-general geometry.\n",
+    "\n",
+    "This notebook corrects the main scientific limitation of v1.0.2: each geometry\n",
+    "batch previously contained one fixed angle, so the geometry loss never observed\n",
+    "two distinct context values. v1.0.3 groups multiple rotated views of the **same\n",
+    "source image**, making route-distance versus angle-distance a real trainable and\n",
+    "measurable relation."
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "802b2927",
+   "metadata": {},
+   "source": [
+    "## Research history and change tracking\n",
+    "\n",
+    "| Version | Question | Outcome |\n",
+    "|---|---|---|\n",
+    "| v1.0.0 | Can functional MMALS geometry be specified and falsified? | Article, protocol and C0 scaffold created. |\n",
+    "| v1.0.1 | Can release claims, gates, memory stubs and notation be audited? | C0-only status and pilot gates formalized. |\n",
+    "| v1.0.2 | Can the Fisher-Rao route loss and Colab pipeline run without NaNs? | Numerical stability passed; finite traces obtained. |\n",
+    "| **v1.0.3** | Does the optimization unit actually contain cross-angle evidence? | Same-source paired protocol introduced. |\n",
+    "\n",
+    "### Tracked changes\n",
+    "\n",
+    "- **CHG-103-01:** same-source multi-angle data primitive.\n",
+    "- **CHG-103-02:** paired square-root-simplex geometry loss.\n",
+    "- **CHG-103-03:** continual stages use only angles already seen.\n",
+    "- **CHG-103-04:** source index retained in every trace.\n",
+    "- **CHG-103-05:** source-block bootstrap and factor-centroid metrics.\n",
+    "- **CHG-103-06:** held-out interpolation accuracy, NLL and route/context interpolation.\n",
+    "- **CHG-103-07:** staged accuracy matrix and forgetting.\n",
+    "- **CHG-103-08:** signed tangent effect with matched orthogonal controls.\n",
+    "- **CHG-103-09:** package version and git SHA recorded in the manifest.\n",
+    "- **CHG-103-10:** explicit non-claims and qualification checklist."
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "3a5e636a",
+   "metadata": {},
+   "source": [
+    "## Why the v1.0.2 run was non-diagnostic\n",
+    "\n",
+    "The v1.0.2 training loop used one `FixedAngleMNIST` loader at a time. Inside a\n",
+    "batch, every factor value was identical:\n",
+    "\n",
+    "\\[\n",
+    "u_1=u_2=\\cdots=u_B.\n",
+    "\\]\n",
+    "\n",
+    "The route loss could enforce within-angle consistency, but it could not learn an\n",
+    "ordered relation among `-60, -30, 0, 30, 60` degrees. Global all-sample\n",
+    "pairwise metrics also mixed digit identity with rotation and produced\n",
+    "dependence-inflated p-values and tie-fragile kNN scores.\n",
+    "\n",
+    "v1.0.3 changes the optimization and measurement unit to:\n",
+    "\n",
+    "> one source image observed under several declared angles.\n",
+    "\n",
+    "This is a stronger test of geometry, while still remaining a supervised\n",
+    "grounded G1-A variant."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "8b75803d",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "import os\n",
+    "import sys\n",
+    "import shutil\n",
+    "import subprocess\n",
+    "import importlib\n",
+    "import importlib.metadata\n",
+    "from pathlib import Path\n",
+    "\n",
+    "REPO_URL = \"https://github.com/gharbonnier78/geometry-mmalls-g1.git\"\n",
+    "REPO_DIR = Path(\"/content/geometry-mmalls-g1\")\n",
+    "SRC_DIR = REPO_DIR / \"src\"\n",
+    "EXPECTED_VERSION = \"1.0.3\"\n",
+    "FORCE_REFRESH = True\n",
+    "STRICT_VERSION = True\n",
+    "\n",
+    "if FORCE_REFRESH and REPO_DIR.exists():\n",
+    "    shutil.rmtree(REPO_DIR)\n",
+    "\n",
+    "if not REPO_DIR.exists():\n",
+    "    subprocess.run(\n",
+    "        [\"git\", \"clone\", \"--depth\", \"1\", REPO_URL, str(REPO_DIR)],\n",
+    "        check=True,\n",
+    "    )\n",
+    "\n",
+    "os.chdir(REPO_DIR)\n",
+    "subprocess.run(\n",
+    "    [sys.executable, \"-m\", \"pip\", \"install\", \"--no-deps\", \"-e\", str(REPO_DIR)],\n",
+    "    check=True,\n",
+    ")\n",
+    "\n",
+    "src_path = str(SRC_DIR)\n",
+    "if src_path not in sys.path:\n",
+    "    sys.path.insert(0, src_path)\n",
+    "importlib.invalidate_caches()\n",
+    "\n",
+    "import geometry_mmalls\n",
+    "\n",
+    "package_version = importlib.metadata.version(\"geometry-mmalls-g1\")\n",
+    "git_sha = subprocess.check_output(\n",
+    "    [\"git\", \"rev-parse\", \"HEAD\"], cwd=REPO_DIR, text=True\n",
+    ").strip()\n",
+    "\n",
+    "print(\"Python:\", sys.executable)\n",
+    "print(\"Package:\", geometry_mmalls.__file__)\n",
+    "print(\"Package version:\", package_version)\n",
+    "print(\"Git SHA:\", git_sha)\n",
+    "\n",
+    "if package_version != EXPECTED_VERSION:\n",
+    "    message = (\n",
+    "        f\"Expected geometry-mmalls-g1 {EXPECTED_VERSION}, got {package_version}. \"\n",
+    "        \"Push the v1.0.3 package or install the supplied v1.0.3 ZIP before running.\"\n",
+    "    )\n",
+    "    if STRICT_VERSION:\n",
+    "        raise RuntimeError(message)\n",
+    "    print(\"WARNING:\", message)"
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "29b0450f",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "from pathlib import Path\n",
+    "import copy\n",
+    "import json\n",
+    "import math\n",
+    "import random\n",
+    "import time\n",
+    "\n",
+    "import numpy as np\n",
+    "import pandas as pd\n",
+    "import torch\n",
+    "import torch.nn.functional as F\n",
+    "import yaml\n",
+    "from torch.utils.data import DataLoader, Subset\n",
+    "from torchvision.datasets import MNIST\n",
+    "\n",
+    "from geometry_mmalls.data import FixedAngleMNIST, MultiAngleMNIST\n",
+    "from geometry_mmalls.geometry import (\n",
+    "    fisher_rao_distance,\n",
+    "    paired_route_geometry_loss,\n",
+    ")\n",
+    "from geometry_mmalls.metrics import (\n",
+    "    bootstrap_mean_ci,\n",
+    "    centroid_geometry_scores,\n",
+    "    grouped_geometry_scores,\n",
+    ")\n",
+    "from geometry_mmalls.model import GeometryMMALS, SmallConvEncoder\n",
+    "\n",
+    "config = yaml.safe_load(Path(\"configs/rotated_mnist_g1.yaml\").read_text())\n",
+    "\n",
+    "RUN_MODE = \"development\"  # \"development\" or \"qualification\"\n",
+    "SEED = 0\n",
+    "METHODS = [\"no_geometry\", \"paired_geometry\"]\n",
+    "DEVICE = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n",
+    "\n",
+    "random.seed(SEED)\n",
+    "np.random.seed(SEED)\n",
+    "torch.manual_seed(SEED)\n",
+    "if torch.cuda.is_available():\n",
+    "    torch.cuda.manual_seed_all(SEED)\n",
+    "\n",
+    "train_angles = list(map(float, config[\"data\"][\"train_angles\"]))\n",
+    "interp_angles = list(map(float, config[\"data\"][\"interpolation_angles\"]))\n",
+    "extra_angles = list(map(float, config[\"data\"][\"extrapolation_angles\"]))\n",
+    "all_eval_angles = train_angles + interp_angles + extra_angles\n",
+    "\n",
+    "if RUN_MODE == \"development\":\n",
+    "    TRAIN_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"development_source_limit\"])\n",
+    "    TEST_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"development_test_source_limit\"])\n",
+    "    SENSORY_EPOCHS = 2\n",
+    "    STAGE_EPOCHS = 2\n",
+    "    BOOTSTRAP_SAMPLES = 500\n",
+    "else:\n",
+    "    TRAIN_SOURCE_LIMIT = int(config[\"paired_protocol\"][\"full_source_limit\"])\n",
+    "    TEST_SOURCE_LIMIT = 2000\n",
+    "    SENSORY_EPOCHS = int(config[\"training\"][\"sensory_pretrain_epochs\"])\n",
+    "    STAGE_EPOCHS = int(config[\"training\"][\"stage_epochs\"])\n",
+    "    BOOTSTRAP_SAMPLES = int(config[\"metrics\"][\"bootstrap_samples\"])\n",
+    "\n",
+    "SOURCE_BATCH_SIZE = int(config[\"paired_protocol\"][\"source_batch_size\"])\n",
+    "print({\n",
+    "    \"run_mode\": RUN_MODE,\n",
+    "    \"device\": str(DEVICE),\n",
+    "    \"methods\": METHODS,\n",
+    "    \"train_source_limit\": TRAIN_SOURCE_LIMIT,\n",
+    "    \"test_source_limit\": TEST_SOURCE_LIMIT,\n",
+    "})"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "cd9af3db",
+   "metadata": {},
+   "source": [
+    "## 1. Numerical and structural self-test\n",
+    "\n",
+    "The training loss uses chordal distance in square-root simplex coordinates.\n",
+    "This is monotonic with Fisher-Rao distance but avoids the derivative singularity\n",
+    "of `arccos` during optimization. Fisher-Rao remains the evaluation distance."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "c4dcf34b",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "_probe_logits = torch.randn(8, 5, 4, requires_grad=True)\n",
+    "_probe_routes = torch.softmax(_probe_logits, dim=-1)\n",
+    "_probe_angles = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])\n",
+    "_probe_loss = paired_route_geometry_loss(_probe_routes, _probe_angles)\n",
+    "_probe_loss.backward()\n",
+    "\n",
+    "assert torch.isfinite(_probe_loss)\n",
+    "assert _probe_logits.grad is not None\n",
+    "assert torch.isfinite(_probe_logits.grad).all()\n",
+    "print(\"Paired route-geometry backward gate: PASS\", float(_probe_loss.detach()))"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "26694811",
+   "metadata": {},
+   "source": [
+    "## 2. Controlled source split\n",
+    "\n",
+    "The same source indices are used at every angle. Interpolation and extrapolation\n",
+    "angles are never included in training. The split is deterministic and recorded."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "c4235471",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "root = Path(config[\"data\"][\"root\"])\n",
+    "base_train = MNIST(root=str(root), train=True, download=True)\n",
+    "base_test = MNIST(root=str(root), train=False, download=True)\n",
+    "\n",
+    "rng = np.random.default_rng(SEED)\n",
+    "train_indices = rng.permutation(len(base_train))[:TRAIN_SOURCE_LIMIT].tolist()\n",
+    "test_indices = rng.permutation(len(base_test))[:TEST_SOURCE_LIMIT].tolist()\n",
+    "\n",
+    "def fixed_loader(angle, train, indices, shuffle):\n",
+    "    ds = FixedAngleMNIST(root, angle=angle, train=train, download=True)\n",
+    "    ds = Subset(ds, indices)\n",
+    "    return DataLoader(\n",
+    "        ds,\n",
+    "        batch_size=128,\n",
+    "        shuffle=shuffle,\n",
+    "        num_workers=0,\n",
+    "    )\n",
+    "\n",
+    "def multi_loader(angles, train, indices, shuffle):\n",
+    "    ds = MultiAngleMNIST(\n",
+    "        root,\n",
+    "        angles=angles,\n",
+    "        train=train,\n",
+    "        indices=indices,\n",
+    "        download=True,\n",
+    "    )\n",
+    "    return DataLoader(\n",
+    "        ds,\n",
+    "        batch_size=SOURCE_BATCH_SIZE,\n",
+    "        shuffle=shuffle,\n",
+    "        num_workers=0,\n",
+    "    )\n",
+    "\n",
+    "split_manifest = {\n",
+    "    \"seed\": SEED,\n",
+    "    \"train_source_count\": len(train_indices),\n",
+    "    \"test_source_count\": len(test_indices),\n",
+    "    \"train_index_checksum\": int(np.sum(train_indices)),\n",
+    "    \"test_index_checksum\": int(np.sum(test_indices)),\n",
+    "}\n",
+    "split_manifest"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "da478339",
+   "metadata": {},
+   "source": [
+    "## 3. Pretrain and freeze the sensory grove\n",
+    "\n",
+    "The frozen encoder is a control boundary. Geometry already present in `z0` is\n",
+    "reported alongside context, route and synthesis geometry."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "28aaac70",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "latent_dim = int(config[\"model\"][\"latent_dim\"])\n",
+    "encoder = SmallConvEncoder(latent_dim).to(DEVICE)\n",
+    "sensory_head = torch.nn.Linear(latent_dim, 10).to(DEVICE)\n",
+    "sensory_optimizer = torch.optim.AdamW(\n",
+    "    list(encoder.parameters()) + list(sensory_head.parameters()),\n",
+    "    lr=float(config[\"training\"][\"learning_rate\"]),\n",
+    "    weight_decay=float(config[\"training\"][\"weight_decay\"]),\n",
+    ")\n",
+    "\n",
+    "sensory_history = []\n",
+    "sensory_loader = fixed_loader(0.0, True, train_indices, True)\n",
+    "\n",
+    "for epoch in range(SENSORY_EPOCHS):\n",
+    "    encoder.train()\n",
+    "    total = correct = 0\n",
+    "    loss_sum = 0.0\n",
+    "    for x, y, _, _ in sensory_loader:\n",
+    "        x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "        logits = sensory_head(encoder(x))\n",
+    "        loss = F.cross_entropy(logits, y)\n",
+    "        if not torch.isfinite(loss):\n",
+    "            raise FloatingPointError(\"Non-finite sensory loss\")\n",
+    "        sensory_optimizer.zero_grad(set_to_none=True)\n",
+    "        loss.backward()\n",
+    "        torch.nn.utils.clip_grad_norm_(\n",
+    "            list(encoder.parameters()) + list(sensory_head.parameters()), 5.0\n",
+    "        )\n",
+    "        sensory_optimizer.step()\n",
+    "        total += y.numel()\n",
+    "        correct += (logits.argmax(1) == y).sum().item()\n",
+    "        loss_sum += float(loss.detach()) * y.numel()\n",
+    "    row = {\n",
+    "        \"epoch\": epoch,\n",
+    "        \"loss\": loss_sum / total,\n",
+    "        \"accuracy\": correct / total,\n",
+    "    }\n",
+    "    sensory_history.append(row)\n",
+    "    print(row)\n",
+    "\n",
+    "sensory_state = copy.deepcopy(encoder.state_dict())"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "5045b0a5",
+   "metadata": {},
+   "source": [
+    "## 4. Continual training variants\n",
+    "\n",
+    "### `no_geometry`\n",
+    "Same architecture and sequential angle schedule, but no paired route geometry.\n",
+    "\n",
+    "### `paired_geometry`\n",
+    "At stage `t`, each source is rendered at all angles already seen in stages\n",
+    "`0..t`. Classification loss is applied to the current angle only. Previous\n",
+    "views are geometry anchors. This is not claimed as a replay-free continual\n",
+    "learning method; it is a controlled G1-A geometry test."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "260d8c0c",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def host_diversity(host_outputs):\n",
+    "    h = F.normalize(host_outputs, dim=-1)\n",
+    "    sim = torch.einsum(\"bhd,bjd->bhj\", h, h)\n",
+    "    mask = ~torch.eye(sim.shape[-1], dtype=torch.bool, device=sim.device)\n",
+    "    return sim[:, mask].square().mean()\n",
+    "\n",
+    "def assert_finite_trace(trace, where):\n",
+    "    tensors = {\n",
+    "        \"z0\": trace.z0,\n",
+    "        \"context\": trace.context,\n",
+    "        \"route\": trace.route,\n",
+    "        \"host_outputs\": trace.host_outputs,\n",
+    "        \"z_mm\": trace.z_mm,\n",
+    "        \"logits\": trace.logits,\n",
+    "    }\n",
+    "    bad = [name for name, value in tensors.items() if not torch.isfinite(value).all()]\n",
+    "    if bad:\n",
+    "        raise FloatingPointError(f\"Non-finite tensors at {where}: {bad}\")\n",
+    "\n",
+    "@torch.no_grad()\n",
+    "def evaluate_model(model, angles, stage, method):\n",
+    "    rows = []\n",
+    "    model.eval()\n",
+    "    for angle in angles:\n",
+    "        loader = fixed_loader(angle, False, test_indices, False)\n",
+    "        total = correct = 0\n",
+    "        nll_sum = 0.0\n",
+    "        for x, y, _, _ in loader:\n",
+    "            x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "            trace = model(x)\n",
+    "            assert_finite_trace(trace, f\"eval method={method}, angle={angle}\")\n",
+    "            nll = F.cross_entropy(trace.logits, y, reduction=\"sum\")\n",
+    "            total += y.numel()\n",
+    "            correct += (trace.logits.argmax(1) == y).sum().item()\n",
+    "            nll_sum += float(nll)\n",
+    "        rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"stage\": stage,\n",
+    "            \"angle\": angle,\n",
+    "            \"angle_type\": (\n",
+    "                \"train\" if angle in train_angles\n",
+    "                else \"interpolation\" if angle in interp_angles\n",
+    "                else \"extrapolation\"\n",
+    "            ),\n",
+    "            \"accuracy\": correct / total,\n",
+    "            \"nll\": nll_sum / total,\n",
+    "        })\n",
+    "    return rows\n",
+    "\n",
+    "def build_model():\n",
+    "    local_encoder = SmallConvEncoder(latent_dim).to(DEVICE)\n",
+    "    local_encoder.load_state_dict(sensory_state)\n",
+    "    return GeometryMMALS(\n",
+    "        local_encoder,\n",
+    "        latent_dim=latent_dim,\n",
+    "        context_dim=int(config[\"model\"][\"context_dim\"]),\n",
+    "        num_hosts=int(config[\"model\"][\"num_hosts\"]),\n",
+    "        host_hidden_dim=int(config[\"model\"][\"host_hidden_dim\"]),\n",
+    "        freeze_encoder=True,\n",
+    "    ).to(DEVICE)\n",
+    "\n",
+    "def train_method(method):\n",
+    "    model = build_model()\n",
+    "    optimizer = torch.optim.AdamW(\n",
+    "        [p for p in model.parameters() if p.requires_grad],\n",
+    "        lr=float(config[\"training\"][\"learning_rate\"]),\n",
+    "        weight_decay=float(config[\"training\"][\"weight_decay\"]),\n",
+    "    )\n",
+    "    stage_rows = []\n",
+    "    evaluation_rows = []\n",
+    "\n",
+    "    for stage, current_angle in enumerate(train_angles):\n",
+    "        seen_angles = train_angles[: stage + 1]\n",
+    "        totals = {\"samples\": 0, \"loss\": 0.0, \"ce\": 0.0, \"geo\": 0.0, \"div\": 0.0}\n",
+    "\n",
+    "        if method == \"paired_geometry\":\n",
+    "            loader = multi_loader(seen_angles, True, train_indices, True)\n",
+    "        else:\n",
+    "            loader = fixed_loader(current_angle, True, train_indices, True)\n",
+    "\n",
+    "        model.train()\n",
+    "        for epoch in range(STAGE_EPOCHS):\n",
+    "            for batch_id, batch in enumerate(loader):\n",
+    "                if method == \"paired_geometry\":\n",
+    "                    views, y, factors, _ = batch\n",
+    "                    batch_size, angle_count = views.shape[:2]\n",
+    "                    flat_views = views.reshape(-1, *views.shape[2:]).to(DEVICE)\n",
+    "                    y = y.to(DEVICE)\n",
+    "                    factors = factors.to(DEVICE)\n",
+    "\n",
+    "                    trace = model(flat_views)\n",
+    "                    assert_finite_trace(\n",
+    "                        trace,\n",
+    "                        f\"{method}, stage={stage}, epoch={epoch}, batch={batch_id}\",\n",
+    "                    )\n",
+    "                    logits = trace.logits.reshape(batch_size, angle_count, -1)\n",
+    "                    routes = trace.route.reshape(batch_size, angle_count, -1)\n",
+    "                    hosts = trace.host_outputs.reshape(\n",
+    "                        batch_size, angle_count, trace.host_outputs.shape[1], -1\n",
+    "                    )\n",
+    "\n",
+    "                    current_index = angle_count - 1\n",
+    "                    ce = F.cross_entropy(logits[:, current_index], y)\n",
+    "                    geo = paired_route_geometry_loss(\n",
+    "                        routes,\n",
+    "                        factors,\n",
+    "                        bandwidth=float(config[\"losses\"][\"route_bandwidth_degrees\"]),\n",
+    "                        far_margin=float(config[\"losses\"][\"paired_route_far_margin\"]),\n",
+    "                        far_weight=float(config[\"losses\"][\"paired_route_far_weight\"]),\n",
+    "                        match_weight=float(config[\"losses\"][\"paired_route_match_weight\"]),\n",
+    "                    )\n",
+    "                    div = host_diversity(hosts[:, current_index])\n",
+    "                    sample_count = batch_size\n",
+    "                else:\n",
+    "                    x, y, _, _ = batch\n",
+    "                    x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "                    trace = model(x)\n",
+    "                    assert_finite_trace(\n",
+    "                        trace,\n",
+    "                        f\"{method}, stage={stage}, epoch={epoch}, batch={batch_id}\",\n",
+    "                    )\n",
+    "                    ce = F.cross_entropy(trace.logits, y)\n",
+    "                    geo = trace.route.sum() * 0.0\n",
+    "                    div = host_diversity(trace.host_outputs)\n",
+    "                    sample_count = y.numel()\n",
+    "\n",
+    "                loss = (\n",
+    "                    float(config[\"losses\"][\"classification\"]) * ce\n",
+    "                    + float(config[\"losses\"][\"route_geometry\"]) * geo\n",
+    "                    + float(config[\"losses\"][\"host_functional_diversity\"]) * div\n",
+    "                )\n",
+    "                if not torch.isfinite(torch.stack([ce, geo, div, loss])).all():\n",
+    "                    raise FloatingPointError(\n",
+    "                        f\"Non-finite loss in {method}, stage={stage}: \"\n",
+    "                        f\"ce={ce.item()}, geo={geo.item()}, div={div.item()}\"\n",
+    "                    )\n",
+    "\n",
+    "                optimizer.zero_grad(set_to_none=True)\n",
+    "                loss.backward()\n",
+    "                grad_norm = torch.nn.utils.clip_grad_norm_(\n",
+    "                    [p for p in model.parameters() if p.requires_grad], 5.0\n",
+    "                )\n",
+    "                if not torch.isfinite(torch.as_tensor(grad_norm)):\n",
+    "                    raise FloatingPointError(\"Non-finite gradient norm\")\n",
+    "                optimizer.step()\n",
+    "\n",
+    "                totals[\"samples\"] += sample_count\n",
+    "                totals[\"loss\"] += float(loss.detach()) * sample_count\n",
+    "                totals[\"ce\"] += float(ce.detach()) * sample_count\n",
+    "                totals[\"geo\"] += float(geo.detach()) * sample_count\n",
+    "                totals[\"div\"] += float(div.detach()) * sample_count\n",
+    "\n",
+    "        count = max(totals.pop(\"samples\"), 1)\n",
+    "        stage_row = {\n",
+    "            \"method\": method,\n",
+    "            \"stage\": stage,\n",
+    "            \"current_angle\": current_angle,\n",
+    "            \"seen_angles\": json.dumps(seen_angles),\n",
+    "            **{key: value / count for key, value in totals.items()},\n",
+    "        }\n",
+    "        stage_rows.append(stage_row)\n",
+    "        print(stage_row)\n",
+    "        evaluation_rows.extend(evaluate_model(model, all_eval_angles, stage, method))\n",
+    "\n",
+    "    return model, pd.DataFrame(stage_rows), pd.DataFrame(evaluation_rows)"
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "73a475d5",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "models = {}\n",
+    "stage_tables = []\n",
+    "evaluation_tables = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    print(\"\\n=== TRAINING\", method, \"===\")\n",
+    "    model, stage_df, evaluation_df = train_method(method)\n",
+    "    models[method] = model\n",
+    "    stage_tables.append(stage_df)\n",
+    "    evaluation_tables.append(evaluation_df)\n",
+    "\n",
+    "stage_df = pd.concat(stage_tables, ignore_index=True)\n",
+    "evaluation_df = pd.concat(evaluation_tables, ignore_index=True)\n",
+    "stage_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "a9bcb97b",
+   "metadata": {},
+   "source": [
+    "## 5. Staged accuracy and forgetting\n",
+    "\n",
+    "Forgetting is computed only on trained angles. Held-out angles are evaluated for\n",
+    "interpolation and extrapolation but are never considered learned tasks."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "632e380a",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def forgetting_table(evaluation):\n",
+    "    rows = []\n",
+    "    final_stage = int(evaluation.stage.max())\n",
+    "    for method in evaluation.method.unique():\n",
+    "        sub = evaluation[\n",
+    "            (evaluation.method == method)\n",
+    "            & (evaluation.angle_type == \"train\")\n",
+    "        ]\n",
+    "        for angle in train_angles:\n",
+    "            angle_rows = sub[sub.angle == angle].sort_values(\"stage\")\n",
+    "            seen_stage = train_angles.index(angle)\n",
+    "            angle_rows = angle_rows[angle_rows.stage >= seen_stage]\n",
+    "            best = float(angle_rows.accuracy.max())\n",
+    "            final = float(angle_rows[angle_rows.stage == final_stage].accuracy.iloc[0])\n",
+    "            rows.append({\n",
+    "                \"method\": method,\n",
+    "                \"angle\": angle,\n",
+    "                \"best_accuracy\": best,\n",
+    "                \"final_accuracy\": final,\n",
+    "                \"forgetting\": best - final,\n",
+    "            })\n",
+    "    return pd.DataFrame(rows)\n",
+    "\n",
+    "forgetting_df = forgetting_table(evaluation_df)\n",
+    "forgetting_df.groupby(\"method\").forgetting.mean()"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "e1772809",
+   "metadata": {},
+   "source": [
+    "## 6. Same-source paired trace collection\n",
+    "\n",
+    "Every row retains `source_index`. Primary geometry scores are computed within\n",
+    "each source block, then bootstrapped across source images."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "4448e068",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "@torch.no_grad()\n",
+    "def collect_paired_trace(model, method, angles, source_indices):\n",
+    "    model.eval()\n",
+    "    rows = []\n",
+    "    loader = multi_loader(angles, False, source_indices, False)\n",
+    "    for views, labels, factors, source_ids in loader:\n",
+    "        batch_size, angle_count = views.shape[:2]\n",
+    "        flat = views.reshape(-1, *views.shape[2:]).to(DEVICE)\n",
+    "        trace = model(flat)\n",
+    "        assert_finite_trace(trace, f\"paired trace {method}\")\n",
+    "\n",
+    "        z0 = trace.z0.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        context = trace.context.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        route = trace.route.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        z_mm = trace.z_mm.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        logits = trace.logits.reshape(batch_size, angle_count, -1).cpu().numpy()\n",
+    "        hosts = trace.host_outputs.reshape(\n",
+    "            batch_size, angle_count, trace.host_outputs.shape[1], -1\n",
+    "        ).cpu().numpy()\n",
+    "\n",
+    "        for b in range(batch_size):\n",
+    "            for a in range(angle_count):\n",
+    "                rows.append({\n",
+    "                    \"method\": method,\n",
+    "                    \"source_index\": int(source_ids[b]),\n",
+    "                    \"label\": int(labels[b]),\n",
+    "                    \"angle\": float(factors[b, a]),\n",
+    "                    \"prediction\": int(np.argmax(logits[b, a])),\n",
+    "                    \"z0\": z0[b, a],\n",
+    "                    \"context\": context[b, a],\n",
+    "                    \"route\": route[b, a],\n",
+    "                    \"z_mm\": z_mm[b, a],\n",
+    "                    \"hosts\": hosts[b, a],\n",
+    "                })\n",
+    "    return pd.DataFrame(rows)\n",
+    "\n",
+    "trace_tables = []\n",
+    "for method, model in models.items():\n",
+    "    trace_tables.append(\n",
+    "        collect_paired_trace(model, method, all_eval_angles, test_indices)\n",
+    "    )\n",
+    "trace_df = pd.concat(trace_tables, ignore_index=True)\n",
+    "print(\"paired trace rows:\", len(trace_df))"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "a8319242",
+   "metadata": {},
+   "source": [
+    "## 7. Source-block and centroid geometry\n",
+    "\n",
+    "Primary uncertainty is block-bootstrap over source images. Factor-centroid\n",
+    "geometry is reported as a complementary tie-free view. No global all-pairs\n",
+    "p-value is used as evidence."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "cfb140f7",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def stack_column(frame, name):\n",
+    "    return np.stack(frame[name].to_numpy())\n",
+    "\n",
+    "geometry_rows = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    sub = trace_df[trace_df.method == method]\n",
+    "    factors = sub.angle.to_numpy(float)\n",
+    "    groups = sub.source_index.to_numpy()\n",
+    "\n",
+    "    spaces = {\n",
+    "        \"sensory\": (\"euclidean\", stack_column(sub, \"z0\")),\n",
+    "        \"context\": (\"euclidean\", stack_column(sub, \"context\")),\n",
+    "        \"route\": (\"fisher_rao\", stack_column(sub, \"route\")),\n",
+    "        \"synthesis\": (\"euclidean\", stack_column(sub, \"z_mm\")),\n",
+    "    }\n",
+    "\n",
+    "    for space, (metric, reps) in spaces.items():\n",
+    "        grouped = grouped_geometry_scores(\n",
+    "            factors,\n",
+    "            reps,\n",
+    "            groups,\n",
+    "            metric=metric,\n",
+    "        )\n",
+    "        rho_mean, rho_low, rho_high = bootstrap_mean_ci(\n",
+    "            grouped[\"rho\"],\n",
+    "            samples=BOOTSTRAP_SAMPLES,\n",
+    "            seed=SEED,\n",
+    "        )\n",
+    "        stress_mean, stress_low, stress_high = bootstrap_mean_ci(\n",
+    "            grouped[\"stress\"],\n",
+    "            samples=BOOTSTRAP_SAMPLES,\n",
+    "            seed=SEED + 1,\n",
+    "        )\n",
+    "        centroid = centroid_geometry_scores(\n",
+    "            factors,\n",
+    "            reps,\n",
+    "            metric=metric,\n",
+    "        )\n",
+    "        geometry_rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"space\": space,\n",
+    "            \"source_rho_mean\": rho_mean,\n",
+    "            \"source_rho_ci_low\": rho_low,\n",
+    "            \"source_rho_ci_high\": rho_high,\n",
+    "            \"source_stress_mean\": stress_mean,\n",
+    "            \"source_stress_ci_low\": stress_low,\n",
+    "            \"source_stress_ci_high\": stress_high,\n",
+    "            \"centroid_rho\": centroid[\"rho\"],\n",
+    "            \"centroid_stress\": centroid[\"stress\"],\n",
+    "            \"source_blocks\": len(grouped[\"rho\"]),\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "\n",
+    "geometry_df = pd.DataFrame(geometry_rows)\n",
+    "geometry_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "6ffa3d0e",
+   "metadata": {},
+   "source": [
+    "## 8. Held-out interpolation controls\n",
+    "\n",
+    "The model is evaluated on held-out angles for accuracy and NLL. Context\n",
+    "centroids are compared with linear interpolation between neighboring trained\n",
+    "centroids. Route centroids are interpolated in square-root simplex coordinates\n",
+    "and compared with a nearest-trained-route control."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "ff6b2c7b",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def centroid_by_angle(frame, column):\n",
+    "    return {\n",
+    "        float(angle): np.stack(group[column].to_numpy()).mean(axis=0)\n",
+    "        for angle, group in frame.groupby(\"angle\")\n",
+    "    }\n",
+    "\n",
+    "def linear_neighbors(angle, trained):\n",
+    "    lower = max(value for value in trained if value < angle)\n",
+    "    upper = min(value for value in trained if value > angle)\n",
+    "    alpha = (angle - lower) / (upper - lower)\n",
+    "    return lower, upper, alpha\n",
+    "\n",
+    "interpolation_rows = []\n",
+    "final_stage = int(evaluation_df.stage.max())\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    final_eval = evaluation_df[\n",
+    "        (evaluation_df.method == method)\n",
+    "        & (evaluation_df.stage == final_stage)\n",
+    "        & (evaluation_df.angle_type == \"interpolation\")\n",
+    "    ]\n",
+    "    sub = trace_df[trace_df.method == method]\n",
+    "    context_centroids = centroid_by_angle(sub, \"context\")\n",
+    "    route_centroids = centroid_by_angle(sub, \"route\")\n",
+    "\n",
+    "    for row in final_eval.itertuples():\n",
+    "        angle = float(row.angle)\n",
+    "        lower, upper, alpha = linear_neighbors(angle, train_angles)\n",
+    "\n",
+    "        c_pred = (\n",
+    "            (1.0 - alpha) * context_centroids[lower]\n",
+    "            + alpha * context_centroids[upper]\n",
+    "        )\n",
+    "        context_error = float(np.linalg.norm(context_centroids[angle] - c_pred))\n",
+    "\n",
+    "        p_low = route_centroids[lower]\n",
+    "        p_high = route_centroids[upper]\n",
+    "        root_pred = (\n",
+    "            (1.0 - alpha) * np.sqrt(np.clip(p_low, 1e-12, None))\n",
+    "            + alpha * np.sqrt(np.clip(p_high, 1e-12, None))\n",
+    "        )\n",
+    "        p_pred = np.square(root_pred)\n",
+    "        p_pred = p_pred / p_pred.sum()\n",
+    "\n",
+    "        actual = route_centroids[angle]\n",
+    "        route_interp_error = fisher_rao_distance(actual, p_pred)\n",
+    "        nearest_error = min(\n",
+    "            fisher_rao_distance(actual, p_low),\n",
+    "            fisher_rao_distance(actual, p_high),\n",
+    "        )\n",
+    "\n",
+    "        interpolation_rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"angle\": angle,\n",
+    "            \"accuracy\": float(row.accuracy),\n",
+    "            \"nll\": float(row.nll),\n",
+    "            \"context_interpolation_error\": context_error,\n",
+    "            \"route_interpolation_error\": route_interp_error,\n",
+    "            \"nearest_route_error\": nearest_error,\n",
+    "            \"route_interpolation_beats_nearest\": route_interp_error < nearest_error,\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "\n",
+    "interpolation_df = pd.DataFrame(interpolation_rows)\n",
+    "interpolation_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "1bbf8d0f",
+   "metadata": {},
+   "source": [
+    "## 9. Host ablation bundle\n",
+    "\n",
+    "Ablation is summarized by mean, median and positive-contribution fraction.\n",
+    "Route mass alone is not interpreted as specialization."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "666da235",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "@torch.no_grad()\n",
+    "def host_ablation_table(model, method, angles, source_indices):\n",
+    "    model.eval()\n",
+    "    rows = []\n",
+    "    for angle in angles:\n",
+    "        loader = fixed_loader(angle, False, source_indices, False)\n",
+    "        for x, y, _, source_id in loader:\n",
+    "            x, y = x.to(DEVICE), y.to(DEVICE)\n",
+    "            trace = model(x)\n",
+    "            base = F.log_softmax(trace.logits, -1).gather(\n",
+    "                1, y[:, None]\n",
+    "            ).squeeze(1)\n",
+    "            for host in range(trace.route.shape[1]):\n",
+    "                route = trace.route.clone()\n",
+    "                route[:, host] = 0.0\n",
+    "                route = route / route.sum(1, keepdim=True).clamp_min(1e-8)\n",
+    "                z = torch.einsum(\"bh,bhd->bd\", route, trace.host_outputs)\n",
+    "                logits = model.classifier(model.synthesis_norm(z))\n",
+    "                ablated = F.log_softmax(logits, -1).gather(\n",
+    "                    1, y[:, None]\n",
+    "                ).squeeze(1)\n",
+    "                impact = (base - ablated).detach().cpu().numpy()\n",
+    "                for idx, value in enumerate(impact):\n",
+    "                    rows.append({\n",
+    "                        \"method\": method,\n",
+    "                        \"angle\": angle,\n",
+    "                        \"source_index\": int(source_id[idx]),\n",
+    "                        \"host\": host,\n",
+    "                        \"ablation_impact\": float(value),\n",
+    "                    })\n",
+    "    raw = pd.DataFrame(rows)\n",
+    "    summary = (\n",
+    "        raw.groupby([\"method\", \"angle\", \"host\"])\n",
+    "        .ablation_impact\n",
+    "        .agg(\n",
+    "            mean=\"mean\",\n",
+    "            median=\"median\",\n",
+    "            positive_fraction=lambda values: float(np.mean(values > 0)),\n",
+    "            count=\"count\",\n",
+    "        )\n",
+    "        .reset_index()\n",
+    "    )\n",
+    "    return raw, summary\n",
+    "\n",
+    "ablation_raw_tables = []\n",
+    "ablation_summary_tables = []\n",
+    "for method, model in models.items():\n",
+    "    raw, summary = host_ablation_table(\n",
+    "        model,\n",
+    "        method,\n",
+    "        train_angles + interp_angles,\n",
+    "        test_indices,\n",
+    "    )\n",
+    "    ablation_raw_tables.append(raw)\n",
+    "    ablation_summary_tables.append(summary)\n",
+    "\n",
+    "ablation_raw_df = pd.concat(ablation_raw_tables, ignore_index=True)\n",
+    "ablation_summary_df = pd.concat(ablation_summary_tables, ignore_index=True)\n",
+    "ablation_summary_df.head()"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "527ca86f",
+   "metadata": {},
+   "source": [
+    "## 10. Signed causal route-direction probe\n",
+    "\n",
+    "The probe estimates a context direction associated with increasing angle and a\n",
+    "route direction from route centroids. It reports a **signed** projection of the\n",
+    "route change and compares it with matched-norm context directions orthogonal to\n",
+    "the angle tangent.\n",
+    "\n",
+    "This remains development evidence. Qualification requires bootstrap confidence\n",
+    "intervals, class-identity gates and replication across seeds."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "ac786437",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "def orthogonal_directions(tangent, count, seed):\n",
+    "    rng = np.random.default_rng(seed)\n",
+    "    directions = []\n",
+    "    for _ in range(count):\n",
+    "        vector = rng.normal(size=tangent.shape)\n",
+    "        vector = vector - np.dot(vector, tangent) * tangent\n",
+    "        norm = np.linalg.norm(vector)\n",
+    "        if norm > 1e-12:\n",
+    "            directions.append(vector / norm)\n",
+    "    return directions\n",
+    "\n",
+    "@torch.no_grad()\n",
+    "def causal_probe(model, method, trace, probe_angle=15.0, scales=(-2, -1, 0, 1, 2)):\n",
+    "    trained = trace[trace.angle.isin(train_angles)]\n",
+    "    contexts = stack_column(trained, \"context\").astype(np.float64)\n",
+    "    angles = trained.angle.to_numpy(float)\n",
+    "\n",
+    "    x = contexts - contexts.mean(0, keepdims=True)\n",
+    "    y = angles - angles.mean()\n",
+    "    ridge = 1e-6 * max(np.trace(x.T @ x) / max(x.shape[1], 1), 1.0)\n",
+    "    tangent = np.linalg.solve(\n",
+    "        x.T @ x + ridge * np.eye(x.shape[1]),\n",
+    "        x.T @ y,\n",
+    "    )\n",
+    "    tangent = tangent / max(np.linalg.norm(tangent), 1e-12)\n",
+    "\n",
+    "    route_centroids = centroid_by_angle(trained, \"route\")\n",
+    "    route_matrix = np.stack([\n",
+    "        np.sqrt(np.clip(route_centroids[angle], 1e-12, None))\n",
+    "        for angle in train_angles\n",
+    "    ])\n",
+    "    centered_angles = np.asarray(train_angles) - np.mean(train_angles)\n",
+    "    route_centered = route_matrix - route_matrix.mean(0, keepdims=True)\n",
+    "    route_direction = (\n",
+    "        centered_angles[:, None] * route_centered\n",
+    "    ).sum(axis=0) / max(np.sum(centered_angles ** 2), 1e-12)\n",
+    "    route_direction = route_direction / max(np.linalg.norm(route_direction), 1e-12)\n",
+    "\n",
+    "    orthogonals = orthogonal_directions(tangent, count=8, seed=SEED + 9)\n",
+    "    loader = fixed_loader(probe_angle, False, test_indices, False)\n",
+    "    x_batch, y_batch, _, _ = next(iter(loader))\n",
+    "    x_batch, y_batch = x_batch.to(DEVICE), y_batch.to(DEVICE)\n",
+    "    base = model(x_batch)\n",
+    "    base_logp = F.log_softmax(base.logits, -1).gather(1, y_batch[:, None]).squeeze(1)\n",
+    "\n",
+    "    tangent_tensor = torch.tensor(tangent, dtype=base.context.dtype, device=DEVICE)\n",
+    "    route_dir_tensor = torch.tensor(\n",
+    "        route_direction, dtype=base.route.dtype, device=DEVICE\n",
+    "    )\n",
+    "\n",
+    "    rows = []\n",
+    "    for scale in scales:\n",
+    "        new_context = base.context + float(scale) * tangent_tensor\n",
+    "        new_route = torch.softmax(\n",
+    "            model.router(torch.cat([base.z0, new_context], dim=-1)),\n",
+    "            dim=-1,\n",
+    "        )\n",
+    "        delta_root = torch.sqrt(new_route.clamp_min(1e-12)) - torch.sqrt(\n",
+    "            base.route.clamp_min(1e-12)\n",
+    "        )\n",
+    "        signed_effect = float(\n",
+    "            (delta_root * route_dir_tensor).sum(dim=1).mean().detach().cpu()\n",
+    "        )\n",
+    "\n",
+    "        z = torch.einsum(\"bh,bhd->bd\", new_route, base.host_outputs)\n",
+    "        logits = model.classifier(model.synthesis_norm(z))\n",
+    "        new_logp = F.log_softmax(logits, -1).gather(1, y_batch[:, None]).squeeze(1)\n",
+    "        identity_drop = float((base_logp - new_logp).mean().detach().cpu())\n",
+    "\n",
+    "        orth_effects = []\n",
+    "        for direction in orthogonals:\n",
+    "            direction_tensor = torch.tensor(\n",
+    "                direction, dtype=base.context.dtype, device=DEVICE\n",
+    "            )\n",
+    "            c_orth = base.context + float(scale) * direction_tensor\n",
+    "            r_orth = torch.softmax(\n",
+    "                model.router(torch.cat([base.z0, c_orth], dim=-1)),\n",
+    "                dim=-1,\n",
+    "            )\n",
+    "            delta_orth = torch.sqrt(r_orth.clamp_min(1e-12)) - torch.sqrt(\n",
+    "                base.route.clamp_min(1e-12)\n",
+    "            )\n",
+    "            orth_effects.append(\n",
+    "                float(\n",
+    "                    torch.abs(\n",
+    "                        (delta_orth * route_dir_tensor).sum(dim=1)\n",
+    "                    ).mean().detach().cpu()\n",
+    "                )\n",
+    "            )\n",
+    "\n",
+    "        orth_mean = float(np.mean(orth_effects)) if orth_effects else float(\"nan\")\n",
+    "        csr = abs(signed_effect) / max(orth_mean, 1e-12) if scale != 0 else 0.0\n",
+    "        rows.append({\n",
+    "            \"method\": method,\n",
+    "            \"probe_angle\": probe_angle,\n",
+    "            \"scale\": scale,\n",
+    "            \"signed_route_effect\": signed_effect,\n",
+    "            \"orthogonal_abs_effect_mean\": orth_mean,\n",
+    "            \"causal_specificity_ratio\": csr,\n",
+    "            \"class_log_prob_drop\": identity_drop,\n",
+    "            \"status\": \"development_not_qualified\",\n",
+    "        })\n",
+    "    return pd.DataFrame(rows)\n",
+    "\n",
+    "causal_tables = []\n",
+    "for method, model in models.items():\n",
+    "    causal_tables.append(\n",
+    "        causal_probe(\n",
+    "            model,\n",
+    "            method,\n",
+    "            trace_df[trace_df.method == method],\n",
+    "        )\n",
+    "    )\n",
+    "causal_df = pd.concat(causal_tables, ignore_index=True)\n",
+    "causal_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "f83a28c6",
+   "metadata": {},
+   "source": [
+    "## 11. Development gate summary\n",
+    "\n",
+    "The notebook computes measurements needed for C1-C4, but it does not\n",
+    "automatically convert a development run into a claim. A gate may be marked\n",
+    "`candidate_pass` only after frozen thresholds, multi-seed aggregation and all\n",
+    "required controls are present."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "3ae29bb8",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "gate_rows = []\n",
+    "\n",
+    "for method in METHODS:\n",
+    "    route_row = geometry_df[\n",
+    "        (geometry_df.method == method) & (geometry_df.space == \"route\")\n",
+    "    ].iloc[0]\n",
+    "    interp = interpolation_df[interpolation_df.method == method]\n",
+    "    forgetting = forgetting_df[forgetting_df.method == method]\n",
+    "\n",
+    "    gate_rows.append({\n",
+    "        \"method\": method,\n",
+    "        \"C1_route_source_rho\": route_row.source_rho_mean,\n",
+    "        \"C1_route_rho_ci_low\": route_row.source_rho_ci_low,\n",
+    "        \"C1_route_centroid_rho\": route_row.centroid_rho,\n",
+    "        \"C2_mean_interpolation_accuracy\": interp.accuracy.mean(),\n",
+    "        \"C2_route_interp_win_fraction\": interp.route_interpolation_beats_nearest.mean(),\n",
+    "        \"mean_trained_angle_forgetting\": forgetting.forgetting.mean(),\n",
+    "        \"qualification_status\": \"not_qualified\",\n",
+    "    })\n",
+    "\n",
+    "gate_summary_df = pd.DataFrame(gate_rows)\n",
+    "gate_summary_df"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "d24cb3e3",
+   "metadata": {},
+   "source": [
+    "## 12. Export and immutable manifest\n",
+    "\n",
+    "All exported tables retain epistemic status. The manifest records the package\n",
+    "version, git SHA, split checksums, compared methods and notebook history."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "64a24fcc",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "output_root = Path(\"results/v1_0_3\") / f\"seed_{SEED}\"\n",
+    "output_root.mkdir(parents=True, exist_ok=True)\n",
+    "\n",
+    "stage_df.to_csv(output_root / \"stage_logs.csv\", index=False)\n",
+    "evaluation_df.to_csv(output_root / \"staged_evaluation.csv\", index=False)\n",
+    "forgetting_df.to_csv(output_root / \"forgetting.csv\", index=False)\n",
+    "geometry_df.to_csv(output_root / \"paired_geometry_metrics.csv\", index=False)\n",
+    "interpolation_df.to_csv(output_root / \"interpolation_metrics.csv\", index=False)\n",
+    "ablation_summary_df.to_csv(output_root / \"host_ablation_summary.csv\", index=False)\n",
+    "ablation_raw_df.to_csv(output_root / \"host_ablation_raw.csv\", index=False)\n",
+    "causal_df.to_csv(output_root / \"causal_probe.csv\", index=False)\n",
+    "gate_summary_df.to_csv(output_root / \"development_gate_summary.csv\", index=False)\n",
+    "pd.DataFrame(sensory_history).to_csv(output_root / \"sensory_history.csv\", index=False)\n",
+    "\n",
+    "run_manifest = {\n",
+    "    \"status\": \"development_not_qualified\",\n",
+    "    \"notebook_version\": \"1.0.3\",\n",
+    "    \"package_version\": package_version,\n",
+    "    \"git_sha\": git_sha,\n",
+    "    \"run_mode\": RUN_MODE,\n",
+    "    \"seed\": SEED,\n",
+    "    \"device\": str(DEVICE),\n",
+    "    \"methods\": METHODS,\n",
+    "    \"train_angles\": train_angles,\n",
+    "    \"interpolation_angles\": interp_angles,\n",
+    "    \"extrapolation_angles\": extra_angles,\n",
+    "    \"split_manifest\": split_manifest,\n",
+    "    \"tracked_changes\": [f\"CHG-103-{index:02d}\" for index in range(1, 11)],\n",
+    "    \"warning\": (\n",
+    "        \"This archive implements the corrected paired protocol. \"\n",
+    "        \"It is not a qualified C1-C6 result.\"\n",
+    "    ),\n",
+    "    \"timestamp\": time.time(),\n",
+    "}\n",
+    "(output_root / \"run_manifest.json\").write_text(\n",
+    "    json.dumps(run_manifest, indent=2),\n",
+    "    encoding=\"utf-8\",\n",
+    ")\n",
+    "print(\"Exported to:\", output_root.resolve())"
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "3decc6cb",
+   "metadata": {},
+   "source": [
+    "## 13. Qualification checklist\n",
+    "\n",
+    "Before any C1-C6 claim:\n",
+    "\n",
+    "1. Freeze gates before qualification runs.\n",
+    "2. Run at least five seeds for pilot qualification and ten for final evidence.\n",
+    "3. Validate `no_geometry` and `paired_geometry` with equal budgets.\n",
+    "4. Add tuned EWC, replay, sparse-MoE, oracle-angle and joint upper-bound controls.\n",
+    "5. Report source-block confidence intervals and failed seeds.\n",
+    "6. Confirm interpolation angles never enter training or checkpoint selection.\n",
+    "7. Add role matching across seeds for host specialization.\n",
+    "8. Add memory-transport and dual-memory experiments before C5.\n",
+    "9. Replicate on a secondary controlled factor or dataset.\n",
+    "10. Archive notebook, CSVs, manifest, environment and commit SHA."
+   ]
+  },
+  {
+   "cell_type": "markdown",
+   "id": "85d78746",
+   "metadata": {},
+   "source": [
+    "## 14. Optional PDF export\n",
+    "\n",
+    "The GitHub archive contains a separate protocol correction report under\n",
+    "`docs/reports/`. Notebook PDF export is optional and should not replace the raw\n",
+    "`.ipynb`, CSV tables or manifest."
+   ]
+  },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "id": "fba381b1",
+   "metadata": {},
+   "outputs": [],
+   "source": [
+    "# Optional: save/upload this notebook first, then run.\n",
+    "# The command passes each list-valued latex argument separately.\n",
+    "#\n",
+    "# import subprocess, sys\n",
+    "# from pathlib import Path\n",
+    "#\n",
+    "# notebook_path = Path(\"/content/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb\")\n",
+    "# output_dir = Path(\"/content/pdf_export\")\n",
+    "# output_dir.mkdir(parents=True, exist_ok=True)\n",
+    "# subprocess.run([\n",
+    "#     sys.executable, \"-m\", \"jupyter\", \"nbconvert\",\n",
+    "#     \"--to\", \"pdf\",\n",
+    "#     str(notebook_path),\n",
+    "#     \"--output-dir\", str(output_dir),\n",
+    "#     \"--PDFExporter.latex_command=xelatex\",\n",
+    "#     \"--PDFExporter.latex_command={filename}\",\n",
+    "#     \"--PDFExporter.latex_command=-interaction=nonstopmode\",\n",
+    "#     \"--PDFExporter.latex_count=3\",\n",
+    "# ], check=True)"
+   ]
+  }
+ ],
+ "metadata": {
+  "colab": {
+   "name": "Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb",
+   "provenance": []
+  },
+  "geometry_mmalls": {
+   "status": "development_not_qualified",
+   "tracked_changes": [
+    "CHG-103-01",
+    "CHG-103-02",
+    "CHG-103-03",
+    "CHG-103-04",
+    "CHG-103-05",
+    "CHG-103-06",
+    "CHG-103-07",
+    "CHG-103-08",
+    "CHG-103-09",
+    "CHG-103-10"
+   ],
+   "version": "1.0.3"
+  },
+  "kernelspec": {
+   "display_name": "Python 3",
+   "language": "python",
+   "name": "python3"
+  },
+  "language_info": {
+   "name": "python",
+   "version": "3.x"
+  }
+ },
+ "nbformat": 4,
+ "nbformat_minor": 5
+}
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/pyproject.toml /mnt/data/geometry-mmalls-g1-v103/pyproject.toml
--- /mnt/data/geometry-mmalls-g1-v102/pyproject.toml	2026-06-13 21:58:03.596796367 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/pyproject.toml	2026-06-13 22:34:10.726508027 +0000
@@ -4,7 +4,7 @@
 
 [project]
 name = "geometry-mmalls-g1"
-version = "1.0.2"
+version = "1.0.3"
 description = "Grounded functional geometry experiments for MMALS continual learning"
 readme = "README.md"
 requires-python = ">=3.10"
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/scripts/build_protocol_report_v103.py /mnt/data/geometry-mmalls-g1-v103/scripts/build_protocol_report_v103.py
--- /mnt/data/geometry-mmalls-g1-v102/scripts/build_protocol_report_v103.py	1970-01-01 00:00:00.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/scripts/build_protocol_report_v103.py	2026-06-13 22:34:16.627924302 +0000
@@ -0,0 +1,9 @@
+"""Build note for the archived v1.0.3 protocol report.
+
+The release PDF was generated programmatically with ReportLab from the
+versioned change record. The editable narrative is preserved in
+docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.md.
+
+Regenerate the PDF with the project artifact builder used for the release or
+convert the Markdown source with the repository's preferred publication tool.
+"""
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/__init__.py /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/__init__.py
--- /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/__init__.py	2026-06-13 19:35:51.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/__init__.py	2026-06-13 22:34:10.727784114 +0000
@@ -4,6 +4,7 @@
     fisher_rao_distance,
     pairwise_fisher_rao,
     route_geodesic_loss,
+    paired_route_geometry_loss,
     normalized_stress,
 )
 from .metrics import (
@@ -11,19 +12,26 @@
     neighborhood_preservation,
     linear_cka,
     route_entropy,
+    bootstrap_mean_ci,
+    grouped_geometry_scores,
+    centroid_geometry_scores,
 )
 
 __all__ = [
     "fisher_rao_distance",
     "pairwise_fisher_rao",
     "route_geodesic_loss",
+    "paired_route_geometry_loss",
     "normalized_stress",
     "distance_order_correlation",
     "neighborhood_preservation",
     "linear_cka",
     "route_entropy",
+    "bootstrap_mean_ci",
+    "grouped_geometry_scores",
+    "centroid_geometry_scores",
 ]
 
-__version__ = "1.0.0"
+__version__ = "1.0.3"
 
 from .memory import ReconstructiveAuditMemory, SyntheticFunctionalMemory, TraceRecord
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/data.py /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/data.py
--- /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/data.py	2026-06-13 18:04:24.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/data.py	2026-06-13 22:34:10.728764433 +0000
@@ -39,6 +39,54 @@
         return image, int(label), torch.tensor(self.angle, dtype=torch.float32), int(index)
 
 
+class MultiAngleMNIST(Dataset):
+    """Return multiple rotated views of the same MNIST source image.
+
+    Each item is ``(views, label, angles, source_index)`` where ``views`` has
+    shape ``[n_angles, 1, 28, 28]``. This is the canonical data primitive for
+    the G1-A cross-angle paired protocol. The true angle is available only to
+    the controlled loss and evaluator; it is never passed to the deployable
+    router.
+    """
+
+    def __init__(
+        self,
+        root: str | Path,
+        angles: Sequence[float],
+        train: bool,
+        indices: Sequence[int] | None = None,
+        download: bool = True,
+    ) -> None:
+        self.base = MNIST(root=str(root), train=train, download=download)
+        self.angles = tuple(float(angle) for angle in angles)
+        if not self.angles:
+            raise ValueError("angles must contain at least one value")
+        if indices is None:
+            self.indices = tuple(range(len(self.base)))
+        else:
+            self.indices = tuple(int(index) for index in indices)
+            if not self.indices:
+                raise ValueError("indices must not be empty")
+            if min(self.indices) < 0 or max(self.indices) >= len(self.base):
+                raise IndexError("indices contain values outside the MNIST split")
+
+    def __len__(self) -> int:
+        return len(self.indices)
+
+    def __getitem__(self, position: int):
+        source_index = self.indices[position]
+        image, label = self.base[source_index]
+        views = torch.stack(
+            [
+                TF.to_tensor(TF.rotate(image, angle=angle, fill=0))
+                for angle in self.angles
+            ],
+            dim=0,
+        )
+        factors = torch.tensor(self.angles, dtype=torch.float32)
+        return views, int(label), factors, int(source_index)
+
+
 @dataclass(frozen=True)
 class AngleProtocol:
     train_angles: Sequence[float]
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/geometry.py /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/geometry.py
--- /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/geometry.py	2026-06-13 21:58:03.596097184 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/geometry.py	2026-06-13 22:34:10.729553754 +0000
@@ -101,6 +101,88 @@
     return smooth + float(far_weight) * far_penalty
 
 
+def paired_route_geometry_loss(
+    routes: torch.Tensor,
+    factors: torch.Tensor,
+    bandwidth: float = 20.0,
+    far_margin: float = 0.20,
+    far_weight: float = 0.25,
+    match_weight: float = 0.50,
+    eps: float = 1e-8,
+) -> torch.Tensor:
+    """Ground route geometry using same-source cross-angle views.
+
+    Parameters
+    ----------
+    routes:
+        Routing probabilities with shape ``[batch, angles, hosts]``.
+    factors:
+        Angle values with shape ``[angles]`` or ``[batch, angles]``.
+
+    Notes
+    -----
+    Optimization uses chordal distance in square-root simplex coordinates,
+    which is monotonic with Fisher-Rao distance and has a stable backward pass.
+    Fisher-Rao distance remains the evaluation metric. The loss combines:
+
+    - local continuity for nearby angles;
+    - a far-angle separation margin;
+    - normalized distance matching across all off-diagonal angle pairs.
+
+    A single-angle input returns a differentiable zero because no cross-angle
+    geometric statement can be made.
+    """
+
+    if routes.ndim != 3:
+        raise ValueError("routes must have shape [batch, angles, hosts]")
+    batch, n_angles, _ = routes.shape
+    if n_angles < 2:
+        return routes.sum() * 0.0
+
+    factors = factors.to(routes.device, routes.dtype)
+    if factors.ndim == 1:
+        if factors.shape[0] != n_angles:
+            raise ValueError("factors length must match the angle dimension")
+        factors = factors.unsqueeze(0).expand(batch, -1)
+    elif factors.ndim == 2:
+        if factors.shape != (batch, n_angles):
+            raise ValueError("factors must have shape [batch, angles]")
+    else:
+        raise ValueError("factors must be 1-D or 2-D")
+
+    p = routes.clamp_min(eps)
+    p = p / p.sum(dim=-1, keepdim=True)
+    roots = torch.sqrt(p)
+    affinity = torch.bmm(roots, roots.transpose(1, 2)).clamp(0.0, 1.0)
+
+    # Squared chordal distance in the square-root simplex embedding.
+    # This is 2(1-affinity), is monotonic with Fisher-Rao distance, and avoids
+    # the arccos derivative singularity during optimization.
+    chord_sq = 2.0 * (1.0 - affinity)
+
+    eye = torch.eye(n_angles, dtype=torch.bool, device=routes.device)
+    pair_mask = (~eye).unsqueeze(0).expand(batch, -1, -1)
+
+    d_factor = torch.abs(factors[:, :, None] - factors[:, None, :])
+    near_w = torch.exp(
+        -torch.square(d_factor / max(float(bandwidth), eps))
+    ).masked_fill(~pair_mask, 0.0)
+    local = (near_w * chord_sq).sum() / near_w.sum().clamp_min(eps)
+
+    far_mask = pair_mask & (d_factor >= float(bandwidth))
+    if torch.any(far_mask):
+        far = torch.relu(float(far_margin) - chord_sq[far_mask]).square().mean()
+    else:
+        far = routes.sum() * 0.0
+
+    max_gap = d_factor.amax(dim=(1, 2), keepdim=True).clamp_min(eps)
+    target = d_factor / max_gap
+    observed = torch.sqrt(chord_sq.clamp_min(eps) / 2.0)
+    match = torch.square(observed - target)[pair_mask].mean()
+
+    return local + float(far_weight) * far + float(match_weight) * match
+
+
 def normalized_stress(
     reference_distances: np.ndarray,
     representation_distances: np.ndarray,
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/metrics.py /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/metrics.py
--- /mnt/data/geometry-mmalls-g1-v102/src/geometry_mmalls/metrics.py	2026-06-13 18:04:24.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/src/geometry_mmalls/metrics.py	2026-06-13 22:34:10.730306734 +0000
@@ -124,3 +124,114 @@
         mask = (u >= left) & (u < right)
         result[f"[{left:g},{right:g})"] = float(np.mean(c[mask])) if np.any(mask) else float("nan")
     return result
+
+
+def bootstrap_mean_ci(
+    values: np.ndarray,
+    samples: int = 1000,
+    confidence: float = 0.95,
+    seed: int = 0,
+) -> tuple[float, float, float]:
+    """Block-bootstrap confidence interval for a vector of group-level scores."""
+
+    x = np.asarray(values, dtype=np.float64).reshape(-1)
+    x = x[np.isfinite(x)]
+    if x.size == 0:
+        return float("nan"), float("nan"), float("nan")
+    if samples < 1:
+        raise ValueError("samples must be positive")
+    if not 0.0 < confidence < 1.0:
+        raise ValueError("confidence must lie in (0, 1)")
+
+    rng = np.random.default_rng(seed)
+    boot = np.empty(samples, dtype=np.float64)
+    for index in range(samples):
+        boot[index] = np.mean(rng.choice(x, size=x.size, replace=True))
+    alpha = 1.0 - confidence
+    return (
+        float(np.mean(x)),
+        float(np.quantile(boot, alpha / 2.0)),
+        float(np.quantile(boot, 1.0 - alpha / 2.0)),
+    )
+
+
+def grouped_geometry_scores(
+    factor_values: np.ndarray,
+    representations: np.ndarray,
+    group_ids: np.ndarray,
+    metric: str = "euclidean",
+) -> dict[str, np.ndarray]:
+    """Compute geometry scores independently inside each source block.
+
+    This avoids treating millions of dependent cross-sample pairs as
+    independent observations. ``group_ids`` should normally be the original
+    image identifier, so every group contains the same source image observed
+    under several angles.
+    """
+
+    from .geometry import normalized_stress, pairwise_fisher_rao
+
+    factors = np.asarray(factor_values, dtype=np.float64).reshape(-1)
+    reps = np.asarray(representations, dtype=np.float64)
+    groups = np.asarray(group_ids).reshape(-1)
+    if reps.ndim != 2 or len(factors) != len(reps) or len(groups) != len(reps):
+        raise ValueError("factors, representations and group_ids must align")
+
+    rhos: list[float] = []
+    stresses: list[float] = []
+    group_values: list[object] = []
+
+    for group in np.unique(groups):
+        mask = groups == group
+        if np.count_nonzero(mask) < 3:
+            continue
+        u = factors[mask]
+        x = reps[mask]
+        d_ref = pairwise_factor_distance(u)
+        if metric == "euclidean":
+            d_rep = euclidean_distance_matrix(x)
+        elif metric == "fisher_rao":
+            d_rep = pairwise_fisher_rao(x)
+        else:
+            raise ValueError("metric must be 'euclidean' or 'fisher_rao'")
+        rho, _ = distance_order_correlation(d_ref, d_rep)
+        rhos.append(rho)
+        stresses.append(normalized_stress(d_ref, d_rep))
+        group_values.append(group)
+
+    return {
+        "group_ids": np.asarray(group_values),
+        "rho": np.asarray(rhos, dtype=np.float64),
+        "stress": np.asarray(stresses, dtype=np.float64),
+    }
+
+
+def centroid_geometry_scores(
+    factor_values: np.ndarray,
+    representations: np.ndarray,
+    metric: str = "euclidean",
+) -> dict[str, float]:
+    """Geometry scores on factor-level centroids, avoiding nearest-neighbor ties."""
+
+    from .geometry import normalized_stress, pairwise_fisher_rao
+
+    factors = np.asarray(factor_values, dtype=np.float64).reshape(-1)
+    reps = np.asarray(representations, dtype=np.float64)
+    if reps.ndim != 2 or len(factors) != len(reps):
+        raise ValueError("factor_values and representations must align")
+
+    unique = np.sort(np.unique(factors))
+    centroids = np.stack([reps[factors == value].mean(axis=0) for value in unique])
+    d_ref = pairwise_factor_distance(unique)
+    if metric == "euclidean":
+        d_rep = euclidean_distance_matrix(centroids)
+    elif metric == "fisher_rao":
+        d_rep = pairwise_fisher_rao(centroids)
+    else:
+        raise ValueError("metric must be 'euclidean' or 'fisher_rao'")
+    rho, _ = distance_order_correlation(d_ref, d_rep)
+    return {
+        "rho": float(rho),
+        "stress": float(normalized_stress(d_ref, d_rep)),
+        "factor_count": int(len(unique)),
+    }
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/tests/test_geometry.py /mnt/data/geometry-mmalls-g1-v103/tests/test_geometry.py
--- /mnt/data/geometry-mmalls-g1-v102/tests/test_geometry.py	2026-06-13 21:58:03.597481470 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/tests/test_geometry.py	2026-06-13 22:34:10.731983468 +0000
@@ -7,6 +7,7 @@
     pairwise_fisher_rao,
     procrustes_aligned_drift,
     route_geodesic_loss,
+    paired_route_geometry_loss,
 )
 
 
@@ -57,3 +58,25 @@
     loss.backward()
     assert logits.grad is not None
     assert torch.isfinite(logits.grad).all()
+
+
+
+def test_paired_route_geometry_loss_has_finite_backward():
+    logits = torch.randn(8, 5, 4, requires_grad=True)
+    routes = torch.softmax(logits, dim=-1)
+    factors = torch.tensor([-60.0, -30.0, 0.0, 30.0, 60.0])
+    loss = paired_route_geometry_loss(routes, factors)
+    assert torch.isfinite(loss)
+    loss.backward()
+    assert logits.grad is not None
+    assert torch.isfinite(logits.grad).all()
+
+
+def test_paired_route_geometry_single_angle_is_zero():
+    logits = torch.randn(3, 1, 4, requires_grad=True)
+    routes = torch.softmax(logits, dim=-1)
+    loss = paired_route_geometry_loss(routes, torch.tensor([0.0]))
+    assert torch.isfinite(loss)
+    assert float(loss.detach()) == 0.0
+    loss.backward()
+    assert logits.grad is not None
diff -ruN '--exclude=*.pdf' '--exclude=*.png' '--exclude=*.jpg' '--exclude=*.zip' '--exclude=.pytest_cache' '--exclude=__pycache__' '--exclude=*.pyc' /mnt/data/geometry-mmalls-g1-v102/tests/test_metrics.py /mnt/data/geometry-mmalls-g1-v103/tests/test_metrics.py
--- /mnt/data/geometry-mmalls-g1-v102/tests/test_metrics.py	2026-06-13 18:04:56.000000000 +0000
+++ /mnt/data/geometry-mmalls-g1-v103/tests/test_metrics.py	2026-06-13 22:34:10.733078164 +0000
@@ -6,6 +6,9 @@
     neighborhood_preservation,
     pairwise_factor_distance,
     route_entropy,
+    bootstrap_mean_ci,
+    grouped_geometry_scores,
+    centroid_geometry_scores,
 )
 
 
@@ -33,3 +36,16 @@
     ent = route_entropy(routes)
     assert ent[0] < 1e-8
     assert np.isclose(ent[1], 1.0)
+
+
+
+def test_grouped_geometry_scores_preserve_exact_source_order():
+    factors = np.tile(np.array([-30.0, 0.0, 30.0]), 5)
+    groups = np.repeat(np.arange(5), 3)
+    representations = factors[:, None]
+    result = grouped_geometry_scores(factors, representations, groups)
+    assert np.nanmean(result["rho"]) > 0.999
+    mean, low, high = bootstrap_mean_ci(result["rho"], samples=100, seed=3)
+    assert low > 0.99 and high <= 1.000001
+    centroid = centroid_geometry_scores(factors, representations)
+    assert centroid["rho"] > 0.999
