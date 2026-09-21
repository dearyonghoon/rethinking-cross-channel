# Result-to-Code Map

| Experimental component | Primary artifact(s) |
|---|---|
| Observed dependency drift | `notebooks/01_dependency_drift/PeMS_Horizon_Dependency_Drift_ICLR27_v2.ipynb`; `CrossDomain_Horizon_Dependency_Drift_ICLR27_v2.ipynb` |
| Ridge controlled Shared vs Adaptive utility | `notebooks/02_controlled_utility/PeMS03_04_07_08_History12_HorizonSpecific.ipynb`; `Predictive_Dependency_Drift_ICLR27.ipynb`; `When_Does_HorizonAdaptive_ChannelSelection_Help_ICLR27.ipynb` |
| Nonlinear controlled-predictor confirmation | `notebooks/02_controlled_utility/Nonlinear_Controlled_MLP_Shared_vs_Adaptive_FULL_ICLR27.ipynb`; `frozen_results/nonlinear_mlp_*` |
| Temporal-stability diagnostic | `notebooks/03_temporal_selection/Rolling_Temporal_Stability_Gate_ICLR27.ipynb` |
| Phase-1 neural backbone benchmark | `notebooks/04_neural_backbones/External_Baseline_Benchmark_Phase1_ModelOnly_ICLR27_v5.ipynb` |
| Complete iTransformer hard-mask transfer | `notebooks/05_transfer_mechanisms/iTransformer_Explicit_Sparse_HorizonSpecific_ChannelMask_All20_ICLR27.ipynb`; `frozen_results/hardmask_all20_*` |
| Softer horizon-conditioning mechanisms | Remaining notebooks in `notebooks/05_transfer_mechanisms/` |
| Grouped source-history permutation | `notebooks/06_functional_reliance/iTransformer_Channel_Information_Permutation_Test_ICLR27.ipynb` |
| Dependency / utility / neural-reliance alignment | `notebooks/06_functional_reliance/Dependency_PredictiveUtility_NeuralImportance_ICLR27.ipynb` |
| Same-checkpoint future-offset reliance | `notebooks/07_robustness_reliability/SameCheckpoint_H720_PerOffset_EPI_ICLR27.ipynb`; `frozen_results/same_checkpoint_*` |
| Utility metric / candidate-pool robustness | `notebooks/07_robustness_reliability/Final_Robustness_ForecasterSpecific_SourceReliance_ICLR27.ipynb` |
| EPI reliability | `notebooks/07_robustness_reliability/Expected_Permutation_Importance_Reliability_ICLR27.ipynb` |
| TimesNet confirmation | `notebooks/07_robustness_reliability/TimesNet_StrongBackbone_EPI_Confirmatory_ICLR27.ipynb` |
| Multi-probe predictive utility | `notebooks/08_additional_controls/Exp4_MultiProbe_PredictiveUtility_Ridge_vs_MLP_ICLR27.ipynb`; `frozen_results/multiprobe_predictive_utility_summary.csv` |
| TimeMixer-XC functional reliance | `notebooks/08_additional_controls/Exp5_ThirdArchitecture_TimeMixer_CrossChannel_EPI_ICLR27.ipynb`; `frozen_results/timemixer_functional_reliance_summary.csv`; `three_forecaster_epi_alignment_summary.csv` |
| High-dimensional target/candidate sensitivity | `notebooks/08_additional_controls/Exp6_HighDim_TargetSubset_CandidateCap_Robustness_ICLR27.ipynb`; `Exp6_PooledMetric_Reanalysis_ICLR27.ipynb`; `frozen_results/highdim_*` |
| Bounded predictive support | `notebooks/09_bounded_support/01_temporal_calibration_safe_support.ipynb`; `02_five_seed_four_horizon_validation.ipynb`; `03_locked_one_shot_test.ipynb`; `frozen_results/bounded_support/test_condition_mse.csv`; `hierarchical_bootstrap.csv`; `locked_test_decision.json` |

The auxiliary grouped predictive-bias result is retained as `frozen_results/internal_horizon_grouped_predictive_bias_results.csv`; its original execution notebook was not present in the retained source snapshot, so no reconstructed code is presented as original experimental code.
