#!/usr/bin/env python3
"""TDG exploratory: physical fresh S4/octupole orientation sampling versus passive gauge.

We extract the spin2->vector coefficient from the exact certified Q-B1852
response source. All subsequent 8D Hamiltonians and stochastic instrument are
new, clearly labelled COMPARATORS; they are not the Root2 physical update.

Run with OPENBLAS_NUM_THREADS=1 TDG_Q1852_SOURCE=... python verify_fresh_chiral_octupole.py
"""
from __future__ import annotations
import contextlib, io, hashlib, itertools, json, math, os, sys
from pathlib import Path
import numpy as np
from numpy.linalg import norm, eigh, svd
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
SOURCE=Path(os.environ.get('TDG_Q1852_SOURCE','/mnt/data/tdg_source_lab/qb1852_extracted/qb1852_full_refined.py'))
sys.path.insert(0,str(SOURCE.parent))
with contextlib.redirect_stdout(io.StringIO()):
    import qb1852_full_refined as q
SHA=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert SHA=='ebbe56f7d9c0b19b5c7e688e2b69c7acd2f9a271d161cf558e50e52cad86b5c7'

# Real orthonormal STF(3) basis in exactly the same order as q.irreps.
E = np.array([
    np.diag([1.,-1.,0.])/np.sqrt(2.),
    np.diag([1.,1.,-2.])/np.sqrt(6.),
    np.array([[0.,1.,0.],[1.,0.,0.],[0.,0.,0.]])/np.sqrt(2.),
    np.array([[0.,0.,1.],[0.,0.,0.],[1.,0.,0.]])/np.sqrt(2.),
    np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,0.]])/np.sqrt(2.),
])
assert norm(np.einsum('aij,bij->ab',E,E)-np.eye(5))<1.e-14
J = np.zeros((3,5));J[0,4]=J[1,3]=J[2,2]=-1/math.sqrt(3)
assert abs(norm(J)-1)<1.e-14
_, coeffs=q.irreps()
MSTF=np.column_stack(coeffs[1:])

# Q-native finite-z A21 coefficients (not the historic readout-free infinite-z c).
qvals=[]
for gamma in (1.,0.):
    for a in (.05,.025,.0125):
        original=q.RefinedQ
        if gamma!=1.:
            q.RefinedQ=lambda scheme,ac,z=2+.7j,need_edges=True,gamma=gamma: original(scheme,ac,z,gamma=gamma,need_edges=need_edges)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                ans=q.analyze('b4',a,2+.7j,do_second=False)
        finally:q.RefinedQ=original
        A21=ans['C'][1:4,:]@MSTF
        c=float(np.sum(A21*J))
        rel=float(norm(A21-c*J)/max(norm(A21),1.e-30))
        assert c>0 and rel<5e-4, (gamma,a,c,rel)
        qvals.append(dict(a=a,gamma=gamma,J_coefficient=c,A21_norm=float(norm(A21)),J_ray_relative_remainder=rel,svd=[float(x) for x in svd(A21,compute_uv=False)],F_cond=float(np.linalg.cond(ans['F']))))
        print('Q',gamma,a,'c',c,'J_residual',rel,flush=True)

C=next(x['J_coefficient'] for x in qvals if x['gamma']==1 and x['a']==.025)
# Cubic rotation matrices; all proper orthogonal rotations with signed axes.
octa=[]
for perm in itertools.permutations(range(3)):
    B=np.eye(3)[:,perm]
    for signs in itertools.product((-1.,1.),repeat=3):
        R=B@np.diag(signs)
        if round(np.linalg.det(R))==1:octa.append(R)
assert len(octa)==24

def U5(R):
    # U_{a,b}=<Ea, R Eb R^T>
    return np.einsum('aij,ik,bkl,jl->ab',E,R,E,R)

def rotate_block(A,R):
    return R@A@U5(R).T

# Symmetry controls. In fixed physical coordinates, a physical rotation of
# the material/background is meaningful, whereas passive gauge transports
# both the field and the coupling and leaves an observable unchanged.
rotJ=[rotate_block(J,R) for R in octa]
chs=[float(np.sum(X*J)) for X in rotJ]
assert max(norm(X-round(chi)*J) for X,chi in zip(rotJ,chs))<1e-13
assert sum(round(x)==1 for x in chs)==12 and sum(round(x)==-1 for x in chs)==12
qmat=next(x for x in qvals if x['gamma']==1 and x['a']==.025)
# The measured exact A21 has its own small O(a^2) departures from the J ray.
with contextlib.redirect_stdout(io.StringIO()):
    full=q.analyze('b4',.025,2+.7j,do_second=False)
Afull=full['C'][1:4,:]@MSTF
qtwirled=np.mean(np.array([rotate_block(Afull,R) for R in octa]),axis=0)
assert norm(qtwirled)<1e-12
# Explicit passive-frame test: physical tensor and vector rotate together.
psi=np.array([0.,0.,1.,0.,0.]);R=octa[7]
passive_error=float(abs(norm(rotate_block(Afull,R)@U5(R)@psi)-norm(Afull@psi)))
assert passive_error<1e-12

# The repair comparator: fixed 8D Hilbert=STF5 + physical vector3.
# H_base assumes five uncoupled tensor components and a gapped vector; it is
# NOT constructed from Q. TT polarizations are tested by an imposed external
# reference polarization (not derived as a constraint by this laboratory).
H0=np.diag([1.]*5+[1.7]*3).astype(complex)
V=np.zeros((8,8),complex)
V[:5,5:]=C*J.T
V[5:,:5]=C*J
Hplus=H0+V;Hminus=H0-V
assert norm(Hplus-Hplus.conj().T)<1e-14
# k=z: normalized plus tensor and cross xy. The initial state superposes both.
psi0=np.zeros(8,complex);psi0[0]=1/math.sqrt(2.);psi0[2]=1/math.sqrt(2.)
rho0=np.outer(psi0,psi0.conj())
T=4.0
Uref=expm(-1j*T*H0)
rho_ref=Uref@rho0@Uref.conj().T

def trace_distance(A,B):
    return .5*float(np.sum(abs(eigh((A-B+A.conj().T-B.conj().T)/2)[0])))

def apply(U,rho):return U@rho@U.conj().T

def vecprob(rho):return float(np.trace(rho[5:,5:]).real)

# Static sector: sign chosen once and kept throughout full experiment. Its
# group mean H=H0 but ensemble retains finite second moment.
UplusT=expm(-1j*T*Hplus);UminusT=expm(-1j*T*Hminus)
rho_static=.5*apply(UplusT,rho0)+.5*apply(UminusT,rho0)

# Fresh, independent, *physical* sign randomization at every time step.
# Kraus K+ = sqrt(p)U+, K- = sqrt(1-p)U-; two-outcome selected records are
# retained in orthogonal fresh slots; unobserved active map is exact CPTP.

def step(p,N):
    dt=T/N;Up=expm(-1j*dt*Hplus);Um=expm(-1j*dt*Hminus)
    Cp=np.sqrt(p)*Up;Cm=np.sqrt(1-p)*Um
    error=float(norm(Cp.conj().T@Cp+Cm.conj().T@Cm-np.eye(8)))
    rho=rho0.copy()
    for _ in range(N):rho=apply(Cp,rho)+apply(Cm,rho)
    eigs=eigh((rho+rho.conj().T)/2)[0]
    purity=float(np.trace(rho@rho).real)
    return dict(steps=N,dt=dt,p=p,vector_probability=vecprob(rho),distance_from_free=trace_distance(rho,rho_ref),
                tr=float(np.trace(rho).real),min_eigenvalue=float(min(eigs)),purity=purity,cptp_error=error)

rows=[]
for p in (.5,.7):
    for N in (10,20,40,80,160,320,640,1280):
        d=step(p,N); rows.append(d)
        assert abs(d['tr']-1)<5e-11 and d['min_eigenvalue']>-5e-12 and d['cptp_error']<1e-12
        print('FRESH',p,N,'vector',d['vector_probability'],'D',d['distance_from_free'],flush=True)
for k in ('distance_from_free','vector_probability'):
    rs=[r for r in rows if r['p']==.5 and r['steps']>=80]
    slope=float(np.polyfit(np.log([r['dt'] for r in rs]),np.log([r[k] for r in rs]),1)[0])
    assert 0.85<slope<1.15,(k,slope)

# Biased p does not remove coherent J: its limit converges to H0+(2p-1)V.
Ubias=expm(-1j*T*(H0+.4*V));rho_bias=apply(Ubias,rho0)
biased_limit=rows[-1]['distance_from_free']
assert abs(biased_limit-trace_distance(rho_bias,rho_ref))<.002

# Direct active TT -> vector leakage for J is not cured by passively
# changing local coordinates. It is suppressed only when the *physical*
# orientation actually changes with fresh independent records.
static_result=dict(vector_probability=vecprob(rho_static),distance_from_free=trace_distance(rho_static,rho_ref),
    free_vector_probability=vecprob(rho_ref),mean_H_H0_error=norm(.5*(Hplus+Hminus)-H0),
    quadratic_coupling_norm=norm(V@V),passive_rotation_error=passive_error)
assert static_result['vector_probability']>rows[-1]['vector_probability']*3

# Existing certified Q-B1852 B3->B2 map can be put in a direct-sum
# absorbing Stinespring instrument independently of the new S4 mixing.
# This tests algebraic COMPATIBILITY, not whether the two dynamics are
# generated from the same Q or whether old memory and tensor are physical.
from scipy.linalg import sqrtm
with contextlib.redirect_stdout(io.StringIO()):model=q.RefinedQ('b4',.025,2+.7j,need_edges=False)
H=model.build_H();f=(0,1,2)
P=np.zeros((model.dim,2),complex)
for ff in model.groupF[f]:P[model.ps(ff),:]+=np.eye(2)/math.sqrt(len(model.groupF[f]))
Vrec=np.asarray(H[model.N4+model.N3:model.N4+model.N3+model.N2,:]@P)
G=Vrec.conj().T@Vrec
w,u=eigh(G);K0=u@np.diag(np.sqrt(1-w))@u.conj().T
rec_error=float(norm(K0.conj().T@K0+Vrec.conj().T@Vrec-np.eye(2)))
# tensor product of 8D independent chiral CPTP and 2D->2D+1020D Q-derived
# outgoing record Stinespring at one step. Completeness follows even if
# one records both the orientation and the absorbing Q memory flag.
dt=T/80;Up=expm(-1j*dt*Hplus);Um=expm(-1j*dt*Hminus)
cp_res=np.zeros((16,16),complex)
for prob,U in [(0.5,Up),(0.5,Um)]:
    cp_res+=prob*np.kron(U.conj().T@U,K0.conj().T@K0)
    cp_res+=prob*np.kron(U.conj().T@U,Vrec.conj().T@Vrec)
combined_error=float(norm(cp_res-np.eye(16)))
assert rec_error<1e-12 and combined_error<1e-12

out={
 'classification':'NEW EXPERIMENTAL QUANTUM CHANNEL: NOT derived Root2 Q update, NOT Einstein equations, NOT validation of future process law',
 'source_q1852_sha256':SHA,
 'source_readout_z':'2+0.7j (conditional finite-z normalization, NOT unique physical coupling)',
 'original_Q_derived_J_amplitude':qvals,
 'chirality_coupling_used':float(C),
 'cubic_group':dict(rotations=24,sign_plus=12,sign_minus=12,full_Q_twirling_error=float(norm(qtwirled)),
                     passive_frame_invariance_error=passive_error,
                     note='Passive relabeling is a NO-GO; active stochastic orientation is an additional physical postulate.'),
 'comparator':dict(H0_tensor_energy=1.,H0_vector_energy=1.7,total_time=T,initial_state='(plus+cross)/sqrt(2) for k=z',
                   static_orientation_mixture=static_result,
                   rows=rows,
                   biased_p_0p7_ideal_limit_distance=float(trace_distance(rho_bias,rho_ref)),
                   weak_per_step_limit='p=1/2: Phi_dt = Ad_{exp(-i dt H0)} - dt^2/2 [V,[V,rho]] + O(dt^3) in one step, T steps -> O(T dt) correction',
                   continuous_unbiased_limit='Unitary H0 ONLY in finite-T weak-step scaling, not for arbitrary strong-memory scalings'),
 'q_b2_record_compatibility':dict(B2_output_dimension=int(Vrec.shape[0]),VdagV_eigs=[float(v) for v in w],
                                  one_step_Q_record_isometry_error=rec_error,
                                  chiral_times_record_cptp_error=combined_error),
 'firewalls':['A21 and c are from true Q-B1852 but 8D H0 gap and randomized sign process are newly imposed.',
              'The new channel does not derive physical TT constraints; two helicities only belong to the reference GR projector.',
              'A static sign ensemble is not enough; the sign needs physical refresh at rate 1/dt and unbiased conditional weights.',
              'p bias leaves O(1) forbidden coherent tensor-vector coupling.',
              'Historical Q STF->gradient obstruction remains nonzero and unaffected in frozen Q.',
              'Composition of two CP instruments is only algebraic capacity, not one joint selected-future Q-native law.']
}
path=HERE/'results.json';path.write_text(json.dumps(out,indent=2)+'\n')
print('RESULTS',path,flush=True)
