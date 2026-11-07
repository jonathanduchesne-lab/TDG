#!/usr/bin/env python3
"""Counterfactual process type: B2 writes persist, B2->B3 return blocked.

Global hermitian Q is untouched. The *counterfactual* triangular operator is
an exploratory reduced-process comparator, not proven CP/unitary or licensed
as TDG's factual update. It isolates the B2-return contribution exactly.
"""
import sys,json,hashlib,time
from pathlib import Path
import numpy as np
from numpy.linalg import norm,pinv,inv,svd
from scipy.sparse import eye as speye
from scipy.sparse.linalg import splu
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_mrp9b_b4_b24_moment_source import construct
from verify_mrp9b_formal_descent import selector,q,SRC

def formal_on_H(m,H,c,f,order=7):
    P=selector(m,c);F=selector(m,f)
    i=c.index(next(iter(set(c)-set(f))))
    Cd=(q.A[i]@q.Bcanon[i]).conj().T
    Cplus=pinv(Cd)
    W=P.copy();V=F.copy();TT=[];FT=[];FF=[]
    for k in range(order+1):
        TT.append(P.conj().T@W);FT.append(F.conj().T@W);FF.append(F.conj().T@V)
        if k<order:W=H@W;V=H@V
    pre=[np.zeros((2,6),complex)]+[Cd@TT[k] for k in range(order)]
    post=[np.zeros((2,6),complex) for _ in range(order+1)]
    for n in range(1,order+1):
        post[n]=FT[n].copy()
        for j in range(1,n+1):post[n]-=FF[j]@post[n-j]
    K=[];res=[]
    for n in range(1,order+1):
        rhs=post[n].copy()
        for j in range(n-1):rhs-=K[j]@pre[n-j]
        k=rhs@Cplus
        res.append(float(norm(rhs-k@Cd)))
        K.append(k)
    return res

def finite_on_H(m,H,c,f,z=2+.7j):
    P=selector(m,c);F=selector(m,f)
    i=c.index(next(iter(set(c)-set(f))))
    Cd=(q.A[i]@q.Bcanon[i]).conj().T
    LU=splu((z*speye(m.dim,format='csc')-H).tocsc())
    U=np.column_stack((P,F));X=LU.solve(U)
    Gtt=P.conj().T@X[:,:6]
    Gft=F.conj().T@X[:,:6]
    Gff=F.conj().T@X[:,6:]
    Lpre=Cd@Gtt
    Lpost=inv(Gff)@Gft
    Pker=np.eye(6)-pinv(Lpre)@Lpre
    return float(norm(Lpost@Pker)/max(norm(Lpost),1e-30))

def run():
    rs=[]
    c=(0,1,2,3);f=(0,1,2)
    for a in [.05,.025,.0125]:
        m=construct('b4',a,1.);H=m.build_H()
        b3=slice(m.N4,m.N4+m.N3)
        b2=slice(m.N4+m.N3,m.N4+m.N3+m.N2)
        Hs=H.tolil()
        write=float(norm(H[b2,b3].data)) if False else float(np.sqrt(np.sum(np.abs(H[b2,b3].data)**2)))
        Hr=H[b3,b2]
        returned=float(np.sqrt(np.sum(np.abs(Hr.data)**2)))
        Hs[b3,b2]=0
        Hs=Hs.tocsc()
        delta=H-Hs
        nonherm=float(np.sqrt(np.sum(np.abs((Hs-Hs.getH()).data)**2)))
        m0=construct('b4',a,0.);H0=m0.build_H()
        herm_formal=formal_on_H(m,H,c,f)
        directed_formal=formal_on_H(m,Hs,c,f)
        zero_formal=formal_on_H(m0,H0,c,f)
        original_finite=finite_on_H(m,H,c,f)
        directed_finite=finite_on_H(m,Hs,c,f)
        zero_finite=finite_on_H(m0,H0,c,f)
        record=dict(a=a,full_gamma_1=herm_formal,fresh_sink=directed_formal,full_gamma_0=zero_formal,
                    initial_record_write_norm=write,initial_record_return_norm=returned,
                    fresh_record_write_norm=write,fresh_record_return_norm=0.0,
                    nonhermiticity_norm=nonherm,
                    removal_matrix_norm=float(np.sqrt(np.sum(np.abs(delta.data)**2))),
                    max_formal_difference_directed_v_no_b2=float(max(abs(x-y) for x,y in zip(directed_formal,zero_formal))),
                    finite_readout_row_defect_full=original_finite,
                    finite_readout_row_defect_sink=directed_finite,
                    finite_readout_row_defect_b2_off=zero_finite)
        rs.append(record)
        print('a',a,'return coupling',returned,'write',write,'nonhermitian',nonherm,
              'D3 full/sink',herm_formal[2],directed_formal[2],
              'D5 full/sink',herm_formal[4],directed_formal[4],
              'rowdefect full/sink/off',original_finite,directed_finite,zero_finite,flush=True)
    dest=(Path(__file__).resolve().parent / 'fresh_sink_results.json')
    dest.write_text(json.dumps({'disclaimer':'Exploratory directed effective operator, not certified CPTP or actual TDG history law',
                                'qb1852_source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
                                'cases':rs},indent=2)+'\n')
    print('SAVED',dest)
if __name__=='__main__':run()
