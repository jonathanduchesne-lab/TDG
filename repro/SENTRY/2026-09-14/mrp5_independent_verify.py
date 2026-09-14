import itertools,json
import numpy as np
from pathlib import Path

rng=np.random.default_rng(94173)
fine=[(i,a,b) for i in range(6) for a in range(3) for b in range(2)]
vals={}
for x,y in itertools.combinations(fine,2):
    if x[0]==y[0]: continue
    vals[tuple(sorted((x,y)))]=float(np.exp(.41*rng.normal()+.023*(x[0]+2)*(y[0]+1)+.031*(x[1]+y[1])))

def push(d,nodes,parent,p):
    ps=sorted(set(parent(x) for x in nodes),key=repr); out={}
    for A,B in itertools.combinations(ps,2):
        target=tuple(sorted((A,B),key=repr)); arr=[]
        for x,y in itertools.combinations(nodes,2):
            if parent(x)==parent(y): continue
            if tuple(sorted((parent(x),parent(y)),key=repr))!=target: continue
            k=tuple(sorted((x,y),key=repr))
            if k in d: arr.append(d[k])
        if arr: out[target]=float(np.sum(np.array(arr)**p)**(1/p))
    return out,ps

checks={}; metrics={}
for p in [1.0,1.5,2.5,4.0]:
    mid,midnodes=push(vals,fine,lambda x:(x[0],x[1]),p)
    c2,_=push(mid,midnodes,lambda x:x[0],p); c1,_=push(vals,fine,lambda x:x[0],p)
    defect=max(abs(c1[k]-c2[k]) for k in c1)/max(c1.values())
    checks[f'p{p}_diamond']=defect<2e-15; metrics[f'p{p}_diamond_rel']=defect
co={p:push(vals,fine,lambda x:x[0],p)[0] for p in [1.0,1.5,2.5,4.0]}
def pres(a,b):
    ks=sorted(a,key=repr); x=np.array([a[k] for k in ks]); y=np.array([b[k] for k in ks]); c=y@x/(y@y)
    return np.linalg.norm(x-c*y)/np.linalg.norm(x)
for a,b in [(1.0,1.5),(1.5,2.5),(2.5,4.0),(1.0,4.0)]:
    r=pres(co[a],co[b]); metrics[f'p{a}_vs_p{b}_ray']=float(r); checks[f'p{a}_vs_p{b}_distinct']=r>1e-4
arr=[v for (x,y),v in vals.items() if tuple(sorted((x[0],y[0])))==(0,1)]; s=sum(arr)
for p in [1.0,1.5,2.5,4.0]:
    z=float(np.sum(np.array(arr)**p)**(1/p)); metrics[f'p{p}_add_rel']=abs(z-s)/s
checks['p1_additive']=metrics['p1.0_add_rel']<1e-14
checks['nonp1_nonadditive']=min(metrics['p1.5_add_rel'],metrics['p2.5_add_rel'],metrics['p4.0_add_rel'])>1e-2
out={'checks':checks,'metrics':metrics,'pass_count':sum(checks.values()),'count':len(checks),'all_pass':all(checks.values())}
Path('MRP5_INDEPENDENT_VERIFY.json').write_text(json.dumps(out,indent=2,sort_keys=True,default=lambda o:bool(o) if isinstance(o,np.bool_) else str(o))+'\n')
print(json.dumps(out,indent=2,sort_keys=True,default=lambda o:bool(o) if isinstance(o,np.bool_) else str(o)))
