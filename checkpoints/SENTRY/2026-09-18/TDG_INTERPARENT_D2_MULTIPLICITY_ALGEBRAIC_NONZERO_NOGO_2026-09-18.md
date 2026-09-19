# Complete TDG — inter-parent D2 multiplicity reduction / algebraic nonzero obstruction

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **D2 INTER-PARENT CONSTITUTIVE WALL REDUCED TO A 3x3 S4 MULTIPLICITY PROBLEM / EXACT ALGEBRAIC NONZERO GIVEN THE SOURCE ORBIT TABLE / CLOSED-FORM c_Q = 938987 sqrt(2) / 123308 / DIRECT b4-b24 PIPELINE AGREEMENT AT FORMAL FLOOR / NO ZERO IDENTITY IN CURRENT REDUCED LAW / NO GR PROMOTION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parents

Immediate parents:

- `TDG_D2_H3_PATH_CLASS_INTERPARENT_CORE_REDUCTION_2026-09-18.md` — commit `4bff4de2160e62b7bb6e21c7d658a42e66424873`;
- `TDG_D2_GIBBS_BETA_INVARIANCE_2026-09-18.md` — commit `25a53bb67b61e7737d8ca73b6426c8f0356e8e63`;
- `TDG_D2_D3_EXACT_3_OVER_130_SOURCE_DERIVATION_2026-09-18.md` — commit `6b2c1aa2f0e1351766d63159cce50dc4dd45fe75`.

Those checkpoints reduced the readout-free dynamic obstruction to the first environment-sensitive D2 coefficient and then to one constitutive H3 mechanism, the inter-parent path

[
P_T	o F	o P_{T'}	o F'.
]

The fine-B4 path is an exact positive refinement copy and cancels from `V F^{-1}`.

---

## 1. Three canonical ordinary-Standard3 copies in the 16-shell

The ordinary Standard3 isotypic sector has multiplicity three.

There is a completely canonical orthogonal decomposition:

1. `R`: radial Standard3, carried by the four radial contexts;
2. `A`: side-pair antisymmetric Standard3, the already-frozen canonical A3/cuboctahedral physical selector `P_can`;
3. `S`: the remaining side-pair symmetric ordinary Standard3.

Let `q_R,q_A,q_S` be normalized vectors in the `-1` fibre of the root transposition `(01)` for those copies.

In the historical shell ordering, exact representatives can be chosen as:

[
q_R=(e_4-e_9)/sqrt2,
]

[
q_A=(-e_5+e_6-e_7+e_8+e_{10}-e_{11}+e_{12}-e_{13})/4
      +(e_{14}-e_{15})/2,
]

[
q_S=(e_5+e_6+e_7+e_8-e_{10}-e_{11}-e_{12}-e_{13})/(2sqrt2).
]

They are mutually orthonormal and generate the three ordinary-Standard3 copies by S4 orbit.

---

## 2. Gradient and Hessian copies are different canonical multiplicity rays

For the canonical A3/cuboctahedral support chart:

- the affine gradient Standard3 lives exactly in copy `A`;
- the off-diagonal STF-Hessian Standard3 `(xy,xz,yz)` lives exactly in copy `S`;
- both have zero projection on the radial copy `R`.

In the normalized `-1` fibre:

[
y_{
abla}=-(4/sqrt3)q_A,
]

up to one global chart sign, while

[
y_{m Hess}=-(4/3)q_S.
]

Thus the dynamic `l=2->l=1` problem is exactly a constitutive transport from multiplicity copy `S` into copy `A`.

---

## 3. Exact rational orbit structure of D2 memory after common local scale is removed

At D2 the inter-parent source carries one common nonzero local spinor/response scale. After factoring that scale, all remaining operations are:

- S4 relabeling;
- equality-only Cons projection;
- arithmetic averaging over equality classes;
- child average-back;
- local face means.

Therefore the shell coefficients are rational incidence coefficients.

The executable source has 15 ordered-pair S4 orbits. Their normalized coefficients collapse to the rational values

[
-3093/7, -1341/4, -48/7, 1, 33/7, 6, 29, 31, 240/7, 243/7, 36, 39,
]

with repeated values on distinct ordered-pair orbits.

A direct reconstruction of the full 16x16 source matrix from these rational orbit values agrees with the fresh executable D2 matrix at:

- b4 `a=.04`: relative defect `2.89e-8` on the full shell matrix; the reduced 3x3 defect is `4.98e-10`;
- b4 `a=.02`: reduced defect `1.91e-9`;
- b24 `a=.02`: reduced defect `2.20e-9`.

The worsening at finer b4 cutoff follows the already-observed formal subtraction floor.

Typing precision: the rational form is fixed by the equality/mean combinatorics once the common local factor is removed; the listed orbit coefficients are independently reconstructed from the certified executable source and checked across refinement controls.

---

## 4. Exact reduced D2 multiplicity matrix

In the ordered multiplicity basis `(R,A,S)`, the common-scale-stripped D2 memory map is

[
oxed{
M=
egin{pmatrix}
-1465/4 & 30sqrt2 & -36\
30sqrt2 & -465 & 30sqrt2\
-26 & 30sqrt2 & -3621/7
end{pmatrix}.
}
]

Equivalently, if one normalizes the `R<->A` entry to one,

[
egin{pmatrix}
-293sqrt2/48 & 1 & -3sqrt2/5\
1 & -31sqrt2/4 & 1\
-13sqrt2/30 & 1 & -1207sqrt2/140
end{pmatrix}.
]

Its determinant is exactly

[
oxed{
det M=-2413123605/28
eq0.
}
]

Thus the ordinary-Standard3 D2 memory block is algebraically invertible.

---

## 5. Exact central output covector

The central T0 Standard3 response, before multiplication by `F^{-1}`, has the shell pattern

[
(0,0,0,0, 1, 9,9,9,9, -1, -9,-9,-9,-9, 0,0)
]

up to one common nonzero response scale and one overall sign convention.

Projection onto the canonical multiplicity basis gives

[
(R,A,S)propto(1,0,18).
]

Equivalently use the normalized row

[
v=(1/18,0,1).
]

The zero A component is exact side-pair symmetry; the factor 18 follows from the radial `±1` pair versus eight side entries of magnitude 9 projected on `q_S`.

Fresh executable controls give `R/S=1/18` to:

- b4 `.04`: `3e-10`;
- b4 `.02`: `1.2e-9`;
- b24 `.02`: `1.5e-9`;

while the A component remains at the numerical cancellation floor.

---

## 6. Constitutive row and exact nonzero coefficient

The multiplicity-space constitutive row is, up to irrelevant common scales,

[
ell=vM^{-1}.
]

Exact inversion gives

[
ell_R=-1850/53624969,
]

[
ell_A=-61654sqrt2/482624721,
]

[
ell_S=-938987/482624721.
]

Both physically relevant components are manifestly nonzero:

[
ell_A
eq0,qquad ell_S
eq0.
]

Because the gradient injection has magnitude `4/sqrt3`, the Hessian-S injection has magnitude `4/3`, and the normalized unique S4 intertwiner `J` has three equal singular channels, the Frobenius coefficient multiplying normalized `J` reduces exactly to

[
c_Q=ell_S/ell_A.
]

Hence

[
oxed{
c_Q=rac{938987sqrt2}{123308}.
}
]

Numerically,

[
c_Q=10.769197053654470112ldots
]

and therefore

[
oxed{c_Q
eq0.}
]

No decimal recognition is needed for the nonzero conclusion once the reduced source orbit table is fixed.

---

## 7. Direct full-pipeline verification

Using the complete saved D2 `F_2,V_2` matrices and the canonical A3 chart, with no reduced-matrix substitution:

### b4

- `a=.04`: `c=10.769197065782972`, relative difference from exact reduced value `~1.13e-9`;
- `a=.02`: `c=10.769197099596418`, relative difference `~4.27e-9`;
- `a=.01`: `c=10.769197239481128`, entering the known formal subtraction floor.

### b24

- `a=.02`: `c=10.769197109075982`, relative difference `~5.15e-9`.

The full 3x5 STF->gradient map lies on normalized `J` with residual:

- b4 `.04`: `2.31e-9`;
- b4 `.02`: `9.44e-9`;
- b24 `.02`: `1.16e-8`.

Thus the exact reduced algebra and the unreduced executable pipeline agree to the formal numerical floor.

---

## 8. No-zero identity consequence inside current RefinedQ

At first environment-sensitive order, the current law has now reduced to:

1. one canonical Hessian Standard3 copy `S`;
2. one canonical gradient Standard3 copy `A`;
3. one invertible D2 multiplicity memory block `M`;
4. one nonzero central output row `v`;
5. one unique S4 intertwiner `J`;
6. an exact nonzero coefficient
   `c_Q=938987 sqrt2 / 123308`.

The fine-B4 contribution is only a positive refinement-scaled copy; Gibbs-beta scale cancels; finite-z choice is absent; D3 is exactly proportional to D2.

Therefore there is no remaining cancellation among already-present D2 path classes, refinement sectors, readout phases, Standard3 copies, or Gibbs probe weights that can set this coefficient to zero.

Any cancellation would have to change at least one of the frozen multiplicity/incidence maps above. That would be a genuinely new constitutive mechanism, not a reinterpretation of the present RefinedQ law.

Classification:

# **CURRENT REFINEDQ D2 l2->l1 CONSTITUTIVE CHANNEL = ALGEBRAICALLY NONZERO IN THE REDUCED SOURCE LAW.**

# **FULL DYNAMIC O(3) CLOSURE IN THE PRESENT REFINEDQ REALIZATION = FAIL AT FIRST ENVIRONMENT-SENSITIVE ORDER.**

This is a no-go for the current realization, not a theorem that no extension of TDG can repair the constitutive law.

---

## 9. What remains open after this no-go

The constructive research question changes.

It is no longer:

- find another readout;
- choose another Standard3;
- average over lenses;
- use b24 instead of b4;
- resum higher formal orders;
- tune the local Gibbs probe.

Those routes are exhausted for this channel.

The next legal question is:

# **WHAT ALREADY-MOTIVATED Q-NATIVE EXTENSION CAN MODIFY THE INTER-PARENT MULTIPLICITY MAP WITHOUT BEING FITTED TO O(3)?**

Candidates may only come from independently motivated unresolved structure already present in the program, e.g. a retained paused route such as H5, an independently required operator-valued/process-comb completion, or another previously earned degree of freedom.

No extension may be introduced solely because it cancels `c_Q`.

---

## 10. Firewalls

- this no-go is realization-specific: current RefinedQ, not all possible TDG;
- no counterterm or O3 projector may be inserted by hand;
- no sector deletion;
- no physical `rho_Kstar` is inferred;
- Born remains NOT DERIVED universally;
- duration NOT DERIVED; Lambda OPEN;
- HDA/spin-2/nonlinear GR remain NOT ESTABLISHED.

## 11. GR traffic light

🟢 **Exact localization achieved:** the dynamic wall is one 3x3 multiplicity calculation.

🟢 **Nonzero coefficient obtained in closed form:** `938987 sqrt2 / 123308`.

🟢 **All previously suspected presentation/readout/refinement rescues are eliminated for this channel.**

🟡 **Research direction must now change:** only an independently motivated Q-native constitutive extension can reopen dynamic O3.

🔴 **Current RefinedQ itself cannot close full dynamic O3 at D2. HDA/spin-2/GR therefore remain closed.**
