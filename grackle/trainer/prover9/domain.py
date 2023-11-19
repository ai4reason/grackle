REPLACE = {
  
}

PARAMS = """
max_weight {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 20000} [%(max_weight)s]
order {lpo,rpo, kbo} [%(order)s]
sos_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000, 20000} [%(sos_limit)s]
max_given {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(max_given)s]
max_kept {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(max_kept)s]
max_megs {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000}  [%(max_megs)s]
fold_denial_max {0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(fold_denial_max)s]
eq_defs {unfold,fold,pass} [%(eq_defs)s]
para_lit_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(para_lit_limit)s]
new_constants {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(new_constants)s]
lex_dep_demod_lim {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(lex_dep_demod_lim)s]
demod_step_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(demod_step_limit)s]
demod_increase_limit {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(demod_increase_limit)s]
pick_given_ratio {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(pick_given_ratio)s]
age_part {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(age_part)s]
true_part {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(true_part)s]
false_part {-1, 0, 1, 10, 20, 30, 40, 50, 100, 200, 500, 1000, 1500, 2000, 5000} [%(false_part)s]

"""
CONDITIONS = ""

FORBIDDENS = """
"""

DEFAULTS = {
   "max_weight" : "-1", 
   "order" : "kbo",
   "sos_limit" : "20000",
   "max_given" : "-1", 
   "max_kept" : "-1", 
   "max_megs" : "200", 
   "fold_denial_max" : "0",
   "eq_defs" : "unfold",
   "para_lit_limit" : "-1",
   "new_constants" : "-1",
   "lex_dep_demod_lim" : "-1",
   "demod_step_limit" : "-1",
   "demod_increase_limit" : "-1",
   "pick_given_ratio" : "-1",
   "age_part" : "-1",
   "true_part" : "-1",
   "false_part" : "-1",
}
