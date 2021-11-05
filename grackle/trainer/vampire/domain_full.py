
REPLACE = {
   "selection" : "-",
   "avatar_split_queue_ratios" : ",",
   "positive_literal_split_queue_ratios" : ",",
   "sine_level_split_queue_ratios" : ",",
   "sine_level_split_queue_cutoffs" : ",",
   "age_weight_ratio" : ":",
   "inst_gen_resolution_ratio" : "/",
}

PARAMS = """
age_weight_ratio {__1_1,__1_2,__2_1,__1_4,__4_1,__1_10,__1_1024,__1_12,__1_128,__1_14,__1_16,__1_20,__1_24,__1_28,__1_3,__1_32,__1_40,__1_5,__1_50,__1_6,__1_64,__1_7,__1_8,__2_3,__3_1,__3_2,__5_1,__5_4,__8_1} [%(age_weight_ratio)s]
age_weight_ratio_shape {constant,decay,converge} [%(age_weight_ratio_shape)s]
age_weight_ratio_shape_frequency {100,1,128,16,2,256,32,4,512,64,8} [%(age_weight_ratio_shape_frequency)s]
avatar {off,on} [%(avatar)s]
avatar_add_complementary {ground,none} [%(avatar_add_complementary)s]
avatar_buffered_solver {off,on} [%(avatar_buffered_solver)s]
avatar_congruence_closure {model,off,on} [%(avatar_congruence_closure)s]
avatar_delete_deactivated {on,large,off} [%(avatar_delete_deactivated)s]
avatar_eager_removal {off,on} [%(avatar_eager_removal)s]
avatar_fast_restart {off,on} [%(avatar_fast_restart)s]
avatar_flush_period {0,1000,10000,100000,4000,40000} [%(avatar_flush_period)s]
avatar_flush_quotient {1.0,1.1,1.2,1.4,1.5,2.0} [%(avatar_flush_quotient)s]
avatar_literal_polarity_advice {false,true,none} [%(avatar_literal_polarity_advice)s]
avatar_minimize_model {off,sco,all} [%(avatar_minimize_model)s]
avatar_nonsplittable_components {all,all_dependent,known,none} [%(avatar_nonsplittable_components)s]
avatar_split_queue {off,on} [%(avatar_split_queue)s]
avatar_split_queue_cutoffs {0,1,2} [%(avatar_split_queue_cutoffs)s]
avatar_split_queue_layered_arrangement {off,on} [%(avatar_split_queue_layered_arrangement)s]
avatar_split_queue_ratios {__1_4,__1_1,__4_1} [%(avatar_split_queue_ratios)s]
avatar_turn_off_time_frac {0,0.2,0.4,0.6,0.8} [%(avatar_turn_off_time_frac)s]
backward_demodulation {all,off,preordered} [%(backward_demodulation)s]
backward_subsumption {off,on,unit_only} [%(backward_subsumption)s]
backward_subsumption_demodulation {off,on} [%(backward_subsumption_demodulation)s]
backward_subsumption_demodulation_max_matches {0,1,3} [%(backward_subsumption_demodulation_max_matches)s]
backward_subsumption_resolution {off,on,unit_only} [%(backward_subsumption_resolution)s]
binary_resolution {off,on} [%(binary_resolution)s]
blocked_clause_elimination {off,on} [%(blocked_clause_elimination)s]
cc_unsat_cores {first,small_ones,all} [%(cc_unsat_cores)s]
condensation {fast,off,on} [%(condensation)s]
demodulation_redundancy_check {off,on} [%(demodulation_redundancy_check)s]
equality_proxy {R,RS,RST,RSTC,off} [%(equality_proxy)s]
equality_resolution_with_deletion {input_only,off} [%(equality_resolution_with_deletion)s]
equational_tautology_removal {off,on} [%(equational_tautology_removal)s]
extensionality_resolution {filter,known,off} [%(extensionality_resolution)s]
fmb_adjust_sorts {off,expand,group,function} [%(fmb_adjust_sorts)s]
fmb_detect_sort_bounds {off,on} [%(fmb_detect_sort_bounds)s]
fmb_enumeration_strategy {sbeam,contour} [%(fmb_enumeration_strategy)s]
fmb_size_weight_ratio {0,1,2,3,4} [%(fmb_size_weight_ratio)s]
fmb_start_size {1,2,4,8} [%(fmb_start_size)s]
fmb_symmetry_ratio {1,1.1,1.2,1.3,1.4,1.5,1.6,2.0} [%(fmb_symmetry_ratio)s]
fmb_symmetry_symbol_order {occurence,input_usage,preprocessed_usage} [%(fmb_symmetry_symbol_order)s]
fmb_symmetry_widget_order {function_first,argument_first,diagonal} [%(fmb_symmetry_widget_order)s]
forward_demodulation {all,off,preordered} [%(forward_demodulation)s]
forward_literal_rewriting {off,on} [%(forward_literal_rewriting)s]
forward_subsumption {off,on} [%(forward_subsumption)s]
forward_subsumption_demodulation {off,on} [%(forward_subsumption_demodulation)s]
forward_subsumption_demodulation_max_matches {0,1,3} [%(forward_subsumption_demodulation_max_matches)s]
forward_subsumption_resolution {off,on} [%(forward_subsumption_resolution)s]
function_definition_elimination {all,none,unused} [%(function_definition_elimination)s]
general_splitting {input_only,off} [%(general_splitting)s]
global_subsumption {off,on} [%(global_subsumption)s]
global_subsumption_avatar_assumptions {off,from_current,full_model} [%(global_subsumption_avatar_assumptions)s]
global_subsumption_explicit_minim {off,on,randomized} [%(global_subsumption_explicit_minim)s]
global_subsumption_sat_solver_power {propagation_only,full} [%(global_subsumption_sat_solver_power)s]
inequality_splitting {0,3} [%(inequality_splitting)s]
inner_rewriting {off,on} [%(inner_rewriting)s]
inst_gen_big_restart_ratio {0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,1.0} [%(inst_gen_big_restart_ratio)s]
inst_gen_passive_reactivation {off,on} [%(inst_gen_passive_reactivation)s]
inst_gen_resolution_ratio {__1_1,__1_128,__1_16,__1_2,__1_32,__1_4,__1_64,__1_8,__128_1,__16_1,__32_1,__64_1} [%(inst_gen_resolution_ratio)s]
inst_gen_restart_period {1000,100,1400,200,2000,400,4000,700} [%(inst_gen_restart_period)s]
inst_gen_restart_period_quotient {1,1.05,1.1,1.2,1.3,1.5,2.0} [%(inst_gen_restart_period_quotient)s]
inst_gen_selection {0,1,1002,1003,1004,1010} [%(inst_gen_selection)s]
inst_gen_with_resolution {off,on} [%(inst_gen_with_resolution)s]
literal_comparison_mode {predicate,reverse,standard} [%(literal_comparison_mode)s]
literal_maximality_aftercheck {off,on} [%(literal_maximality_aftercheck)s]
lrs_weight_limit_only {off,on} [%(lrs_weight_limit_only)s]
naming {8,0,1024,16,2,32,4,6,64} [%(naming)s]
newcnf {off,on} [%(newcnf)s]
nongoal_weight_coefficient {1,1.1,1.2,1.3,1.5,1.7,10,2,2.5,3,4,5} [%(nongoal_weight_coefficient)s]
nonliterals_in_clause_weight {off,on} [%(nonliterals_in_clause_weight)s]
positive_literal_split_queue {off,on} [%(positive_literal_split_queue)s]
positive_literal_split_queue_cutoffs {0,1,2} [%(positive_literal_split_queue_cutoffs)s]
positive_literal_split_queue_layered_arrangement {off,on} [%(positive_literal_split_queue_layered_arrangement)s]
positive_literal_split_queue_ratios {__1_4,__1_1,__4_1} [%(positive_literal_split_queue_ratios)s]
restrict_nwc_to_goal_constants {off,on} [%(restrict_nwc_to_goal_constants)s]
sat_solver {minisat} [%(sat_solver)s]
saturation_algorithm {discount,fmb,inst_gen,lrs,otter} [%(saturation_algorithm)s]
selection {_1,1,_10,10,1002,1003,1004,1010,1011,_11,11,_2,2,_3,3,_4,4} [%(selection)s]
simultaneous_superposition {off,on} [%(simultaneous_superposition)s]
sine_depth {0,1,10,2,3,4,5,7} [%(sine_depth)s]
sine_generality_threshold {0,1,2,4,8,16,32,64} [%(sine_generality_threshold)s]
sine_level_split_queue {off,on} [%(sine_level_split_queue)s]
sine_level_split_queue_cutoffs {__0_1,__0_2,__1_2} [%(sine_level_split_queue_cutoffs)s]
sine_level_split_queue_layered_arrangement {off,on} [%(sine_level_split_queue_layered_arrangement)s]
sine_level_split_queue_ratios {__1_2_3,__3_2_1,__1_3_2,__1_1_1} [%(sine_level_split_queue_ratios)s]
sine_selection {axioms,included,off} [%(sine_selection)s]
sine_to_age {off,on} [%(sine_to_age)s]
sine_to_age_generality_threshold {0,1,2,4,8,16,32,64} [%(sine_to_age_generality_threshold)s]
sine_to_age_tolerance {1.0,1.5,4.0,5.0} [%(sine_to_age_tolerance)s]
sine_to_pred_levels {no,off,on} [%(sine_to_pred_levels)s]
sine_tolerance {1,1.2,1.5,2.0,3.0,5.0} [%(sine_tolerance)s]
sos {all,off,on,theory} [%(sos)s]
split_at_activation {off,on} [%(split_at_activation)s]
superposition_from_variables {off,on} [%(superposition_from_variables)s]
symbol_precedence {arity,occurrence,reverse_arity,frequency,reverse_frequency} [%(symbol_precedence)s]
symbol_precedence_boost {none,goal,units,goal_then_units} [%(symbol_precedence_boost)s]
term_ordering {kbo,lpo} [%(term_ordering)s]
unit_resulting_resolution {ec_only,off,on} [%(unit_resulting_resolution)s]
unused_predicate_definition_removal {off,on} [%(unused_predicate_definition_removal)s]
"""

CONDITIONS = """
avatar_add_complementary | avatar in {on}
avatar_buffered_solver | avatar in {on}
avatar_congruence_closure | avatar in {on}
avatar_delete_deactivated | avatar in {on}
avatar_fast_restart | avatar in {on}
avatar_flush_period | avatar in {on}
avatar_flush_quotient | avatar in {on}
avatar_literal_polarity_advice | avatar in {on}
avatar_minimize_model | avatar in {on}
avatar_nonsplittable_components | avatar in {on}
nonliterals_in_clause_weight | avatar in {on}
split_at_activation | avatar in {on}
avatar_split_queue_cutoffs | avatar_split_queue in {on}
avatar_split_queue_layered_arrangement | avatar_split_queue in {on}
avatar_split_queue_ratios | avatar_split_queue in {on}
fmb_enumeration_strategy | fmb_adjust_sorts in {off,group,function}
global_subsumption_explicit_minim | global_subsumption in {on}
global_subsumption_sat_solver_power | global_subsumption in {on}
extensionality_resolution | inequality_splitting in {0}
restrict_nwc_to_goal_constants | nongoal_weight_coefficient in {1.1,1.2,1.3,1.5,1.7,10,2,2.5,3,4,5}
positive_literal_split_queue_cutoffs | positive_literal_split_queue in {on}
positive_literal_split_queue_layered_arrangement | positive_literal_split_queue in {on}
positive_literal_split_queue_ratios | positive_literal_split_queue in {on}
equality_proxy | saturation_algorithm in {discount,inst_gen,lrs,otter}
inst_gen_big_restart_ratio | saturation_algorithm in {inst_gen}
inst_gen_passive_reactivation | saturation_algorithm in {inst_gen}
inst_gen_restart_period | saturation_algorithm in {inst_gen}
inst_gen_restart_period_quotient | saturation_algorithm in {inst_gen}
inst_gen_selection | saturation_algorithm in {inst_gen}
inst_gen_with_resolution | saturation_algorithm in {inst_gen}
sine_selection | saturation_algorithm in {discount,inst_gen,lrs,otter}
sine_level_split_queue_cutoffs | sine_level_split_queue in {on}
sine_level_split_queue_layered_arrangement | sine_level_split_queue in {on}
sine_level_split_queue_ratios | sine_level_split_queue in {on}
binary_resolution | unit_resulting_resolution in {ec_only,on}
cc_unsat_cores | avatar_congruence_closure in {model,on}
fmb_size_weight_ratio | fmb_enumeration_strategy in {contour}
inst_gen_resolution_ratio | inst_gen_with_resolution in {on}
sine_tolerance | sine_selection in {axioms,included}
forward_subsumption | forward_subsumption_resolution in {off}
global_subsumption_avatar_assumptions | avatar in {on}
global_subsumption_avatar_assumptions | global_subsumption in {on}
avatar_eager_removal | avatar in {on}
avatar_eager_removal | avatar_minimize_model in {all}
avatar_turn_off_time_frac | avatar in {on}
inst_gen_selection | saturation_algorithm in {inst_gen}
sine_depth | sine_selection in {axioms,included}
sine_generality_threshold | sine_selection in {axioms,included}
fmb_detect_sort_bounds | fmb_adjust_sorts in {off,expand,group}
sine_to_pred_levels | literal_comparison_mode in {standard}
"""

FORBIDDENS = """
{age_weight_ratio=__1_2,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__2_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_4,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__4_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_10,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_1024,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_12,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_128,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_14,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_16,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_20,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_24,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_28,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_3,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_32,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_40,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_5,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_50,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_6,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_64,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_7,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__1_8,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__2_3,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__3_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__3_2,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__5_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__5_4,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{age_weight_ratio=__8_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_demodulation=off,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_demodulation=preordered,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_subsumption=on,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_subsumption=unit_only,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_subsumption_resolution=on,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{backward_subsumption_resolution=unit_only,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{condensation=fast,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{condensation=on,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{demodulation_redundancy_check=off,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{forward_literal_rewriting=on,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{forward_subsumption_resolution=off,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_10,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1002,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1003,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1004,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1010,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=1011,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_11,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=11,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_2,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=2,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_3,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=3,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=_4,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{selection=4,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{superposition_from_variables=off,saturation_algorithm=inst_gen,inst_gen_with_resolution=off}
{sine_to_age_generality_threshold=1,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=2,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=4,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=8,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=16,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=32,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=64,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_tolerance=1.5,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_tolerance=4.0,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_tolerance=5.0,sine_to_age=off,sine_to_pred_levels=off}
{sine_to_age_generality_threshold=1,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=2,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=4,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=8,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=16,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=32,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=64,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_tolerance=1.5,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_tolerance=4.0,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_tolerance=5.0,sine_to_age=off,literal_comparison_mode=predicate}
{sine_to_age_generality_threshold=1,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=2,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=4,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=8,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=16,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=32,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_generality_threshold=64,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_tolerance=1.5,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_tolerance=4.0,sine_to_age=off,literal_comparison_mode=reverse}
{sine_to_age_tolerance=5.0,sine_to_age=off,literal_comparison_mode=reverse}
{avatar_congruence_closure=model,avatar_minimize_model=sco}
{saturation_algorithm=inst_gen,avatar=on}
{selection=1002,inst_gen_with_resolution=off,saturation_algorithm=inst_gen}
{selection=1003,inst_gen_with_resolution=off,saturation_algorithm=inst_gen}
{selection=1004,inst_gen_with_resolution=off,saturation_algorithm=inst_gen}
{selection=1010,inst_gen_with_resolution=off,saturation_algorithm=inst_gen}
{selection=1011,inst_gen_with_resolution=off,saturation_algorithm=inst_gen}
"""


DEFAULTS = {
   "age_weight_ratio": "__1_1",
   "age_weight_ratio_shape": "constant",
   "age_weight_ratio_shape_frequency": "100",
   "avatar": "on",
   "avatar_add_complementary": "ground",
   "avatar_buffered_solver": "off",
   "avatar_congruence_closure": "off",
   "avatar_delete_deactivated": "on",
   "avatar_eager_removal": "on",
   "avatar_fast_restart": "off",
   "avatar_flush_period": "0",
   "avatar_flush_quotient": "1.5",
   "avatar_literal_polarity_advice": "none",
   "avatar_minimize_model": "all",
   "avatar_nonsplittable_components": "known",
   "avatar_split_queue": "off",
   "avatar_split_queue_cutoffs": "0",
   "avatar_split_queue_layered_arrangement": "off",
   "avatar_split_queue_ratios": "__1_1",
   "avatar_turn_off_time_frac": "0",
   "backward_demodulation": "all",
   "backward_subsumption": "off",
   "backward_subsumption_demodulation": "off",
   "backward_subsumption_demodulation_max_matches": "0",
   "backward_subsumption_resolution": "off",
   "binary_resolution": "on",
   "blocked_clause_elimination": "off",
   "cc_unsat_cores": "all",
   "condensation": "off",
   "demodulation_redundancy_check": "on",
   "equality_proxy": "off",
   "equality_resolution_with_deletion": "input_only",
   "equational_tautology_removal": "off",
   "extensionality_resolution": "off",
   "fmb_adjust_sorts": "group",
   "fmb_detect_sort_bounds": "off",
   "fmb_enumeration_strategy": "sbeam",
   "fmb_size_weight_ratio": "1",
   "fmb_start_size": "1",
   "fmb_symmetry_ratio": "1",
   "fmb_symmetry_symbol_order": "occurence",
   "fmb_symmetry_widget_order": "function_first",
   "forward_demodulation": "all",
   "forward_literal_rewriting": "off",
   "forward_subsumption": "on",
   "forward_subsumption_demodulation": "off",
   "forward_subsumption_demodulation_max_matches": "0",
   "forward_subsumption_resolution": "on",
   "function_definition_elimination": "all",
   "general_splitting": "off",
   "global_subsumption": "off",
   "global_subsumption_avatar_assumptions": "off",
   "global_subsumption_explicit_minim": "randomized",
   "global_subsumption_sat_solver_power": "propagation_only",
   "inequality_splitting": "0",
   "inner_rewriting": "off",
   "inst_gen_big_restart_ratio": "0",
   "inst_gen_passive_reactivation": "off",
   "inst_gen_resolution_ratio": "__1_1",
   "inst_gen_restart_period": "1000",
   "inst_gen_restart_period_quotient": "1",
   "inst_gen_selection": "0",
   "inst_gen_with_resolution": "off",
   "literal_comparison_mode": "standard",
   "literal_maximality_aftercheck": "off",
   "lrs_weight_limit_only": "off",
   "naming": "8",
   "newcnf": "off",
   "nongoal_weight_coefficient": "1",
   "nonliterals_in_clause_weight": "off",
   "positive_literal_split_queue": "off",
   "positive_literal_split_queue_cutoffs": "0",
   "positive_literal_split_queue_layered_arrangement": "off",
   "positive_literal_split_queue_ratios": "__1_4",
   "restrict_nwc_to_goal_constants": "off",
   "sat_solver": "minisat",
   "saturation_algorithm": "lrs",
   "selection": "10",
   "simultaneous_superposition": "on",
   "sine_depth": "0",
   "sine_generality_threshold": "0",
   "sine_level_split_queue": "off",
   "sine_level_split_queue_cutoffs": "__0_1",
   "sine_level_split_queue_layered_arrangement": "on",
   "sine_level_split_queue_ratios": "__1_2_3",
   "sine_selection": "off",
   "sine_to_age": "off",
   "sine_to_age_generality_threshold": "0",
   "sine_to_age_tolerance": "1.0",
   "sine_to_pred_levels": "off",
   "sine_tolerance": "1",
   "sos": "off",
   "split_at_activation": "off",
   "superposition_from_variables": "on",
   "symbol_precedence": "arity",
   "symbol_precedence_boost": "none",
   "term_ordering": "kbo",
   "unit_resulting_resolution": "off",
   "unused_predicate_definition_removal": "on",
}

