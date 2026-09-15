# Complete TDG / Root2 — History-resonance Gate A asymptotic readout-free projective limit

**Date:** 2026-09-15 (America/Toronto)  
**Status:** **STRONG ASYMPTOTIC NUMERICAL PASS / RAY-INDEPENDENT PROJECTIVE LIMIT EVIDENCE / DIRECT b4-b24 PASS / EXACT LAURENT THEOREM NOT DERIVED**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Purpose

Earlier Gate-A work established two facts that must be reconciled:

1. finite complex resolvent readouts can change the normalized positive resonance operator `Rhat_C = F_C^dag F_C / Tr(F_C^dag F_C)` by `O(1)`;
2. the resonance organization is nevertheless highly stable under cutoff, real readout changes and direct b4/b24 refinement, and has strong held-out full-vector process relevance.

The legal remaining question was whether the Q resolvent family itself contains a target-blind **large-|z| projective limit** that removes the finite-readout ambiguity without choosing a preferred finite complex `z`.

This is a legitimate historical diagnostic class. GR39 already used large-|z| convergence as a readout-free/formal-leading-coefficient adversary, classifying strong asymptotic evidence while explicitly keeping `EXACT LAURENT THEOREM = NOT DERIVED`.

The same epistemic discipline is used here.

No energy/time interpretation of `z`, no preferred ray, no O(3), SAME-h, HDA or GR target is introduced.

## 1. Definition of the asymptotic candidate

For the Q-B1850 process-unit response map `F_C(z)` define

`Rhat_C(z) = F_C(z)^dag F_C(z) / Tr(F_C(z)^dag F_C(z))`.

Let `Rbar_C(z)` be its exact S4 Reynolds/commutant projection.

The candidate readout-free projective resonance object is

`R_infty := projective-lim_{|z|->infty} Rbar_C(z)`,

provided the normalized operator and its separated spectral projectors converge independently of the ray in the tested resolvent domain.

This checkpoint does **not** assert an exact Laurent coefficient formula. It tests existence and ray-independence numerically over a controlled asymptotic range.

## 2. Fresh multi-ray asymptotic test

Fixed microscopic cutoff: `a=.01`.

Radii tested:

`|z| = 8, 16, 32, 64, 128`.

Primary ray panel:

- positive real ray;
- angle `pi/6`;
- angle `pi/4`.

### Polar Standard3 eigenvalues on the real ray

At `|z|=8`:

- `0.09901985040`;
- `0.06610275577`;
- `0.05284360146`.

At `16`:

- `0.09901874043`;
- `0.06610155001`;
- `0.05284431502`.

At `32`:

- `0.09901864529`;
- `0.06610144294`;
- `0.05284437654`.

At `64`:

- `0.09901862885`;
- `0.06610142479`;
- `0.05284438721`.

At `128`:

- `0.09901862367`;
- `0.06610142157`;
- `0.05284439070`.

These approach a stable nondegenerate multiplicity spectrum.

## 3. Ray-independence convergence

Relative normalized-operator difference between the `pi/4` ray and positive-real ray:

- `|z|=8`: `0.03021469143`;
- `16`: `0.00449920724`;
- `32`: `0.00082860204`;
- `64`: `0.00017692990`;
- `128`: `0.00004113803`.

Thus the finite complex-readout `O(1)` disagreement seen near the physical-scale resolvent region contracts rapidly in the large-|z| regime.

For the `pi/6` ray:

- `|z|=8`: `0.02745383184`;
- `16`: `0.00277261756`;
- `32`: `0.00045152072`.

### Spectral projectors

At `|z|=32`, `pi/4` vs real minimum principal cosines for the three polar Standard3 projectors are

- `0.9999999079`;
- `0.9999994701`;
- `0.9999995461`.

At `64`:

- `0.9999999958`;
- `0.9999999760`;
- `0.9999999795`.

At `128`:

- `0.9999999998`;
- `0.9999999987`;
- `0.9999999989`.

**Classification:** ray-independent projective spectral convergence = **STRONG NUMERICAL PASS** in the tested asymptotic panel.

## 4. Asymptotic held-out process relevance

The asymptotic resonance modes were evaluated against the independent Q-B1851 full-vector response `V(z)` at the same large-|z| readout, without fitting any mode to `V`.

### z=64 real

Held-out Standard3 polar-response captures by the three frozen `F` resonance modules:

- top: `0.7431269199`;
- middle: `0.1883456669`;
- lower: `0.0685274132`.

The maximum possible rank-3 capture from the independently diagonalized `V` sector is `0.8016865424`.

The top `F` resonance module therefore achieves `92.6954%` of the held-out optimum.

Top-F/top-V minimum principal cosine: `0.9554347695`.

### z=128 real

- top capture: `0.7431270327`;
- middle: `0.1883455683`;
- lower: `0.0685273991`;
- optimum: `0.8016865601`;
- fraction of optimum: `0.9269545851`;
- top-F/top-V min cosine: `0.9554348449`.

### z=128 at pi/4

- top capture: `0.7431207556`;
- middle: `0.1883573271`;
- lower: `0.0685219173`;
- fraction of optimum: `0.9269616676`;
- top-F/top-V min cosine: `0.9554379881`.

Thus the asymptotic ray-independent resonance geometry retains and even sharpens the independent held-out process relevance found at finite reference readout.

## 5. Direct Q-B1852 b4/b24 asymptotic refinement test

The exact same-Q 101-parent Q-B1852 refined engine was rerun at

`a=.02`, `z=64` real,

using the same Q-B1849 process-unit normalization for `F`.

### Conditions

- b4 `cond(F) = 29.0459269323`;
- b24 `cond(F) = 29.0459037949`.

### Resonance operator agreement

Normalized S4-commutant resonance operators differ by only

`3.8553205775e-7`.

The three polar Standard3 projectors have b4-vs-b24 minimum principal cosines

- `0.999999999999582`;
- `0.999999999999131`;
- `0.999999999999340`.

This is substantially stronger than the already-strong finite-reference-readout b4/b24 comparison.

### Asymptotic held-out V relevance under refinement

b4:

- top capture `0.7431259498`;
- fraction of held-out optimum `0.9269534020`;
- top-F/top-V min cosine `0.9554341015`.

b24:

- top capture `0.7431262759`;
- fraction of held-out optimum `0.9269537810`;
- top-F/top-V min cosine `0.9554343381`.

Hence the asymptotic resonance geometry and its held-out process relevance are both strongly refinement-natural in the direct b4/b24 test.

## 6. Relationship to the finite-complex-readout failure

There is no contradiction.

At finite complex readout, `Rhat_C(z)` can vary by `O(1)` and its lower polar Standard3 projectors can rotate significantly. The new result shows that this finite-readout dependence contracts toward a common projective operator as the resolvent is taken into the large-|z| formal regime.

Therefore the correct current classification is:

- `FINITE COMPLEX z UNIVERSAL R_C` = **FAIL in tested family**;
- `LARGE-|z| R_C PROJECTIVE LIMIT` = **STRONG NUMERICAL PASS / RAY-INDEPENDENT EVIDENCE**;
- `EXACT FORMAL LAURENT COEFFICIENT/THEOREM FOR R_infty` = **OPEN / NOT DERIVED**.

No finite `z` is promoted as physical or preferred.

## 7. Does this count as readout-free?

Only in the precise projective-asymptotic sense.

`R_infty` is not tied to one chosen finite probe value and the tested rays converge to the same normalized geometry. This makes it a legitimate **candidate readout-free response invariant**.

However, until the exact leading Laurent structure of the Q-B1850 process-unit map is derived, the project may claim only:

> **strong numerical/formal evidence for a Q-native asymptotic projective resonance operator.**

It may not yet claim an exact theorem defining `R_infty` from a closed Laurent coefficient formula.

## 8. Gate A status after this checkpoint

### Strongly closed positively

- exact S4 collective-mode organization;
- cutoff robustness;
- real-readout robustness;
- direct b4/b24 refinement robustness;
- held-out Q-B1851 full-vector process relevance;
- large-|z| ray-independent projective resonance convergence;
- direct b4/b24 asymptotic projective agreement;
- asymptotic held-out process relevance.

### Closed negatively in tested scope

- one universal finite-complex-readout positive resonance spectrum;
- cubic-polar Standard3 as a pure `R_C` eigenmodule.

### Exact mathematical item still open

- derive the leading Laurent coefficient/order of the process-unit response map sufficiently explicitly to promote `R_infty` from STRONG ASYMPTOTIC NUMERICAL to EXACT FORMAL/ALGEBRAIC.

Gate B history/lens ensemble covariance remains a separate live frontier.

## 9. Evidence hashes

- `GATEA_ASYMPTOTIC_Z_RESULTS.json` SHA-256 `939f80bcfaa547ac14dcb66bb1399ed4eb84d3bcdbb3ee50867eb149a440faa8`;
- `GATEA_ASYMPTOTIC_TAIL_RESULTS.json` SHA-256 `f0d0accc37573b736a37e876e7f6c8beb1e1dc54d8d7edacff0b31eef7dbb76e`;
- `GATEA_ASYMPTOTIC_HELDOUT_RESULTS.json` SHA-256 `f9fe1a5ecde7e095514410b6912532335eb90336516325bb023e6bd870df19ff`;
- `GATEA_ASYMPTOTIC_REFINED_RESULTS.json` SHA-256 `2b6b9f48c4b0978ef423b989e5fc534da8c2644586c8aa45e2b0ec3465f65058`.

## 10. Exact next legal work

Two legal directions remain:

1. **Gate A exactification:** derive the formal leading Laurent coefficient/order behind the observed `R_infty` convergence without fitting any finite `z` or importing downstream geometry.
2. **Gate B:** identify a physically licensed same-stage history/lens ensemble and measure, then test effective covariance of the conditional response.

No H5 microscopic completion is licensed merely from the present resonance results. H5 remains PAUSED / NOT REJECTED.

## 11. GR traffic light

🟢 **Major structural advance:** the resonance program now has a plausible Q-native readout-free object in the asymptotic projective sense, with multi-ray, cutoff, refinement and held-out-process support.

🟢 **The finite complex-readout failure is now localized rather than fatal:** it is a finite-probe ambiguity that contracts strongly in the formal large-|z| regime.

🟡 **Exact theorem still needed:** the Laurent coefficient/order behind `R_infty` is not yet derived.

🟡 **Gate B remains open:** physical lens/history ensemble measure is not fixed.

🔴 **No GR promotion:** no factual-winner rule, Born remains NOT DERIVED, O(3) remains FAIL/NOT CLOSED, HDA/spin-2/full nonlinear GR remain NOT ESTABLISHED.
