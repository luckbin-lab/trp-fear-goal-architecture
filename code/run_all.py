from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def run(script):
    print(f'\n--- Running {script} ---')
    subprocess.check_call([sys.executable, str(HERE / script)])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['figures','validate','baseline','all','refit_hmm'], default='figures')
    args = parser.parse_args()
    if args.mode in ['validate','all','baseline']:
        run('01_validate_and_prepare.py')
    if args.mode in ['baseline','all']:
        run('02_dimensionality_and_fa.py')
    if args.mode in ['figures','all']:
        run('04_make_manuscript_figures.py')
        run('05_boli_validation_summary.py')
    if args.mode == 'refit_hmm':
        run('03_hmm_model_selection_optional.py')
