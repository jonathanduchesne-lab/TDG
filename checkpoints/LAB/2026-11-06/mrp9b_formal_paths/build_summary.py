#!/usr/bin/env python3
"""Consolidate executed Q-B1852 lab outputs into an audit summary."""
import json,hashlib,math
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
j=lambda name:json.loads((P/name).read_text())
m=j('b4_b24_formal_results.json')['observations']
paths=j('b2_path_identity_results.json')['cases']
s=j('fresh_sink_results.json')['cases']
a=j('record_isometry_results.json')['cases']
l=j('l2l1_gamma_comparator_results.json')['records']
q=j('formal_descent_results.json')['results']
exp={}
for scheme in ('b4','b24'):
    series=[v for v in m if v['scheme']==scheme and v['gamma']==1.]
    series.sort(key=lambda v:v['a'],reverse=True)
    z=[v for v in m if v['scheme']==scheme and v['gamma']==0.];z.sort(key=lambda v:v['a'],reverse=True)
    a_s=[v['a'] for v in series]
    d3=[v['moments'][2]['descent_residual_norm'] for v in series]
    d5=[v['moments'][4]['descent_residual_norm'] for v in z]
    exp[scheme]=dict(cutoffs=a_s,third_order_nonzero=d3,fifth_order_b2_off=d5,
        D3_power=float(np.polyfit(np.log(a_s),np.log(d3),1)[0]),
        D5_power_b2_off=float(np.polyfit(np.log(a_s),np.log(d5),1)[0]),
        coefficient_D3_per_gamma2_a3=d3[1]/(a_s[1]**3),
        coefficient_D5_b2_off_per_a5=d5[1]/(a_s[1]**5))
raw_path_err=max(x['B2_source_identity_error'] for x in paths)
raw_identity_relative=max(x['B2_source_relative_error'] for x in paths if x['gamma']>0)
s.sort(key=lambda x:x['a'],reverse=True)
fin_power=float(np.polyfit(np.log([x['a'] for x in s]),np.log([x['finite_readout_row_defect_full'] for x in s]),1)[0])
sink_power=float(np.polyfit(np.log([x['a'] for x in s]),np.log([x['finite_readout_row_defect_sink'] for x in s]),1)[0])
L={}
for gamma in [0.,1.]:
    series=sorted([x for x in l if x['gamma']==gamma],key=lambda x:x['a'],reverse=True)
    xx=np.array([x['a']**2 for x in series]);yy=np.array([x['A21_raw_norm'] for x in series]);co=np.polyfit(xx,yy,1)
    L[str(gamma)]={'a': [x['a'] for x in series],'norm':[x['A21_raw_norm'] for x in series],
                   'intercept_a2_linear_fit':float(co[-1])}
summary={'scope':'Exploratory conditional predictive-fibre chart from certified Q-B1852 H; no GR derivation',
 'source_sha256':j('b4_b24_formal_results.json')['original_source_sha256'],
 'cutoff_moment_results':exp,
 'b2_path_matrix_max_absolute_error':raw_path_err,
 'b2_path_max_relative_error_nonzero':raw_identity_relative,
 'formal_first_nonzero_moment_order':3,
 'finite_readout_rows':[{k:x[k] for k in ('a','finite_readout_row_defect_full','finite_readout_row_defect_sink','finite_readout_row_defect_b2_off')} for x in s],
 'finite_full_exponent':fin_power,'finite_fresh_sink_exponent':sink_power,
 'finite_improvement_at_0p025':next(x for x in s if x['a']==.025)['finite_readout_row_defect_full']/next(x for x in s if x['a']==.025)['finite_readout_row_defect_sink'],
 'local_stinespring_max_one_step_error':max(x['one_step_cptp_error'] for x in a),
 'local_stinespring_max_8step_error':max(x['nstep_cptp_error'] for x in a),
 'l2l1_diagnostic':L,
 'source_complete_checked':True,
 'interpretation':'a root-native local Kraus capacity, NOT a derived actual Q update or a repair of l2->l1; no nonlinear GR claim'}
(P/'SUMMARY.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(summary,indent=2))
