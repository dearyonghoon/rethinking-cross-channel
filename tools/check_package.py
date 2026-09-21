#!/usr/bin/env python3
"""Integrity and anonymization checks for the anonymous supplementary archive."""

import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

EXPECTED = [
    "notebooks/01_dependency_drift/PeMS_Horizon_Dependency_Drift_ICLR27_v2.ipynb",
    "notebooks/01_dependency_drift/CrossDomain_Horizon_Dependency_Drift_ICLR27_v2.ipynb",
    "notebooks/02_controlled_utility/PeMS03_04_07_08_History12_HorizonSpecific.ipynb",
    "notebooks/02_controlled_utility/Predictive_Dependency_Drift_ICLR27.ipynb",
    "notebooks/02_controlled_utility/When_Does_HorizonAdaptive_ChannelSelection_Help_ICLR27.ipynb",
    "notebooks/02_controlled_utility/Nonlinear_Controlled_MLP_Shared_vs_Adaptive_FULL_ICLR27.ipynb",
    "notebooks/03_temporal_selection/Rolling_Temporal_Stability_Gate_ICLR27.ipynb",
    "notebooks/04_neural_backbones/External_Baseline_Benchmark_Phase1_ModelOnly_ICLR27_v5.ipynb",
    "notebooks/05_transfer_mechanisms/iTransformer_Explicit_Sparse_HorizonSpecific_ChannelMask_All20_ICLR27.ipynb",
    "notebooks/05_transfer_mechanisms/iTransformer_HorizonGated_DependencyMixture_ICLR27.ipynb",
    "notebooks/05_transfer_mechanisms/iTransformer_Sparse_HorizonQuery_CrossChannel_Attention_ICLR27.ipynb",
    "notebooks/05_transfer_mechanisms/iTransformer_LastBlock_HorizonGrouped_QueryAdapter_ICLR27.ipynb",
    "notebooks/06_functional_reliance/iTransformer_Channel_Information_Permutation_Test_ICLR27.ipynb",
    "notebooks/06_functional_reliance/Dependency_PredictiveUtility_NeuralImportance_ICLR27.ipynb",
    "notebooks/07_robustness_reliability/SameCheckpoint_H720_PerOffset_EPI_ICLR27.ipynb",
    "notebooks/07_robustness_reliability/Final_Robustness_ForecasterSpecific_SourceReliance_ICLR27.ipynb",
    "notebooks/07_robustness_reliability/Expected_Permutation_Importance_Reliability_ICLR27.ipynb",
    "notebooks/07_robustness_reliability/TimesNet_StrongBackbone_EPI_Confirmatory_ICLR27.ipynb",
    "notebooks/09_bounded_support/01_temporal_calibration_safe_support.ipynb",
    "notebooks/09_bounded_support/02_five_seed_four_horizon_validation.ipynb",
    "notebooks/09_bounded_support/03_locked_one_shot_test.ipynb",
    "frozen_results/internal_horizon_grouped_predictive_bias_results.csv",
    "frozen_results/hardmask_all20_variant_results.csv",
    "frozen_results/hardmask_all20_paired_summary.csv",
    "frozen_results/hardmask_all20_aggregate_summary.csv",
    "frozen_results/nonlinear_mlp_full_condition_summary.csv",
    "frozen_results/nonlinear_mlp_seed_stability_summary.csv",
    "frozen_results/nonlinear_mlp_aggregate_summary.csv",
    "frozen_results/same_checkpoint_cross_offset_epi_stability_summary.csv",
    "frozen_results/same_checkpoint_offset_P_vs_EPI_alignment_summary.csv",
    "frozen_results/bounded_support/test_condition_mse.csv",
    "frozen_results/bounded_support/hierarchical_bootstrap.csv",
    "frozen_results/bounded_support/locked_test_decision.json",
]

CSV_EXPECTED_ROWS = {
    "frozen_results/hardmask_all20_variant_results.csv": 60,
    "frozen_results/hardmask_all20_paired_summary.csv": 20,
    "frozen_results/hardmask_all20_aggregate_summary.csv": 1,
    "frozen_results/nonlinear_mlp_full_condition_summary.csv": 32,
    "frozen_results/nonlinear_mlp_seed_stability_summary.csv": 3,
    "frozen_results/nonlinear_mlp_aggregate_summary.csv": 2,
    "frozen_results/same_checkpoint_cross_offset_epi_stability_summary.csv": 6,
    "frozen_results/same_checkpoint_offset_P_vs_EPI_alignment_summary.csv": 4,
    "frozen_results/bounded_support/test_condition_mse.csv": 16,
    "frozen_results/bounded_support/hierarchical_bootstrap.csv": 20,
}


def main():
    failures = []

    for rel in EXPECTED:
        if not (ROOT / rel).exists():
            failures.append("missing: " + rel)

    notebooks = sorted((ROOT / "notebooks").rglob("*.ipynb"))
    for p in notebooks:
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append("invalid notebook JSON: %s (%s)" % (p.relative_to(ROOT), exc))

    for rel, expected_rows in CSV_EXPECTED_ROWS.items():
        p = ROOT / rel
        if not p.exists():
            continue
        try:
            rows = len(pd.read_csv(p))
            if rows != expected_rows:
                failures.append("unexpected CSV row count: %s (%d != %d)" % (rel, rows, expected_rows))
        except Exception as exc:
            failures.append("invalid CSV: %s (%s)" % (rel, exc))

    # Conservative patterns for common double-blind identity leaks.
    patterns = {
        "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
        "home path": re.compile(r"/(?:home|Users)/[^/\s\"']+"),
        "personal github path": re.compile(r"github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", re.I),
        "user-specific data path": re.compile(r"/data/[A-Za-z][A-Za-z0-9_.-]{3,}/(?:code|src|project|workspace|repo|repos)/"),
        "Korean text": re.compile(r"[\uac00-\ud7a3]"),
        "assistant trace": re.compile(
            "|".join(
                (
                    "Chat" + "GPT",
                    "Open" + "AI",
                    "Clau" + "de",
                    "Gem" + "ini",
                    r"AI[ -]?assi" + "stant",
                    "user " + "asked",
                    "conversation " + "transcript",
                )
            ),
            re.I,
        ),
    }

    text_suffixes = {".md", ".txt", ".csv", ".yml", ".yaml", ".py", ".ipynb"}
    text_files = [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in text_suffixes]
    for p in text_files:
        text = p.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in patterns.items():
            for match in pattern.finditer(text):
                if label == "personal github path" and match.group(0).lower().startswith("github.com/thuml/time-series-library"):
                    continue
                failures.append("possible %s in %s: %s" % (label, p.relative_to(ROOT), match.group(0)))
                break

    print("notebooks:", len(notebooks))
    print("expected artifacts:", len(EXPECTED))
    print("frozen CSV checks:", len(CSV_EXPECTED_ROWS))
    if failures:
        print("CHECK FAILED")
        for item in failures:
            print(" -", item)
        raise SystemExit(1)
    print("CHECK PASSED")


if __name__ == "__main__":
    main()
