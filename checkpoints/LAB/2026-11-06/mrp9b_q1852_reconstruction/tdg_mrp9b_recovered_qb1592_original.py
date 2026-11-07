import os,sys,contextlib,io,itertools,numpy as np
from numpy.linalg import inv,norm,det,svd
BASE='/mnt/data/tdg_qb1540_work/src';sys.path.insert(0,BASE)
ns={'__file__':os.path.join(BASE,'qb1585_semicausal_B2_fresh_record_restores_mixed_cut_2jet.py'),'__name__':'defs'}
text=open(ns['__file__']).read().split('rows=[]')[0]
with contextlib.redirect_stdout(io.StringIO()):exec(text,ns)
B,Z,SemiRecordModel=ns['B'],ns['Z'],ns['SemiRecordModel']
from tdg_qb1001_base import O,A,Bcanon,sig
M=SemiRecordModel(B.boundary_s4(),q=.2)
# chart map between B4-side predictive row map and retained B3-side row map
def chart(H,T,F):
 R=inv(Z*np.eye(M.dim)-H);ci=np.arange(M.cs(M.i4[T]).start,M.cs(M.i4[T]).stop)
 Gc=R[np.ix_(ci,ci)];He=Z*np.eye(6)-inv(Gc);Rc=inv(Z*np.eye(6)-He)
 outside=next(iter(set(T)-set(F)));f=T.index(outside);C=A[f]@Bcanon[f];Lpre=C.conj().T@Rc
 p=M.i3[F];pp=np.arange(M.ps(p).start,M.ps(p).stop);G=R[np.ix_(pp,pp)];Lpost=inv(G)@R[np.ix_(pp,ci)]
 Q=Lpost@np.linalg.pinv(Lpre)
 # deterministic det-normalized SL2 chart; branch near positive real background
 S=Q/np.sqrt(det(Q)+0j)
 return S,Q,norm(Lpost-Q@Lpre)/max(norm(Lpost),1e-30)
def core_source(T,X):
 V=np.zeros((M.dim,M.dim),complex);sl=np.arange(M.cs(M.i4[T]).start,M.cs(M.i4[T]).stop);V[np.ix_(sl,sl)]=X;return V
# sl2 coefficient vector (complex 3) of left-trivialized tangent A=S^-1 dS
def avec(S,dS):
 X=inv(S)@dS;X=X-np.trace(X)/2*np.eye(2);return np.array([np.trace(sig[k]@X)/2 for k in range(3)])
tet=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/np.sqrt(3)
P1=np.ones((4,4))/4;P3=np.eye(4)-P1
rows=[];eps=2e-5
for a in [.05,.025,.012,.006]:
 H=M.build(a,bundle=True);sing=[];tripr=[];trip_s=[];rowres=[];unitfrac=[]
 for T in M.B4:
  # use each crossed face F; four local deformations indexed by b in T
  for F0 in itertools.combinations(T,3):
   F=tuple(sorted(F0));S0,Q0,rr=chart(H,T,F);rowres.append(rr);cols=[]
   for b,v in enumerate(T):
    V=core_source(T,O[b]);Sp,_,_=chart(H+eps*V,T,F);Sm,_,_=chart(H-eps*V,T,F);dS=(Sp-Sm)/(2*eps);z=avec(S0,dS);cols.append(np.r_[z.real,z.imag])
   J=np.column_stack(cols) # 6 x4
   js=J@np.ones(4)/4;Jt=J@P3
   sing.append(norm(js));s=svd(Jt,compute_uv=False);tripr.append(np.sum(s>s[0]*1e-7) if s[0]>0 else 0);trip_s.append(s[:3])
   # unitary(rotation) vs Hermitian(boost) split of sl2 tangent via X components: for coeff z, imag is unitary rotation if sigma Hermitian times i
   nr=norm(J[:3]);ni=norm(J[3:]);unitfrac.append(ni/max(np.sqrt(nr*nr+ni*ni),1e-30))
 ts=np.array(trip_s);print('a',a,'singlet med/max',np.median(sing),max(sing),'trip rank set',sorted(set(tripr)),'trip sv med',np.median(ts,axis=0),'rowres max',max(rowres),'imag(rotation)-fraction med',np.median(unitfrac))
 rows.append((a,np.median(sing),np.median(ts[:,2]),max(rowres)))
print('CLASSIFICATION: SEMICAUSAL CROSSING SL2-CHART CONNECTION DIAGNOSTIC. The Q-derived B4<->B3 predictive-fibre transition is det-normalized to an SL2 chart. Its response to the four local core deformation slots is decomposed into A4 singlet and triplet. A suppressed singlet with rank3 triplet would supply a process-derived moving-frame connection candidate compatible with the geometric 1+3 cut anchor; it is not by itself identification of O_v sources with lapse generators.')
