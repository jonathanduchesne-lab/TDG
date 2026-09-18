# Complete TDG — canonical Standard3 / pre-post actualization dynamic obstruction unification

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **PRE-EVENT CANONICAL STF->GRAD DEFECT AND POST-EVENT S4-RESTORED A21 LIE ON THE SAME UNIQUE S4 l2->l1 INTERTWINER RAY / ACTUALIZATION CHANGES CONDITIONAL ANISOTROPY AND AMPLITUDE BUT DOES NOT REMOVE THE CHANNEL / CURRENT REFinedQ DYNAMIC O3 MISMATCH STRUCTURALLY LOCALIZED / NO GR PROMOTION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Binding parents

1. `TDG_SIGNED_FORMAL_SELECTOR_CANONICAL_A3_CORRECTION_DYNAMIC_FAIL_2026-09-18.md` — commit `512dd7d02a3504bf9c66bf2c2cde65a4226a6030`.
2. `TDG_GATE_B_S4_COVARIANCE_AND_STATE_UNIVERSAL_FP_OPERATOR_NONCANCELLATION_2026-09-16.md` — commit `5123657ddebe51bc6972eeef0eb5d0867d35b016`.
3. `TDG_GATE_B_KSTAR_STATE_SELECTION_GAP_SYMMETRIC_CONTROL_NONZERO_EXHAUSTION_2026-09-16.md` — commit `8a07d4fb00b8f735b2a217dc191ec94a5bf6b23c`.

The canonical angular Standard3 projector is frozen as

`P_can=P_std P_anti`,

with exact rank 3, exact radial support zero, 12 side directions forming the A3/cuboctahedral antipodal root orbit.

The dynamic question is now independent of selector/readout ambiguity.

---

## 1. Exact S4 representation gate

Use the physical 3D Standard3 action `R(p)` inherited from the tetrahedral root-slot representation.

On the normalized traceless-Hessian 5D space, let `D2(p)` act by

`H -> R(p) H R(p)^T`.

Solve the exact intertwining equations

`J D2(p) = R(p) J`

for all 24 elements of S4.

The stacked linear system has nullity exactly:

# `dim Hom_S4(l=2,l=1)=1`.

In the historical STF basis

`(xx-yy, xx+yy-2zz, xy, xz, yz)`

and vector basis `(x,y,z)`, the normalized unique intertwiner is, up to global sign,

[
J=-rac1{sqrt3}
\begin{pmatrix}
0&0&0&0&1\\
0&0&0&1&0\\
0&0&1&0&0
\end{pmatrix}.
]

Equivalently, it is the unique ordinary-Standard3 channel

`(yz,xz,xy) -> (x,y,z)`.

Therefore every nonzero S4-equivariant map from the matching 3D component of l=2 into the physical Standard3 is a scalar multiple of this one ray.

---

## 2. Pre-event canonical dynamic defect converges to J

Using the corrected readout-free canonical selector `P_can`, retain the historical current-Q prolongation

`L_Q=V F^{-1}`

and reconstruct the central traceless-Hessian-to-gradient block.

Projection onto the unique normalized intertwiner `J` gives:

### b4

- `a=.04`: relative residual `4.7048831e-4`, cosine `0.999999889320`;
- `a=.02`: relative residual `1.1590748e-4`, cosine `0.999999993283`;
- `a=.01`: relative residual `2.8868866e-5`, cosine `0.999999999583`.

The residual decreases by approximately four under each halving of `a`, hence is consistent with `O(a^2)`.

The scalar coefficient along normalized `J` is:

- `.04`: `11.75815128`;
- `.02`: `11.69718087`;
- `.01`: `11.68233263`.

An `a^2` extrapolation gives approximately

`c_pre = 11.6771`,

consistent with the previous Richardson estimate `11.67738`.

Thus:

# **PRE-EVENT CANONICAL DYNAMIC OBSTRUCTION -> c_pre J, c_pre != 0.**

The trace-to-gradient channel independently tends to zero as approximately `a^2`; the surviving obstruction is the unique matching Standard3/STF channel.

---

## 3. Post-event conditional family and S4 restoration

Gate B established structurally

`A21(pC)=R_p A21(C) D2(p)^(-1)`.

A fixed actualized event belongs to one of two S4 orbits relative to T0:

- radial: 4 events;
- side: 12 events.

Individual conditional blocks need not be S4-invariant because the actualized event breaks the full pre-event symmetry.

Their continuum norms are nonzero:

- radial representative: `~0.321612`;
- side representative: `~0.549269`.

Exact covariance generates the full 4+12 family from the two representatives.

---

## 4. Orbit averaging returns the same unique intertwiner ray

The already-frozen Gate-B symmetric control gives:

### radial orbit average

`||A_rad_avg|| = 0.2881097170`

with singular values approximately

`(0.16634343,0.16634076,0.16633648)`.

### side orbit average

`||A_side_avg|| = 0.1392624758`

with singular values approximately

`(0.08040362,0.08040323,0.08040284)`.

Their matrix cosine is

`0.999999999184`

with the same sign.

Because each orbit average is S4-equivariant and

`dim Hom_S4(l=2,l=1)=1`,

both must lie on the same exact representation-theoretic ray `J` in the continuum.

For the uniform 16-lens symmetric control,

`||Abar21_sym|| = 0.1764742860`,

with singular values

`(0.10188799,0.10188761,0.10188683)`.

For normalized `J`, a scalar multiple `cJ` has three singular values `|c|/sqrt(3)`. Indeed

`0.1764742860/sqrt(3) = 0.101887... `,

matching the observed spectrum.

Therefore:

# **POST-EVENT S4-RESTORED A21 = c_post J, c_post != 0.**

The present finite symmetric-control coefficient is approximately

`c_post = 0.1764742860`

in its post-event normalization convention.

No equality of `c_pre` and `c_post` is claimed; the two pipelines use different shells/normalizations and actualization conditioning.

---

## 5. Structural unification

The current RefinedQ dynamic wall is no longer typed as several unrelated anisotropies.

Before actualization:

`A21_pre -> c_pre J`, `c_pre ~ 11.677 !=0`.

After one actualization:

- conditional blocks split into radial/side anisotropic representatives;
- exact S4 covariance transports them through their event orbits;
- S4-restored/orbit-averaged response returns to the same unique ray `J`;
- the coefficient remains nonzero.

Thus:

# **ACTUALIZATION DOES NOT REMOVE OR CHANGE THE REPRESENTATION TYPE OF THE DYNAMIC l2->l1 OBSTRUCTION.**

It changes:

- conditional shell dimension (16 -> 19 successor directions);
- event stabilizer / anisotropy;
- amplitude/normalization;

but the symmetry-restored forbidden channel is the same unique Standard3 intertwiner.

This is a structural localization result, not a GR assumption.

---

## 6. Relation to exact FP noncancellation

Gate B already proves the stronger operator statement

`M_A21 != 0`

without choosing a state, by restricting to a T0-boundary B3 port supported by exactly one allowed radial lens.

Therefore the same channel cannot be removed universally by ensemble averaging.

The symmetric-control average additionally shows that when S4 symmetry is restored in the most natural diagnostic state, the obstruction does not cancel; it becomes a clean scalar multiple of `J`.

Hence:

- selector ambiguity = removed;
- analytic-phase ambiguity = removed at leading signed/positive level;
- S4 representation ambiguity of the surviving dynamic defect = removed;
- universal FP ensemble cancellation = exact fail.

The remaining problem is genuinely constitutive/dynamical.

---

## 7. What is and is not proved

### CLOSED / STRONG

- unique S4 `l2->l1` intertwiner dimension = 1;
- pre-event corrected canonical dynamic defect converges to that ray as `O(a^2)`;
- post-event S4-restored/orbit-averaged A21 lies on the same ray by exact covariance + uniqueness;
- both pre- and post-event coefficients are nonzero;
- actualization does not erase the channel;
- universal FP cancellation remains exact fail.

### NOT DERIVED

- an exact amplitude transport law relating `c_pre` to `c_post`;
- a Q-native constitutive identity forcing this coefficient to zero;
- physical `rho_Kstar`;
- full/dynamical O(3);
- HDA, spin-2 or nonlinear GR.

---

## 8. Exact next gate

# **NONZERO INTERTWINER COEFFICIENT ORIGIN / CONSTITUTIVE ZERO GATE**

The representation problem is now solved: only one offending channel exists.

Next:

1. express the scalar coefficient `c_Q` multiplying `J` directly in the pre-inversion Q/H-path algebra;
2. determine its first nonzero formal order and exact dependence on the already-fixed local blocks `H_TT,H_FF,H_FT`, Cons and refinement;
3. track the corresponding scalar through one actualization into radial/side conditional coefficients;
4. ask whether any already-earned Q identity, parity, Ward relation, Feshbach relation or cofinal quotient forces `c_Q=0`;
5. if no such identity exists and the coefficient is structurally nonzero, certify the current RefinedQ realization as dynamically incompatible with O(3) at this constitutive channel rather than searching for another selector;
6. do not fit a counterterm or delete the Standard3 component;
7. parallel: finish the exact symbolic `3/130` source identity.

---

## 9. GR traffic light

🟢 **Major localization:** the pre/post dynamic wall is one and the same unique S4 `l2->l1` intertwiner channel.

🟢 **Selector issue is no longer the blocker:** the canonical A3 Standard3 is fixed readout-free.

🟢 **Actualization does not wash the problem away:** the same representation channel survives after the event and under S4 restoration.

🟡 **Immediate mathematical target:** derive the scalar coefficient multiplying this unique channel and test whether Q contains an exact zero identity.

🔴 **If the coefficient is structurally nonzero, current RefinedQ cannot deliver full dynamic O(3) without a genuinely new mechanism.**

🔴 **No HDA/spin-2/GR promotion yet.**
