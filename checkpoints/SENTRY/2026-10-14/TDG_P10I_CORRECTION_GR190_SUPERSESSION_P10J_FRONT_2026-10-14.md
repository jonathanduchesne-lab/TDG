# Complete TDG — P10I correction reconciled into current front

Date: 2026-10-14 (America/Toronto)
Status: P10I HISTORICAL WORKING CORRECTION ADOPTED / GR190 LONG-MOMENT FOURTH-NULL ROUTE SUPERSEDED / P10J BECOMES ACTIVE GATE
Historical FINAL-CERTIFIED authority: Q-B1858L unchanged.

## 1. Binding numerical correction

The GR189/P10G formal rcoord implementation solved its defining 5x4 system by normal equations:

(A^T A) r = A^T b.

Because the triplet block scales as a^-4 while the singlet normalization row is O(1):

cond(A) ~ a^-4

and the normal equations square the conditioning to roughly a^-8.

Measured:
- a=.04: cond(A)=6.9084e7; cond(A^T A)=4.2423e15;
- a=.02: cond(A)=1.10535e9; cond(A^T A)=1.90905e16;
- a=.01: cond(A)=1.76855e10; cond(A^T A)=1.27270e16.

Thus the old degree4 rank3 / exact fourth-null inference is not a stable Q theorem. It is a numerical formal-solver artifact.

## 2. Stable direct identity/path result

Using direct S4-central singlet identities and H(a)=H_diag+aK with t=a^2:

- stable central contraction matches tau^T DeltaG tau/16 at numerical floor;
- first resolved raw Cons-transferred D4 central singlet is t^2 = a^8, not a^12;
- stable singlet+triplet reconstruction restores a full rank4 D4 affine pencil in both b4 and b24.

Representative fourth-singular strength:
- b4 median sigma4/sigma1 ~0.0906;
- b24 ~0.180.

Within each scheme the corrected D4 operator is cutoff-stable and scales approximately a^4.

## 3. Remaining wall

Cross-scheme b4/b24 projective naturality still fails:
- a=.02: residual 0.255441, overlap 0.966803;
- a=.01: residual 0.254704, overlap 0.967008.

The discrepancy is cutoff-stable.

Therefore:
- FULL-RANK FOUR-AFFINE CAPACITY = RESTORED;
- COMMON b4<->b24 D4 OPERATOR = FAIL;
- UNIVERSAL Q-NATIVE FOUR-AFFINE PENCIL = NOT DERIVED.

## 4. Supersession rule

GR190 D8-D12 search for a higher-order fourth affine lift is paused/superseded.

Do not run D8-D12 until the leading D4 scheme cocycle is resolved.

## 5. Active gate

P10J — STABLE FULL-RANK D4 SCHEME-COCYCLE / COFINAL TRANSPORT GATE

1. Freeze the P10I stable singlet+triplet solver.
2. Never use normal equations for the central rcoord.
3. Rebuild complete D4 pencils for b4 and b24.
4. Audit coefficientwise and phase-ray scheme naturality.
5. Test only already-derived Q-native Cons/synchronization/cofinal transports.
6. No fitted GL4/O3 projector, whitening, preferred z, inverse-regulator normalization, target subtraction, duration/Born/QSC input.
7. PASS only if one pre-existing Q transport makes the rank4 D4 pencil refinement/cofinal-natural.
8. FAIL certifies missing universal refinement transport at leading four-affine order.

## 6. GR traffic light

GREEN: fourth affine channel exists already at D4.
GREEN: full rank4 capacity restored without new field or parameter.
GREEN: within-scheme scaling/naturality strong.
YELLOW: b4/b24 cofinal transport is the active finite problem.
RED: universal D4 operator not yet derived.
RED: dynamic O3/HDA/spin2/GR remain closed.
RED: P10I remains working/local, not retroactive FINAL-CERTIFIED.