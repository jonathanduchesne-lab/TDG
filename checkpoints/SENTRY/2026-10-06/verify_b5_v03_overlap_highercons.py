import itertools, numpy as np
from numpy.linalg import svd, matrix_rank, norm, eigvalsh

TOL=1e-10

# Q-B1489 carrier: h21 = vertex6 + edge15, six B5 labels = omitted-vertex6.
V=tuple(range(6))
E=[tuple(x) for x in itertools.combinations(V,2)]
B=np.zeros((15,6))
for i,e in enumerate(E):
    for v in e:
        B[i,v]=1

J66=np.ones((6,6))
J615=np.ones((6,15))
Cb=[]
for X,Y in [
    (np.eye(6),np.zeros((6,15))),
    (J66,np.zeros((6,15))),
    (np.zeros((6,6)),B.T),
    (np.zeros((6,6)),J615)]:
    Cb.append(np.hstack([X,Y]))

Gcarrier=np.vstack([np.eye(6),.5*B])
A=np.column_stack([(C@Gcarrier).reshape(-1) for C in Cb])
_,_,vh=svd(A)
N=vh[matrix_rank(A,TOL):].T
assert N.shape[1]==2
Qg=np.linalg.qr(Gcarrier,mode='complete')[0][:,6:]

u6=np.ones(6)/np.sqrt(6)
P1=np.outer(u6,u6)
P5=np.eye(6)-P1

def fmap(y):
    x=N@y
    return sum(x[i]*Cb[i] for i in range(4))

# Isolate the pure Standard5 channel by requiring zero singlet output.
M1=np.column_stack([
    (P1@fmap(np.eye(2)[:,j])@Qg).reshape(-1)
    for j in range(2)
])
_,_,vh1=svd(M1)
C5=fmap(vh1[-1])
F=P5@C5@Qg
assert matrix_rank(F,TOL)==5
assert norm(P1@C5@Qg)<1e-10

# All proper subsets of the six overlapping B5 samples must be independent;
# the full six have exactly one constant-mode identity.
rank_dist={}
sv_ratio={}
for k in range(1,7):
    ranks=[]
    ratios=[]
    for S in itertools.combinations(range(6),k):
        R=F[list(S),:]
        ranks.append(matrix_rank(R,TOL))
        ss=svd(R,compute_uv=False)
        nz=ss[ss>TOL]
        ratios.append(float(nz[-1]/nz[0]) if len(nz) else 0.0)
    rank_dist[k]=sorted(set(ranks))
    sv_ratio[k]=min(ratios)

assert rank_dist=={1:[1],2:[2],3:[3],4:[4],5:[5],6:[5]}

_,_,vhL=svd(F.T,full_matrices=True)
left=vhL[matrix_rank(F.T,TOL):].T
assert left.shape==(6,1)
lv=left[:,0]/norm(left[:,0])
if lv@u6<0:
    lv=-lv
assert norm(lv-u6)<1e-10

# Source quotient kernel must be exactly 10D = singlet1 + carrier9.
qs=np.concatenate([5*np.ones(6),-2*np.ones(15)])
qs/=norm(qs)
assert norm(Gcarrier.T@qs)<1e-10
singlet_source_resid=norm(C5@qs)

Pc=B@np.linalg.pinv(B)
P9e=np.eye(15)-Pc
_,_,vh9=svd(P9e)
Q9=vh9[:matrix_rank(P9e,TOL)].T
X9=np.vstack([np.zeros((6,Q9.shape[1])),Q9])
nine_resid=norm(C5@X9)
assert singlet_source_resid<1e-10
assert nine_resid<1e-10
assert 15-matrix_rank(F,TOL)==10

# Correct oriented B5 basis and d4 boundary.
B5=[tuple(x) for x in itertools.combinations(V,5)]
B4=[tuple(x) for x in itertools.combinations(V,4)]
i4={S:i for i,S in enumerate(B4)}
d4=np.zeros((15,6))
for j,S in enumerate(B5):
    for p in range(5):
        d4[i4[S[:p]+S[p+1:]],j]=(-1)**p

om=[next(iter(set(V)-set(S))) for S in B5]
H=np.zeros((6,6))
for j,o in enumerate(om):
    H[j,o]=1
Tor=np.diag([1,-1,1,-1,1,-1])@H

Brel=d4@Tor
L=Brel.T@Brel
expected=6*np.eye(6)-np.ones((6,6))
lap_resid=norm(L-expected)
spec=eigvalsh(L)
assert lap_resid<1e-10
assert norm(Brel@u6)<1e-10
assert np.max(np.abs(spec-np.array([0,6,6,6,6,6])))<1e-10

Fo=Tor@F
boundary_relation=d4@Fo
sbr=svd(boundary_relation,compute_uv=False)
assert matrix_rank(boundary_relation,TOL)==5
assert np.max(np.abs(sbr[:5]-sbr[0]))<1e-10

# Canonical higher-cell overlap control on seven vertices:
# d5 identities among B5 relation cells must exhaust ker(d4), with no hidden H4 syndrome.
def boundary_matrix(vertices,k_vertices):
    dom=[tuple(x) for x in itertools.combinations(vertices,k_vertices)]
    cod=[tuple(x) for x in itertools.combinations(vertices,k_vertices-1)]
    ci={c:i for i,c in enumerate(cod)}
    D=np.zeros((len(cod),len(dom)))
    for j,S in enumerate(dom):
        for p in range(len(S)):
            D[ci[S[:p]+S[p+1:]],j]=(-1)**p
    return cod,dom,D

V7=tuple(range(7))
B4_7,B5_7,d4_7=boundary_matrix(V7,5)
B5b_7,B6_7,d5_7=boundary_matrix(V7,6)
assert B5_7==B5b_7
assert norm(d4_7@d5_7)<1e-12

i5={S:i for i,S in enumerate(B5_7)}
i4_7={S:i for i,S in enumerate(B4_7)}
patch_stats={}
for m in range(1,8):
    vals=[]
    for sel in itertools.combinations(range(len(B6_7)),m):
        tops=[B6_7[j] for j in sel]
        faces5=sorted({f for S in tops for f in itertools.combinations(S,5)})
        faces4=sorted({f for F5 in faces5 for f in itertools.combinations(F5,4)})
        I5=[i5[f] for f in faces5]
        I4=[i4_7[f] for f in faces4]
        D4=d4_7[np.ix_(I4,I5)]
        D5=d5_7[np.ix_(I5,list(sel))]
        r4=matrix_rank(D4,TOL)
        r5=matrix_rank(D5,TOL)
        null4=len(I5)-r4
        h4=null4-r5
        topnull=m-r5
        vals.append((len(I5),len(I4),r4,r5,null4,h4,topnull))
        assert h4==0
        assert topnull==(1 if m==7 else 0)
    patch_stats[m]=sorted(set(vals))

print('SIX_B5_SUBSET_RANKS',rank_dist)
print('SIX_B5_MIN_SV_RATIOS',sv_ratio)
print('FULL_PATCH_LEFT_NULL_DIM',left.shape[1])
print('LEFT_NULL_UNIFORM_RESID',norm(lv-u6))
print('REGIONAL_RELATION_RANK',matrix_rank(F,TOL),'KERNEL_DIM',15-matrix_rank(F,TOL))
print('SOURCE_SINGLET_ANNIHILATION',singlet_source_resid)
print('SOURCE_9_ANNIHILATION',nine_resid)
print('ORIENTED_OVERLAP_LAPLACIAN_RESID',lap_resid)
print('ORIENTED_OVERLAP_LAPLACIAN_SPECTRUM',spec)
print('BOUNDARY_RELATION_RANK',matrix_rank(boundary_relation,TOL))
print('BOUNDARY_RELATION_NONZERO_SINGULARS',sbr[:5])
print('SEVEN_VERTEX_PATCH_SIGNATURES')
for m in range(1,8):
    print(m,patch_stats[m])
print('VERDICT: actual six-B5 regional register has exactly five nonconstant scalar relations plus one derivative-constant singlet identity.')
print('VERDICT: oriented overlap operator is exactly the A6 K6 Laplacian 6I-J; no anisotropic or extra regional conormal appears.')
print('VERDICT: canonical multi-region chain control has ker(d4)=im(d5) on every tested overlap patch; no hidden H4 syndrome.')
print('FIREWALL: beta!=0 is still a constitutive premise; this does not prove nonlinear constrained-comb HDA.')
