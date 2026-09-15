#!/usr/bin/env python3
import numpy as np

# Historical Q-B1828A global residue-rank data.
n = np.array([6, 26, 106], dtype=int)
r2 = np.array([10, 50, 210], dtype=int)
r4 = np.array([20, 100, 420], dtype=int)

checks = {}
checks['global_R2_extensive'] = np.array_equal(r2, 2*(n-1))
checks['global_R4_extensive'] = np.array_equal(r4, 4*(n-1))
checks['global_type_ratio_fixed'] = np.array_equal(r4, 2*r2)

# Q-B1828D/E local closed form:
# Sigma_T(z) = m a^2 [1/(z-3) + 2/(z-4.25)] P_T,
# rank(P_T)=2. Build an explicit fixed four-state realization.
boundary_dim = 4
U = np.zeros((boundary_dim, 2), dtype=complex)
U[0,0] = 1.0
U[1,1] = 1.0
P = U @ U.conj().T

m = 2.0
a = 0.031
q = m*a*a
A = np.block([
    [3.0*np.eye(2), np.zeros((2,2))],
    [np.zeros((2,2)), 4.25*np.eye(2)]
]).astype(complex)
B = np.vstack([np.sqrt(q)*U.conj().T, np.sqrt(2*q)*U.conj().T])
C = np.hstack([np.sqrt(q)*U, np.sqrt(2*q)*U])

zs = [2.0+0.7j, 5.1+0.3j, -1.2+1.1j]
max_transfer_res = 0.0
for z in zs:
    transfer = C @ np.linalg.inv(z*np.eye(4)-A) @ B
    target = q*(1/(z-3.0) + 2/(z-4.25))*P
    max_transfer_res = max(max_transfer_res, float(np.linalg.norm(transfer-target)))

Ctr = np.hstack([B, A@B])
Obs = np.vstack([C, C@A])
ctr_rank = np.linalg.matrix_rank(Ctr, tol=1e-12)
obs_rank = np.linalg.matrix_rank(Obs, tol=1e-12)

checks['fixed_4_state_realization_exact'] = max_transfer_res < 1e-12
checks['realization_controllable_rank4'] = ctr_rank == 4
checks['realization_observable_rank4'] = obs_rank == 4
checks['local_mcmillan_degree4'] = ctr_rank == obs_rank == 4

print('n', n.tolist())
print('R2 ranks', r2.tolist(), 'expected', (2*(n-1)).tolist())
print('R4 ranks', r4.tolist(), 'expected', (4*(n-1)).tolist())
print('max transfer residual', max_transfer_res)
print('controllability rank', ctr_rank)
print('observability rank', obs_rank)
for name, ok in checks.items():
    print('PASS' if ok else 'FAIL', name)
print('TOTAL', sum(checks.values()), '/', len(checks), 'PASS')

if not all(checks.values()):
    raise SystemExit(1)
