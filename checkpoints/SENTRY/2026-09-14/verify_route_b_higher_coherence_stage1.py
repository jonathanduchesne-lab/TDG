#!/usr/bin/env python3
"""Route B higher-coherence Stage-I algebraic verifier.

Pretarget only. No O(3), HDA, spin-2 or GR target is used.

Checks two generic control theorems used by the 2026-09-14 sentry:

B1. A scalar/central 3-cell on a filled contractible tetrahedral overlap is a
    coboundary: H^3 of that single filled 3-simplex vanishes.
B2. A genuine connected three-event response is invisible on all proper
    one-/two-event faces, but any finite-depth response table can be exactly
    Markovized by a fixed one-event update law on enlarged prefix memory.

These are ontology/identifiability controls. They do not claim that all
non-central or globally topological higher cells are trivial.
"""

from itertools import product
import numpy as np

checks = []


def check(name, cond, detail=""):
    ok = bool(cond)
    checks.append((name, ok, detail))
    print(("PASS" if ok else "FAIL"), name, detail)


# ---------------------------------------------------------------------------
# B1: central scalar local higher cell on one filled 3-simplex
# ---------------------------------------------------------------------------
# Oriented boundary of [0123]: [123] - [023] + [013] - [012].
# For scalar 2-cochains beta on the four triangular faces, d beta is the
# 1-dimensional 3-cochain obtained by this row vector.
d2 = np.array([[1.0, -1.0, 1.0, -1.0]])
rank_d2 = np.linalg.matrix_rank(d2, tol=1e-12)
dim_C3 = 1
H3_dim = dim_C3 - rank_d2

check("B1_filled_simplex_d2_rank_one", rank_d2 == 1, f"rank={rank_d2}")
check("B1_filled_simplex_H3_zero", H3_dim == 0, f"H3_dim={H3_dim}")

# Explicit reconstruction of arbitrary scalar 3-cell k as d beta.
for k in (-3.25, 0.0, 2.0, 7.125):
    beta = np.array([k, 0.0, 0.0, 0.0])
    err = abs(float((d2 @ beta)[0]) - k)
    check(f"B1_scalar_cell_{k}_is_coboundary", err < 1e-12, f"err={err:.3e}")


# ---------------------------------------------------------------------------
# B2a: connected triple response is independent of all proper faces
# ---------------------------------------------------------------------------
# Generic multilinear response on three binary interventions.
a0, ax, ay, az = 2.0, 3.0, -5.0, 7.0
axy, axz, ayz, kxyz = 11.0, -13.0, 17.0, 19.0


def f(x, y, z, k=kxyz):
    return (
        a0 + ax*x + ay*y + az*z
        + axy*x*y + axz*x*z + ayz*y*z + k*x*y*z
    )


def third_difference(fun):
    return (
        fun(1, 1, 1)
        - fun(1, 1, 0)
        - fun(1, 0, 1)
        - fun(0, 1, 1)
        + fun(1, 0, 0)
        + fun(0, 1, 0)
        + fun(0, 0, 1)
        - fun(0, 0, 0)
    )

triple = third_difference(f)
check("B2_connected_triple_recovers_k", abs(triple - kxyz) < 1e-12,
      f"Delta3={triple:.16g}")

# Removing/changing k cannot affect a proper face because xyz=0 there.
max_face_defect = 0.0
for x, y, z in product((0, 1), repeat=3):
    if x*y*z == 0:
        v0 = f(x, y, z, k=0.0)
        v1 = f(x, y, z, k=kxyz)
        max_face_defect = max(max_face_defect, abs(v0-v1))
check("B2_all_proper_faces_blind_to_triple_cell", max_face_defect < 1e-12,
      f"max_defect={max_face_defect:.3e}")


# ---------------------------------------------------------------------------
# B2b: finite-depth response table admits exact prefix-memory dilation
# ---------------------------------------------------------------------------
# Use binary event strings through depth 3. Memory states are all prefixes.
prefixes = [()]
for n in range(1, 4):
    prefixes += list(product((0, 1), repeat=n))
idx = {h: i for i, h in enumerate(prefixes)}
N = len(prefixes)

# Fixed one-event update matrices U_e. They do not depend on time/depth; the
# current prefix memory state carries all finite history dependence.
U = {}
for e in (0, 1):
    M = np.zeros((N, N))
    for h, j in idx.items():
        if len(h) < 3:
            hp = h + (e,)
            M[idx[hp], j] = 1.0
        else:
            # Terminal depth; keep terminal states fixed for this bounded test.
            M[j, j] = 1.0
    U[e] = M

# Readout only at depth 3. Interpret h=(x,y,z).
r = np.zeros(N)
for h, j in idx.items():
    if len(h) == 3:
        r[j] = f(*h)

psi0 = np.zeros(N)
psi0[idx[()]] = 1.0
max_repro_error = 0.0
for h in product((0, 1), repeat=3):
    psi = psi0.copy()
    for e in h:
        psi = U[e] @ psi
    pred = float(r @ psi)
    exact = float(f(*h))
    max_repro_error = max(max_repro_error, abs(pred-exact))

check("B2_prefix_memory_has_15_states", N == 15, f"N={N}")
check("B2_fixed_one_event_update_count_two", len(U) == 2, f"count={len(U)}")
check("B2_prefix_memory_exactly_reproduces_full_table", max_repro_error < 1e-12,
      f"max_error={max_repro_error:.3e}")
check("B2_nonzero_connected_triple_survives_in_memory_realization",
      abs(triple) > 1e-12 and max_repro_error < 1e-12,
      f"connected_triple={triple:.16g}")


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
passed = sum(ok for _, ok, _ in checks)
total = len(checks)
print(f"TOTAL {passed}/{total} PASS")

# Expected: 12/12 with the explicit four coboundary examples above.
if passed != total:
    raise SystemExit(1)
