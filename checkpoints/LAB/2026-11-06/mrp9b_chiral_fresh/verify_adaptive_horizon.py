#!/usr/bin/env python3
"""Uniform-in-horizon sufficient condition for unbiased physical chiral refresh.

Mathematical comparator only: refresh durations delta_n=a/(n+1)^p with
1/2 < p <= 1, so sum_n delta_n = infinity yet sum_n delta_n^2 < infinity.
The fresh unbiased random-unitary channel differs from the free unitary
in trace distance by <= ||V||^2 sum delta_n^2 on all finite horizons.
"""
from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
from numpy.linalg import eigvalsh,eigh,norm
HERE=Path(__file__).resolve().parent
r=json.loads((HERE/'results.json').read_text());c=r['chirality_coupling_used']
J=np.zeros((3,5));J[0,4]=J[1,3]=J[2,2]=-1/math.sqrt(3)
H0=np.diag([1.]*5+[1.7]*3).astype(complex)
V=np.zeros((8,8),complex);V[:5,5:]=c*J.T;V[5:,:5]=c*J
Ep,Pp=eigh(H0+V);Em,Pm=eigh(H0-V)
Vop=float(max(abs(eigvalsh(V))))
Tpref=np.zeros(8,complex);Tpref[0]=1/math.sqrt(2);Tpref[2]=1/math.sqrt(2)
rhoinit=np.outer(Tpref,Tpref.conj())

# The independent channel's second derivative in the coupling parameter
# has induced trace norm <=4*delta^2*||V||^2. Symmetric average difference
# from unitary H0 is bounded by 2*delta^2*||V||^2. Half trace norm gets
# <= delta^2*||V||^2 per step. Triangle+trace contraction telescopes.

def stepU(eval,vec,dt):
    return (vec*np.exp(-1j*eval*dt))@vec.conj().T

def experiment(a,p,N=12000):
    rho=rhoinit.copy();T=0.0;sd2=0.0;rows=[]
    for n in range(1,N+1):
        d=a/n**p;T+=d;sd2+=d*d
        Up=stepU(Ep,Pp,d);Um=stepU(Em,Pm,d)
        rho=.5*(Up@rho@Up.conj().T+Um@rho@Um.conj().T)
        if n in [10,100,1000,N]:
            U0=np.diag(np.exp(-1j*np.diag(H0)*T));ref=U0@rhoinit@U0.conj().T
            delta=(rho-ref);trdist=.5*float(np.sum(abs(eigvalsh((delta+delta.conj().T)/2))))
            bound=Vop**2*sd2
            rows.append(dict(steps=n,T=T,quadratic_time_sum=sd2,distance=trdist,bound=bound,
                 vector_probability=float(np.trace(rho[5:,5:]).real),state_trace=float(np.trace(rho).real)))
            assert trdist<=bound+1e-9,(a,p,n,trdist,bound)
            assert abs(np.trace(rho).real-1)<1e-8
    return rows

rows=[];p=.6
for a in (.2,.1):
    data=experiment(a,p)
    rows.append(dict(a=a,p=p,history=data,upper_bound_infinite_horizon_estimate=float(Vop**2 *a*a *sum(n**(-2*p) for n in range(1,200000)))))
    print('ADAPTIVE',a, data[-1],flush=True)

# A rigorous tail bound for infinite sum n^-s (s>1): sum_{n>N}n^-s <=N^(1-s)/(s-1).
maxN=200000;s=2*p
zeta_est=sum(n**(-s) for n in range(1,maxN+1))
tail=(maxN**(1-s))/(s-1)
upper=zeta_est+tail
assert upper>zeta_est
for row in rows:row['guaranteed_all_horizons_trace_distance_upper_bound']=float(Vop**2 *row['a']**2 *upper)

out={'classification':'MATHEMATICAL SUFFICIENT CONDITION for a new nonstationary refresh law; no physical time scaling derived by TDG',
  'finite_T_source_c':c,'p':p,'sum_dt_diverges':True,'sum_dt_squared_converges':True,
  'proof':'Symmetric random-unitary average cancels O(dt) coupling; one-step trace distance <= ||V||^2 dt^2; telescoping CP contractions gives uniform trace distance <= ||V||^2 a^2 zeta(2p), all finite N. Sum dt = infinite for p<=1.',
  'op_norm_V':Vop,'zeta_upper_bound':upper,'rows':rows,
  'firewalls':['The schedule delta_n=a/n^p is imposed; no TDG proper-time or event-rate law implies it.',
   'For fixed a>0 there can be a finite accumulated nonunitary correction; only uniform a->0 is proven.',
   'No Einstein action, HDA or physical SO3 frame dynamics is derived.']}
(HERE/'adaptive_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('DONE',HERE/'adaptive_results.json')
