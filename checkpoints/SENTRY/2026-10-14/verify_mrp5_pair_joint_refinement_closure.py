import itertools, math, numpy as np
from numpy.linalg import det, matrix_rank, norm

# Frozen MRP4 local sum-zero doublet basis.
q=np.array([[1/math.sqrt(2),1/math.sqrt(6)],
            [-1/math.sqrt(2),1/math.sqrt(6)],
            [0,-2/math.sqrt(6)]],float)

def G(d):
    return q.T@np.diag(np.asarray(d,float))@q

def P(d):
    g=G(d)
    return g/math.sqrt(det(g))

# Exact algebraic witness:
# for d=(1,2,4), d'=(1,3,2), the unnormalized commutator is
# [[0,-5*sqrt(3)/9],[5*sqrt(3)/9,0]], hence nonzero.
A=P([1,2,4]); B=P([1,3,2])
comm=B@A-A@B
assert norm(comm)>1e-3
prod=B@A
assert norm(prod-prod.T)>1e-3

# Global 15-edge chi chart on K6.
V=tuple(range(6)); B2=list(itertools.combinations(V,2)); B3=list(itertools.combinations(V,3))
inc=[(F,e) for F in B3 for e in B2 if set(e).issubset(F)]
edge_index={e:i for i,e in enumerate(B2)}

def perfect_matchings(C):
    C=tuple(sorted(C)); a=C[0]; out=[]
    for b in C[1:]:
        rem=[x for x in C if x not in (a,b)]
        out.append(tuple(sorted((tuple(sorted((a,b))),tuple(sorted(rem))))))
    return tuple(sorted(set(out)))

def perm3(src,tgt,fn):
    M=np.zeros((3,3))
    for i,s in enumerate(src): M[tgt.index(fn(s)),i]=1
    return M

def induced(M): return q.T@M@q

def R0(F,e):
    F=tuple(sorted(F)); e=tuple(sorted(e))
    u=next(iter(set(F)-set(e)))
    O=tuple(sorted(set(V)-set(F)))
    C=tuple(sorted(set(V)-set(e)))
    Ms=perfect_matchings(C)
    def f(m):
        for pair in m:
            if u in pair: return pair[0] if pair[1]==u else pair[1]
        raise RuntimeError
    return induced(perm3(Ms,O,f))

def response_vec(logchi):
    chi=np.exp(logchi); out=[]
    for F,e in inc:
        u=next(iter(set(F)-set(e)))
        O=tuple(sorted(set(V)-set(F)))
        d=[chi[edge_index[tuple(sorted((u,v)))]] for v in O]
        out.extend((P(d)@R0(F,e)).ravel())
    return np.asarray(out)

x=np.linspace(-.7,.9,15); eps=1e-6
J=np.column_stack([(response_vec(x+eps*np.eye(15)[j])-response_vec(x-eps*np.eye(15)[j]))/(2*eps) for j in range(15)])
assert matrix_rank(J,tol=1e-8)==14
assert norm(response_vec(x+1.234*np.ones(15))-response_vec(x))<1e-12

# Generic sequential-composition stress: MRP4 positive factors are not a semigroup.
rng=np.random.default_rng(505)
defs=[]
for _ in range(1000):
    d1=np.exp(rng.normal(size=3)); d2=np.exp(rng.normal(size=3))
    M=P(d2)@P(d1)
    defs.append(norm(M-M.T)/norm(M))
assert min(defs)>1e-6

# Even retaining a continuous polar rotation does not keep the positive factor
# inside the positive-chi cone for all compositions.
E=np.eye(3)
L=np.column_stack([[G(E[k])[0,0],G(E[k])[0,1],G(E[k])[1,1]] for k in range(3)])
Linv=np.linalg.inv(L)
def d_from_sym(H):
    return Linv@np.array([H[0,0],H[0,1],H[1,1]])
def left_polar(M):
    w,v=np.linalg.eigh(M@M.T)
    return (v*np.sqrt(w))@v.T
O=np.array([[-.5,-math.sqrt(3)/2],[math.sqrt(3)/2,-.5]])
H=left_polar(P([2,1,5])@O@P([1,1,3]))
dw=d_from_sym(H)
assert dw[1]<0

print("MRP5_GLOBAL_CHI_RESPONSE_RANK",matrix_rank(J,tol=1e-8),"/15")
print("MRP5_COMMON_SCALAR_BLINDNESS_PASS")
print("MRP5_EXACT_NONCOMMUTING_WITNESS_COMM_NORM",norm(comm))
print("MRP5_GENERIC_NONCLOSURE_MIN_DEFECT",min(defs))
print("MRP5_POLAR_POSITIVE_CONE_WITNESS_d",dw)
print("VERDICT: MRP4 chi-only state family is not closed under generic refinement composition.")
print("VERDICT: MRP1 full projective response transport remains the natural larger closure candidate.")
