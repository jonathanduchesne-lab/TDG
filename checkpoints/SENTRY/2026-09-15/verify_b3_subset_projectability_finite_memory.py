#!/usr/bin/env python3
import itertools
import numpy as np

labels = range(4)
rng = np.random.default_rng(20260915)

# Generic vector-valued primitive pair response table. No symmetry or GR target is used.
Phi = {(s, h): rng.normal(size=7) for s in labels for h in labels if s != h}

def future_law(history, h):
    S = frozenset(history)
    return sum((Phi[(s, h)] for s in S), np.zeros(7))

ordered_counts = []
subset_counts = []
max_same_subset_defect = 0.0

for k in range(5):
    histories = list(itertools.permutations(labels, k)) if k else [()]
    ordered_counts.append(len(histories))
    classes = {}
    for hist in histories:
        classes.setdefault(frozenset(hist), []).append(hist)
    subset_counts.append(len(classes))

    for S, hs in classes.items():
        for h in labels:
            if h in S:
                continue
            vals = [future_law(hist, h) for hist in hs]
            for v in vals[1:]:
                max_same_subset_defect = max(
                    max_same_subset_defect,
                    float(np.linalg.norm(v - vals[0])),
                )

# Exact relabel covariance: relabel the carrier and primitive table together.
p = {0: 2, 1: 0, 2: 3, 3: 1}
Phi_p = {(p[s], p[h]): v.copy() for (s, h), v in Phi.items()}

def future_law_p(history, h):
    S = frozenset(history)
    return sum((Phi_p[(s, h)] for s in S), np.zeros(7))

max_covariance_defect = 0.0
for k in range(5):
    histories = list(itertools.permutations(labels, k)) if k else [()]
    for hist in histories:
        S = set(hist)
        for h in labels:
            if h in S:
                continue
            relabeled_history = tuple(p[x] for x in hist)
            max_covariance_defect = max(
                max_covariance_defect,
                float(np.linalg.norm(
                    future_law(hist, h)
                    - future_law_p(relabeled_history, p[h])
                )),
            )

checks = {
    "ordered_prefix_counts": ordered_counts == [1, 4, 12, 24, 24],
    "subset_state_counts": subset_counts == [1, 4, 6, 4, 1],
    "total_subset_states_16": sum(subset_counts) == 16,
    "same_subset_future_law_exact": max_same_subset_defect < 1e-14,
    "relabel_covariance_exact": max_covariance_defect < 1e-14,
}

print("ordered_prefix_counts", ordered_counts)
print("subset_state_counts", subset_counts, "total", sum(subset_counts))
print("max_same_subset_defect", max_same_subset_defect)
print("max_relabel_covariance_defect", max_covariance_defect)
for name, ok in checks.items():
    print("PASS" if ok else "FAIL", name)
print("TOTAL", sum(checks.values()), "/", len(checks), "PASS")

if not all(checks.values()):
    raise SystemExit(1)
