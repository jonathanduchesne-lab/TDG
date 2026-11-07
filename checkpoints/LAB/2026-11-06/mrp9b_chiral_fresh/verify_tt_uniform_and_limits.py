#!/usr/bin/env python3
"""Adversarial controls for fresh physical octupole randomization.

No Q source re-evaluated: reads the verified Q-B1852 extracted coefficient
from results.json, then tests non-z TT directions and noncommuting limits.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
from scipy.linalg import expm, null_space
from numpy.linalg import norm,eigvalsh
HERE=Path(__file__).resolve().parent
parent=json.loads((HERE/'results.json').read_text())
c=parent['chirality_coupling_used']
E=np.array([np.diag([1.,-1.,0.])/np.sqrt(2.),np.diag([1.,1.,-2.])/np.sqrt(6.),
    [[0.,1/math.sqrt(2),0.],[1/math.sqrt(2),0.,0.],[0.,0.,0.]],
    [[0.,0.,1/math.sqrt(2)],[0.,0.,0.],[1/math.sqrt(2),0.,0.]],
    [[0.,0.,0.],[0.,0.,1/math.sqrt(2)],[0.,1/math.sqrt(2),0.]]])
J=np.zeros((3,5));J[0,4]=J[1,3]=J[2,2]=-1/math.sqrt(3)
H0=np.diag([1.]*5+[1.7]*3).astype(complex)
V=np.zeros((8,8),complex);V[:5,5:]=c*J.T;V[5:,:5]=c*J
Hp=H0+V;Hm=H0-V

def channel(psi,T,dt,p=.5):
    N=int(round(T/dt));assert abs(N*dt-T)<1e-9
    Up=expm(-1j*dt*Hp);Um=expm(-1j*dt*Hm)
    rho=np.outer(psi,psi.conj())
    for _ in range(N):rho=p*(Up@rho@Up.conj().T)+(1-p)*(Um@rho@Um.conj().T)
    return rho

rng=np.random.default_rng(20261106)
ks=[];states=[];projs=[]
for _ in range(40):
    k=rng.normal(size=3);k/=norm(k)
    D=np.einsum('aij,j->ia',E,k)
    TT=null_space(D,rcond=1e-12)
    assert TT.shape==(5,2)
    psi=np.zeros(8,complex);psi[:5]=(TT[:,0]+TT[:,1])/math.sqrt(2)
    P=np.zeros((8,8),complex);P[:5,:5]=TT@TT.T
    assert abs(norm(psi)-1)<1e-12
    ks.append(k);states.append(psi);projs.append(P)

rows=[]
for N in (32,128,512):
    dt=4./N;Up=expm(-1j*dt*Hp);Um=expm(-1j*dt*Hm)
    leaks=[];vecs=[]
    for psi,P in zip(states,projs):
        rho=np.outer(psi,psi.conj())
        for _ in range(N):rho=.5*(Up@rho@Up.conj().T+Um@rho@Um.conj().T)
        leaks.append(float(np.trace((np.eye(8)-P)@rho).real))
        vecs.append(float(np.trace(rho[5:,5:]).real))
    rows.append(dict(steps=N,dt=dt,mean_outside_TT=float(np.mean(leaks)),max_outside_TT=float(max(leaks)),
                     mean_vector_pop=float(np.mean(vecs)),max_vector_pop=float(max(vecs))))
    print('TT',rows[-1],flush=True)
assert rows[-1]['max_outside_TT'] < rows[0]['max_outside_TT']/8

# Nonuniform-in-time limit. At fixed refresh dt, the unbiased channel may
# reach a nonzero population in the vector branch for sufficiently long T.
psi=np.zeros(8,complex);psi[0]=1/math.sqrt(2);psi[2]=1/math.sqrt(2)
long=[]
for total in (4.,40.,400.,1600.):
    rho=channel(psi,total,.1,.5)
    p=float(np.trace(rho[5:,5:]).real)
    long.append(dict(time=total,dt=.1,steps=int(round(total/.1)),vector_pop=p,purity=float(np.trace(rho@rho).real)))
    print('LONG',long[-1],flush=True)
assert long[-1]['vector_pop']>.15, long

# At fixed horizon, dt->0 repairs; at fixed dt, horizon->infty does not.
# Note that the vector subspace reachable from this state is 1D, and only
# the cross (xy) half of the initial state mixes; limiting vector population 1/4.
out={'classification':'Comparator adversary; NOT physical TDG update',
     'J_Q_value':c,'TT_directions':len(ks),'TT_tests':rows,
     'long_time_noncommutativity':long,
     'conditional_long_time_limit_vector':.25,
     'limitations':['The TT projector is imposed from a GR reference, not derived from Q.',
       'The chiral signs are new active physical interventions, not passive changes of coordinates.',
       'The weak-step finite-T limit is nonuniform in T; no eternal stability proved.']}
(HERE/'adversarial_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('SAVED',HERE/'adversarial_results.json')
