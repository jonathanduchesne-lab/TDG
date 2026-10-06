import itertools, numpy as np
from numpy.linalg import svd, matrix_rank, norm
TOL=1e-10
V=tuple(range(6)); E=[tuple(x) for x in itertools.combinations(V,2)]
ei={e:i for i,e in enumerate(E)}
B=np.zeros((15,6))
for i,e in enumerate(E):
    for v in e: B[i,v]=1
u6=np.ones(6)/np.sqrt(6); u15=np.ones(15)/np.sqrt(15)
P1d=np.outer(u6,u6); P5d=np.eye(6)-P1d
P1e=np.outer(u15,u15); Pc=B@np.linalg.pinv(B); P5e=Pc-P1e; P9e=np.eye(15)-Pc
Wes=np.sqrt(.3)*P1e+np.sqrt(.375)*P5e+P9e
Weis=np.sqrt(1/.3)*P1e+np.sqrt(1/.375)*P5e+P9e
Wis=np.zeros((21,21)); Wis[:6,:6]=np.eye(6); Wis[6:,6:]=Weis

def rich_D(alpha=1.0,gam=.35):
    R1=np.sqrt(18)*alpha*np.hstack([np.eye(6),np.zeros((6,15))])
    R2=np.sqrt(8)*gam*Wes@np.hstack([-.5*B,np.eye(15)])
    R3=np.sqrt(3)*gam*np.hstack([P5d,np.zeros((6,15))])
    return np.vstack([R1,R2,R3])@Wis

def parity_list(a):
    return -1 if sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2 else 1
def parity(g): return parity_list(g)
Gs=[g for g in itertools.permutations(V) if parity(g)==1]
def perm_matrix(g):
    P=np.zeros((6,6))
    for i,j in enumerate(g): P[j,i]=1
    return P
def edge_perm(g):
    P=np.zeros((15,15))
    for j,e in enumerate(E): P[ei[tuple(sorted((g[e[0]],g[e[1]])))],j]=1
    return P
def Rh(g): return np.block([[perm_matrix(g),np.zeros((6,15))],[np.zeros((15,6)),edge_perm(g)]])
def Rm(g): return np.block([[perm_matrix(g),np.zeros((6,15)),np.zeros((6,6))],[np.zeros((15,6)),edge_perm(g),np.zeros((15,6))],[np.zeros((6,6)),np.zeros((6,15)),perm_matrix(g)]])

J66=np.ones((6,6)); J615=np.ones((6,15))
Cb=[]
for X,Y in [(np.eye(6),np.zeros((6,15))),(J66,np.zeros((6,15))),(np.zeros((6,6)),B.T),(np.zeros((6,6)),J615)]:
    Cb.append(np.hstack([X,Y]))
Gcarrier=np.vstack([np.eye(6),.5*B])
A=np.column_stack([(C@Gcarrier).reshape(-1) for C in Cb])
_,_,vh=svd(A); N=vh[matrix_rank(A,TOL):].T
Qg=np.linalg.qr(Gcarrier,mode='complete')[0][:,6:]
P1=np.outer(u6,u6); P5=np.eye(6)-P1
def fmap(y):
    x=N@y
    return sum(x[i]*Cb[i] for i in range(4))
M1=np.column_stack([(P1@fmap(np.eye(2)[:,j])@Qg).reshape(-1) for j in range(2)])
_,_,vh1=svd(M1); C5=fmap(vh1[-1])
M5=np.column_stack([(P5@fmap(np.eye(2)[:,j])@Qg).reshape(-1) for j in range(2)])
_,_,vh5=svd(M5); C1=fmap(vh5[-1])
assert matrix_rank(P5@C5@Qg,TOL)==5 and norm(P1@C5@Qg)<1e-10
assert matrix_rank(P1@C1@Qg,TOL)==1 and norm(P5@C1@Qg)<1e-10

B5=[tuple(x) for x in itertools.combinations(V,5)]; idx5={S:i for i,S in enumerate(B5)}
om=[next(iter(set(V)-set(S))) for S in B5]
H=np.zeros((6,6))
for j,o in enumerate(om): H[j,o]=1
Tor=np.diag([1,-1,1,-1,1,-1])@H
B4=[tuple(x) for x in itertools.combinations(V,4)]; i4={S:i for i,S in enumerate(B4)}
d4=np.zeros((15,6))
for j,S in enumerate(B5):
    for p in range(5): d4[i4[S[:p]+S[p+1:]],j]=(-1)**p
_,_,vh4=svd(d4); r4=matrix_rank(d4,TOL); n5=vh4[r4:].T[:,0]; n5/=norm(n5)
if norm(Tor@u6+n5)<norm(Tor@u6-n5): Tor=-Tor
def R5(g):
    R=np.zeros((6,6))
    for j,S in enumerate(B5):
        im=[g[v] for v in S]; R[idx5[tuple(sorted(im))],j]=parity_list(im)
    return R
C5o=Tor@C5; C1o=Tor@C1
cov5=max(norm(R5(g)@C5o-C5o@Rh(g)) for g in Gs[::13])
cov1=max(norm(R5(g)@C1o-C1o@Rh(g)) for g in Gs[::13])
assert cov5<1e-10 and cov1<1e-10
assert norm(Tor@u6-n5)<1e-10
assert matrix_rank(d4@C5o@Qg,TOL)==5
assert norm(d4@C1o@Qg)<1e-10

D=rich_D()
_,_,vhd=svd(D.T,full_matrices=True); rd=matrix_rank(D.T,TOL); Z=vhd[rd:].T
rng=np.random.default_rng(1488); A0=rng.normal(size=(27,6)); Tint=np.zeros_like(A0)
for g in Gs: Tint += Rm(g)@A0@R5(g).T
Tint/=len(Gs); Tint=Z@(Z.T@Tint)
covT=max(norm(Rm(g)@Tint-Tint@R5(g)) for g in Gs[::17])
assert matrix_rank(Tint,TOL)==6 and matrix_rank(Tint@C5o@Qg,TOL)==5
assert covT<1e-10 and norm(D.T@Tint)<1e-10

M=np.block([[np.eye(21),np.zeros((21,27))],[np.zeros((21,21)),Wis@D.T]])
assert matrix_rank(M,TOL)==42
P=np.zeros((12,42)); P[:6,:6]=np.eye(6); P[6:,21:27]=np.eye(6)
R=P@M
assert matrix_rank(R,TOL)==12

Bs=[]
for i in range(3):
    X=np.zeros((3,3)); X[i,i]=1; Bs.append(X)
for i,j in [(0,1),(0,2),(1,2)]:
    X=np.zeros((3,3)); X[i,j]=X[j,i]=1/np.sqrt(2); Bs.append(X)
Bs=np.array(Bs)
def vec(X): return np.array([np.sum(X*b) for b in Bs])
def Gmat(g): return np.column_stack([vec(np.outer(g,np.eye(3)[a])+np.outer(np.eye(3)[a],g)) for a in range(3)])
def Srow(g): return vec(np.outer(g,g)-(g@g)*np.eye(3))
def nullspace(A):
    _,s,vh=svd(A,full_matrices=True); return vh[np.sum(s>TOL):].T
rank_tests=[]
for g in [np.array([0.,0.,1.]),np.array([1.,2.,3.])/np.sqrt(14),np.array([.3,-.7,.5])]:
    C=np.zeros((4,12)); C[0,:6]=Srow(g); C[1:,6:]=Gmat(g).T
    Ksrc=nullspace(C@R); RR=R@Ksrc
    s=svd(RR,compute_uv=False); nz=s[s>TOL]
    rank_tests.append((matrix_rank(RR,TOL),float(nz[-1]/nz[0]),float(norm(C@RR))))
    assert matrix_rank(RR,TOL)==8 and norm(C@RR)<1e-10

print('BASIC_ALLOWED_MAP_DIM',N.shape[1])
print('PURE_CHANNEL_RANKS singlet/std5',matrix_rank(P1@C1@Qg,TOL),matrix_rank(P5@C5@Qg,TOL))
print('ORIENTED_D4_RANK_NULLITY',r4,6-r4)
print('ORIENTED_SINGLET_IS_D4_KERNEL_RESID',norm(Tor@u6-n5))
print('A6_COVARIANCE_RESID singlet/std5',cov1,cov5)
print('STD5_BOUNDARY_RANK',matrix_rank(d4@C5o@Qg,TOL))
print('SINGLET_BOUNDARY_NORM',norm(d4@C1o@Qg))
print('DARK_SLOT_DIM',Z.shape[1],'B5_TO_DARK_RANK',matrix_rank(Tint,TOL),'DARK_STD5_RANK',matrix_rank(Tint@C5o@Qg,TOL))
print('B5_TO_DARK_A6_COV_RESID',covT,'DARK_Q_NULL_RESID',norm(D.T@Tint))
print('QRICH_CAUCHY_RANK',matrix_rank(M,TOL))
print('LOCAL_LINEAR_CONSTRAINED_RANK_TESTS',rank_tests)
print('VERDICT: A6 B5/dark multiplier register = EXACT REPRESENTATION CAPACITY PASS at principal derivative order.')
print('VERDICT: local linear no-extra-syndrome = EXACT PASS, rank8, conditional on relation-only extension leaving bulk->cut map unchanged.')
print('FIREWALL: beta!=0 remains a new constitutive choice; overlapping/regional nonlinear relation-cell composition remains OPEN.')
