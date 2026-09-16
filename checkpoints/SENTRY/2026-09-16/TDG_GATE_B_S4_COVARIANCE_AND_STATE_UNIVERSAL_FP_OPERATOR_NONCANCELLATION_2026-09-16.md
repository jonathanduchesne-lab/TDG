# Complete TDG / Gate B — S4 covariance of conditional A21 family and state-universal FP operator noncancellation

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **POST-EVENT A21 S4 COVARIANCE = STRUCTURAL EXACT / DIRECT NUMERICAL STRONG PASS UNTIL FLOATING FLOOR / 4+12 ORBIT FAMILY REDUCES TO TWO REPRESENTATIVES / STATE-UNIVERSAL FP OPERATOR CANCELLATION = EXACT FAIL / NO NEW ROOT2 LAW**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Parent

Immediate parent checkpoint:

`TDG_GATE_B_QB1852_SOURCE_RECOVERY_POST_EVENT_19D_TWO_ORBIT_A21_CONTINUUM_PASS_2026-09-16.md`

commit `2c97b281bddbe80f4d2fbea317ea515a7476c29a`.

That checkpoint established:

- exact historical Q-B1852 source/repro recovered and verifier PASS;
- old 16D source pipeline replayed exactly;
- genuine post-event common-T0 shell has 19 legal successor directions;
- post-event `F_C:19x19` and `V_C:80x19` are full rank on radial and side event representatives in b4/b24 at a=.04,.02,.01;
- post-event polynomial stencil follows the historical barycentric rule, rank 4/10;
- radial and side representative `A21(C)` blocks are nonzero and strongly b4/b24 continuum-stable.

This checkpoint closes the orbit-covariance typing and evaluates the stronger state-universal FP operator criterion.

---

## 1. Exact S4 covariance of the post-event construction

The historical Q-B1838/Q-B1852 construction already supplies:

- exact root-slot S4 label maps `labelmap(p)`;
- exact context relabeling `mapC`;
- orthogonal spatial Standard3 action `Rperm(p)`;
- exact S4 automorphisms of the pre-event carrier grammar.

Fresh exact check on the historical support chart:

`pos(mapC(C,p)) = Rperm(p) pos(C)`

for all 24 root-slot permutations, with maximum floating defect about `2e-16`.

The post-event construction is built exclusively from relabeling-natural operations:

1. frontier incidence/multiplicity;
2. fresh-vertex legal attachment;
3. `Active432Scalar` incidence Q law;
4. b4 or b24 refinement of the same relabeled parent set;
5. current-Q resolvent blocks;
6. Cons equalities on shared B3 pairs;
7. `local_grams`;
8. `avg_back` on the four children replacing the moved context;
9. permutation-invariant `tau=(1,1,1,1)` in `rcoord`;
10. the permutation-covariant `nbasis` sign convention;
11. the historical barycentric support chart;
12. affine/Hessian polynomial evaluation;
13. ordinary invertible linear solves for `F_C`, `J_aff`, and the Hessian response.

Therefore the complete conditional construction commutes with the root-slot relabeling.

For the physical spatial chart,

`x' = R_p x`,

so gradients transform by

`g' = R_p g`,

and symmetric traceless Hessians by

`H' = R_p H R_p^T`.

Let `D2(p)` be the induced orthogonal 5D matrix on the historical normalized traceless-Hessian basis. Then structurally

# `A21(pC) = R_p A21(C) D2(p)^(-1)`.

The induced `D2` matrices have orthogonality defect at floating floor (`~1.4e-15` in the direct controls).

This is a covariance theorem of the already-fixed construction, not an O(3)/GR assumption.

---

## 2. Direct independent b4 spot checks

Two directly recomputed event pairs were compared with the covariantly transported representative, without fitting the target block.

### Radial orbit

Representative:

`C=(1,2,3,5)`

target:

`C'=(0,2,3,6)`

root permutation:

`p=(1,0,2,3)`.

Relative matrix defects:

- `a=.04`: `9.0220402514e-5`;
- `a=.02`: `2.2004509868e-5`;
- `a=.01`: `9.4269046812e-5`.

At `.02`, cosine = `0.999999999779`.

### Side orbit

Representative:

`C=(0,1,4,7)`

target:

`C'=(0,1,4,8)`

root permutation:

`p=(0,1,3,2)`.

Relative matrix defects:

- `a=.04`: `1.8331455506e-4`;
- `a=.02`: `4.5741375174e-5`;
- `a=.01`: `1.7560616506e-4`.

At `.02`, cosine = `0.999999999220`.

From `.04` to `.02`, both defects decrease by approximately a factor four, consistent with the known `O(a^2)` refinement discrepancy. At `.01`, the full-vector response scale has fallen to roughly `1e-13`, and subtraction/solve noise dominates; the rising `.01` defect is therefore retained as a floating-precision floor, not used as continuum evidence.

A direct b24 two-carrier recomputation exceeded the available runtime window. No numerical b24 S4 number is fabricated. This does not affect the structural relabeling theorem; independently, the representative radial and side post-event blocks already have strong b4/b24 continuum agreement from the parent checkpoint.

Classification:

# **POST-EVENT A21 S4 ORBIT COVARIANCE = STRUCTURAL EXACT / DIRECT STRONG NUMERICAL CONTROL.**

---

## 3. Full sixteen-lens family reduces to two representatives

The exact pre-event S4 action splits the 16 T0-preserving first events into two transitive orbits:

- radial: 4 events;
- side: 12 events.

The structural covariance theorem therefore determines every member of each orbit from one directly evaluated representative:

`A21(C)=R_p A21(C_rep) D2(p)^(-1)`

for any `p` carrying the representative to `C`.

No sixteen independent constitutive choices exist.

The full conditional family is thus typed by the two already-frozen continuum representatives, subject to their stabilizer covariance, which follows from the same exact relabeling theorem.

---

## 4. Q-B1819 effects needed for the ensemble operator

Q-B1819A/F gives, for an elementary extension along active B4 interface `T`:

`A_e^dag A_e = 3 a^2 P_T`,

where `P_T` is the projector on the **eight B3-port degrees of the active B4 interface T**.

The Stinespring/FP effect is

`K_e^dag K_e = (1/2) P_T`.

On every tested closed frontier,

`sum_e A_e^dag A_e = 6 a^2 P_frontier-B3`

because every frontier B3 belongs to exactly two frontier B4 contexts.

Thus the physical extension effects have a concrete incidence support; they are not analyst weights.

The overall factor `1/2` is irrelevant for testing whether the conditioned operator moment vanishes.

---

## 5. Exact Kstar incidence at the common interface

For the actual Gate-B base carrier:

`T0=(0,1,2,3)`

and

`boundary(Kstar) = {T0} disjoint_union others`, `|others|=16`.

Every frontier B3 has incidence exactly two.

The four B3 faces of `T0` have the following exact two-parent incidences:

- `(0,1,2)` belongs to `T0` and `(0,1,2,8)`;
- `(0,1,3)` belongs to `T0` and `(0,1,3,7)`;
- `(0,2,3)` belongs to `T0` and `(0,2,3,6)`;
- `(1,2,3)` belongs to `T0` and `(1,2,3,5)`.

After conditioning on the T0-preserving lens ensemble, the extension **along `T0` itself is excluded**. Therefore, on each of these four B3-port subspaces, exactly one allowed event effect remains: the corresponding radial lens.

This is the decisive support separation.

---

## 6. State-universal FP operator criterion

The already-defined stronger Gate-B criterion is the operator moment

`M_A21 = sum_(C in others) P_C tensor A21(C)`

(up to the irrelevant common Stinespring factor `1/2`).

State-universal ensemble cancellation for all separating admissible parent states requires

`M_A21 = 0`

on the conditioned support.

Choose, for example, the B3-port subspace corresponding to

`F=(1,2,3) subset T0`.

Within the allowed conditioned 16-lens domain, this B3 is contained in exactly one interface projector:

`P_(1,2,3,5)`.

Therefore the restriction of the operator moment to that B3-port subspace is

`M_A21|_F = I_F tensor A21((1,2,3,5))`

(up to a common nonzero normalization convention for `P_F`).

The radial conditional block is already independently established nonzero, with continuum norm approximately

`||A21_rad|| = 0.321612`

and nonzero singular values approximately

`(0.1990875, 0.1786035, 0.1786035)`.

Hence

# `M_A21|_F != 0`,

and therefore

# **`M_A21 != 0`.**

No cancellation among the other 15 events can alter this restriction because none of their interface effects has support on this conditioned-isolated B3 port.

The same proof applies independently to each of the four T0 boundary faces/radial lenses.

---

## 7. Gate-B universal verdict

# **STATE-UNIVERSAL FP ENSEMBLE CANCELLATION OF THE CONDITIONAL A21 OBSTRUCTION = EXACT FAIL.**

This is stronger than a numerical nonzero weighted average:

- no parent state was selected;
- no occurrence probabilities were fitted;
- no analyst-uniform averaging was used;
- no b4/b24 scale matching is needed for the nonzero-support proof;
- no side-orbit details are required for the decisive restriction;
- no GR/O(3) target enters.

It follows only from:

1. exact Q-B1819 interface-effect support;
2. exact Kstar frontier incidence;
3. exact conditioning that excludes the T0 extension;
4. independently nonzero radial post-event `A21`.

---

## 8. What remains open after the universal failure

The exact universal failure does **not** imply every particular parent state has a nonzero scalar/mean obstruction under every readout. A special state could have zero support on the decisive radial B3 sectors or exhibit a state-specific weighted cancellation among supported sectors.

Therefore the next legitimate question is state-dependent:

1. recover/define the actual current parent predictive state `rho_Kstar` at the declared Q-B1819/FP interface;
2. compute the physical conditioned weights
   `mu_T0(C|rho)=Tr(rho P_C)/Tr(rho B_T0)`;
3. form the state-dependent transported mean and variance of the 16 conditional `A21(C)` blocks;
4. determine whether the actual Q-native parent state cancels, suppresses or retains the obstruction.

But this is now a **special-state question**, not a universal symmetry-restoration theorem.

---

## 9. Firewalls

- Born remains NOT DERIVED as a universal factual winner law; Q-B1819F supplies the already-frozen conditional FP extension instrument in its finite configuration scope.
- Do not replace `Tr(rho P_C)` by uniform lens weights unless the state itself proves them uniform.
- Do not infer a state-specific conclusion from the operator noncancellation theorem.
- Do not delete radial support sectors to force `M_A21=0`.
- No preferred z, fitted transport, pseudoinverse, GR projector or added field is used.
- O(3) remains FAIL / NOT CLOSED.
- HDA / spin-2 / full nonlinear GR remain NOT ESTABLISHED.

---

## 10. Exact next gate

# **ACTUAL KSTAR FP STATE / CONDITIONED A21 MEAN-VARIANCE GATE**

Recover the physical parent state used by the Q-B1819 configuration-Q/FP construction on `Kstar`, preserving the distinction between:

- local/interface support state;
- predictive/global Q state;
- factual ledger.

Then compute the true 16-lens conditioned weights and the state-dependent A21 mean/variance.

Do not assume a symmetric/uniform state unless it follows from the recovered parent construction.

---

## 11. GR traffic light

🟢 **Major closure:** the sixteen conditional blocks are no longer sixteen independent unknowns; exact S4 covariance reduces them to the two established orbit representatives.

🟢 **Major Gate-B result:** state-universal FP cancellation is ruled out exactly by an isolated T0-boundary B3 support sector.

🟡 **Next:** determine whether the actual Q-native Kstar parent state happens to suppress/cancel the obstruction state-dependently.

🟡 **Interpretation pressure increases:** if the actual state also retains the block, Gate B will no longer offer ensemble restoration of the non-O(3) mixing in the current construction.

🔴 **No GR promotion:** this is a negative closure of one rescue route, not a derivation of O(3), HDA, spin-2 or nonlinear GR.
