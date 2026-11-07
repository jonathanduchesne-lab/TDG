from pathlib import Path
import sys,contextlib,io
sys.path.insert(0,str(Path(__file__).resolve().parent))
import verify_mrp9b_formal_descent as v
for g in [0.,0.25,.5,1.,2.]:
 with contextlib.redirect_stdout(io.StringIO()):m=v.q.RefinedQ('b4',.025,2+.7j,gamma=g,need_edges=False)
 x=v.calc(m,(0,1,2,3),(0,1,2),order=6)
 print('gamma',g,'D3',x['formal_obstruction'][2]['abs_defect'],'D4',x['formal_obstruction'][3]['abs_defect'],'rowres',x['finite_readout']['row_space_descent_defect'],'rank',x['finite_readout']['null_response_rank'])
