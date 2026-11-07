# TDG / Root2: unrestricted exploratory GR bridge laboratory

**Date:** 2026-11-06  
**Status:** RESEARCH SANDBOX, NOT A NEW CERTIFIED TDG RESULT.  
**Frozen parent:** https://github.com/jonathanduchesne-lab/TDG/blob/main/CURRENT_FRONT_LATEST.md  
**Reproduction:** `tdg_bridge_sans_barrieres_2026_11_06.py` and `tdg_bridge_sans_barrieres_resultats.json`.

## Aim and controls

Try previously forbidden repairs, without claiming any of them was derived from the original Q law. Inputs from documented TDG work: (i) 2 physical TT configurations in the conditional B5 parent, (ii) a scalar-only B5 correction `DeltaW=(15/4)|I><I|`, (iii) a nonzero STF(l=2)->vector(l=1) obstruction in the current Q dynamic, (iv) a non-null rank-3 vertical SU2/frame process curvature, (v) a Q-rich 42/42 Cauchy-surjective local chart and a 6-dimensional dark B5 host. The later MRP9A chart reconstruction is documented as incomplete. We do not replace missing Q data with guessed matrices.

Critical distinction: the 3x5 matrix below shares the irreducible tensor *type* of the TDG obstruction. It is **not** the original Q-B1854 operator. The historical magnitude 11.6773 is only a label/scale for a diagnostic, and never a calculated new TDG residual.

## A. Tensor obstruction: what repairs are even algebraically possible?

Let `T` be a real symmetric traceless 3x3 tensor and `n` a unit vector. A canonical illustrative map STF2 -> vector1 is `A_n(T)=T n`, of rank 3. B5 acts only on the trace and annihilates all STF tensors, so it cannot cancel `A_n` regardless of its scalar activation.

- Illustrative 3x5 obstruction rank: **3**.
- Nonzero singular values after multiplying by historical diagnostic scale 11.6773: **13.4838, 11.6773, 11.6773**; these are NOT Q eigenvalues.
- B5 pure-trace action on all five STF basis elements: **1.69e-16** (zero at numerical precision).
- A by-hand counterterm `-A_n` cancels the full cross block exactly. This is a tautology, not a physical derivation; any such correction has rank at least 3 for this example.

One can instead make `n` a transforming physical field. Then `A_{Rn}(R T R^T)=R A_n(T)` exactly (numeric defect 1.27e-16). If the same `n` is frozen during the rotation, covariance fails (example norm 0.811). Averaging random `n` kills the linear mean but not the variance: `E_n ||Tn||^2 = ||T||_F^2/3`. Thus merely averaging the obstruction is not an acceptable symmetry repair.

## B. New genuine SO3 Gauss capacity in a cotriad (not original Q)

Introduce an invertible cotriad `E^a_i` (3x3) and momentum `P^a_i`. Let `h=E^T E`, and on the Gauss surface `P=2 E pi` for symmetric canonical metric momentum `pi`. The local rotational moment map is `G_a=epsilon_abc sum_i E_bi P_ci`.

Verified exactly/numerically:

- Internal frame rotations `E->R E`, `P->R P` leave `(h,pi)` unchanged (metric error ~7e-16).
- The canonical one-form `sum P dE = sum pi dh` holds on the Gauss surface (error ~1.39e-17).
- The Poisson algebra is `{G_a,G_b}=epsilon_abc G_c` (residual 0 in numeric analytic-gradient verification).
- Generic internal gauge orbit rank is 3.
- Cotriad phase-space dimension 18 minus 3 first-class Gauss constraints minus 4 first-class ADM constraints = 4 physical phase-space dimensions, or 2 configuration degrees of freedom, **provided** the full first-class ADM constraints are supplied and consistent.

This is a legitimate kinematic bridge into triad geometrodynamics. It does NOT prove the real Q-port rank-3 curvature is gauge-null. The historical Q obstruction is relationally observable; changing its status would alter the original physical theory and requires recertification.

## C. Exact non-linear GR wave sector from two tensor profiles

Construct an explicit four-metric:

`ds^2=-2du dv + dx^2+dy^2 + H(u,x,y) du^2`,

`H=f(u)(x^2-y^2)+2g(u)xy`.

The symbolic SymPy Christoffel and full Ricci computation yields `Ricci_{mu nu}=0` **exactly for arbitrary smooth f,g**. However the Riemann components are nonzero:

- `R_{uxux}=-f(u)`;
- `R_{uxuy}=-g(u)`;
- `R_{uyuy}=+f(u)`.

This is an exact nonlinear Einstein vacuum solution, not a linearized-only match, and it carries two arbitrary wave profiles matching the **count and tensor polarization type** of a two-helicity graviton sector.

**Limit:** the functions f and g have not been calculated from TDG Q. Mapping its two tensor observables to these GR profiles is an explicit *conditional embedding* into a known Einstein solution, not an emergence theorem or a prediction of TDG. It does not solve general cosmological or matter-coupled geometry.

## D. Is a scalar B5 relation activated by record retention alone?

An illustrative *chosen* law `beta_N=1-|cos(0.7)|^N` grows from 0 to 1 as the decohering record count N rises; e.g. beta_16=0.9863, beta_32=0.99981. This can switch on a scalar relation, but the formula is new physics by assumption, not a consequence of Q. Even at beta=1 it cannot remove a traceless STF-to-vector obstruction.

Pure non-selective dephasing does not enforce a state constraint. A scalar population initially equal to 0.4 remains 0.4 under arbitrarily strong dephasing. An independently chosen amplitude-damping jump changes it to `0.4 exp(-3t)` and makes it asymptotically vanish, while leaving an initially forbidden-free subspace unchanged. The jump operator is an additional constitutive input; it is not ordinary dephasing and has not been derived from TDG.

## E. A more interesting repair: strong environmental monitoring (Zeno)

Take a canonical 8-state model `V3 + STF5`, with Hamiltonian mixing between the vector and tensor sectors through A and an otherwise SO3-invariant block-diagonal Hamiltonian. Add the standard trace-preserving projector-dephasing Lindbladian, at rate gamma:

`drho/dt = -i[H,rho] + gamma(P1 rho P1 + P2 rho P2 - rho)`.

Because P1 and P2 project onto SO3 irreducible sectors, the *monitoring operation itself* is rotation-invariant. For a fixed test duration t=1 the following is **numerically verified**:

| gamma | vector-sector leakage probability | SO3 covariance defect (Frobenius norm, test state) |
| ---: | ---: | ---: |
| 0 | 57.51% | 0.7400 |
| 1 | 43.25% | 0.5183 |
| 5 | 20.37% | 0.2237 |
| 20 | 6.68% | 0.0734 |
| 100 | 1.46% | 0.0162 |
| 500 | 0.30% | 0.00331 |

This is the promising **conditional** finding: a measurement/record channel can quench unwanted mixing *dynamically*, without inserting the target-specific counterterm -A. If such a monitoring rate emerges from Q and grows sufficiently fast under a continuum limit, effective rotational invariance might be restored at finite observation times.

**Crucial failure:** it is not a uniform all-time limit. At any finite gamma, the two-level coupled control has population leakage -> 1/2 as t -> infinity. The exact analytic slow eigenvalue scales as `-4g^2/gamma`. For a family t=gamma and gamma->infinity, leakage tends to `(1-exp(-4g^2))/2`, about 0.49084 for g=1, NOT 0. Strong monitoring first and infinite time first do not commute.

The original Q dynamics may contain other symmetry defects; this toy tests only one representation crossing. The measurement operators are not Q-derived, and the required gamma(refinement,records) scaling is unspecified.

## F. Minimal speculative completion and real remaining gap

The strongest speculative strategy with the smallest direct cancellation is:

1. Keep the Q/Ext/Cons regional memory structure and identify physically recorded events through quantum instruments.
2. Seek a *Q-generated* projector-monitoring channel onto the retained physical tensor sector. If gamma(a)->infinity appropriately while TT dynamics survives, STF-to-vector mixing can become ineffective in a finite-time continuum limit (Zeno mechanism).
3. Let a physically generated stable record activate a scalar relation if a non-dephasing admissibility mechanism is discovered. It cannot be presumed from simple loss of coherence.
4. Lift Q-derived positive definite `h` to cotriad `E` and demand an actual Q-induced first-class SO3 moment map. The kinematic cotriad construction proves capacity but not such an origin.
5. Demand full ADM/HDA closure with the *same Q-derived dynamic h*, then self-consistent graviton self-coupling. Standard Einstein-Hilbert/ADM supplies such a completion if imported, but that is a change of theory, not a TDG theorem.
6. Only then claim a general nonlinear GR bridge. The exact pp wave is merely an explicit nontrivial subfamily of the imported target.

**The essential missing theorem:** the very same original Q/memory/process law must derive the relevant monitoring rate, the non-dephasing scalar admissibility rule, and a first-class Gauss/HDA dynamics. No microscopic source is yet identified. Do not call this an achieved derivation of Einstein gravity.

## Scientific status ledger

- **DERIVED in sandbox:** rank/type checks; B5 scalar orthogonality; covariance tests; canonical SO3 Gauss algebra; canonical one-form; correct 2-DOF count conditional on ADM; exact two-profile Ricci-flat pp-wave metric; numerical Zeno suppression and its nonuniform infinite-time caveat.
- **ASSUMED:** toy cross-block resembles original Q type; gamma is environmental monitoring; scalar damping/beta activation; physical identification of Q observables with cotriad/GR wave functions; standard ADM as complete nonlinear dynamics.
- **UNPROVEN:** any quantitative improvement of original Q-B1852 STF l2->l1 coefficient; original Q-port curvature becomes genuine gauge; original MRP9B source recovered; Q-native graviton bootstrap; universal Einstein equations or unique factual outcome.
- **NEXT DECISIVE EXPERIMENT:** reconstruct a Q-native open-process superoperator on the actual 101-parent/154-face carrier, evaluate physical spectral amplitudes with/without a genuinely derived record-monitoring channel, then verify Q-predictive quotient, tensor propagation, HDA bracket, and independent b4/b24 refinement. No fit to desired GR residual is allowed at this decisive stage.

## External conceptual foundations

- S. Deser, *Self-Interaction and Gauge Invariance* (1970), https://arxiv.org/abs/gr-qc/0411023
- Hojman, Kuchar, Teitelboim, *Geometrodynamics Regained* (1976), DOI 10.1016/0003-4916(76)90112-3
- Ashtekar variables / Gauss constraint, https://www.scholarpedia.org/article/Ashtekar_variables
- W. Zurek, Quantum Darwinism, https://www.nature.com/articles/nphys1202
- Exact pp-wave geometry as a known Einstein vacuum family (Brinkmann metric).

**Final verdict:** An Einstein-compatible *conditional completion* can be constructed with explicit verified mathematics, and a plausible decoherence-based suppression mechanism emerges in a toy sector. Nothing here proves a Q-derived or observationally validated bridge from TDG to full GR. The original TDG repository has not been changed.
