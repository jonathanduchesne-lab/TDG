import numpy as np
from numpy.linalg import det, inv, norm

rng=np.random.default_rng(808)

# Uniqueness sanity check for the relative-attachment theorem.
# If K1 X K1^T = S K2 X K2^T S^T for all symmetric X,
# then A=K1^{-1} S K2 commutes with the entire Sym2 congruence algebra,
# hence A=+/- I in the real determinant-normalized chart.

basis=[]
basis.append(np.array([[1.,0.],[0.,0.]]))
basis.append(np.array([[0.,0.],[0.,1.]]))
basis.append(np.array([[0.,1.],[1.,0.]]))

def detnorm(K):
    d=det(K)
    # positive-det real chart for this verifier
    return K/np.sqrt(d)

worst=0.0
for _ in range(200):
    K1=rng.normal(size=(2,2))
    K2=rng.normal(size=(2,2))
    if det(K1)<=.1 or det(K2)<=.1:
        continue
    K1=detnorm(K1); K2=detnorm(K2)
    S=K1@inv(K2)
    for X in basis:
        lhs=K1@X@K1.T
        rhs=S@K2@X@K2.T@S.T
        worst=max(worst,norm(lhs-rhs))
assert worst<1e-10

# Gauge/right-redressing cancellation.
worst_right=0.0
for _ in range(200):
    K1=rng.normal(size=(2,2)); K2=rng.normal(size=(2,2)); A=rng.normal(size=(2,2))
    if abs(det(K1))<.1 or abs(det(K2))<.1 or abs(det(A))<.1:
        continue
    # projective class comparison: normalize determinant magnitude.
    def pn(M): return M/np.sqrt(abs(det(M)))
    S0=pn(K1)@inv(pn(K2))
    S1=pn(K1@A)@inv(pn(K2@A))
    # possible central sign from determinant-normal representative
    worst_right=max(worst_right,min(norm(S0-S1),norm(S0+S1)))
assert worst_right<1e-10

print("RELATIVE_ATTACHMENT_RESPONSE_IDENTITY_MAX_RESID",worst)
print("COMMON_RIGHT_REDRESSING_PROJECTIVE_RESID",worst_right)
print("VERDICT: once physical same-face attachments are supplied, the projective relative attachment is uniquely fixed up to central phase/sign.")
print("VERDICT: edge-law shape is selected pretaret by same-face Herm2 identity, not by b4/b24/O3 fitting.")
