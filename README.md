# Synthetic evaluation artifacts and frozen models

Supplementary data for the manuscript by Park and Park on lactate-state estimation from cycling cardiopulmonary exercise tests.

This repository holds the stored outputs of the synthetic final evaluation and the 21 frozen model files evaluated in the paper. It does not contain training or evaluation code, the synthetic-data generator, or any human participant data. Models estimate a synthetic generator lactate state, not clinical blood lactate.

## Contents

- `synthetic-evaluation/` – evaluation cases (8), per-unit predictions and receipts (168), summary tables, preprocessing and generation records, and a manifest with SHA-256 hashes.
- `models/` – 21 model files: GRU, causal TCN and MLP (6 each, `.pt`) and HGB (3, `.joblib`), with `checkpoint-index.json` listing the SHA-256 of each file.

## Verification

```
python3 synthetic-evaluation/verify_bundle.py
```

The script checks archived bytes against `MANIFEST.json` and the 48 manuscript Table 6 cells recorded in `VALIDATION.json`. It never runs training or inference.

Four generation and preprocessing JSON files had the absolute local path prefix of the original run replaced with `<local>`. Their manifest entries are marked `sanitized`, and the stored hash refers to the sanitized bytes. All other files are byte-identical to the originals.

## Using the models

The model files alone do not provide the preprocessing configuration or input data needed for inference. `.joblib` files use pickle; load serialized models only from a source you trust, and compare each file with the hash in `models/checkpoint-index.json` first.

## License

Creative Commons Attribution 4.0 International (see `LICENSE`).
