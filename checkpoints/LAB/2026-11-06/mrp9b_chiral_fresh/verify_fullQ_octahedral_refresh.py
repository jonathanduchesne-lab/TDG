#!/usr/bin/env python3
"""No-ray-projection control: randomize all 24 physical cubic orientations of
actual finite-cutoff Q-B1852 A21, including its non-J subleading remainder.

Fixed SO3 group basis assumes a *new* physical coupling orientation dynamics.
Passive basis relabeling is NOT interpreted as a physical repair.
"""
import os,sys,itertools,io,contextlib,json,math
from pathlib import Path
import numpy as np
from numpy.linalg import norm,svd,eigh
from scipy.linalg import expm
HERE=Path(__file__).resolve().parent
SRC=Path(os.environ.get('TDG_Q1852_SOURCE','/mnt/data/tdg_source_lab/qb1852_extracted/qb1852_full_refined.py'))
sys.path.insert(0,str(SRC.parent))
with contextlib.redirect_stdout(io.StringIO()):import qb1852_full_refined as q
with contextlib.redirect_stdout(io.StringIO()): x=q.analyze('b4',.025,2+.7j,do_second=False)
_,coef=q.irreps();A21=x['C'][1:4,:]@np.column_stack(coef[1:])
E=np.array([np.diag([1.,-1.,0.])/np.sqrt(2.),np.diag([1.,1.,-2.])/np.sqrt(6.),
    [[0.,1/math.sqrt(2),0.],[1/math.sqrt(2),0.,0.],[0.,0.,0.]],
    [[0.,0.,1/math.sqrt(2)],[0.,0.,0.],[1/math.sqrt(2),0.,0.]],
    [[0.,0.,0.],[0.,0.,1/math.sqrt(2)],[0.,1/math.sqrt(2),0.]]])
Oct=[]
for perm in itertools.permutations(range(3)):
 for signs in itertools.product((-1.,1.),repeat=3):
  R=np.eye(3)[:,perm]@np.diag(signs)
  if round(np.linalg.det(R))==1:Oct.append(R)
assert len(Oct)==24

def U5(R):return np.einsum('aij,ik,bkl,jl->ab',E,R,E,R)
Arot=[R@A21@U5(R).T for R in Oct]
Aavg=np.mean(Arot,axis=0)
assert norm(Aavg)<1e-13
H0=np.diag([1.]*5+[1.7]*3).astype(complex)
Hs=[]
for A in Arot:
 V=np.zeros((8,8),complex);V[:5,5:]=A.T;V[5:,:5]=A;Hs.append(H0+V)
psi=np.zeros(8,complex);psi[0]=psi[2]=1/math.sqrt(2)
rho=np.outer(psi,psi.conj());T=4.

def eigtrace(M):return .5*float(np.sum(abs(eigh((M+M.conj().T)/2)[0])))

Ustatic=[expm(-1j*T*H) for H in Hs]
static=sum((U@rho@U.conj().T for U in Ustatic),np.zeros((8,8),complex))/len(Hs)
stat_vec=float(np.trace(static[5:,5:]).real)
print('STATIC 24',stat_vec,flush=True)
rows=[]
for N in [40,160,640]:
 dt=T/N;Us=[expm(-1j*dt*H) for H in Hs];cur=rho.copy()
 for _ in range(N):
  nxt=np.zeros_like(cur)
  for U in Us:nxt+=(U@cur@U.conj().T)/24
  cur=nxt
 ref=expm(-1j*T*H0)@rho@expm(1j*T*H0)
 Uerr=max(norm(U.conj().T@U-np.eye(8)) for U in Us)
 cp_error=norm(sum((U.conj().T@U for U in Us),np.zeros((8,8),complex))/24-np.eye(8))
 row=dict(steps=N,dt=dt,vector_probability=float(np.trace(cur[5:,5:]).real),distance_from_reference=eigtrace(cur-ref),
  cp_error=float(cp_error),max_unitarity_error=float(Uerr),state_trace=float(np.trace(cur).real))
 rows.append(row);print('FRESH full Q 24',row,flush=True)
 assert Uerr<1e-12 and cp_error<1e-12 and abs(row['state_trace']-1)<1e-10
assert rows[-1]['vector_probability']<rows[0]['vector_probability']*.1
out={'scope':'Actual finite-cutoff Q A21, all 24 active physical cubic orientations; dynamics is newly POSTULATED',
 'scheme':'b4','a':.025,'spectral_readout':'2+0.7j','A21_matrix':A21.tolist(),'A21_norm':float(norm(A21)),
 'mean_coupling_norm':float(norm(Aavg)),'n_orientations':24,
 'static_24_vector_probability':stat_vec,'fresh_24':rows,
 'caveats':['Finite-z A21 is a diagnostic, not a universal physical coupling.',
  'Physical refresh of octupolar background is added, not derived from Q.',
  'TT 2-helicity constraint algebra and GR nonlinear dynamics remain open.']}
(HERE/'fullQ_24_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('SAVED',HERE/'fullQ_24_results.json')
