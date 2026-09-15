#!/usr/bin/env python3
import numpy as np

# Six independent Krylov chains. Lengths sum to 42.
# One chain ends after depth 1; five continue to depth 7.
lengths = [2, 8, 8, 8, 8, 8]
N = sum(lengths)
A = np.zeros((N, N), dtype=int)
C = np.zeros((6, N), dtype=int)

start = 0
for i, L in enumerate(lengths):
    # local output sees the first coordinate of each chain
    C[i, start] = 1
    # A shifts basis e_j -> e_{j+1}; observability rows C A^k
    # therefore use superdiagonal so row e_start^T A^k = e_{start+k}^T
    for j in range(L - 1):
        A[start + j, start + j + 1] = 1
    start += L

blocks = []
for k in range(8):
    blocks.append(C @ np.linalg.matrix_power(A, k))
    O = np.vstack(blocks)
    rank = np.linalg.matrix_rank(O)
    print(f"depth{k}: rank={rank}")

ranks = [np.linalg.matrix_rank(np.vstack([C @ np.linalg.matrix_power(A, j) for j in range(k+1)])) for k in range(8)]
expected = [6,12,17,22,27,32,37,42]
checks = []
checks.append(("dimension_42", N == 42))
checks.append(("rank_profile_exact", ranks == expected))
checks.append(("global_saturates_42", ranks[-1] == 42))
checks.append(("finite_nilpotent_memory", np.all(np.linalg.matrix_power(A,8) == 0)))
checks.append(("local_growth_not_unbounded", all(r <= 42 for r in ranks)))

for name, ok in checks:
    print(("PASS" if ok else "FAIL"), name)
print(f"TOTAL {sum(ok for _,ok in checks)}/{len(checks)} PASS")
if not all(ok for _,ok in checks):
    raise SystemExit(1)
