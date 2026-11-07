"""TDG laboratory: a working GR benchmark + quantitative fault-isolation for the TDG l=2 -> l=1 channel.

This code does NOT derive GR from TDG's microscopic Q. It builds a known-GR benchmark
(linearized TT dynamics + exact Kasner vacuum) and asks which TDG obstruction
prevents identification with the benchmark. TDG historical J is modeled on a
canonical STF(3)->R^3 representative, conditional on the physical identification.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as sp
from numpy.linalg import norm, matrix_rank
from scipy.linalg import null_space, expm
from scipy.integrate import solve_ivp

OUT=Path('/mnt/data')
SQ=np.sqrt

def eij(i,j):
    a=np.zeros((3,3));a[i,j]=1;return a
E=np.array([
    np.diag([1.,-1.,0.])/SQ(2),
    np.diag([1.,1.,-2.])/SQ(6),
    (eij(0,1)+eij(1,0))/SQ(2),
    (eij(0,2)+eij(2,0))/SQ(2),
    (eij(1,2)+eij(2,1))/SQ(2)
]);
assert norm(np.einsum('aij,bij->ab',E,E)-np.eye(5))<1e-14

def representation(R):
    rotated=np.einsum('ia,bac,jc->bij', R,E,R)
    return np.einsum('aij,bij->ab',E,rotated)

def D(k):
    return np.einsum('aij,j->ia',E,k)

# Historical canonical S4 ray J = -(1/sqrt3)[yz->x, xz->y, xy->z]
J=np.zeros((3,5)); J[0,4]=J[1,3]=J[2,2]=-1/SQ(3)
c_inf=10.769201
Jphysical=c_inf*J
kz=np.array([0.,0.,1.]); D_z=D(kz); TT=null_space(D_z, rcond=1e-12)
assert TT.shape==(5,2)
assert norm(D_z@TT)<1e-13
assert matrix_rank(J)==3 and matrix_rank(D_z)==3

# Intersection dim of kernels = 5-rank([J;D_z])
intersection_dim=5-matrix_rank(np.vstack([D_z,J]))
leak_TT=J@TT
leak_TT_norm=float(norm(leak_TT))
TT_basis_wave=np.column_stack([np.array([1.,0.,0.,0.,0.]),np.array([0.,0.,1.,0.,0.])])
assert norm(D_z@TT_basis_wave)<1e-13
assert norm(TT@TT.T-TT_basis_wave@TT_basis_wave.T)<1e-13

# Tensor-vector SO3 covariance: D_(Rk) U5(R) = R D_k.
rng=np.random.default_rng(20261106)
rotation_defects=[]; J_cov_defects=[]; J_D_overlap=[]; J_TT_leaks=[]; J_TT_kernel_dims=[]
for _ in range(300):
    X=rng.normal(size=(3,3)); R,_=np.linalg.qr(X)
    if np.linalg.det(R)<0:R[:,0]*=-1
    U=representation(R)
    kk=rng.normal(size=3); kk/=norm(kk)
    rotation_defects.append(float(norm(D(R@kk)@U-R@D(kk))))
    J_cov_defects.append(float(norm(R@J@U.T-J)/norm(J)))
    J_D_overlap.append(float(np.sum(J*D(kk))))
    J_TT_leaks.append(float(norm(J@null_space(D(kk),rcond=1e-12))/norm(J)))
    J_TT_kernel_dims.append(5-matrix_rank(np.vstack([D(kk),J])))
max_gradient_cov=float(max(rotation_defects))
median_j_defect=float(np.median(J_cov_defects))

# Best fit D_k: J is exactly Frobenius-orthogonal to all D_ei.
F=np.column_stack([D(np.eye(3)[i]).reshape(-1) for i in range(3)])
fit=np.linalg.lstsq(F,J.reshape(-1),rcond=None)[0]
best_fit_relative=float(norm(F@fit-J.reshape(-1))/norm(J))

# The full octahedral group gives a finite exactly symmetric twirl for this J.
rotations=[]
for perm in itertools.permutations(range(3)):
    P=np.eye(3)[:,perm]
    for signs in itertools.product([-1.,1.],repeat=3):
        R=P@np.diag(signs)
        if round(np.linalg.det(R))==1:
            rotations.append(R)
assert len(rotations)==24
Jrot=np.stack([R@J@representation(R).T for R in rotations])
twirl_mean=Jrot.mean(axis=0)
twirl_norm=float(norm(twirl_mean))
twirl_second_moment=float(np.mean([norm(x)**2 for x in Jrot]))
assert abs(twirl_second_moment-norm(J)**2)<1e-12

# Linearized GR TT harmonic oscillator (per one |k|, physical modes = + and x).
omega=1.7
q_init=np.array([0.8,0.3]); p_init=np.array([0.4,-0.2])
energies=[];divergence=[];tt_norm_pres=[];full_j_drive=[]
for t in np.linspace(0.,30.,601):
    qs=q_init*np.cos(omega*t)+p_init*np.sin(omega*t)/omega
    ps=-q_init*omega*np.sin(omega*t)+p_init*np.cos(omega*t)
    h=TT_basis_wave@qs; mom=TT_basis_wave@ps
    energies.append(0.5*(ps@ps+omega*omega*(qs@qs)))
    divergence.append(norm(D_z@h))
    tt_norm_pres.append(norm(h-TT_basis_wave@(TT_basis_wave.T@h)))
    full_j_drive.append(norm(Jphysical@h))
energy_delta_rel=float((max(energies)-min(energies))/np.mean(energies))

# Exact nonlinear Kasner vacuum: g=-dt²+t^(2p1)dx²+... ; R_mu_nu=0 and curvature !=0
# Bianchi I: analytical Ricci formula checked directly from Christoffel symbols.
t=sp.symbols('t',positive=True)
p=[-sp.Rational(1,3), sp.Rational(2,3), sp.Rational(2,3)]
gdiag=[-sp.Integer(1)]+[t**(2*pi) for pi in p]
invdiag=[1/x for x in gdiag]
# Geometry depends only on x^0=t, making derivatives exact and cheap.
Gamma=sp.MutableDenseNDimArray.zeros(4,4,4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            # Gamma^a_bc = 1/2 g^aa (delta_b0 delta_ca d_t g_aa + delta_c0 delta_ba d_t g_aa - delta_a0 delta_bc d_t g_bb)
            expr=0
            if b==0 and c==a:expr+=sp.diff(gdiag[a],t)
            if c==0 and b==a:expr+=sp.diff(gdiag[a],t)
            if a==0 and b==c:expr-=sp.diff(gdiag[b],t)
            Gamma[a,b,c]=sp.simplify(invdiag[a]*expr/2)
Ricci=sp.zeros(4,4)
for mu in range(4):
  for nu in range(4):
    R=0
    for r in range(4):
        if r==0:R+=sp.diff(Gamma[r,mu,nu],t)
        if nu==0:R-=sp.diff(Gamma[r,mu,r],t)
        for s in range(4):
            R+=Gamma[r,r,s]*Gamma[s,mu,nu]-Gamma[r,nu,s]*Gamma[s,mu,r]
    Ricci[mu,nu]=sp.simplify(R)
assert Ricci==sp.zeros(4)

def Riemann(a,b,c,d):
    # R_abcd = g_aa R^a_bcd, diagonal g
    R1=sp.diff(Gamma[a,b,d],t) if c==0 else 0
    R2=sp.diff(Gamma[a,b,c],t) if d==0 else 0
    for lam in range(4):
        R1+=Gamma[a,c,lam]*Gamma[lam,b,d]
        R2+=Gamma[a,d,lam]*Gamma[lam,b,c]
    return sp.simplify(gdiag[a]*(R1-R2))
R_0101=Riemann(0,1,0,1)
R_0202=Riemann(0,2,0,2)
assert R_0101!=0 and R_0202!=0
kretsch=sp.simplify(4*(sum((pi*(pi-1))**2 for pi in p)+sum(p[i]**2*p[j]**2 for i in range(3) for j in range(i+1,3)))/t**4)
assert sp.simplify(kretsch-64/(27*t**4))==0
constraint=sp.simplify((sum(p))**2-sum(pi**2 for pi in p))
assert constraint==0

# B5 pure-trace correction (independently documented) cannot change a tracefree tensor.
B5_tensor_action_norm=float(max(norm((15/4)*np.trace(X)*np.eye(3)) for X in E))
assert B5_tensor_action_norm<1e-13

# Memory/decoherence as classical-record interface, not as gravity law.
# Pure dephasing channel E_eta preserves diagonal probabilities but loses coherences.
gamma=0.8; timepoints=[0,1,2,4,8,16]
coherence=[float(np.exp(-gamma*v)) for v in timepoints]
# two valid Kraus operators K0/K1 implement this completely positive trace-preserving map.
eta=coherence[2]
I=np.eye(2,dtype=complex);Z=np.diag([1,-1]).astype(complex)
K0=np.sqrt((1+eta)/2)*I
K1=np.sqrt((1-eta)/2)*Z
rho=np.array([[.5,.5],[.5,.5]],dtype=complex)
rho_after=K0@rho@K0.conj().T+K1@rho@K1.conj().T
assert abs(np.trace(rho_after)-1)<1e-13
assert min(np.linalg.eigvalsh(rho_after))>=-1e-14
assert abs(rho_after[0,0]-0.5)<1e-14
assert abs(rho_after[0,1]-eta/2)<1e-14

# Fault injection: TDG-J drives a spurious vector channel; gradient D_k does not drive it on TT waves.
# This is a controlled diagnostic ODE, NOT an actual microscopic TDG evolution equation.
nu=0.7

def qwave(tt):
    return q_init*np.cos(omega*tt)+p_init*np.sin(omega*tt)/omega

def drive(tt, map3x5):
    return c_inf*map3x5@(TT_basis_wave@qwave(tt))

def integrate_fault(M):
    sol=solve_ivp(lambda tt,v: -nu*v+drive(tt,M),[0,30],[0.,0.,0.],rtol=1e-11,atol=1e-13,dense_output=True)
    assert sol.success
    grid=np.linspace(0,30,601)
    v=sol.sol(grid)
    return float(np.max(np.linalg.norm(v,axis=0))),float(np.linalg.norm(v[:,-1])),[float(v[i,-1]) for i in range(3)]
J_max,J_last,J_vector=integrate_fault(J)
D_max,D_last,D_vector=integrate_fault(D_z)
assert D_max<1e-10 and J_max>0.1

# Full finite R spatial gauge compact rotations cannot eliminate the fluctuating J strength.
# For any orientation, ||R J U(R)^T||_F = ||J||_F, independent of twirl mean.

# Quantum Zeno benchmark: monitor the physical TT subspace; do NOT claim
# the monitoring projectors are already generated by TDG.
H=np.zeros((8,8),dtype=complex)
H[:5,:5]=1.7*np.eye(5)
H[5:,5:]=1.2*np.eye(3)
H[5:,:5]=1.0*J
H[:5,5:]=1.0*J.T
Ptt=np.zeros((8,8),dtype=complex);Ptt[:5,:5]=TT@TT.T
P5=np.diag([1.]*5+[0.]*3).astype(complex)
psi0=np.zeros(8,dtype=complex);psi0[2]=1.
zeno_stats=[];Tobs=6.
for n in [1,2,5,10,20,50,100,500,1000,2000]:
    A=expm(-1j*H*Tobs/n)
    # each P corresponds to a successful constraint-compatible measurement.
    psi_tt=psi0.copy();psi_tensor=psi0.copy()
    for j in range(n):
        psi_tt=Ptt@A@psi_tt
        psi_tensor=P5@A@psi_tensor
    zeno_stats.append({"N":n,"TT_success_probability":float(np.vdot(psi_tt,psi_tt).real),"tensor5_success_probability":float(np.vdot(psi_tensor,psi_tensor).real)})
assert zeno_stats[-1]['TT_success_probability']>0.99

result={
"scope":"Known-GR benchmark and diagnostic comparison, not microscopic GR-from-TDG derivation",
"source":{"url":"https://github.com/jonathanduchesne-lab/TDG/blob/main/checkpoints/SENTRY/2026-09-18/TDG_FORMAL_READOUT_FREE_DYNAMIC_L2_TO_L1_NONZERO_2026-09-18.md","status":"Historical canonical J ray assumed to map to physical STF(3)->vector; identification is conditional"},
"gr_linearized":{"tt_dimension":int(TT.shape[1]),"constraint_divergence_max":float(max(divergence)),"energy_relative_variation":energy_delta_rel,"tt_projection_error_max":float(max(tt_norm_pres)),"max_J_source_on_gr_wave":float(max(full_j_drive))},
"gr_nonlinear":{"kasner_exponents":[str(v) for v in p],"ricci_matrix":[[str(Ricci[i,j]) for j in range(4)] for i in range(4)],"hamiltonian_constraint":str(constraint),"riemann_0101":str(R_0101),"riemann_0202":str(R_0202),"kretschmann":str(kretsch)},
"B5_trace_test":{"maximum_action_on_STF_basis":B5_tensor_action_norm,"interpretation":"scalar rank-one correction has zero STF action by type, irrespective of fitted coefficient"},
"tdg_J_test":{"J_matrix":J.tolist(),"rank_J":int(matrix_rank(J)),"rank_divergence_kz":int(matrix_rank(D_z)),"kernel_TT":int(TT.shape[1]),"intersection_TT_kerJ":int(intersection_dim),"J_TT_fro_norm":leak_TT_norm,"J_TT_relative_to_J_norm":float(leak_TT_norm/norm(J)),"J_divergence_best_fit_relative_error":best_fit_relative,"J_divergence_best_fit_k":fit.tolist(),"max_gradient_covariance_defect":max_gradient_cov,"median_J_rotation_defect_relative":median_j_defect,"min_J_rotation_defect_relative":float(min(J_cov_defects)),"max_J_rotation_defect_relative":float(max(J_cov_defects)),"octahedral_twirl_mean_norm":twirl_norm,"octahedral_twirl_single_orientation_mean_square":twirl_second_moment,"mean_relative_TT_leak_over_k":float(np.mean(J_TT_leaks)),"joint_kernel_dimensions_300_generic_k":sorted(set(int(d) for d in J_TT_kernel_dims)),"J_coefficient_formal_inf":c_inf,"J_D_orthogonality_max":float(max(abs(v) for v in J_D_overlap))},
"zeno_comparison":{"comment":"Conditional sequence of successful projective constraint checks; TT projector imported from GR, not TDG-derived", "total_time":Tobs,"coupling_strength":1.0,"measurements":zeno_stats},
"fault_injection":{"equation":"dv/dt=-nu*v+c_inf*(J or D_k)*h_TT(t)","scope":"diagnostic only, not frozen Q process", "nu":nu,"TDG_J_max_vector_norm":J_max,"TDG_J_final_vector_norm":J_last,"GR_Dk_max_vector_norm":D_max,"GR_Dk_final_vector_norm":D_last,"intervention":"replace fixed J by covariant divergence D_k; requires new Q-derived law"},
"decoherence":{"gamma":gamma,"times":timepoints,"offdiagonal_visibility":coherence,"t2_probability_0":float(rho_after[0,0].real),"t2_offdiagonal":float(rho_after[0,1].real),"born_selector_imported":True}
}
path=OUT/'tdg_machine_etalon_resultats_2026_11_06.json';path.write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
print('=== WORKING MACHINE / BENCHMARK ===')
for section,values in result.items():
  print(section,values if not isinstance(values,dict) else json.dumps(values,ensure_ascii=False)[:2300])
print('VERIFIED',path)
