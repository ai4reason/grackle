import re
from .paramils import ParamilsTrainer

DOMAIN = """
full_saturate_quant {yes,no} [no]
full_saturate_quant_rd {yes,no} [yes]
quant_ind {yes,no} [no]
finite_model_find {yes,no} [no]
macros_quant {yes,no} [no]
macros_quant_mode {all,ground,ground_uf} [ground_uf]
e_matching {yes,no} [yes]
inst_when {full,full_delay,full_last_call,full_delay_last_call,last_call} [full_last_call]
fmf_inst_engine {yes,no} [no]
uf_ss {full,no_minimal,none} [full]
decision {internal,justification,justification_stoponly} [internal]
fs_interleave {yes,no} [no]
mbqi {none,fmc} [fmc]
multi_trigger_cache {yes,no} [no]
multi_trigger_priority {yes,no} [no]
multi_trigger_when_single {yes,no} [no]
multi_trigger_linear {yes,no} [yes]
inst_no_entail {yes,no} [yes]
quant_cf {yes,no} [yes]
pre_skolem_quant {yes,no} [no]
relevant_triggers {yes,no} [no]
simplification {none,batch} [batch]
term_db_mode {all,relevant} [all]
trigger_sel {min,max,min_s_max,min_s_all,all} [min]

macros_quant_mode | macros_quant in {yes}
"""

# mbqi {none,fmc,trust} [fmc]  -- `trust` was removed as being incomplete

DEFAULTS = dict(re.findall(r"^\s*(\w*).*\[(\w*)\]", DOMAIN, flags=re.MULTILINE))

class Cvc4Trainer(ParamilsTrainer):
   
   def domains(self, params):
      return DOMAIN
   

