# Complete TDG / Gate A — all-angle leading positive-projective class exhaustion

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **ALL REAL ANGULAR RAYS EXHAUSTED INTO THREE STRATA / D0=D1 EXACT STRUCTURAL ZERO / PI/8 BASE-SINGULAR STRATUM SAME PROJECTIVE CLASS / COS6-ZERO MOVE-SINGULAR STRATUM SAME PROJECTIVE CLASS TO STRONG FORMAL-NUMERICAL PRECISION / NO FOURTH EARLY STRATUM / NO NEW ROOT2 LAW**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Binding parents

1. `TDG_GATE_A_FULL_PIPELINE_GENERIC_VS_PI8_PROJECTIVE_COINCIDENCE_PASS_2026-09-16.md`  
   commit `b8c4ce3ca721984f75221f392724857ae09bc24f`.

2. `TDG_GATE_A_COS6_ZERO_D3_PROJECTIVE_COINCIDENCE_PASS_2026-09-16.md`  
   commit `a1ad5b234120f9eff7e99306c417a0bfaecc0df0`.

3. `TDG_GATE_A_D0_D1_EXACT_STRUCTURAL_CANCELLATION_PROOF_2026-09-16.md`  
   commit `61134fae88ae3b273069ab26f9d15b387a076456`.

The recovered certified Q-B1852/Q-B1850 source/repro chain remains the executable scientific source.

---

## 1. Exact upstream ray law

For `z=r exp(i theta)`, the Hermitianized response coefficients carry the exact angular factors

`cos((k+4) theta)`.

At the full formal Q-B1850 baseline-vs-move level, the exact structural result now established is

`D0 = D1 = 0`.

The first environment-sensitive move coefficient is therefore `D2`; if its angular factor vanishes, the next surviving coefficient is `D3`.

For the base Gram, the generic leader is `G0`; if its angular factor vanishes, `G1` is the next leader.

Thus only the zeros of

- `cos(4 theta)` for the base leader;
- `cos(6 theta)` for the first move-difference leader

can change the leading full-pipeline typing at the orders relevant here.

---

## 2. The three and only three leading angular strata

### Stratum A — generic

If

`cos(4 theta) != 0` and `cos(6 theta) != 0`,

then

- base leader = `G0`;
- move leader = `D2`;
- scalar-memory coefficient matrix = the generic `K2` built using `nbasis(G0)`.

Positive response class:

`[R_gen] = [K2^dag K2]`.

### Stratum B — base-singular

If

`cos(4 theta) = 0`,

then necessarily

`cos(5 theta) != 0`.

Reason: simultaneous zeros would require

`(2m+1)/8 = (2n+1)/10`,

which after clearing denominators would equate an even integer with an odd integer.

Also `cos(6 theta)` cannot vanish simultaneously with `cos(4 theta)` by the same parity obstruction between denominators 8 and 12.

Therefore:

- base leader = `G1`;
- move leader = `D2`.

The parent checkpoint establishes across b4 `.04,.02,.01` and b24 `.02`:

`G1 = 34.5 G0`

to arithmetic precision, with the historical `nbasis` invariant under nonzero overall scale/sign.

Consequently the leading full-pipeline matrices satisfy

`K_gen = 34.5 K_base-sing`

and the positive operators satisfy

`R_gen = 34.5^2 R_base-sing = 1190.25 R_base-sing`

with relative residuals at `~1e-15`.

Hence

`[R_base-sing] = [R_gen]`.

### Stratum C — move-singular

If

`cos(6 theta) = 0`,

then necessarily

- `cos(4 theta) != 0`;
- `cos(7 theta) != 0`.

Again the simultaneous-zero equations reduce to parity contradictions.

Therefore:

- base leader = `G0`;
- `D2` is killed by the angular factor;
- move leader = `D3`.

The parent checkpoint establishes full-pipeline rank-16 projective coincidence

`K2 ~= (3/130) K3`

across b4 `.04,.02,.01` and b24 `.02`, with residuals from approximately `1e-10` to `2e-9` as the coefficient scale approaches the floating floor.

The corresponding positive operators obey

`[K3^dag K3] = [K2^dag K2]`

to the same strong formal-numerical precision.

The simple rational `3/130` is stable across regulator and refinement scheme, but its exact symbolic derivation is not yet promoted.

---

## 3. No fourth stratum exists at leading order

Because `D0=D1=0` exactly, a move-response leader cannot occur before `D2`.

Because `cos(4 theta)=0` and `cos(6 theta)=0` cannot occur simultaneously, there is no ray requiring both a shifted base leader and a shifted move leader at once.

Because:

- `cos(4 theta)=0 => cos(5 theta)!=0`;
- `cos(6 theta)=0 => cos(7 theta)!=0`,

neither exceptional family can suppress two consecutive relevant leaders.

Therefore every real `theta` lies in exactly one of the three cases above.

This is an exhaustive angular classification of the leading full Q-B1850 response-resonance class.

---

## 4. Structural reason D0=D1 vanish

The exact certified Hamiltonian block graph gives

`U0(T,F)=P_F H P_T = H_FT`,

and, because there is no B3-B3 off-diagonal coupling and no other two-step sector connects the same parent-face pair,

`U1(T,F)=P_F H^2 P_T = H_FF H_FT + H_FT H_TT`.

Thus `U0,U1` depend only on the local `(T,F)` pair and its slot typing.

Q-B1818G certifies exact functorial extension `I^dag H_K' I = H_K`; Q-B1818H certifies the exact S4-covariant one-context to four-context replacement.

Under the canonical fresh-slot relabeling used by `avg_back`, every child has the same local `U0,U1` as the replaced parent. Hence the response/Gram coefficients `G0,G1`, which depend only on these moments, are identical before and after the move at these orders.

They are already in the Cons-fixed subspace; the Cons coequalizer acts as identity on them.

Therefore the baseline-vs-move coefficients satisfy exactly

`D0 = D1 = 0`.

The first possible path that senses exterior carrier environment occurs in `H^3`, hence `U2`, hence `D2`.

---

## 5. All-angle projective conclusion

Within the recovered certified formal Q-B1850/Q-B1852 response family:

- every generic real angular ray leads to `[K2^dag K2]`;
- every `cos(4 theta)=0` ray leads to the same positive projective class via `G1 ~ G0`;
- every `cos(6 theta)=0` ray leads to the same positive projective class via `K3 ~ K2`;
- there is no simultaneous base/move singular ray at these leading orders;
- no preferred finite complex `z`, angular average, fitted rotation or counterterm is used.

Therefore:

# **GATE-A LEADING RESPONSE-RESONANCE PROJECTIVE CLASS IS ALL-ANGLE UNIVERSAL IN THE TESTED CERTIFIED FORMAL FAMILY.**

Typing precision:

- angular-strata exhaustion = exact arithmetic/combinatorial theorem;
- `D0=D1=0` = structural source-level theorem;
- `pi/8` projective coincidence = machine-precision full-pipeline pass with scale `69/2`;
- `cos6=0` / D3 projective coincidence = strong b4+b24+cutoff formal-numerical pass; exact symbolic proportionality remains open.

Thus the all-angle verdict is stronger than finite-z numerical agreement, but the D2/D3 proportionality is not yet promoted as a symbolic identity.

---

## 6. What Gate A does and does not establish

### Established

- no exceptional real angular ray found at leading order that changes the positive response-resonance projective class;
- the former `theta=pi/8` singular-stratum loophole is closed positively;
- the independent `cos6theta=0` move-singular loophole also closes positively to strong formal-numerical precision;
- low-order floating remnants are now structurally typed: `D0,D1` are exact zeros, not hidden physical coefficients;
- the leading class no longer requires choosing a privileged phase/readout direction.

### Not established

- exact symbolic identity `K2=(3/130)K3`;
- all higher-order subleading coefficient universality;
- O(3) restoration of the separate post-event `A21` obstruction;
- HDA, spin-2 or full nonlinear GR;
- Born as a universal factual-winner law;
- metric duration.

Gate B remains independently negative and cannot be erased by Gate A.

---

## 7. Exact next constructive gate

# **D2 / D3 SYMBOLIC PROPORTIONALITY + PHYSICAL CONSEQUENCE GATE**

Two tasks are now separated cleanly.

### A. Algebraic closure

Derive from the local Hamiltonian path algebra and Cons/avg_back structure whether

`K2 = (3/130) K3`

is an exact identity in the certified family, or determine the exact coefficient replacing `3/130`.

This should be done before declaring the all-angle equality literally symbolic.

### B. Physical consequence

With leading angular/readout projective ambiguity removed, ask what structure this single positive response-resonance class actually fixes:

1. its exact S4 irrep/eigenspace typing;
2. whether it supplies a target-blind preferred response direction or only a projective resonance object;
3. whether that object interacts with the independent Gate-B `A21` obstruction or leaves it untouched;
4. whether any retained historical H5 route can now be reopened without assuming O(3), HDA or GR.

No gravity-facing projection may be inserted by hand.

---

## 8. Firewalls

- Root1 frozen; `A_path` retired; global Q uncollapsed.
- factual ledger append-only/separate.
- actualisation soustractive retained; not a positive winner selector.
- Born NOT DERIVED universally.
- metric duration NOT DERIVED; Lambda OPEN.
- Gate B ensemble restoration remains exhausted.
- no preferred finite complex readout.
- no angular averaging.
- no pseudoinverse/rank rescue.
- no fitted rotation, counterterm, sector deletion, microscopic J, metric projector, tetrad, ADM/EH target or factual-history backflow.
- ELGC remains author-approved working postulate, not old-Root theorem.
- O(3) FAIL/NOT CLOSED.
- HDA/spin-2/full nonlinear GR NOT ESTABLISHED.

---

## 9. GR traffic light

🟢 **Gate A major positive closure:** all real angular rays are exhausted and fall on one leading positive projective response-resonance class in the certified formal family.

🟢 **The dangerous analytic-phase ambiguity is sharply reduced:** neither the base-singular nor move-singular ray produces a new leading physical projective class.

🟢 **Low-order seam closed structurally:** `D0=D1=0` is now derived from the local Q path graph, functorial extension and Cons-fixedness.

🟡 **Immediate exact algebra task:** prove the observed `3/130` D2/D3 proportionality symbolically.

🟡 **Then:** determine what the all-angle projective class physically licenses without bypassing the independent Gate-B anisotropy.

🔴 **No GR promotion:** O(3), HDA, spin-2 and full nonlinear GR remain unestablished.
