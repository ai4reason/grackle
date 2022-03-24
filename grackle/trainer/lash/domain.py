
### UNUSED FLAGS:
#
# CHOICE_AS_DEFAULT {false} [false]
# HOUNIF1IMITATE {1} [1]
# HOUNIF1PROJECT {1} [1]
# USE_E {false,true} [false]
# USE_MODELS {false,true} [false]
# USE_SINE {false,true} [false]
# SINE_DEPTH {0} [0]
# SINE_GENERALITY_THRESHOLD {0,4} [0]
# SINE_RANK_LIMIT {2,3,4} [3]
# SINE_TOLERANCE {1.0,1.2} [1.2]
#

PARAMS = """
ALL_DEFS_AS_EQNS {false,true} [%(ALL_DEFS_AS_EQNS)s]
APPLY_PATTERN_CLAUSES_EARLY {false,true} [%(APPLY_PATTERN_CLAUSES_EARLY)s]
AP_WEIGHT {1,100} [%(AP_WEIGHT)s]
ARTP_WEIGHT {0,1} [%(ARTP_WEIGHT)s]
AXIOM_DELAY {0,1,4,5} [%(AXIOM_DELAY)s]
BASETP_WEIGHT {0,1} [%(BASETP_WEIGHT)s]
BASETYPESFINITE {false,true} [%(BASETYPESFINITE)s]
BASETYPESMAXSIZE {1,2,3} [%(BASETYPESMAXSIZE)s]
BASETYPESTOPROP {false,true} [%(BASETYPESTOPROP)s]
CHOICE_EMPTY_DELAY {0,1,1000} [%(CHOICE_EMPTY_DELAY)s]
CHOICE_IN_DELAY {0,1,1000} [%(CHOICE_IN_DELAY)s]
CHOICE_TP_WEIGHT_FAC {1,100} [%(CHOICE_TP_WEIGHT_FAC)s]
CHOICE_WEIGHT {1,100} [%(CHOICE_WEIGHT)s]
CONFR_DIFF_DELAY {0,1,20,100,500,1000} [%(CONFR_DIFF_DELAY)s]
CONFR_SAME1_DELAY {0,1,5,10,20,100,500,1000} [%(CONFR_SAME1_DELAY)s]
CONFR_SAME2_DELAY {0,1,10,20,100,1000} [%(CONFR_SAME2_DELAY)s]
DB_TP_WEIGHT_FAC {1,100} [%(DB_TP_WEIGHT_FAC)s]
DB_WEIGHT {1,100} [%(DB_WEIGHT)s]
DEFAULTELTINST_DELAY {0,1,10,30,100,1000} [%(DEFAULTELTINST_DELAY)s]
DEFAULTELT_DELAY {0,1,10,30,50,100,1000} [%(DEFAULTELT_DELAY)s]
DELAY_FO {0,1,2,4,8,10,16} [%(DELAY_FO)s]
DELAY_FO_CLAUSE {0,1,2,4,8,16} [%(DELAY_FO_CLAUSE)s]
DELAY_FO_LIT {0,1,2,4,8} [%(DELAY_FO_LIT)s]
DELAY_SEMANTIC_EQUIV_INSTANTIATION {0,1} [%(DELAY_SEMANTIC_EQUIV_INSTANTIATION)s]
DYNAMIC_PATTERN_CLAUSES {false,true} [%(DYNAMIC_PATTERN_CLAUSES)s]
EAGERLY_PROCESS_INSTANTIATIONS {false,true} [%(EAGERLY_PROCESS_INSTANTIATIONS)s]
ENABLE_PATTERN_CLAUSES {false,true} [%(ENABLE_PATTERN_CLAUSES)s]
ENUM_ARROW {1,10,20,100} [%(ENUM_ARROW)s]
ENUM_CHOICE {0,2,10,20,50,100,200,500} [%(ENUM_CHOICE)s]
ENUM_EQ {0,1,2,5,10,20,100,500} [%(ENUM_EQ)s]
ENUM_FALSE {0,20,50,100,200,500} [%(ENUM_FALSE)s]
ENUM_FORALL {1,20,50,100} [%(ENUM_FORALL)s]
ENUM_IMP {0,1,2,20,50,100,200,500} [%(ENUM_IMP)s]
ENUM_ITER_DEEP {false,true} [%(ENUM_ITER_DEEP)s]
ENUM_ITER_DEEP_DELAY {5,100,1000,5000} [%(ENUM_ITER_DEEP_DELAY)s]
ENUM_ITER_DEEP_INCR {0,1} [%(ENUM_ITER_DEEP_INCR)s]
ENUM_ITER_DEEP_INIT {1,2,3,4,6,7,8,9,10} [%(ENUM_ITER_DEEP_INIT)s]
ENUM_NEG {0,1,5,10,25,50,100,500} [%(ENUM_NEG)s]
ENUM_O {0,2,5,20,50,100,200,500} [%(ENUM_O)s]
ENUM_SORT {0,2,10,20,200,500} [%(ENUM_SORT)s]
ENUM_START {0,1,2,10,20,30,1000,2000} [%(ENUM_START)s]
EQ_TP_WEIGHT_FAC {1,100} [%(EQ_TP_WEIGHT_FAC)s]
EQ_WEIGHT {1,100} [%(EQ_WEIGHT)s]
EXISTSTOCHOICE {false,true} [%(EXISTSTOCHOICE)s]
EXISTS_DELAY {0,1,2,4,10,15,17,20} [%(EXISTS_DELAY)s]
E_AUTOSCHEDULE {false,true} [%(E_AUTOSCHEDULE)s]
E_EQO_EQUIV {false,true} [%(E_EQO_EQUIV)s]
E_PERIOD {10,100,300,1000} [%(E_PERIOD)s]
E_TIMEOUT {1,2,3,4,10,22,30} [%(E_TIMEOUT)s]
FALSE_WEIGHT {1,100} [%(FALSE_WEIGHT)s]
FILTER_INCR {1,5} [%(FILTER_INCR)s]
FILTER_NEGATM {false,true} [%(FILTER_NEGATM)s]
FILTER_NEGATM_USABLE {false,true} [%(FILTER_NEGATM_USABLE)s]
FILTER_NEGEQ {false,true} [%(FILTER_NEGEQ)s]
FILTER_NEGEQ_USABLE {false,true} [%(FILTER_NEGEQ_USABLE)s]
FILTER_POSATM {false,true} [%(FILTER_POSATM)s]
FILTER_POSATM_USABLE {false,true} [%(FILTER_POSATM_USABLE)s]
FILTER_POSEQ {false,true} [%(FILTER_POSEQ)s]
FILTER_POSEQ_USABLE {false,true} [%(FILTER_POSEQ_USABLE)s]
FILTER_START {0,5} [%(FILTER_START)s]
FILTER_UNIV {false,true} [%(FILTER_UNIV)s]
FILTER_UNIV_USABLE {false,true} [%(FILTER_UNIV_USABLE)s]
FORALL_DELAY {0,1,2,3,6,7,9,10,16,20,1000} [%(FORALL_DELAY)s]
FORALL_TP_WEIGHT_FAC {1,100} [%(FORALL_TP_WEIGHT_FAC)s]
FORALL_WEIGHT {1,100} [%(FORALL_WEIGHT)s]
HOUNIF1 {false,true} [%(HOUNIF1)s]
HOUNIF1BOUND {1,4,10,16} [%(HOUNIF1BOUND)s]
HOUNIF1MATE {false,true} [%(HOUNIF1MATE)s]
HOUNIF1MATEBELOWEQUIV {false,true} [%(HOUNIF1MATEBELOWEQUIV)s]
HOUNIF1MATENONLITS {false,true} [%(HOUNIF1MATENONLITS)s]
HOUNIF1MAXMATES {1,2} [%(HOUNIF1MAXMATES)s]
HOUNIF1NEGFLEX {false,true} [%(HOUNIF1NEGFLEX)s]
IMITATE_DEFNS {false,true} [%(IMITATE_DEFNS)s]
IMITATE_DEFN_DELAY {0,100,1000} [%(IMITATE_DEFN_DELAY)s]
IMITATE_DELAY {0,1,2,3,4,5,6,9,10,30,100,1000} [%(IMITATE_DELAY)s]
IMP_WEIGHT {1,100} [%(IMP_WEIGHT)s]
INITIAL_SUBTERMS_AS_INSTANTIATIONS {false,true} [%(INITIAL_SUBTERMS_AS_INSTANTIATIONS)s]
INSTANTIATE_WITH_FUNC_DISEQN_SIDES {false,true} [%(INSTANTIATE_WITH_FUNC_DISEQN_SIDES)s]
INSTANTIATION_DELAY {0,1} [%(INSTANTIATION_DELAY)s]
INSTANTIATION_ORDER_CYCLE {1,2,3,4,6,7,8} [%(INSTANTIATION_ORDER_CYCLE)s]
INSTANTIATION_ORDER_MASK {0,1,2,3,4,5,6,7,8,14,40,46,52,62,68,79,108,129,165,198,207,228,229,249,252,253,254} [%(INSTANTIATION_ORDER_MASK)s]
LAM_TP_WEIGHT_FAC {1,100} [%(LAM_TP_WEIGHT_FAC)s]
LAM_WEIGHT {1,100} [%(LAM_WEIGHT)s]
LEIBEQ_TO_PRIMEQ {false,true} [%(LEIBEQ_TO_PRIMEQ)s]
MINISAT_SEARCH_PERIOD {1,10,1000000000} [%(MINISAT_SEARCH_PERIOD)s]
NAME_TP_WEIGHT_FAC {0,1} [%(NAME_TP_WEIGHT_FAC)s]
NAME_WEIGHT {0,1} [%(NAME_WEIGHT)s]
NEW_HEAD_ENUM_DELAY {0,4,10,200,1000} [%(NEW_HEAD_ENUM_DELAY)s]
NOT_IN_PROP_MODEL_DELAY {0,1,2,5} [%(NOT_IN_PROP_MODEL_DELAY)s]
OTP_WEIGHT {0,1} [%(OTP_WEIGHT)s]
PATTERN_CLAUSES_DELAY {0,1,2,3,6} [%(PATTERN_CLAUSES_DELAY)s]
PATTERN_CLAUSES_EARLY {false,true} [%(PATTERN_CLAUSES_EARLY)s]
PATTERN_CLAUSES_EQNLITS {false,true} [%(PATTERN_CLAUSES_EQNLITS)s]
PATTERN_CLAUSES_EQN_DELAY {0,1,3} [%(PATTERN_CLAUSES_EQN_DELAY)s]
PATTERN_CLAUSES_FORALL_AS_LIT {false,true} [%(PATTERN_CLAUSES_FORALL_AS_LIT)s]
PATTERN_CLAUSES_ONLYALLSTRICT {false,true} [%(PATTERN_CLAUSES_ONLYALLSTRICT)s]
PATTERN_CLAUSES_TRANSITIVITY_EQ {false,true} [%(PATTERN_CLAUSES_TRANSITIVITY_EQ)s]
PFTRM_ADD_SYM_CLAUSES {false,true} [%(PFTRM_ADD_SYM_CLAUSES)s]
PFTRM_PRESORT_CLAUSES {false,true} [%(PFTRM_PRESORT_CLAUSES)s]
PFTRM_REMOVE_INDEPENDENT {false,true} [%(PFTRM_REMOVE_INDEPENDENT)s]
POST_CONFRONT1_DELAY {0,1,4,1000} [%(POST_CONFRONT1_DELAY)s]
POST_CONFRONT2_DELAY {0,1,200,1000} [%(POST_CONFRONT2_DELAY)s]
POST_CONFRONT3_DELAY {0,1,200,500,1000} [%(POST_CONFRONT3_DELAY)s]
POST_CONFRONT4_DELAY {0,1,200,1000} [%(POST_CONFRONT4_DELAY)s]
POST_DEC_DELAY {0,3,1000} [%(POST_DEC_DELAY)s]
POST_EQO_L_DELAY {0,1,5,1000} [%(POST_EQO_L_DELAY)s]
POST_EQO_NL_DELAY {0,1,5,1000} [%(POST_EQO_NL_DELAY)s]
POST_EQO_NR_DELAY {0,1,5,1000} [%(POST_EQO_NR_DELAY)s]
POST_EQO_R_DELAY {0,1,5,1000} [%(POST_EQO_R_DELAY)s]
POST_FEQ_DELAY {0,1,1000} [%(POST_FEQ_DELAY)s]
POST_MATING_DELAY {0,2,200,1000} [%(POST_MATING_DELAY)s]
POST_NEQO_L_DELAY {0,1,5,1000} [%(POST_NEQO_L_DELAY)s]
POST_NEQO_NL_DELAY {0,1,5,1000} [%(POST_NEQO_NL_DELAY)s]
POST_NEQO_NR_DELAY {0,1,5,1000} [%(POST_NEQO_NR_DELAY)s]
POST_NEQO_R_DELAY {0,1,5,1000} [%(POST_NEQO_R_DELAY)s]
POST_NFEQ_DELAY {0,1,1000} [%(POST_NFEQ_DELAY)s]
POST_NOR_L_DELAY {0,1,5,9,20} [%(POST_NOR_L_DELAY)s]
POST_NOR_R_DELAY {0,1,5} [%(POST_NOR_R_DELAY)s]
POST_OR_L_DELAY {0,1,2,3,5,6,20,1000} [%(POST_OR_L_DELAY)s]
POST_OR_R_DELAY {0,1,2,5,10,20,1000} [%(POST_OR_R_DELAY)s]
PREPROCESS_BEFORE_SPLIT {false,true} [%(PREPROCESS_BEFORE_SPLIT)s]
PRE_MATING_DELAY_NEG {0,2,3,5} [%(PRE_MATING_DELAY_NEG)s]
PRE_MATING_DELAY_POS {0,1,2,3,4} [%(PRE_MATING_DELAY_POS)s]
PRIORITY_QUEUE_IMPL {0,1,3,4,5,6,7,8,9} [%(PRIORITY_QUEUE_IMPL)s]
PROJECT_DELAY {0,1,2,3,7,10,1000} [%(PROJECT_DELAY)s]
RELEVANCE_DELAY {0,1,2,4,5,100} [%(RELEVANCE_DELAY)s]
SPLIT_GLOBAL_DISJUNCTIONS {false,true} [%(SPLIT_GLOBAL_DISJUNCTIONS)s]
SPLIT_GLOBAL_DISJUNCTIONS_EQO {false,true} [%(SPLIT_GLOBAL_DISJUNCTIONS_EQO)s]
SPLIT_GLOBAL_DISJUNCTIONS_IMP {false,true} [%(SPLIT_GLOBAL_DISJUNCTIONS_IMP)s]
TREAT_CONJECTURE_AS_SPECIAL {false,true} [%(TREAT_CONJECTURE_AS_SPECIAL)s]
"""

CONDITIONS = ""

FORBIDDENS = ""

DEFAULTS = {
   "ALL_DEFS_AS_EQNS": "false",
   "APPLY_PATTERN_CLAUSES_EARLY": "false",
   "AP_WEIGHT": "1",
   "ARTP_WEIGHT": "1",
   "AXIOM_DELAY": "0",
   "BASETP_WEIGHT": "1",
   "BASETYPESFINITE": "false",
   "BASETYPESMAXSIZE": "3",
   "BASETYPESTOPROP": "false",
   "CHOICE": "true",
   "CHOICE_EMPTY_DELAY": "0",
   "CHOICE_IN_DELAY": "0",
   "CHOICE_TP_WEIGHT_FAC": "1",
   "CHOICE_WEIGHT": "1",
   "CONFR_DIFF_DELAY": "100",
   "CONFR_SAME1_DELAY": "5",
   "CONFR_SAME2_DELAY": "0",
   "DB_TP_WEIGHT_FAC": "1",
   "DB_WEIGHT": "1",
   "DEFAULTELTINST_DELAY": "30",
   "DEFAULTELT_DELAY": "30",
   "DELAY_FALSE_IN_MODELS": "0",
   "DELAY_FO": "0",
   "DELAY_FO_CLAUSE": "0",
   "DELAY_FO_LIT": "0",
   "DELAY_SEMANTIC_EQUIV_INSTANTIATION": "0",
   "DELAY_TRUE_IN_MODELS": "0",
   "DELAY_UNINFORMATIVE_IN_MODELS": "0",
   "DUALQUEUE_MOD": "2",
   "DYNAMIC_PATTERN_CLAUSES": "true",
   "EAGERLY_PROCESS_INSTANTIATIONS": "true",
   "ENABLE_PATTERN_CLAUSES": "false",
   "ENUM_ARROW": "10",
   "ENUM_CHOICE": "0",
   "ENUM_EQ": "5",
   "ENUM_FALSE": "20",
   "ENUM_FORALL": "50",
   "ENUM_IMP": "20",
   "ENUM_ITER_DEEP": "false",
   "ENUM_ITER_DEEP_DELAY": "100",
   "ENUM_ITER_DEEP_INCR": "0",
   "ENUM_ITER_DEEP_INIT": "1",
   "ENUM_MASK": "0",
   "ENUM_NEG": "5",
   "ENUM_O": "5",
   "ENUM_SORT": "2",
   "ENUM_START": "20",
   "EQ_TP_WEIGHT_FAC": "1",
   "EQ_WEIGHT": "1",
   "EXISTSTOCHOICE": "false",
   "EXISTS_DELAY": "1",
   "E_AUTOSCHEDULE": "false",
   "E_EQO_EQUIV": "false",
   "E_PERIOD": "100",
   "E_TIMEOUT": "1",
   "FALSE_WEIGHT": "1",
   "FILTER_INCR": "5",
   "FILTER_NEGATM": "false",
   "FILTER_NEGATM_USABLE": "false",
   "FILTER_NEGEQ": "false",
   "FILTER_NEGEQ_USABLE": "false",
   "FILTER_POSATM": "false",
   "FILTER_POSATM_USABLE": "false",
   "FILTER_POSEQ": "false",
   "FILTER_POSEQ_USABLE": "false",
   "FILTER_START": "5",
   "FILTER_UNIV": "false",
   "FILTER_UNIV_USABLE": "false",
   "FORALL_DELAY": "1",
   "FORALL_TP_WEIGHT_FAC": "1",
   "FORALL_WEIGHT": "1",
   "HOUNIF1": "false",
   "HOUNIF1BOUND": "4",
   "HOUNIF1MATE": "false",
   "HOUNIF1MATEBELOWEQUIV": "true",
   "HOUNIF1MATENONLITS": "false",
   "HOUNIF1MAXMATES": "1",
   "HOUNIF1NEGFLEX": "false",
   "IMITATE_DEFNS": "true",
   "IMITATE_DEFN_DELAY": "0",
   "IMITATE_DELAY": "10",
   "IMP_WEIGHT": "1",
   "INITIAL_SUBTERMS_AS_INSTANTIATIONS": "false",
   "INITIAL_SUBTERMS_AS_INSTANTIATIONS_O": "true",
   "INSTANTIATE_WITH_FUNC_DISEQN_SIDES": "true",
   "INSTANTIATION_DELAY": "1",
   "INSTANTIATION_ORDER_CYCLE": "1",
   "INSTANTIATION_ORDER_MASK": "0",
   "LAM_TP_WEIGHT_FAC": "1",
   "LAM_WEIGHT": "1",
   "LEIBEQ_TO_PRIMEQ": "false",
   "MAX_INTERPS_PER_AXIOM": "3",
   "MINISAT_SEARCH_DELAY": "10000",
   "MINISAT_SEARCH_PERIOD": "1",
   "MINISAT_SEARCH_PERIOD_FACTOR": "2",
   "MODEL_SEARCH_TIMEOUT": "1",
   "NAME_TP_WEIGHT_FAC": "1",
   "NAME_WEIGHT": "1",
   "NEW_HEAD_ENUM_DELAY": "10",
   "NONFORALL_PATTERN_CLAUSES_USABLE": "false",
   "NOT_IN_PROP_MODEL_DELAY": "0",
   "ONTOLOGY_DEFS_TRANSLUCENT": "false",
   "OTP_WEIGHT": "1",
   "PATTERN_CLAUSES_DELAY": "1",
   "PATTERN_CLAUSES_EARLY": "false",
   "PATTERN_CLAUSES_EQNLITS": "false",
   "PATTERN_CLAUSES_EQN_DELAY": "1",
   "PATTERN_CLAUSES_FORALL_AS_LIT": "true",
   "PATTERN_CLAUSES_ONLYALLSTRICT": "false",
   "PATTERN_CLAUSES_TRANSITIVITY_EQ": "false",
   "PFTRM_ADD_SYM_CLAUSES": "true",
   "PFTRM_PRESORT_CLAUSES": "true",
   "PFTRM_REMOVE_INDEPENDENT": "true",
   "POST_CONFRONT1_DELAY": "0",
   "POST_CONFRONT2_DELAY": "0",
   "POST_CONFRONT3_DELAY": "0",
   "POST_CONFRONT4_DELAY": "0",
   "POST_DEC_DELAY": "0",
   "POST_EQO_L_DELAY": "0",
   "POST_EQO_NL_DELAY": "0",
   "POST_EQO_NR_DELAY": "0",
   "POST_EQO_R_DELAY": "0",
   "POST_FEQ_DELAY": "0",
   "POST_MATING_DELAY": "0",
   "POST_NEQO_L_DELAY": "0",
   "POST_NEQO_NL_DELAY": "0",
   "POST_NEQO_NR_DELAY": "0",
   "POST_NEQO_R_DELAY": "0",
   "POST_NFEQ_DELAY": "0",
   "POST_NOR_L_DELAY": "0",
   "POST_NOR_R_DELAY": "0",
   "POST_OR_L_DELAY": "0",
   "POST_OR_R_DELAY": "0",
   "PREPROCESS_BEFORE_SPLIT": "false",
   "PRE_CHOICE_MATING_DELAY_NEG": "0",
   "PRE_CHOICE_MATING_DELAY_POS": "0",
   "PRE_MATING_DELAY_NEG": "0",
   "PRE_MATING_DELAY_POS": "0",
   "PRIORITY_QUEUE_IMPL": "0",
   "PROJECT_DELAY": "10",
   "RELEVANCE_DELAY": "0",
   "SPLIT_GLOBAL_DISJUNCTIONS": "false",
   "SPLIT_GLOBAL_DISJUNCTIONS_EQO": "true",
   "SPLIT_GLOBAL_DISJUNCTIONS_IMP": "true",
   "SPLIT_GLOBAL_DISJUNCTIONS_LIMIT": "8",
   "SYM_EQ": "true",
   "TRANSLUCENT_EXPAND_DELAY": "5",
   "TREAT_CONJECTURE_AS_SPECIAL": "false",
}
 