import os,io,contextlib,itertools,time,sys
import numpy as np
from numpy.linalg import inv,norm,svd,lstsq,solve,matrix_rank
from scipy.sparse import lil_matrix,eye as speye
from scipy.sparse.linalg import splu
HERE=os.path.dirname(os.path.abspath(__file__));ROOT=os.path.join(HERE,'deps','repro_qb1850')
P44=os.path.join(ROOT,'deps/repro_qb1844/qb1844_final_repro.py');qb={'__file__':P44};tb=open(P44).read()
with contextlib.redirect_stdout(io.StringIO()):exec(tb[:tb.index("print('E exact Frechet G4 kernel residuals')")],qb)
base=qb['qf']['ns'];H0=base['H0'];SHIFT=base['SHIFT'];MU=base['MU'];A=base['A'];Bcanon=base['Bcanon'];I2=qb['I2'];sig=qb['sig'];O=qb['O'];h4=qb['h4'];eta=qb['eta'];V4=qb['V4'];I3=np.eye(3)
P38=os.path.join(ROOT,'deps/inherited_qb1838/qb1838h_exact_S4_orbit_process.py');top={'__file__':P38};tt=open(P38).read()
with contextlib.redirect_stdout(io.StringIO()):exec(tt.split('# run modes')[0],top)
Kstar=top['Kstar'];moves=top['moves'];third=top['third'];after_nb=top['after_nb'];nbstar=top['nbstar'];others=top['others'];T0=top['T0'];boundary=top['boundary'];central_neighbors=top['central_neighbors'];avg_back=top['avg_back'];nbasis=top['nbasis'];Apoly=top['Apoly'];gibbs=top['gibbs'];h3d=top['h3d'];vec=top['vec'];mat=top['mat'];tau=np.ones(4);cons_projector=top['cons_projector'];local_grams=top['local_grams'];labelmap=top['labelmap'];mapC=top['mapC']
tri=np.triu_indices(3);perms=list(itertools.permutations(range(4)))

def coarse_universe():
 # SAME final Q as certified Q-B1851: retain every B4 context present in Kfull, including predictive spectators.
 M=qb['Active432Scalar'](top['Kfull'],q=.2)
 return sorted(M.B4)

def canon(vs):return tuple(sorted(vs,key=str))
class RefinedQ:
 def __init__(self,scheme,ac,z=2+.7j,gamma=1.0,need_edges=True):
  self.scheme=scheme;self.ac=ac;self.z=z;self.gamma=gamma;self.parents=coarse_universe();self.iP={T:i for i,T in enumerate(self.parents)}
  self.coarseB3=sorted(set(tuple(sorted(F)) for T in self.parents for F in itertools.combinations(T,3)))
  self.coarseB2=sorted(set(tuple(sorted(e)) for T in self.parents for e in itertools.combinations(T,2)))
  if scheme=='b24':self._top_b24()
  elif scheme=='b4':self._top_b4()
  else:raise ValueError(scheme)
  self.i4={T:i for i,T in enumerate(self.FB4)};self.i3={F:i for i,F in enumerate(self.FB3)};self.i2={e:i for i,e in enumerate(self.FB2)}
  self.N4=6*len(self.FB4);self.N3=2*len(self.FB3);self.N2=2*len(self.FB2);self.NP=6*len(self.parents);self.dim=self.N4+self.N3+self.N2+self.NP
  print('REFINED',scheme,'parents',len(self.parents),'fine B4/B3/B2',len(self.FB4),len(self.FB3),len(self.FB2),'dim',self.dim,'groupF',set(map(len,self.groupF.values())),'groupE',set(map(len,self.groupE.values())))
  t=time.time();H=self.build_H();print('H nnz',H.nnz,'build sec',time.time()-t);t=time.time();self.LU=splu((z*speye(self.dim,format='csc')-H).tocsc());print('LU sec',time.time()-t)
  if need_edges:self.U,self.BE,self.EB=self._compressed_blocks()
  else:self.U=self._parent_blocks();self.BE={};self.EB={}
  self.G0=gibbs();self.gcache={}
 def _top_b24(self):
  self.scale=24**(-1/6);FB4=set();FB3=set();FB2=set()
  for T in self.parents:
   for p in itertools.permutations(T):
    ch=tuple(tuple(sorted(p[:k])) for k in range(1,5));FB4.add(ch)
    FB3.update(tuple(q) for q in itertools.combinations(ch,3));FB2.update(tuple(q) for q in itertools.combinations(ch,2))
  self.FB4=sorted(FB4,key=str);self.FB3=sorted(FB3,key=str);self.FB2=sorted(FB2,key=str);self.order={T:T for T in self.FB4}
  self.groupF={F:[] for F in self.coarseB3}
  for ff in self.FB3:
   m=max(ff,key=len)
   if len(m)==3 and tuple(m) in self.groupF:self.groupF[tuple(m)].append(ff)
  self.groupE={e:[(tuple([u]),tuple(sorted(e))) for u in e] for e in self.coarseB2}
  assert set(map(len,self.groupF.values()))=={6} and set(map(len,self.groupE.values()))=={2}
 def _top_b4(self):
  self.scale=4**(-1/6);FB4_order={};FB3=set();FB2=set()
  vv=lambda v:('v',v);cc=lambda T:('c',)+tuple(T)
  for T in self.parents:
   Ts=tuple(sorted(T));c=cc(T)
   for f in range(4):
    order=tuple(c if t==f else vv(Ts[t]) for t in range(4));key=canon(order);FB4_order[key]=order
    FB3.update(canon([order[t] for t in range(4) if t!=j]) for j in range(4));FB2.update(canon(e) for e in itertools.combinations(order,2))
  self.FB4=sorted(FB4_order,key=str);self.FB3=sorted(FB3,key=str);self.FB2=sorted(FB2,key=str);self.order=FB4_order
  self.groupF={F:[canon([vv(v) for v in F])] for F in self.coarseB3};self.groupE={e:[canon([vv(v) for v in e])] for e in self.coarseB2}
 def cs(self,T):i=self.i4[T];return slice(6*i,6*i+6)
 def ps(self,F):i=self.i3[F];return slice(self.N4+2*i,self.N4+2*i+2)
 def es(self,e):i=self.i2[e];return slice(self.N4+self.N3+2*i,self.N4+self.N3+2*i+2)
 def pcs(self,T):i=self.iP[T];return slice(self.N4+self.N3+self.N2+6*i,self.N4+self.N3+self.N2+6*i+6)
 def build_H(self):
  af=self.scale*self.ac;H=lil_matrix((self.dim,self.dim),dtype=complex)
  for T in self.FB4:H[self.cs(T),self.cs(T)]=H0+SHIFT*np.eye(6)
  for F in self.FB3:H[self.ps(F),self.ps(F)]=(MU+SHIFT)*I2
  for e in self.FB2:H[self.es(e),self.es(e)]=SHIFT*I2
  for T in self.parents:H[self.pcs(T),self.pcs(T)]=H0+SHIFT*np.eye(6)
  for T in self.FB4:
   order=self.order[T]
   for f in range(4):
    F=tuple(x for j,x in enumerate(order) if j!=f) if self.scheme=='b24' else canon([order[j] for j in range(4) if j!=f]);C=af*A[f]@Bcanon[f];H[self.cs(T),self.ps(F)]=C;H[self.ps(F),self.cs(T)]=C.conj().T
  for F in self.FB3:
   for e0 in itertools.combinations(F,2):
    e=tuple(e0) if self.scheme=='b24' else canon(e0);C=self.gamma*af*I2;H[self.ps(F),self.es(e)]=C;H[self.es(e),self.ps(F)]=C
  for T in self.parents:
   Ts=tuple(sorted(T))
   for F0 in itertools.combinations(T,3):
    F=tuple(sorted(F0));om=next(v for v in T if v not in F);f=Ts.index(om);ng=len(self.groupF[F]);C=self.ac*A[f]@Bcanon[f]/np.sqrt(ng)
    for ff in self.groupF[F]:H[self.pcs(T),self.ps(ff)]=C;H[self.ps(ff),self.pcs(T)]=C.conj().T
  return H.tocsc()

 def _parent_blocks(self,batch=12):
  U={}
  for ib in range(0,len(self.parents),batch):
   Ts=self.parents[ib:ib+batch];B=np.zeros((self.dim,6*len(Ts)),complex)
   for j,T in enumerate(Ts):B[self.pcs(T),6*j:6*j+6]=np.eye(6)
   X=self.LU.solve(B)
   for j,T in enumerate(Ts):
    col=slice(6*j,6*j+6)
    for F0 in itertools.combinations(T,3):
     F=tuple(sorted(F0));U[(T,F)]=sum(X[self.ps(ff),col] for ff in self.groupF[F])/np.sqrt(len(self.groupF[F]))
  return U
 def _compressed_blocks(self,batch=12):
  U={};BE={};EB={}
  # parent core -> coarse B3 singlet
  for ib in range(0,len(self.parents),batch):
   Ts=self.parents[ib:ib+batch];B=np.zeros((self.dim,6*len(Ts)),complex)
   for j,T in enumerate(Ts):B[self.pcs(T),6*j:6*j+6]=np.eye(6)
   X=self.LU.solve(B)
   for j,T in enumerate(Ts):
    col=slice(6*j,6*j+6)
    for F0 in itertools.combinations(T,3):
     F=tuple(sorted(F0));U[(T,F)]=sum(X[self.ps(ff),col] for ff in self.groupF[F])/np.sqrt(len(self.groupF[F]))
  # coarse B2 singlet -> coarse B3 singlet resolvent blocks
  for ib in range(0,len(self.coarseB2),batch):
   Es=self.coarseB2[ib:ib+batch];B=np.zeros((self.dim,2*len(Es)),complex)
   for j,e in enumerate(Es):
    for ee in self.groupE[e]:B[self.es(ee),2*j:2*j+2]+=np.eye(2)/np.sqrt(len(self.groupE[e]))
   X=self.LU.solve(B); XT=self.LU.solve(B,trans='T')
   for j,e in enumerate(Es):
    col=slice(2*j,2*j+2)
    for F in self.coarseB3:
     Z=sum(X[self.ps(ff),col] for ff in self.groupF[F])/np.sqrt(len(self.groupF[F])); BE[(F,e)]=Z
     Zt=sum(XT[self.ps(ff),col] for ff in self.groupF[F])/np.sqrt(len(self.groupF[F])); EB[(e,F)]=Zt.T
  return U,BE,EB
 def getG(self,front):
  k=tuple(sorted(front))
  if k in self.gcache:return self.gcache[k]
  vars_,vi,P=cons_projector(None,front);y=np.zeros(len(vi))
  for T in front:
   rho=self.G0;comm={v:-1j*(O[T.index(v)]@rho-rho@O[T.index(v)]) for v in T}
   for F0 in itertools.combinations(T,3):
    F=tuple(sorted(F0));UB=self.U[(T,F)];X={}
    for v in F:
     z=UB@comm[v]@UB.conj().T;X[v]=(z+z.conj().T)/2
    for i,u in enumerate(F):
     for v in F[i:]:y[vi[(T,F,u,v)]]=float(np.real_if_close(h4(X[u])@eta@h4(X[v])))
  G=local_grams(front,vi,P@y);self.gcache[k]=G;return G
 def faces(self,T):T=tuple(sorted(T));return [tuple(sorted(T[:i]+T[i+1:])) for i in range(4)]
 def A0local(self,T,F):
  Fs=self.faces(T);E=[tuple(sorted(e)) for e in itertools.combinations(tuple(sorted(F)),2)];Inc=np.array([[float(set(e).issubset(ff)) for e in E] for ff in Fs]);return np.kron(Inc,I3)@V4
 def chart_scale(self,T,F):
  Fs=self.faces(T);E=[tuple(sorted(e)) for e in itertools.combinations(tuple(sorted(F)),2)];A0=self.A0local(T,F);cols=[]
  for k in range(4):
   blocks=[(e,sum(V4[3*j+a,k]*sig[a] for a in range(3))) for j,e in enumerate(E)];vv=[]
   for ff in Fs:
    Y=np.zeros((2,2),complex)
    for e,X in blocks:
     Rpe=self.BE[(ff,e)];Rep=self.EB[(e,ff)]
     Y+=Rpe@X@Rep
    Y=(Y+Y.conj().T)/2;vv.extend([.5*np.trace(S@Y).real for S in sig])
   cols.append(vv)
  AA=np.column_stack(cols);c=np.vdot(A0,AA).real
  if c<0:AA=-AA
  return np.sqrt(np.trace(AA.T@AA)/4)
 def desc_pair(self,T,S):
  vals=[]
  for v in T:
   F=tuple(sorted(set(T)-{v}));D=tuple(sorted(set(S)-{v}));vals.append(np.log(self.chart_scale(D,F)/self.chart_scale(T,F)))
  vals=np.array(vals)
  if vals.mean()<0:vals=-vals
  return vals

def rcoord(G,dG):
 Gi=inv(G);s=float(np.real_if_close(tau@Gi@tau));q=(Gi@tau)/s;dGi=-Gi@dG@Gi;ds=float(np.real_if_close(tau@dGi@tau));dq=dGi@tau/s-q*ds/s;dn=-ds/(s*s);S=Gi-s*np.outer(q,q);return np.real_if_close(lstsq(np.vstack([S,q[None,:]]),np.r_[-dq,dn/2],rcond=None)[0]).astype(float)

def memory(q):
 fb=boundary(Kstar);Gb=q.getG(fb);contexts=[T0]+others;N={T:nbasis(Gb[T]) for T in fb};F=np.zeros((16,16));V=np.zeros((68,16))
 for j,C in enumerate(others):
  S=moves[C];xx=next(v for v in S if v not in C);fp=boundary(Kstar+[S]);Gp=q.getG(fp);kids=[D for D in fp if xx in D and len(set(D)&set(C))==3]
  for ti,T in enumerate(contexts):
   rep=avg_back(Gp,kids,C,xx) if T==C else Gp[T];dG=rep-Gb[T];V[4*ti:4*ti+4,j]=rcoord(Gb[T],dG)/(q.ac*q.ac)
   if T!=T0:F[others.index(T),j]=np.vdot(N[T],dG).real/max(norm(Gb[T]),1e-30)/(q.ac*q.ac)
 return F,V,Gb

def irreps():
 B=[np.eye(3)/np.sqrt(3),np.diag([1,-1,0])/np.sqrt(2),np.diag([1,1,-2])/np.sqrt(6)]
 for ii,jj in [(0,1),(0,2),(1,2)]:
  Z=np.zeros((3,3));Z[ii,jj]=Z[jj,ii]=1/np.sqrt(2);B.append(Z)
 Cin=[np.array([Q[0,0],Q[1,1],Q[2,2],Q[0,1],Q[0,2],Q[1,2]]) for Q in B]
 return B,Cin

def M6(RH):
 B,Cin=irreps();M=np.zeros((6,6))
 for j,c in enumerate(Cin):
  Y=mat(RH@c)
  for i,Q in enumerate(B):M[i,j]=np.sum(Q*Y)
 cc=np.trace(M)/6;one=norm(M-cc*np.eye(6))/norm(M);g=np.array([M[0,0],np.trace(M[1:3,1:3])/2,np.trace(M[3:6,3:6])/3]);return M,g,one

def analyze(scheme,a,z=2+.7j,do_second=True):
 q=RefinedQ(scheme,a,z,need_edges=do_second);F,V,Gb=memory(q);Aff=Apoly[:,:4];Hess=Apoly[:,4:];L0=V[:4]@inv(F);Jaff=L0@Aff;Jh=L0@Hess;C=solve(Jaff,Jh);Hcov=Hess-Aff@C
 # irrep constrained residuals
 Z=V[:4];_,ss,vh=svd(Z);rk=np.sum(ss>ss[0]*1e-10);Ker=vh[rk:].T;Aeq=F@Ker
 bcoef=[np.array([2,2,2,0,0,0])/np.sqrt(3),np.array([2,-2,0,0,0,0])/np.sqrt(2),np.array([2,2,-4,0,0,0])/np.sqrt(6),np.array([0,0,0,np.sqrt(2),0,0]),np.array([0,0,0,0,np.sqrt(2),0]),np.array([0,0,0,0,0,np.sqrt(2)])]
 cres=[]
 for b in bcoef:
  y=Hess@b;c=lstsq(Aeq,y,rcond=None)[0];cres.append(norm(Aeq@c-y)/norm(y))
 # S4 covariance scalar F
 idx={C:i for i,C in enumerate(others)};errs=[]
 for p in perms:
  mp=labelmap(p);P=np.zeros((16,16))
  for Cc in others:P[idx[mapC(Cc,mp)],idx[Cc]]=1
  errs.append(norm(P@F@P.T-F)/norm(F))
 print('MEM',scheme,'a',a,'F/V cond',np.linalg.cond(F),np.linalg.cond(V),'Jaff',np.linalg.cond(Jaff),'S4 max',max(errs),'Cdiag',np.diag(C[:,:3]) if False else C[0,:3],'CT',[-C[3,3],-C[2,4],-C[1,5]],'cres',cres,'covdef',norm(L0@Hcov)/norm(L0@Hess))
 out=dict(q=q,F=F,V=V,C=C,Hcov=Hcov,cres=cres)
 if not do_second:return out
 # process-selected Kgeom using refined chart descriptor
 def future(T,s,active):
  if T==nbstar[s] and moves[T] not in active:return moves[T]
  if T==after_nb[s] and third[s] not in active:return third[s]
  raise RuntimeError((s,T))
 def Pproc(nb,active):
  Pm=np.zeros((4,4))
  for s,T in nb.items():
   S=future(T,s,active);d=q.desc_pair(T,S)/(a*a)
   for j,v in enumerate(T):
    slot=s if v not in T0 else T0.index(v);Pm[slot,s]=d[j]
  return Pm
 def Kgeom(K,target=None):
  if target is None:target=np.ones(4)
  fr=boundary(K);Gb0=q.getG(fr);nb=central_neighbors(fr,T0);active=set(K);HH=[]
  for s in range(4):
   T=nb[s];S=future(T,s,active);fp=boundary(list(K)+[S]);Gp=q.getG(fp);HH.append(h3d(Gb0[T0],Gp[T0]-Gb0[T0])[1][tri])
  Pm=Pproc(nb,active);return .5*np.column_stack(HH)@solve(Pm,target),Pm
 K0,P0=Kgeom(Kstar);D=[]
 for Cc in others:D.append(Kgeom(Kstar+[moves[Cc]])[0]-K0)
 D=np.column_stack(D);RHraw=D@solve(F,Hess);RHcov=D@solve(F,Hcov);Mr,gr,rr=M6(RHraw);Mc,gc,rc=M6(RHcov)
 print('SECOND',scheme,'a',a,'Pcond',np.linalg.cond(P0),'raw g/res',gr,rr,'cov g/res',gc,rc,'rank',matrix_rank(Mc,svd(Mc,compute_uv=False)[0]*1e-8))
 print('M6cov\n',Mc)
 out.update(P0=P0,Mc=Mc,gc=gc,rc=rc,Mr=Mr,gr=gr,rr=rr)
 return out

if __name__=='__main__':
 scheme=sys.argv[1] if len(sys.argv)>1 else 'b24';a=float(sys.argv[2]) if len(sys.argv)>2 else .02;z=complex(sys.argv[3]) if len(sys.argv)>3 else 2+.7j;analyze(scheme,a,z,True)
