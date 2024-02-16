PARAMS = """
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

DEFAULTS = {
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
