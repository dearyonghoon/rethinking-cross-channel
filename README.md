# Rethinking Cross-Channel Importance in Time-Series Forecasting

Official implementation and reproducibility code for **Rethinking Cross-Channel Importance in Time-Series Forecasting**.

## Abstract

Cross-channel modeling is central to multivariate time-series forecasting, yet channels that are statistically related, predictively useful, and actually used by a trained forecaster are often treated as if they defined the same notion of importance. We show that they need not coincide. Cross-channel dependency structures change substantially across future offsets, and horizon-adaptive source selection improves a controlled Ridge predictor in 21 of 32 dataset–prediction-length conditions, with a mean gain of 5.16%. This selected-set signal also transfers to a matched nonlinear predictor. Yet imposing the same horizon-specific source logic on iTransformer yields only 11 of 20 wins and a mean gain of 0.208%, with little alignment between controlled and neural gains. Functional interventions further show that strong forecasters use cross-channel information, while their source-reliance rankings agree little with controlled utility or with one another across iTransformer, TimesNet, and a cross-channel TimeMixer. As a constructive consequence, bounded post-hoc support improves a frozen channel-independent forecaster in 12 of 16 dataset–horizon conditions, with a positive aggregate bootstrap interval. Cross-channel importance should therefore be interpreted relative to the forecasting mechanism and question that define it: **related ≠ useful ≠ used**.

This repository studies three notions that are often conflated as *cross-channel importance* in multivariate time-series forecasting:

> **related ≠ useful ≠ used**

- **Observed dependency:** which channels are statistically associated with a target at a future offset.
- **Controlled predictive utility:** which channels improve a specified controlled predictor.
- **Functional reliance:** which channel histories a fixed trained forecaster relies on under matched interventions.

The repository contains the experiments used to evaluate dependency drift, controlled Ridge and MLP utility, transfer to iTransformer, same-checkpoint functional reliance, TimesNet and cross-channel TimeMixer confirmations, multi-probe utility, high-dimensional robustness, and bounded predictive support under chronological calibration.

## Repository structure

```text
.
├── README.md
├── RESULT_MAP.md
├── DATA_LAYOUT.md
├── requirements.txt
├── environment.yml
├── notebooks/
│   ├── 01_dependency_drift/
│   ├── 02_controlled_utility/
│   ├── 03_temporal_selection/
│   ├── 04_neural_backbones/
│   ├── 05_transfer_mechanisms/
│   ├── 06_functional_reliance/
│   ├── 07_robustness_reliability/
│   ├── 08_additional_controls/
│   └── 09_bounded_support/
├── frozen_results/
└── tools/
```

## Environment

The main executed experiments use Python 3.8.x and PyTorch 2.4.1 with CUDA. The neural-backbone experiments use model implementations from [Time-Series-Library](https://github.com/thuml/Time-Series-Library).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For neural experiments, clone Time-Series-Library separately and install its dependencies.

## Data

The experiments use standard public forecasting datasets: PeMS03, PeMS04, PeMS07, PeMS08, Electricity, Weather, Solar, ETTh1, and ETTm1. Dataset files are not redistributed. See [`DATA_LAYOUT.md`](DATA_LAYOUT.md) for recognized filenames and directory conventions.

## Local paths

Several retained notebooks record the original `/data/...` execution roots. They are not required canonical paths. Edit the configuration cell in a notebook or use:

```bash
python tools/patch_paths.py \
  --project-root /workspace/rethinking-cross-channel \
  --data-root /workspace/datasets \
  --tslib-root /workspace/Time-Series-Library
```

## Reproduction order

The notebooks are organized by experimental stage. A practical order is:

1. `01_dependency_drift`: observed cross-offset dependency drift.
2. `02_controlled_utility`: Shared-vs-Adaptive controlled utility and nonlinear MLP confirmation.
3. `03_temporal_selection`: temporal-stability diagnostic.
4. `04_neural_backbones`: Phase-1 neural checkpoints.
5. `05_transfer_mechanisms`: iTransformer hard-mask and softer matched transfer mechanisms.
6. `06_functional_reliance`: grouped/individual source-history interventions and ranking alignment.
7. `07_robustness_reliability`: same-checkpoint offsets, reliability, and TimesNet confirmation.
8. `08_additional_controls`: multi-probe utility, TimeMixer-XC, and high-dimensional robustness.
9. `09_bounded_support`: chronological calibration, five-seed/four-horizon validation, and the locked one-shot test.

See [`RESULT_MAP.md`](RESULT_MAP.md) for the detailed mapping from findings to notebooks and frozen result files.

## Key reproduction checks

A successful reproduction should recover the main aggregate patterns reported by the code snapshot, up to small floating-point differences:

- Positive cross-offset dependency-drift bootstrap lower bounds in **18/20** general benchmark conditions.
- Controlled Ridge Adaptive > Shared in **21/32** conditions, with mean pooled endpoint-MSE gain about **+5.16%**.
- Matched nonlinear MLP Adaptive > Shared in **19/32** conditions; on the General-20 subset, **13/20**, mean gain about **+2.14%**, with Ridge–MLP gain Spearman about **0.713**.
- Complete iTransformer hard-mask AdaptiveSparse > SharedSparse in **11/20** conditions, mean full-horizon gain about **+0.208%**; controlled Ridge gain vs hard-mask gain Spearman about **0.057**.
- Same-checkpoint H=720 cross-offset EPI rank correlations of approximately **0.148–0.482**, while predictive utility and EPI remain weakly/negatively aligned at the evaluated offsets.
- Median functional-reliance rank correlation about **-0.091** between iTransformer and TimesNet under matched full-MSE interventions.
- Multi-probe Ridge-vs-MLP utility-ranking median Spearman **0.365** over 170 target instances; both probe-specific utilities remain weakly aligned with matched iTransformer EPI.
- TimeMixer-XC has positive grouped all-other effects for **19/19** evaluated targets. Median neural EPI correlations are about **-0.091** (iTransformer–TimesNet), **-0.009** (iTransformer–TimeMixer), and **0.103** (TimesNet–TimeMixer).
- High-dimensional target-subset/candidate-cap analyses show that controlled Adaptive-vs-Shared gains can be protocol-conditioned; the original pooled metric is reproduced within **0.0034 percentage points**.
- In the locked bounded-support evaluation, the pre-specified cross-fitted controller improves **12/16** dataset–horizon cells, and none of the five-seed cell means regresses by more than **0.5%**. Its hierarchical-bootstrap mean MSE gain is **+0.388%**, with 95% CI **[+0.155%, +0.661%]**.

## Frozen results

`frozen_results/` contains compact CSV summaries for fast verification without rerunning every expensive neural experiment. The `bounded_support/` subdirectory contains the condition-level locked-test MSE table, hierarchical-bootstrap summary, and sealed decision record. Executed notebook outputs are retained where available.

## Integrity check

```bash
python tools/check_package.py
```

The checker validates expected artifacts and notebook JSON. `SHA256SUMS.txt` records file-level checksums for the reproducibility snapshot.

## Citation

An arXiv citation will be added when the public manuscript is released.
