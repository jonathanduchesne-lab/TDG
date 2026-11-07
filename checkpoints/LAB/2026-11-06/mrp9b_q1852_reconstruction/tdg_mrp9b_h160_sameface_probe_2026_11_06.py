#!/usr/bin/env python3
"""Exact historical Q-B1592 H160 same-face link probe (original model imports).

Not current Q-B1852 RefinedQ. Original chart formula reproduced from recovered
qb1592_semicausal_crossing_SL2_frame_connection_triplet.py.
"""
from __future__ import annotations
import sys, itertools, json, hashlib
from pathlib import Path
import numpy as np
from numpy.linalg import inv, norm, det, pinv, cond
ROOT = Path('/mnt/data/tdg_source_lab/qb1592/repro')
sys.path.insert(0,str(ROOT/'base'))
import qb1307_global_BSR_H160 as B
from tdg_qb1191_b2 import Z
from tdg_qb1001_base import A,Bcanon
I2 = np.eye(2, dtype=complex)

class SemiRecordModel(B.BSRModel):
    def build(self,a,up=None,bundle=True):
        H=super().build(a,up=up,bundle=bundle).copy()
        for pidx,eidx in self.inc32:
            ps=np.arange(self.ps(pidx).start,self.ps(pidx).stop)
            es=np.arange(self.es(eidx).start,self.es(eidx).stop)
            H[np.ix_(ps,es)]=0
        return H

def mid(x): return float(np.median(x)) if len(x) else 0.
def central_def(M):
    return float(norm(M-np.trace(M)/2*I2)/max(norm(M),1e-30))

def attachments(M,a):
    H=M.build(a,bundle=True)
    R=inv(Z*np.eye(M.dim)-H)
    d={};rowres=[];qconds=[];prec=[];dets=[]
    for T in M.B4:
        ci=np.arange(M.cs(M.i4[T]).start,M.cs(M.i4[T]).stop)
        Gc=R[np.ix_(ci,ci)]
        He=Z*np.eye(6)-inv(Gc)
        Rc=inv(Z*np.eye(6)-He)
        for F0 in itertools.combinations(T,3):
            F=tuple(sorted(F0))
            outside=next(iter(set(T)-set(F)))
            f=T.index(outside)
            C=A[f]@Bcanon[f]
            Lpre=C.conj().T@Rc
            p=M.i3[F]
            pp=np.arange(M.ps(p).start,M.ps(p).stop)
            G=R[np.ix_(pp,pp)]
            Lpost=inv(G)@R[np.ix_(pp,ci)]
            # Exactly the historical Q-B1592 chart, including its canonical pinv.
            Q=Lpost@pinv(Lpre)
            S=Q/np.sqrt(det(Q)+0j)
            rr=norm(Lpost-Q@Lpre)/max(norm(Lpost),1e-30)
            d[(T,F)]=S
            rowres.append(rr);qconds.append(cond(Q));prec.append(cond(Lpre));dets.append(abs(det(Q)))
    return d,dict(rowres_max=float(max(rowres)),rowres_median=mid(rowres),
                  qcond_max=float(max(qconds)),Lpre_cond_max=float(max(prec)),
                  determinant_min=float(min(dets)),determinant_max=float(max(dets)))

def analyze(M,a):
    ks,base=attachments(M,a)
    edge={};same=[];diff=[];lens=[]
    for T,U in itertools.combinations(M.B4,2):
        F=tuple(sorted(set(T)&set(U)))
        if len(F)!=3: continue
        edge[(T,U)] = (F, ks[(T,F)]@inv(ks[(U,F)]))
        lens.append(central_def(edge[(T,U)][1]))
    def link(T,U):
        if (T,U) in edge: return edge[(T,U)][1]
        return inv(edge[(U,T)][1])
    for T,U,V in itertools.combinations(M.B4,3):
        ftu=tuple(sorted(set(T)&set(U)))
        fuv=tuple(sorted(set(U)&set(V)))
        fvt=tuple(sorted(set(V)&set(T)))
        if min(len(ftu),len(fuv),len(fvt))!=3: continue
        P=link(T,U)@link(U,V)@link(V,T)
        (same if ftu==fuv==fvt else diff).append(central_def(P))
    result=dict(a=a,**base,attachments_count=len(ks),edges_count=len(edge),
                same_face_triangles=len(same),different_face_triangles=len(diff),
                same_face_loop_max=float(max(same)) if same else 0.,
                different_face_loop_max=float(max(diff)) if diff else 0.,
                different_face_loop_median=mid(diff),
                different_face_loop_min=float(min(diff)) if diff else 0.,
                links_central_median=mid(lens),links_central_max=float(max(lens)))
    return result

if __name__=='__main__':
    experiments=[]
    for name,model,cutoffs in [
       ('semicausal_q0.2',SemiRecordModel(B.boundary_s4(),q=.2),[.1,.05,.025,.0125,.00625]),
       ('persistent_q0.2',B.BSRModel(B.boundary_s4(),q=.2),[.05,.025,.0125]),
       ('semicausal_q0',SemiRecordModel(B.boundary_s4(),q=0),[.05,.025,.0125]),
    ]:
        for a in cutoffs:
            r=analyze(model,a);r['variant']=name;experiments.append(r)
            print(name, 'a',a,'rowres',r['rowres_max'],'links',r['links_central_median'], 'loops',r['different_face_loop_median'],'loops_max',r['different_face_loop_max'],'same_face_max',r['same_face_loop_max'],flush=True)
    out=dict(scope='Recovered historical Q-B1592 H160 source, not current qb1852 RefinedQ',
             source_archive='Complete_TDG_A_to_Z_QB1592_Handoff_2026-08-15.tar.gz',
             records=experiments)
    fp=Path('/mnt/data/tdg_source_lab/mrp9b_historical_sameface_results.json')
    fp.write_text(json.dumps(out,indent=2)+'\n')
    print('RESULTS',fp)
