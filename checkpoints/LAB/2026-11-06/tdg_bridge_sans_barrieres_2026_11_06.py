#!/usr/bin/env python3
"""Sandbox TDG bridge experiment, November 2026.

WARNING: This is NOT the full TDG Q-B1852 or MRP9B code.
It tests precise candidate extensions using the documented B5 tensor types,
SU2 obstruction rank, two TT modes, and known exact GR identities.
No existing TDG code or repository is modified.
"""
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
from numpy.linalg import norm, matrix_rank, svd
from scipy.linalg import expm

OUT=Path(__file__).resolve().parent
rng=np.random.default_rng(20261106)
TOL=1e-10

def vec_to_stf(v):
    a,b,c,d,e = v
    return np.array([[a+b/math.sqrt(3),c,d],
                     [c,-a+b/math.sqrt(3),e],
                     [d,e,-2*b/math.sqrt(3)]], dtype=float)

# A. The exact *type* of the retained l=2 -> l=1 obstacle.
# This is a canonical rank-3 diagnostic on STF_2, not the actual TDG Q matrix.
n=np.array([0.,0.,1.])
B=np.column_stack([vec_to_stf(np.eye(5)[k])@n for k in range(5)])
assert matrix_rank(B)==3
B5trace=(15/4)*np.outer(np.eye(3).reshape(-1)/math.sqrt(3),
                         np.eye(3).reshape(-1)/math.sqrt(3))
trace_on_STF=max(norm(B5trace @ vec_to_stf(np.eye(5)[k]).reshape(-1)) for k in range(5))
assert trace_on_STF < TOL
# Scalar-only modifications cannot correct the 3x5 STF->vector block.
alpha=11.6773  # historical magnitude, NOT a normalized Q-native matrix
A=alpha*B
singular=svd(A,compute_uv=False)
cterm=-A
assert norm(A+cterm)<TOL
assert matrix_rank(cterm)==3

# If the preferred n is promoted to a transforming field, T n is equivariant.
v=np.array([0.5,-0.1,0.7,-0.3,0.25])
T=vec_to_stf(v)
axis=rng.normal(size=3)
axis/=norm(axis)
angle=0.89
cross=np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
R=expm(angle*cross)
assert norm(R.T@R-np.eye(3))<TOL
eq_cov=norm((R@T@R.T)@(R@n)-R@(T@n))
fixed_dir_failure=norm((R@T@R.T)@n - R@(T@n))
assert eq_cov<TOL and fixed_dir_failure>1e-4
# Isotropic averaging vanishes only in the first moment; fluctuations survive.
Ns=60000
unit=rng.normal(size=(Ns,3))
unit/=norm(unit,axis=1)[:,None]
responses=unit@T.T
emp_mean=responses.mean(axis=0)
emp_mean_square=np.mean(np.sum(responses**2,axis=1))
expected_mean_square=norm(T,ord='fro')**2/3
assert abs(emp_mean_square-expected_mean_square)/expected_mean_square<0.02

# B. Actually build the missing rank-3 internal rotation gauge capacity.
# Canonical cotriad phase space (E,P) with 9+9 local components.
# This new cotriad sector was NOT produced by frozen Q.
E=np.array([[1.20,0.05,-0.08],[0.10,1.10,0.07],[0.03,-0.02,0.95]])
pi0=np.array([[0.16,-0.07,0.08],[-0.07,-0.09,0.05],[0.08,0.05,0.11]])
P=2*E@pi0
h=E.T@E
pi_rec=0.5*np.linalg.inv(E)@P
Gmatrix=P@E.T-E@P.T
assert norm(Gmatrix)<TOL and norm(pi_rec-pi0)<TOL

Er=R@E
Pr=R@P
hr=Er.T@Er
pir=0.5*np.linalg.inv(Er)@Pr
frame_metric_error=norm(hr-h)
frame_pi_error=norm(pir-pi0)
assert frame_metric_error<TOL and frame_pi_error<TOL
# Pullback of canonical one-form on the Gauss slice:
dE=rng.normal(size=(3,3))*.09
dh=dE.T@E+E.T@dE
oneform_E=float(np.sum(P*dE))
oneform_h=float(np.sum(pi0*dh))
oneform_error=abs(oneform_E-oneform_h)
assert oneform_error<TOL

# Angular-momentum moment map G_a=sum_i epsilon_abc E_bi P_ci.
eps=np.zeros((3,3,3),dtype=float)
for a in range(3):
 for b in range(3):
  for c in range(3):
   eps[a,b,c]=float(sp.LeviCivita(a,b,c))

def gauss(E,P):
    return np.einsum('abc,bi,ci->a',eps,E,P)

def gauss_grad(E,P):
    gE=np.einsum('adc,ci->adi',eps,P)
    gP=np.einsum('abd,bi->adi',eps,E)
    return gE,gP
# Test the algebra at a generic (off-shell) phase-space point.
Pg=rng.normal(size=(3,3))
G=gauss(E,Pg)
dGE,dGP=gauss_grad(E,Pg)
PB=np.einsum('adi,bdi->ab',dGE,dGP)-np.einsum('adi,bdi->ab',dGP,dGE)
expected_PB=np.einsum('abc,c->ab',eps,G)
gauss_closure_error=norm(PB-expected_PB)
assert gauss_closure_error<TOL
# Verify internal SO3 orbits are genuinely 3-dimensional for invertible triads.
orbit=np.column_stack([(np.array([[0,-1,0],[1,0,0],[0,0,0]])@E).reshape(-1),
                       (np.array([[0,0,1],[0,0,0],[-1,0,0]])@E).reshape(-1),
                       (np.array([[0,0,0],[0,0,-1],[0,1,0]])@E).reshape(-1)])
gauss_orbit_rank=matrix_rank(orbit)
assert gauss_orbit_rank==3
# Remaining 18 - 2*3 Gauss - 2*4 ADM = 4 dimensional reduced phase space.
local_reduced_phase_dimension=18-2*3-2*4
assert local_reduced_phase_dimension==4

# C. A concrete exact nonlinear Einstein vacuum family with two profiles.
# These are generic u-dependent amplitudes, not prescribed by Q.
u,vx,x,y=sp.symbols('u v x y',real=True)
f=sp.Function('f')(u)
g=sp.Function('g')(u)
H=f*(x*x-y*y)+2*g*x*y
coords=(u,vx,x,y)
gcov=sp.Matrix([[H,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
ginv=gcov.inv()
assert gcov.det()==-1
# Connection Gamma^rho_{mu nu}
Gam=[[[sp.simplify(sp.Rational(1,2)*sum(
    ginv[rho,s]*(sp.diff(gcov[s,nu],coords[mu])+sp.diff(gcov[s,mu],coords[nu])
                -sp.diff(gcov[mu,nu],coords[s])) for s in range(4)))
    for nu in range(4)] for mu in range(4)] for rho in range(4)]
# R_{mu nu}=partial_rho Gamma^rho_{mu nu}-partial_nu Gamma^rho_{mu rho}
# +Gamma^rho_{rho sigma}Gamma^sigma_{mu nu}-Gamma^rho_{nu sigma}Gamma^sigma_{mu rho}
Ric=sp.MutableDenseMatrix.zeros(4)
for mu in range(4):
 for nu in range(4):
  z=0
  for rho in range(4):
   z+=sp.diff(Gam[rho][mu][nu],coords[rho])-sp.diff(Gam[rho][mu][rho],coords[nu])
   for sig in range(4):
    z+=Gam[rho][rho][sig]*Gam[sig][mu][nu]-Gam[rho][nu][sig]*Gam[sig][mu][rho]
  Ric[mu,nu]=sp.simplify(z)
ricci_is_zero=all(sp.simplify(Ric[mu,nu])==0 for mu in range(4) for nu in range(4))
assert ricci_is_zero
# Generic spacetime NOT flat: R_{uxux}=-f, R_{uxuy}=-g, R_{uyuy}=+f.
# Compute one (nonzero) Riemann component by differentiating Gamma.
def riemann_up(rho,sigma,mu,nu):
    z=sp.diff(Gam[rho][nu][sigma],coords[mu])-sp.diff(Gam[rho][mu][sigma],coords[nu])
    for lam in range(4):
        z+=Gam[rho][mu][lam]*Gam[lam][nu][sigma]-Gam[rho][nu][lam]*Gam[lam][mu][sigma]
    return sp.simplify(z)
def riemann_down(a,b,c,d):
    return sp.simplify(sum(gcov[a,r]*riemann_up(r,b,c,d) for r in range(4)))
Ruxux=riemann_down(0,2,0,2)
Ruxuy=riemann_down(0,2,0,3)
Ruyuy=riemann_down(0,3,0,3)
assert sp.simplify(Ruxux+f)==0
assert sp.simplify(Ruxuy+g)==0
assert sp.simplify(Ruyuy-f)==0
# Exact full curvature, not just approximate weak-field waves.

# D. A specific exploratory law to switch beta on using decoherence records.
# This is BY HAND (NOT derived from Q), included to see what it can do.
c=math.cos(.7)
assumed_beta={str(k):float(1-c**k) for k in [0,1,2,4,8,16,32,128]}
assert abs(1-assumed_beta['128'])<1e-12
# The scalar switch still cannot affect a traceless sector.

# E. Can the familiar decoherence dynamics suppress the STF->vector leak by a
# continuous-measurement (Zeno) effect, WITHOUT manually adding -A?
# This is a toy Hamiltonian sharing only the 5+3 tensor types with real Q.
from scipy.linalg import expm as matrix_expm
D=8
A_norm=B/norm(B,ord=2)
Hmix=np.zeros((D,D))
Hmix[:3,3:]=A_norm
Hmix[3:,:3]=A_norm.T
# Free internal tensor evolution is left untouched by sector monitoring.
Hmix[:3,:3]=-.19*np.eye(3)
Hmix[3:,3:]=.13*np.eye(5)
PV=np.diag([1.]*3+[0.]*5)
PT=np.eye(D)-PV
vec0=np.zeros(D);vec0[6]=1.  # STF xz state, coupled to the vector sector
rho0=np.outer(vec0,vec0)

# vec(AXB)=(B^T tensor A)vec(X), Fortran vector order.
H_super=-1j*(np.kron(np.eye(D),Hmix)-np.kron(Hmix.T,np.eye(D)))
D_super=(np.kron(PV,PV)+np.kron(PT,PT)-np.eye(D*D))
# The block projectors are invariant under SO3. Build exact l=2 action.
from scipy.linalg import block_diag
basis_stf=[vec_to_stf(np.eye(5)[j])/math.sqrt(2) for j in range(5)]
D2=np.array([[np.sum(basis_stf[i]*(R@basis_stf[j]@R.T))
              for j in range(5)] for i in range(5)])
assert norm(D2.T@D2-np.eye(5))<TOL
Urot=block_diag(R,D2)
assert norm(Urot@PV-PV@Urot)<TOL
rho0rot=Urot@rho0@Urot.T
zeno=[]
for gamma in [0.,1.,5.,20.,100.,500.]:
    prop=matrix_expm(H_super+gamma*D_super)
    rho_t=(prop@rho0.reshape(-1,order='F')).reshape((D,D),order='F')
    rho_rot=(prop@rho0rot.reshape(-1,order='F')).reshape((D,D),order='F')
    rotation_defect=float(norm(rho_rot-Urot@rho_t@Urot.T))
    rho_t=(rho_t+rho_t.conj().T)/2
    leakage=float(np.trace(PV@rho_t).real)
    assert abs(np.trace(rho_t)-1)<2e-9
    assert np.linalg.eigvalsh(rho_t).min()>-1e-8
    zeno.append({'monitor_rate':gamma,'vector_leakage_at_time_1':leakage,'SO3_state_covariance_defect_at_time_1':rotation_defect})
assert zeno[0]['vector_leakage_at_time_1']>0.1
assert zeno[-1]['vector_leakage_at_time_1']<0.01
assert zeno[-1]['SO3_state_covariance_defect_at_time_1'] < .02

# Crucial noncommuting limit: at any finite monitoring rate, time -> infinity
# in a connected two-state model gives an equal classical mixture (1/2,1/2),
# so this is not an automatic fundamental constraint.
h2=np.array([[0.,1.],[1.,0.]])
p0=np.diag([1.,0.]);p1=np.diag([0.,1.]);ii=np.eye(2)
Li2=-1j*(np.kron(ii,h2)-np.kron(h2.T,ii))
Li2_D=np.kron(p0,p0)+np.kron(p1,p1)-np.eye(4)
rho_init2=np.diag([1.,0.]).reshape(-1,order='F')
rho2=(matrix_expm(100*(Li2+5.*Li2_D))@rho_init2).reshape((2,2),order='F')
long_time_leakage=float(np.real(rho2[1,1]))
assert abs(long_time_leakage-.5)<1e-8

# Zeno non-commuting macroscopic-time versus monitoring limit, exact two-state formula.
def two_level_leakage(gamma,time,g_coupling=1.):
    # z'' + gamma*z' + 4*g^2*z=0; z(0)=1,z'(0)=0.
    disc=math.sqrt(gamma*gamma-16*g_coupling*g_coupling)
    z=((gamma+disc)/(2*disc))*math.exp((disc-gamma)*time/2) \
      +((disc-gamma)/(2*disc))*math.exp((-gamma-disc)*time/2)
    return (1-z)/2
zeno_double_scaling=[]
for gamma in [20.,100.,500.,1000.]:
    zeno_double_scaling.append({
      'monitor_rate':gamma,
      'fixed_time_1_leak':two_level_leakage(gamma,1.),
      'time_equals_monitor_rate_leak':two_level_leakage(gamma,gamma)
    })
assert zeno_double_scaling[-1]['fixed_time_1_leak']<.003
assert abs(zeno_double_scaling[-1]['time_equals_monitor_rate_leak']
           - .5*(1-math.exp(-4)))<.001

# F. Does decoherence alone enforce a C0=0 B5 scalar restriction?
# A two-level scalar (forbidden) vs allowed record is enough for a no-go.
# Pure dephasing only kills coherence, not scalar population.
scalar_initial_population=.4
scalar_after_dephase=scalar_initial_population
# Non-unital amplitude damping can remove scalar population, but it is an
# independently specified, dissipative constitutive interaction.
scalar_after_amplitude_damping={str(t):scalar_initial_population*math.exp(-3*t)
                                for t in [0,0.5,1.,2.,5.]}
assert scalar_after_dephase==.4
assert scalar_after_amplitude_damping['5.0']<1.5e-7

result={
 'sources':{
  'TDG':'jonathanduchesne-lab/TDG, CURRENT_FRONT_LATEST.md and 2026-10-06 B5 v0.3/v0.4 branch stop',
  'scope':'toy representation tests + exact canonical triad kinematics + exact vacuum pp wave, NOT original Q-MRP9B dynamics'},
 'obstruction':{
  'Q_historical_STF_gradient_magnitude_about':alpha,
  'diagnostic_rank':int(matrix_rank(A)),
  'diagnostic_singular_values':singular.tolist(),
  'exact_B5_trace_to_STF_error':float(trace_on_STF),
  'exact_cancellation_if_counterterm_minus_A':float(norm(A+cterm)),
  'counterterm_required_rank_at_least':int(matrix_rank(A)),
  'dynamical_direction_SO3_covariance_error':float(eq_cov),
  'fixed_direction_SO3_covariance_failure':float(fixed_dir_failure),
  'orientation_average_first_moment_norm':float(norm(emp_mean)),
  'orientation_average_mean_square':float(emp_mean_square),
  'orientation_average_mean_square_exact':float(expected_mean_square)
 },
 'cotriad_gauss_completion':{
  'new_assumption':'independent invertible 3x3 triad with canonical momentum; physical metrics are E.T E',
  'metric_rotation_error':float(frame_metric_error),
  'momentum_rotation_error':float(frame_pi_error),
  'canonical_oneform_error':float(oneform_error),
  'gauss_algebra_error':float(gauss_closure_error),
  'gauss_orbit_rank':int(gauss_orbit_rank),
  'phase_dimensions':{'raw':18,'after_three_Gauss':12,'after_four_ADM':4,'config_degrees_freedom':2},
  'HDA':'Requires adopting ADM Hamiltonian/diffeomorphism constraints as NEW input; not derived from Q'
 },
 'exact_gr_sector':{
  'metric':'ds^2 = -2 du dv + dx^2+dy^2 + H(u,x,y) du^2',
  'H':'f(u)*(x^2-y^2)+2*g(u)*x*y',
  'det_g':str(gcov.det()),
  'Ricci_tensor':str(Ric),
  'Ricci_zero_for_arbitrary_f_g':bool(ricci_is_zero),
  'R_uxux':str(Ruxux),'R_uxuy':str(Ruxuy),'R_uyuy':str(Ruyuy),
  'classification':'Exact nonlinear vacuum Einstein family, but f(u),g(u) are NOT output by TDG Q'
 },
 'decoherence_Zeno_exploration':{
  'monitoring_t1':zeno,
  'noncommuting_limits_exact_two_level':zeno_double_scaling,
  'finite_rate_long_time_2state_leakage':long_time_leakage,
  'interpretation':'Strong monitoring suppresses cross-sector transitions only at fixed time if gamma->infinity. At finite gamma and time->infinity leakage can return.'
 },
 'dephasing_vs_constraint':{
  'initial_scalar_population':scalar_initial_population,
  'after_arbitrarily_strong_unselective_dephasing':scalar_after_dephase,
  'after_hand_added_amplitude_damping':scalar_after_amplitude_damping,
  'interpretation':'Decoherence alone does not set C0=0; amplitude damping requires new physical coupling.'
 },
 'memory_beta_ansatz':{
  'beta_N_equals_1_minus_absolute_coherence':assumed_beta,
  'status':'Assumed constitutive law, not derived, affects scalar only, does not solve STF or HDA'
 },
 'open':['Q-to-(E,P) physical map satisfying symplectic and quotient descent',
         'Q-derived first class Gauss law rather than new sector',
         'Q-derived ADM constraints and their HDA closure',
         'coupled quantum record backreaction and Born/unique result',
         'cofinality/refinement and all local observables']
}
(OUT/'tdg_bridge_sans_barrieres_resultats.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('A: STF->vector diagnostic rank:',matrix_rank(A),'singular values',singular)
print('A: B5 trace correction STF residual:',trace_on_STF)
print('A: rotating direction covariance error:',eq_cov,'fixed-background failure:',fixed_dir_failure)
print('A: direction average mean square measured:',emp_mean_square,'expected:',expected_mean_square)
print('B: triad metric gauge error:',frame_metric_error,'canonical oneform error:',oneform_error)
print('B: Gauss bracket error:',gauss_closure_error,'Gauss rank:',gauss_orbit_rank,'physical DOF:',local_reduced_phase_dimension//2)
print('C: Exact nonlinear Einstein Ricci=0:',ricci_is_zero,'R_uxux:',Ruxux,'R_uxuy:',Ruxuy,'R_uyuy:',Ruyuy)
print('D: Beta(memory) test:',assumed_beta)
print('E: Zeno monitoring numerical sweep:',zeno)
print('E: finite-rate long-time leakage tends:',long_time_leakage)
print('E: monitoring/time double scaling:',zeno_double_scaling)
print('F: Scalar population unchanged by pure dephasing:',scalar_after_dephase,'amplitude damping:',scalar_after_amplitude_damping)
print('VERDICT: Conditional bridge exists in exact GR wave sector after adding a triad/ADM law; no Q-derived GR bridge proved.')
