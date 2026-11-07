#!/usr/bin/env python3
"""TDG exploratory math experiment: can a universal 'now' be forced by causal growth?

Exact finite-poset enumeration, standard library only.
Not a proof or experiment about reality or a full TDG theory.

A fact/effect a->b means a must have actualized before b. Incomparable
facts can actualize in either order or in the same front. A foliation is
an ordered partition into nonempty antichains obeying this precedence.
"""
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path


def ancestors_from_edges(n, edges):
    """Compute strict ancestor masks for a DAG with edges (i,j), i<j."""
    pred = [0] * n
    for i, j in edges:
        assert 0 <= i < j < n
        pred[j] |= 1 << i
    anc = [0] * n
    for j in range(n):
        total = pred[j]
        for i in range(j):
            if (pred[j] >> i) & 1:
                total |= anc[i]
        anc[j] = total
    return tuple(anc)


def available(mask, ancestors):
    missing = ((1 << len(ancestors)) - 1) ^ mask
    avail = 0
    for i, parent_mask in enumerate(ancestors):
        if (missing >> i) & 1 and not (parent_mask & missing):
            avail |= 1 << i
    return avail


def counts(ancestors):
    """# linear extensions and # ordered antichain foliations, exactly."""
    n = len(ancestors)
    full = (1 << n) - 1

    @lru_cache(None)
    def rec(mask):
        if mask == full:
            return (1, 1)
        avail = available(mask, ancestors)
        sub = avail
        seq, fronts = 0, 0
        while sub:
            other_seq, other_fronts = rec(mask | sub)
            fronts += other_fronts
            if sub & (sub - 1) == 0:  # select a single fact now
                seq += other_seq
            sub = (sub - 1) & avail
        return seq, fronts
    return rec(0)


def parallel_frontier_rule(ancestors):
    """Candidate additional dynamics: actualize EVERY causally eligible event per tick.
    This selects a common front by a NEW rule rather than by causality alone.
    """
    n = len(ancestors)
    mask = 0
    fronts = []
    full = (1 << n) - 1
    while mask != full:
        now = available(mask, ancestors)
        assert now
        fronts.append(tuple(i for i in range(n) if (now >> i) & 1))
        mask |= now
    return fronts


def list_foliations(ancestors, labels):
    n = len(ancestors)
    full = (1 << n) - 1
    out = []
    def walk(mask, fronts):
        if mask == full:
            out.append(tuple(fronts))
            return
        avail = available(mask, ancestors)
        sub = avail
        while sub:
            group = tuple(labels[i] for i in range(n) if (sub >> i) & 1)
            walk(mask | sub, fronts + [group])
            sub = (sub - 1) & avail
    walk(0, [])
    return sorted(out, key=lambda v: (len(v), str(v)))


def earliest_latest(ancestors):
    """Two valid causal time assignments with the same minimal #levels."""
    n = len(ancestors)
    early = []
    for i in range(n):
        early.append(1 + max((early[j] for j in range(i) if (ancestors[i] >> j) & 1), default=-1))
    maxlevel = max(early)
    futures = []
    for i in range(n):
        futures.append(sum((1 << j) for j in range(i + 1, n) if (ancestors[j] >> i) & 1))
    lag = [0] * n
    for i in reversed(range(n)):
        lag[i] = 1 + max((lag[j] for j in range(i + 1, n) if (futures[i] >> j) & 1), default=-1)
    late = [maxlevel - x for x in lag]
    assert all(early[i] < early[j] and late[i] < late[j]
               for j in range(n) for i in range(j) if (ancestors[j] >> i) & 1)
    return early, late


def enumerate_naturally_labeled_posets(n):
    """Enumerate unique causal orders with 0,1,..,n-1 one legal ordering.
    This is NOT all labeled posets; the ordering restriction is intentional.
    """
    pairs = list(combinations(range(n), 2))
    posets = set()
    for m in range(1 << len(pairs)):
        edges = [pair for k, pair in enumerate(pairs) if (m >> k) & 1]
        posets.add(ancestors_from_edges(n, edges))
    return posets


def main():
    path = Path('/mnt/data/tdg_resultats_emergence_present.txt')
    # Three events: A causes C, B completely independent.
    tri = ancestors_from_edges(3, [(0, 2)])
    triseq, trifronts = counts(tri)
    fols = list_foliations(tri, ['A', 'B', 'C'])
    early, late = earliest_latest(tri)
    assert (triseq, trifronts) == (3, 5)
    assert early == [0, 0, 1] and late == [0, 1, 1]
    # These two different shortest foliations are both causally valid:
    assert (('A','B'), ('C',)) in fols
    assert (('A',), ('B','C')) in fols

    # Two causally isolated regions, each has three successive events.
    twochains = ancestors_from_edges(6, [(0, 1), (1, 2), (3, 4), (4, 5)])
    chainseq, chainfronts = counts(twochains)
    assert chainseq == comb(6, 3) == 20
    assert counts(ancestors_from_edges(6, [])) == (720, 4683)

    # Exhaustive across distinct naturally-labeled causal orders of 5 facts.
    population = enumerate_naturally_labeled_posets(5)
    with_more_than_one = 0
    with_distinct_shortest = 0
    passing_parallel_rule = 0
    for causet in population:
        nlin, nfronts = counts(causet)
        if nfronts > 1:
            with_more_than_one += 1
        e, l = earliest_latest(causet)
        parallel = parallel_frontier_rule(causet)
        if all(all(e[j] == i for j in front) for i, front in enumerate(parallel)):
            passing_parallel_rule += 1
        if e != l:
            with_distinct_shortest += 1

    assert passing_parallel_rule == len(population)

    # Relativity: 4 billion ly in a frame where events are simultaneous.
    # Under boosts, t_B - t_A = - gamma beta D/c. Units D/c = 4e9 years.
    D_over_c = 4e9
    boosts = [0., .01, -.01, .1, -.1]
    time_offsets = {v: -(v / (1-v*v)**0.5)*D_over_c for v in boosts}
    assert abs(time_offsets[.01] + time_offsets[-.01]) < 1e-5

    lines = [
        'TDG - REAL TEST: DOES CAUSAL ACTUALIZATION FORCE A UNIVERSAL PRESENT?',
        'Exact arithmetic, finite causal partial orders, standard library only.',
        '',
        'EXAMPLE (A causes C; B is causally independent):',
        f'  Single-event growth sequences: {triseq}',
        f'  Admissible ordered-front decompositions: {trifronts}',
        f'  Earliest fronts: A={early[0]}, B={early[1]}, C={early[2]}',
        f'  Latest fronts:   A={late[0]}, B={late[1]}, C={late[2]}',
        '  Both achieve the MINIMUM of 2 fronts, but disagree about whether',
        '  B is simultaneous with A or with C.',
        '  All valid foliations:',
    ]
    lines.extend('    ' + ' | '.join('{' + ','.join(s) + '}' for s in f) for f in fols)
    lines += [
        '',
        'TWO INDEPENDENT REGIONS (3 causally ordered events each):',
        f'  One-event-at-a-time growth histories: {chainseq}',
        f'  All ordered antichain foliations: {chainfronts}',
        '  An update-every-ready-event rule gives the three shared layers',
        '  {A1,B1}, {A2,B2}, {A3,B3}, but that rule has to be added.',
        '',
        'EXHAUSTIVE FINITE-POSET SUBFAMILY, N=5:',
        '  Includes all distinct orders with 0<1<2<3<4 a legal growth ordering.',
        f'  Unique causal orders in this subfamily: {len(population)}',
        f'  More than one causally valid layering: {with_more_than_one}',
        f'  Earliest and latest MINIMAL-LENGTH layering disagree: {with_distinct_shortest}',
        f'  Unique fronts under new all-eligible-at-once rule: {passing_parallel_rule}',
        '',
        'RELATIVITY OF SIMULTANEITY (separation 4 billion light years):',
    ]
    lines.extend(f'  boost {v:+.0%} c: delta t = {dt/1e6:+,.2f} million years'
                 for v, dt in time_offsets.items())
    lines += [
        '',
        'LOGICAL RESULTS:',
        '  - Causality, order-respecting actualization, and a single factual history',
        '    do NOT force a unique universal simultaneity relation.',
        '  - A common actualization front CAN be defined; simultaneous update of',
        '    all ready events is a POSSIBLE new dynamical law, not a derivation',
        '    from causality alone.',
        '  - To make a privileged present necessary, TDG needs an independent',
        '    selection principle (and consequences compatible with observations).',
        '  - This toy mathematics is not a proof of or against fundamental TDG.',
    ]
    report = '\n'.join(lines) + '\n'
    path.write_text(report, encoding='utf-8')
    print(report)
    print('FILE:', path)


if __name__ == '__main__':
    main()
