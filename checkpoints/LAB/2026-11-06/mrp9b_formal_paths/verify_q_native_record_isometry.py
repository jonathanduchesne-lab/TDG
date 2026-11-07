#!/usr/bin/env python3
"""A CPTP/append-only proof-of-capacity using actual Q-B1852 B3->B2 couplings.

This is a *new, proposed* absorbing-record instrument, not the frozen Q law.
It uses actual bright B3 to B2 block V from certified sparse H, and an
untuned unit-step Kraus completion K0=sqrt(I-V^dag V), K1=V whenever V is a
contraction. Fresh records are terminal outputs and never feed back. The
result is an explicit Stinespring isometry; it is not the same as replacing
H with a one-way triangular matrix, and does not derive Einstein equations.
"""
import sys,hashlib,json
from pathlib import Path
import numpy as np
from numpy.linalg import norm,eigh
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_mrp9b_b4_b24_moment_source import construct
from verify_mrp9b_formal_descent import selector,SRC

def one(scheme,a,gamma=1.,face=(0,1,2),nsteps=8):
    m=construct(scheme,a,gamma)
    H=m.build_H();P=selector(m,face)
    B2=slice(m.N4+m.N3,m.N4+m.N3+m.N2)
    V=H[B2,:]@P # extracted from original Hermitian Q; size N2 x M2
    G=V.conj().T@V
    w,U=eigh(G)
    if min(w)<-1e-11 or max(w)>1.+1e-11:raise ArithmeticError('V not a contraction; no zero-parameter completion')
    K0=U@np.diag(np.sqrt(np.maximum(0.,1.-w)))@U.conj().T
    K1=V
    I=np.eye(2,dtype=complex)
    isometry_error=norm(K0.conj().T@K0+K1.conj().T@K1-I)
    # n-step absorbing (first-event) Kraus map:
    # one active K0^n, and a retained R[k]=K1 K0^k for each k=0..n-1.
    full=[np.linalg.matrix_power(K0,nsteps)]+[K1@np.linalg.matrix_power(K0,k) for k in range(nsteps)]
    completeness=sum((X.conj().T@X for X in full),np.zeros((2,2),complex))
    chronology_error=norm(completeness-I)
    # First record R0=K1 is exactly unchanged as n grows.
    for n in [1,2,4,8]:
        short=[np.linalg.matrix_power(K0,n)]+[K1@np.linalg.matrix_power(K0,k) for k in range(n)]
        assert norm(sum((X.conj().T@X for X in short),np.zeros((2,2),complex))-I)<1e-10
    rho=np.array([[.5,.5],[.5,.5]],complex)
    probs=[float(np.real(np.trace(X@rho@X.conj().T))) for X in full]
    return dict(scheme=scheme,a=a,gamma=gamma,face=list(face),B2_dimension=int(V.shape[0]),
                V_gram_eigs=[float(x) for x in w],one_step_cptp_error=float(isometry_error),
                nstep_cptp_error=float(chronology_error),nsteps=nsteps,
                nstep_outcome_prob_sum=float(sum(probs)),
                no_record_probability=probs[0],first_record_probability=probs[1],
                late_record_probability=probs[-1],
                retained_first_record_operator_norm=float(norm(K1)),
                physical_claim='This is a new candidate Stinespring instrument using Q coupling, not proof of actual TDG update')

if __name__=='__main__':
    out=[]
    for scheme in ['b4','b24']:
        for a in [.05,.025,.0125]:
            r=one(scheme,a);out.append(r)
            print(scheme,a,'eigs',r['V_gram_eigs'],'1step',r['one_step_cptp_error'],
                  '8step',r['nstep_cptp_error'],'P_recordfirst',r['first_record_probability'],
                  'P_norecord',r['no_record_probability'],flush=True)
    f=(Path(__file__).resolve().parent / 'record_isometry_results.json')
    f.write_text(json.dumps({'scope':'New absorbing-record isometry from actual Q-B1852 B3->B2 block, NOT licensed as Q update',
                             'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'cases':out},indent=2)+'\n')
    print('SAVED',f)
