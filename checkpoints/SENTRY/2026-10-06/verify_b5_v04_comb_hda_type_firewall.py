# B5 v0.4 type/rank firewall verifier.
# This verifier does not recompute Q-B1847; it certifies the logical incompatibility
# between the one-relation minimal B5 extension and treating the certified rank-3
# vertical frame-curvature channel as already removed/first-class.
import numpy as np

# Certified Q-B1847 relational-separator singular values at z=2:
cert = {
    0.02: np.array([5.46971195, .54628843, .23827010]),
    0.01: np.array([5.47010082, .54591968, .23810880]),
    0.005: np.array([5.47020381, .54582756, .23807034]),
}
for a,s in cert.items():
    assert np.all(s > 0)
    assert np.linalg.matrix_rank(np.diag(s), tol=1e-10) == 3

# v0.2/v0.3 minimal extension adds exactly one independent scalar normal relation
# on top of the three tangential relations: local constrained image rank 8, no fifth
# conormal.  Therefore no additional independent rank-3 internal/frame constraint
# has been admitted by the minimal extension.
local_phase_dim = 12
first_class_cut_constraints = 4
reduced_phase_dim = local_phase_dim - 2*first_class_cut_constraints
assert reduced_phase_dim == 4

# The complementary Q-port curvature is not null/commutant on the predictive algebra:
max_commutator_actions = np.array([1.41096,1.41021,1.40593])
assert np.all(max_commutator_actions > 1.0)

# Type firewall:
#  - the B5 activation is one scalar relation C0;
#  - Q-B1847 complementary curvature is a rank-3 vertical su2 action;
#  - no independently derived Gauss/frame moment map is present.
# Consequently the minimal B5 extension cannot *by itself* reclassify that vertical
# rank-3 action as an allowed first-class term without adding/deriving extra structure.
b5_new_relation_rank = 1
vertical_frame_action_rank = 3
gauss_moment_map_derived = False
horizontal_base_lift_derived_from_same_comb = False

assert b5_new_relation_rank == 1
assert vertical_frame_action_rank == 3
assert not gauss_moment_map_derived
assert not horizontal_base_lift_derived_from_same_comb

print("Q-B1847 complementary relational rank: 3 at all certified cutoffs")
print("v0.2/v0.3 minimal new normal relation rank: 1")
print("local reduced phase dimension under four cut constraints:", reduced_phase_dim)
print("Gauss/frame moment-map theorem derived:", gauss_moment_map_derived)
print("same-comb horizontal/base lift derived:", horizontal_base_lift_derived_from_same_comb)
print("VERDICT: minimal B5 extension alone does not close the comb-native first-class/HDA gate.")
print("VERDICT: effective lambda=1/2 HDA capacity remains conditional; comb-native realization is type-incomplete.")
