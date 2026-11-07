#!/bin/sh
set -eu
: "${TDG_Q1852_SOURCE:?Please export full path to authentic qb1852_full_refined.py}"
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
cd "$(dirname "$0")"
python verify_fresh_chiral_octupole.py > execution.log 2>&1
python verify_fullQ_octahedral_refresh.py > fullQ_24_execution.log 2>&1
python verify_tt_uniform_and_limits.py > adversarial_execution.log 2>&1
python verify_adaptive_horizon.py > adaptive_execution.log 2>&1
python verify_selected_trajectories.py > selected_execution.log 2>&1
printf '%s\n' "All five experimental scripts passed; see individual logs."
