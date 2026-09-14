import itertools, json, math
import numpy as np
from pathlib import Path

q=np.array([[1/math.sqrt(2),1/math.sqrt(6)],[-1/math.sqrt(2),1/math.sqrt(6)],[0,-2/math.sqrt(6)]],float)
d=2.3
c=0.41
G4=np.full((4,4),c,float); np.fill_diagonal(G4,d)
eigs=np.linalg.eigvalsh(G4)
pair_det={}; pair_chi={}
for u,v in itertools.combinations(range(4),2):
    M=G4[np.ix_([u,v],[u,v])]
    det=float(np.linalg.det(M)); pair_det[(u,v)]=det; pair_chi[(u,v)]=math.sqrt(det)
chi0=next(iter(pair_chi.values()))
D=np.diag([chi0,chi0,chi0]); G=q.T@D@q; P=G/math.sqrt(np.linalg.det(G))
rng=np.random.default_rng(20260914)
H=rng.normal(size=(4,4)); H=(H+H.T)/2
H-=np.mean(np.diag(H))*np.eye(4)
off=[H[i,j] for i in range(4) for j in range(i+1,4)]; mean_off=np.mean(off)
for i in range(4):
    for j in range(i+1,4): H[i,j]-=mean_off; H[j,i]=H[i,j]
eps=1e-5; Ga=G4+eps*H; chi_aniso={}; lin_pred={}
for u,v in itertools.combinations(range(4),2):
    M=Ga[np.ix_([u,v],[u,v])]; chi_aniso[(u,v)]=math.sqrt(float(np.linalg.det(M)))
    du=H[u,u]; dv=H[v,v]; dc=H[u,v]
    lin_pred[(u,v)]=chi0+eps*(d*(du+dv)-2*c*dc)/(2*chi0)
max_lin_err=max(abs(chi_aniso[e]-lin_pred[e]) for e in chi_aniso); spread=max(chi_aniso.values())-min(chi_aniso.values())
checks={'homogeneous_gram_positive_definite':bool(eigs.min()>0),'all_pair_minor_determinants_equal':bool(max(pair_det.values())-min(pair_det.values())<1e-14),'all_pair_chi_equal':bool(max(pair_chi.values())-min(pair_chi.values())<1e-14),'MRP4_positive_factor_identity':bool(np.linalg.norm(P-np.eye(2))<1e-14),'anisotropic_perturbation_splits_pair_chi':bool(spread>1e-8),'linearized_pair_chi_formula_verified':bool(max_lin_err<1e-9)}
out={'gate':'current-Q pair-minor chi homogeneous-phase MRP4 collapse','theorem':{'base':'S4-central Gram has G_uu=d and G_uv=c for u!=v','pair_minor':'det G^(uv)=d^2-c^2 independent of pair','chi':'chi_uv=sqrt(d^2-c^2) is uniform','MRP4_consequence':'D_Fe=chi I3, G_Fe=chi I2, P_Fe=I; response reduces exactly to MRP3 incidence map','linearized_anisotropic_response':'delta chi_uv=[d(delta d_u+delta d_v)-2c delta c_uv]/(2 sqrt(d^2-c^2))'},'metrics':{'G4_eigenvalues':eigs.tolist(),'pair_det_value':chi0**2,'chi_uniform_value':chi0,'P_identity_defect':float(np.linalg.norm(P-np.eye(2))),'anisotropic_chi_spread_at_eps_1e-5':float(spread),'linearization_max_abs_error':float(max_lin_err)},'checks':checks,'pass_count':sum(checks.values()),'check_count':len(checks),'classification':{'homogeneous_currentQ_pair_minor_chi_as_noncompact_MRP4_source':'EXACT FAIL / COLLAPSES TO UNIFORM MRP3 LIMIT','anisotropic_pair_minor_chi_capacity':'OPEN / NONTRIVIAL AT LINEAR ORDER','physical_anisotropic_process_source_typing':'NOT DERIVED BY THIS TEST'}}
Path('/mnt/data/tdg_mrp5/CURRENT_Q_PAIR_MINOR_HOMOGENEOUS_COLLAPSE_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True))
print(json.dumps(out,indent=2,sort_keys=True))