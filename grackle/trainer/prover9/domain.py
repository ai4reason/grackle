REPLACE = {
  
}

PARAMS = """

lrs_ticks {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(lrs_ticks)s]
lrs_interval {1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(lrs_interval)s]    
min_sos_limit {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(min_sos_limit)s]
order {lpo,rpo, kbo} [%(order)s]
eq_defs {unfold,fold,pass} [%(eq_defs)s]
inverse_order {set, clear} [%(inverse_order)s]
expand_relational_defs {set, clear} [%(expand_relational_defs)s]
predicate_elim {set, clear} [%(predicate_elim)s]
fold_denial_max {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(fold_denial_max)s]
sort_initial_sos {set, clear} [%(sort_initial_sos)s]
process_initial_sos {set, clear} [%(process_initial_sos)s]
sos_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(sos_limit)s]
max_given {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_given)s]
max_kept {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_kept)s]
max_megs {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647}  [%(max_megs)s]
age_part {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(age_part)s]
weight_part {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(weight_part)s]
true_part {0, 4, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(true_part)s]
false_part {0, 4, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(false_part)s]
random_part {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(random_part)s]
hints_part {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(hints_part)s]
default_parts {set, clear} [%(default_parts)s]
pick_given_ratio {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(pick_given_ratio)s]
lightest_first {set, clear} [%(lightest_first)s]
breadth_first {set, clear} [%(breadth_first)s]
random_given {set, clear} [%(random_given)s]
input_sos_first {set, clear} [%(input_sos_first)s]
binary_resolution {set, clear} [%(binary_resolution)s]
neg_binary_resolution {set, clear} [%(neg_binary_resolution)s]
ordered_res {set, clear} [%(ordered_res)s]
check_res_instances {set, clear} [%(check_res_instances)s]
literal_selection {max_negative, all_negative, none} [%(literal_selection)s]
pos_hyper_resolution {set, clear} [%(pos_hyper_resolution)s]
hyper_resolution {set, clear} [%(hyper_resolution)s]
neg_hyper_resolution {set, clear} [%(neg_hyper_resolution)s]
ur_resolution {set, clear} [%(ur_resolution)s]
pos_ur_resolution {set, clear} [%(pos_ur_resolution)s]
neg_ur_resolution {set, clear} [%(neg_ur_resolution)s]
initial_nuclei {set, clear} [%(initial_nuclei)s]
ur_nucleus_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(ur_nucleus_limit)s]
paramodulation {set, clear} [%(paramodulation)s]
ordered_para {set, clear} [%(ordered_para)s]
check_para_instances {set, clear} [%(check_para_instances)s]
para_from_vars {set, clear} [%(para_from_vars)s]
para_lit_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(para_lit_limit)s]
para_units_only {set, clear} [%(para_units_only)s]
basic_paramodulation {set, clear} [%(basic_paramodulation)s]
lex_order_vars {set, clear} [%(lex_order_vars)s]
demod_step_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(demod_step_limit)s]
demod_increase_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(demod_increase_limit)s]
back_demod {set, clear} [%(back_demod)s]
lex_dep_demod {set, clear} [%(lex_dep_demod)s]
lex_dep_demod_lim {-1, 0, 1, 11, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(lex_dep_demod_lim)s]
lex_dep_demod_sane {set, clear} [%(lex_dep_demod_sane)s]
unit_deletion {set, clear} [%(unit_deletion)s]
cac_redundancy {set, clear} [%(cac_redundancy)s]
max_literals {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_literals)s]
max_depth {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_depth)s]
max_vars {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_vars)s]
max_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_weight)s]
safe_unit_conflict {set, clear} [%(safe_unit_conflict)s]
factor {set, clear} [%(factor)s]
new_constants {-1, 0, 1, 3, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(new_constants)s]
back_subsume {set, clear} [%(back_subsume)s]
backsub_check {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(backsub_check)s]
constant_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(constant_weight)s]
sk_constant_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(sk_constant_weight)s]
variable_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(variable_weight)s]
not_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(not_weight)s]
or_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(or_weight)s]
prop_atom_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(prop_atom_weight)s]
nest_penalty {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(nest_penalty)s]
depth_penalty {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(depth_penalty)s]
var_penalty {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(var_penalty)s]
default_weight {-2147483648, -1000000, -100000, -20000, -10000, -5000, -2000, -100, -10, -1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(default_weight)s]
reuse_denials {set, clear} [%(reuse_denials)s]
auto_denials {set, clear} [%(auto_denials)s]
restrict_denials {set, clear} [%(restrict_denials)s]

a__cng0_action {demod_step_limit,demod_increase_limit,new_constants,para_lit_limit,max_given,max_weight,max_depth,max_vars,max_literals,constant_weight,variable_weight,not_weight,or_weight,prop_atom_weight,nest_penalty,depth_penalty,default_weight,pick_given_ratio,age_part,weight_part,false_part,true_part} [%(a__cng0_action)s]
a__cng0_cond {100,500,1000,2000,5000,10000} [%(a__cng0_cond)s]
a__cng0_counter {none,given,generated,kept,level} [%(a__cng0_counter)s]
a__cng0_value {0,1,5,10,15,20,50,100,10000} [%(a__cng0_value)s]
a__cng1_action {demod_step_limit,demod_increase_limit,new_constants,para_lit_limit,max_given,max_weight,max_depth,max_vars,max_literals,constant_weight,variable_weight,not_weight,or_weight,prop_atom_weight,nest_penalty,depth_penalty,default_weight,pick_given_ratio,age_part,weight_part,false_part,true_part} [%(a__cng1_action)s]
a__cng1_cond {100,500,1000,2000,5000,10000} [%(a__cng1_cond)s]
a__cng1_counter {none,given,generated,kept,level} [%(a__cng1_counter)s]
a__cng1_value {0,1,5,10,15,20,50,100,10000} [%(a__cng1_value)s]
a__flg0_action {set,clear} [%(a__flg0_action)s]
a__flg0_cond {100,500,1000,2000,5000,10000} [%(a__flg0_cond)s]
a__flg0_counter {none,given,generated,kept,level} [%(a__flg0_counter)s]
a__flg0_flag {reuse_denials,breadth_first,lightest_first} [%(a__flg0_flag)s]
a__flg1_action {set,clear} [%(a__flg1_action)s]
a__flg1_cond {100,500,1000,2000,5000,10000} [%(a__flg1_cond)s]
a__flg1_counter {none,given,generated,kept,level} [%(a__flg1_counter)s]
a__flg1_flag {reuse_denials,breadth_first,lightest_first} [%(a__flg1_flag)s]
a__hgh0_order {weight,age,random} [%(a__hgh0_order)s]
a__hgh0_prp0_cond {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__hgh0_prp0_cond)s]
a__hgh0_prp0_connect {and,or} [%(a__hgh0_prp0_connect)s]
a__hgh0_prp0_neg {yes,no} [%(a__hgh0_prp0_neg)s]
a__hgh0_prp0_val {1,2,3,5,7,10,15,20,50,1000} [%(a__hgh0_prp0_val)s]
a__hgh0_prp1_cond {none,positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__hgh0_prp1_cond)s]
a__hgh0_prp1_neg {yes,no} [%(a__hgh0_prp1_neg)s]
a__hgh0_prp1_val {1,2,3,5,7,10,15,20,50,1000} [%(a__hgh0_prp1_val)s]
a__hgh0_ratio {0,1,2,3,4,5,10,20,50} [%(a__hgh0_ratio)s]
a__low0_order {weight,age,random} [%(a__low0_order)s]
a__low0_prp0_cond {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__low0_prp0_cond)s]
a__low0_prp0_connect {and,or} [%(a__low0_prp0_connect)s]
a__low0_prp0_neg {yes,no} [%(a__low0_prp0_neg)s]
a__low0_prp0_val {1,2,3,5,7,10,15,20,50,1000} [%(a__low0_prp0_val)s]
a__low0_prp1_cond {none,positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__low0_prp1_cond)s]
a__low0_prp1_neg {yes,no} [%(a__low0_prp1_neg)s]
a__low0_prp1_val {1,2,3,5,7,10,15,20,50,1000} [%(a__low0_prp1_val)s]
a__low0_ratio {0,1,2,3,4,5,10,20,50} [%(a__low0_ratio)s]
a__low1_order {weight,age,random} [%(a__low1_order)s]
a__low1_prp0_cond {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__low1_prp0_cond)s]
a__low1_prp0_connect {and,or} [%(a__low1_prp0_connect)s]
a__low1_prp0_neg {yes,no} [%(a__low1_prp0_neg)s]
a__low1_prp0_val {1,2,3,5,7,10,15,20,50,1000} [%(a__low1_prp0_val)s]
a__low1_prp1_cond {none,positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level} [%(a__low1_prp1_cond)s]
a__low1_prp1_neg {yes,no} [%(a__low1_prp1_neg)s]
a__low1_prp1_val {1,2,3,5,7,10,15,20,50,1000} [%(a__low1_prp1_val)s]
a__low1_ratio {0,1,2,3,4,5,10,20,50} [%(a__low1_ratio)s]
"""

# prolog_style_variables {set, clear} [%(prolog_style_variables)s]
# max_proofs{-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(max_proofs)s]
# random_seed {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647} [%(random_seed)s]

# kept for now:
# max_megs {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 10000, 20000, 100000, 1000000, 2147483647}  [%(max_megs)s]

CONDITIONS = """
a__flg0_cond | a__flg0_counter in {given,generated,kept,level}
a__flg0_action | a__flg0_counter in {given,generated,kept,level}
a__flg0_flag | a__flg0_counter in {given,generated,kept,level}
a__flg1_cond | a__flg1_counter in {given,generated,kept,level}
a__flg1_action | a__flg1_counter in {given,generated,kept,level}
a__flg1_flag | a__flg1_counter in {given,generated,kept,level}
a__flg1_counter | a__flg0_counter in {given,generated,kept,level}
a__cng0_cond | a__cng0_counter in {given,generated,kept,level}
a__cng0_action | a__cng0_counter in {given,generated,kept,level}
a__cng0_flag | a__cng0_counter in {given,generated,kept,level}
a__cng1_cond | a__cng1_counter in {given,generated,kept,level}
a__cng1_action | a__cng1_counter in {given,generated,kept,level}
a__cng1_flag | a__cng1_counter in {given,generated,kept,level}
a__cng1_counter | a__cng0_counter in {given,generated,kept,level}
a__low0_prp0_val | a__low0_prp0_cond in {weight,literals,variables,depth,level}
a__low0_prp0_connect | a__low0_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__low0_prp1_val | a__low0_prp1_cond in {weight,literals,variables,depth,level}
a__low0_prp1_neg | a__low0_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__low0_order | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp0_cond | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp0_val | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp0_neg | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp0_connect | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp1_cond | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp1_val | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low0_prp1_neg | a__low0_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp0_val | a__low1_prp0_cond in {weight,literals,variables,depth,level}
a__low1_prp0_connect | a__low1_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__low1_prp1_val | a__low1_prp1_cond in {weight,literals,variables,depth,level}
a__low1_prp1_neg | a__low1_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__low1_order | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp0_cond | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp0_val | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp0_neg | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp0_connect | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp1_cond | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp1_val | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_prp1_neg | a__low1_ratio in {1,2,3,4,5,10,20,50}
a__low1_ratio | a__low0_ratio in {1,2,3,4,5,10,20,50}
age_part | a__low0_ratio in {0}
weight_part | a__low0_ratio in {0}
false_part | a__low0_ratio in {0}
true_part | a__low0_ratio in {0}
random_part | a__low0_ratio in {0}
a__hgh0_prp0_val | a__hgh0_prp0_cond in {weight,literals,variables,depth,level}
a__hgh0_prp0_connect | a__hgh0_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__hgh0_prp1_val | a__hgh0_prp1_cond in {weight,literals,variables,depth,level}
a__hgh0_prp1_neg | a__hgh0_prp1_cond in {positive,negative,mixed,unit,horn,definite,has_equality,true,false,initial,resolvent,hyper_resolvent,ur_resolvent,factor,paramodulant,back_demodulant,subsumer,all,weight,literals,variables,depth,level}
a__hgh0_order | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp0_cond | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp0_val | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp0_neg | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp0_connect | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp1_cond | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp1_val | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
a__hgh0_prp1_neg | a__hgh0_ratio in {1,2,3,4,5,10,20,50}
age_part | a__hgh0_ratio in {0}
weight_part | a__hgh0_ratio in {0}
false_part | a__hgh0_ratio in {0}
true_part | a__hgh0_ratio in {0}
random_part | a__hgh0_ratio in {0}
"""

FORBIDDENS = ""

DEFAULTS = {
   "prolog_style_variables" : "clear", 
   "lrs_ticks" : "1",
   "lrs_interval" : "50", 
   "min_sos_limit" : "0", 
   "order" : "lpo",
   "eq_defs" : "unfold",
   "inverse_order" : "set", 
   "expand_relational_defs" : "clear",
   "predicate_elim" : "set",
   "fold_denial_max" : "0",
   "sort_initial_sos" : "clear",
   "process_initial_sos" : "set", 
   "sos_limit" : "20000",
   "max_given" : "-1", 
   "max_kept" : "-1", 
   "max_megs" : "200", 
   "age_part" : "1",
   "weight_part" : "0",
   "true_part" : "4",
   "false_part" : "4",
   "random_part" : "0",
   "hints_part" : "2147483647",
   "default_parts" : "set", 
   "pick_given_ratio" : "0",
   "lightest_first" : "clear",
   "breadth_first" : "clear",
   "random_given" : "clear",
   "random_seed" : "0", 
   "input_sos_first" : "set", 
   "binary_resolution" : "clear",
   "neg_binary_resolution" : "clear",
   "ordered_res" : "set", 
   "check_res_instances" : "clear",
   "literal_selection" : "max_negative",
   "pos_hyper_resolution" : "clear",
   "hyper_resolution" : "clear",
   "neg_hyper_resolution" : "clear",
   "ur_resolution" : "clear",
   "pos_ur_resolution" : "clear",
   "neg_ur_resolution" : "clear",
   "initial_nuclei" : "clear",
   "ur_nucleus_limit" : "-1", 
   "paramodulation" : "clear",
   "ordered_para" : "set",
   "check_para_instances" : "clear",
   "para_from_vars" : "set",
   "para_lit_limit" : "-1",
   "para_units_only" : "clear",
   "basic_paramodulation" : "clear",
   "lex_order_vars" : "clear",
   "demod_step_limit" : "1000",
   "demod_increase_limit" : "1000",
   "back_demod" : "set", 
   "lex_dep_demod" : "set",
   "lex_dep_demod_lim" : "11",
   "lex_dep_demod_sane" : "set",
   "unit_deletion" : "clear",
   "cac_redundancy" : "set",
   "max_literals" : "-1", 
   "max_depth" : "-1", 
   "max_vars" : "-1", 
   "max_weight" : "100", 
   "safe_unit_conflict" : "clear",
   "factor" : "clear",
   "new_constants" : "0",
   "back_subsume" : "set",
   "backsub_check" : "500", 
   "constant_weight" : "1",
   "sk_constant_weight" : "1",
   "variable_weight" : "1", 
   "not_weight" : "0",
   "or_weight" : "0", 
   "prop_atom_weight" : "1", 
   "nest_penalty" : "0", 
   "depth_penalty" : "0",
   "var_penalty" : "0",
   "default_weight" : "2147483647", 
   "max_proofs" : "1",
   "reuse_denials" : "clear",
   "auto_denials" : "set",
   "restrict_denials" : "clear",
   #
   "a__cng0_action": "demod_step_limit",
   "a__cng0_cond": "100",
   "a__cng0_counter": "none",
   "a__cng0_value": "0",
   "a__cng1_action": "demod_step_limit",
   "a__cng1_cond": "100",
   "a__cng1_counter": "none",
   "a__cng1_value": "0",
   "a__flg0_action": "set",
   "a__flg0_cond": "100",
   "a__flg0_counter": "none",
   "a__flg0_flag": "reuse_denials",
   "a__flg1_action": "set",
   "a__flg1_cond": "100",
   "a__flg1_counter": "none",
   "a__flg1_flag": "reuse_denials",
   "a__hgh0_order": "weight",
   "a__hgh0_prp0_cond": "positive",
   "a__hgh0_prp0_connect": "and",
   "a__hgh0_prp0_neg": "yes",
   "a__hgh0_prp0_val": "1",
   "a__hgh0_prp1_cond": "none",
   "a__hgh0_prp1_neg": "yes",
   "a__hgh0_prp1_val": "1",
   "a__hgh0_ratio": "0",
   "a__low0_order": "weight",
   "a__low0_prp0_cond": "positive",
   "a__low0_prp0_connect": "and",
   "a__low0_prp0_neg": "yes",
   "a__low0_prp0_val": "1",
   "a__low0_prp1_cond": "none",
   "a__low0_prp1_neg": "yes",
   "a__low0_prp1_val": "1",
   "a__low0_ratio": "0",
   "a__low1_order": "weight",
   "a__low1_prp0_cond": "positive",
   "a__low1_prp0_connect": "and",
   "a__low1_prp0_neg": "yes",
   "a__low1_prp0_val": "1",
   "a__low1_prp1_cond": "none",
   "a__low1_prp1_neg": "yes",
   "a__low1_prp1_val": "1",
   "a__low1_ratio": "0",
}
