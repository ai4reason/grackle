
PARAMS = """
full_saturate_quant {yes,no} [%(full_saturate_quant)s] 
full_saturate_quant_rd {yes,no} [%(full_saturate_quant_rd)s] 
quant_ind {yes,no} [%(quant_ind)s] 
finite_model_find {yes,no} [%(finite_model_find)s] 
macros_quant {yes,no} [%(macros_quant)s] 
macros_quant_mode {all,ground,ground_uf} [%(macros_quant_mode)s] 
e_matching {yes,no} [%(e_matching)s] 
inst_when {full,full_delay,full_last_call,full_delay_last_call,last_call} [%(inst_when)s] 
fmf_inst_engine {yes,no} [%(fmf_inst_engine)s] 
uf_ss {full,no_minimal,none} [%(uf_ss)s] 
decision {internal,justification,justification_stoponly} [%(decision)s] 
fs_interleave {yes,no} [%(fs_interleave)s] 
mbqi {none,fmc} [%(mbqi)s] 
multi_trigger_cache {yes,no} [%(multi_trigger_cache)s] 
multi_trigger_priority {yes,no} [%(multi_trigger_priority)s] 
multi_trigger_when_single {yes,no} [%(multi_trigger_when_single)s] 
multi_trigger_linear {yes,no} [%(multi_trigger_linear)s] 
inst_no_entail {yes,no} [%(inst_no_entail)s] 
quant_cf {yes,no} [%(quant_cf)s] 
pre_skolem_quant {yes,no} [%(pre_skolem_quant)s] 
relevant_triggers {yes,no} [%(relevant_triggers)s] 
simplification {none,batch} [%(simplification)s] 
term_db_mode {all,relevant} [%(term_db_mode)s] 
trigger_sel {min,max,min_s_max,min_s_all,all} [%(trigger_sel)s] 
# new ones:
fmf_bound {yes,no} [%(fmf_bound)s] 
fmf_bound_int {yes,no} [%(fmf_bound_int)s]
fmf_bound_lazy {yes,no} [%(fmf_bound_lazy)s]
fmf_fmc_simple {yes,no} [%(fmf_fmc_simple)s]
fmf_fresh_dc {yes,no} [%(fmf_fresh_dc)s]
fmf_fun {yes,no} [%(fmf_fun)s]
fmf_fun_rlv {yes,no} [%(fmf_fun_rlv)s]
"""
# mbqi {none,fmc,trust} [fmc]  -- `trust` was removed as being incomplete
# fmf_type_completion_thresh [100,10000] [1000]

CONDITIONS = """
macros_quant_mode | macros_quant in {yes}
full_saturate_quant_rd | full_saturate_quant in {yes}
fmf_bound | finite_model_find in {yes}
fmf_bound_int | finite_model_find in {yes}
fmf_bound_lazy | finite_model_find in {yes}
fmf_fmc_simple | finite_model_find in {yes}
fmf_fresh_dc | finite_model_find in {yes}
fmf_fun | finite_model_find in {yes}
fmf_fun_rlv | finite_model_find in {yes}
fmf_inst_engine | finite_model_find in {yes}
fmf_bound_lazy | fmf_bound in {yes}
fmf_bound_int | fmf_bound in {yes}
"""

FORBIDDENS = """
{full_saturate_quant=yes, finite_model_find=yes}
"""

DEFAULTS = {
   'full_saturate_quant': 'no', 
   'full_saturate_quant_rd': 'yes', 
   'quant_ind': 'no', 
   'finite_model_find': 'no', 
   'macros_quant': 'no', 
   'macros_quant_mode': 'ground_uf', 
   'e_matching': 'yes', 
   'inst_when': 'full_last_call', 
   'fmf_inst_engine': 'no', 
   'uf_ss': 'full', 
   'decision': 'internal', 
   'fs_interleave': 'no', 
   'mbqi': 'fmc', 
   'multi_trigger_cache': 'no', 
   'multi_trigger_priority': 'no', 
   'multi_trigger_when_single': 'no', 
   'multi_trigger_linear': 'yes', 
   'inst_no_entail': 'yes', 
   'quant_cf': 'yes', 
   'pre_skolem_quant': 'no', 
   'relevant_triggers': 'no', 
   'simplification': 'batch', 
   'term_db_mode': 'all', 
   'trigger_sel': 'min',
   'fmf_bound': 'no', 
   'fmf_bound_int': 'no', 
   'fmf_bound_lazy': 'no', 
   'fmf_fmc_simple': 'yes', 
   'fmf_fresh_dc': 'no', 
   'fmf_fun': 'no', 
   'fmf_fun_rlv': 'no', 
   'fmf_inst_engine': 'yes', 
}

