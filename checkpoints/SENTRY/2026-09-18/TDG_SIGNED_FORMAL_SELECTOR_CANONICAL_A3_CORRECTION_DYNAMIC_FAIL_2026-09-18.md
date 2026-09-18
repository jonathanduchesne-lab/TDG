# Complete TDG — signed formal selector canonical A3 correction / dynamic co-selection re-audit

**Date:** 2026-09-18 (America/Toronto)  
**Status:** **PREVIOUS FORMAL-LEADING T3 FAIL SUPERSEDED / ABSOLUTE-THRESHOLD ARTIFACT IDENTIFIED / SIGNED FORMAL ALL-ANGLE SELECTOR = CANONICAL SIDE-ORBIT A3 STANDARD3 TO NUMERICAL FLOOR / FINITE-z Q-B1854 SELECTOR -> SAME CANONICAL COPY AS O(a^2) / DYNAMIC STF->GRAD OBSTRUCTION REMAINS O(1) / NO O3-DYNAMIC OR GR PROMOTION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Superseded parent interpretation

The immediate parents

- `TDG_SIGNED_ALL_ANGLE_LEADING_SELECTOR_FORMAL_PASS_O3_COMPATIBILITY_FAIL_2026-09-16.md` — commit `bd369a56f9c2d5873656900d7108f98389b0833a`;
- `TDG_SIGNED_FORMAL_VS_FINITE_SELECTOR_SAMEBASIS_SENSITIVITY_2026-09-16.md` — commit `56687ecb5d0512c6a8e35033ad1f46027db784b9`;

correctly established the signed D2/D3 common kernel and the source-level `3/130` ratio, but their conclusion

`formal-leading signed ray has T3 ~ 0.117851 and is not O3-compatible`

is superseded here.

The discrepancy came from the historical diagnostic implementation

`sel = rr > 1e-10`

inside the Q-B1854 `t3` function. The formal selector has four structurally radial-null rows whose floating norms landed just above that absolute threshold, while the finite-z selector often put the same four rows just below it. Treating those numerical nulls as four additional unit directions creates the spurious `~1/(6 sqrt(2))` third moment.

No scientific source law changed. This is a diagnostic-typing correction.

---

## 1. Exact 4+12 orbit decomposition

The 16 same-cut noncentral contexts split S4-invariantly into:

- radial orbit: 4 contexts, the `nbstar` orbit;
- side orbit: 12 contexts.

Each side context intersects `T0` in one unordered edge. For every one of the six edges of `T0`, there are exactly two side contexts.

Define the exact 6D side-pair antisymmetric projector `P_anti` by taking, for each edge pair `(C+,C-)`, the normalized difference

`(e_C+ - e_C-)/sqrt(2)`.

Let `P_std` be the exact S4 character projector onto the ordinary physical Standard3 isotypic sector.

Numerically/arithmeticly:

- `rank(P_anti)=6`;
- `[P_std,P_anti]=0` exactly in the permutation realization;
- `P_can = P_std P_anti`;
- `P_can^T=P_can`;
- `P_can^2=P_can` to `2.5e-16`;
- `rank(P_can)=3`;
- `tr(P_can)=3`;
- radial diagonal entries = exactly 0;
- all 12 side diagonal entries = exactly `1/4`.

Thus `P_can` is an exact combinatorial/S4-defined 3D Standard3 copy supported purely on the side orbit.

---

## 2. Formal signed selector equals the canonical side Standard3

For the formal signed D2 kernel, construct its 3D S4 orbit subspace and projector `P_sel`.

Relative projector defects `||P_sel-P_can||/||P_can||`:

- b4 `a=.04`: `1.98e-9`;
- b4 `a=.02`: `7.49e-9`;
- b4 `a=.01`: `3.20e-8`;
- b24 `a=.02`: `8.94e-9`.

The drift worsens only as the formal coefficient extraction approaches floating cancellation floor.

Principal cosines at b4 `.02` are `(1,1,1)` to displayed precision.

Classification:

# **FORMAL SIGNED D2 SELECTOR = CANONICAL SIDE-ORBIT STANDARD3 = STRONG STRUCTURAL / NUMERICAL-FLOOR PASS.**

Since D3 has the same signed kernel ray, the all-angle signed theorem selects the same `P_can`.

---

## 3. Exact A3 / cuboctahedral typing and T3

On the 12 nonzero side rows of the selected 3D copy:

- the normalized dot spectrum is exactly of A3-root type:
  `{-1,-1/2,0,+1/2,+1}`;
- the 12 directions split into six antipodal pairs;
- each pair corresponds to one unordered edge of `T0`.

This is the normalized A3 root system / cuboctahedral orbit, up to one global orthogonal chart.

Because the set is antipodal, every odd tensor moment vanishes identically. In particular its tetrahedral third-moment obstruction is exactly zero at the representation level.

Numerically, computing T3 only on the nonzero side support gives:

- b4 `.04`: `1.70e-9`;
- b4 `.02`: `6.40e-9`;
- b4 `.01`: `2.72e-8`;
- b24 `.02`: `7.69e-9`.

The four formal radial row norms are only numerical leakage, relative to the side norm:

- b4 `.04`: `2.47e-10`;
- b4 `.02`: `1.55e-9`;
- b4 `.01`: `7.17e-9`;
- b24 `.02`: `1.27e-9`.

Therefore the previous formal `T3 ~ 0.117851` result was produced by normalizing numerical zeros.

Classification:

# **FORMAL LEADING SIGNED ALL-ANGLE SELECTOR -> CANONICAL A3 / O3-COMPATIBLE ANGULAR STANDARD3 = PASS.**

Typing precision: the exact A3 identification is representation/combinatorial; equality of the Q-derived floating selector with that exact projector is verified to numerical floor across scheme/cutoff controls.

---

## 4. Historical finite-z selector converges to the same canonical copy

Using one common historical multiplicity basis `W` and comparing the finite-z Q-B1854 selector at `z=2+.7i` with the formal D2 selector:

### b4 angular separation

- `a=.04`: `4.5690804e-3` rad;
- `a=.02`: `1.1367054e-3` rad;
- `a=.01`: `2.8384751e-4` rad.

Each halving of `a` reduces the angle by approximately 4.

Log-log exponent:

`2.00436`.

Thus:

`finite-z selector -> formal/canonical selector as O(a^2)`.

The side-only T3 values of the finite-z selector are:

- `.04`: `5.5958198e-3`;
- `.02`: `1.3921657e-3`;
- `.01`: `3.4761353e-4`;

with exponent

`2.00440`.

For b24 `a=.02`:

- formal-vs-finite angle: `6.9208825e-4` rad;
- finite side T3: `8.4762337e-4`.

Therefore the historical finite-family Q-B1854 selector is not a distinct physical continuum line. It is an `O(a^2)` regulator/readout deformation of the same exact canonical side Standard3.

---

## 5. Consequence for the signed all-angle gate

The signed Gate-A result is stronger after correction:

- D0=D1 remain structurally zero;
- D2 and D3 signed skews have the same kernel;
- the `3/130` amplitude ratio remains strongly visible;
- the common kernel defines the exact canonical side-orbit Standard3 `P_can`;
- the 12 active directions are A3/cuboctahedral and odd moments vanish by antipodality;
- finite-z Q-B1854H converges to this same selector as `O(a^2)`.

Hence no finite readout is needed to select the continuum angular Standard3.

# **READOUT-FREE / ALL-ANGLE / S4-CANONICAL ANGULAR STANDARD3 SELECTION = CLOSED IN THE TESTED CERTIFIED FORMAL FAMILY.**

This does not imply full dynamical O(3).

---

## 6. Dynamic co-selection re-audit with the corrected canonical selector

The same canonical/formal selector was inserted into the historical Q-B1854 first-jet/second-order test while leaving the current Q prolongation

`L_Q = V F^{-1}`

unchanged.

The traceless-Hessian-to-gradient norm is:

- b4 `.04`: `11.75815258`;
- b4 `.02`: `11.69718095`;
- b4 `.01`: `11.68233264`;
- b24 `.02`: `11.69146287`.

An `a^2` extrapolation on the b4 sequence gives intercept approximately

`11.6771`;

two-point Richardson from `.02,.01` gives

`11.67738`.

The trace-to-gradient leakage remains tiny and decays:

- `.04`: `1.3278e-4`;
- `.02`: `3.3906e-5`;
- `.01`: `8.5230e-6`.

Thus the corrected canonical angular selector does **not** cure the constitutive/dynamic obstruction.

Classification:

# **CANONICAL ANGULAR STANDARD3 = PASS.**
# **SAME STANDARD3 DYNAMIC STF->GRAD CO-SELECTION = STRONG CONTINUUM FAIL.**
# **FULL/DYNAMICAL O(3) = NOT CLOSED.**

The historical Q-B1854J/K dynamic conclusion survives the diagnostic correction and is now stronger because the selector ambiguity has been removed.

---

## 7. Relation to Gate B

Gate B remains independently binding:

- post-event 19D `A21(C)` family is nonzero and S4-covariant;
- universal FP ensemble cancellation fails exactly;
- no physical `rho_Kstar` is derived.

This checkpoint does not yet identify the pre-event `~11.677` STF->grad scalar with the post-event 19D `A21(C)` coefficient. That comparison is the next legal target.

---

## 8. Exact next gate

# **CANONICAL STANDARD3 / DYNAMIC OBSTRUCTION UNIFICATION GATE**

1. Freeze `P_can` as the Q-derived all-angle continuum angular Standard3 selector.
2. Express the surviving pre-event STF->grad map in the Q-derived SO3/little-group `l=2 -> l=1` typing.
3. Determine whether it is the same unique intertwiner ray as the base/post-event `A21` obstruction, modulo already-earned transports and normalizations.
4. Track that map through one actualization event and the genuine 19D post-event shell.
5. If the obstruction is one transported nonzero scalar channel, certify the current RefinedQ constitutive mismatch as structural rather than selector/readout ambiguity.
6. Search only already-earned Q-native cancellations/quotients. No fitted O3 projection, sector deletion, new field, state measure or counterterm.
7. Parallel algebra: derive the exact signed `3/130` ratio from local H-path/Cons algebra.

---

## 9. Firewalls

- old absolute `1e-10` T3 support threshold is not a physical selection law;
- structurally zero radial rows must not be normalized into unit directions;
- use orbit support / exact projector typing instead of absolute floating thresholds;
- angular Standard3 closure does not imply dynamic O3 closure;
- Gate B remains negative;
- Root1 frozen; `A_path` retired; global Q uncollapsed;
- factual ledger append-only/separate;
- Born NOT DERIVED universally;
- metric duration NOT DERIVED; Lambda OPEN;
- no preferred finite z, fitted rotation/counterterm, O3 projector, pseudoinverse rescue, microscopic J, tetrad or ADM/EH target;
- HDA/spin-2/full nonlinear GR remain NOT ESTABLISHED.

## 10. GR traffic light

🟢 **Major correction/advance:** the signed all-angle leader actually selects an exact canonical A3/cuboctahedral Standard3; the prior formal T3 fail was a threshold artifact.

🟢 **Readout ambiguity further reduced:** the historical finite-z selector converges to the same canonical line as `O(a^2)`.

🟢 **Angular/kinematic O3-compatible selector is now readout-free and target-blind in the tested formal family.**

🟡 **Immediate wall is now purely dynamical/constitutive:** same canonical selector still gives STF->grad `~11.677` in the continuum.

🟡 **Next:** unify that pre-event obstruction with the post-event 19D `A21(C)` family.

🔴 **No GR promotion:** full/dynamical O(3), HDA, spin-2 and nonlinear GR remain unestablished.
