# Complete TDG / Unified Bridge Sentry — MRP4 `chi` Herm2 response-norm typing

**Date:** 2026-09-14 (America/Toronto)  
**Status:** **CONDITIONAL STRUCTURAL PASS / SCALARIZATION CAN BE CANONICAL / PHYSICAL PAIR-RESOLVED `F_uv` STILL NOT DERIVED**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Scope and latest-wins corrections

This checkpoint follows the modern MRP5 refinement-functor identifiability no-go and asks a narrower question:

> If Q itself supplies a physically distinguished positive Herm2 response for each unordered physical pair `u,v`, can the MRP4 scalar field `chi_uv>0` be extracted canonically, without choosing an additive CP-effect ontology or a fitted scalarization?

Binding historical corrections are preserved:

- Q-B1008: identifying a path-independent joint object with the **composite branch effect** on both paths compactifies the face holonomy to `SU2`; this cannot be used as the generic Lorentz-curved response route.
- Q-B1009: Q-B731's `F_ij` is a **Q-defined Herm2 joint response**, not generically the branch occurrence effect `M^dagger M`. The old Q-B984 parallel-sum effect construction is only an existence/positivity toy and is not a derivation of the geometric joint response.
- Q-B1014: the invariant object at a completed Cons endpoint is a Herm2 response system with frame-covariant representatives.
- Q-B1015: intervention-complete future data canonically determine the response **system/module**, but do not select one preferred Herm2 element unless a future observable/subchannel is independently physically distinguished.

No b4/b24, O(3), HDA, spin-2, Einstein or GR target is used here.

---

## 1. Historical Q precedent: positive Herm2 response magnitude

Q-B1143 already supplies the relevant normalization in a Q response setting.

For the four locked positive face responses `E_f`, which have the same determinant, it defines

`F_0 = sqrt(det E_f) I`,

`G_f = sqrt(E_f/F_0) in SL2(C)`,

so that

`E_f = G_f F_0 G_f^dagger`.

The positive square root makes the frame canonical at the locked phase, and the dynamic response family remains rank-healthy on an open positive neighborhood.

Thus `sqrt(det E)` as the positive scalar magnitude separated from an `SL2` frame is **already present in the Q lineage**; it is not introduced here to repair MRP4.

This is distinct from Born/factual probability and distinct from identifying the response with a branch effect.

---

## 2. Conditional candidate

Assume only for this construction that Q has independently supplied, for each physically distinguished compatible pair `{u,v}`, a positive-definite Herm2 response

`F_uv > 0`

belonging to the physical carrier response system.

Define

`chi_uv = sqrt(det F_uv)`.

This is a positive degree-one magnitude on the future-timelike Herm2 cone.

The assumption that such pair-specific `F_uv` exists and is physically distinguished is **not** silently promoted; it is the remaining open gate.

---

## 3. Exact frame-covariance theorem

Q-B1014 uses frame-chart representatives of the form

`E = A^{-dagger} F A^{-1}`.

For any invertible `A in GL2(C)`,

`det E = |det A|^{-2} det F`.

Therefore

`sqrt(det E) = |det A|^{-1} sqrt(det F)`.

For all pair responses represented in the same carrier frame, the factor `|det A|^{-1}` is common.

MRP4 is exactly blind to a common positive scaling of the local response triple because

`G_Fe = Q_F^dagger diag(chi_uv) Q_F`,

`P_Fe = G_Fe / sqrt(det G_Fe)`.

Hence the full projective MRP4 transport is unchanged.

For determinant-one `SL2(C)` frames the scalar is exactly invariant:

`sqrt(det E)=sqrt(det F)`.

Thus `chi_uv=sqrt(det F_uv)` is compatible with the already-retained Q-B1014 frame 2-morphism rather than requiring a preferred response chart.

---

## 4. Why the square root is selected if `chi` is a response magnitude

Consider the entire determinant-power family

`chi_uv^(r) = (det F_uv)^r`, `r>0`.

Under a positive rescaling of the physical response,

`F -> lambda F`,

one has

`det(lambda F)=lambda^2 det F`,

so

`chi^(r)(lambda F)=lambda^(2r) chi^(r)(F)`.

If `chi` is required to be a **degree-one response magnitude**,

`chi(lambda F)=lambda chi(F)`,

then exactly

`2r=1`, i.e.

`r=1/2`.

Therefore the previous determinant-power ambiguity disappears once the scalar is typed as a magnitude of the Herm2 response rather than as an arbitrary positive function of it.

This does not assert linear additivity. In fact there is no nonzero scalar linear functional invariant under the full noncompact `SL2` Herm2 action without an additional transforming dual state/order unit. The determinant norm is necessarily nonlinear.

---

## 5. Fresh verifier

A generic set of 15 positive-definite complex Herm2 pair responses was generated before evaluating any MRP4 output.

### Primary audit — 8/8 PASS

- minimum `det F_uv`: `2.3629650916`;
- minimum eigenvalue: `0.4682974161`;
- generic GL2 frame expected common scale: `0.8104240647162173`;
- measured mean scale ratio: `0.8104240647162175`;
- ratio spread: `1.84e-16`;
- MRP4 coupling projective residual after GL2 frame change: `2.26e-16`;
- maximum `SL2` chi defect: `3.55e-15`;
- MRP4 coupling projective residual under SL2 frame: `1.86e-16`;
- common physical response scaling by `lambda=5.7` gives mean chi scale exactly `5.7` and MRP4 residual `2.44e-16`;
- sampled determinant powers `r={.25,.5,1,1.5}`: only `r=.5` is degree-one;
- other powers give genuinely different MRP4 transports; for example `r=.5` vs `r=1` has maximum local projective response residual `0.2449138681`;
- a six-transformation SL2 fixed-covector audit has constraint rank `4/4`, numerically witnessing the absence of a nonzero invariant linear scalar functional.

### Independent audit — 5/5 PASS

A second positive response ensemble and independent GL2 frame gives:

- minimum eigenvalue `0.2001190523`;
- expected frame scale `0.8967718890`;
- maximum scale-ratio defect `6.66e-16`;
- only `r=.5` among `{.2,.5,.8,1.2}` is degree-one;
- `r=.5` and `r=1` response rays differ projectively by `0.3220810`.

The structural result is therefore not tied to the first random control.

---

## 6. What this fixes — and what it does not

### Fixed conditionally

If Q supplies a physically distinguished positive pair response `F_uv`, then the scalarization problem has a natural Q-native solution:

`F_uv -> chi_uv = sqrt(det F_uv)`.

It is:

- positive on the positive-definite Herm2 chart;
- target-blind;
- frame covariant under the Q-B1014 congruence law;
- exactly invariant under determinant-one frames;
- projectively invariant in MRP4 under general common GL2 frame changes;
- homogeneous of degree one;
- consistent with the Q-B1143 response/frame split;
- unrelated to Born/factual probability;
- not an illicit branch-effect identification.

### Still open

The current Root/corpus has **not yet derived a unique positive pair-resolved `F_uv` for every MRP4 pair**.

Q-B1015 is binding: a full future response quotient selects a response system, not one preferred Herm2 element. A unique `F_uv` requires an independently distinguished future observable/subchannel.

Q-B58/59 establish that a future process can be conditioned by process contraction when the extension-resolved subchannel is **physically distinguished**, but arbitrary Kraus labels cannot be promoted to facts.

Therefore the missing object is no longer an arbitrary `chi` refinement axiom. It is:

**a Q-native physically distinguished pair-resolved positive Herm2 response natural under Cons/refinement.**

---

## 7. Relation to the modern MRP5 p-family no-go

The earlier modern MRP5 result remains correct.

If `chi` is treated as a **primitive positive scalar field**, positivity + homogeneity + relabeling + spectators + refinement diamonds admit a continuum of `l_p` pushforwards, so the scalar refinement law is underdetermined.

The present result identifies a possible way around that ambiguity:

1. derive the physical Herm2 response `F_uv` from Q at each scale;
2. let Q/Cons/Feshbach determine the refinement/descent of `F_uv`;
3. only then define `chi_uv=sqrt(det F_uv)`.

Then no independent scalar `p`-law is chosen.

This is a conditional route, not yet a closure, because step 1 and the cross-refinement naturality of `F_uv` remain open.

---

## 8. Updated G0-G10 reading

For the MRP4 response-state route:

- G0 new-microphysics necessity: **unchanged OPEN / not Root-derived**;
- G1 physical typing of scalar magnitude: **CONDITIONAL STRONG PASS** once positive physical `F_uv` is derived;
- G1 physical selection/existence of pair-specific `F_uv`: **OPEN**;
- G2 nonredundancy: **OPEN**; static-common-cause MRP4 null remains binding until the underlying `F_uv` is shown process-sensitive;
- G3 composition-normality: **moves upstream to the response-system / `F_uv` descent law**;
- G4 dilation-normality: **NOT PASSED**;
- G5 parameter selection: **no fitted scalar exponent remains; degree-one typing fixes `r=1/2`**;
- G6 matched-null margin: **not yet earned**;
- G7 Cons/naturality: Q-B1014 supplies the response-system frame law, but pair-resolved `F_uv` naturality remains open;
- G8 refinement survival: **not yet tested for actual Q-derived `F_uv`**;
- G9 conservative Q consistency: **structural pass only; no new physical Q adopted**;
- G10 target-blind freeze: **PASS for this audit**.

MRP4 is still **NOT promoted as final physical Q**.

---

## 9. Exact next legal gate

### PAIR-RESOLVED POSITIVE RESPONSE / PROCESS-CONTRACTION NATURALITY GATE

Before any P10M/P10O, b4/b24, O(3), ELGC or GR-facing test:

1. identify a physically distinguished pair-resolved future observable/subchannel from the Q process itself; no arbitrary Kraus label;
2. contract the intervention-complete process to obtain `F_uv in R_S`;
3. prove `F_uv` is Hermitian positive/future-timelike on an open physical chart, or explicitly classify where it becomes null/boundary;
4. verify Q-B1014 frame-chart covariance and response Cons;
5. derive its coarse/fine transformation from the same Q process / Cons / Feshbach descent, rather than prescribing a scalar refinement law;
6. define only afterward `chi_uv=sqrt(det F_uv)`;
7. freeze this construction and confront spectator/dilation/static-common-cause controls;
8. only after those pass may MRP4/MRP5 face P10 cofinality and downstream little-group/O(3) gates.

If Q cannot independently distinguish such pair responses, MRP4 remains a mathematically valid comparator with no physical `chi` source.

---

## 10. Petit verdict — avance vers GR ?

🟢 **Oui, progrès de fond.** The scalar `chi` itself no longer appears to require an arbitrary physical postulate: the retained Herm2 geometry supplies a canonical degree-one magnitude, conditionally on a physical positive `F_uv`.

🟡 **The bottleneck is now one level upstream:** derive the pair-resolved positive response from the intervention-complete Q process and prove its Cons/refinement naturality.

🔴 **No GR promotion.** The static-common-cause null is not defeated, MRP4 is not physical Q, and O(3), HDA, spin-2 and nonlinear GR remain not established.
