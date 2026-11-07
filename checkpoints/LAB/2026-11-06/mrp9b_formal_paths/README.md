# TDG MRP9B — Formal Q paths and fresh-record diagnostic (2026-11-06)

**Research status:** conditional laboratory result; source-Q derived path identity; new fresh-record isometry is a proposed capacity, not an actual Q update or a GR derivation.

Start with `REPORT.md` and `SUMMARY.json`. `SHA256SUMS.txt` records original artefact hashes. `run_all.sh` runs the same numerical trials and rewrites the result files.

## Required archived source

`qb1852_full_refined.py` SHA-256 `ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7` and the original adjacent `deps/` tree. Original Library archive: `/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz`. Set `TDG_Q1852_SOURCE` to point to the extracted original `.py`; the scripts **do not reconstruct this from prose**. NumPy, SciPy, Python 3.10+ required.

Run from a local copy of this directory:

```sh
export TDG_Q1852_SOURCE=/path/to/original/qb1852_full_refined.py
sh run_all.sh
```

## Test files

- `verify_mrp9b_formal_descent.py`: exact Q-B1852 moment expansion and 2-cell kernel descent criterion; finite-z control, not used to derive moment coefficients.
- `verify_mrp9b_b4_b24_moment_source.py`: b4 and b24 full sparse Q-H moment tests for gamma = 0, .5, 1, 2.
- `verify_b2_return_paths.py`: exact matrix comparison with the B4→B3→B2→B3 path class.
- `verify_fresh_sink_counterfactual.py`: unphysical as a fundamental H, useful as a conditional one-way geometry diagnostic.
- `verify_q_native_record_isometry.py`: new local Kraus completion using actual Q B3→B2 V block; genuine finite-dimensional isometry, but not certified as TDG process.
- `test_gamma_effect_on_l2l1.py`: necessary adversarial control in historical Q-B1852 geometry pipeline; shows STF/gradient obstruction survives.
- `build_summary.py`: transcribes the experiment outputs without changing computations.
- `gamma_probe.py`: early exploratory gamma sweep, redundant but retained for completeness.

See `*_results.json` and `*_execution.log` for raw numerical results and logs. GitHub LAB checkpoint only. Root1, Q-B1858L, historical checkpoints and `CURRENT_FRONT_LATEST.md` are unchanged.
