from __future__ import annotations
import shutil
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from utils import RESULTS_DIR, FIG_DIR, OUT_DIR, ensure_out

out = ensure_out()
fig_out = out / 'figures'
# Copy canonical figures from the model run. These are the authoritative figure exports.
for name in ['continuous_vs_discrete_comparison.png','bic_cv_model_selection.png','emission_profiles.png','transition_matrices_by_stage.png','boli_validation.png']:
    src = FIG_DIR / name
    if src.exists():
        shutil.copy(src, fig_out / name)

# Generate a simple compact model-selection figure from bundled CSV.
ks = pd.read_csv(RESULTS_DIR / 'K_selection_BIC_CV.csv')
plt.figure(figsize=(6,4))
plt.plot(ks['K'], ks['CV_LL_mean'], marker='o')
plt.xlabel('Number of HMM states (K)')
plt.ylabel('Grouped CV log-likelihood/sample')
plt.title('HMM model selection')
plt.tight_layout()
plt.savefig(fig_out / 'reproduced_cv_ll_by_K.png', dpi=300)
plt.close()

em = pd.read_csv(RESULTS_DIR / 'K4_emission_means.csv')
plt.figure(figsize=(8,4))
em.set_index('state')[['usv22_count','usv50_count','leverpress_count','freezing_pct']].plot(kind='bar', ax=plt.gca())
plt.ylabel('Emission mean')
plt.title('K=4 macro-state emission signatures')
plt.tight_layout()
plt.savefig(fig_out / 'reproduced_K4_emission_means.png', dpi=300)
plt.close()
print('Figures copied/generated in reproduced_outputs/figures')
