import itertools, math, json
from pathlib import Path
import numpy as np

V=tuple(range(6)); B2=list(itertools.combinations(V,2)); B3=list(itertools.combinations(V,3))
inc=[(F,e) for F in B3 for e in B2 if set(e).issubset(F)]
idxE={e:i for i,e in enumerate(B2)}; idxF={F:i for i,F in enumerate(B3)}
q=np.array([[1/math.sqrt(2),1/math.sqrt(6)],[-1/math.sqrt(2),1/math.sqrt(6)],[0,-2/math.sqrt(6)]],float)

def perfect_matchings(C):
    C=tuple(sorted(C)); a=C[0]; out=[]
    for b in C[1:]:
        rem=[x for x in C if x not in (a,b)]
        out.append(tuple(sorted((tuple(sorted((a,b))),tuple(sorted(rem))))))
    return tuple(sorted(set(out)))

def perm3_from_bijection(src,tgt,fn):
    P=np.zeros((3,3))
    for i,s in enumerate(src): P[tgt.index(fn(s)),i]=1
    return P

def induced(P): return q.T@P@q

def R0(F,e):
    F=tuple(sorted(F)); e=tuple(sorted(e)); u=next(iter(set(F)-set(e)))
    O=tuple(sorted(set(V)-set(F))); C=tuple(sorted(set(V)-set(e))); M=perfect_matchings(C)
    def f(m):
        for pair in m:
            if u in pair: return pair[0] if pair[1]==u else pair[1]
        raise RuntimeError
    return induced(perm3_from_bijection(M,O,f))

def local_P(F,e,chi):
    u=next(iter(set(F)-set(e))); O=tuple(sorted(set(V)-set(F)))
    d=np.array([chi[tuple(sorted((u,v)))] for v in O],float)
    G=q.T@np.diag(d)@q; det=float(np.linalg.det(G))
    if det<=0: raise ValueError
    return G/math.sqrt(det)

def Rchi(F,e,chi): return local_P(F,e,chi)@R0(F,e)

def build_C(chi):
    C=np.zeros((2*len(B3),2*len(B2)))
    for F,e in inc: C[2*idxF[F]:2*idxF[F]+2,2*idxE[e]:2*idxE[e]+2]=Rchi(F,e,chi)
    return C

def proj_resid(X,Y):
    x=np.asarray(X).ravel(); y=np.asarray(Y).ravel(); c=np.vdot(y,x)/np.vdot(y,y)
    return float(np.linalg.norm(x-c*y)/np.linalg.norm(x))

rng=np.random.default_rng(20260914)
F={}
for e in B2:
    B=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    X=B.conj().T@B+(0.3+0.04*(e[0]+e[1]))*np.eye(2)
    F[e]=(X+X.conj().T)/2
mindet=min(float(np.linalg.det(X).real) for X in F.values())
mineig=min(float(np.min(np.linalg.eigvalsh(X))) for X in F.values())

def chi_from_F(Fs,r=0.5): return {e:float(np.linalg.det(X).real**r) for e,X in Fs.items()}
chi=chi_from_F(F,0.5); C=build_C(chi)

A=np.array([[1.31+0.17j,0.22-0.11j],[-0.18+0.09j,0.91-0.07j]],complex)
Ai=np.linalg.inv(A); Fp={e:Ai.conj().T@X@Ai for e,X in F.items()}; chip=chi_from_F(Fp,0.5); Cp=build_C(chip)
expected_scale=1/abs(np.linalg.det(A)); ratio=np.array([chip[e]/chi[e] for e in B2])

B=np.array([[1.12+0.08j,0.19-0.13j],[-0.07+0.16j,0.94-0.03j]],complex); B=B/np.sqrt(np.linalg.det(B))
Bi=np.linalg.inv(B); Fs={e:Bi.conj().T@X@Bi for e,X in F.items()}; chi_sl2=chi_from_F(Fs,0.5); C_sl2=build_C(chi_sl2)

lam=5.7; Fl={e:lam*X for e,X in F.items()}; chil=chi_from_F(Fl,0.5); Cl=build_C(chil); scale_ratio=np.array([chil[e]/chi[e] for e in B2])
rs=[0.25,0.5,1.0,1.5]; chi_by_r={r:chi_from_F(F,r) for r in rs}; C_by_r={r:build_C(chi_by_r[r]) for r in rs}
pairwise={}
for i,r in enumerate(rs):
    for s in rs[i+1:]:
        pairwise[f'{r}_vs_{s}']={'chi_projective_residual':proj_resid([chi_by_r[r][e] for e in B2],[chi_by_r[s][e] for e in B2]),'C_projective_residual':proj_resid(C_by_r[r],C_by_r[s]),'max_local_R_projective_residual':max(proj_resid(Rchi(Fc,e,chi_by_r[r]),Rchi(Fc,e,chi_by_r[s])) for Fc,e in inc)}
degree_one={r:abs(lam**(2*r)-lam)/lam for r in rs}

pauli=[np.array([[1,0],[0,1]],complex),np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
def coords(X): return np.array([0.5*np.trace(P@X).real for P in pauli])
def induced4(S):
    L=np.zeros((4,4))
    for j,P in enumerate(pauli): L[:,j]=coords(S@P@S.conj().T)
    return L
def expm2(H):
    w,V=np.linalg.eig(H); return V@np.diag(np.exp(w))@np.linalg.inv(V)
Ss=[]; sig=pauli[1:]
for k in range(3): Ss += [expm2(0.37*sig[k]),expm2(0.41j*sig[k])]
M=[]
for S in Ss:
    S=S/np.sqrt(np.linalg.det(S)); M.append(induced4(S).T-np.eye(4))
M=np.vstack(M); sv=np.linalg.svd(M,compute_uv=False); rank=int(np.linalg.matrix_rank(M,tol=1e-10))

checks={'positive_F_chart':mindet>0 and mineig>0,'sqrt_det_GL2_common_relative_scale':float(np.std(ratio/expected_scale))<1e-12 and abs(float(np.mean(ratio))-expected_scale)<1e-12,'MRP4_exactly_blind_to_common_frame_scale':proj_resid(Cp,C)<1e-12,'sqrt_det_SL2_frame_invariant':max(abs(chi_sl2[e]-chi[e]) for e in B2)<1e-12 and proj_resid(C_sl2,C)<1e-12,'sqrt_det_degree_one_under_F_scaling':max(abs(scale_ratio-lam))<1e-12 and proj_resid(Cl,C)<1e-12,'only_r_half_among_tested_is_degree_one':degree_one[0.5]<1e-12 and all(degree_one[r]>1e-3 for r in rs if r!=0.5),'other_r_change_MRP4_transport':all(v['max_local_R_projective_residual']>1e-4 for k,v in pairwise.items() if '0.5' in k),'no_nonzero_SL2_invariant_linear_functional_witness':rank==4 and sv[-1]>1e-6}
out={'gate':'MRP4 response-system scalarization / Herm2 norm typing audit','assumption_for_constructive_part':'a physically distinguished positive-definite Herm2 pair response F_uv exists in the Q response system','candidate':'chi_uv=sqrt(det F_uv)','metrics':{'min_F_det':mindet,'min_F_eigenvalue':mineig,'GL2_expected_common_scale':expected_scale,'GL2_ratio_mean':float(np.mean(ratio)),'GL2_ratio_std':float(np.std(ratio)),'GL2_MRP4_C_projective_residual':proj_resid(Cp,C),'SL2_max_chi_abs_defect':float(max(abs(chi_sl2[e]-chi[e]) for e in B2)),'SL2_MRP4_C_projective_residual':proj_resid(C_sl2,C),'F_scale_ratio_mean':float(np.mean(scale_ratio)),'F_scale_ratio_std':float(np.std(scale_ratio)),'F_scale_MRP4_C_projective_residual':proj_resid(Cl,C),'degree_one_relative_errors':degree_one,'det_power_pairwise':pairwise,'SL2_linear_functional_constraint_rank':rank,'SL2_linear_functional_constraint_singular_values':sv.tolist()},'checks':{k:bool(v) for k,v in checks.items()},'pass_count':sum(bool(v) for v in checks.values()),'check_count':len(checks),'classification':{'sqrt_det_as_frame_covariant_degree1_positive_response_magnitude':'EXACT STRUCTURAL PASS (CONDITIONAL ON POSITIVE PHYSICAL F_uv)','bare_response_system_selects_pair_specific_F_uv':'NO / Q-B1015 BASIS-OBSERVABLE SELECTION GAP REMAINS','Q_current_derives_positive_pair_joint_F_uv_for_MRP4':'NOT ESTABLISHED','MRP4_final_physical_Q':'NOT PROMOTED'}}
Path('/mnt/data/tdg_mrp5/MRP4_RESPONSE_NORM_TYPING_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True,default=lambda o:o.item() if hasattr(o,'item') else str(o)))
print(json.dumps(out,indent=2,sort_keys=True,default=lambda o:o.item() if hasattr(o,'item') else str(o)))