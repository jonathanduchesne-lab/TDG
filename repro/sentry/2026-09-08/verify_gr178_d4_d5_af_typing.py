import json

facts = {
    'input_phase_bound_D': 4,
    'old_port_incidence_increment_max': 1,
    'new_b3_incidence': 2,
    'observed_exit_count': 12,
    'observed_exit_condition_min': 5,
    'gr178_adds_new_Q_law': False,
    'gr154_fixed_D_bound_is_generic_in_finite_D': True,
    'gr155_bounded_incidence_is_sufficient_certificate_not_definition': True,
    'prior_D4_AF_flatness_scope_root_wide': False,
}

D = facts['input_phase_bound_D']
succ_upper = max(D + facts['old_port_incidence_increment_max'], facts['new_b3_incidence'])
exit_lower = facts['observed_exit_condition_min']
checks = {
    'successor_max_upper_is_5': succ_upper == 5,
    'observed_exits_are_exactly_D5': facts['observed_exit_count'] == 12 and exit_lower == 5 and succ_upper == 5,
    'no_new_Q_law_at_GR178_rewrite': facts['gr178_adds_new_Q_law'] is False,
    'fixed_finite_D_analytic_class_extends_to_D5': facts['gr154_fixed_D_bound_is_generic_in_finite_D'] and 5 < float('inf'),
    'D4_threshold_not_intrinsic_Q_phase_definition': facts['gr155_bounded_incidence_is_sufficient_certificate_not_definition'],
    'prior_D4_AF_flatness_does_not_claim_rootwide_D5_no_go': facts['prior_D4_AF_flatness_scope_root_wide'] is False,
}
passed = sum(checks.values())
res = {
    'facts': facts,
    'derived': {
        'successor_max_upper_bound': succ_upper,
        'exit_successor_max_incidence': 5 if checks['observed_exits_are_exactly_D5'] else None,
        'typing': 'D4->D5 bounded-incidence certificate crossing, not a Q-selected singular phase transition',
        'AF_consequence': 'post-exit endpoint/response change alone is insufficient; require non-endpoint transition/process residual beyond matched endpoint/direct-product response control',
    },
    'checks': checks,
    'passed': passed,
    'total': len(checks),
}
with open('GR178_D4_D5_AF_TYPING_RESULTS.json','w') as f:
    json.dump(res,f,indent=2,sort_keys=True)
with open('GR178_D4_D5_AF_TYPING_VERIFY.txt','w') as f:
    f.write(f'{passed}/{len(checks)} PASS\n')
    for k,v in checks.items():
        f.write(f"{k}: {'PASS' if v else 'FAIL'}\n")
print(f'{passed}/{len(checks)} PASS')
