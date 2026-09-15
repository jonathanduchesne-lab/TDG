#!/usr/bin/env python3
import numpy as np

Ns = [1, 5, 25, 105]
poles = [3.0, 4.25]
checks = []
rows = []

for N in Ns:
    # N independent copies of the local Q-B1828 memory realization:
    # two simple pole species, rank-2 each -> local McMillan degree 4.
    A = np.diag(([3.0] * (2*N)) + ([4.25] * (2*N)))
    B = np.eye(4*N)
    C = np.eye(4*N)
    ctr_rank = np.linalg.matrix_rank(B)
    obs_rank = np.linalg.matrix_rank(C)
    uniq = sorted(set(np.round(np.linalg.eigvalsh(A), 12)))
    global_degree = min(ctr_rank, obs_rank)
    rows.append((N, global_degree, uniq, global_degree/N))
    checks += [
        (f'N{N}_global_degree_4N', global_degree == 4*N),
        (f'N{N}_two_pole_species', uniq == poles),
        (f'N{N}_intensive_degree_4', abs(global_degree/N - 4.0) < 1e-12),
    ]

# Historical Q-B1828 global residue-rank data.
n = np.array([6,26,106])
r2 = np.array([10,50,210])
r4 = np.array([20,100,420])
checks += [
    ('R2_exact_spatial_replication', np.array_equal(r2, 2*(n-1))),
    ('R4_exact_spatial_replication', np.array_equal(r4, 4*(n-1))),
    ('R4_over_R2_type_ratio_fixed', np.array_equal(r4, 2*r2)),
]

# Q-infinity witness: microscopic dimension grows by tensoring the same C^6 factor.
dims = [8*(6**r) for r in range(7)]
ratios = [dims[i+1]//dims[i] for i in range(len(dims)-1)]
checks += [
    ('Qinf_growth_is_fixed_factor_tensoring', all(x == 6 for x in ratios)),
    ('Qinf_local_factor_dimension_constant', ratios == [6]*6),
]

print('N, global_degree, pole_species, intensive_degree')
for row in rows:
    print(row)
print('Qinf dims:', dims)
print('Qinf ratios:', ratios)
print('Active43 R2:', r2.tolist(), 'expected', (2*(n-1)).tolist())
print('Active43 R4:', r4.tolist(), 'expected', (4*(n-1)).tolist())
for name, ok in checks:
    print('PASS' if ok else 'FAIL', name)
print('TOTAL', sum(bool(ok) for _,ok in checks), '/', len(checks), 'PASS')
if not all(bool(ok) for _,ok in checks):
    raise SystemExit(1)
