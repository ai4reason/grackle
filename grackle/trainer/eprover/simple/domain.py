
FIXED = """\
   sel {SelectMaxLComplexAvoidPosPred,SelectNewComplexAHP,SelectComplexG,SelectCQPrecWNTNp} [SelectMaxLComplexAvoidPosPred]
   tord {LPO4,KBO6} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   sine {0,1} [1]
   sineG {CountFormulas,CountTerms} [CountFormulas]
   sineh {none,hypos} [hypos]
   sinegf {1.1,1.2,1.4,1.5,2.0,5.0,6.0} [1.2]
   sineD {none,1,3,10,20,40,160} [none]
   sineR {none,01,02,03,04} [none]
   sineL {10,20,40,60,80,100,500,20000} [100]
   sineF {1.0,0.8,0.6} [1.0]
"""

# slots, cef{n}, freq{n}

PARAMS = """\
   splaggr {0,1} [1]
   srd {0,1} [0]
   forwardcntxtsr {0,1} [1]
   prefer {0,1} [0]
   presat {0,1} [0]
   condense {0,1} [0]
   defcnf {none,0,3,24} [none]
   splcl {0,4,7} [4]
   fwdemod {0,1,2} [2]
   der {none,std,strong,agg,stragg} [none]
   simparamod {none,normal,oriented} [normal]
"""

CONDITIONS = ""

FORBIDDENS = ""


DEFAULTS = {
   "sel": "SelectMaxLComplexAvoidPosPred",
   "tord": "LPO4",
   "tord_prec": "arity",
   "tord_weight": "arity",
   "simparamod": "none",
   "srd": "0",
   "forwardcntxtsr": "0",
   "splaggr": "0",
   "splcl": "0",
   "tord_const": "0",
   "sine": "0",
   "defcnf": "none",
   "prefer": "0",
   "fwdemod": "2",
   "der": "none",
   "presat": "0",
   "condense": "0",
}

SINE_DEFAULTS = { 
   "sineG": "CountFormulas", 
   "sineh": "hypos", 
   "sinegf": "1.2",
   "sineD": "none", 
   "sineR": "none", 
   "sineL": "100",
   "sineF": "1.0" 
}

