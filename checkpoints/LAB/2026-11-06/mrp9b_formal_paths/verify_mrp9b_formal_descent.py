#!/usr/bin/env python3
"""MRP9B: formal moment descent audit on the certified qb1852 RefinedQ source.

This is a *diagnostic*, not a derivation of selected-future physical transport.
Each P_T, P_F projects the exact Q to its documented parent and bright port.
Exact resolvent moments are obtained by repeated sparse H multiplication;
no spectral readout, optimized scalar, graph target or continuum fit enters
in the formal obstruction. The candidate chart typing remains conditional.
"""
import sys, os, hashlib, json, contextlib, io, math, time
from pathlib import Path
import numpy as np
from numpy.linalg import norm, pinv, svd, inv

SRC = Path(os.environ.get('TDG_Q1852_SOURCE', '/mnt/data/tdg_source_lab/qb1852_extracted/qb1852_full_refined.py'))
sys.path.insert(0, str(SRC.parent))
with contextlib.redirect_stdout(io.StringIO()):
    import qb1852_full_refined as q
I2 = np.eye(2,dtype=complex)


def selector(model, label):
    if len(label)==4:
        B=np.zeros((model.dim,6),complex)
        B[model.pcs(label),:]=np.eye(6)
        return B
    F=label
    B=np.zeros((model.dim,2),complex)
    for f in model.groupF[F]:
        B[model.ps(f),:]+=I2/math.sqrt(len(model.groupF[F]))
    return B


def calc(model, cell, face, order=8, z=None):
    assert len(set(face))==3 and set(face).issubset(set(cell))
    P=selector(model,cell)
    F=selector(model,face)
    idx=cell.index(next(iter(set(cell)-set(face))))
    C=q.A[idx]@q.Bcanon[idx]
    Cd=C.conj().T
    Pinv=pinv(Cd)
    Pnull=np.eye(6)-Pinv@Cd
    H=model.build_H()
    V=P.copy()
    W=F.copy()
    TT=[];FT=[];FF=[]
    for k in range(order+1):
        TT.append(P.conj().T@V)
        FT.append(F.conj().T@V)
        FF.append(F.conj().T@W)
        if k<order:
            V=H@V
            W=H@W
    # Coefficients: R=(1/z) sum_k (1/z)^k H^k.
    # Lpre = Cdag R_TT = sum_{n>=1} t^n Cdag TT[n-1].
    # Lpost = R_FF^-1 R_FT = (sum FF[k] t^k)^-1 (sum FT[k] t^k).
    # Note FT[0]=0, FF[0]=I.
    Lpre=[np.zeros((2,6),complex)]+[Cd@TT[k-1] for k in range(1,order+1)]
    Lpost=[np.zeros((2,6),complex) for _ in range(order+1)]
    for n in range(1,order+1):
        Lpost[n]=FT[n].copy()
        for k in range(1,n+1):
            Lpost[n]-=FF[k]@Lpost[n-k]
    leading=Lpost[1]
    scale=model.ac
    c_error=norm(leading-scale*Cd)/max(norm(leading),1e-30)
    # At each order n solve for K_{n-1} such that Lpost=K(t)*Lpre.
    # If residual on the nullspace is nonzero, exact factorization is impossible.
    K=[];rows=[]
    for n in range(1,order+1):
        rhs=Lpost[n].copy()
        for j in range(n-1):
            rhs-=K[j]@Lpre[n-j]
        Knew=rhs@Pinv
        residual=rhs-Knew@Cd
        nrm=float(norm(residual))
        r0=float(norm(rhs))
        rows.append(dict(n=n,abs_defect=nrm,relative_rhs_defect=nrm/max(r0,1e-30),
                         rank_null= int(np.linalg.matrix_rank(rhs@Pnull,tol=max(1e-12,norm(rhs)*1e-8))),
                         norm_K_coefficient=float(norm(Knew)),
                         null_defect_ratio=float(norm(rhs@Pnull)/max(norm(rhs),1e-30))))
        K.append(Knew)
    # Compare with full Q(z) and null-map singular values, basis-free.
    z=z if z is not None else model.z
    U=np.column_stack([P,F]); X=model.LU.solve(U)
    Rtt=P.conj().T@X[:,:6];Rft=F.conj().T@X[:,:6];Rff=F.conj().T@X[:,6:]
    Lp=Cd@Rtt
    Lq=inv(Rff)@Rft
    null_exact=np.eye(6)-pinv(Lp)@Lp
    singular=svd(Lq@null_exact,compute_uv=False)
    row_res=norm(Lq@null_exact)/max(norm(Lq),1e-30)
    # The null map is rank2 iff *every* 2x2 K can be changed by a right-inverse choice.
    rank_lqnull=int(np.linalg.matrix_rank(Lq@null_exact,tol=max(singular[0]*1e-8,1e-14)))
    # Analytical upper bound for a generic right inverse Y+Pker W.
    # A fixed Q-independent W=unit reference can change K by the Q-null map.
    zmeta={"z":str(z),"row_space_descent_defect":float(row_res),
        "null_response_singular_values":[float(x) for x in singular],
        "null_response_rank":rank_lqnull,
        "null_map_frobenius":float(norm(Lq@null_exact)),
        "post_response_frobenius":float(norm(Lq)),
        "core_input_frobenius":float(norm(Lp))}
    return dict(cell=list(cell),face=list(face),scheme=model.scheme,cutoff=float(model.ac),source_q_hash=hashlib.sha256(SRC.read_bytes()).hexdigest(),
                operator_dim=int(model.dim),parents=int(len(model.parents)),
                moments_order=int(order),leading_scalar_relative_error=float(c_error),
                leading_scalar=float(scale),
                first_nonzero_abs_order=next((int(x['n']) for x in rows if x['abs_defect']>1e-10),None),
                formal_obstruction=rows,
                finite_readout=zmeta)


def run():
    cells=[((0,1,2,3),(0,1,2)),((0,1,2,4),(0,1,2)),((0,1,2,3),(0,1,3))]
    out=[]
    for a in [0.05,0.025,0.0125]:
        with contextlib.redirect_stdout(io.StringIO()):
            model=q.RefinedQ('b4',a,2+0.7j,need_edges=False)
        for c,f in cells:
            t=time.time()
            ret=calc(model,c,f,order=8)
            ret['compute_seconds']=round(time.time()-t,2)
            out.append(ret)
            nn=ret['finite_readout']['null_response_singular_values']
            print('a',a,'cell',c,'face',f,'first_not_zero',ret['first_nonzero_abs_order'],
                  'moment_res_2_to_5',[round(x['abs_defect'],11) for x in ret['formal_obstruction'][1:5]],
                  'null_rank',ret['finite_readout']['null_response_rank'],
                  'row_res',round(ret['finite_readout']['row_space_descent_defect'],9),
                  'null_sing',nn,'dt',ret['compute_seconds'],flush=True)
    result={'scope':'Q-B1852 *actual H* moments; Q-B1592 chart *conditional transplant*; no GR claim',
            'source_original_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
            'results':out}
    target=(Path(__file__).resolve().parent / 'formal_descent_results.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print('SAVED',target,flush=True)
if __name__=='__main__':run()
