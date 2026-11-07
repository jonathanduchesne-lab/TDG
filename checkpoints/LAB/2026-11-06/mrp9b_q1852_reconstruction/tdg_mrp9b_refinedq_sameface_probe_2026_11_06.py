#!/usr/bin/env python3
"""MRP9B fresh two-cell same-face *candidate* on the exact Q-B1852 RefinedQ.

Source current Q is byte-exact qb1852_full_refined.py (SHA-256 pin in report).
The MRP9B attachment is an explicit transplant of the recovered Q-B1592
resolvent chart; its validity as selected-future process chart is NOT proven.
"""
import os,sys,itertools,contextlib,io,json,math,hashlib
from pathlib import Path
import numpy as np
from numpy.linalg import inv,norm,det,pinv,cond
SRC=Path('/mnt/data/tdg_source_lab/qb1852_extracted')
sys.path.insert(0,str(SRC))
with contextlib.redirect_stdout(io.StringIO()):
 import qb1852_full_refined as q0
I2=np.eye(2,dtype=complex)

def centraldef(M):return float(norm(M-np.trace(M)/2*I2)/max(norm(M),1e-30))
def med(a):return float(np.median(a)) if len(a) else 0.
def choose_cells():
    P=q0.coarse_universe(); T=q0.T0
    neigh=[U for U in P if len(set(U)&set(T))==3]
    return [T]+neigh

def make_data(a,z=2+.7j,cell_subset=None):
    with contextlib.redirect_stdout(io.StringIO()):model=q0.RefinedQ('b4',a,z,need_edges=False)
    cs=cell_subset or choose_cells()
    faces=sorted({tuple(sorted(F)) for T in cs for F in itertools.combinations(T,3)})
    # exact full-Q projected parent-core resolvent blocks G_TT
    Gc={}
    for start in range(0,len(cs),10):
        cells=cs[start:start+10];B=np.zeros((model.dim,6*len(cells)),complex)
        for j,T in enumerate(cells):B[model.pcs(T),6*j:6*j+6]=np.eye(6)
        X=model.LU.solve(B)
        for j,T in enumerate(cells):Gc[T]=X[model.pcs(T),6*j:6*j+6]
    # exact full-Q groupF bright-port resolvent blocks G_FF
    Gf={}
    for start in range(0,len(faces),12):
        chunk=faces[start:start+12];B=np.zeros((model.dim,2*len(chunk)),complex)
        for j,F in enumerate(chunk):
            for ff in model.groupF[F]:B[model.ps(ff),2*j:2*j+2]+=I2/math.sqrt(len(model.groupF[F]))
        X=model.LU.solve(B)
        Gfull=B.T@X
        for j,F in enumerate(chunk):Gf[F]=Gfull[2*j:2*j+2,2*j:2*j+2]
    S={};S_alt={};rowres=[];scores=[];gcond=[];determinants=[];err_u=[];alt_relative=[]
    for T in cs:
        G=Gc[T]
        for F0 in itertools.combinations(T,3):
            F=tuple(sorted(F0));outside=next(iter(set(T)-set(F)));f=T.index(outside)
            # Original Q-B1592 A[f] Bcanon[f], no new 2D compression.
            C=q0.A[f]@q0.Bcanon[f]
            Lpre=C.conj().T@G
            # U is EXACT full-Q parent-to-bright-face block q0.RefinedQ._parent_blocks()
            U=model.U[(T,F)]
            Lpost=inv(Gf[F])@U
            Y=pinv(Lpre)
            K=Lpost@Y
            if abs(det(K))<1e-25:raise ArithmeticError('noninvertible '+str((T,F,a,det(K))))
            S[(T,F)]=K/np.sqrt(det(K)+0j)
            # Mathematically valid but NOT Q-licensed alternative right inverse.
            # Its size is comparable to the norm of canonical Moore-Penrose.
            UU,SS,VV=np.linalg.svd(Lpre,full_matrices=True)
            N=VV[2:].conj().T  # ker(Lpre), 6x4
            seed=int.from_bytes(hashlib.sha256(repr((T,F)).encode()).digest()[:8],'little')
            gen=np.random.default_rng(seed)
            W=(gen.standard_normal((4,2))+1j*gen.standard_normal((4,2)))
            W=W/norm(W)
            Yalt=Y+norm(Y)*(N@W)
            if norm(Lpre@Yalt-I2)>1e-10:raise AssertionError('bad right inverse')
            Kalt=Lpost@Yalt
            S_alt[(T,F)]=Kalt/np.sqrt(det(Kalt)+0j)
            alt_relative.append(norm(Kalt-K)/max(norm(K),1e-30))
            rowres.append(norm(Lpost-K@Lpre)/max(norm(Lpost),1e-30))
            scores.append(cond(K));gcond.append(cond(Gf[F]));determinants.append(abs(det(K)))
            # Cross-check direct full-Q bright-port projection against U from source.
            # U is not recomputed here, so this check is only a consistency marker.
    E={};edge_norm=[];same=[];cross=[];loopstats=[]
    for T,U in itertools.combinations(cs,2):
        F=tuple(sorted(set(T)&set(U)))
        if len(F)==3:
            E[(T,U)]=(F,S[(T,F)]@inv(S[(U,F)]))
            edge_norm.append(centraldef(E[(T,U)][1]))
    def link(T,U):
        if (T,U) in E:return E[(T,U)][1]
        if (U,T) in E:return inv(E[(U,T)][1])
        raise ValueError('not neighbors')
    for T,U,V in itertools.combinations(cs,3):
        ftu=tuple(sorted(set(T)&set(U)));fuv=tuple(sorted(set(U)&set(V)));fvt=tuple(sorted(set(V)&set(T)))
        if min(len(ftu),len(fuv),len(fvt))!=3: continue
        P=link(T,U)@link(U,V)@link(V,T)
        (same if ftu==fuv==fvt else cross).append(centraldef(P))
        if not (ftu==fuv==fvt):
            loopstats.append((centraldef(P),[list(T),list(U),list(V)],[list(ftu),list(fuv),list(fvt)]))
    mx=max(loopstats,key=lambda x:x[0]) if loopstats else None
    def alt_link(T,U):
        F=tuple(sorted(set(T)&set(U)))
        return S_alt[(T,F)]@inv(S_alt[(U,F)])
    alt_links=[];alt_loops=[]
    for T,U in itertools.combinations(cs,2):
        if len(set(T)&set(U))==3:alt_links.append(centraldef(alt_link(T,U)))
    for T,U,V in itertools.combinations(cs,3):
        ftu=set(T)&set(U);fuv=set(U)&set(V);fvt=set(V)&set(T)
        if min(len(ftu),len(fuv),len(fvt))!=3 or ftu==fuv==fvt:continue
        alt_loops.append(centraldef(alt_link(T,U)@alt_link(U,V)@alt_link(V,T)))
    return dict(scheme='b4',ac=a,z=str(z),dim=model.dim,parents=len(model.parents),b4cells=len(model.FB4),sample_cells=len(cs),sample_faces=len(faces),
                attachments=len(S),shared_edges=len(E),same_face_triangles=len(same),mixed_face_triangles=len(cross),
                same_face_loop_max=max(same) if same else 0.,mixed_face_loop_median=med(cross),mixed_face_loop_max=max(cross) if cross else 0.,
                mixed_face_loop_over_a2=med(cross)/(a*a),mixed_face_loop_over_a4=med(cross)/(a**4),
                max_loop_cells=mx[1] if mx else None,max_loop_faces=mx[2] if mx else None,
                link_median=med(edge_norm),link_max=max(edge_norm) if edge_norm else 0.,rowres_max=max(rowres),rowres_median=med(rowres),
                max_K_condition=max(scores),max_Gf_condition=max(gcond),K_det_min=min(determinants),K_det_max=max(determinants),
                alternative_right_inverse_relative_median=med(alt_relative),
                alternative_right_inverse_link_median=med(alt_links),
                alternative_right_inverse_mixed_loop_median=med(alt_loops),
                alternative_versus_canonical_loop_ratio=med(alt_loops)/max(med(cross),1e-30))

if __name__=='__main__':
    aa=[float(x) for x in sys.argv[1:]] or [.05,.025]
    results=[]
    for a in aa:
        r=make_data(a);results.append(r)
        print('a',a,'dim',r['dim'],'links',r['link_median'],'loops',r['mixed_face_loop_median'],'row_res',r['rowres_max'],'over/a2',r['mixed_face_loop_over_a2'],'sameface_max',r['same_face_loop_max'], 'alt_loop',r['alternative_right_inverse_mixed_loop_median'],flush=True)
    out={'scope':'Certified Q-B1852 full RefinedQ H; candidate Q-B1592 chart transplant, not certified selected-future chart',
         'source_sha256':hashlib.sha256((SRC/'qb1852_full_refined.py').read_bytes()).hexdigest(),
         'results':results}
    f=Path('/mnt/data/tdg_source_lab/mrp9b_refinedq_sameface_results.json')
    f.write_text(json.dumps(out,indent=2)+'\n');print('RESULTS',f)
