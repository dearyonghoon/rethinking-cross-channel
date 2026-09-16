# Data Layout

A simple recommended layout is:

```text
<DATA_ROOT>/
├── PeMS03.npz
├── PeMS04.npz
├── PeMS07.npz
├── PeMS08.npz
├── electricity/
│   └── electricity.csv
├── weather/
│   └── weather.csv
├── solar/
│   └── solar_AL.txt
└── ETT-small/
    ├── ETTh1.csv
    └── ETTm1.csv
```

Some notebooks also recognize common aliases such as `ECL/electricity.csv`, `Solar/solar_AL.txt`, and dataset-specific subdirectories such as `PEMS03/PEMS03.npz`.

The datasets are standard public forecasting benchmarks and are not redistributed here.

## Time-Series-Library

Clone [THUML Time-Series-Library](https://github.com/thuml/Time-Series-Library) to a convenient location, for example:

```text
/workspace/Time-Series-Library/
```

Then edit each notebook's configuration cell or run:

```bash
python tools/patch_paths.py \
  --project-root /workspace/rethinking-cross-channel \
  --data-root /workspace/datasets \
  --tslib-root /workspace/Time-Series-Library
```

The neural notebooks import model implementations directly from that checkout.
