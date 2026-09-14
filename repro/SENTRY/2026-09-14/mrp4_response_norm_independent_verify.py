import itertools,json,math
from pathlib import Path
import numpy as np
rng=np.random.default_rng(7311014)
pairs=list(itertools.combinations(range(6),2))
F={}
for e in pairs:
    B=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    F[e]=B.conj().T@B+(0.15+0.03*(e[0]+1))*np.eye(2)

def chi(Fs,r=.5): return {e:float(np.linalg.det(X).real**r) for e,X in Fs.items()}
c=chi(F)
A=np.array([[0.83+0.11j,0.31-0.08j],[-0.23+0.14j,1.27+0.05j]],complex)
Ai=np.linalg.inv(A); Ft={e:Ai.conj().T@X@Ai for e,X in F.items()}; ct=chi(Ft)
s=1/abs(np.linalg.det(A)); ratios=np.array([ct[e]/c[e] for e in pairs])
lam=3.2
cl=chi({e:lam*X for e,X in F.items()})
rs=[.2,.5,.8,1.2]
errs={r:abs(lam**(2*r)-lam)/lam for r in rs}
mineig=min(np.linalg.eigvalsh(X).min() for X in F.values())
c05=np.array([np.linalg.det(F[e]).real**.5 for e in pairs])
c10=np.array([np.linalg.det(F[e]).real for e in pairs])
a=np.dot(c10,c05)/np.dot(c10,c10); sep=np.linalg.norm(c05-a*c10)/np.linalg.norm(c05)
checks={'positive_chart':bool(mineig>0),'GL2_relative_invariance':bool(np.max(np.abs(ratios-s))<1e-12),'degree1_response_scaling':bool(max(abs(cl[e]-lam*c[e]) for e in pairs)<1e-11),'r_half_unique_in_test_family':bool(errs[.5]<1e-13 and all(errs[r]>1e-3 for r in rs if r!=.5)),'different_det_powers_not_same_ray':bool(sep>1e-3)}
out={'gate':'independent Herm2 response-norm scalarization verify','checks':checks,'pass_count':sum(checks.values()),'check_count':len(checks),'metrics':{'min_eig':float(mineig),'expected_GL2_scale':float(s),'scale_ratio_max_defect':float(np.max(np.abs(ratios-s))),'degree_errors':errs,'r05_vs_r1_projective_sep':float(sep)},'classification':'PASS' if all(checks.values()) else 'FAIL'}
Path('/mnt/data/tdg_mrp5/MRP4_RESPONSE_NORM_INDEPENDENT_VERIFY.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))