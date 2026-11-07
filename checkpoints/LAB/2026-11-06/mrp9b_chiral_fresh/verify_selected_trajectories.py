#!/usr/bin/env python3
"""Single selected factual histories: independent binary orientation labels.

A CP mean may look isotropic while individual selected histories remain
anisotropic. This adversary tests a sample of actual conditional pure paths.
The Bernoulli labels and 8D sector dynamics are new experimental postulates,
not the Root2 Q selection law.
"""
from pathlib import Path
import json,math
import numpy as np
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'results.json').read_text())
c=base['chirality_coupling_used'];J=np.zeros((3,5));J[0,4]=J[1,3]=J[2,2]=-1/math.sqrt(3)
H0=np.diag([1.]*5+[1.7]*3).astype(complex)
V=np.zeros((8,8),complex);V[:5,5:]=c*J.T;V[5:,:5]=c*J
psi0=np.zeros(8,complex);psi0[0]=psi0[2]=1/math.sqrt(2)
T=4.0;ref=expm(-1j*T*H0)@psi0
rng=np.random.default_rng(20261106)
rows=[];trials=1600
for p in (.5,.7):
 for N in (128,512,2048):
    dt=T/N;Up=expm(-1j*dt*(H0+V));Um=expm(-1j*dt*(H0-V))
    states=np.tile(psi0[:,None],(1,trials)); psum=np.zeros(trials)
    for _ in range(N):
        choices=(rng.random(trials)<p)
        plus=Up@states;minus=Um@states
        states=np.where(choices[None,:],plus,minus)
        psum+=choices.astype(float)
    vprobs=np.sum(abs(states[5:,:])**2,axis=0).real
    fidelity=np.abs(ref.conj()@states)**2
    trdist=np.sqrt(np.maximum(0,1-fidelity))
    row={'p_plus':p,'steps':N,'dt':dt,'trials':trials,
      'mean_vector_probability':float(np.mean(vprobs)),
      'p90_vector_probability':float(np.quantile(vprobs,.9)),
      'p99_vector_probability':float(np.quantile(vprobs,.99)),
      'mean_selected_trace_distance':float(np.mean(trdist)),
      'p90_selected_trace_distance':float(np.quantile(trdist,.9)),
      'mean_realized_plus_fraction':float(np.mean(psum/N)),
      'state_norm_max_err':float(max(abs(np.sum(abs(states)**2,axis=0)-1)))}
    print('SELECTED',row,flush=True)
    assert row['state_norm_max_err']<1e-10
    rows.append(row)
for N in (128,512,2048):
    x=next(r for r in rows if r['p_plus']==.5 and r['steps']==N)
    assert x['mean_vector_probability']<.04 and x['mean_selected_trace_distance']<.1
unbiased=[r for r in rows if r['p_plus']==.5]
assert unbiased[-1]['mean_selected_trace_distance']<unbiased[0]['mean_selected_trace_distance']*.34
out={'classification':'Finite-sample selected paths of new Q-inspired 8D two-sign instrument; NOT Root2 fact-selection law',
     'amplitude_from_Q':c,'trials_per_case':trials,'results':rows,
     'conclusion':'p=1/2 selected histories converge in probability as dt->0 at fixed T, slower (roughly sqrt(dt) in pure-state distance) than unselected density; bias p=.7 fails.',
     'limitations':['Sample is Monte Carlo evidence, not a uniform pathwise bound.',
       'No Born probability or fresh label selection law is derived by original TDG Q.',
       'At fixed dt and T->infinity, there is no persistent recovery.']}
(HERE/'selected_results.json').write_text(json.dumps(out,indent=2)+'\n')
