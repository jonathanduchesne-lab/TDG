#!/usr/bin/env python3
"""TDG MRP9B laboratory: first-principles Feshbach response and face-link holonomy.

NOT the unrecovered Q-B1592 numerical chart and NOT a numerical execution of the
canonical TDG Q. The Hamiltonian is a minimal, explicitly declared comparator
respecting the documented B4 C6 / shared B3 C2 block types and scalar-I2 bare legs.

Author: TDG collaborative research laboratory, 2026-11-06.
"""
import json
import numpy as np
from numpy.linalg import inv, det, norm, matrix_rank
from scipy.linalg import logm, expm
from pathlib import Path

OUT=Path('/mnt/data/tdg_mrp9b_feshbach_holonomy_resultats_2026_11_06.json')
I2=np.eye(2,dtype=complex)
sx=np.array([[0,1],[1,0]],dtype=complex)
sy=np.array([[0,-1j],[1j,0]],dtype=complex)
sz=np.array([[1,0],[0,-1]],dtype=complex)
paulis=[sx,sy,sz]
Z=2.0
weights=np.array([1,2,1],dtype=float)/np.sqrt(6)


def schur_chart(a,v,source_power=1,z=Z):
    """Full 6x2 bare incidence -> 2x2 port self-energy with no pseudoinverse.

    H_B = I3 tensor [a^p (v dot sigma)] is a synthetic Herm2 core.
    B = a (w tensor I2) is a bare scalar-internal 6x2 B4<->B3 leg.
    Sigma = B^dag (zI6-H_B)^-1 B; det-normalize to SL(2,C).
    """
    X=sum(float(v[i])*paulis[i] for i in range(3))
    H=np.kron(np.eye(3), (a**source_power)*X)
    B=a*np.kron(weights.reshape(3,1),I2)
    G=inv(z*np.eye(6)-H)
    Sigma=B.conj().T @ G @ B
    d=det(Sigma)
    if abs(d.imag)>1e-9 or d.real<=0:
        raise ValueError('Response not positive invertible for selected parameters')
    K=Sigma/np.sqrt(d.real)
    return K,Sigma,H,B


def source_resolvent_identity(a,v,p=1):
    K,Sigma,H,B=schur_chart(a,v,p)
    Hfull=np.block([[np.zeros((2,2),dtype=complex), B.conj().T],[B,H]])
    R=inv(Z*np.eye(8,dtype=complex)-Hfull)
    Rpe=R[2:,:2]; Ree=R[:2,:2]
    C=Rpe@inv(Ree)
    canon=inv(Z*np.eye(6)-H)@B
    projected=B.conj().T@C
    return float(norm(C-canon)),float(norm(projected-Sigma))


def loop_link(a,p=1):
    """Four edges around a plaquette; each edge has two shared-port charts.

    Each oriented edge source chart=I, target chart=K(v) with v=x,y,-x,-y.
    These face-specific assignments are deliberately synthetic, not Q-derived.
    Links act from the source cell to the target cell; path order is reversed.
    """
    dirs=[(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]
    links=[]
    for direction in dirs:
        src=schur_chart(a,(0,0,0),p)[0]
        dst=schur_chart(a,direction,p)[0]
        links.append(dst@inv(src))
    P=I2.copy()
    for L in links:
        P=L@P
    return P,links


def pure_gauge_loop(a):
    """K_{cell,face}=G_cell for all faces => telescoping loop identically I.
    Despite noncentral links, there is no curvature.
    """
    vecs=[(1,0,0),(0,1,0),(-1,0,0),(0,0,1)]
    G=[schur_chart(a,v)[0] for v in vecs]
    links=[G[(i+1)%4]@inv(G[i]) for i in range(4)]
    P=I2.copy()
    for L in links:P=L@P
    return float(norm(P-I2)),float(max(norm(L-I2) for L in links))


def common_right_frame_test(a):
    """K_{c,f}->K_{c,f}H_f cancels in K_{d,f}K_{c,f}^-1."""
    Kc=schur_chart(a,(1,0.2,0))[0]
    Kd=schur_chart(a,(0.1,1,0))[0]
    H=expm(0.23j*sz + 0.17*sx)
    original=Kd@inv(Kc)
    transformed=(Kd@H)@inv(Kc@H)
    return float(norm(original-transformed))


def common_spin_covariance(a):
    """At a shared 2x2 spin basis, X->UXU^dag, Sigma->USigmaU^dag."""
    U=expm(.3j*sy+.2j*sz)
    P,_=loop_link(a)
    links=[]
    for v in [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]:
        v=np.asarray(v)
        X=sum(float(v[i])*paulis[i] for i in range(3))
        H=np.kron(np.eye(3),a*(U@X@U.conj().T))
        B=a*np.kron(weights.reshape(3,1),I2)
        Sigma=B.conj().T@inv(Z*np.eye(6)-H)@B
        K=Sigma/np.sqrt(det(Sigma).real)
        links.append(K)
    Q=I2.copy()
    for K in links:Q=K@Q
    return float(norm(Q-U@P@U.conj().T))


def real3_rank_jacobian(a):
    """Central finite difference on the three independent Herm2 source slots."""
    eps=1e-6
    tangent=[]
    for i in range(3):
        v=np.zeros(3);v[i]=eps
        U,_S,_H,_B=schur_chart(a,v)
        D,_S,_H,_B=schur_chart(a,-v)
        t=(U-D)/(2*eps)
        tangent.append(np.r_[t.real.flatten(),t.imag.flatten()])
    return int(matrix_rank(np.stack(tangent,axis=1),tol=1e-8)), float(norm(np.stack(tangent,axis=1)))


metrics={}
for a in [.4,.2,.1,.05,.025,.0125]:
    P,L=loop_link(a)
    target=(sy@sx-sx@sy)/(Z**2)
    F=logm(P)/(a*a)
    gauge_error=common_spin_covariance(a)
    gerr,glink=pure_gauge_loop(a)
    e1,e2=source_resolvent_identity(a,(1.,.3,.2))
    metrics[str(a)]={
        'loop_norm_P_minus_I':float(norm(P-I2)),
        'curvature_log_over_a2_norm':float(norm(F)),
        'curvature_limit_error':float(norm(F-target)),
        'trace_P_real':float(np.trace(P).real),
        'imaginary_trace_abs':float(abs(np.trace(P).imag)),
        'determinant_error':float(abs(det(P)-1)),
        'spin_frame_covariance_error':gauge_error,
        'pure_gauge_holonomy_error':gerr,
        'pure_gauge_link_nontriviality':glink,
        'exact_resolvent_crossing_identity_error':e1,
        'exact_self_energy_projection_error':e2,
        'common_face_right_factor_cancellation_error':common_right_frame_test(a),
    }
    assert metrics[str(a)]['determinant_error'] < 1e-10
    assert gauge_error < 1e-10
    assert gerr < 1e-10
    assert glink > 1e-4
    assert e1<1e-10 and e2<1e-10

rank,tangent_norm=real3_rank_jacobian(.1)
assert rank==3
# Scaling adversaries: p=0 makes curvature/a^2 diverge; p=2 makes it vanish.
scaling={}
for p in [0,1,2]:
    points=[]
    for a in [.2,.1,.05,.025]:
        if p==0:
            # fixed Herm2 source 0.25 to avoid too-large nonlinearity.
            # use an alternative effective scale b=0.25, keeping incidence a.
            # changing incidence only scales Sigma by a^2 and does not change chart.
            P,_=loop_link(.25,1)
        else:P,_=loop_link(a,p)
        points.append({'a':a,'norm_logP_over_a2':float(norm(logm(P))/(a*a))})
    ratios=[points[i+1]['norm_logP_over_a2']/points[i]['norm_logP_over_a2'] for i in range(len(points)-1)]
    scaling[str(p)]={'points':points,'halving_ratios':ratios}

# Stronger factorization theorem: K_(cell,face)=G_cell H_face telescopes.
def cell_face_factorization_control(a):
    G=[schur_chart(a,v)[0] for v in [(1,0,0),(0,1,0),(-1,0,0),(0,0,1)]]
    Hf=[expm((i+1)*.17j*sx + (i+1)*.07*sz) for i in range(4)]
    P=I2.copy(); most_noncentral=0.0
    for i in range(4):
        Ksrc=G[i]@Hf[i]
        Kdst=G[(i+1)%4]@Hf[i]
        L=Kdst@inv(Ksrc)
        most_noncentral=max(most_noncentral,float(norm(L-I2)))
        P=L@P
    return float(norm(P-I2)),most_noncentral


def lorentz_representation(K):
    '''Spinor SL2(C) action X->K X K^dag on Herm2 Minkowski coefficients.'''
    mats=[I2,sx,sy,sz]
    Lambda=np.zeros((4,4),dtype=float)
    for nu,M in enumerate(mats):
        H=K@M@K.conj().T
        for mu,S in enumerate(mats):
            Lambda[mu,nu]=float((np.trace(S@H)/2).real)
    eta=np.diag([1,-1,-1,-1])
    return Lambda,float(norm(Lambda.T@eta@Lambda-eta)),float(abs(det(Lambda)-1))

# Exact rank-three vertical su(2) commutator sector of independent boosts.
commutators=[sy@sx-sx@sy,sz@sy-sy@sz,sx@sz-sz@sx]
comm_columns=np.stack([np.r_[m.real.reshape(-1),m.imag.reshape(-1)] for m in commutators],axis=1)
frame_curvature_rank=matrix_rank(comm_columns,tol=1e-12)
assert frame_curvature_rank==3
factor_test={str(a): cell_face_factorization_control(a) for a in [.2,.1,.05]}
assert all(v[0]<1e-10 and v[1]>1e-4 for v in factor_test.values())
P_small,_=loop_link(.05)
Lsmall,lorentz_err,lorentz_det_err=lorentz_representation(P_small)
assert lorentz_err<1e-10 and lorentz_det_err<1e-10

# Analytic series: for p=1, log holonomy / a^2 -> [sy,sx]/Z^2.
expected=(sy@sx-sx@sy)/(Z*Z)
# Orthogonality/control of bare scalar H: all charts central.
def scalar_control(a):
    H=np.zeros((6,6),complex)
    B=a*np.kron(weights.reshape(3,1),I2)
    Sig=B.conj().T@inv(Z*np.eye(6)-H)@B
    K=Sig/np.sqrt(det(Sig).real)
    return float(norm(K-I2))

output={
 'scope':'Synthetic Q-typed B4=C6/B3=C2 exact Schur/Feshbach comparator; NOT the recovered numerical Q-B1592 chart; NOT a current Q derivation.',
 'provenance':'Uses the recovered port-source ratio R_pe R_ee^-1 and documented bare 6x2 scalar-I2 incidence shape, plus a plainly assumed synthetic Herm2 core.',
 'rank3_herm2_tangent':rank,
 'boost_commutator_vertical_su2_rank':int(frame_curvature_rank),
 'cell_face_factorized_flat_control':{k:{'holonomy_error':v[0],'max_link_nontriviality':v[1]} for k,v in factor_test.items()},
 'lorentz_action_at_a_0_05':{'metric_preservation_error':lorentz_err,'determinant_error':lorentz_det_err,'matrix':Lsmall.tolist()},
 'tangent_total_norm':tangent_norm,
 'scalar_bare_source_control':scalar_control(.1),
 'curvature_limit_matrix_real':expected.real.tolist(),
 'curvature_limit_matrix_imag':expected.imag.tolist(),
 'curvature_limit_norm':float(norm(expected)),
 'metrics':metrics,
 'source_scaling_adversaries':scaling,
 'conclusion':'Noncentral relative links can occur with scalar-I2 bare incidence after Herm2 Schur dressing. Noncentrality alone insufficient: cell-only charts telescope to flat holonomy. Face-dependent dressed attachments generate O(a^2) loop curvature for an O(a) Herm2 contrast, but this mechanism is hypothetical until same-Q cell/face charts are reconstructed.'
}
OUT.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
print('MRP9B_SYNTHETIC_SCHUR_COMPARATOR',output['scope'])
print('RANK3_HERM2_TANGENT',rank)
print('RANK3_VERTICAL_SU2_COMMUTATORS',frame_curvature_rank)
print('CELL_FACE_FACTORIZATION_ERRORS',factor_test)
print('LORENTZ_PRESERVATION_ERR',lorentz_err)
print('EXPECTED_LIMIT_NORM',norm(expected))
for a,vals in metrics.items():
 print('a',a,'hol_norm',vals['loop_norm_P_minus_I'],'F_norm',vals['curvature_log_over_a2_norm'],'F_err',vals['curvature_limit_error'],'pure_gauge_err',vals['pure_gauge_holonomy_error'],'frame_err',vals['spin_frame_covariance_error'])
for k,v in scaling.items():print('SCALING_POWER',k,'RATIOS',v['halving_ratios'])
print('RESULTS',OUT)
