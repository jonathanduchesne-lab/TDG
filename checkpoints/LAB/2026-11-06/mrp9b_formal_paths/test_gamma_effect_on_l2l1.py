#!/usr/bin/env python3
"""Exploratory check: is B2-return channel the actual l=2->l=1 obstruction?

Run the original Q-B1852 memory/geometry pipeline unmodified except for a
controlled gamma parameter in RefinedQ. Gamma=0 is a comparator and is NOT
claimed to be licensed actualization, nor a new root model.
"""
import sys,io,contextlib,json,hashlib,os
from pathlib import Path
import numpy as np
from numpy.linalg import norm,svd
sys.path.insert(0,str(Path(os.environ.get('TDG_Q1852_SOURCE', '/mnt/data/tdg_source_lab/qb1852_extracted/qb1852_full_refined.py')).parent))
import qb1852_full_refined as q
real=q.RefinedQ
res=[]
for gamma in [1.,0.]:
  for a in [.05,.025,.0125]:
    print('BEGIN gamma',gamma,'a',a,flush=True)
    q.RefinedQ=lambda scheme,ac,z=2+.7j,gamma=gamma,need_edges=True: real(scheme,ac,z,gamma=gamma,need_edges=need_edges)
    try:
      r=q.analyze('b4',a,2+.7j,do_second=False)
      C=r['C']
      mats,coeff=q.irreps()
      A21=C[1:4,:]@np.column_stack(coeff[1:])
      cv=dict(gamma=gamma,a=a,C_shape=list(C.shape),
             A21_raw_norm=float(norm(A21)),A21_sv=[float(x) for x in svd(A21,compute_uv=False)],
             F_condition=float(np.linalg.cond(r['F'])),
             C_first_row=[float(np.real(x)) for x in C[0,:]])
      print('END',cv,flush=True)
      res.append(cv)
    except Exception as e:
      print('FAIL',type(e).__name__,str(e),flush=True)
      res.append(dict(gamma=gamma,a=a,error=type(e).__name__+' '+str(e)))
q.RefinedQ=real
out=(Path(__file__).resolve().parent / 'l2l1_gamma_comparator_results.json')
out.write_text(json.dumps({'scope':'EXPLORATORY, not actualized TDG model and no GR claim','records':res},indent=2)+'\n')
print('SAVED',out,flush=True)
