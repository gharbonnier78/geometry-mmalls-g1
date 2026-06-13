# Status

## Current release: v1.0.3 protocol correction

The accepted claim remains **C0 pipeline and protocol implementation only**.

v1.0.2 repaired numerical stability but its development run used one angle per
geometry batch. Therefore the loss never observed cross-angle pairs and the run
was non-diagnostic for grounded angular geometry.

v1.0.3 introduces a same-source cross-angle paired protocol. It is designed to
make C1-C4 measurable, but no gate is considered passed until the notebook is
run with frozen thresholds, multiple seeds, matched controls and archived
results.

The primary notebook is:

`notebooks/Geometry_MMALS_G1_CrossAngle_Paired_v1_0_3.ipynb`

The archived change report is:

`docs/reports/Geometry_MMALS_G1_v1_0_3_Protocol_Correction_Report.pdf`
