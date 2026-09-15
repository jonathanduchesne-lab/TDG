# Complete TDG / Root2 — Initial impulse, single factual history, path-space reduction and selector symmetry audit

**Date:** 2026-09-15 (America/Toronto)  
**Status:** **EXACT ABSTRACT SINGLE-SEED/PATH-SPACE REPRESENTATION PASS / EXACT COVARIANT SYMMETRY SELECTOR NO-GO / CURRENT-Q WINNER SELECTOR NOT DERIVED / INITIAL-IMPULSE PHYSICAL COMPLETION OPEN / NO ROOT2 ADMISSION**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

## 0. Author notation and scope

Jonathan's present conceptual notation is taken literally here:

- `A` = the ensemble of still-possible continuations;
- `W` = the relational/constraint "web" acting on those possibilities;
- `B` = the one factual actualization/event;
- `C` = the resulting projection/effective post-actualization description.

The author's intuition is that an initial impulse/first actualization launches the process; thereafter information organizes, the web suppresses incompatible continuations, and one factual history is retained through successive actualizations.

This checkpoint does **not** assume a hidden selector merely because that intuition exists. It asks how far the current TDG corpus and exact abstract mathematics take the idea.

No O(3), HDA, spin-2, GR, metric, preferred z, fitted selector or factual-history backflow is used.

## 1. Permanent firewalls

- Root1 frozen; `A_path` retired.
- global Q uncollapsed.
- factual ledger append-only and separate from predictive/global Q.
- actualisation soustractive retained as Jonathan Duchesne's conceptual contribution; it is not yet a positive winner-selection law.
- Born NOT DERIVED.
- metric/proper duration NOT DERIVED.
- Lambda OPEN.
- ELGC remains an author-approved working postulate, not an old-Root theorem.
- O(3) FAIL / NOT CLOSED.
- HDA / spin-2 / full nonlinear GR NOT ESTABLISHED.
- no hidden occurrence register or factual-history feedback into predictive Q.

## 2. What the current Q already supplies

Q-B1819F gives, in its audited physical extension scope, a genuine extension-resolved instrument. For each admissible extension `e` there is a branch operator `K_e`, exact completeness, and Q/FP relative branch weights. Q-B1819G is Born-equivariance/consistency only, not winner selection.

Q-B1818/Q-B1822 further establish that old global-Q/carrier structure persists under legal extension and that factual branch poststates must not replace the noncollapsed predictive Q.

Therefore current TDG has the three logically distinct layers:

1. **possibility/support layer** — multiple legal next continuations can exist;
2. **weight/response layer** — Q/FP assigns physically meaningful relative support/weights in audited scopes;
3. **factual layer** — one realized history is recorded.

The map from 1+2 to the single factual winner is not yet derived.

## 3. The web can be typed without adding a new substance

A useful, conservative interpretation is:

`W = legal Ext incidence + Cons compatibility/descent + current-Q predictive response/weights + all already-derived causal/interface constraints`.

This is an **interpretive identification**, not a new Root axiom.

On this reading, the web does at least two things already present in TDG:

- rules out illegal/incompatible continuations;
- changes the predictive support/weights after a factual event while preserving unaffected old Q structure.

What it does **not** currently do is prove that exactly one supported branch remains before every actualization.

## 4. Exact nested-cylinder reduction theorem

Consider any sequential physical branch process for which each finite factual prefix

`h_n = (e_1,...,e_n)`

has a normalized next-event kernel

`p(e | h_n) >= 0`, `sum_e p(e|h_n)=1`.

This includes the Q-B1819/FP branch structure in its declared scope.

Let `Omega` be the space of infinite legal histories and `[h_n]` the cylinder set of all histories beginning with prefix `h_n`.

Define the path measure on cylinders by

`mu([h_n]) = product_(k=1..n) p(e_k | h_(k-1))`.

After event `e_(n+1)` becomes factual, the updated possibility measure is simply conditionalization on the narrower cylinder:

`mu_(n+1)(X) = mu_n(X intersect [h_(n+1)]) / p(e_(n+1)|h_n)`

whenever the denominator is nonzero.

### Consequences

- every path incompatible with the new factual prefix receives conditional weight zero;
- compatible futures remain represented;
- no unrelated part of the possibility structure must be rebuilt;
- the factual history is the nested chain
  `[h_0] superset [h_1] superset [h_2] superset ...`;
- if the infinite event sequence uniquely labels a history, the nested intersection contains one factual history.

This is an exact mathematical realization of a **reduction machine**: actualization narrows the admissible future cylinder and renormalizes what remains.

### Status

**NESTED-CYLINDER REDUCTION = EXACT ABSTRACT THEOREM GIVEN A NORMALIZED SEQUENTIAL BRANCH KERNEL.**

It is not a derivation of the physical branch kernel itself and not a derivation of Born.

## 5. Exact one-initial-draw equivalence theorem

The same path measure admits two exactly equivalent descriptions at the level of factual-path statistics:

### Sequential description

At every stage draw one next event from `p(e|h_n)`.

### One-shot description

Draw one complete history `omega` from the path measure `mu` once, at the initial boundary, and subsequently reveal only its successive prefixes.

For every finite history `h_n`, both procedures assign exactly

`P(h_n)=product_(k=1..n) p(e_k|h_(k-1))`.

Therefore:

# **ONE INITIAL STOCHASTIC IMPULSE + PREFIX REVELATION IS DISTRIBUTIONALLY EQUIVALENT TO FRESH STOCHASTIC DRAWS AT EACH ACTUALIZATION.**

This gives a rigorous sense in which the randomness can be moved to the initial boundary without changing any finite factual-path statistics.

But this is a representation theorem, not yet an explanatory physical mechanism.

## 6. Constructive one-seed theorem

For a finite branch set at each step, the one-shot path draw can be encoded by a single initial seed `u_0 in [0,1)`.

At history `h`, partition `[0,1)` into intervals `I_e(h)` of lengths `p(e|h)`. The branch containing `u` is factual. If branch `e` occupies interval `[a_e,a_e+p_e)`, update

`u' = (u-a_e)/p_e`.

Then:

- a fixed `u_0` gives one deterministic factual history;
- if `u_0` is uniform, the first branch has exactly the prescribed `p(e|h_0)` distribution;
- conditioned on the chosen branch, `u'` is again uniform;
- by induction all finite history probabilities are exactly the original product-kernel probabilities.

Thus:

# **ONE CONTINUOUS INITIAL SEED IS MATHEMATICALLY SUFFICIENT TO GENERATE THE ENTIRE SINGLE HISTORY FOR ANY SUCH SEQUENTIAL WEIGHT PROCESS.**

### Critical caveat

A real seed can contain arbitrarily much information. Therefore "one variable" does **not** automatically mean "simple physical explanation". Without an independently physical law for the seed and its branch partition, this construction can be only a coded version of the complete future history.

## 7. Exact covariant symmetry-selector no-go

The initial-impulse question becomes sharper in a symmetric branch situation.

Let a symmetry group `G` act on a predictive state `x` and on its supported branch set `E_x`. Suppose:

1. `x` is invariant: `g.x = x` for every `g in G`;
2. the supported branches contain no element fixed by all of `G` (for example a transitive multi-branch orbit);
3. a deterministic selector `S(x) in E_x` is required to be covariant:
   `S(g.x) = g.S(x)`.

Then no such selector exists.

### Proof

Since `g.x=x`, covariance gives

`S(x)=S(g.x)=g.S(x)`

for every `g`.

Therefore `S(x)` must be fixed by all of `G`, contradicting assumption 2.

QED.

### TDG consequence

Q-B1819M explicitly contains S4-related elementary extension orbit structure in the four-slot grammar. More generally, any exact TDG state in which supported next events are symmetry-equivalent cannot produce one covariant factual winner from the symmetric predictive/web data alone.

A deterministic completion must then have at least one of:

1. additional symmetry-breaking pre-factual data `lambda`;
2. a physically asymmetric initial condition already contained in the complete state;
3. irreducible stochastic factualization;
4. a genuine physical symmetry breaking in the law/state.

Simply saying "choose the largest branch weight" does not solve the symmetric case and does not reproduce a nontrivial probabilistic law under repeated identical preparations.

## 8. Current-Q selector candidate sweep

The strongest already-derived objects were screened as possible `lambda`-type selectors.

### C1 — branch weights themselves

**FAIL as winner selector.** They rank/support alternatives but do not supply a unique branch in general; Q-B1819G remains equivariance/consistency, not selection.

### C2 — current carrier / endpoint Q algebra

**FAIL in general as hidden selector.** Existing endpoint/realization audits show endpoint data do not reconstruct missing history/process distinctions, and the current Active43 extension operator is carrier-determined/operator-Markov.

### C3 — factual ledger/history state

**FORBIDDEN as pre-factual selector source under current firewalls.** Feeding realized history back into predictive Q/next operator without an independent law violates the global-Q/factual-ledger separation.

### C4 — sequential occurrence/path labels

**NOT A PRE-FACTUAL WINNER SELECTOR.** Occurrence identity can be physically substantive in the process layer, but passive occurrence labels do not generate a new active next-transition law, and naive physical occurrence splitting is not licensed.

### C5 — Cons cells / quotient structure

**CONSTRAINT, NOT WINNER.** Cons identifies/constrains compatible descriptions/routes and can flatten filled route classes; it does not itself manufacture one factual branch.

### C6 — Q-B1849->Q-B1852 first-order process transport

**PROCESS GEOMETRY, NOT FACTUAL SELECTION.** It gives powerful legal-move/process descriptors and transport after a move is typed, but no general branch winner.

### C7 — Q-B1854/55 selected angular Standard3 ray / Q-B1858 projective-conformal mode

**TYPE FAIL AS GENERAL WINNER SELECTOR.** These are selected process/response directions in their own geometric type; the selected ray is not a dynamically invariant universal branch channel, and absolute conformal scale is not licensed.

### C8 — future coorientation used in process descriptors

**ORIENTATION DATA, NOT ENOUGH FOR GENERAL MULTI-BRANCH SELECTION.** It orients already-derived process charts; no recovered theorem turns it into a unique Ext occurrence selector.

### C9 — GR178 local process-state update

**DETERMINISTIC CONDITIONED-ON-MOVE, NOT MOVE SELECTION.** GR178 can predict the exact successor descriptor once one legal move is marked, including D4->D>4 exits; it does not derive which port/move becomes factual.

### C10 — hidden full path / scalar seed

**MATHEMATICAL CAPACITY PASS / PHYSICAL DERIVATION FAIL.** Exact by Sections 5-6, but absent as a Q-derived Root object and vulnerable to the "prewritten script" objection.

### Inventory verdict

Within the presently recovered/audited corpus:

# **NO ALREADY-DERIVED CURRENT-Q OBJECT HAS BEEN IDENTIFIED AS A GENERAL PRE-FACTUAL WINNER SELECTOR.**

This is conditional on the recovered corpus, not a universal impossibility theorem.

## 9. What the author's initial impulse can mean without overclaiming

Three distinct meanings must be kept separate.

### I. Initial stochastic sample of one whole history

Exact representation of existing branch probabilities. No repeated random draw is needed. **Mathematically valid, physically non-explanatory unless the initial path measure is itself derived.**

### II. Initial deterministic seed `lambda_0`

A fixed pre-factual state plus a deterministic contextual update rule produces one history. **Mathematically viable, new foundational candidate, not Q-derived.**

### III. First factual event leaves a real symmetry-breaking physical trace in the web

Later selections could in principle become deterministic from the enlarged complete state if that trace remains pre-factually relevant. **This is conceptually close to the author's wording but is not established by current Q.** In the current Active43 architecture, later one-event operators are current-carrier determined and do not receive an independent hidden ledger-order argument.

## 10. Born does not disappear

Moving selection to the initial boundary does not derive the measure.

For the single-seed construction, exact branch frequencies require an initial measure `mu(lambda_0)` whose pushed-forward path distribution matches Q/FP/Born-compatible weights.

For one universe and repeated experiments, a stronger typicality/ergodic theorem would be required to obtain observed frequencies from a single fixed seed/history.

Neither is currently derived.

Therefore:

**Born remains NOT DERIVED.**

## 11. Strongest scientifically honest reclassification

The current conceptual architecture is now:

`A + W` = weighted/constrained possible continuations;

`B` = one factual branch;

`B` then induces the already-closed predictive update/projection side (`A+B -> C` in the previous quotient-descent theorem).

The unresolved map is:

`(A,W) -> one B`.

The exact results above establish:

- one initial impulse can encode one entire factual history without repeated randomness;
- this does not by itself add empirical content or explain Born;
- a perfectly symmetric web cannot covariantly select one symmetry-equivalent branch without additional symmetry-breaking data or stochasticity;
- no current recovered Q object has yet supplied that general extra selector datum.

## 12. Assistant-only conceptual hypothesis — quarantined

**This section is explicitly assistant-origin, not Jonathan-origin.**

A mathematically natural type for a future deterministic selector would be a **pre-factual contextual section over the Root Ext/channel layer**, not a hidden geometric coordinate and not factual-ledger feedback.

Schematically, let the supported physical next-channel fibre over current state `x` be `E_x`. A selector state `lambda_x` would transform covariantly with branch relabelings and define

`S_x(lambda_x) in E_x`.

After the chosen event, `lambda` would be transported prospectively by a target-blind law. Such a selector would need to be contextual/relational: it must respond to the full physical instrument/context rather than assign context-independent classical values to all counterfactual branches.

This is only a proposed **type** for a completion. No such Root/Q object has been derived.

A scalar "actualization phase" is one possible minimal coordinate model of this type, but without a Q-derived equivariant partition/update law it is merely a coding device and must not be promoted.

## 13. Exact next scientific gate

The highest-value selection work is now:

1. search the recovered Root/Q corpus for a **pre-factual symmetry-breaking datum** that survives relabeling/covariance and is not branch weight, ledger history, geometry downstream or a readout convention;
2. if none exists, stop derivation-only selector mining and classify deterministic single-history completion as explicit new foundational content;
3. if a new selector is deliberately proposed, freeze it before any GR comparison and test:
   - support legality;
   - covariance/relabeling;
   - symmetry-breaking source;
   - non-script/non-lookup character;
   - no ledger backflow;
   - contextual/intervention consistency;
   - Cons/refinement compatibility;
   - Born/FP measure or typicality;
   - empirical/nonredundancy versus the stochastic representation.

## 14. DERIVED / AUTHOR INTUITION / ASSISTANT INTUITION / OPEN

### DERIVED / EXACT ABSTRACTLY

- nested-cylinder conditional reduction;
- one-shot whole-history sampling is distributionally equivalent to sequential sampling;
- one real seed can encode the complete sequential branch process constructively;
- a covariant deterministic selector cannot choose one branch from an exactly symmetric state when the supported branch orbit has no global fixed point.

### DERIVED / CURRENT TDG SCOPE

- Q-B1819 physical branch instrument and relative weights;
- one factual history is compatible with uncollapsed predictive Q;
- current Root does not derive a general winner selector;
- current Active43 later extension operators are carrier-determined, not history-fed.

### AUTHOR INTUITION — NOT PROMOTED

- initial impulse/first actualization launches the process;
- information organizes through a reduction web;
- incompatible possible paths are suppressed;
- one factual history is retained.

### ASSISTANT INTUITION — NOT PROMOTED

- the web may be most cleanly interpreted as Ext+Cons+Q/FP constraints;
- the reduction machine is naturally represented by conditionalization on nested history cylinders;
- if a deterministic selector exists, its natural type is a contextual pre-factual Ext/channel section, possibly carrying an "actualization phase";
- a mere scalar seed with no Q-derived law is explanatory coding, not physics.

### OPEN

- physical source of the initial impulse/selector;
- whether the first factual event leaves a Q-native persistent symmetry-breaking datum usable by later selection;
- selector dynamics or irreducible stochastic factualization;
- Born measure/typicality;
- quotient descent of emergent continuum structures;
- metric duration, Lambda, O(3), HDA, spin-2 and nonlinear GR.

## 15. GR traffic light

🟢 **Conceptual advance:** the single-history/reduction intuition now has exact path-space mathematics and a sharp symmetry constraint.

🟢 **Localization:** the missing physics is specifically the symmetry-breaking/contextual rule or datum mapping the supported weighted branch set to one factual event.

🟡 **Initial impulse remains viable but unearned:** it can be represented exactly, but current Q does not yet give it physical status.

🔴 **No GR promotion:** Born remains not derived; O(3), HDA, spin-2 and nonlinear GR remain open/unestablished.
