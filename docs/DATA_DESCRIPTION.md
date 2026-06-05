# Data Description

## Dataset title

TRP multimodal fear-goal arbitration dataset, version 1.0 open release.

## Experimental scope

The data derive from rat experiments designed to sample behavior across fear acquisition, threat-generalization, long-delay retest, extinction/retention, and renewal. The behavioral channels quantify defensive immobility, aversive vocalization, appetitive vocalization, instrumental goal pursuit, and session-level autonomic output.

## Unit of observation

One row corresponds to one 5-second bin for one subject in one session.

## Primary four-channel model

The primary architecture-discovery analyses use rows where all four primary channels are non-missing:

- 22-kHz USV call count per 5 s
- 50-kHz USV call count per 5 s
- lever-press count per 5 s
- FreezeFrame freezing percentage per 5 s

The complete-case subset is stored in:

`data/analysis_ready/TRP_analysis_ready_primary_complete_four_channel.csv`

## Full harmonized data

The full harmonized dataset is stored in:

`data/analysis_ready/TRP_analysis_ready_full_multimodal_v6.csv`

This file preserves structural missingness and includes modality-recording flags.

## Reconstruction notes

- Freezing was reconstructed from FreezeFrame wide-table exports by extracting the individual animal identifier from row labels rather than cohort/date tokens in file names. This corrected previous key-level conflicts.
- Lever pressing was reconstructed from Graphic State Notation CSV exports as entries into the `rat press` state and aggregated into 5-second integer counts.
- USV call counts were reconstructed from DeepSqueak/Matlab call-level exports using frequency-band filters and source-selection rules documented in the audit files.
- Boli counts are session-level and currently available primarily from structured Study 2 logs.

## Missingness

Missingness is modality-specific and should not be globally imputed. The recording flags (`usv_recorded`, `lever_recorded`, `freezing_recorded`, `boli_recorded`) and audit tables should be used to distinguish structural non-recording from within-session missing values.
