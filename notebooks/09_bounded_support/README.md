# Bounded Predictive Support

This directory contains the validation and locked-test notebooks for the constructive experiment reported in Appendix D.7.

The method begins with a frozen channel-independent PatchTST predictor. A lightweight residual support module attends across channel latents at each patch and proposes a bounded correction in normalized output space. Correction strength is estimated from a chronologically held-out calibration region and is frozen before evaluation.

## Recommended order

1. `01_temporal_calibration_safe_support.ipynb` develops the chronological calibration protocol without constructing the test split.
2. `02_five_seed_four_horizon_validation.ipynb` runs the locked 4-dataset x 4-horizon x 5-seed validation factorial and writes the frozen calibration manifest.
3. `03_locked_one_shot_test.ipynb` consumes the frozen checkpoints and calibration manifest for the single test evaluation. It writes a completion marker and reloads the sealed results on subsequent execution.

The notebooks use the `Forecast-JEPA` kernel metadata. Set `FORECAST_PROJECT_ROOT` to the experiment workspace and `TSLIB_ROOT` to a Time-Series-Library checkout containing `models/PatchTST.py`. Dataset discovery follows the conventions in the archive-level `DATA_LAYOUT.md`.

## Protocol safeguards

- Architecture, optimizer settings, seeds, calibration rules, and the primary endpoint are fixed before test evaluation.
- Calibration uses chronological training subregions; no test-conditioned correction strength or test oracle is used.
- The primary comparison is `CrossFitSafe` versus the frozen channel-independent predictor.
- `NaturalSupport`, `CalGlobal`, and `CalChannelShrink` are descriptive ablations.
- The test phase is closed after the one-shot evaluation; no post-test method switching or tuning is permitted.

## Frozen summaries

The corresponding files in `frozen_results/bounded_support/` provide the condition-level test MSE table, hierarchical bootstrap summary, and sealed decision record. These summaries permit direct verification of the manuscript values without rerunning model inference.

Notebook outputs and execution counters are intentionally cleared in this distribution. This avoids embedding machine-specific paths while leaving all executable cells and frozen result artifacts intact.
