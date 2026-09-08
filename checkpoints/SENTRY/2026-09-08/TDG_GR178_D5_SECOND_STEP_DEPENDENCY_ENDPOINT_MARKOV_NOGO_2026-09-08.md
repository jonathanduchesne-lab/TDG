# Complete TDG / Unified Bridge Sentry — GR178 D5 second-step dependency / endpoint-Markov audit

**Date:** 2026-09-08 (America/Toronto)  
**Classification:** **POSITIVE SEQUENTIAL INCIDENCE-DEPENDENCY PASS / ENDPOINT-STATE MEDIATION EXACT / AF NONENDPOINT RESIDUAL NOT EARNED**  
**Historical FINAL-CERTIFIED authority:** `Q-B1858L`, unchanged.

---

## 1. Question

After the GR178 D4→D5 typing correction, the useful remaining structural question is not whether the first successor has incidence 5. It is:

> Does the first legal move change the **law of the second move** in a way that cannot be reduced to the first successor's local endpoint state?

This is the minimal source-level question required before spending a cold Q-response replay on D5.

---

## 2. Frozen pulse terminal geometry

GR177's three independent incidence-4 terminal controls are:

- `pulse_d2`, current TIP profile `{2,2,2,4}`;
- `pulse_d5`, current TIP profile `{2,2,2,4}`;
- `pulse_d8`, current TIP profile `{2,2,2,4}`.

The four legal current actions are the four B3 ports of the TIP.

Thus each pulse control has one distinguished high-incidence old port `h` with incidence 4 and three ordinary old ports with incidence 2.

GR178's exact stellar rewrite is frozen:

1. current TIP becomes internal;
2. **all four old B3 ports gain +1 incidence**;
3. four new boundary B4 faces are created, one associated with each old port;
4. the B4 associated with the selected port becomes the successor TIP;
5. the successor TIP contains its associated old selected port plus three new x-containing B3 intersections, each born at incidence 2.

No new Q law is introduced by GR178.

---

## 3. First-step branching theorem

Before the move:

`{4,2,2,2}`.

After any first stellar move, the old ports become

`{5,3,3,3}`.

Hence **all four first moves enter exact D=5**.

But the new successor TIP depends on which port was selected.

### Branch A — select the high port

If the selected old port was the incidence-4 port, the successor TIP contains the same physical old face after its update to 5:

`TIP_A = {5,2,2,2}`.

There is exactly **one** such first move per pulse control.

### Branch B — select any ordinary port

If one of the three incidence-2 old ports is selected, the successor TIP contains that port after `2→3` plus three new incidence-2 intersections:

`TIP_B = {3,2,2,2}`.

The old high face has still become 5 globally, but it lies on the neighboring new B4 associated with the high port rather than on the chosen successor TIP.

There are exactly **three** such first moves per pulse control.

Across the three pulse controls this gives the documented 12 D5 exits as:

- 3 direct-high successor branches;
- 9 side-successor branches.

---

## 4. Exact second-step dependency

GR178's same stellar rule applies to the next current TIP: every old B3 port of that TIP gains +1.

Therefore:

### After Branch A

Because the incidence-5 face is itself a port of the current successor TIP, **every legal second move** increments it again:

`5 -> 6`.

### After Branch B

Because the incidence-5 face is not a port of the current successor TIP, the next stellar attachment does not touch that face:

`5 -> 5`

at this second step.

Thus the first move genuinely changes the incidence update experienced by the concentrated face at the second move.

Classification:

**FIRST MOVE -> SECOND-STEP INCIDENCE LAW = POSITIVE SEQUENTIAL DEPENDENCY.**

This is stronger than a statement that the first endpoint differs numerically.

---

## 5. Why this is still not AF `N_12`

The same calculation supplies the decisive matched-endpoint control.

The two first-successor TIP states are already distinguishable locally:

- Branch A: `{5,2,2,2}`;
- Branch B: `{3,2,2,2}`.

Once the complete successor local state is specified, the second stellar update is deterministic. No additional realized-history label is required to know whether the high face is incremented.

Therefore the two-step dependence factors as

`first move -> successor local endpoint state -> second update`.

There is no residual of the form

`same successor local state + different realized first history -> different second transition law`

in the exact incidence rewrite audited here.

This is the precise endpoint-Markov pattern that the frozen AF matched-control firewall requires us to subtract.

Hence:

**SEQUENTIAL DEPENDENCY = REAL**, but

**NONENDPOINT / DIRECT-PRODUCT-NORMAL PROCESS RESIDUAL = ZERO AT THE INCIDENCE-REWRITE LEVEL.**

No AF soldering margin is earned from this combinatorial dependency alone.

---

## 6. Scientific consequence

The next useful test becomes sharper still.

Do not compare Branch A and Branch B as if their different second-step incidence were already AF evidence. Their successor endpoint states differ, so an ordinary Markov/local-state model reproduces the distinction exactly.

Instead ask whether the actual Q response supplies one of the following:

1. two histories with the **same full successor `M_Q^(2)` local state** but different next-transition Q operator/morphism;
2. an off-diagonal/inter-fibre two-event block not determined by either successor endpoint state;
3. a conditional second-event instrument that changes under causal break while the matched successor endpoint response is frozen;
4. a higher/boundary/inflow datum not reducible to the local stellar state update.

Only such a residual may proceed as `N_12(a)`.

---

## 7. DERIVED / ASSUMED / OPEN / NEXT

### DERIVED

1. Each pulse terminal has one incidence-4 and three incidence-2 current TIP ports.
2. All four first moves enter D=5 because every old port gets +1.
3. Selecting the high port yields successor TIP `{5,2,2,2}`; selecting a side port yields `{3,2,2,2}`.
4. There are 3 direct-high and 9 side D5 exits across the three pulse controls.
5. At the next move, direct-high branches force the concentrated face `5→6`; side branches leave it at 5.
6. The first move therefore changes the second-step incidence law.
7. The distinction is exactly encoded in the successor local endpoint state, so no extra history variable is required.

### ASSUMED / INHERITED

- Exact GR178 local stellar rewrite and GR177 pulse profiles.
- Root1/global-Q/factual-ledger firewalls.
- AF requires subtraction of complete matched endpoint/local-state response before calling a transition residual microscopic-normal.

### OPEN

- D5 Q-response operator after the first successor;
- same-endpoint/history-dependent conditional Q transition morphism;
- causal-break-sensitive two-event Q block;
- coherent higher or boundary/inflow escape.

### NEXT

Search the archives first for a D5/high-incidence **Q response transition** where the successor local endpoint can be matched across distinct histories. If none exists, recover the GR177/178 production chain before any new cold computation. The key test is not different endpoint response; it is different **next operator at fixed full local endpoint state**.

---

## 8. Verification

Portable algebraic verifier:

`repro/sentry/2026-09-08/verify_gr178_d5_second_step_markov.py`

Result: **8/8 PASS**.

SHA-256:

- verifier: `b755e7a1a34145368b57b03504b5ed2c2281b7b98dc2c72e9487b655e41e1de5`
- results: `e2a8f3aeb6a010131291a1d555d41ea3547a727e4f9dafc539411c9b717c6a62`
- verify text: `75760b6fd7e35c0d0edbba8556dc8d0e46090b85d01f01ec5afb1e21d09ce404`

---

## 9. Global status

No AF soldering margin earned.  
AC quotient-lock not reached.  
Two-helicity `q^2` and common Lorentz cone unchanged.  
O(3) remains FAIL / NOT CLOSED.  
Full nonlinear GR remains **NOT ESTABLISHED**.
