# Canonical Four-State Architecture in Multimodal Fear-Goal Arbitration

## Executive Summary

Evidence supports a canonical four-state macro-architecture, not exactly four empirical micro-states.

Discrete sequence models strongly outperform continuous latent factor baselines. The best statistical fit continues improving up to K=8, but higher-K models coarse-grain into the same four biological modes: Quiescent/Baseline, Safety/Appetitive, Fear/Distress, and Goal-directed behavior.

The strongest pattern is stable emissions with flexible transitions: state signatures are mostly invariant across studies, while transition matrices reconfigure strongly across conditioning stage, context, and session type.

## Dataset Inclusion Audit

- Total rows: 74,164
- Complete four-channel primary rows: 47,004
- Subjects: 29
- Subject-sessions: 213
- Excluded rows: 27,160, primarily structural missingness from non-recorded modalities; 1,237 rows had missing freezing despite four-channel flag.

Event-derived zeros were treated as informative no-event bins. Freezing zeros were treated as true 0% freezing. No structural missingness was zero-filled.

## Continuous vs. Discrete Models

Discrete HMMs dominate PCA/FA:

- Best HMM (K=5): +31.82 nats/sample
- Best FA (2 components): -5.65 nats/sample
- Gap: ~37 nats/sample

This reflects strong temporal dependencies in the data that i.i.d. factor models cannot capture.

## HMM K-Selection

| K | BIC | CV LL/sample |
|---|-----|--------------|
| 2 | -702,376 | 7.23 +/- 0.45 |
| 3 | -1,389,415 | 14.45 +/- 0.45 |
| 4 | -1,448,118 | 15.07 +/- 0.35 |
| 5 | -1,475,401 | 15.35 +/- 0.30 |
| 6 | -1,499,431 | 15.61 +/- 0.27 |
| 7 | -1,513,793 | 15.36 +/- 0.66 |
| 8 | -1,521,522 | 15.70 +/- 0.22 |

BIC decreases monotonically. K=8 is the empirical winner in the diagonal-covariance sweep. K=4 captures 96% of optimal CV LL and remains the theory-relevant macro-state model.

## K=4 State Signatures

| State | Label | Occupancy | USV22 | USV50 | Lever | Freezing |
|-------|-------|-----------|-------|-------|-------|----------|
| 0 | Quiescent/Baseline | 81.7% | ~0 | ~0 | ~0 | 35.6% |
| 1 | Safety/Appetitive | 8.0% | ~0 | 0.91 | ~0 | 21.1% |
| 2 | Danger/Fear | 7.8% | 2.33 | 0.79 | ~0 | 67.7% |
| 3 | Goal-directed | 2.5% | 0.01 | 0.13 | 1.00 | 31.8% |

## Robustness

- 100 random initializations for K=4.
- Top 5 solutions nearly identical: NMI mean 0.999, minimum 0.998.
- Top 20 show multiple local optima; multiple restarts are essential.
- Leave-one-subject-out validation: 29/29 subjects and 213/213 sessions show K=4 HMM > K=1 baseline.

## Context and Stage-Dependent Transition Reconfiguration

Emissions are mostly stable across study/session groups (80% of meaningful effects |d| < 0.5). Transitions differ strongly by session type, study, and within-session stage. During learning, Fear/Distress rises from 0% in early deciles to 63.8% in the final decile; during extinction, fear declines; during renewal/retrieval, fear rebounds.

## Conflict State Analysis

No dedicated conflict emission state appears at K=4, K=6, or K=8. Higher-K models split the Fear/Distress state into subtypes, especially mixed-vocalization fear vs. 22-kHz-only fear. Direct Fear-to-Goal transitions are rare (<0.4% of transitions). The Quiescent state acts as a buffer between defensive and appetitive modes.

## HMM vs. HSMM Duration Structure

HSMM-style duration correction improves held-out LL in all fold-K comparisons, but by only +0.019 nats/obs (~0.12%). Duration distributions strongly reject geometric assumptions in all states, with heavy-tailed and overdispersed bouts.

## Count-Aware Diagnostics

The Gaussian-log1p approximation is useful for decoding but imperfect generatively. Negative binomial and zero-inflated negative binomial distributions outperform Poisson for several active state-channel combinations, especially USV50 in the Fear/Distress state and sparse residual USV channels in the Lever state.

## Boli Validation

State occupancy predicts session-level fecal boli better than mean freezing alone. The Fear/Distress state positively predicts boli (beta=1.21, p=1.4e-7), while the Goal-directed state negatively predicts boli (beta=-10.94, p=6.3e-4). This validates the biological interpretation of the HMM states.

## Interpretive Conclusion

The dataset supports a canonical four-state macro-architecture for multimodal fear-goal arbitration. The empirical optimum is finer than four states, but the extra states are subdivisions of the same macro-architecture. Fear-goal conflict is not a stable mixed emission state; it is a transition-level phenomenon shaped by stage, context, and experimental contingencies.

## Key Limitations

- BIC does not plateau; K=8 is best in the diagonal screening sweep.
- Some sweeps used diagonal covariance and fewer random starts for runtime reasons.
- HSMM comparison used post-hoc duration correction, not full HSMM EM.
- Study 1b has sparse USV22 events, weakening distress-state recovery in that sub-cohort.
- Gaussian-log1p emissions are an approximation for sparse counts.
- CS+ vs CS- transition differences were not significant (p=0.19).
