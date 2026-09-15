# Complete TDG / History Resonance Gate A — exact ray-stratified resolvent symbol and singular-stratum frontier

**Date:** 2026-09-15 (America/Toronto)  
**Status:** **EXACT MICROSCOPIC/LOCAL RAY-STRATIFIED SYMBOL THEOREM / GENERIC-RAY LEADING PROJECTIVE FACTORIZATION PASS / FULL Q-B1850 SINGULAR-STRATUM `[F^dag F]` UNIVERSALITY STILL OPEN**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Purpose

The latest Gate-A frontier asks for an exact real/bianalytic leading-symbol theorem explaining why the large-`|z|` resonance geometry

`[R_infty] = lim [F_C(z)^dag F_C(z)]`

appears independent of complex readout ray, including the deliberate angular-cancellation ray `theta=pi/8`.

The preceding checkpoints established strong numerical/structural convergence but correctly did not promote it to an exact algebraic theorem.

This checkpoint proves the upstream ray stratification exactly and isolates the only remaining Q-specific step.

No O(3), HDA, GR, factual-winner or lens-measure target is used.

---

## 1. Source/provenance discipline

The certified Q-B1850 physical response uses resolvent-derived opposite blocks and explicitly Hermitianizes the resulting local response before the real `h4`/Gram/Cons pipeline.

The historical formal-prolongation source recovered in the Library independently reconstructs the same architecture coefficientwise from powers of the fixed Hermitian Q Hamiltonian:

- repeated `H @ X` builds the off-diagonal moment blocks;
- for coefficient order `k`, the local Hermitian response is a convolution of left/right H-moment blocks around one Hermitian source insertion;
- the result is Hermitianized before `h4`;
- real Gram coefficients are then built bilinearly and descended through Cons.

The exact `qb1852_full_refined.py` source is attested by multiple manifests with SHA-256

`ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7`,

but was not recovered in this audit as a standalone executable Library file. Therefore no new Q-specific coefficient proportionality is claimed below without proof.

---

## 2. Exact resolvent setup

Let `H=H^dag` be the finite current-Q Hamiltonian in the audited local/refined realization.

Let `P` and `Q` be two orthogonal physical block projectors for the opposite response blocks entering the local Q-B1850 resolvent construction, so

`P Q = 0`.

For `|z| > ||H||`, define

`R(z) = (z I - H)^(-1)`.

Because `P Q=0`, the off-diagonal block has no `z^-1` identity term:

`P R(z) Q = sum_{m>=0} z^(-(m+2)) A_m`,

with

`A_m = P H^(m+1) Q`.

Since every `H^n` is Hermitian,

`Q H^(m+1) P = A_m^dag`.

Let `X=X^dag` be the Hermitian microscopic/local source insertion used by the response construction.

Define the same-`z` opposite-block response before Hermitianization by

`Z_X(z) = (P R(z) Q) X (Q R(z) P)`.

The physical Hermitianized response is

`Y_X(z) = Herm[Z_X(z)] = (Z_X(z)+Z_X(z)^dag)/2`.

---

## 3. Exact ray-stratified theorem

For every `k>=0`, define

`S_k(X) = sum_(m+n=k) A_m X A_n^dag`.

### Lemma 1 — each `S_k` is Hermitian

Because `X=X^dag`,

`S_k(X)^dag = sum_(m+n=k) A_n X A_m^dag`.

Relabeling `m <-> n` leaves the finite sum unchanged, hence

`S_k(X)^dag = S_k(X)`.

### Lemma 2 — exact angular/radial factorization

Substituting the Neumann expansion gives

`Z_X(z) = sum_(k>=0) z^(-(k+4)) S_k(X)`.

Since `S_k` is Hermitian,

`Herm[z^(-(k+4)) S_k] = Re[z^(-(k+4))] S_k`.

Writing

`z = r exp(i theta)`, `r=|z|`,

therefore yields the exact convergent expansion

# `Y_X(r,theta) = sum_(k>=0) r^(-(k+4)) cos((k+4) theta) S_k(X)`.

This is the exact upstream real/bianalytic ray stratification that the prior numerical Gate-A scans were seeing.

It follows from the Hermitian Q generator, the off-diagonal block typing and the physical Hermitianization. No fit and no preferred readout is involved.

---

## 4. Immediate consequences

### 4.1 Generic rays

If the first nonzero microscopic coefficient is `S_0(X) != 0` and

`cos(4 theta) != 0`,

then

`Y_X(r,theta) = r^-4 cos(4 theta) S_0(X) + O(r^-5)`.

Therefore the **leading local response ray** is independent of `theta` projectively; all generic-ray angular dependence at this order is one scalar.

Any fixed real linear readout applied before nonlinear normalization — in particular the Hermitian-coordinate map used by the response construction — inherits this scalar factorization.

### 4.2 The deliberate `theta=pi/8` adversary is exactly singular at the generic leading stratum

At

`theta=pi/8`,

`cos(4 theta)=cos(pi/2)=0`.

Thus the generic `r^-4` stratum vanishes **exactly**, not numerically.

The next angular factor is

`cos(5 pi/8) != 0`.

More generally, no angle satisfying `cos(4 theta)=0` can also satisfy `cos(5 theta)=0`: the simultaneous equations would require

`theta=(2a+1)pi/8=(2b+1)pi/10`,

or

`5(2a+1)=4(2b+1)`,

whose left side is odd while the right side is even.

Hence any further suppression on the `pi/8`-type singular rays must come from a **Q-specific coefficient cancellation such as `S_1=0` or a later pipeline cancellation**, not from the angular geometry itself.

This sharply separates ray singularity from Q dynamics.

---

## 5. Gram/bianalytic corollary

Let a local real response coordinate be obtained by a fixed real-linear map `L`:

`x_X(z)=L(Y_X(z))`.

Then

`x_X(r,theta)=sum_(k>=0) c_k(r,theta) x_k`,

where

`c_k(r,theta)=r^(-(k+4)) cos((k+4)theta)`

and `x_k=L(S_k)`.

For any fixed real bilinear Gram form `eta`,

`G_X(z) = x_X(z)^T eta x_X(z)`

has the exact double expansion

`G_X(r,theta)=sum_(k,l>=0) c_k(r,theta)c_l(r,theta) G_kl`.

Thus the physical Gram response is formally real/bianalytic in inverse `z,zbar`, exactly as the previous Gate-A retyping required.

On a generic ray with nonzero leading coefficient,

`G_X(r,theta)=r^-8 cos^2(4theta) G_00 + O(r^-9)`.

Therefore the **leading local Gram class** is also generic-ray projectively independent.

On `theta=pi/8`, the `G_00` contribution vanishes and the first available angular stratum is shifted. If `x_1 != 0`, the local Gram begins at `r^-10 cos^2(5theta) G_11`; whether `[G_11]=[G_00]` is a Q-specific question, not a consequence of Hermitianity alone.

---

## 6. Why this does NOT yet prove the full `R_infty` theorem

The actual Q-B1850 resonance operator is downstream of more structure than one local Gram:

1. baseline and moved same-Q responses are differenced;
2. Cons descent is applied;
3. the normal direction `N_i` is reconstructed from the current local Gram;
4. scalar cross-memory responses are formed;
5. Q-B1849 process-unit column normalization is applied;
6. the final `16x16` map `F_C` is used to form `F_C^dag F_C`.

For generic rays, the exact scalar factorization above explains why ray dependence can cancel projectively through homogeneous parts of this pipeline.

But the full exact theorem, especially on singular rays, still requires showing that the **first nonzero coefficient surviving the complete Q-B1850 pipeline** lies in the same projective operator class as the generic leading coefficient.

Equivalently, after all exact Cons/difference/normalization operations, the first nonzero singular-stratum matrix must be projectively collinear with the generic-stratum matrix (or at minimum give the same positive Gram class).

Hermitianity alone does not force this.

The existing numerical result that `theta=pi/8` converges to the same normalized `F^dag F` is therefore important Q-specific evidence, but it is not converted here into an algebraic identity.

---

## 7. Exact new frontier

The Gate-A problem is now smaller and sharper.

### CLOSED EXACTLY

- treating Q-B1850 physical response as one holomorphic Laurent series in `z` alone;
- ambiguity about why `theta=pi/8` behaves as a singular amplitude ray;
- ambiguity about generic-ray leading local response orientation;
- ambiguity about whether real/bianalytic ray stratification is merely a numerical observation.

### OPEN

Only the Q-specific **singular-stratum projective-coincidence theorem through the full Q-B1850 pipeline**:

> Let `K_gen` be the first nonzero generic-ray coefficient of the fully normalized process map and `K_sing` the first nonzero coefficient on a ray where the generic scalar angular factor vanishes. Prove, from current Q/Cons/process structure alone, either
>
> `[K_sing^dag K_sing] = [K_gen^dag K_gen]`,
>
> or the appropriate equivalent common positive S4-typed projective class.

The first target is the `theta=pi/8` stratum because `cos4theta=0` but `cos5theta!=0`; therefore the next candidate coefficient is uniquely exposed unless Q itself cancels it.

### Required source for exact completion

Recover or reconstruct from certified primary source the full `qb1852_full_refined.py` / Q-B1850 coefficient pipeline, or an equivalent provenance-complete coefficient bundle, then compare the first surviving generic and singular formal coefficients **before finite-z fitting**.

Do not infer the missing identity from downstream numerical convergence alone.

---

## 8. DERIVED / STRONG NUMERICAL / OPEN

### DERIVED EXACTLY IN THIS CHECKPOINT

- off-diagonal Hermitian resolvent response admits the exact ray-stratified expansion
  `Y_X=sum r^(-(k+4)) cos((k+4)theta) S_k`;
- every `S_k` is Hermitian;
- generic leading local response and local Gram classes are ray-independent up to scalar factors;
- `theta=pi/8` exactly removes the `k=0` / `r^-4` response stratum;
- `cos(5theta)` cannot vanish simultaneously on the `cos(4theta)=0` set;
- any further singular-ray suppression is Q-specific, not purely angular.

### RETAINED STRONG NUMERICAL/STRUCTURAL

- normalized Q-B1850 `F^dag F` converges to one common large-`|z|` class on generic complex rays;
- the same convergence survives the `theta=pi/8` singular-ray adversary;
- direct b4/b24 asymptotic agreement is strong;
- asymptotic held-out Q-B1851 process relevance is strong.

### OPEN

- exact Q-specific singular-stratum coefficient coincidence after complete Cons/cross-memory/process-unit normalization;
- therefore the full global `[F^dag F]` `R_infty` theorem remains not yet promoted to exact.

---

## 9. GR traffic light

🟢 **Advance:** the formerly empirical bianalytic/ray-stratified behavior now has an exact upstream theorem, and the deliberate `pi/8` adversary is mathematically explained.

🟢 **Localization:** the entire remaining Gate-A algebraic gap is reduced to a Q-specific coefficient-coincidence statement after the full Q-B1850 pipeline.

🟡 **Next:** recover the certified formal coefficient source/bundle and test/prove singular-stratum projective coincidence without finite-z fitting.

🔴 **No GR promotion:** no factual-winner rule is derived, no new Root2 law is admitted, Born remains NOT DERIVED, O(3) remains FAIL/NOT CLOSED, HDA/spin-2/full nonlinear GR remain NOT ESTABLISHED.
