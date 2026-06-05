from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA, FactorAnalysis
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
from utils import load_primary, make_model_matrix, CHANNELS, ensure_out

out = ensure_out()
df = load_primary()
X, _, _ = make_model_matrix(df, CHANNELS)

pca = PCA().fit(X)
pca_table = pd.DataFrame({
    'component': np.arange(1, X.shape[1]+1),
    'explained_variance': pca.explained_variance_,
    'explained_variance_ratio': pca.explained_variance_ratio_,
    'cumulative_variance_ratio': np.cumsum(pca.explained_variance_ratio_)
})
pca_table.to_csv(out / 'tables' / 'pca_results_reproduced.csv', index=False)

# Basic FA CV log-likelihood. This is not identical to the Kosmos run but provides a transparent baseline.
groups = (df['study'].astype(str)+'_'+df['subject_id'].astype(str)+'_'+df['session_name'].astype(str)).to_numpy()
gkf = GroupKFold(n_splits=5)
rows = []
for n in range(1, 7):
    fold_ll = []
    for tr, te in gkf.split(X, groups=groups):
        scaler = StandardScaler().fit(X[tr])
        Xtr = scaler.transform(X[tr])
        Xte = scaler.transform(X[te])
        fa = FactorAnalysis(n_components=n, random_state=0).fit(Xtr)
        fold_ll.append(float(fa.score(Xte)))
    rows.append({'n_factors': n, 'cv_ll_per_sample_mean': float(np.mean(fold_ll)), 'cv_ll_per_sample_sd': float(np.std(fold_ll))})
pd.DataFrame(rows).to_csv(out / 'tables' / 'factor_analysis_cv_reproduced.csv', index=False)
print('Wrote PCA and FA baseline tables to reproduced_outputs/tables')
