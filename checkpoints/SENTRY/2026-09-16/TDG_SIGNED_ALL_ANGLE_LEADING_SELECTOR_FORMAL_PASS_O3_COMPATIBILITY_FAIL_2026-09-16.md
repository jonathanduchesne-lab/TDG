# Complete TDG — signed all-angle leading selector / O(3)-compatibility gate

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **SIGNED FORMAL LEADING SELECTOR = READOUT-FREE / ALL-ANGLE KERNEL-RAY PASS / D2-D3 SAME SIGNED RAY / 3/130 AMPLITUDE RATIO STRONGLY RETAINED / BUT FORMAL LEADING RAY HAS NONZERO T3 AND IS NOT THE HISTORICAL Q-B1854 O3-COMPATIBLE SELECTOR / LEADING SIGNED ALL-ANGLE RESCUE FAIL / NO NEW ROOT2 LAW**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parents and provenance

Binding current parents:

1. `TDG_GATE_A_ALL_ANGLE_LEADING_PROJECTIVE_CLASS_EXHAUSTION_2026-09-16.md` — commit `a7fc3976f8fb29867524605b0a62798cede12f4a`.
2. `TDG_GATE_A_ALL_ANGLE_POSITIVE_CLASS_PHYSICAL_TYPING_NO_STANDARD3_SELECTOR_2026-09-16.md` — commit `238ecb7c1727ef729c4bc080805fdc6ebef06da0`.

Historical Q-B1854 full handoff was recovered directly from the persistent Library:

`Complete_TDG_Root2_FULL_HANDOFF_QB1854L_2026-08-19.tar.gz`

Recovered SHA-256:

`59ec9a0ea5eab2aaa716c53b9493fb07122eb400c0c3258dd0414308afd2cde4`

which matches the certified handoff hash exactly.

The nested Q-B1854 repro contains the original scripts:

- `qb1854b_F_multiplicity.py`;
- `qb1854h_skew_selector_firstjet.py`;
- the certified Q-B1852/Q-B1850 dependency chain.

Thus the multiplicity/skew reduction used below is the historical Q-B1854 construction, not a reconstructed surrogate.

---

## 1. Historical signed selector map

Q-B1854 reduces the signed scalar memory `F:R^16->R^16` as follows.

1. Exact S4 Reynolds symmetrization:

`F_sym = (1/24) sum_p P_p^T F P_p`.

2. Exact physical Standard3 multiplicity basis `W:R^3->R^16`, obtained from the physical Standard3 projector and the `-1` fibre of one transposition.

3. Multiplicity operator:

`A_F = W^T F_sym W`.

4. Oriented/nonreciprocal part:

`K_F = (A_F - A_F^T)/2`.

A nonzero real 3x3 skew matrix has rank two and a one-dimensional kernel. Historical Q-B1854H used that kernel ray as the target-blind physical same-cut Standard3 selector.

Crucially, this whole reduction is linear in `F` before the final kernel extraction.

Therefore it can be applied coefficientwise to the formal Laurent/moment leaders from Gate A.

---

## 2. Formal signed coefficient construction

Let `K_m` denote the full 16x16 formal scalar-memory coefficient built from

`D_m[C,T]`

using the Gate-A asymptotic normal `nbasis(G0)` and the same Q-B1850 normalization.

For each coefficient `m`, define

`A_m = W^T Sym_S4(K_m) W`,

`S_m = (A_m - A_m^T)/2`.

The signed formal selector ray is

`x_m = ker S_m`.

No finite complex `z` is chosen.

---

## 3. Result: m=2 and m=3 select the same signed ray

### b4, a=.02

`S_2` singular values:

`(0.102677861, 0.102677861, ~1e-18)`.

`S_3` singular values:

`(4.44937400, 4.44937400, ~1e-16)`.

Both are exact numerical rank two and their one-dimensional kernels coincide to machine precision in the fixed historical multiplicity construction.

The same kernel coincidence is retained at:

- b4 `a=.04`;
- b4 `a=.01`;
- b24 `a=.02`.

Therefore:

# **FORMAL SIGNED D2 AND D3 SELECT THE SAME MULTIPLICITY KERNEL RAY.**

This is the signed analogue of the positive Gate-A D2/D3 projective coincidence.

---

## 4. The 3/130 relation descends directly to the signed source

The ratio of the nonzero skew singular value at `m=2` to that at `m=3` is:

- b4 `.04`: `0.0230769231288`;
- b4 `.02`: `0.0230769229559`;
- b4 `.01`: `0.0230769226101`;
- b24 `.02`: `0.0230769229890`.

The rational comparator is

`3/130 = 0.0230769230769...`.

The deviations are at approximately `5e-11`, `-1e-10`, `-5e-10`, `-9e-11`, respectively, with the finest b4 run closest to its floating-response floor.

Thus the previously observed full-matrix relation

`K2 ~= (3/130) K3`

is reflected directly in the **signed antisymmetric multiplicity source**, not only in the positive `K^T K` sector.

Classification:

`3/130 SIGNED-SKEW AMPLITUDE RATIO = VERY STRONG FORMAL-NUMERICAL PASS / EXACT SYMBOLIC DERIVATION STILL OPEN`.

---

## 5. All-angle consequence for the signed leading kernel

Gate A already proved:

- `D0=D1=0` exactly;
- generic rays use `D2`;
- `cos(4 theta)=0` changes only the base normal from `G0` to `G1`, with `G1` projectively identical to `G0`;
- `cos(6 theta)=0` kills `D2` but leaves `D3` as next move leader;
- `cos4=0` and `cos6=0` cannot occur simultaneously.

Since the signed multiplicity reduction is linear and since `S_2` and `S_3` have the same kernel ray, every real angular stratum gives the same **leading signed kernel ray**.

Therefore:

# **A READOUT-FREE / ALL-ANGLE FORMAL SIGNED SELECTOR RAY EXISTS AT LEADING ORDER.**

This closes the pure analytic-phase ambiguity for the leading signed selector itself.

---

## 6. Decisive adversary: the formal leading signed ray is not the historical O3-compatible selector

The historical Q-B1854H finite-family selector was physically interesting because, after converting its multiplicity ray into the aligned same-cut Standard3 embedding, the forbidden tetrahedral third moment obeyed

`T3 = O(a^2) -> 0`.

The same exact historical `irrep -> align -> t3` pipeline was applied to the new formal signed kernel ray.

Results:

### b4 a=.02

- `m=2`: `T3 = 0.117851134996...`
- `m=3`: `T3 = 0.117851131852...`

### b4 a=.01

- `m=2`: `T3 = 0.117851150616...`
- `m=3`: `T3 = 0.117851136784...`

### b24 a=.02

- `m=2`: `T3 = 0.117851135966...`
- `m=3`: `T3 = 0.117851132064...`

These values are stable rather than tending to zero. Numerically they coincide with the simple comparator

`1/(6 sqrt(2)) = 0.117851130197...`

to the scale expected from the finite-cutoff/formal extraction, but no exact identity is promoted here.

By contrast, the certified historical Q-B1854H finite-family selector had, at `z=2+.7i`,

- `.04`: `T3 = 5.59582e-3`;
- `.02`: `1.39217e-3`;
- `.01`: `3.47614e-4`,

scaling as `O(a^2) -> 0`.

Therefore the formal leading signed kernel is **not** the same physical multiplicity ray as the Q-B1854 O3-compatible selector.

Classification:

# **LEADING FORMAL SIGNED SELECTOR -> O3-COMPATIBLE STANDARD3 = STRONG FAIL.**

---

## 7. Interpretation

This result sharply corrects a tempting but invalid inference.

The new all-angle Gate-A positive theorem does extend to a leading signed kernel ray in the sense of analytic-phase independence. However:

- the leading signed ray is angularly tetrahedral, with nonzero continuum-stable `T3`;
- the historical good Q-B1854 selector is not the Laurent-leading kernel;
- its O3-compatible ray must arise from a **nontrivial combination/resummation of multiple analytic orders** of the signed response family.

Therefore the historical empirical readout stability of the Q-B1854 kernel cannot yet be retyped as a single leading formal coefficient theorem.

This also explains why the finite-z signed selector may be highly stable while remaining distinct from the strict `|z|->infinity` leader.

---

## 8. Relation to the dynamic obstruction

The result does **not** weaken the historical Q-B1854J or current Gate-B obstruction.

Indeed it strengthens the localization:

1. the leading formal signed response selects the wrong angular copy (`T3 != 0`);
2. a resummed finite-family signed response selects a much better angular copy (`T3 -> 0`);
3. even that better historical copy is not dynamically preserved by `L_Q=V F^-1`;
4. Gate B independently finds nonzero post-event 19D `A21(C)` and exact universal ensemble noncancellation.

Thus there are now two distinct layers of failure:

- **formal-leading signed selection mismatch**;
- **dynamic co-selection mismatch even after the improved resummed selector is used**.

No O(3)/HDA/GR promotion follows.

---

## 9. Exact next gate

# **SIGNED MULTI-ORDER / RESUMMED SELECTOR CANONICALITY GATE**

The next legal question is no longer whether the leading signed coefficient is all-angle; it is, and it selects the wrong copy.

The next gate is:

1. express the signed multiplicity family coefficientwise as
   `A(t)=sum_m t^m A_m`, with `S(t)=skew A(t)`;
2. determine whether Q itself supplies a readout-independent analytic rule that combines the noncollinear coefficient data into the historical O3-compatible kernel ray;
3. distinguish a genuine analytic connection/parallel-transport law from choosing a finite `z` by hand;
4. test whether the good Q-B1854 kernel is the unique fixed/adiabatic/transported line of the full signed coefficient pencil;
5. require b4/b24 naturality and all-angle compatibility of that construction;
6. only then retest dynamic co-selection against current/post-event `A21`;
7. if no Q-native canonical combination exists, classify the present RefinedQ signed selector as readout-family dependent despite its strong finite-z directional stability.

Parallel algebra subtask:

- derive exact `3/130` from the local H-path/Cons coefficient algebra;
- the signed result shows this ratio is source-level, making that derivation more plausible.

---

## 10. Firewalls

- leading signed kernel != historical finite-family Q-B1854 physical selector;
- numerical closeness of a rational ratio != exact proof;
- no finite `z` may be declared physical by convenience;
- no angular averaging or fitted multi-order combination;
- no hand-selected multiplicity ray;
- no positive Gram substitution for signed orientation;
- Gate B obstruction remains binding;
- Root1 frozen; global Q uncollapsed; factual ledger separate;
- Born NOT DERIVED universally;
- duration NOT DERIVED; Lambda OPEN;
- O(3), HDA, spin-2 and full nonlinear GR remain NOT ESTABLISHED.

---

## 11. GR traffic light

🟢 **Real progress:** the signed selector itself now has a readout-free all-angle leading kernel theorem.

🟢 **Source localization improved:** the `3/130` relation is visible directly in the signed physical multiplicity source.

🟢 **A false rescue is eliminated:** the leading signed all-angle ray is not the O3-compatible Q-B1854 ray.

🟡 **Immediate target:** derive a Q-native canonical multi-order/resummed signed selector, rather than choosing finite `z`.

🟡 **After that:** retest dynamic co-selection against the post-event 19D A21 obstruction.

🔴 **No GR closure:** current dynamics still does not co-select an O3 Standard3; HDA/spin-2/GR remain closed.
