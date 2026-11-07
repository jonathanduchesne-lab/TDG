#!/usr/bin/env python3
"""TDG scientific decoherence lens: reproducible, non-invasive diagnostic.

Sources: TDG repository CURRENT_FRONT_LATEST.md and B5 v0.3/v0.4
(October 2026). This program does NOT claim to run the missing full Q-B1592
numerical chart or derive Born, objective collapse, beta coupling or GR.

Numerical tests:
  1. Microscopic two-path system + N environmental fragments (pure unitary).
  2. Recoherence vs incomplete access; accessible memory Holevo info.
  3. Bell-pair local instruments in either causal labeling order.
  4. A6-covariant record channel on verified B5 Standard-5 quotient.
  5. Independent TT spectator unchanged; pure-trace correction null on STF.
"""
import json
import math
from itertools import permutations
from pathlib import Path
import numpy as np
from numpy.linalg import eigvalsh, norm

OUT = Path(__file__).resolve().parent
EPS = 1e-11

def binary_entropy(p):
    if p < 1e-14 or p > 1 - 1e-14:
        return 0.0
    return -p*math.log2(p)-(1-p)*math.log2(1-p)

def holevo_for_m_fragments(c, m):
    # Equal-prior binary pure-state ensemble, overlap c**m.
    return binary_entropy((1+abs(c)**m)/2)

def accessible_info_helstrom(c, m):
    # For an equiprobable binary pure-state ensemble, the optimal Helstrom
    # binary measurement gives the accessible mutual information.
    overlap=abs(c)**m
    p_err=(1-math.sqrt(max(0.0,1-overlap*overlap)))/2
    return 1-binary_entropy(p_err)

def min_fragment_size(c, info_fraction=0.9, N=32):
    for m in range(1,N+1):
        if accessible_info_helstrom(c,m) >= info_fraction:
            return m
    return None

def dephase(rho, P):
    return P @ rho @ P + (np.eye(rho.shape[0])-P) @ rho @ (np.eye(rho.shape[0])-P)

# ---- A. Two-path pointer with environmental records ----
theta=0.7  # an explicitly illustrative coupling, NOT a fitted physical parameter
c=math.cos(theta)
Nmax=32
ns=(0,1,2,4,8,16,32)
rows=[]
for n in ns:
    V=c**n
    chi=holevo_for_m_fragments(c,n)
    info=accessible_info_helstrom(c,n)
    m=min_fragment_size(c,0.9,n) if n else None
    redund=(n//m if m else 0)
    rows.append({"N":n,"visibility_local":V,"holevo_total_bits_upper_bound":chi,"accessible_information_bits":info,
                 "R_0p1_disjoint_fragments_via_helstrom":redund})

n=16
partial_reversal={str(m):c**(n-m) for m in (0,4,8,12,16)}
assert abs(partial_reversal["16"]-1) < EPS
# The total S+E state is still pure and all couplings are invertible.
# If all environment interactions are inverted, original V=1 is restored.

# ---- B. Local quantum instruments on two spacelike independent sites ----
ket0=np.array([1.,0.]);ket1=np.array([0.,1.]);I2=np.eye(2)
phi=(np.kron(ket0,ket0)+np.kron(ket1,ket1))/math.sqrt(2)
rho_bell=np.outer(phi,phi)
Ps=[np.outer(ket0,ket0),np.outer(ket1,ket1)]
max_order_diff=0.0
joint=np.zeros((2,2))
for a in (0,1):
 for b in (0,1):
    MA=np.kron(Ps[a],I2)
    MB=np.kron(I2,Ps[b])
    joint[a,b]=np.trace(MA@MB@rho_bell@MB@MA).real
    max_order_diff=max(max_order_diff,norm(MA@MB@rho_bell@MB@MA - MB@MA@rho_bell@MA@MB))
assert abs(joint.sum()-1)<EPS
# Local B reduced state before and after ignoring A's result.
rho_B_initial=np.einsum('abac->bc',rho_bell.reshape(2,2,2,2))
rho_after_A=sum(np.kron(p,I2)@rho_bell@np.kron(p,I2) for p in Ps)
rho_B_after=np.einsum('abac->bc',rho_after_A.reshape(2,2,2,2))
no_signal_defect=norm(rho_B_after-rho_B_initial)
assert no_signal_defect<EPS and max_order_diff<EPS

# ---- C. Original certified B5 region, NOT an invented geometry ----
# B5 v0.3 certifies L = 6I - J and the one-dimensional constant singlet kernel.
I6=np.eye(6);J6=np.ones((6,6));L=6*I6-J6
u=np.ones(6)/math.sqrt(6);P1=np.outer(u,u);P5=I6-P1
assert norm(L-6*P5)<EPS
l_spec=eigvalsh(L)
assert norm(l_spec-np.array([0,6,6,6,6,6]))<EPS

# Construct state fully on the physically nonconstant Standard-5 register.
e0=I6[:,0]
psi=P5@e0;psi=psi/norm(psi)
rho5=np.outer(psi,psi)
assert abs(np.trace(rho5)-1)<EPS
assert norm(P1@rho5)<EPS

# Naive six-label observation (projective dephasing) violates singlet-null typing.
naive=sum(np.outer(I6[:,j],I6[:,j])@rho5@np.outer(I6[:,j],I6[:,j])
          for j in range(6))
naive_singlet=float(np.trace(P1@naive).real)
assert abs(naive_singlet-1/6)<EPS

# In contrast, a normalized A6-equivariant instrument acts only on Standard5.
# M_j = sqrt(6/5) P5 |j><j| P5; sum_j M_j^dag M_j = P5.
Ms=[math.sqrt(6/5)*P5@np.outer(I6[:,j],I6[:,j])@P5 for j in range(6)]
completeness=sum(M.T@M for M in Ms)
complete_defect=norm(completeness-P5)
rho5_out=sum(M@rho5@M.T for M in Ms)
singlet_leak=float(np.trace(P1@rho5_out).real)
trace_defect=abs(np.trace(rho5_out)-1)
ps=np.array([np.trace(M@rho5@M.T).real for M in Ms])
assert complete_defect<EPS and abs(singlet_leak)<EPS and trace_defect<EPS
assert abs(ps.sum()-1)<EPS

# Permutation covariance, all 720 permutations of A6 labels' larger S6 group.
max_cov=0.0
for permutation in permutations(range(6)):
    U=I6[list(permutation),:]
    before=sum(M@(U@rho5@U.T)@M.T for M in Ms)
    after=U@rho5_out@U.T
    max_cov=max(max_cov,norm(before-after))
assert max_cov<2e-11

# B5 correction is pure trace, hence cannot erase five STF directions.
E=np.eye(3)
T=np.zeros((9,9))
Ivec=E.reshape(-1)/math.sqrt(3)
# Normalized |I><I| with nonzero trace target eigenvalue 15/4.
DeltaW=(15/4)*np.outer(Ivec,Ivec)
stf=[]
for i in range(3):
 for j in range(i+1,3):
    A=np.zeros((3,3));A[i,j]=A[j,i]=1/math.sqrt(2)
    stf.append(A.reshape(-1))
for k in range(2):
    A=np.zeros((3,3));A[k,k]=1;A[k+1,k+1]=-1
    A/=norm(A)
    stf.append(A.reshape(-1))
stf_resid=max(norm(DeltaW@v) for v in stf)
assert stf_resid<EPS

# TT spectator remains fixed by a channel restricted to the relation register.
rho_TT=np.diag([0.35,0.65]);rho_joint=np.kron(rho5,rho_TT)
new_joint=sum(np.kron(M,I2)@rho_joint@np.kron(M.T,I2) for M in Ms)
red_TT=np.einsum('iajb->ab',new_joint.reshape(6,2,6,2)*I6[:,None,:,None])
tt_error=norm(red_TT-rho_TT)
assert tt_error<EPS

results={
"provenance":{"model":"TDG current documented Root2/MRP9B + B5 v0.3/0.4 certified registers",
  "note":"A diagnostic lens at Sigma and certified B5 operator, NOT execution of full missing MRP9B Q-B1592 chart."},
"known_physics":{"theta_radians_assumed":theta,"single_fragment_overlap":c,
  "records":rows,"partial_reversal_at_N16":partial_reversal},
"two_local_detectors":{"joint_probabilities":joint.tolist(),
  "max_order_defect":float(max_order_diff),"no_signal_defect":float(no_signal_defect)},
"B5_exact":{"spectrum":l_spec.tolist(),"naive_singlet_leakage":naive_singlet,
  "projected_instrument_completeness_defect":float(complete_defect),
  "projected_singlet_leakage":singlet_leak,
  "trace_defect":float(trace_defect),"permutation_covariance_defect":float(max_cov),
  "outcome_probabilities":ps.tolist(),"tt_spectator_defect":float(tt_error),
  "pure_trace_STF_action_defect":float(stf_resid)},
"limits":["Born probabilities used as standard input, not derived",
  "No ontological unique-outcome law derived",
  "No unique global present or foliation derived",
  "No Q-native active-to-dark beta coupling generated",
  "MRP9B original numerical fibre chart source is documented as unrecovered"],
}
(OUT/'tdg_lentille_decoherence_resultats.json').write_text(json.dumps(results,indent=2,ensure_ascii=True)+'\n')

print('KNOWN PHYSICS: overlap c=',c)
for r in rows: print(f"N={r['N']:2d} visibility={r['visibility_local']:.8f} Holevo={r['holevo_total_bits_upper_bound']:.8f} I_access={r['accessible_information_bits']:.8f} R_0.1={r['R_0p1_disjoint_fragments_via_helstrom']}")
print('PARTIAL REVERSAL (N16):',partial_reversal)
print('BELL joint:',joint)
print('BELL max order defect',max_order_diff,'no-signaling defect',no_signal_defect)
print('B5 spectrum',l_spec,'naive singlet leakage',naive_singlet)
print('B5 admissible record probabilities',ps)
print('B5 corrected singlet leakage',singlet_leak,'completeness',complete_defect,'covariance',max_cov)
print('TT spectator defect',tt_error,'STF pure trace defect',stf_resid)
print('RESULT: All numeric assertions passed; limitations recorded in JSON.')
