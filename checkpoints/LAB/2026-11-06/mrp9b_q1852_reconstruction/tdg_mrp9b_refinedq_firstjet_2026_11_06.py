#!/usr/bin/env python3
"""Exact low-rank Q-B1852 marked core-source response of candidate same-face charts.

The full RefinedQ Hamiltonian/Schur resolvent is untouched. This is a probe
of a Q-B1592-style chart transplant, not an established selected-future map.
"""
import sys,io,contextlib,json,hashlib
from pathlib import Path
import numpy as np
from numpy.linalg import inv,norm,det,pinv,svd
BASE=Path('/mnt/data/tdg_source_lab/qb1852_extracted')
sys.path.insert(0,str(BASE))
with contextlib.redirect_stdout(io.StringIO()):import qb1852_full_refined as q
I2=np.eye(2,dtype=complex)
T=(0,1,2,3);U=(0,1,2,4);V=(0,1,3,4)
Ft=tuple(sorted(set(T)&set(U)))
Fu=tuple(sorted(set(U)&set(V)))
Fv=tuple(sorted(set(V)&set(T)))
CELLS=[T,U,V]; FACES=[Ft,Fu,Fv]

def central(M):return float(norm(M-np.trace(M)/2*I2)/max(norm(M),1e-30))

def one(a,eps=1e-4,z=2+.7j,check_woodbury=False):
    with contextlib.redirect_stdout(io.StringIO()):model=q.RefinedQ('b4',a,z,need_edges=False)
    def basis(lab):
        if len(lab)==4:
            B=np.zeros((model.dim,6),complex);B[model.pcs(lab),:]=np.eye(6);return B
        F=lab;B=np.zeros((model.dim,2),complex)
        for ff in model.groupF[F]:B[model.ps(ff),:]+=I2/np.sqrt(len(model.groupF[F]))
        return B
    B={k:basis(k) for k in [*CELLS,*FACES]}
    joins=[T,U,V,Ft,Fu,Fv]
    Bs=np.column_stack([B[k] for k in joins]); X=model.LU.solve(Bs)
    cols={};j=0
    for k in joins:
        w=B[k].shape[1];cols[k]=X[:,j:j+w];j+=w
    def R(X,Y):return B[X].T@cols[Y]
    SS=R(T,T)
    def updated(X,Y,src):
        if src is None:return R(X,Y)
        coeff,Ov=src
        W=coeff*Ov@inv(np.eye(6)-coeff*SS@Ov)
        return R(X,Y)+R(X,T)@W@R(T,Y)
    def chart(c,f,src=None):
        idx=c.index(next(iter(set(c)-set(f))))
        C=q.A[idx]@q.Bcanon[idx]
        Lpre=C.conj().T@updated(c,c,src)
        Lpost=inv(updated(f,f,src))@updated(f,c,src)
        Q=Lpost@pinv(Lpre)
        S=Q/np.sqrt(det(Q)+0j)
        return S,float(norm(Lpost-Q@Lpre)/norm(Lpost))
    def loop(src=None):
        ab=chart(T,Ft,src)[0]@inv(chart(U,Ft,src)[0])
        bc=chart(U,Fu,src)[0]@inv(chart(V,Fu,src)[0])
        ca=chart(V,Fv,src)[0]@inv(chart(T,Fv,src)[0])
        return ab@bc@ca
    P0=loop()
    entries=[];jet_cols=[]
    for b in range(4):
        Ov=q.O[b]
        pp=loop((eps,Ov));pm=loop((-eps,Ov));Dp=(pp-pm)/(2*eps)
        dtr=Dp-np.trace(Dp)/2*I2
        S0,_=chart(T,Ft)
        Sp,_=chart(T,Ft,(eps,Ov));Sm,_=chart(T,Ft,(-eps,Ov))
        DS=(Sp-Sm)/(2*eps)
        Xj=inv(S0)@DS;Xj-=np.trace(Xj)/2*I2
        zz=np.array([np.trace(q.sig[k]@Xj)/2 for k in range(3)])
        jet_cols.append(np.r_[zz.real,zz.imag])
        entries.append(dict(slot=b,loop_response_traceless_norm=float(norm(dtr)),local_chart_tangent_norm=float(norm(zz))))
    J=np.column_stack(jet_cols);P3=np.eye(4)-np.ones((4,4))/4;sv=svd(J@P3,compute_uv=False)
    rr=[chart(c,f)[1] for c,f in [(T,Ft),(U,Ft),(U,Fu),(V,Fu),(V,Fv),(T,Fv)]]
    result=dict(a=a,dim=model.dim,loop_centrality=central(P0),loop_over_a2=central(P0)/a**2,baseline_rowres_max=float(max(rr)),
                marked_source_entries=entries,median_loop_firstjet_norm=float(np.median([x['loop_response_traceless_norm'] for x in entries])),
                firstjet_singular_values=[float(x) for x in sv],singlet_tangent_norm=float(norm(J@np.ones(4)/4)),
                imag_rotation_fraction=float(norm(J[3:])/max(norm(J),1e-30)))
    if check_woodbury:
        from scipy.sparse.linalg import splu
        H=model.build_H();Bsource=B[T]
        Vfull=Bsource@(eps*q.O[0])@Bsource.T
        H2=H+__import__('scipy').sparse.csc_matrix(Vfull)
        LU2=splu((z*__import__('scipy').sparse.eye(model.dim,format='csc')-H2).tocsc())
        X2=LU2.solve(Bs);j=0;cols2={}
        for k in joins:
            w=B[k].shape[1];cols2[k]=X2[:,j:j+w];j+=w
        err=[]
        for p in joins:
            for s in joins:
                full=B[p].T@cols2[s]
                calc=updated(p,s,(eps,q.O[0]))
                err.append(norm(full-calc)/max(norm(full),1e-30))
        result['woodbury_sparse_direct_max_rel_error']=float(max(err))
    return result

if __name__=='__main__':
    ret=[]
    for a in [.05,.025,.0125]:
        r=one(a,check_woodbury=(a==.05));ret.append(r)
        print('a',a,'loop',r['loop_centrality'],'firstjet',r['median_loop_firstjet_norm'],'rowres',r['baseline_rowres_max'],
              'sv',r['firstjet_singular_values'],'wb',r.get('woodbury_sparse_direct_max_rel_error'),flush=True)
    f=Path('/mnt/data/tdg_source_lab/mrp9b_refinedq_firstjet_results.json')
    f.write_text(json.dumps({'scope':'Q-B1852 exact Q source, source-marked physical perturbations; conditional Q-B1592 chart transplant', 'source_sha256':hashlib.sha256((BASE/'qb1852_full_refined.py').read_bytes()).hexdigest(), 'records':ret},indent=2)+'\n')
    print('RESULTS',f)
