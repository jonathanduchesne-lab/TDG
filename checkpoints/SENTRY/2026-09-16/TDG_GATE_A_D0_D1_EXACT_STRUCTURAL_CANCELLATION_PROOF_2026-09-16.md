# Complete TDG / Gate A — exact structural cancellation of D0 and D1

**Date:** 2026-09-16 (America/Toronto)  
**Status:** **D0=D1 EXACT BY SOURCE BLOCK-ADJACENCY + FUNCTORIAL LOCAL-Q + S4/CONS FIXEDNESS / FIRST ENVIRONMENT-SENSITIVE MOVE COEFFICIENT = D2 / NO NEW LAW**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Purpose

The two preceding Gate-A checkpoints found:

- generic-vs-`theta=pi/8` full-pipeline positive projective coincidence;
- `cos(6theta)=0` / D3 projective coincidence;
- formal move-difference coefficients `D0,D1` at floating cancellation floor across b4/b24/cutoff;
- first robust move-sensitive coefficient `D2`.

The remaining seam was to establish why `D0,D1` vanish structurally rather than merely numerically.

This checkpoint derives that cancellation from the certified source block graph and the exact carrier-extension/replacement laws.

---

## 1. Certified Hamiltonian block graph

In the recovered certified `RefinedQ.build_H`, the relevant blocks are:

- parent-core block `T`: `H_TT = H0 + SHIFT I6`;
- B3-port block `F`: `H_FF = (MU+SHIFT) I2`;
- parent-core -> each B3 face coupling `H_TF` determined only by the local omitted slot and the same fixed matrices `A[f] Bcanon[f]`;
- there is **no B3->B3 off-diagonal block**;
- parent cores couple directly only to their B3 ports;
- B2/fine-B4 sectors do not directly couple to a parent core.

This is an exact source-graph statement, not a numerical observation.

Historical Q-B1818G independently certifies exact functorial extension:

`I^dag H_K' I = H_K`

for the canonical inclusion of all old degrees, with new cross terms attached only through the new active interface ports.

Thus an extension does not retune any old local block.

---

## 2. Formal moments U0 and U1 are strictly local

The formal BG engine defines

`U_k(T,F) = coarse-B3 projection of H^(k+1) from parent T to face F`.

Therefore

### k=0

`U0(T,F) = P_F H P_T = H_FT`.

It depends only on the direct local parent-face coupling.

### k=1

Insert a complete block decomposition into

`P_F H^2 P_T`.

A contributing intermediate sector `X` must satisfy both

`H_XT != 0` and `H_FX != 0`.

From the exact source adjacency, only two possibilities exist:

- `X=T`, giving `H_FT H_TT`;
- `X=F`, giving `H_FF H_FT`.

No other B3 contributes because there is no B3-B3 off-diagonal coupling. B2/fine-B4 sectors do not couple directly to the parent core.

Hence exactly

# `U1(T,F) = H_FF H_FT + H_FT H_TT`.

Thus `U0,U1` depend only on the local pair `(T,F)` and its slot typing. They cannot sense the exterior carrier completion.

---

## 3. First possible exterior/environment path is H^3

At three Hamiltonian factors, paths can leave the direct parent-face pair through a B3 port, enter an additional neighboring active sector created or enabled by the carrier extension, and return to a B3 response port.

Therefore `U2 ~ P_F H^3 P_T` is the first formal moment that can depend on the changed environment/context incidence.

This source-graph conclusion matches the fresh coefficient audit:

- child-vs-parent low-order response identical at k=0,1;
- first real difference at k=2.

---

## 4. Exact one-context -> four-context replacement

Historical Q-B1818H certifies exactly that appending one maximal cell along frontier B4 `T`:

- removes `T` from the frontier;
- creates four children
  `T_u={x} union (T\{u})`;
- preserves closed B3 incidence and S4-covariant slot structure.

For each child, replace the fresh vertex `x` by the omitted parent slot `u`. This is the canonical local relabeling used by historical `avg_back`.

Under that relabeling:

- the child local parent-core block equals the parent local core block;
- its corresponding B3 diagonal block equals the parent B3 block;
- its direct local coupling has the same slot matrix.

Therefore, exactly at the level of the local Q law,

`U0(T_u,F_u) ~= U0(T,F)`

and

`U1(T_u,F_u) ~= U1(T,F)`

under the canonical slot relabeling, where `~=` denotes literal equality after the prescribed label/slot identification.

No averaging is required for this low-order equality; all four children separately carry the same relabeled low-order local response.

---

## 5. Response/Gram coefficients G0 and G1 inherit the equality

The formal response engine constructs, for each source slot `v`,

`X_v[k] = Hermitian sum_(p=0..k) U_p comm_v U_(k-p)^dag`.

Hence:

- `X[0]` depends only on `U0`;
- `X[1]` depends only on `U0,U1`.

The Gram coefficient is then the bilinear convolution

`G[k] ~ sum_(p=0..k) X_u[p]^T eta X_v[k-p]`.

Therefore:

- `G0` depends only on `U0`;
- `G1` depends only on `U0,U1`.

Since the canonically relabeled child `U0,U1` equal the parent values, every child has the same relabeled `G0,G1` as the replaced parent.

Thus historical `avg_back`, which is merely the arithmetic mean of the four canonically relabeled child Grams, returns exactly the parent coefficient at orders 0 and 1.

---

## 6. Cons does not generate the cancellation

The certified `cons_projector` imposes only linear equality constraints:

1. the same `(u,v)` pair on a shared B3 must agree across its frontier parents;
2. the same pair appearing on different B3 faces inside one B4 context must agree.

At orders 0 and 1, the response depends only on the local slot-covariant blocks above. The same-pair copies are therefore related by exact local relabelings/stabilizers of the tetrahedral slot law and already satisfy these equality constraints.

Hence `G0,G1` lie in the Cons-fixed subspace before projection. The Cons projector acts as the identity on them.

Fresh independent diagnostics confirm the source proof:

### base carrier
- k=0 Cons projection relative defect `1.73e-15`;
- k=1 `1.73e-15`;
- k=2 rises to `8.28e-6`.

### moved carrier
- k=0 `1.65e-15`;
- k=1 `1.66e-15`;
- k=2 rises to `9.92e-6`.

The `~1e-15` values are arithmetic roundoff of an exact equality; k=2 is physically/nontrivially sewn.

---

## 7. Fresh raw-layer localization control

Before Cons, comparing base to every one-move carrier and returning the replaced child quartet through `avg_back` gives:

- all unchanged contexts: exact numerical difference `0.0` for k=0,1,2,3;
- replaced context:
  - k=0 max difference `1.08e-24`;
  - k=1 `3.77e-23`;
  - k=2 `4.74e-11`;
  - k=3 `2.05e-9`.

For one explicit replaced context, each of the four children separately agrees with the parent at k=0 and k=1 to `3e-16–6e-16` relative, while k=2 differs at `~9e-6–1.8e-5` relative.

This independently confirms the exact block-path derivation and shows that the low-order cancellation is local, not a fragile global cancellation among many contexts.

---

## 8. Exact conclusion

For every legal first move in the certified Q-B1850 formal carrier family:

# `D0 = 0`,

# `D1 = 0`.

The first carrier-environment-sensitive baseline-vs-move coefficient is

# `D2`.

This follows from:

- exact Q block adjacency;
- exact carrier-extension functoriality Q-B1818G;
- exact S4-covariant 1->4 frontier replacement Q-B1818H;
- exact locality of `U0,U1`;
- linear Cons equalities already satisfied by those low-order local coefficients.

The former machine-floor caveat is therefore retired as a physical ambiguity.

---

## 9. Consequence for Gate-A angular stratification

Because `D0=D1=0` exactly:

- generic move response begins at `D2 cos(6theta)`;
- if `cos(6theta)=0`, `D3 cos(7theta)` is the next candidate and `cos(7theta)` cannot vanish simultaneously;
- the base response begins at `G0 cos(4theta)`;
- if `cos(4theta)=0`, `G1 cos(5theta)` survives and `cos(5theta)` cannot vanish simultaneously;
- `cos4theta=0` and `cos6theta=0` cannot occur simultaneously.

Thus the leading angular problem is exhausted by:

1. generic `(G0,D2)`;
2. base-singular `(G1,D2)`;
3. move-singular `(G0,D3)`.

The two preceding checkpoints show all three have the same positive projective class to strong, scheme-stable formal-numerical precision.

A separate final synthesis checkpoint may now state the resulting all-angle **strong projective universality**, while retaining that the simple rational coefficient proportionalities `G1/G0=69/2` and `K2/K3=3/130` are numerically exact-looking but not yet independently symbolically reduced from the small local matrices.

---

## 10. Firewalls

- no preferred finite z;
- no angular averaging;
- no fit to GR/O(3);
- no new microscopic rule;
- this exact cancellation theorem concerns the formal predictive-memory coefficient hierarchy only;
- Gate-B A21 obstruction remains independently binding;
- O(3), HDA, spin-2, GR remain unestablished.

---

## 11. GR traffic light

🟢 **Critical seam closed structurally:** the apparent low-order floating remnants are now typed as roundoff of exact source-level cancellations.

🟢 **Angular classification becomes finite and complete at leading order:** only generic, base-singular and move-singular cases remain.

🟡 **Final Gate-A synthesis now available:** combine this exact zero theorem with the two projective-coincidence checkpoints into an all-angle strong universality statement.

🔴 **No GR closure:** the analytic-family problem is much cleaner, but the independent Gate-B/O(3)/HDA obstruction remains.