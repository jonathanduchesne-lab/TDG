#!/usr/bin/env python3
"""TDG toy-model checks: joint/global vs sequential actualization.
Not a validation of TDG or a quantum-gravity model. Standard library only.
"""
from itertools import permutations, product
from math import sqrt

# P precedes A and B, both precede D. A and B are incomparable.
events = ("P", "A", "B", "D")
prec = {("P", "A"), ("P", "B"), ("A", "D"), ("B", "D")}
valid_orders = [t for t in permutations(events) if all(t.index(i) < t.index(j) for i, j in prec)]
assert valid_orders == [("P", "A", "B", "D"), ("P", "B", "A", "D")]
# Canonical layers of this finite directed acyclic graph by longest ancestral path.
layers = {}
for t in valid_orders[:1]:
    for e in t:
        parents = [p for p, ch in prec if ch == e]
        layers[e] = max((layers[p] + 1 for p in parents), default=0)
assert layers == {"P": 0, "A": 1, "B": 1, "D": 2}

# One joint/global distribution on two spacelike outcomes.
joint = {(0,0): .45, (0,1): .05, (1,0): .05, (1,1): .45}
assert abs(sum(joint.values()) - 1) < 1e-12

def factorize(order, p):
    first = 0 if order == 'A-first' else 1
    second = 1-first
    marg = {s: sum(w for z,w in p.items() if z[first] == s) for s in sorted({z[first] for z in p})}
    out = {}
    for bits, w in p.items():
        p_first = marg[bits[first]]
        p_second_given_first = w / p_first
        out[bits] = p_first * p_second_given_first
    return out

ab = factorize('A-first', joint)
ba = factorize('B-first', joint)
assert all(abs(ab[k]-ba[k])<1e-12 and abs(ab[k]-joint[k])<1e-12 for k in joint)

# Arbitrarily changing transition laws between orders makes the final history order-dependent.
bad_ba = {(0,0): .375,(0,1):.125,(1,0):.125,(1,1):.375}
total_variation = .5*sum(abs(joint[k]-bad_ba[k]) for k in joint)
assert abs(total_variation-.15)<1e-12

# CHSH with ideal binary outputs a,b in {-1,+1}. E00=E01=E10=+1/sqrt2, E11=-1/sqrt2.
def bell_table(strength):
    result = {}
    for x,y in product((0,1), repeat=2):
        corr = strength * (-1 if (x,y) == (1,1) else 1)
        result[x,y] = {(a,b):(1+a*b*corr)/4 for a,b in product((-1,1),repeat=2)}
    return result

def analyze_bell(table):
    E, max_signal = {}, 0.0
    for x,y in product((0,1),repeat=2):
        p = table[x,y]
        assert abs(sum(p.values())-1)<1e-12
        E[x,y] = sum(a*b*prob for (a,b),prob in p.items())
    # Changing remote knob should not change the local marginals.
    for x in (0,1):
        for a in (-1,1):
            mx = [sum(prob for (aa,bb), prob in table[x,y].items() if aa==a) for y in (0,1)]
            max_signal = max(max_signal,abs(mx[0]-mx[1]))
    for y in (0,1):
        for b in (-1,1):
            my = [sum(prob for (aa,bb), prob in table[x,y].items() if bb==b) for x in (0,1)]
            max_signal = max(max_signal,abs(my[0]-my[1]))
    S = E[0,0] + E[0,1] + E[1,0] - E[1,1]
    # Both sequential orders must reconstruct every joint probability table.
    max_order_error = max(abs(factorize('A-first',t)[ab]-factorize('B-first',t)[ab])
                          for t in table.values() for ab in t)
    return S, max_signal, max_order_error

quantum = analyze_bell(bell_table(1/sqrt(2)))
pr_box = analyze_bell(bell_table(1.))
assert abs(quantum[0] - 2*sqrt(2))<1e-12
assert abs(pr_box[0] - 4)<1e-12
assert quantum[1:] == (0.,0.) and pr_box[1:] == (0.,0.)

# Two spacelike-separated events: distinct admissible foliations each preserve causal ordering.
# Units: t in years, x in light years, c=1 light year / year. T_k = t + k*x/c.
D = 4e9
foliation_offsets = {k: k * D for k in (0, .001, .01, .1)}
assert all(abs(k)<1 for k in foliation_offsets)

print('TDG EXACT TOY MODEL TESTS')
print('-------------------------')
print('Causal growth linear extensions:', valid_orders)
print('Canonical finite causal layers:', layers)
print('Global joint P(A,B):', joint)
print('Global vs A-first vs B-first max absolute error:', max(max(abs(joint[k]-ab[k]),abs(joint[k]-ba[k])) for k in joint))
print('Inconsistent sequential-order dynamics total-variation distance:', total_variation)
print('Quantum CHSH |S|, max signaling, order error:',quantum)
print('PR-box CHSH |S|, max signaling, order error:',pr_box)
print('Two events 4 billion ly apart, delta T_k (years):',foliation_offsets)
print('CONCLUSION: same factual joint history can be generated globally or in either causal-compatible sequential labeling.')
print('No preferred foliation follows from that construction; no-signaling and order independence alone do not select quantum statistics.')
