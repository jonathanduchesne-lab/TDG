"""Exact numerical classification of rotation-covariant maps STF2->V,
with/without one spatial derivative. Complements the spin-3 experiment."""
import json
from pathlib import Path
import numpy as np
from numpy.linalg import norm
from scipy.linalg import svd

rng=np.random.default_rng(92383)
def eij(i,j):
 A=np.zeros((3,3));A[i,j]=1.;return A
E=np.array([
 np.diag([1.,-1.,0.])/np.sqrt(2),np.diag([1.,1.,-2.])/np.sqrt(6),
 (eij(0,1)+eij(1,0))/np.sqrt(2),(eij(0,2)+eij(2,0))/np.sqrt(2),
 (eij(1,2)+eij(2,1))/np.sqrt(2)])
def U(R):
 ER=np.einsum('ij,ajk,lk->ail',R,E,R)
 return np.einsum('aij,bij->ab',E,ER)
def Rrandom():
 A=rng.normal(size=(3,3));Q,Z=np.linalg.qr(A)
 s=np.sign(np.diag(Z));s[s==0]=1
 Q=Q@np.diag(s)
 if np.linalg.det(Q)<0:Q[:,0]*=-1
 return Q
ROTS=[Rrandom() for _ in range(14)]
# Constant M: R M = M U(R). Hom_SO3(STF2,V) is zero.
M0=[]
for R in ROTS:
 UU=U(R)
 cols=[]
 for a in range(15):
  M=np.zeros((3,5));M.flat[a]=1
  cols.append((M@UU-R@M).reshape(-1))
 M0.append(np.column_stack(cols))
A0=np.vstack(M0)
s0=svd(A0,compute_uv=False)
rank0=int(np.sum(s0>1e-9));null0=15-rank0
assert rank0==15 and null0==0

# First derivative M(k)=sum_j k_j A_j; SO3 intertwining constraints.
# for each k=e_m: sum_j R_{jm} A_j U(R) = R A_m.
M1=[]
for R in ROTS:
 UU=U(R)
 cols=[]
 for d in range(45):
  blocks=np.zeros((3,3,5))
  blocks.flat[d]=1
  defects=[]
  for m in range(3):
   left=sum(R[j,m]*blocks[j]@UU for j in range(3))
   right=R@blocks[m]
   defects.append((left-right).reshape(-1))
  cols.append(np.concatenate(defects))
 M1.append(np.column_stack(cols))
A1=np.vstack(M1)
Uvals,s1,Vh=svd(A1,full_matrices=False)
rank1=int(np.sum(s1>1e-9));null1=45-rank1
assert rank1==44 and null1==1, (rank1,s1[-5:])

# Compare singular nullvector with the physical divergence A_j[i,a]=E[a,i,j].
Div=np.einsum('aij->jia',E)
vec=Div.reshape(-1)
vec/=norm(vec)
vnull=Vh[-1]
fit=abs(float(vec@vnull))
residual=norm(A1@vec)
assert 1-fit<1e-12 and residual<1e-12

result={
  'constant_map':{'dimension':15,'constraint_rank':rank0,'equivariant_nullity':null0,'smallest_singular_value':float(s0[-1])},
  'linear_momentum_map':{'dimension':45,'constraint_rank':rank1,'equivariant_nullity':null1,'smallest_nonzero_singular':float(s1[-2]),'smallest_singular':float(s1[-1]),'overlap_with_divergence':fit,'divergence_residual':float(residual)},
  'physical_claim':'Under SO(3), no nonzero k-independent linear map STF2->V; with exactly one k, unique map is M_i=k^j h_ij up to an overall scalar. Source is representation theory, not an equation of TDG-Q.'
}
Path('/mnt/data/tdg_q_bridge_covariance_rank_resultats_2026_11_06.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result,indent=2))
