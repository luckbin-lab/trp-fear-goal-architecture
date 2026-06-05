from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
from utils import load_primary, make_model_matrix, subject_session_lengths, CHANNELS, ensure_out

out = ensure_out()
try:
    from hmmlearn.hmm import GaussianHMM
except Exception as e:
    raise SystemExit('hmmlearn is required for optional HMM refitting. Install with pip install hmmlearn. Error: %s' % e)

df = load_primary()
X_raw, _, _ = make_model_matrix(df, CHANNELS)
lengths = subject_session_lengths(df)
# Fit on globally transformed data for demonstration. The reported manuscript tables are bundled under data/model_results.
rows = []
for k in range(2, 9):
    model = GaussianHMM(n_components=k, covariance_type='diag', n_iter=200, random_state=0, verbose=False)
    model.fit(X_raw, lengths=lengths)
    ll = model.score(X_raw, lengths=lengths)
    n_features = X_raw.shape[1]
    n_params = (k - 1) + k*(k - 1) + k*n_features + k*n_features  # start, trans, means, diag vars
    bic = -2*ll + n_params*np.log(len(X_raw))
    rows.append({'K':k, 'train_log_likelihood': float(ll), 'approx_bic': float(bic), 'n_params_approx': int(n_params)})
pd.DataFrame(rows).to_csv(out / 'tables' / 'hmm_model_selection_optional_refit.csv', index=False)
print('Optional HMM refit complete. Use bundled data/model_results for manuscript values.')
