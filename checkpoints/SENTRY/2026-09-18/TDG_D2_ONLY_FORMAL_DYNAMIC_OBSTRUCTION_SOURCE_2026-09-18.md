# Complete TDG — D2-only source localization of the formal dynamic obstruction

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **READOUT-FREE NONZERO l2->l1 COEFFICIENT IS ALREADY PRESENT IN THE FIRST ENVIRONMENT-SENSITIVE D2 COEFFICIENT / NO HIGHER-ORDER RESUMMATION REQUIRED / b4-b24 DIRECT CONTROL PASS / LOCAL H3 PATH-CLASS REDUCTION IS NEXT**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parent

Immediate parent:

`TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md`

commit `8e915dca3270ebd58088e7a1227525db5474d566`.

That checkpoint established a readout-free formal dynamic coefficient

`c_inf ~ 10.769201 != 0`

on the unique S4 `l=2 -> l=1` intertwiner `J`, with direct b4/b24 agreement.

The remaining question was whether that coefficient arises only after combining many formal orders or is already present at the first environment-sensitive order.

---

## 1. Exact D2-only construction

Gate A established structurally:

`D0=D1=0`.

The first environment-sensitive baseline-vs-move Gram coefficient is `D2`, arising first at the `H^3/U2` moment level.

Construct directly, without evaluating any finite formal parameter `t`:

- base metric = exact formal `G0`;
- base normal = `nbasis(G0)`;
- scalar memory coefficient
  `F2[T,C]=<N0(T),D2[C,T]>/||G0(T)|| / a^2`;
- full response coefficient
  `V2[T,C]=rcoord(G0(T),D2[C,T])/a^2`.

No `D3,D4,...`, no finite `t`, no finite `z`, and no asymptotic fit enters.

Both matrices retain full column rank:

### b4 a=.02
- rank F2 = 16;
- cond F2 = 31.0805807118;
- rank V2 = 16;
- cond V2 = 5.3437669563.

### b24 a=.02
- rank F2 = 16;
- cond F2 = 31.0805806484;
- rank V2 = 16;
- cond V2 = 5.3437670425.

---

## 2. D2-only constitutive block

Using the already-frozen canonical A3/cuboctahedral Standard3 polynomial design:

`L2 = V2_T0 F2^{-1}`.

Construct the central affine/Hessian response exactly as in the historical Q-B1852/Q-B1854 pipeline and project the STF->gradient block onto the normalized unique S4 intertwiner `J`.

### b4 a=.02

- `c_D2 = 10.769197696826911`;
- `||A21_D2|| = 10.769197696826910`;
- relative residual from `c_D2 J`:
  `9.44e-9`;
- singular values:
  `(6.21759924, 6.21759919, 6.21759914)`.

### b24 a=.02

- `c_D2 = 10.769197826299518`;
- `||A21_D2|| = 10.769197826299516`;
- relative residual from `c_D2 J`:
  `1.16e-8`;
- singular values:
  `(6.21759933, 6.21759926, 6.21759920)`.

Direct scheme difference in the scalar is approximately

`1.29e-7` absolute,

already at the numerical-formal extraction floor relative to the O(10) coefficient.

---

## 3. Comparison with full formal t->0 limit

Previous full formal pencil plateau:

`c_inf ~ 10.769201...`.

Direct D2-only:

`c_D2 ~ 10.7691978`.

The tiny difference is consistent with the finite small-t contamination/floating floor in the full formal evaluation.

Therefore:

# **THE NONZERO READOUT-FREE DYNAMIC OBSTRUCTION IS ALREADY PRESENT ENTIRELY AT THE FIRST ENVIRONMENT-SENSITIVE D2 ORDER.**

Higher formal coefficients are not required to create the forbidden channel.

They can only perturb its finite-t amplitude around the same already-existing nonzero source.

---

## 4. Structural consequence

The chain is now:

1. `D0=D1=0` exactly because local parent/face moments are unchanged under legal extension through `U1`;
2. exterior/environment sensitivity first enters through `U2=P_F H^3 P_T`;
3. the resulting `D2` alone gives full-rank `F2,V2`;
4. their constitutive quotient already gives
   `A21_D2 = c_D2 J`;
5. `c_D2 !=0` in both b4 and b24.

Thus the current dynamic O3 obstruction is born exactly at the first path length capable of leaving the local parent/face pair, sampling the environment, and returning.

It is not:

- a finite-z artifact;
- a higher-order resummation artifact;
- a selector ambiguity;
- a refinement-scheme artifact;
- an exceptional angular-ray artifact.

---

## 5. Exact next gate

# **H3 / U2 PATH-CLASS DECOMPOSITION OF c_D2**

Because the obstruction is already D2-only, the algebraic target is finite.

1. Decompose
   `U2=P_F H^3 P_T`
   into exact intermediate-sector path classes.
2. Use the block graph of the frozen H:
   parent core / B3 / fine B4 / B2.
3. Identify which U2 path classes change between the parent context and the four replacement children under Q-B1818H.
4. Propagate each legal class through the linear D2 Gram/Cons construction.
5. Determine which classes feed the unique S4 `J` channel.
6. Ask whether their exact sum can vanish by an already-earned Q identity.
7. If the source sum is provably nonzero, certify present RefinedQ as constitutively incompatible with full dynamic O3 at first environment-sensitive order.
8. No fitted counterterm, sector deletion or new law.

Parallel:
- exact symbolic source of the D2/D3 signed `3/130` ratio.

---

## 6. GR traffic light

🟢 **Major localization:** the obstruction is D2-only; no infinite resummation problem remains at its origin.

🟢 **First-environmental-order source:** it appears exactly when H-paths can first sample nonlocal carrier structure.

🟢 **b4/b24 control:** same coefficient and same unique J ray.

🟡 **Immediate exact task:** decompose H^3/U2 path classes and test whether their source sum has any internal zero identity.

🔴 **No dynamic O3/HDA/spin-2/GR closure.**
