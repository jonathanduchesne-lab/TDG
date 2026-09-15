# Complete TDG / Root2 — History-resonance Gate A: scale, refinement, readout and cubic-alignment audit

**Date:** 2026-09-15 (America/Toronto)  
**Status:** **GATE A STRONG PARTIAL CLOSURE — SCALE/S4/REAL-READOUT/REFINEMENT ROBUSTNESS PASS; COMPLEX-READOUT UNIVERSALITY FAIL IN TESTED FAMILY; CUBIC-POLAR EIGENMODE ALIGNMENT FAIL; HELD-OUT PREDICTIVE RELEVANCE OPEN**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Purpose and latest-wins scope

This checkpoint continues the live front established by

`TDG_HISTORY_RESONANCE_RESPONSE_SPECTRUM_S4_MODE_DECOMPOSITION_2026-09-15.md`.

The fixed-readout Q-native resonance operator is

`R_C = F_C^dag F_C`,

with normalized form

`Rhat_C = R_C / Tr(R_C)`.

Here `F_C` is the Q-B1850 same-Q legal-move -> Cons/Feshbach response map, process-unit normalized by the already-derived Q-B1849 legal-move descriptor.

The audit is strictly target-blind. No factual winner, O(3), SAME-h, HDA or GR objective is used.

## 1. Provenance and fresh replay

### Q-B1850 / GR1 source

Fresh source archive:

`TDG_QB1860BW_RC40F_GR1_FULL_HANDOFF_2026-08-27.tar.gz`

SHA-256:

`25910cbe37f22cb422b5dd739334f224532026c765453e5f340ea5a432973f4a`

The archive contains the certified fresh Q-B1850 dumps

- `QB1850_F_a001.npy`;
- `QB1850_F_a002.npy`;
- `gr1_dumpF.py`;
- full Q-B1850 dependencies.

The certified script was replayed without changing the definition of `F_C`, adding only the missing cutoff `a=.04` to the existing `.02,.01` loop.

Fresh process-unit ranks/conditions at `z=2+0.7i`:

- `a=.04`: rank `16/16`, cond `2.867336840737162`;
- `a=.02`: rank `16/16`, cond `2.910548272031448`;
- `a=.01`: rank `16/16`, cond `2.921449515145497`.

### Q-B1852 refinement source

Fresh source archive:

`Complete_TDG_Root2_FULL_HANDOFF_QB1852L_2026-08-19.tar.gz`

SHA-256:

`6ea97808a6f60b0d798d46d08be1631639ab4fa371d0c60a1b1d6aeeff6897b2`.

Embedded repro:

`TDG_QB1852A_QB1852L_FRESH_repro_2026-08-19.tar.gz`

SHA-256:

`9961cd64e7a858eac60f22a3075ac6c8a0e1b2752e67b5469970d1b914f16b66`.

The exact Q-B1852 `RefinedQ` engine was used on the same 101-parent universe. For the present resonance comparison each scalar memory column was normalized by the same Q-B1849 process-descriptor amplitude used by Q-B1850.

At `a=.02`, `z=2+0.7i`:

- b4: rank `16/16`, cond `2.914462332406195`;
- b24: rank `16/16`, cond `2.919829804854446`.

No fitted inter-scheme map was used.

## 2. Exact S4 decomposition and commutant projection

The exact legal-move permutation representation was reconstructed directly from the certified Q-B1838/Q-B1850 source.

Fresh character-projector ranks:

- trivial `1`: rank 2;
- doublet `2`: rank 2;
- polar Standard3 `3`: rank 9;
- axial Standard3 `3'`: rank 3;
- sign singlet `1'`: rank 0.

Thus the exact decomposition is reproduced:

`2*1 + 1*2 + 3*3 + 1*3'`.

Projector idempotency/orthogonality is at floating floor and their sum is exactly the 16D identity to numerical precision.

For finite-cutoff `Rhat_C`, define the target-blind Reynolds/commutant projection

`Rbar_C = (1/|S4|) sum_g P_g^T Rhat_C P_g`,

renormalized to unit trace. The difference `||Rhat_C-Rbar_C||/||Rhat_C||` is used only as a covariance diagnostic; `Rbar_C` is not a new physical law.

## 3. Fixed complex readout scale robustness — STRONG PASS

At `z=2+0.7i`, the S4-commutant leakage is

- `.04`: `7.4235892188e-5`;
- `.02`: `2.0288432595e-5`;
- `.01`: `5.2112389658e-6`.

The corresponding max group-commutator defects are

- `.04`: `1.3075612517e-4`;
- `.02`: `3.5432076991e-5`;
- `.01`: `9.0640514475e-6`.

Both are consistent with the inherited `O(a^2)` S4 covariance improvement.

Normalized commutant-operator changes are

- `.04 -> .02`: `0.0047136810`;
- `.02 -> .01`: `0.0012329874`.

The ratio is approximately the expected factor four under halving `a`.

### Polar Standard3 multiplicity spectrum

The three triply-degenerate commutant eigenvalues are:

`a=.04`: `0.1067844977`, `0.06248017981`, `0.05080814554`;

`a=.02`: `0.1065088967`, `0.06249702424`, `0.05090049180`;

`a=.01`: `0.1064395878`, `0.06249964719`, `0.05092308807`.

The corresponding rank-3 spectral projectors are extremely stable.

Minimum principal cosines after optimal identity matching:

`.04 -> .02`:

- `0.9999737173`;
- `0.9999161019`;
- `0.9999284557`.

`.02 -> .01`:

- `0.9999981018`;
- `0.9999937460`;
- `0.9999946272`.

**Classification:** fixed-readout resonance families and projectors are strongly cutoff-stable.

## 4. Real-resolvent family — STRONG PASS

The exact same Q-B1850 engine was rerun at real `z=2` for `.04,.02,.01`.

Ranks remain `16/16`; conditions are

- `.04`: `29.1662570642`;
- `.02`: `29.0760048135`;
- `.01`: `29.0533988141`.

S4 leakage again follows approximately `O(a^2)`:

- `.04`: `8.5020249442e-5`;
- `.02`: `2.1200142032e-5`;
- `.01`: `5.2966175739e-6`.

Normalized `Rbar` changes:

- `.04 -> .02`: `0.0022323466`;
- `.02 -> .01`: `0.0005524752`.

At `a=.01`, changing the real resolvent from `z=2` to `z=1.4` or `z=8` changes `Rbar` only by

- `8.3676e-5` for `1.4 vs 2`;
- `1.3373e-4` for `8 vs 2`.

The three polar Standard3 spectral projectors agree to printed numerical unity in the principal-cosine diagnostic.

**Classification:** the real-readout resonance spectrum is strongly projectively/readout stable in the tested family.

## 5. Complex-readout adversary — O(1) NONUNIVERSALITY

Two target-blind complex probes were compared to the reference `z=2+0.7i` at all three cutoffs.

### Moderate complex probe `z=1.4+0.5i`

Relative `Rbar` differences:

- `.04`: `0.07133214374`;
- `.02`: `0.06904798400`;
- `.01`: `0.06851382574`.

These do not scale to zero as `O(a^2)` over the tested sequence.

Nevertheless the polar rank-3 projectors remain close. At `.01` their minimum principal cosines are

- `0.9998020`;
- `0.9974482`;
- `0.9975995`.

### Strong complex adversary `z=3+0.8i`

Relative `Rbar` differences:

- `.04`: `0.7786921807`;
- `.02`: `0.7904245238`;
- `.01`: `0.7929152584`.

Thus the positive resonance-strength geometry itself changes by `O(1)` under this probe family; the effect is not confined to the polar-unitary phase `U_C`.

At `.01`, the three polar spectral-projector minimum cosines relative to the reference are

- top mode: `0.9990930`;
- middle mode: `0.8987009`;
- lower mode: `0.8994770`.

The lower two projectors therefore undergo a finite rotation that is not trending to identity over `.04,.02,.01`.

**Classification:**

`ONE UNIVERSAL COMPLEX-READOUT R_C SPECTRUM/PROJECTOR FAMILY` = **STRONG FAIL IN THE TESTED FINITE/REFINING FAMILY**.

This is not an all-readout analytic no-go theorem. A separately derived readout-free/asymptotic construction remains logically open.

## 6. b4 vs parity-balanced b24 — STRONG PASS AT a=.02

Using the exact Q-B1852 same-Q full101 refined engine and identical Q-B1849 process-unit normalization:

- b4 cond: `2.9144623324`;
- b24 cond: `2.9198298049`;
- b4 S4 leakage: `3.3984234209e-5`;
- b24 S4 leakage: `1.5194980399e-5`.

The normalized commutant operators differ by only

`||Rbar_b24-Rbar_b4||/||Rbar_b4|| = 7.9744752971e-4`.

Polar Standard3 eigenprojector minimum principal cosines are

- `0.99999908199`;
- `0.99999689922`;
- `0.99999736446`.

Corresponding maximum principal angles are approximately

- `0.0776 deg`;
- `0.1427 deg`;
- `0.1315 deg`.

**Classification:** fixed-readout resonance-mode geometry is strongly b4/b24 refinement-natural in this direct parity-balanced Q-B1852 comparison.

## 7. Cubic-polar Standard3 vs resonance eigenmodes — FAIL AS PURE EIGENMODE

The exact degree `<=2` jet image has rank 10. Its orthogonal cubic quotient has rank 6 and decomposes exactly as

`3_cubic-polar + 3'_cubic-axial`.

The rank-3 cubic-polar subspace was compared directly with each of the three rank-3 polar Standard3 eigenmodules of `Rbar_C`.

At reference `z=2+0.7i`:

### a=.04

cubic-polar weights in the three resonance Standard3 modules:

- top: `~0.1289`;
- middle: `~0.6853`;
- lower: `~0.1858`.

### a=.02

- top: `~0.1241`;
- middle: `~0.6807`;
- lower: `~0.1952`.

### a=.01

- top: `0.122785`;
- middle: `0.679411`;
- lower: `0.197804`.

For the best-aligned middle resonance module, the minimum principal cosine tends near `0.824`, corresponding to a maximum principal angle near `34.5 deg`, not zero.

The Q-B1852 direct refined comparison gives the same result at `.02`:

- b4 middle cubic weight `0.682376`, min cosine `0.826060`;
- b24 middle cubic weight `0.681470`, min cosine `0.825512`.

For real `z=2` at `.01`, the middle mode carries about `0.72243` of cubic-polar weight with min cosine `0.849959`; it is still not the same subspace.

Under the strong complex probe `z=3+0.8i`, the dominant cubic-polar overlap moves toward the lowest resonance module rather than becoming pure.

Therefore:

`UNIQUE CUBIC-POLAR STANDARD3 FROM JET FILTRATION = ONE EIGENMODULE OF R_C`

is **STRONG FAIL / NOT TRUE IN THE TESTED FIXED-READOUT FAMILIES**.

This does not demote the cubic-polar Standard3 itself. It remains a real Q/process-selected filtration subspace. The new result is that the response-resonance operator mixes the three equivalent polar Standard3 copies in a nontrivial, stable way.

## 8. What Gate A now establishes

### STRONG PASS

- exact S4 mode organization;
- no dark legal-move direction on the tested shell;
- cutoff stability of normalized resonance-strength operator at fixed reference readout;
- stable separated polar Standard3 resonance projectors under refinement;
- strong real-resolvent readout stability;
- direct b4/b24 fixed-readout resonance-mode naturality at `.02`.

### STRONG FAIL / NEGATIVE RESULT

- universal complex-readout `R_C` spectrum/projectors across the tested analytic probes;
- interpretation that all complex-readout dependence sits only in the polar phase/orientation `U_C`;
- identification of the cubic-polar Standard3 as a pure eigenmodule of `R_C`.

### RETAINED / INHERITED, NOT FRESHLY REEXECUTED HERE

- Q-B1850 far-spectator locality control;
- exact same-final 120/120 Cons path/order independence;
- full-rank predictive field / jet synthesis.

### OPEN

- a readout-free or asymptotic resonance operator independently selected by Q;
- physical status of the complex readout parameter family;
- held-out predictive relevance of the resonance eigenmodes to later fragmentation/recombination, without conditioning on the factual winner;
- Gate B physical history/lens ensemble and its measure.

## 9. Interpretation

The strongest defensible statement is now sharper than the parent checkpoint:

> **Q contains robust collective resonance organization, but no single universal positive resonance spectrum has been derived across the full complex analytic readout family.**

The collective S4 mode families are not an artifact: they are stable under cutoff, real readout changes and b4/b24 refinement.

However a far complex analytic probe changes the positive response-strength geometry itself by `O(1)`. Therefore a future universal “history resonance spectrum” needs an independently Q-selected readout-free construction; one cannot simply nominate one complex resolvent value.

The cubic-polar Standard3 remains useful as a Q-selected jet-filtration mode, but it should no longer be described as if it were already the principal resonance eigenmode. It is instead a stable mixture across the three equivalent polar Standard3 resonance modules.

## 10. Numerical evidence hashes

Fresh result files produced in the audit:

- `GATEA_S4_SPECTRUM_RESULTS.json` SHA-256 `1acd9ee23adef16d9223873a2bfb5fcac38dcb2a6d83730c9329b52ceac6487d`;
- `GATEA_READOUT_COMPARE_RESULTS.json` SHA-256 `738e71592f9aeae72f7ecf7105dafeb026a5dbac175baa9aeca83fa7fe89fb0b`;
- `GATEA_B4_B24_RESULTS.json` SHA-256 `8f096e6f20d8ab3a8e447660f619ad0b7bd72734ce17a2f469e1428ea1f9282e`;
- `GATEA_COMPLEX_SCALING_RESULTS.json` SHA-256 `87f7294ef967b93a116d640938c705672775155d3fc6aeb5a9c0f5ceab295099`.

The underlying fresh matrices are source-derived diagnostics, not new canonical Q content.

## 11. Exact next legal work

Gate A is not fully closed because held-out predictive relevance remains open.

The next legal test is:

1. freeze the resonance eigenprojectors without factual-winner information;
2. use only future/process data available at the same predictive stage;
3. test whether projection onto one or more stable resonance modules improves prediction of a held-out later fragmentation/recombination/process observable relative to symmetry-matched controls;
4. separately keep the strong complex-readout adversary live;
5. do not choose a readout because it predicts the realized winner.

In parallel, Gate B may proceed only after identifying a physically licensed same-stage history/lens ensemble and measure.

H5 remains PAUSED / NOT REJECTED.

## 12. GR traffic light

🟢 **Advance:** collective resonance-mode geometry is now quantitatively robust under cutoff, real readout and b4/b24 refinement.

🟢 **Advance:** an ambiguity is removed — cubic-polar process selection and response-resonance eigenmodes are distinct structures, not synonyms.

🟡 **Live frontier:** held-out predictive relevance and a Q-selected readout-free resonance construction; Gate B physical ensemble/measure remains open.

🔴 **No GR promotion:** complex-readout universality fails in the tested family; no factual-winner rule, no new Root2 law, O(3) still FAIL/NOT CLOSED, HDA/spin-2/full nonlinear GR still NOT ESTABLISHED.