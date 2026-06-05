from __future__ import annotations
import pandas as pd
from utils import load_full, load_primary, CHANNELS, ensure_out, write_json

out = ensure_out()
full = load_full()
primary = load_primary()

summary = {
    'full_rows': int(len(full)),
    'full_subjects': int(full['subject_id'].nunique()),
    'full_subject_sessions': int(full[['study','subject_id','session_name']].drop_duplicates().shape[0]),
    'primary_rows': int(len(primary)),
    'primary_subjects': int(primary['subject_id'].nunique()),
    'primary_subject_sessions': int(primary[['study','subject_id','session_name']].drop_duplicates().shape[0]),
    'channel_missing_counts_full': {c:int(full[c].isna().sum()) for c in CHANNELS},
    'event_zero_proportions_primary': {
        'usv22_call_count_5s': float((primary['usv22_call_count_5s'] == 0).mean()),
        'usv50_call_count_5s': float((primary['usv50_call_count_5s'] == 0).mean()),
        'leverpress_count_5s': float((primary['leverpress_count_5s'] == 0).mean()),
    },
    'freezing_range_primary': [float(primary['freezing_pct_5s'].min()), float(primary['freezing_pct_5s'].max())]
}

pd.DataFrame([summary]).to_csv(out / 'tables' / 'dataset_validation_summary.csv', index=False)
write_json(summary, out / 'tables' / 'dataset_validation_summary.json')
print(summary)
