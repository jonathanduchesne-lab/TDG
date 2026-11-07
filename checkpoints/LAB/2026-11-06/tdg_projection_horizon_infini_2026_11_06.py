#!/usr/bin/env python3
"""TDG projection d'une lentille de decoherence sur l'horizon N -> infinity.

This is a target-blind asymptotic stress test, not a microscopic TDG/Q numerical
rerun or a derivation of gravitational field equations. No canonical TDG source
files or source repository are modified.

Verified parent:
  tdg_lentille_decoherence_2026_11_06.py
  TDG CURRENT_FRONT_LATEST.md; B5 v0.3/v0.4; B5-to-GR stop checkpoint.

Four distinct limits are tested:
  A: indefinitely many environment fragments for a two-path system;
  B: repeated S6-covariant completely positive instrument on B5 Standard5;
  C: refinement limit a -> 0 against number of interactions N -> infinity;
  D: spectator/trace type firewalls for the retained STF obstruction.
"""
import json
import math
from pathlib import Path
import numpy as np
from numpy.linalg import norm, eigvalsh

HERE = Path(__file__).resolve().parent
TOL = 5e-11


def h2(p):
    if p <= 1e-15 or p >= 1 - 1e-15:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def information_of_fragment(overlap, m):
    # Equiprobable pure binary record states. Helstrom readout mutual info.
    q = abs(overlap) ** m
    p_err = (1 - math.sqrt(max(0., 1 - q * q))) / 2
    return 1 - h2(p_err)


# A. Nonselective two-path decoherence, all interactions unitary before
#    tracing the environment. Equal path priors.
theta = .7
c = math.cos(theta)
assert 0 < c < 1
n_values = [0, 1, 2, 4, 8, 16, 32, 64, 128, 1024]
records = []
for n in n_values:
    visibility = c ** n
    rho = np.array([[.5, .5 * visibility], [.5 * visibility, .5]])
    rho_infty = np.eye(2) / 2
    assert abs(np.trace(rho) - 1) < TOL
    assert np.min(eigvalsh(rho)) > -TOL
    records.append({
        "N": n, "visibility": float(visibility),
        "trace_distance_to_classical_mixture": float(abs(visibility)/2),
        "distance_to_branch0_at_infinity": .5 if n == n_values[-1] else None,
        "record_information_bits_optimal_m_fragment": information_of_fragment(c, n),
    })
# No stochastic outcome selected by the unconditioned limit.
limit = np.eye(2) / 2
branch0 = np.diag([1., 0.])
branch1 = np.diag([0., 1.])
trace_dist_to_each_branch = [sum(abs(eigvalsh(limit-b))) / 2 for b in (branch0, branch1)]
assert np.allclose(trace_dist_to_each_branch, [.5, .5])

m90 = next(m for m in range(1, 100) if information_of_fragment(c, m) >= .9)
redundancy = {str(n): n//m90 for n in (16, 32, 64, 128, 1024)}

# B. Repeated compatible instrument on the EXISTING certified B5 Standard5
#    quotient, as constructed in parent diagnostic. It is an illustrative
#    instrument, NOT a Q-derived microphysical B5 measurement dynamics.
I6 = np.eye(6)
u = np.ones(6)/math.sqrt(6)
P1 = np.outer(u, u)
P5 = I6-P1
L = 6*I6 - np.ones((6, 6))
assert norm(L - 6*P5) < TOL
M = [math.sqrt(6/5)*P5@np.outer(I6[:, j],I6[:, j])@P5 for j in range(6)]
assert norm(sum(k.T@k for k in M) - P5) < TOL

# Subspace dimension exactly five; find real orthonormal basis.
vals,U0 = np.linalg.eigh(P5)
U5 = U0[:, vals > .5]
assert U5.shape == (6, 5)
K = [U5.T@k@U5 for k in M]
superop = sum(np.kron(k, k) for k in K) # real vectorization
spectrum = np.sort(np.real_if_close(np.linalg.eigvals(superop)).real)
expected = np.sort(np.array([0.]*19+[.8]*5+[1.]))
assert norm(spectrum-expected) < TOL

rho0 = np.outer(P5[:,0],P5[:,0])
rho0 /= np.trace(rho0)
rho = rho0.copy()
stat = P5/5
err0 = norm(rho0-stat)
b5rows = []
current_n = 0
for n in [0, 1, 2, 4, 8, 16, 32, 64, 128]:
    for _ in range(n-current_n):
        rho = sum(k@rho@k.T for k in M)
    current_n = n
    assert norm(P1@rho) < TOL
    assert abs(np.trace(rho)-1)<TOL
    err = float(norm(rho-stat))
    b5rows.append({"iterations":n,"distance_to_P5_over_5":err,
                   "expected_for_this_initial_state":err0*(.8**n)})
    assert abs(err - err0*.8**n) < TOL
assert b5rows[-1]["distance_to_P5_over_5"] < 1e-10

# C. Weak interaction continuum scaling: theta(a)=sqrt(2g)*a.
#    N=round(T/a^2) gives exp(-g*T). N fixed -> 1. At each fixed a,
#    N->infinity -> 0. Thus the limiting operations do not commute.
g = .3
T = 1.
Nfixed=16
scales=[]
for a in [1/4, 1/8, 1/16, 1/32, 1/64]:
    overlap = math.cos(math.sqrt(2*g)*a)
    assert 0<overlap<1
    Ndiff=int(round(T/(a*a)))
    Nslow=int(round(T/a))
    Nfast=int(round(T/(a*a*a)))
    scales.append({
      "a":a,"N_fixed":Nfixed,"V_Nfixed":overlap**Nfixed,
      "N_slow":Nslow,"V_slow":overlap**Nslow,
      "N_diffusive":Ndiff,"V_diffusive":overlap**Ndiff,
      "N_fast":Nfast,"V_fast":overlap**Nfast,
    })
target = math.exp(-g*T)
assert abs(scales[-1]["V_diffusive"]-target) < 1e-5
assert scales[-1]["V_Nfixed"] > .99
assert scales[-1]["V_slow"] > .99
assert scales[-1]["V_fast"] < 1e-6

# D. TDG B5 pure trace correction is blind to STF, identically at all N.
E = np.eye(3)
e_id = E.reshape(-1)/math.sqrt(3)
Deltaw = (15/4)*np.outer(e_id, e_id)
STF=[]
for i in range(3):
    for j in range(i+1,3):
        X=np.zeros((3,3)); X[i,j]=X[j,i]=1/math.sqrt(2)
        STF.append(X.reshape(-1))
for diag in ([1,-1,0],[1,1,-2]):
    X = np.diag(diag).astype(float)
    X /= norm(X)
    STF.append(X.reshape(-1))
assert len(STF)==5
stf_error = max(norm(Deltaw @ v) for v in STF)
assert stf_error < TOL

# Using a separate record channel D and unaltered dynamic operator T,
# (D \otimes id)(id \otimes T)=(id \otimes T)(D \otimes id).
# This is a conditional mathematical firewall, not a full Q coupling test.
Ttoy = np.array([[1.,2.],[-1.,.5]])
Atoy = np.array([[.7,.3],[.2,.8]])
commutator_defect = norm(np.kron(Atoy,np.eye(2))@np.kron(np.eye(2),Ttoy)
                         -np.kron(np.eye(2),Ttoy)@np.kron(Atoy,np.eye(2)))
assert commutator_defect<TOL

result={
 "scope":"toy quantum long-time/continuum asymptotics + existing certified TDG B5 structural projector; no Q-MRP9B microscopic coupling",
 "initial_two_path":{"theta_radians":theta,"overlap":c,"rho_infinite":limit.tolist(),
   "infinite_trace_distance_to_either_definite_branch":trace_dist_to_each_branch,
   "environment_fragments_for_90pct_accessible_bit":m90,"redundancy":redundancy,
   "finite_horizon":records,
   "infinite_horizon":"visibility 0, effective improper mixture, no selected ontic outcome derived"},
 "B5_record_instrument":{"spectrum_of_25D_channel":spectrum.tolist(),
    "unique_fixed_state":"P5/5 within Standard5", "convergence_factor_after_first_step":.8,
    "distance_rows":b5rows,
    "physical_notice":"illustrative instrument is not a Q-native detector; discarding measurement outcomes erases sector information"},
 "continuum_double_scaling":{"g_assumed":g,"T":T,"target_exp_minus_gT":target,
   "scales":scales,
   "order_of_limits":{"N_infty_then_a_zero":"V=0",
     "a_zero_then_N_infty":"V=1", "N=T_over_a_squared":"V=exp(-gT)"},
   "notice":"a and g are illustrative, no calibration to TDG b4/b24 refinements"},
 "gravity_firewall":{"B5_pure_trace_on_STF_max_residual":float(stf_error),
  "spectator_tensor_commutator":float(commutator_defect),
  "historical_Q_obstruction":"STF->gradient nonzero ~11.6773; SAME-h ~0.74596 from existing TDG checkpoint, NOT recomputed here",
  "verdict":"no derived effect on GR obstruction from spectator lens, no GR improvement established"},
 "open":["Born rule not derived from TDG","individual outcome not selected by nonselective decoherence",
   "no physical threshold of absolute irreversibility", "no new beta!=0 B5 activation",
   "no MRP9B predictive-fibre chart nor microscopic Q coupling", "no universal foliation", "no nonlinear GR closure"],
}
path=HERE/'tdg_projection_horizon_infini_resultats.json'
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print("[A] local visibility N=16,32,128,1024",[(r['N'],r['visibility']) for r in records if r['N'] in [16,32,128,1024]])
print("[A] m(90% info)=",m90,"redundancy at N1024",redundancy['1024'])
print("[A] infinite reduced state",limit,"distance to each definite outcome",trace_dist_to_each_branch)
print("[B] B5 physical channel spectrum counts (0, 0.8, 1)=(19, 5, 1)")
print("[B] B5 long-time convergence",[(row['iterations'],row['distance_to_P5_over_5']) for row in b5rows])
print("[C] weak-coupling continuum exp(-gT)=",target)
for r in scales: print('a=',r['a'],'N=',r['N_diffusive'],'Vjoint=',r['V_diffusive'],'Vfixed=',r['V_Nfixed'],'Vslow=',r['V_slow'],'Vfast=',r['V_fast'])
print("[D] STF null response",stf_error,"spectator commutation",commutator_defect)
print("ALL ASSERTIONS PASS. JSON:",path)
