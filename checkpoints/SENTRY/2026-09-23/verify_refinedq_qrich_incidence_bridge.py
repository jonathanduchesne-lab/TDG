# Reproducer for the exact incidence-level part of the 2026-09-23 TDG bridge gate.
# Pure Python; exact-zero chain test plus modular-rank certificates.
from itertools import combinations
PARENTS = [(0, 1, 2, 3), (0, 1, 2, 4), (0, 1, 2, 8), (0, 1, 2, 20), (0, 1, 2, 39), (0, 1, 3, 4), (0, 1, 3, 7), (0, 1, 3, 21), (0, 1, 3, 38), (0, 1, 4, 7), (0, 1, 4, 8), (0, 1, 4, 22), (0, 1, 4, 23), (0, 1, 7, 21), (0, 1, 7, 22), (0, 1, 8, 20), (0, 1, 8, 23), (0, 1, 20, 39), (0, 1, 21, 38), (0, 2, 3, 4), (0, 2, 3, 6), (0, 2, 3, 24), (0, 2, 3, 37), (0, 2, 4, 6), (0, 2, 4, 8), (0, 2, 4, 25), (0, 2, 4, 26), (0, 2, 6, 24), (0, 2, 6, 25), (0, 2, 8, 20), (0, 2, 8, 26), (0, 2, 20, 39), (0, 2, 24, 37), (0, 3, 4, 6), (0, 3, 4, 7), (0, 3, 4, 27), (0, 3, 4, 28), (0, 3, 6, 24), (0, 3, 6, 27), (0, 3, 7, 21), (0, 3, 7, 28), (0, 3, 21, 38), (0, 3, 24, 37), (0, 4, 6, 25), (0, 4, 6, 27), (0, 4, 7, 22), (0, 4, 7, 28), (0, 4, 8, 23), (0, 4, 8, 26), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 29), (1, 2, 3, 36), (1, 2, 4, 5), (1, 2, 4, 8), (1, 2, 4, 30), (1, 2, 4, 31), (1, 2, 5, 29), (1, 2, 5, 30), (1, 2, 8, 20), (1, 2, 8, 31), (1, 2, 20, 39), (1, 2, 29, 36), (1, 3, 4, 5), (1, 3, 4, 7), (1, 3, 4, 32), (1, 3, 4, 33), (1, 3, 5, 29), (1, 3, 5, 32), (1, 3, 7, 21), (1, 3, 7, 33), (1, 3, 21, 38), (1, 3, 29, 36), (1, 4, 5, 30), (1, 4, 5, 32), (1, 4, 7, 22), (1, 4, 7, 33), (1, 4, 8, 23), (1, 4, 8, 31), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 4, 34), (2, 3, 4, 35), (2, 3, 5, 29), (2, 3, 5, 34), (2, 3, 6, 24), (2, 3, 6, 35), (2, 3, 24, 37), (2, 3, 29, 36), (2, 4, 5, 30), (2, 4, 5, 34), (2, 4, 6, 25), (2, 4, 6, 35), (2, 4, 8, 26), (2, 4, 8, 31), (3, 4, 5, 32), (3, 4, 5, 34), (3, 4, 6, 27), (3, 4, 6, 35), (3, 4, 7, 28), (3, 4, 7, 33)]

def rank_mod(A,p=1000003):
    A=[[x%p for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],p-2,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                q=A[i][c]%p; A[i]=[(A[i][j]-q*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

faces=sorted({f for T in PARENTS for f in combinations(T,3)}); fi={f:i for i,f in enumerate(faces)}
pi={T:i for i,T in enumerate(PARENTS)}
U=[[0]*len(PARENTS) for _ in faces]; d3=[[0]*len(PARENTS) for _ in faces]
for j,T in enumerate(PARENTS):
    for k in range(4):
        F=T[:k]+T[k+1:]; U[fi[F]][j]=1; d3[fi[F]][j]=(-1)**k
Ps=set(PARENTS); cand=set()
face_parents={F:[T for T in PARENTS if set(F).issubset(T)] for F in faces}
for pp in face_parents.values():
    for a,b in combinations(pp,2):
        S=tuple(sorted(set(a)|set(b)))
        if len(S)==5: cand.add(S)
B5=[S for S in sorted(cand) if all(tuple(x) in Ps for x in combinations(S,4))]
d4=[[0]*len(B5) for _ in PARENTS]
for j,S in enumerate(B5):
    for k in range(5): d4[pi[S[:k]+S[k+1:]]][j]=(-1)**k
prod=[[sum(d3[i][k]*d4[k][j] for k in range(len(PARENTS))) for j in range(len(B5))] for i in range(len(faces))]
assert all(x==0 for row in prod for x in row)
assert all(abs(d3[i][j])==U[i][j] for i in range(len(faces)) for j in range(len(PARENTS)))
ru,rd,r4=rank_mod(U),rank_mod(d3),rank_mod(d4)
assert (ru,rd,r4)==(101,76,25)
assert len(B5)==25
print('B3 x B4:',len(faces),len(PARENTS))
print('B5 complete cells:',len(B5))
print('exact ranks U,d3,d4:',ru,rd,r4)
print('nullity d3:',len(PARENTS)-rd)
print('d3*d4 exact zero: PASS')
print('ker(d3)=im(d4): CERTIFIED BY dimensions + exact chain identity')
