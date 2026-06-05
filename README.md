[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20551231.svg)](https://doi.org/10.5281/zenodo.20551231)

# TRP Canonical Four-State Macro-Architecture: Open Data and Code Package

This repository contains the open data, result tables, figures, and reproducibility scripts for the manuscript:

**A canonical four-state macro-architecture governs multimodal fear-goal arbitration across learning and relapse**

The package is intended for OSF, Zenodo, or GitHub release. It supports reproduction of the reported analysis from the cleaned analysis-ready dataset and provides audit files documenting the raw-to-model reconstruction of ultrasonic vocalizations (USVs), freezing, lever pressing, and session-level boli.

## Package contents

```text
TRP_open_data_code_v1/
├── README.md
├── LICENSE_DATA_CC_BY_4.0.txt
├── LICENSE_CODE_MIT.txt
├── CITATION.cff
├── requirements.txt
├── environment.yml
├── code/
│   ├── run_all.py
│   ├── utils.py
│   ├── 01_validate_and_prepare.py
│   ├── 02_dimensionality_and_fa.py
│   ├── 03_hmm_model_selection_optional.py
│   ├── 04_make_manuscript_figures.py
│   └── 05_boli_validation_summary.py
├── data/
│   ├── analysis_ready/
│   │   ├── TRP_analysis_ready_full_multimodal_v6.csv
│   │   ├── TRP_analysis_ready_primary_complete_four_channel.csv
│   │   └── dataset_summary.json
│   ├── channels/
│   ├── audit/
│   └── model_results/
├── figures/
├── reports/
├── docs/
│   ├── data_dictionary.csv
│   ├── DATA_DESCRIPTION.md
│   └── OPEN_DATA_NOTES.md
└── raw/
    └── README_RAW.md
```

## Data overview

The primary analysis file is:

`data/analysis_ready/TRP_analysis_ready_primary_complete_four_channel.csv`

This complete-case file contains rows for which all four primary 5-second behavioral channels are non-missing:

- `usv22_call_count_5s`
- `usv50_call_count_5s`
- `leverpress_count_5s`
- `freezing_pct_5s`

The full harmonized file is:

`data/analysis_ready/TRP_analysis_ready_full_multimodal_v6.csv`

It includes structural missingness flags and session-level boli values where available.

Important encoding rules:

- USV and lever are event-derived count channels. Within sessions where a modality was recorded, `0` means that no event occurred in that 5-second bin. `NaN` means the modality was not recorded or unavailable.
- Freezing is a dense percentage time-series. `0` means true 0% freezing. `NaN` means missing or not recorded.
- Boli is session-level and is used as external physiological validation, not as a 5-second emission channel.

## Reproducibility quick start

Create an environment:

```bash
conda env create -f environment.yml
conda activate trp-open
```

Or with pip:

```bash
pip install -r requirements.txt
```

Run validation and figure regeneration from the bundled result tables:

```bash
python code/run_all.py --mode figures
```

Optional model refitting scripts are included, but the exact Kosmos/HMM run used for the manuscript may require more compute and package versions than the lightweight figure-regeneration workflow. The bundled `data/model_results/` tables are the authoritative result exports for the current manuscript version.

## Main result files

- `reports/TRP_canonical_architecture_report.md`: narrative report from the architecture-validation run.
- `data/model_results/K_selection_BIC_CV.csv`: HMM K-selection results.
- `data/model_results/K4_emission_means.csv`: four macro-state emission means.
- `data/model_results/K4_transition_matrix.csv`: K=4 transition matrix.
- `data/model_results/coarsegraining_mapping.csv`: empirical microstate to macro-state mapping.
- `data/model_results/boli_regression_coefficients.csv`: session-level boli validation.
- `data/model_results/initialization_robustness.csv`: random-initialization robustness.
- `data/model_results/loso_results.csv`: leave-one-subject-out validation.

## Citation

Please cite the manuscript and this repository. A machine-readable `CITATION.cff` file is included.

## Contact

Corresponding author: Bin Yin, School of Psychology, Fujian Normal University. Email to be added before public release.
