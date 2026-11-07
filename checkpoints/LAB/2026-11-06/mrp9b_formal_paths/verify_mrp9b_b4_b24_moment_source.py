#!/usr/bin/env python3
"""Q-B1852 formal selected-port descent obstruction: first offending Q moment.

Exact sparse Hamiltonian for both historical b4 and b24 topologies. This
bypasses *only* unnecessary LU: full-Q moments H^k (not G(z)) are computed
with exact sparse applications. No fitted projectors, z or target tensors.
"""
import sys,hashlib,json,itertools,contextlib,io,time
from pathlib import Path
import numpy as np
from numpy.linalg import norm, pinv, svd
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_mrp9b_formal_descent import q, selector, SRC


def construct(scheme,ac,gamma):
    m=q.RefinedQ.__new__(q.RefinedQ)
    m.scheme=scheme;m.ac=ac;m.gamma=gamma;m.z=None;m.parents=q.coarse_universe();m.iP={t:i for i,t in enumerate(m.parents)}
    m.coarseB3=sorted(set(tuple(sorted(F)) for t in m.parents for F in itertools.combinations(t,3)))
    m.coarseB2=sorted(set(tuple(sorted(e)) for t in m.parents for e in itertools.combinations(t,2)))
    if scheme=='b4':m._top_b4()
    else:m._top_b24()
    m.i4={t:i for i,t in enumerate(m.FB4)};m.i3={t:i for i,t in enumerate(m.FB3)};m.i2={t:i for i,t in enumerate(m.FB2)}
    m.N4=6*len(m.FB4);m.N3=2*len(m.FB3);m.N2=2*len(m.FB2);m.NP=6*len(m.parents)
    m.dim=m.N4+m.N3+m.N2+m.NP
    return m


def moment_descent(model,c,f,order=7):
    H=model.build_H()
    A=selector(model,c);F=selector(model,f)
    idx=c.index(next(iter(set(c)-set(f))))
    Cd=(q.A[idx]@q.Bcanon[idx]).conj().T
    Cplus=pinv(Cd)
    V=A.copy();W=F.copy()
    mtt=[];mft=[];mff=[]
    for n in range(order+1):
        mtt.append(A.conj().T@V);mft.append(F.conj().T@V);mff.append(F.conj().T@W)
        if n<order:V=H@V;W=H@W
    pre=[np.zeros((2,6),complex)]+[Cd@x for x in mtt[:order]]
    post=[np.zeros((2,6),complex) for _ in range(order+1)]
    for n in range(1,order+1):
        post[n]=mft[n].copy()
        for k in range(1,n+1):post[n]-=mff[k]@post[n-k]
    K=[];results=[]
    for n in range(1,order+1):
        rhs=post[n].copy()
        for j in range(n-1):rhs-=K[j]@pre[n-j]
        Kn=rhs@Cplus
        residual=rhs-Kn@Cd
        K.append(Kn)
        results.append({'n':n,'descent_residual_norm':float(norm(residual)),
                        'rhs_norm':float(norm(rhs)),'residual_fraction':float(norm(residual)/max(norm(rhs),1e-30)),
                        'relative_to_port_coupling':float(norm(residual)/max(norm(mft[1]),1e-30))})
    return {'scheme':model.scheme,'a':model.ac,'gamma':model.gamma,'dim':model.dim,'nnz':H.nnz,
            'parent_count':len(model.parents),'fine_B4':len(model.FB4),
            'fine_B3':len(model.FB3),'fine_B2':len(model.FB2),
            'leading_coupling_error':float(norm(mft[1]-model.ac*Cd)/max(norm(mft[1]),1e-30)),
            'moments':results}


def main():
    out=[]
    for scheme in ['b4','b24']:
        for a in [.05,.025,.0125]:
            for gamma in [0.,.5,1.,2.]:
                t0=time.perf_counter();m=construct(scheme,a,gamma)
                x=moment_descent(m,(0,1,2,3),(0,1,2),7)
                x['runtime_seconds']=round(time.perf_counter()-t0,2)
                out.append(x)
                D=x['moments'][2]['descent_residual_norm'];D5=x['moments'][4]['descent_residual_norm']
                print(scheme,'a',a,'gamma',gamma,'dim',x['dim'],'nnz',x['nnz'],
                      'D3',D,'D3/(g^2*a^3)',D/(gamma*gamma*a**3) if gamma else None,
                      'D5',D5,'run',x['runtime_seconds'],flush=True)
    dest=(Path(__file__).resolve().parent / 'b4_b24_formal_results.json')
    dest.write_text(json.dumps({'status':'Q-B1852 source H path-moment audit (no resolvent readout)',
        'original_source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
        'observations':out},indent=2)+'\n')
    print('SAVED',dest)
if __name__=='__main__':main()
