# Complete TDG — source derivation of the D2/D3 3/130 proportionality

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **D3/D2 PROPORTIONALITY LOCALIZED BEFORE nbasis / SOURCE-LEVEL AFFINE ENERGY-INSERTION LAW IDENTIFIED / CANONICAL FACTOR 130/3 EXPLAINED BY 10 GLOBAL INSERTION POSITIONS = 5 PARENT + 5 B3 WITH H0 HIGH-SECTOR WEIGHT / 3/130 PROMOTED FROM RATIONAL-LOOKING FIT TO STRUCTURALLY DERIVED SOURCE IDENTITY WITH NUMERICAL VERIFICATION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parents

Relevant parents:

- `TDG_GATE_A_ALL_ANGLE_LEADING_PROJECTIVE_CLASS_EXHAUSTION_2026-09-16.md`;
- `TDG_D2_H3_PATH_CLASS_INTERPARENT_CORE_REDUCTION_2026-09-18.md` — commit `4bff4de2160e62b7bb6e21c7d658a42e66424873`;
- `TDG_D2_GIBBS_BETA_INVARIANCE_2026-09-18.md` — commit `25a53bb67b61e7737d8ca73b6426c8f0356e8e63`.

Historically the relation

`K2 ~= (3/130) K3`

was only a strong formal-numerical observation. This checkpoint pushes the relation upstream to the Gram-difference jet and identifies its source coefficient.

---

## 1. Proportionality exists before scalar-memory contraction

Save the complete post-Cons baseline-vs-move Gram coefficient arrays

`D2[C,T]`, `D3[C,T]`

for all 16 legal moves and all 17 base contexts.

At canonical b4 `a=.02`, the global best relation is

[
D_3=lambda_{23}D_2
]

with

`lambda_23 = 43.333333332903024`.

Comparator:

`130/3 = 43.333333333333336`.

Global relative residual:

`3.80e-10`.

Per nonzero local matrix:

- median best ratio `43.33333333290228`;
- range only `43.3333333182 ... 43.3333333603`;
- median local non-collinearity `5.48e-10`;
- max `1.62e-9`.

Thus the relation is already present in the full Gram-difference coefficient tensor. It is not created by `nbasis`, F, the positive Gram, or the S4 multiplicity reduction.

---

## 2. Why the dependence on one extra H insertion is affine

D2 is the first topology-sensitive coefficient.

D3 differs from D2 by exactly one additional Hamiltonian insertion in the formal resolvent/response expansion.

Therefore, when the diagonal parts of H are varied independently, the D3/D2 coefficient must be affine in those one-insertion energies as long as the D2 source itself remains fixed.

This is a structural one-extra-insertion statement, not a fit ansatz.

---

## 3. Exact global-shift coefficient = 10

The scalar Gram response built from parent->B3 resolvent blocks begins at total resolvent order `z^-8`.

The first topology-sensitive move coefficient is D2, hence lies at total order

`z^-(8+2)=z^-10`.

For a uniform scalar Hamiltonian shift

`H -> H + S I`,

the resolvent obeys exactly

`R_H+SI(z)=R_H(z-S)`.

Expanding a leading `z^-10` term under `z -> z-S` produces at the next order the binomial coefficient

`10 S`.

Direct source deformation confirms:

- SHIFT 2 -> ratio `33.3333333330`;
- SHIFT 3 -> `43.3333333329`;
- SHIFT 4 -> `53.3333333327`.

Slope = 10 to numerical floor.

Therefore the `10*SHIFT` term is exact.

---

## 4. Sector split: five B3 and five parent insertion positions

The frozen inter-parent D2 source lives on the `P/F` graph.

Varying only the B3 diagonal offset `MU` gives:

- MU 1 -> ratio `38.3333333331`;
- MU 2 -> `43.3333333329`;
- MU 3 -> `48.3333333326`.

Thus B3-only slope = 5.

Independently adding a scalar `s_P I6` only to the parent-core diagonal gives:

- `s_P=0` -> `43.3333333329`;
- `.5` -> `45.8333333327`;
- `1` -> `48.3333333327`;
- `2` -> `53.3333333326`.

Parent-only slope = 5.

Hence the 10 global insertion positions decompose exactly as:

# **5 B3 positions + 5 parent positions.**

This matches the inter-parent response/Gram path combinatorics.

---

## 5. H0 contribution

The exact local core matrix obeys

[
H_0^2=rac54 H_0,
]

so its spectrum is

`0 x2 + (5/4) x4`.

For every slot, define the canonical parent/B3 port embedding

`C_f=A_f Bcanon_f`.

Exact source identities, verified at arithmetic floor:

[
Q_0^dagger C_f=I_2,
]

[
C_f^dagger C_f=3I_2,
]

[
C_f^dagger H_0 C_f=rac52 I_2.
]

Thus the high-sector fraction carried by a canonical port is

[
rac{C_f^dagger P_{high}C_f}{C_f^dagger C_f}
=rac23.
]

A controlled scaling

`H0 -> s_H H0`

gives D3/D2:

- `s_H=0`: 40;
- `.5`: `41.6666666663`;
- `1`: `43.3333333329`;
- `1.5`: `44.9999999994`;
- `2`: `46.6666666660`.

Therefore the H0 coefficient is exactly the source value

[
rac{10}{3}s_H.
]

The path interpretation is consistent with four response-active parent insertions carrying high-sector weight `2/3`, while the remaining parent insertion lies on the low Q0 anchor where H0 vanishes:

[
4cdotrac23cdotrac54=rac{10}{3}.
]

This insertion typing is the source-level explanation of the non-scalar H0 contribution.

---

## 6. Full affine one-insertion law

The source law is therefore

[
oxed{
lambda_{23}
=
10,S+5,mu+rac{10}{3}s_H
}
]

for the diagnostic deformation in which:

- `S` is the common SHIFT;
- `mu` is the extra B3 diagonal;
- `s_H` scales the frozen H0.

An off-grid adversarial test:

- `S=1.7`;
- `mu=2.3`;
- `s_H=.7`.

Prediction:

`30.833333333333332`.

Direct full D3/D2 measurement:

`30.83333333319863`.

Difference:

`-1.35e-10`;

non-collinearity residual:

`1.94e-10`.

---

## 7. Canonical coefficient

For the actual frozen law:

- `SHIFT=3`;
- `MU=2`;
- `s_H=1`.

Therefore

[
lambda_{23}
=10(3)+5(2)+rac{10}{3}
=40+rac{10}{3}
=rac{130}{3}.
]

Hence

[
oxed{
D_3=rac{130}{3}D_2
}
]

at the first topology-sensitive formal Gram-difference jet, and equivalently

[
oxed{
D_2=rac{3}{130}D_3.
}
]

Because the downstream signed memory map is linear at this order, the same source identity produces the previously measured

`K2=(3/130)K3`

and equal signed kernel/projective classes.

Classification:

# **3/130 D2/D3 PROPORTIONALITY = SOURCE-DERIVED / STRUCTURAL PASS.**

The finite floating residuals measure executable coefficient extraction, not a fitted physical constant.

---

## 8. Consequence for Gate A

The last algebraic caveat in the all-angle move-singular stratum is removed.

At `cos(6 theta)=0`, D2 is killed by its angular scalar and D3 becomes the leader. Since D3 is exactly the same source tensor scaled by `130/3`, its signed kernel and positive projective class are necessarily the same.

Thus the Gate-A all-angle projective/signed coincidence no longer relies on recognizing a stable rational from several numerical runs.

The coefficient is explained by the frozen Hamiltonian energy-insertion algebra.

---

## 9. Firewalls

- diagnostic variation of SHIFT/MU/H0 is an algebraic probe, not a change to the TDG canon;
- only the canonical values define the actual theory;
- no new coefficient is fitted;
- no finite-z readout is used;
- this closes the D2/D3 proportionality, not the nonzero dynamic O3 coefficient itself.

## 10. Next exact target

Return to the primary wall:

# **INTER-PARENT D2 CONSTITUTIVE NONZERO THEOREM**

Use the already-reduced canonical port identities and Cons/S4 incidence to derive the nonzero scalar

`c_D2 ~ 10.7691977`

without decimal recognition.

The remaining question is no longer why D3 follows D2. It is why D2 itself has a nonzero projection on the unique J channel.

## 11. GR traffic light

🟢 **3/130 caveat closed:** the ratio is now sourced by exact energy-insertion structure.

🟢 **Gate-A exceptional move stratum becomes algebraically clean.**

🟢 **No hidden readout/refinement coefficient was needed.**

🟡 **Single remaining local wall:** prove the inter-parent D2 coefficient on J is structurally nonzero.

🔴 **No full/dynamic O3, HDA, spin-2 or nonlinear GR yet.**
