from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
RESULTS_DIR = DATA_DIR / 'model_results'
FIG_DIR = ROOT / 'figures'
OUT_DIR = ROOT / 'reproduced_outputs'
CHANNELS = ['usv22_call_count_5s', 'usv50_call_count_5s', 'leverpress_count_5s', 'freezing_pct_5s']
COUNT_CHANNELS = ['usv22_call_count_5s', 'usv50_call_count_5s', 'leverpress_count_5s']


def ensure_out():
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / 'figures').mkdir(exist_ok=True)
    (OUT_DIR / 'tables').mkdir(exist_ok=True)
    return OUT_DIR


def load_full() -> pd.DataFrame:
    path = DATA_DIR / 'analysis_ready' / 'TRP_analysis_ready_full_multimodal_v6.csv'
    df = pd.read_csv(path, dtype={'study': str})
    if 'four_channel_complete' not in df.columns:
        df['four_channel_complete'] = df[CHANNELS].notna().all(axis=1)
    return df


def load_primary() -> pd.DataFrame:
    path = DATA_DIR / 'analysis_ready' / 'TRP_analysis_ready_primary_complete_four_channel.csv'
    return pd.read_csv(path, dtype={'study': str})


def make_model_matrix(df: pd.DataFrame, channels=CHANNELS):
    x = df.loc[:, channels].copy()
    for c in COUNT_CHANNELS:
        if c in x.columns:
            x[c] = np.log1p(x[c].astype(float))
    # Freezing is already percentage; z-score each channel.
    arr = x.astype(float).to_numpy()
    mean = np.nanmean(arr, axis=0)
    sd = np.nanstd(arr, axis=0)
    sd[sd == 0] = 1.0
    z = (arr - mean) / sd
    return z, mean, sd


def subject_session_lengths(df: pd.DataFrame) -> list[int]:
    return [len(g) for _, g in df.groupby(['study','subject_id','session_name'], sort=False)]


def write_json(obj, path):
    path = Path(path)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)
