
REPLACE = {
   "selection" : "-",
   "age_weight_ratio" : ":",
}

PARAMS = """
age_weight_ratio {__1_1,__1_2,__2_1,__1_4,__4_1,__1_10,__1_1024,__1_12,__1_128,__1_14,__1_16,__1_20,__1_24,__1_28,__1_3,__1_32,__1_40,__1_5,__1_50,__1_6,__1_64,__1_7,__1_8,__2_3,__3_1,__3_2,__5_1,__5_4,__8_1} [%(age_weight_ratio)s]
age_weight_ratio_shape {constant,decay,converge} [%(age_weight_ratio_shape)s]
age_weight_ratio_shape_frequency {100,1,128,16,2,256,32,4,512,64,8} [%(age_weight_ratio_shape_frequency)s]
avatar {off,on} [%(avatar)s]
avatar_add_complementary {ground,none} [%(avatar_add_complementary)s]
avatar_congruence_closure {model,off,on} [%(avatar_congruence_closure)s]
avatar_fast_restart {off,on} [%(avatar_fast_restart)s]
avatar_flush_period {0,1000,10000,100000,4000,40000} [%(avatar_flush_period)s]
avatar_flush_quotient {1.0,1.1,1.2,1.4,1.5,2.0} [%(avatar_flush_quotient)s]
avatar_minimize_model {off,sco,all} [%(avatar_minimize_model)s]
avatar_nonsplittable_components {all,all_dependent,known,none} [%(avatar_nonsplittable_components)s]
backward_demodulation {all,off,preordered} [%(backward_demodulation)s]
backward_subsumption {off,on,unit_only} [%(backward_subsumption)s]
backward_subsumption_resolution {off,on,unit_only} [%(backward_subsumption_resolution)s]
binary_resolution {off,on} [%(binary_resolution)s]
cc_unsat_cores {first,small_ones,all} [%(cc_unsat_cores)s]
condensation {fast,off,on} [%(condensation)s]
extensionality_resolution {filter,known,off} [%(extensionality_resolution)s]
function_definition_elimination {all,none,unused} [%(function_definition_elimination)s]
general_splitting {input_only,off} [%(general_splitting)s]
global_subsumption {off,on} [%(global_subsumption)s]
global_subsumption_explicit_minim {off,on,randomized} [%(global_subsumption_explicit_minim)s]
inner_rewriting {off,on} [%(inner_rewriting)s]
literal_comparison_mode {predicate,reverse,standard} [%(literal_comparison_mode)s]
literal_maximality_aftercheck {off,on} [%(literal_maximality_aftercheck)s]
lrs_weight_limit_only {off,on} [%(lrs_weight_limit_only)s]
naming {8,0,1024,16,2,32,4,6,64} [%(naming)s]
newcnf {off,on} [%(newcnf)s]
nongoal_weight_coefficient {1,1.1,1.2,1.3,1.5,1.7,10,2,2.5,3,4,5} [%(nongoal_weight_coefficient)s]
nonliterals_in_clause_weight {off,on} [%(nonliterals_in_clause_weight)s]
sat_solver {minisat} [%(sat_solver)s]
saturation_algorithm {discount,fmb,inst_gen,lrs,otter} [%(saturation_algorithm)s]
selection {_1,1,_10,10,1002,1003,1004,1010,1011,_11,11,_2,2,_3,3,_4,4} [%(selection)s]
sine_depth {0,1,10,2,3,4,5,7} [%(sine_depth)s]
sine_selection {axioms,included,off} [%(sine_selection)s]
sine_to_age {off,on} [%(sine_to_age)s]
sine_tolerance {1,1.2,1.5,2.0,3.0,5.0} [%(sine_tolerance)s]
sos {all,off,on,theory} [%(sos)s]
symbol_precedence {arity,occurrence,reverse_arity,frequency,reverse_frequency} [%(symbol_precedence)s]
term_ordering {kbo,lpo} [%(term_ordering)s]
unit_resulting_resolution {ec_only,off,on} [%(unit_resulting_resolution)s]
unused_predicate_definition_removal {off,on} [%(unused_predicate_definition_removal)s]
"""

CONDITIONS = """
avatar_add_complementary | avatar in {on}
avatar_congruence_closure | avatar in {on}
avatar_fast_restart | avatar in {on}
avatar_flush_period | avatar in {on}
avatar_flush_quotient | avatar in {on}
avatar_minimize_model | avatar in {on}
avatar_nonsplittable_components | avatar in {on}
nonliterals_in_clause_weight | avatar in {on}
global_subsumption_explicit_minim | global_subsumption in {on}
sine_selection | saturation_algorithm in {discount,inst_gen,lrs,otter}
binary_resolution | unit_resulting_resolution in {ec_only,on}
cc_unsat_cores | avatar_congruence_closure in {model,on}
sine_tolerance | sine_selection in {axioms,included}
sine_depth | sine_selection in {axioms,included}
"""

FORBIDDENS = """
{avatar_congruence_closure=model,avatar_minimize_model=sco}
{saturation_algorithm=inst_gen,avatar=on}
"""


DEFAULTS = {
   "age_weight_ratio": "__1_1",
   "age_weight_ratio_shape": "constant",
   "age_weight_ratio_shape_frequency": "100",
   "avatar": "on",
   "avatar_add_complementary": "ground",
   "avatar_congruence_closure": "off",
   "avatar_fast_restart": "off",
   "avatar_flush_period": "0",
   "avatar_flush_quotient": "1.5",
   "avatar_minimize_model": "all",
   "avatar_nonsplittable_components": "known",
   "backward_demodulation": "all",
   "backward_subsumption": "off",
   "backward_subsumption_resolution": "off",
   "binary_resolution": "on",
   "cc_unsat_cores": "all",
   "condensation": "off",
   "extensionality_resolution": "off",
   "function_definition_elimination": "all",
   "general_splitting": "off",
   "global_subsumption": "off",
   "global_subsumption_explicit_minim": "randomized",
   "inner_rewriting": "off",
   "literal_comparison_mode": "standard",
   "literal_maximality_aftercheck": "off",
   "lrs_weight_limit_only": "off",
   "naming": "8",
   "newcnf": "off",
   "nongoal_weight_coefficient": "1",
   "nonliterals_in_clause_weight": "off",
   "sat_solver": "minisat",
   "saturation_algorithm": "lrs",
   "selection": "10",
   "sine_depth": "0",
   "sine_selection": "off",
   "sine_to_age": "off",
   "sine_tolerance": "1",
   "sos": "off",
   "symbol_precedence": "arity",
   "term_ordering": "kbo",
   "unit_resulting_resolution": "off",
   "unused_predicate_definition_removal": "on",
}

