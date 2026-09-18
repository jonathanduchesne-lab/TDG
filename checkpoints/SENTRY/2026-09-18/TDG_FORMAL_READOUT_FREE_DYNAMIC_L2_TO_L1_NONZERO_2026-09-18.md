# Complete TDG — readout-free formal dynamic l2->l1 obstruction

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **UNIQUE S4 l2->l1 DYNAMIC CHANNEL SURVIVES IN FORMAL z->infinity Q PENCIL / b4-b24 SAME COEFFICIENT / FINITE-READOUT AMPLITUDE VARIES BUT REPRESENTATION RAY DOES NOT / READOUT ARTIFACT RESCUE CLOSED / NO O3-DYNAMIC OR GR PROMOTION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parent

Immediate parent:

`TDG_CANONICAL_STANDARD3_PRE_POST_A21_UNIQUE_INTERTWINER_UNIFICATION_2026-09-18.md`

commit `b8b5fc63006cc5aa2b40fa2996d0a1f20c2e3c05`.

That checkpoint established:

- exact `dim Hom_S4(l2,l1)=1`;
- unique normalized intertwiner
  `J=-(1/sqrt3)[yz->x, xz->y, xy->z]`;
- pre-event canonical dynamic defect converges to `c_pre J`;
- post-event S4-restored A21 lies on the same unique ray;
- actualization changes conditional anisotropy/amplitude but does not remove the representation channel.

This checkpoint tests whether the pre-event nonzero coefficient is merely a finite analytic-readout artifact.

---

## 1. Fixed canonical selector and unique ray

The angular/source selector remains frozen as the exact side-orbit A3/cuboctahedral Standard3

`P_can=P_std P_anti`.

No finite spectral readout is used to select the physical Standard3.

The dynamic STF->gradient block is projected only on the already-derived unique S4 intertwiner `J`.

---

## 2. Finite-readout adversarial sweep

At b4 `a=.02`, using the same `P_can`, the historical finite resolvent family gives:

| z | ||A21|| | c_J | relative defect from c_J J |
|---|---:|---:|---:|
| `1.4+.5i` | 10.76247732 | 10.76247730 | 7.07e-5 |
| `2+.7i` | 11.69718095 | 11.69718087 | 1.16e-4 |
| `3+.8i` | 3.09881278 | 3.09881266 | 2.76e-4 |
| `8` | 10.77373826 | 10.77373825 | 4.55e-5 |
| `12` | 10.76991385 | 10.76991384 | 4.72e-5 |
| `20` | 10.76938007 | 10.76938006 | 2.65e-5 |

Thus finite-readout amplitude is not universal. However the matrix remains overwhelmingly on the same unique `J` ray throughout the tested family.

Classification:

- **REPRESENTATION RAY = READOUT-STABLE / UNIQUE**;
- **FINITE-z AMPLITUDE = READOUT-DEPENDENT**.

A finite readout therefore cannot be used as the physical normalization of the coefficient.

---

## 3. Formal readout-free construction

Use the recovered formal Q-B1850/Q-B1852 moment prolongation:

- construct `Gbar(t)` and move differences coefficientwise from exact H powers;
- no large-z numerical fit;
- no preferred complex phase;
- retain current `nbasis(Gbar)`;
- build formal scalar memory `F(t)`;
- build formal full response `Vbar(t)`;
- form
  `L(t)=Vbar_T0(t) F(t)^(-1)`;
- evaluate the corrected canonical A3 polynomial design;
- extract the STF->gradient block;
- project it onto normalized unique `J`.

The common scale stripped from the formal response cancels in `L(t)`, so the resulting constitutive block is projectively/readout-free.

---

## 4. b4 formal limit

At b4 `a=.02`:

| t | c_J | relative defect from c_J J |
|---:|---:|---:|
| .020 | 10.7692217300 | 2.54e-7 |
| .010 | 10.7692042252 | 1.40e-7 |
| .005 | 10.7692014534 | 5.36e-7 |
| .002 | 10.7692128225 | 3.46e-6 |

The smallest-t values enter floating cancellation floor, but the stable plateau is

`c_inf ~ 10.769201...`.

The three singular values become equal to the expected scalar-intertwiner spectrum at the same precision.

Therefore:

# **FORMAL / READOUT-FREE PRE-EVENT DYNAMIC l2->l1 COEFFICIENT IS NONZERO.**

---

## 5. b24 independent formal control

The entire formal construction was rerun directly in the parity-balanced b24 refinement, not inferred by scaling b4.

At b24 `a=.02`:

| t | c_J | relative defect from c_J J |
|---:|---:|---:|
| .020 | 10.7692055591 | 7.17e-8 |
| .010 | 10.7692012869 | 1.44e-7 |
| .005 | 10.7692014962 | 6.29e-7 |
| .002 | 10.7692162392 | 4.06e-6 |

The stable plateau is again

`c_inf ~ 10.769201...`.

Thus b4 and b24 agree on the formal readout-free coefficient to the available numerical precision before the small-t floor.

Classification:

# **FORMAL DYNAMIC COEFFICIENT b4/b24 NATURALITY = STRONG PASS.**

---

## 6. Binding interpretation

The current obstruction cannot be attributed to:

- the old finite-z selector;
- the old T3 support threshold;
- a choice among several Standard3 copies;
- a finite resolvent readout;
- b4 versus b24 refinement;
- an exceptional angular ray.

After all those choices are removed, the current Q law still produces

[
A21_{m formal}=c_infty J,qquad c_inftyapprox10.769201
eq0.
]

Therefore the dynamic O3 wall is now a genuine scalar constitutive coefficient on an already-identified unique representation channel.

Finite-z readouts deform the amplitude, sometimes strongly, but do not remove the underlying formal nonzero source.

---

## 7. Relation to post-event Gate B

The previous unification checkpoint already establishes that the S4-restored post-event A21 family lies on the same unique `J` ray and remains nonzero.

Hence:

- pre-event formal Q: `c_inf J`, `c_inf !=0`;
- post-event conditional Q: anisotropic radial/side blocks;
- post-event S4 restoration: `c_post J`, `c_post !=0`;
- state-universal FP cancellation: exact fail.

Actualization therefore does not repair the formal constitutive channel.

No equality between `c_inf` and `c_post` is asserted because post-event shell dimension, conditioning and normalization differ.

---

## 8. Exact next gate

# **FORMAL SCALAR COEFFICIENT ORIGIN / ZERO-IDENTITY GATE**

The representation and readout questions are now exhausted.

Next:

1. derive `c_inf` directly from the first nonzero formal H-path coefficients before numerical inversion;
2. reduce the coefficient through exact S4/Cons symmetry as far as possible;
3. identify which local path classes feed the unique `J` channel;
4. test whether any already-earned identity (parity, Cons coequalizer, Feshbach relation, Ward relation, StateSync/refinement transport, cofinal quotient) forces their sum to zero;
5. if the exact source sum is nonzero, certify the present RefinedQ realization as constitutively incompatible with full dynamic O3;
6. no counterterm, fitted coefficient, sector deletion or new state law may be added to cancel it;
7. parallel: derive the exact signed `3/130` D2/D3 relation.

---

## 9. GR traffic light

🟢 **Readout rescue closed:** the unique forbidden channel survives in the formal `z->infinity` Q pencil.

🟢 **Refinement control:** b4 and b24 converge to the same nonzero formal coefficient `~10.769201`.

🟢 **Representation ambiguity closed:** the map remains the unique `J` channel.

🟡 **Next exact target:** derive the scalar from local H-path algebra and ask whether an internal Q identity can make it zero.

🔴 **No full/dynamic O3, HDA, spin-2 or nonlinear GR yet.**
