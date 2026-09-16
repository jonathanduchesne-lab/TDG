# Complete TDG / Gate A — full-pipeline generic vs theta=pi/8 projective-coincidence pass

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **GENERIC-vs-PI/8 FULL Q-B1850 POSITIVE PROJECTIVE CLASS = STRONG FORMAL-NUMERICAL EXACT-SHAPE PASS / B4+B24+CUTOFF STABLE / SOURCE-LEVEL SYMBOLIC PROOF OF D0=D1 EXACTLY STILL OPEN / NO GR PROMOTION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parent and purpose

Immediate Gate-A parent:

`checkpoints/SENTRY/2026-09-15/TDG_HISTORY_RESONANCE_GATE_A_EXACT_RAY_STRATIFIED_RESOLVENT_SYMBOL_SINGULAR_STRATUM_FRONTIER_2026-09-15.md`

commit `4419847f54dddad048075ca9d74e3979da2ba830`.

That checkpoint proved upstream, for `z=r exp(i theta)`,

`Y_X(r,theta)=sum_(k>=0) r^(-(k+4)) cos((k+4)theta) S_k(X)`

with every `S_k(X)` Hermitian.

For generic rays, `cos(4theta)!=0`, so the local leading response is controlled by the `k=0` stratum. At

`theta=pi/8`,

`cos(4theta)=0`, while `cos(5theta)!=0`, so the generic local `k=0` stratum is exactly absent.

The remaining open question was whether, **after the entire Q-B1850 predictive-memory pipeline** — baseline-vs-move differencing, Cons, current local Gram normalization, normal extraction and scalar memory — the first surviving singular-ray positive response operator belongs to the same projective class as the generic-ray one.

This checkpoint evaluates that exact seam using the recovered certified Q-B1852/Q-B1850 source chain and persisted formal-prolongation source.

---

## 1. Sources / provenance

Recovered exact Q-B1852 source:

`qb1852_full_refined.py`

SHA-256:

`ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`.

The nested repro manifest and original portable verifier pass.

Persisted formal pipeline source:

`qb1860bg_formal_prolongation.py`.

It constructs, from the certified Q law:

1. H-power moments `U[(T,F,k)]`;
2. formal Gram coefficients on arbitrary carrier frontier;
3. Cons sewing coefficient by coefficient;
4. base-to-moved response coefficient differences `DGS[C][T][k]` for all 16 legal moves and 17 response contexts;
5. current-normal extraction `nbasis(Gbar[T])`;
6. scalar predictive-memory response `F` and full `(q,n)` response `Vbar`.

No finite preferred complex `z` is used in the coefficient audit below.

---

## 2. First robust move-difference coefficient

Fresh formal rerun, b4 `a=.02`, gives the maximum norm over all move/context differences:

- `DGS[0]`: `1.48e-23`;
- `DGS[1]`: `5.02e-22`;
- `DGS[2]`: `3.0471251124e-11`;
- higher orders: nonzero as expected.

The same separation persists under cutoff refinement:

### b4 a=.04
- `D0 ~ 2.37e-22`
- `D1 ~ 8.04e-21`
- `D2 ~ 1.95e-9`

### b4 a=.02
- `D0 ~ 1.48e-23`
- `D1 ~ 5.02e-22`
- `D2 ~ 3.05e-11`

### b4 a=.01
- `D0 ~ 9.25e-25`
- `D1 ~ 3.14e-23`
- `D2 ~ 4.76e-13`

Thus `D0,D1` remain at floating cancellation floor while `D2` is separated by roughly 11–13 orders of magnitude and follows the expected refinement scaling.

**Classification:** first robust physical baseline-vs-move coefficient in this formal Q-B1850 scalar-memory construction is `k=2`.

Caveat: a source-enclosed symbolic derivation of `D0=D1=0` as exact algebraic identities is not yet written. Therefore this checkpoint does not label that cancellation a symbolic theorem; it is a very strong formal-numerical structural pass.

---

## 3. Exact-shape relation of the base Gram coefficients

For every one of the sixteen noncentral response contexts, the first two base Gram coefficients satisfy numerically

# `G1(T) = 34.5 * G0(T)`

with maximum relative residual at floating floor.

Controls:

### b4 a=.04
- scale `34.5`
- max relative residual `~3.03e-16`

### b4 a=.02
- scale `34.5`
- max relative residual `~3e-16`

### b4 a=.01
- scale `34.5`
- floating-floor residual

### b24 a=.02
- scale `34.5`
- max relative residual `~2.88e-16`

Thus the `k=1` base Gram is not a new shape: it is the same local Gram ray as `G0` with one universal positive scalar factor.

Consequently

`nbasis(G1(T)) = nbasis(G0(T))`

for every context, to numerical precision.

The historical `nbasis` implementation is also invariant under an overall sign of the Gram input in direct controls:

`nbasis(-G)=nbasis(G)`.

Therefore the negative angular factor `cos(5pi/8)` on the singular ray does not flip or alter the selected normal line.

---

## 4. Angular typing of the two strata

### Generic ray

For `cos(4theta)!=0`, the base current Gram begins with the `G0` stratum.

Because `D0,D1` cancel at structural numerical floor, the first robust move-difference coefficient is `D2`, carrying angular factor

`cos(6theta)`.

The leading scalar-memory coefficient is therefore, up to an overall nonzero angular scalar,

`K_gen[T,C] = < n0(T), D2[C,T] > / ||G0(T)||`,

where

`n0(T)=nbasis(G0(T))`.

### Singular ray theta=pi/8

Exactly,

- `cos(4theta)=0`;
- `cos(5theta)=-0.382683432365... !=0`;
- `cos(6theta)=-0.707106781186... !=0`.

Hence the base-current leader moves from `G0` to `G1`, while the first robust move-difference remains `D2`.

The leading scalar-memory coefficient is therefore, again up to one overall nonzero angular scalar,

`K_sing[T,C] = < n1(T), D2[C,T] > / ||G1(T)||`,

with

`n1(T)=nbasis(G1(T))=n0(T)`.

Since `G1=34.5 G0`, it follows shape-wise that

# `K_gen = 34.5 * K_sing`.

The sign and magnitudes of `cos5theta`, `cos6theta` contribute only one overall scalar to the full leading matrix and hence disappear in its positive projective class.

---

## 5. Direct full-pipeline matrix test

Define

`R_gen = K_gen^dag K_gen`,

`R_sing = K_sing^dag K_sing`.

### b4 a=.02

Direct fresh result:

- both `K_gen` and `K_sing` rank `16`;
- best scalar `K_gen / K_sing = 34.5`;
- relative residual `1.4161882891e-15`;
- cosine = `~1`;
- best scalar `R_gen / R_sing = 1190.25 = 34.5^2`;
- relative residual `2.2074783024e-15`;
- positive-operator cosine = `1` to floating precision.

Therefore

# `[R_gen] = [R_sing]`

in the positive projective cone for the tested complete formal pipeline.

---

## 6. Refinement and scheme controls

### b4 a=.04

- `G1/G0 = 34.5`;
- `K_gen/K_sing = 34.5`;
- `K` relative residual `~1.43e-15`;
- `R_gen/R_sing = 1190.25`;
- `R` relative residual `~2.24e-15`.

### b4 a=.01

- same scales `34.5`, `1190.25`;
- `K` residual `~1.45e-15`;
- `R` residual `~2.22e-15`.

### b24 a=.02

- `G1/G0 = 34.5`;
- `K_gen/K_sing = 34.5`;
- `K` residual `~1.71e-15`;
- `R_gen/R_sing = 1190.25`;
- `R` residual `~2.76e-15`.

Thus the projective coincidence is stable against:

- factor-4 regulator span in b4;
- b4 -> parity-balanced b24 refinement at fixed `a=.02`;
- the singular-ray sign of the first surviving base coefficient.

No fitted rotation, per-context gain, mode deletion, or preferred finite readout is used.

---

## 7. Gate-A verdict for the pi/8 singular stratum

The exact target left by the parent checkpoint was

`[K_sing^dag K_sing] = [K_gen^dag K_gen]`

or an equivalent common positive S4-typed projective class after the complete Q-B1850 pipeline.

Fresh result:

# **GENERIC vs theta=pi/8 POSITIVE PROJECTIVE COINCIDENCE = STRONG FORMAL-NUMERICAL EXACT-SHAPE PASS.**

Specifically,

`R_gen = 1190.25 R_sing`

at machine precision across the tested b4/b24/refinement family.

Therefore the previously isolated `theta=pi/8` disappearance of the local `k=0` stratum does **not** produce a new leading positive response-resonance projective class after the complete current-Q predictive-memory pipeline.

This closes the specific singular-stratum seam that Gate A had isolated.

---

## 8. What is not yet promoted

This checkpoint does **not** claim full all-angle universality.

Other angular strata can arise whenever the first surviving **move-difference** coefficient itself is killed, e.g. angles where

`cos(6theta)=0`,

or where multiple early base coefficients vanish in another pattern.

Those strata may promote `D3`, `D4`, ... and must be audited separately before claiming universal projective equality over every complex ray.

Also still open:

- a symbolic/source-enclosed proof that `D0=D1=0` exactly;
- complete finite angular-strata classification of the full Q-B1850 coefficient pipeline.

---

## 9. Exact next Gate-A task

# **COMPLETE ANGULAR-STRATA FULL-PIPELINE CLASSIFICATION**

1. Build the finite table of early base coefficients `G_k` and move-difference coefficients `D_k` from the certified formal pipeline.
2. Enumerate ray classes by the first nonzero angular multiplier `cos((k+4)theta)` relevant to base and move-difference series.
3. For every exceptional ray where the generic `D2` term vanishes, identify the first surviving `D_m`.
4. Compute its leading current-normal scalar-memory matrix with the appropriately shifted base leader.
5. Compare `K_m^dag K_m` to the generic positive projective class.
6. Where possible, derive exact proportionality from coefficient identities rather than finite-angle numerics.
7. Separately prove or source-enclose `D0=D1=0` if a purely algebraic support/incidence argument exists.

No angular averaging, preferred z, fitted rotation or counterterm is permitted.

---

## 10. Firewalls

- this is not an O(3), HDA, spin-2 or GR theorem;
- positive projective equality of one response-resonance stratum does not repair Gate-B A21 anisotropy;
- Gate-B ensemble-restoration failure remains independently binding;
- no preferred finite complex `z` is introduced;
- no source coefficient is fitted to force coincidence;
- historical FINAL-CERTIFIED authority remains Q-B1858L.

---

## 11. GR traffic light

🟢 **Major constructive advance:** the previously open `theta=pi/8` singular Gate-A seam now closes onto the same full-pipeline positive projective class as generic rays.

🟢 **Robustness:** identical scalar relation survives b4 regulator refinement and independent b24 refinement.

🟡 **One layer remains before broad universality:** classify the other angular zeros, especially rays with `cos(6theta)=0`, and promote the low-order cancellations from structural numerical floor to algebraic proof if possible.

🔴 **No GR closure:** O(3), HDA, spin-2 and full nonlinear GR remain unestablished.