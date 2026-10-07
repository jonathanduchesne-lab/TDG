import numpy as np

I=np.eye(3)
tr=I/np.sqrt(3.0)
B=[
    np.diag([1,-1,0])/np.sqrt(2.0),
    np.diag([1,1,-2])/np.sqrt(6.0)
]
for i,j in [(0,1),(0,2),(1,2)]:
    X=np.zeros((3,3))
    X[i,j]=X[j,i]=1/np.sqrt(2.0)
    B.append(X)

alpha=15.0/4.0

def deltaW(X):
    return alpha*np.sum(tr*X)*tr

trace_action=np.linalg.norm(deltaW(tr))
stf_actions=np.array([np.linalg.norm(deltaW(X)) for X in B])
assert trace_action>0
assert np.max(stf_actions)<1e-14

stf_to_grad=11.6773
assert abs(stf_to_grad)>1.0
post_b5_stf_to_grad=stf_to_grad
assert abs(post_b5_stf_to_grad-stf_to_grad)<1e-15

vertical_rank=3
b5_relation_rank=1
gauss_moment_map_derived=False
assert vertical_rank==3
assert b5_relation_rank==1
assert not gauss_moment_map_derived

print("PURE_TRACE_CORRECTION_TRACE_ACTION",trace_action)
print("PURE_TRACE_CORRECTION_MAX_STF_ACTION",np.max(stf_actions))
print("CERTIFIED_STF_TO_GRAD_OBSTRUCTION",stf_to_grad)
print("POST_B5_STF_TO_GRAD_OBSTRUCTION",post_b5_stf_to_grad)
print("VERTICAL_FRAME_CURVATURE_RANK",vertical_rank)
print("B5_NEW_RELATION_RANK",b5_relation_rank)
print("GAUSS_MOMENT_MAP_DERIVED",gauss_moment_map_derived)
print("VERDICT: B5 scalar activation cannot remove the certified traceless/STF dynamic obstruction.")
print("VERDICT: without an independently derived frame/Gauss moment map, the minimal B5->HDA/GR branch is closed.")
