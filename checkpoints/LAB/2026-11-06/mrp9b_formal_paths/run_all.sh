#!/bin/sh
set -eu
cd "$(dirname "$0")"
: "${TDG_Q1852_SOURCE:?Set TDG_Q1852_SOURCE to the original qb1852_full_refined.py with its deps/}"
python3 verify_mrp9b_formal_descent.py > formal_execution.log 2>&1
python3 verify_mrp9b_b4_b24_moment_source.py > b4_b24_execution.log 2>&1
python3 verify_b2_return_paths.py > b2_path_execution.log 2>&1
python3 verify_fresh_sink_counterfactual.py > fresh_sink_execution.log 2>&1
python3 verify_q_native_record_isometry.py > record_isometry_execution.log 2>&1
python3 test_gamma_effect_on_l2l1.py > l2l1_execution.log 2>&1
python3 build_summary.py > summary_execution.log 2>&1
printf 'TDG Q1852 MRP9B FORMAL PATHS: ALL EXPERIMENTS COMPLETED\n'
