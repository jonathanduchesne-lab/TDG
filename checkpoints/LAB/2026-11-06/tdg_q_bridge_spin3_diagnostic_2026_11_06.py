"""TDG/Q -> geometry, next lab: classify the canonical S4 J obstruction,
then compare it with genuinely covariant (continuum) discrete divergence maps.

Scope: diagnostic conditioned on identifying TDG's S4 (l2,l1) modules with
physical STF(3) and ordinary vectors. This does not reconstruct microscopic Q.
The certified J ray is from TDG's 2026-09-18 formal-readout-free checkpoint.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as sp
from numpy.linalg import norm, matrix_rank
from scipy.linalg import null_space

P = Path('/mnt/data')
rng = np.random.default_rng(20261106)

def eij(i,j):
    x=np.zeros((3,3));x[i,j]=1.;return x

E=np.array([
    np.diag([1.,-1.,0.])/np.sqrt(2),
    np.diag([1.,1.,-2.])/np.sqrt(6),
    (eij(0,1)+eij(1,0))/np.sqrt(2),
    (eij(0,2)+eij(2,0))/np.sqrt(2),
    (eij(1,2)+eij(2,1))/np.sqrt(2),
])
assert norm(np.einsum('aij,bij->ab',E,E)-np.eye(5))<1e-14

# Fixed canonical TDG ray: J = -(1/sqrt3)[yz->x, xz->y, xy->z].
J=np.zeros((3,5))
J[0,4]=J[1,3]=J[2,2]=-1/np.sqrt(3)
assert abs(norm(J)-1)<1e-14
c_inf=10.769201
T=np.einsum('ia,ajk->ijk',J,E)
permutation_errors=[float(norm(T-np.transpose(T,perm))) for perm in itertools.permutations(range(3))]
trace_errors=[float(norm(np.einsum('ijj->i',T))),float(norm(np.einsum('jij->i',T))),float(norm(np.einsum('jji->i',T)))]
assert max(permutation_errors+trace_errors)<1e-13
nonzero_t=[(i,j,k,float(T[i,j,k])) for i,j,k in itertools.product(range(3),repeat=3) if abs(T[i,j,k])>1e-12]
assert len(nonzero_t)==6
assert max(abs(item[3]+1/np.sqrt(6)) for item in nonzero_t)<1e-14
x,y,z=sp.symbols('x y z',real=True)
H=-sp.sqrt(6)*x*y*z
assert sum(sp.diff(H,s,2) for s in [x,y,z])==0

# Eigenvector decomposition on physical spin-2; J is a pure spin-3 octupolar background.
def U5(R):
    ER=np.einsum('ij,ajk,lk->ail',R,E,R)
    return np.einsum('aij,bij->ab',E,ER)

def Jrot(R):
    return R@J@U5(R).T

Rz90=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,1.]])
Rtetr=np.diag([-1.,-1.,1.])
Rcycle=np.array([[0.,1.,0.],[0.,0.,1.],[1.,0.,0.]])
assert norm(Jrot(Rz90)+J)<1e-14
assert norm(Jrot(Rtetr)-J)<1e-14
assert norm(Jrot(Rcycle)-J)<1e-14

# Enumerate 24 signed/permuted proper rotations (octahedral group).
octa=[]
for perm in itertools.permutations(range(3)):
    base=np.eye(3)[:,perm]
    for sig in itertools.product([-1.,1.],repeat=3):
        R=base@np.diag(sig)
        if round(np.linalg.det(R))==1:
            octa.append(R)
assert len(octa)==24
J_oct=np.array([Jrot(R) for R in octa])
oct_mean=np.mean(J_oct,axis=0)
oct_JtJ=np.mean([A.T@A for A in J_oct],axis=0)
assert norm(oct_mean)<1e-13
assert norm(oct_JtJ-np.diag([0,0,1/3,1/3,1/3]))<1e-13

# The 24 proper cubic rotations realize an abstract S4 group. In this
# representative model, J is NOT an intertwiner to the physical vector R;
# it IS an intertwiner to the sign-twisted three-dimensional S4 module chi(R)*R.
# This discrete sign character cannot extend as a nontrivial continuous sign
# character on connected SO3. Actual TDG-to-SO3 module identification remains open.
s4_sign_test=[]
for R in octa:
    A=Jrot(R)
    chi=int(round(float(np.sum(A*J)/(norm(J)**2))))
    perm=np.argmax(abs(R),axis=0)
    permutation=np.eye(3)[:,perm]
    chi_perm=int(round(np.linalg.det(permutation)))
    s4_sign_test.append((chi,chi_perm,float(norm(A-chi*J))))
assert len(s4_sign_test)==24
assert all(chi==chi_perm for chi,chi_perm,_ in s4_sign_test)
assert max(row[2] for row in s4_sign_test)<1e-13
assert sum(chi==1 for chi,_,_ in s4_sign_test)==12
assert sum(chi==-1 for chi,_,_ in s4_sign_test)==12

# Samples of proper Haar distributed SO3 orientations.
def rotation():
    X=rng.normal(size=(3,3))
    Q,R=np.linalg.qr(X)
    signs=np.sign(np.diag(R)); signs[signs==0]=1
    Q=Q@np.diag(signs)
    if np.linalg.det(Q)<0:Q[:,0]*=-1
    return Q

n_rot=6000
T2=np.zeros((5,5))
Jsum=np.zeros((3,5))
for _ in range(n_rot):
    JR=Jrot(rotation())
    T2+=JR.T@JR
    Jsum+=JR
T2/=n_rot
Jsum/=n_rot
haar_quadratic_error=norm(T2-np.eye(5)/5)
assert haar_quadratic_error<0.06

# TT vectors and SO3-natural continuum divergence.
def D(k):
    return np.einsum('aij,j->ia',E,k)

def Dlat(k,a,order):
    if order==2:
        khat=np.sin(a*k)/a
    elif order==4:
        khat=(8*np.sin(a*k)-np.sin(2*a*k))/(6*a)
    else:
        raise ValueError('order=2|4')
    return D(khat)

n_trials=300
ks=[];rots=[];TTS=[];jtt=[]
for _ in range(n_trials):
    k=rng.normal(size=3); k/=norm(k)
    R=rotation(); TT=null_space(D(k),rcond=1e-12)
    assert TT.shape==(5,2)
    ks.append(k); rots.append(R);TTS.append(TT)
    jtt.append(norm(J@TT))
assert np.mean(jtt)>0.1

# A fixed J is not a derivative: its TT leakage persists as a->0.
scales=[.8,.4,.2,.1,.05]
rows=[]
for a in scales:
    row={'a':a}
    for order in [2,4]:
        vals=[];cov=[]
        for k,R,TT in zip(ks,rots,TTS):
            vals.append(norm(Dlat(k,a,order)@TT))
            U=U5(R)
            cov.append(norm(Dlat(R@k,a,order)@U-R@Dlat(k,a,order)))
        row[f'tt_leak_o{order}']=float(np.mean(vals))
        row[f'cov_defect_o{order}']=float(np.mean(cov))
    row['J_TT_leak']=float(np.mean(jtt))
    rows.append(row)

# a^2 and a^4 convergence observed; monotonic.
for order in [2,4]:
    key=f'tt_leak_o{order}'
    values=np.array([row[key] for row in rows])
    slope=float(np.polyfit(np.log(scales),np.log(values),1)[0])
    assert abs(slope-order)<0.22, (order,slope)
    for r in rows:r[f'fit_rate_o{order}']=slope

# A mean of randomly oriented octupolar couplings vanishes, while a quadratic
# memory/intensity observable survives (constant 1/5*Id by SO3 irreducibility).
coarsening=[]
for N in [1,4,16,64,256]:
    norms=[]
    for _ in range(150):
        M=sum((Jrot(rotation()) for __ in range(N)),np.zeros((3,5)))/N
        norms.append(norm(M))
    coarsening.append({'domains':N,'mean_coupling_norm':float(np.mean(norms)), 'mean_square':float(np.mean(np.array(norms)**2)),'haar_expected_mean_square':1/N})
assert abs(coarsening[-1]['mean_square']-1/256)<0.002

# Projected TT response from fixed J, and static divergence for k=z.
kz=np.array([0.,0.,1.])
TTz=null_space(D(kz),rcond=1e-13)
TTz_intersect=5-matrix_rank(np.vstack([D(kz),J]))
assert TTz_intersect==1
assert norm(D(kz)@TTz)<1e-14

# No order-zero O3-intertwiner exists between STF2 and vector;
# group average demonstrates this explicitly for the certified J.
# But quadratic invariants remain even when mean coupling is zero.
res={
    'scope':'Diagnostic map and synthetic discrete-geometry repair, NOT a recovered microscopic TDG-Q law or a derivation of nonlinear GR',
    'model_source':'Canonical J ray in TDG 2026-09-18 formal readout-free checkpoint',
    'conditional_identification':'Assumes S4 l2 and l1 TDG slots realize physical SO3 STF2 and vector modules',
    'spin3':{
        'J_frobenius_norm':float(norm(J)),
        'full_symmetry_error_max':max(permutation_errors),
        'trace_error_max':max(trace_errors),
        'nonzero_T_ijk':nonzero_t,
        'harmonic_polynomial':'-sqrt(6)*x*y*z',
        'laplacian_H':'0',
        'tetrahedral_halfturn_invariance_error':float(norm(Jrot(Rtetr)-J)),
        'tetrahedral_cyclic_invariance_error':float(norm(Jrot(Rcycle)-J)),
        'quarterturn_sign_reversal_error':float(norm(Jrot(Rz90)+J)),
        'physical_TT_nonzero_at_kz':float(norm(J@TTz)),
        'physical_TT_joint_kernel_at_kz':int(TTz_intersect),
        'random_k_mean_J_on_TT':float(np.mean(jtt)),
        'random_k_min_J_on_TT':float(np.min(jtt)),
        'random_k_max_J_on_TT':float(np.max(jtt)),
    },
    'octahedral_S4_twist':{
        'rotations':24,
        'regular_vector_intertwinement_fails':'12 of the 24 signed-permutation rotations return -J',
        'twisted_vector_intertwinement_passes':'chi(R)*R with chi parity of permutation axes',
        'chi_positive':12,
        'chi_negative':12,
        'max_twisted_intertwiner_error':max(row[2] for row in s4_sign_test),
        'important_caveat':'This uses a selected embedding of the abstract S4 into proper cubic rotations; mapping these modules to physical rotations in frozen TDG-Q remains a separate unresolved problem.'
    },
    'octahedral_twirling':{
        'rotations':len(octa),
        'mean_J_norm':float(norm(oct_mean)),
        'mean_JtJ_diagonal':np.diag(oct_JtJ).tolist(),
        'mean_JtJ_offdiag_norm':float(norm(oct_JtJ-np.diag(np.diag(oct_JtJ))))
    },
    'haar_SO3_twirling':{
        'rotations':n_rot,
        'mean_J_norm':float(norm(Jsum)),
        'quadratic_deviation_from_I5/5':float(haar_quadratic_error),
        'quadratic_diagonal':np.diag(T2).tolist(),
        'theoretical_quadratic':float(norm(J)**2/5),
        'renormalized_quadratic_with_c_inf':float(c_inf*c_inf/5)
    },
    'discrete_covariant_divergence':{
        'wave_number':1,
        'random_directions':n_trials,
        'rows':rows,
        'fits':{str(order):float(rows[0][f'fit_rate_o{order}']) for order in [2,4]},
        'limiting_J_TT_leak':float(np.mean(jtt)),
        'limiting_discrete_D_TT_leak':'0',
        'note':'Flat link transport is identity, a true curved-space construction needs covariant Q-generated links'
    },
    'orientation_domain_coarsening':coarsening,
    'conclusion':'A fixed cubic-harmonic spin-3 intertwiner cannot become the O3-natural divergence by mere lattice refinement or an average that discards second moments. Q requires a genuine dynamical transport/derivative or IR suppression of the spin-3 operator.'
}
jsonfile=P/'tdg_q_bridge_spin3_resultats_2026_11_06.json'
jsonfile.write_text(json.dumps(res,ensure_ascii=False,indent=2),encoding='utf8')
print('SPIN3',json.dumps(res['spin3'],ensure_ascii=False))
print('OCT_TWIRL',json.dumps(res['octahedral_twirling'],ensure_ascii=False))
print('SO3_TWIRL',json.dumps(res['haar_SO3_twirling'],ensure_ascii=False))
print('DISCRETE_DIVERGENCE')
for row in rows:print(row)
print('COARSENING',coarsening)
print('VERIFIED',jsonfile)
