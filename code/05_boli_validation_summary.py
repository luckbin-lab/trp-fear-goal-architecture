from __future__ import annotations
import pandas as pd
from utils import RESULTS_DIR, ensure_out

out = ensure_out()
coeff = pd.read_csv(RESULTS_DIR / 'boli_regression_coefficients.csv')
val = pd.read_csv(RESULTS_DIR / 'boli_validation.csv')
coeff.to_csv(out / 'tables' / 'boli_regression_coefficients_copy.csv', index=False)
# Lightweight summary table.
summary = {
    'n_rows_boli_validation': int(len(val)),
    'coefficients_file': 'data/model_results/boli_regression_coefficients.csv'
}
pd.DataFrame([summary]).to_csv(out / 'tables' / 'boli_validation_summary.csv', index=False)
print(summary)
