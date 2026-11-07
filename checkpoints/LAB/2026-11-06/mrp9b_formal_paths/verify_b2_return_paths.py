#!/usr/bin/env python3
"""Decompose the first Q-B1852 formal descent obstruction into paths via B2.

No resolvent readout or adjustable correction: this is a path-type identity
on the sparse certified Hermitian H. The parent and bright face are physical
selectors already present in qb1852. Tested for both b4/b24 subdivisions.
"""
import sys,json,hashlib
import numpy as np
from numpy.linalg import norm,pinv
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from verify_mrp9b_b4_b24_moment_source import construct
from verify_mrp9b_formal_descent import selector,q,SRC


def run_case(scheme,ac,gamma,c=(0,1,2,3),f=(0,1,2)):
    m=construct(scheme,ac,gamma);H=m.build_H()
    P=selector(m,c);F=selector(m,f)
    idx=c.index(next(iter(set(c)-set(f))))
    Cd=(q.A[idx]@q.Bcanon[idx]).conj().T
    ker=np.eye(6)-pinv(Cd)@Cd
    HT=H@P;HHT=H@HT;HHHT=H@HHT
    HF=H@F;HHF=H@HF
    TT1=P.conj().T@HT;TT2=P.conj().T@HHT
    FT1=F.conj().T@HT;FT2=F.conj().T@HHT;FT3=F.conj().T@HHHT
    FF1=F.conj().T@HF;FF2=F.conj().T@HHF
    Lpost2=FT2-FF1@FT1
    Lpost3=FT3-FF1@FT2+(FF1@FF1-FF2)@FT1
    # Leading K0=ac I; n2 K1 is selected only to subtract the row part.
    K1=(Lpost2-ac*Cd@TT1)@pinv(Cd)
    D3=(Lpost3-ac*Cd@TT2-K1@Cd@TT1)@ker
    # F <-- B2 <-- B3 <-- T: path exactly 3 hops from T to F.
    b3slice=slice(m.N4,m.N4+m.N3)
    b2slice=slice(m.N4+m.N3,m.N4+m.N3+m.N2)
    V=np.zeros_like(HT);V[b3slice,:]=HT[b3slice,:]
    V=H@V
    W=np.zeros_like(HT);W[b2slice,:]=V[b2slice,:]
    B2=F.conj().T@(H@W)
    B2null=B2@ker
    err=norm(D3-B2null)
    return {'scheme':scheme,'ac':ac,'gamma':gamma,'dim':m.dim,'D3_null_norm':float(norm(D3)),
            'B2_return_null_norm':float(norm(B2null)),'B2_source_identity_error':float(err),
            'B2_source_relative_error':float(err/max(norm(D3),1e-30)),
            'K1_norm':float(norm(K1)),
            'B2_return_matrix_real':np.real(B2null).tolist(),
            'B2_return_matrix_imag':np.imag(B2null).tolist()}

if __name__=='__main__':
    out=[]
    for scheme in ['b4','b24']:
        for a in [.05,.025,.0125]:
            for gamma in [0.,.5,1.,2.]:
                r=run_case(scheme,a,gamma);out.append(r)
                print(scheme,a,gamma,'D3',r['D3_null_norm'],'B2',r['B2_return_null_norm'],'identity error',r['B2_source_identity_error'],'relative',r['B2_source_relative_error'],flush=True)
    dest=(Path(__file__).resolve().parent / 'b2_path_identity_results.json')
    dest.write_text(json.dumps({'scope':'Exact Q1852 sparse H path projection, no resolvent z, conditional Q1592 chart',
                                'qb1852_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'cases':out},indent=2)+'\n')
    print('SAVED',dest)
