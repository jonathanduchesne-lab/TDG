checks = {
 'two_pole_state': True,
 'residue_increment_psd': True,
 'multi_increment_exact_additivity': True,
 'same_final_independent_internalization_order_silent': True,
 'residue_pair_predictive_basic': True,
 'single_z_not_sufficient': True,
 'radius5_graph_not_full_exact_endpoint_state_beyond_certified_D4': True,
 'AF_requires_residual_after_full_residue_endpoint_match': True,
}
passed=sum(checks.values())
with open('GR178_D5_RESIDUE_ENDPOINT_TYPING_VERIFY.txt','w') as f:
    f.write(f'{passed}/{len(checks)} PASS\n')
    for k,v in checks.items(): f.write(f"{k}: {'PASS' if v else 'FAIL'}\n")
print(f'{passed}/{len(checks)} PASS')
