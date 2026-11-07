#!/usr/bin/env python3
"""TDG/Root2 MRP9B conditional laboratory, November 6, 2026.

Tests necessary properties of a Q-derived frame transport without inventing the
missing Q-B1592 executable chart.  Uses the previously certified canonical
S4 l2->l1 intertwiner J in a conditional physical STF2/vector dictionary.
This is NOT a microscopic Q rerun or a derivation of Einstein equations.

Requirements: numpy, scipy.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np
from numpy.linalg import norm, eigvalsh
from scipy.spatial.transform import Rotation
from scipy.linalg import null_space

OUT = Path(__file__).resolve().parent
SEED = 20261106
rng = np.random.default_rng(SEED)
TOL = 1e-11


def e(i, j):
    v = np.zeros((3,3)); v[i,j] = 1.; return v

E = np.array([
    np.diag([1.,-1.,0.]) / np.sqrt(2),
    np.diag([1.,1.,-2.]) / np.sqrt(6),
    (e(0,1)+e(1,0)) / np.sqrt(2),
    (e(0,2)+e(2,0)) / np.sqrt(2),
    (e(1,2)+e(2,1)) / np.sqrt(2),
])
assert norm(np.einsum('aij,bij->ab', E, E)-np.eye(5)) < TOL

J = np.zeros((3,5))
J[0,4] = J[1,3] = J[2,2] = -1 / np.sqrt(3)
assert abs(norm(J)**2-1.) < TOL


def U5(R):
    return np.einsum('aij,bkl,ik,jl->ab', E, E, R, R)


def dressed_J(R):
    return R @ J @ U5(R).T


def twirl(group):
    mats = Rotation.create_group(group).as_matrix()
    Js = np.array([dressed_J(R) for R in mats])
    A = np.mean(Js, axis=0)
    B = np.einsum('kia,kib->ab', Js, Js) / len(mats)
    B = 0.5*(B+B.T)
    return len(mats), A, B


groups = {}
for group in ('T','O','I'):
    count,A,B = twirl(group)
    groups[group] = {
        'rotations':count,
        'mean_J_norm':float(norm(A)),
        'quadratic_eigenvalues':np.sort(eigvalsh(B)).tolist(),
        'quadratic_iso_defect':float(norm(B - np.trace(B)/5*np.eye(5))),
        'quadratic_trace':float(np.trace(B)),
    }
    assert abs(np.trace(B)-1) < 4e-13

# Cubic O has two distinct STF sectors E(2) and T2(3).
_, J_O, B_O = twirl('O')
assert norm(J_O) < 1e-13
assert norm(B_O - np.diag([0,0,1/3,1/3,1/3])) < 1e-12
# The icosahedral A5 group has an irreducible 5D l=2 representation.
_, J_I, B_I = twirl('I')
assert norm(J_I) < 1e-13
assert norm(B_I - np.eye(5)/5) < 2e-12

# Do not confuse twirling J with twirling its SECOND-ORDER Schur response.
# In a vector auxiliary with positive m^2, eliminating the vector changes
# k^2 I_5 by -(g^2/m^2) J^T J. The second moment survives twirling.
TT_z = np.zeros((5,2))
TT_z[0,0] = 1
TT_z[2,1] = 1
m2 = 25.0
g2 = 1.0
baseline_k2 = 1.0
spectrum = {}
for name, B in [('unaveraged', J.T @ J), ('cubic_O',B_O), ('icosa_I',B_I)]:
    resp = TT_z.T @ (baseline_k2*np.eye(5) - g2/m2*B) @ TT_z
    eigs = eigvalsh(resp)
    spectrum[name] = {'TT_eigenvalues':eigs.tolist(), 'TT_split':float(eigs[-1]-eigs[0]), 'TT_shift_from_baseline':[float(1-v) for v in eigs]}
assert spectrum['icosa_I']['TT_split'] < 2e-14
assert abs(spectrum['icosa_I']['TT_eigenvalues'][0] - (1-1/125)) < 2e-14
assert abs(spectrum['cubic_O']['TT_split'] - (1/75)) < 2e-14

# A genuine first derivative must vanish on a transverse-traceless (TT) mode.
def D(k):
    return np.einsum('aij,j->ia', E, k)

k = np.array([0.3,0.5,0.812403840463596])
k /= norm(k)
TT = null_space(D(k), rcond=1e-12)
assert TT.shape == (5,2)
H = 0.7 * np.einsum('a,aij->ij', TT[:,0], E) + 0.3*np.einsum('a,aij->ij', TT[:,1], E)
assert norm(H@k)<1e-12

# Seven lattice sites: 0 at origin, 6 at +/- Cartesian axes.
# Each site has an independently chosen LOCAL SO3 frame R_s (maps local->global).
# The link from s to center is L_0s=R_0.T@R_s, acting on local STF tensors.
frames = Rotation.random(7, random_state=rng).as_matrix()
gauges = Rotation.random(7, random_state=rng).as_matrix()
phase=0.71

def local_divergence(a, frame_set, apply_links=True):
    positions = [np.zeros(3)]
    for axis in range(3):
        for sign in (1,-1):
            pos=np.zeros(3);pos[axis]=sign*a;positions.append(pos)
    tensors=[]
    for s,pos in enumerate(positions):
        Hg=H * np.sin(float(k@pos)+phase)
        R=frame_set[s]
        tensors.append(R.T@Hg@R)
    R0=frame_set[0]
    result=np.zeros(3)
    for axis in range(3):
        plus,minus = 1+2*axis,2+2*axis
        def back(s):
            h=tensors[s]
            if not apply_links:
                return h
            link=R0.T @ frame_set[s]
            return link @ h @ link.T
        deriv=(back(plus)-back(minus))/(2*a)
        result += deriv @ R0[axis,:]
    return result

# Physical TT fields have divergence 0. The linked central-difference method
# has O(a^2) residual even with violently changing local frames.
scales=[.4,.2,.1,.05,.025]
frame_rows=[]
for a in scales:
    d=local_divergence(a,frames,True)
    dg=local_divergence(a,np.einsum('sij,sjk->sik',frames,gauges),True)
    expected=gauges[0].T@d
    no_links=local_divergence(a,frames,False)
    frame_rows.append({
        'a':a,
        'linked_TT_divergence_norm':float(norm(d)),
        'local_SO3_gauge_covariance_defect':float(norm(dg-expected)),
        'naive_untransported_divergence_norm':float(norm(no_links)),
    })
assert max(r['local_SO3_gauge_covariance_defect'] for r in frame_rows)<3e-13
slope=float(np.polyfit(np.log(scales), np.log([r['linked_TT_divergence_norm'] for r in frame_rows]),1)[0])
assert 1.85 < slope < 2.15, slope
assert frame_rows[-1]['linked_TT_divergence_norm'] < frame_rows[0]['linked_TT_divergence_norm']/100
assert frame_rows[-1]['naive_untransported_divergence_norm'] > frame_rows[0]['naive_untransported_divergence_norm']

# Curvature comparator: an arbitrary non-flat SO3 plaquette still respects
# gauge covariance of its Wilson-loop trace. This does NOT give Einstein HDA.
rot_c=Rotation.from_rotvec(np.array([0,0,0.41])).as_matrix()
links=[np.eye(3),np.eye(3),np.eye(3),rot_c]
G=Rotation.random(4,random_state=rng).as_matrix()
def holonomy(links):
    ans=np.eye(3)
    for z in links:ans=ans@z
    return ans
Hloop=holonomy(links)
trans_links=[G[i].T@links[i]@G[(i+1)%4] for i in range(4)]
Hloop2=holonomy(trans_links)
assert norm(Hloop2-G[0].T@Hloop@G[0])<2e-13
plaquette={
    'nonflat_rot_angle_radians':0.41,
    'loop_trace':float(np.trace(Hloop)),
    'expected_trace':float(1+2*np.cos(.41)),
    'local_gauge_trace_defect':float(abs(np.trace(Hloop2)-np.trace(Hloop))),
    'holonomy_covariance_error':float(norm(Hloop2-G[0].T@Hloop@G[0])),
}

result={
 'status':'LABORATORY CONDITIONAL TEST: group-twirled spin3 obstruction and frame-link divergence; NOT Q-B1592 recovered, NOT TDG derivation of GR',
 'seed':SEED,
 'canonical_anchor':'S4 unique J ray, norm(J)_F=1; physical STF2/vector identification is provisional',
 'group_twirls':groups,
 'effective_TT_auxiliary':{'g2':g2,'m2':m2,'baseline_k2':baseline_k2,'spectra':spectrum},
 'local_frame_covariant_divergence':{'wavevector':k.tolist(),'frame_count':len(frames),'rows':frame_rows,'measured_convergence_order':slope,'local_frame_gauges_independent':True},
 'curvature_control':plaquette,
 'open':'Recover actual Q-B1592 predictive-fibre connection; show resulting transport is Q-licensed, sitewise covariant, has continuum directional derivative, closes the normal bracket, and eliminates O(1) J without imported Einstein structure.',
}
out=OUT/'tdg_mrp9b_transport_twirling_resultats_2026_11_06.json'
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('GROUP TWIRLS:')
for group,d in groups.items():print(group, d)
print('SCHUR TT:',spectrum)
print('LINK COVARIANT:')
for d in frame_rows:print(d)
print('SLOPE:',slope)
print('PLAQUETTE:',plaquette)
print('PASS: conditional type-safe transport and no-go for simple cubic averaging.')
print('CAVEAT: missing original Q-B1592 source, not physical GR recovery.')
print('RESULTS',out)
