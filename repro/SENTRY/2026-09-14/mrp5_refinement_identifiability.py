import itertools, math, json
from pathlib import Path
import numpy as np

V=tuple(range(6))
B2=list(itertools.combinations(V,2)); B3=list(itertools.combinations(V,3))
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
    for i,s in enumerate(src):
        t=fn(s); P[tgt.index(t),i]=1
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
    G=q.T@np.diag(d)@q; det=np.linalg.det(G)
    if det<=0: raise ValueError('nonpositive MRP4 chart')
    return G/math.sqrt(det)

def Rchi(F,e,chi): return local_P(F,e,chi)@R0(F,e)

def build_C(chi):
    C=np.zeros((2*len(B3),2*len(B2)))
    for F,e in inc: C[2*idxF[F]:2*idxF[F]+2,2*idxE[e]:2*idxE[e]+2]=Rchi(F,e,chi)
    return C

def proj_resid_vec(x,y):
    x=np.asarray(x,float).reshape(-1); y=np.asarray(y,float).reshape(-1)
    c=np.dot(y,x)/max(np.dot(y,y),1e-300)
    return float(np.linalg.norm(x-c*y)/max(np.linalg.norm(x),1e-300))

def proj_resid_mat(X,Y): return proj_resid_vec(np.asarray(X).ravel(),np.asarray(Y).ravel())

fine=[(i,a,b) for i in V for a in range(2) for b in range(2)]
rng=np.random.default_rng(20260914)
fine_chi={}
for x,y in itertools.combinations(fine,2):
    if x[0]==y[0]: continue
    z=0.23*rng.normal()+0.035*(x[0]+1)*(y[0]+2)+0.07*(x[1]-y[1])+0.04*(x[2]+y[2])
    fine_chi[tuple(sorted((x,y)))]=float(np.exp(z))

def pushforward(child_values,child_nodes,parent_of,p):
    parents=sorted(set(parent_of(x) for x in child_nodes),key=repr); out={}
    for A,B in itertools.combinations(parents,2):
        vals=[]; target=tuple(sorted((A,B),key=repr))
        for x,y in itertools.combinations(child_nodes,2):
            if parent_of(x)==parent_of(y): continue
            if tuple(sorted((parent_of(x),parent_of(y)),key=repr))!=target: continue
            k=tuple(sorted((x,y),key=repr))
            if k in child_values: vals.append(child_values[k])
        if vals:
            vals=np.array(vals,float); out[target]=float(np.sum(vals**p)**(1.0/p))
    return out,parents

def pf_fine_mid(p): return pushforward(fine_chi,fine,lambda x:(x[0],x[1]),p)
def pf_mid_coarse(mid_chi,mid_nodes,p): return pushforward(mid_chi,mid_nodes,lambda x:x[0],p)
def pf_fine_coarse(p): return pushforward(fine_chi,fine,lambda x:x[0],p)

ps=[1.0,2.0,3.0]; rows={}; coarse_chis={}
for p in ps:
    m,midnodes=pf_fine_mid(p); c2,_=pf_mid_coarse(m,midnodes,p); c1,_=pf_fine_coarse(p)
    keys=sorted(c1,key=repr); diamond=max(abs(c1[k]-c2[k]) for k in keys); rel=diamond/max(max(c1.values()),1e-30)
    cc={tuple(sorted(k)):v for k,v in c1.items()}; coarse_chis[p]=cc; C=build_C(cc)
    C0=build_C({e:1.0 for e in B2}); _,_,Vh=np.linalg.svd(C0,full_matrices=True); K=Vh.T[:,-5:]; CK=C@K; sv=np.linalg.svd(CK,compute_uv=False)
    rows[p]={'diamond_abs':float(diamond),'diamond_rel':float(rel),'coarse_min':float(min(cc.values())),'coarse_max':float(max(cc.values())),'C_rank':int(np.linalg.matrix_rank(C,tol=1e-10)),'kernel_origin_image_rank':int(np.linalg.matrix_rank(CK,tol=1e-10)),'kernel_origin_image_sv_min':float(min(sv)),'kernel_origin_image_sv_max':float(max(sv))}

scale=7.3; scalar_cov={}
for p in ps:
    scaled={k:scale*v for k,v in fine_chi.items()}; cscaled,_=pushforward(scaled,fine,lambda x:x[0],p); base,_=pf_fine_coarse(p)
    scalar_cov[p]=float(max(abs(cscaled[k]-scale*base[k]) for k in base)/max(cscaled.values()))

ts=np.array([0.7,1.1,1.8]); spectator={}
for p in ps:
    factor=float(np.sum(ts**p)**(1/p)); base,_=pf_fine_coarse(p); spec={k:factor*v for k,v in base.items()}; keys=sorted(base,key=repr)
    spectator[p]={'factor':factor,'projective_residual':proj_resid_vec([spec[k] for k in keys],[base[k] for k in keys])}

perm={0:4,1:2,2:5,3:0,4:3,5:1}; perm_micro=lambda x:(perm[x[0]],x[1],x[2]); fine_perm=[perm_micro(x) for x in fine]
fine_chi_perm={tuple(sorted((perm_micro(x),perm_micro(y)))):v for (x,y),v in fine_chi.items()}; relabel={}
for p in ps:
    cp,_=pushforward(fine_chi_perm,fine_perm,lambda x:x[0],p); c,_=pf_fine_coarse(p); expected={tuple(sorted((perm[a],perm[b]))):v for (a,b),v in c.items()}
    relabel[p]=float(max(abs(cp[k]-expected[k]) for k in expected)/max(expected.values()))

represent=(0,1); vals=[v for (x,y),v in fine_chi.items() if tuple(sorted((x[0],y[0])))==represent]; additive_target=float(sum(vals))
direct_sum_error={p:abs((sum(np.array(vals)**p))**(1/p)-additive_target)/additive_target for p in ps}
pairwise={}
for i,p in enumerate(ps):
    for qv in ps[i+1:]:
        kp=sorted(B2); chip=[coarse_chis[p][k] for k in kp]; chiq=[coarse_chis[qv][k] for k in kp]; Cp=build_C(coarse_chis[p]); Cq=build_C(coarse_chis[qv])
        pairwise[f'{p}_vs_{qv}']={'chi_projective_residual':proj_resid_vec(chip,chiq),'C_common_scalar_projective_residual':proj_resid_mat(Cp,Cq),'max_local_R_projective_residual':float(max(proj_resid_mat(Rchi(F,e,coarse_chis[p]),Rchi(F,e,coarse_chis[qv])) for F,e in inc))}

checks={'p_family_diamond_functoriality':all(rows[p]['diamond_rel']<1e-12 for p in ps),'p_family_positive':all(rows[p]['coarse_min']>0 for p in ps),'p_family_scalar_covariant':all(scalar_cov[p]<1e-12 for p in ps),'p_family_spectator_projectively_blind':all(spectator[p]['projective_residual']<1e-12 for p in ps),'p_family_relabel_covariant':all(relabel[p]<1e-12 for p in ps),'p_family_preserves_five_kernel_origin_modes_generically':all(rows[p]['kernel_origin_image_rank']==5 and rows[p]['kernel_origin_image_sv_min']>1e-10 for p in ps),'different_p_give_distinct_MRP4_transport':all(v['max_local_R_projective_residual']>1e-4 for v in pairwise.values()),'ordinary_additive_direct_sum_selects_p1':direct_sum_error[1.0]<1e-14 and direct_sum_error[2.0]>1e-3 and direct_sum_error[3.0]>1e-3}
result={'gate':'MRP5 modern Stage-I refinement-law identifiability audit','family':'chi_parent(A,B)=(sum chi_ab^p)^(1/p), p>0','p_tested':ps,'rows':rows,'scalar_covariance':scalar_cov,'spectator':spectator,'relabel':relabel,'direct_sum_relative_error_vs_linear_additivity':direct_sum_error,'pairwise_physical_difference':pairwise,'checks':checks,'pass_count':sum(bool(v) for v in checks.values()),'check_count':len(checks),'classification':{'MRP4_typing_alone_selects_unique_refinement_functor':'FAIL','positive_homogeneous_relabel_spectator_diamond_axioms_unique':'NO / CONTINUUM p-FAMILY','linear_CP_direct_sum_additivity_would_select_p1':'YES, BUT EXTRA PHYSICAL TYPING AXIOM FOR chi','MRP5_as_originally_requested':'NOT CLOSED / G1-G3 UNDERDETERMINED','MRP4_final_physical_Q':'NOT ADOPTED','GR':'CLOSED'}}
Path('MRP5_REFINEMENT_IDENTIFIABILITY_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True,default=lambda o:bool(o) if isinstance(o,np.bool_) else str(o))+'\n')
print(json.dumps(result,indent=2,sort_keys=True,default=lambda o:bool(o) if isinstance(o,np.bool_) else str(o)))
