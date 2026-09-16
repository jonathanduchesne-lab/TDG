# Complete TDG / Gate B — exact Q-B1852 recovery + post-event 19D two-orbit A21 continuum pass

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **Q-B1852 PRIMARY SOURCE/REPRO GAP CLOSED / EXACT HISTORICAL PIPELINE RECOVERED / POST-EVENT 19D SAME-Q REBASE FULL-RANK / RADIAL+SIDE ORBIT REPRESENTATIVE A21(C) NONZERO AND B4/B24 CONTINUUM-STABLE / FULL 16-LENS FAMILY NOT YET CLOSED / OPERATOR MOMENT NOT YET RUN / NO ROOT2 NEW LAW**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Scope

The prior Gate-B front established exactly:

- 16 first-event lenses `C` preserving common interface `T0`;
- each post-event carrier `K_C=Kstar+[moves[C]]` has 20 frontier B4 contexts;
- each post-event common-`T0` successor shell has 19 elementary directions;
- the old 16D `F,V,Apoly` therefore cannot simply be reused after actualization;
- the live task is to reconstruct the same Q-B1850/51/52 response pipeline on the genuine post-event shell.

This checkpoint closes the documentary source gap and executes that rebase on the two exact S4 event-orbit representatives.

No GR/O(3) target, preferred `z`, pseudoinverse, fitted mode deletion, fitted transport or new microscopic law is introduced.

---

## 1. Exact historical Q-B1852 source recovered

A full binary handoff archive still exists in the persistent Library:

`/TDG/Recovery/Complete_TDG_Root2_FULL_A_TO_Z_THREAD_HANDOFF_QB1860BW_COMPLETE_2026-08-21.tar.gz`

A recursive read-only traversal of its nested repro chain recovers the exact file

`qb1852_full_refined.py`.

Recovered SHA-256:

`ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`

This exactly matches the historical certified hash pinned in D2/Q-B1857/Q-B1858 provenance.

The entire nested `repro_qb1852` subtree was recovered: 1902 files, including Q-B1850/Q-B1844/Q-B1838 dependencies, historical outputs and verifier.

`sha256sum -c MANIFEST_SHA256.txt` = **PASS, RC=0**.

Historical `python3 qb1852_final_verify.py` = **PASS, RC=0**, ending in:

`QB1852 FINAL PORTABLE VERIFY PASS`.

Therefore:

# **Q-B1852 PRIMARY SOURCE/REPRO GAP = CLOSED.**

---

## 2. Generic post-event rebase is an exact extension of the historical pipeline

The recovered Q-B1852 source computes the base 16D shell from:

- the same `RefinedQ` law;
- current carrier boundary;
- Cons projector;
- local Gram responses;
- one legal extension per shell context;
- `avg_back` on the replaced context;
- scalar memory map `F` and full q,n response map `V`.

A carrier-generic implementation of this same construction was written, with no new coefficients.

### Exact replay control on original Kstar

Applying the generic implementation back to the original 16D `Kstar` shell gives:

- historical-source `F` vs generic `F`: absolute difference `0.0`;
- historical-source `V` vs generic `V`: absolute difference `0.0`;
- historical `RefinedQ` vs custom-carrier `RefinedQ` `F`: `0.0`;
- same for `V`: `0.0`.

It exactly reproduces:

- `||F|| = 5.79152904473554`;
- `rank(F)=16`;
- `cond(F)=3.1821486016256793`;
- `rank(V)=16`.

Thus the 19D construction below is not a nearby model; it is the same executable Q-B1852 response algorithm applied to the post-event carrier.

---

## 3. Exact post-event grammar used

For one first event `C`:

`K_C = Kstar + [moves[C]]`.

Its frontier has 20 B4 contexts, hence

`others_C = boundary(K_C) \ {T0}`

has 19 contexts.

The post-event predictive universe is built by the same historical recursive grammar:

1. add one legal fresh-vertex extension for each of the 19 `others_C` contexts;
2. add the same four next radial support extensions used historically by Q-B1852/Q-B1850;
3. form the current-Q parent universe using the same `Active432Scalar(...,q=.2)` law.

For the tested post-event carriers this gives:

- 29 maximal cells in the complete local grammar;
- 117 coarse parent B4 contexts.

This is a concrete same-Q microscopic realization of the post-event predictive interface. It is **not** promoted as a universal uniqueness theorem over all response-equivalent microscopic realizations.

---

## 4. Two first-event S4 orbits

The original 16 first moves split exactly under the root-slot S4 action into:

- radial orbit: 4 events;
- side/lateral orbit: 12 events.

One representative from each orbit was evaluated.

Full sixteen-lens closure is not yet claimed until explicit post-event S4 covariance is verified.

---

## 5. Post-event F_C and V_C are full rank

For both event-orbit representatives, both refinement schemes `b4`,`b24`, and all tested cutoffs `a=.04,.02,.01`:

- `F_C` has shape `19 x 19` and rank `19/19`;
- `V_C` has shape `80 x 19` and rank `19/19`.

No pseudoinverse, hand quotient or rank rescue is required.

Representative condition numbers:

### a=.02

Radial b4:
- `cond(F_C)=3.4246345059`
- `cond(V_C)=4.1172906975`

Radial b24:
- `cond(F_C)=3.4317512080`
- `cond(V_C)=4.1240738272`

Side b4:
- `cond(F_C)=3.3862293423`
- `cond(V_C)=4.0950397821`

Side b24:
- `cond(F_C)=3.3929660570`
- `cond(V_C)=4.1014542578`

Full rank remains stable at `.04` and `.01`.

Therefore:

# **POST-EVENT Q-B1850/52 MEMORY/RESPONSE MAP DOES NOT LOSE RANK ON THE TESTED TWO-ORBIT FAMILY.**

---

## 6. b4/b24 projective naturality of F_C

After one best global scalar b24->b4, no mode-by-mode fit:

### a=.02

Radial:
- relative `F_C` defect `2.3712842231e-4`;
- cosine `0.999999971885`.

Side:
- relative defect `2.3663721714e-4`;
- cosine `0.999999972001`.

### a=.01

Radial:
- relative defect `5.9057366901e-5`;
- cosine `0.999999998256`.

Side:
- relative defect `5.8935565786e-5`;
- cosine `0.999999998263`.

Halving `a` reduces the defect by approximately four, consistent with an `O(a^2)` refinement discrepancy.

Thus the new 19D response map has strong b4/b24 projective naturality on both event orbits.

---

## 7. Post-event polynomial stencil is reconstructed by the exact historical rule

The historical Q-B1838/Q-B1852 source constructs its sixteen support positions recursively:

- the fresh extension vertex is placed at the barycentre of the B4 attachment face;
- each new boundary B4 context is assigned the barycentre of its four vertices;
- `Apoly` is then the degree<=2 evaluation matrix
  `[1,x,y,z,.5x^2,.5y^2,.5z^2,xy,xz,yz]`.

Applying this same recursive rule before extension reproduces every historical original support position with maximum error

`1.1102230246251565e-16`.

Applying it once more to `K_C` gives a 19-point post-event stencil with:

- affine evaluation rank `4`;
- affine+Hessian evaluation rank `10`;

for both radial and side representatives.

No position is interpolated or fitted to the desired A21 result.

This barycentric stencil remains a polynomial/process presentation chart, not a promoted physical metric scale.

---

## 8. Conditional post-event A21(C) construction

Using exactly the historical Q-B1852 algebra:

- `L_C = V_T0^(C) F_C^{-1}`;
- `J_aff^(C)=L_C Aff_C`;
- `J_H^(C)=L_C Hess_C`;
- `C_Q^(C)=(J_aff^(C))^{-1}J_H^(C)`;
- normalized Sym3 basis exactly as in Q-B1852;
- `A21(C)` = gradient/l=1 rows against the traceless-Hessian/l=2 basis.

No pseudoinverse is used because all required square maps are full rank in the tested cases.

Historical source diagnostic

`CT=[-C[z,xy],-C[y,xz],-C[x,yz]]`

is retained as an auxiliary component readout.

---

## 9. Radial-orbit representative A21 continuum result

### Finite cutoff norms

- b4 `.02`: `||A21||=0.3215104672`
- b4 `.01`: `0.3215853900`
- b24 `.02`: `0.3215448825`
- b24 `.01`: `0.3215936969`

### a^2 continuum extrapolation

b4:
- `||A21_rad|| = 0.3216117566`
- singular values `(0.1990874706, 0.1786033499, 0.1786033159)`
- `CT=(0.1176850085,0.1176846779,0.1176801155)`

b24:
- `||A21_rad|| = 0.3216123060`
- singular values `(0.1990876275,0.1786037467,0.1786037334)`
- `CT=(0.1176832726,0.1176839211,0.1176822255)`

Continuum b4/b24 comparison:

- relative matrix difference `2.7555949136e-5`;
- cosine `0.999999999622`.

Finite b4/b24 relative defects shrink:

`.04: 1.51635e-3 -> .02: 3.72744e-4 -> .01: 9.90854e-5`.

Classification:

# **RADIAL CONDITIONAL A21(C) = NONZERO / STRONG B4-B24 CONTINUUM PASS IN TESTED REALIZATION.**

---

## 10. Side-orbit representative A21 continuum result

### Finite cutoff norms

- b4 `.02`: `||A21||=0.5500005221`
- b4 `.01`: `0.5494546254`
- b24 `.02`: `0.5496724268`
- b24 `.01`: `0.5493632416`

### a^2 continuum extrapolation

b4:
- `||A21_side|| = 0.5492693413`
- singular values `(0.4010699594,0.3475319251,0.1416377704)`
- `CT=(0.0004090414,0.0004069809,0.1703780060)`

b24:
- `||A21_side|| = 0.5492682191`
- singular values `(0.4010635469,0.3475393207,0.1416334299)`
- `CT=(0.0004060891,0.0004059541,0.1703612509)`

Continuum b4/b24 comparison:

- relative matrix difference `7.4026876879e-5`;
- cosine `0.999999997262`.

Finite b4/b24 relative defects shrink:

`.04: 3.59219e-3 -> .02: 8.81790e-4 -> .01: 2.46290e-4`.

Classification:

# **SIDE CONDITIONAL A21(C) = NONZERO / STRONG B4-B24 CONTINUUM PASS IN TESTED REALIZATION.**

---

## 11. Important new physical structure: the two event orbits are genuinely different

The radial and side conditional blocks do not collapse to one identical post-event matrix in the common T0 chart:

- radial continuum norm `~0.321612`;
- side continuum norm `~0.549269`;
- radial singular spectrum has a near-degenerate lower pair;
- side spectrum is strongly anisotropic;
- radial CT is approximately three-equal;
- side CT is dominated by one component `~0.17037` with the other two near `4e-4`.

This is not by itself a symmetry failure. A specific actualized event breaks the full pre-event S4 to its stabilizer, and radial vs side events belong to different initial S4 orbits relative to the fixed common interface `T0`.

The correct next question is covariance of blocks within each orbit and their transformation in the common physical T0 frame.

---

## 12. What is now CLOSED

### CLOSED / STRONG PASS

- exact Q-B1852 source bytes recovered and SHA-certified;
- full nested repro integrity and historical verifier PASS;
- source-gap classification retired;
- exact generic-carrier replay of historical 16D F,V with zero difference;
- post-event 19D F_C,V_C full rank on radial and side orbit representatives;
- b4/b24 projective naturality of F_C with approximately `a^2` discrepancy;
- recursive barycentric polynomial chart exactly replays historical support positions;
- post-event polynomial affine/Hessian ranks 4/10;
- radial representative conditional A21(C) exists, is nonzero and continuum-stable b4/b24;
- side representative conditional A21(C) exists, is nonzero and continuum-stable b4/b24.

### NOT YET CLOSED

- explicit S4 covariance theorem carrying each representative across all members of its orbit;
- complete frozen family of all sixteen A21(C) in one common licensed convention;
- full predictive-quotient universality over every response-equivalent microscopic realization;
- state-universal FP operator moment `M_A21=sum_C P_C tensor A21(C)`;
- state-dependent mean/variance if the operator moment is nonzero;
- O(3), HDA, spin-2 or full nonlinear GR.

---

## 13. Exact next gate

# **POST-EVENT A21 S4 ORBIT-COVARIANCE GATE**

1. Select a second radial event and a second side event.
2. Use the exact root-slot S4 label maps already present in Q-B1838 to map representative event -> target event.
3. Extend the label map canonically to fresh post-event labels by mapping attachment contexts, not by arbitrary fresh-label matching.
4. Verify Q/Cons/Gram and F_C/V_C covariance under row/column relabeling.
5. On the physical T0 chart, transform gradients with the already-earned `Rperm(p)` action and traceless Hessians by `H -> R H R^T`.
6. Verify that directly recomputed `A21(C')` equals the covariantly transformed representative block within numerical/refinement tolerance.
7. If this passes, generate/freeze all 4 radial + 12 side A21(C) blocks from the two representatives and independently spot-check direct recomputations.
8. Only then construct the physical FP operator moment `M_A21`.

---

## 14. GR traffic light

🟢 **Major Gate-B advance:** the source/repro gap is gone and the actual post-event 19D Q-B1852 calculation runs with full rank.

🟢 **Continuum robustness:** both event-orbit representative A21 blocks are nonzero and b4/b24-convergent; scheme differences shrink strongly under refinement.

🟢 **No fit/rescue used:** old 16D pipeline is reproduced exactly, barycentric chart rule is historical, and no pseudoinverse is needed.

🟡 **Immediate live frontier:** prove S4 covariance and close the full sixteen-lens conditional family.

🟡 **After that:** the state-universal FP operator moment decides whether ensemble covariance cancels the conditional obstruction.

🔴 **No GR promotion:** O(3), HDA, spin-2 and full nonlinear GR remain unestablished.
