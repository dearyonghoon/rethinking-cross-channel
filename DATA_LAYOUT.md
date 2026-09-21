# Data Layout

The notebooks search several common local paths and can be adapted with `tools/patch_paths.py`.
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

Some notebooks also recognize common aliases such as:

- `ECL/electricity.csv`
- `Solar/solar_AL.txt`
- dataset-specific subdirectories such as `PEMS03/PEMS03.npz`

The datasets are standard public benchmarks and are not redistributed in this supplementary archive.

## Time-Series-Library

Place a Time-Series-Library checkout at a convenient location, e.g.

```text
/workspace/Time-Series-Library/
```

and either edit the notebook path cell or run:

```bash
python tools/patch_paths.py \
  --project-root /workspace/iclr27 \
  --data-root /workspace/datasets \
  --tslib-root /workspace/Time-Series-Library
```

The neural notebooks import model implementations directly from that checkout.
