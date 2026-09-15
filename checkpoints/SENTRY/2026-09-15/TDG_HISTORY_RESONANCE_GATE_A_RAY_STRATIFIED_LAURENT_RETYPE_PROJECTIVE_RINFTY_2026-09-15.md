# Complete TDG / Root2 — Gate A ray-stratified Laurent retype and projective `R_infty`

**Date:** 2026-09-15 (America/Toronto)  
**Status:** **BINDING TYPING CORRECTION / SINGLE HOLomorphic LAURENT COEFFICIENT OF PROCESS-NORMALIZED F NOT THE RIGHT UNIVERSAL OBJECT / PROJECTIVE `Rhat=F^dag F/Tr` LIMIT RETAINED AS STRONG ASYMPTOTIC EVIDENCE**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Why this correction is required

The immediately preceding asymptotic checkpoint found very strong multi-ray evidence that

`Rhat_C(z)=F_C(z)^dag F_C(z)/Tr(F_C(z)^dag F_C(z))`

converges to one common S4-typed projective operator as `|z|->infty`.

Its next proposed exactification was phrased as deriving one leading Laurent coefficient/order of the process-unit map `F_C(z)`.

A fresh audit of the actual Q-B1850 source and a deliberately chosen singular-phase ray shows that this phrasing is too strong and slightly mistyped.

The projective `R_infty` evidence survives. What changes is the correct formal object to derive.

## 1. Exact source-level typing fact: the response is not holomorphic in z alone

In the certified Q-B1850 source, the collective process scale uses resolvent blocks in

`Y += R_pe X R_ep`

followed explicitly by

`Y = (Y + Y^dag)/2`.

The local physical presentation likewise uses

`z_block = U_B comm U_B^dag`

followed by Hermitianization and real Gram contractions.

Therefore after physical Hermitian/readout construction the observable response depends on both the analytic resolvent and its Hermitian conjugate. Formally the large-readout expansion is real/bianalytic in inverse powers of `z` and `zbar`, not a single holomorphic Laurent series in `z` alone.

This is an **exact code/type fact** of the certified construction.

Consequently a scalar angular factor in the leading physical readout can vanish on special rays even if the projective response direction has a common continuation at the next nonzero order.

## 2. Deliberate singular-ray adversary

The phase

`theta = pi/8 = 22.5 deg`

was chosen because a leading Hermitianized contribution of schematic type `Re(z^-4)` can vanish there.

The normalized resonance operator was compared directly to the positive-real ray at fixed `a=.01`.

Relative `Rbar` differences:

- `|z|=16`: `1.7655902e-3`;
- `32`: `2.7337444e-4`;
- `64`: `5.4651548e-5`;
- `128`: `1.2265437e-5`;
- `256`: `2.9007514e-6`.

At `|z|=256`, the three polar Standard3 projectors have minimum principal cosines versus the real ray

- `0.999999999999176`;
- `0.999999999994642`;
- `0.999999999995213`.

Thus the singular-phase adversary **does not break the projective resonance limit**.

## 3. But the process-normalized F amplitude has ray-stratified asymptotic degree

To diagnose the formal structure, the following were separated:

1. raw Q-B1850 scalar cross-memory matrix norm `||F_raw||`;
2. mean Q-B1849 process-descriptor normalization amplitude `A_proc`;
3. resulting process-unit norm `||F_proc||`.

### Positive real ray

For `|z|=16,32,64,128`:

`||F_raw|| = 0.16354, 0.028727, 0.0061522, 0.00142987`.

Successive effective inverse powers:

`2.509, 2.223, 2.105`, approaching approximately order 2.

Mean process amplitudes:

`0.22729, 0.040533, 0.0087347, 0.00203586`.

Effective powers:

`2.487, 2.214, 2.101`, again approaching approximately order 2.

Therefore `||F_proc||` tends to a finite value:

`0.71863, 0.70786, 0.70347, 0.70148`.

### Singular `pi/8` ray

`||F_raw|| = 0.072655, 0.017217, 0.0040486, 0.00097759`.

Effective powers:

`2.077, 2.088, 2.050`, again near order 2.

But the process-normalization amplitude follows a different angularly cancelled hierarchy:

`0.43449, 0.16416, 0.068610, 0.031135`,

with effective powers `1.404, 1.259, 1.140` over this range.

Accordingly the process-unit matrix norm decreases:

`0.16701, 0.10475, 0.05894, 0.03136`.

Yet its normalized Gram/projective geometry converges to the same `R_infty`.

## 4. Binding retype

The following statement is withdrawn as the immediate target:

> derive one universal leading holomorphic Laurent coefficient of process-normalized `F_C(z)` valid uniformly over all complex rays.

The correct asymptotic object is instead projective and physically Hermitian:

`[R_infty] = lim_{|z|->infty} [F_C(z)^dag F_C(z)]`,

or equivalently its unit-trace representative where nonzero.

A future exact theorem should be formulated in a real/bianalytic inverse-resolvent expansion, allowing angularly stratified scalar leading order while proving that the first nonzero projective positive form belongs to one common ray-independent class.

In other words:

**scalar asymptotic degree may be ray-stratified; projective resonance geometry may still be universal.**

## 5. What remains strongly retained

The prior asymptotic evidence is strengthened, not demoted:

- generic complex rays converge rapidly toward the real-ray `R_infty`;
- the deliberately singular `pi/8` ray also converges to the same projective operator;
- direct Q-B1852 b4/b24 at `z=64` gives normalized-operator difference `3.86e-7` and projector agreement at ~`1e-12` level;
- asymptotic held-out Q-B1851 full-vector relevance remains ~`74.31%` top-mode capture and ~`92.70%` of the held-out optimum.

Therefore:

`PROJECTIVE R_infty` = **STRONG ASYMPTOTIC NUMERICAL / STRUCTURAL PASS**.

`ONE UNIFORM F_PROC LAURENT LEADING COEFFICIENT` = **RETYPE / NOT THE CORRECT UNIVERSAL OBJECT**.

## 6. Exact mathematical frontier after correction

The Gate-A exactification target is now:

> derive from the finite-dimensional Q resolvent construction a real/bianalytic inverse-readout expansion of the physical process response and prove that, after removing its first nonzero scalar angular/radial factor, the leading positive Gram class `F^dag F` is independent of the admissible ray, including rays where lower scalar coefficients vanish.

This is a projective-leading-symbol theorem, not a preferred-readout theorem.

No finite `z`, no energy/time interpretation of `z`, and no GR target is licensed.

## 7. Evidence

Fresh singular-ray result file:

`GATEA_ASYMPTOTIC_SINGULAR_RAY_RESULTS.json`

SHA-256:

`3268fb3b6b6e442340f663d1f62a3b7a20ca5742610736549d68d4b867866f8d`.

The scale diagnostics are reproducible directly from the certified Q-B1850 engine; no fitted physical coefficient was introduced.

## 8. GR traffic light

🟢 **Advance:** the candidate readout-free resonance object survives the strongest obvious angular-cancellation adversary.

🟢 **Advance:** the formal target is now typed correctly as a projective/bianalytic leading-symbol problem rather than an incorrectly assumed single holomorphic Laurent coefficient of `F`.

🟡 **Open exact theorem:** prove the common projective leading positive form algebraically.

🟡 **Gate B remains open:** physical history/lens ensemble measure.

🔴 **No GR promotion:** no factual-winner rule, Born NOT DERIVED, O(3) FAIL/NOT CLOSED, HDA/spin-2/full nonlinear GR NOT ESTABLISHED.
