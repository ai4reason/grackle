import json
from itertools import cycle

from grackle.runner.eprover import cef2block

DOMAIN = {
	"freq": "1,2,3,4,5,8,10,13,21,34", 
   #"cefs": CefFile("cefs.txt"),
   #"prio": DomainFile("prios.txt"),
   "prio": "SimulateSOS,PreferGroundGoals,PreferUnitGroundGoals,DeferSOS,ByNegLitDist,ByCreationDate,PreferProcessed,PreferGoals,ConstPrio,PreferNonGoals", # never remove ConstPrio for enigma
   "level": "1,0,2", 
   "weight": "1,200,20,10,300,18,400,50,0,3,2,-1,4,7,-2,5,100,9999", 
   "cost":   "1,200,20,10,300,18,400,50,0,3,2,-1,4,7,-2,5,100,9999", 
   #"cost": "0,1,5,10,100,9999",
   "mult": "0.8,1,4,1.5,0.1,0.3,0.2,0.5,0.7,1,3,2,5,4,3,2,2.5,9999.9", # never remove 0.2 for enigma
   "factor": "1,1.5,2",
   "var": "0,1",
   "rel": "0,1,2,3",
   "ext": "0,1,2",
   "docs": "0,1",
   "fact": "0,1,10,9999.9",
   "real": "0,0.1,0.5,1,5,10,100,9999.9",
}

# prord {arity,invfreq,invfreqconstmin} [invfreqconstmin]
# tord {Auto,LPO4,KBO6} [LPO4]

BASE_PARAMS = """
   sel {SelectMaxLComplexAvoidPosPred,SelectNewComplexAHP,SelectComplexG,SelectCQPrecWNTNp} [SelectMaxLComplexAvoidPosPred]
   simparamod {none,normal,oriented} [normal]
   srd {0,1} [0]
   forwardcntxtsr {0,1} [1]
   splaggr {0,1} [1]
   splcl {0,4,7} [4]
"""

ORDER_PARAMS = """
   tord {Auto,LPO4,KBO6} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
"""

SINE_PARAMS = """
   sineG {CountFormulas,CountTerms} [CountFormulas]
   sineh {none,hypos} [hypos]
   sinegf {1.1,1.2,1.4,1.5,2.0,5.0,6.0} [1.2]
   sineD {none,1,3,10,20,40,160} [none]
   sineR {none,01,02,03,04} [none]
   sineL {10,20,40,60,80,100,500,20000} [100]
   sineF {1.0,0.8,0.6} [1.0]
"""

#   sineL {10,20,40,60,80,100,500,20000} [100]
#   sineR {UU,01,02,03,04} [UU]
#   sinegf {1.1,1.2,1.4,1.5,2.0,5.0,6.0} [1.2]
#   sineh  {hypos,none} [hypos]
#   sine {0,1} [0]
#   sineL  | sine in {1}
#   sineR  | sine in {1}
#   sinegf | sine in {1}
#   sineh  | sine in {1}
#"""

BASE_CONDITIONS = ""

ORDER_CONDITIONS = """
   tord_prec   | tord in {LPO4,KBO6}
   tord_weight | tord in {KBO6}
   tord_const  | tord in {KBO6}
"""

BASE_FORBIDDENS = ""

WEIGHTS = {
   "ClauseWeightAge":                  "prio:prio f:weight v:weight pos:mult w:mult",
   "Clauseweight":                     "prio:prio f:weight v:weight pos:mult",
   "ConjectureGeneralSymbolWeight":    "prio:prio f:weight c:weight p:weight conj_f:weight conj_c:weight conj_p:weight v:weight maxt:mult maxl:mult pos:mult",
   "ConjectureRelativeSymbolWeight":   "prio:prio conj:mult f:weight c:weight p:weight v:weight maxt:mult maxl:mult pos:mult",
   "ConjectureSymbolWeight":           "prio:prio f:weight p:weight conj_f:weight conj_p:weight v:weight maxt:mult maxl:mult pos:mult",
   "Defaultweight":                    "prio:prio",
   "FIFOWeight":                       "prio:prio",
   "OrientLMaxWeight":                 "prio:prio f:weight v:weight unlit:mult maxl:mult pos:mult",
   "PNRefinedweight":                  "prio:prio f:weight v:weight nf:weight nv:weight maxt:mult maxl:mult pos:mult",
   "Refinedweight":                    "prio:prio f:weight v:weight maxt:mult maxl:mult pos:mult",
   "RelevanceLevelWeight":             "prio:prio const:level lin:level square:level default:level f:weight c:weight p:weight v:weight maxt:mult maxl:mult pos:mult",
   "RelevanceLevelWeight2":            "prio:prio const:level lin:level square:level default:level f:weight c:weight p:weight v:weight maxt:mult maxl:mult pos:mult",
   "StaggeredWeight":                  "prio:prio stagger:factor",
   "SymbolTypeweight":                 "prio:prio f:weight v:weight c:weight p:weight maxt:mult maxl:mult pos:mult",
   "Uniqweight":                       "prio:prio",
   "ConjectureRelativeTermWeight":     "prio:prio var:var rel:rel conj:mult f:weight c:weight p:weight v:weight ext:ext maxt:mult maxl:mult pos:mult",
   "ConjectureTermTfIdfWeight":        "prio:prio var:var rel:rel docs:docs tffact:fact ext:ext maxt:mult maxl:mult pos:mult",
   "ConjectureTermPrefixWeight":       "prio:prio var:var rel:rel match:real mis:real ext:ext maxt:mult maxl:mult pos:mult",
   "ConjectureLevDistanceWeight":      "prio:prio var:var rel:rel ins:cost del:cost ch:cost ext:ext maxt:mult maxl:mult pos:mult",
   "ConjectureTreeDistanceWeight":     "prio:prio var:var rel:rel ins:cost del:cost ch:cost ext:ext maxt:mult maxl:mult pos:mult",
   "ConjectureStrucDistanceWeight":    "prio:prio var:var rel:rel varmis:real symmis:real inst:real gen:real ext:ext maxt:mult maxl:mult pos:mult",
}

def cefs_load(f_cefs):
   return json.load(file(f_cefs))

def cefs_save(f_cefs, cefs):
   json.dump(cefs, file(f_cefs,"w"), indent=3, sort_keys=True)

def cefs_weight(cef):
   return cef.split("(")[0]

def cefs_usage(weight, cefs):
   weight_cefs = [cef for cef in cefs if cef.startswith(weight+"(")]
   usage = sum([cefs[cef] for cef in weight_cefs])
   bests = sorted([(cefs[cef],cef) for cef in weight_cefs],reverse=True)
   return (usage, bests)

def cefs_domain(count, cefs):
   ret = []
   weights = set(map(cefs_weight,cefs))
   w_bests = sorted([cefs_usage(w,cefs) for w in weights],reverse=True)
   count = min(len(cefs), count)

   for (usage,bests) in cycle(w_bests):
      if len(ret) >= count:
         return ret[:count]
      if bests:
         cef = bests.pop(0)[1]
         ret.append(cef)



def base_params(config, cefs):
   pars = ""
   slots = ",".join(map(str, range(config["min_slots"], config["max_slots"]+1)))
   pars += "   slots {%s} [%s]\n" % (slots, config["min_slots"])
   for i in xrange(config["max_slots"]):
      pars += "   freq%d {%s} [%s]\n" % (i, DOMAIN["freq"], 1)
      pars += "   cef%d {%s} [%s]\n" % (i, ",".join(cefs), cefs[i%len(cefs)])
   return pars
   
def base_conditions(config):
   conds = ""
   for i in range(config["min_slots"], config["max_slots"]):
       dom = ",".join(map(str,range(i+1, config["max_slots"]+1)))
       conds += "   %s | %s in {%s}\n" % ("freq%d"%i, "slots", dom)
       conds += "   %s | %s in {%s}\n" % ("cef%d"%i, "slots", dom)
   return conds

def base_forbiddens(config, cefs):
   bans = ""
   for n in range(config["min_slots"], config["max_slots"]+1):
      bans += "#%d\n" % n
      ns = range(0,n)
      pairs = [(i,j) for i in ns for j in ns if i<j]
      for cef in cefs:
         for (i,j) in pairs:
            bans += "   {%s=%s,%s=%s,%s=%s}\n" % ("slots",n,"cef%d"%i,cef,"cef%d"%j,cef)
   return bans 

def base(config, init=None):
   cefs = cefs_load(config["cefs_db"])
   cefs = map(cef2block, cefs_domain(config["cefs_count"], cefs))
   if init:
      for x in init:
         if x.startswith("cef") and init[x] not in cefs:
            cefs.append(init[x])

   return BASE_PARAMS     + base_params(config, cefs) + \
          BASE_CONDITIONS + base_conditions(config) + \
          BASE_FORBIDDENS + base_forbiddens(config, cefs)



def glob(config, init=None):
   cefs = cefs_load(config["cefs_db"])
   cefs = map(cef2block, cefs_domain(config["cefs_count"], cefs))
   if init:
      for x in init:
         if x.startswith("cef") and init[x] not in cefs:
            cefs.append(init[x])

   return BASE_PARAMS     + ORDER_PARAMS     + base_params(config, cefs) + \
          BASE_CONDITIONS + ORDER_CONDITIONS + base_conditions(config) + \
          BASE_FORBIDDENS + base_forbiddens(config, cefs)



def fine_args(cef, prefix):
   wargs = cef.replace("_M_","-").replace("_D_",".").split("__")
   weight = wargs.pop(0)
   argtyps = [x.split(":") for x in WEIGHTS[weight].split(" ") if x]
   args = []
   for (arg,typ) in argtyps:
      dom = DOMAIN[typ]
      default = wargs.pop(0)
      args += [(prefix+arg,dom,default)]
   return args

def fine_main(params):
   main = {}
   slots = int(params["slots"])
   for i in range(slots):
      args = fine_args(params["cef%d"%i], "cef%d_"%i)
      for (name,dom,default) in args:
         main[name] = default
   return main

def fine_cef(weight, main, key):
   args = [x.split(":")[0] for x in WEIGHTS[weight].split(" ")]
   args = [main["%s_%s"%(key,x)] for x in args]
   return "%s(%s)" % (weight, ",".join(args))

def fine_cefs(main, extra):
   cefs = {}
   slots = int(extra["slots"])
   for i in range(slots):
      key = "cef%d"%i
      cef = fine_cef(extra[key], main, key) 
      cefs[key] = cef2block(cef)
   return cefs

def fine(params):
   slots = int(params["slots"])
   args = ""
   for i in range(slots):
      args += "# %s\n" % params["cef%d"%i] # just a comment
      for arg in fine_args(params["cef%d"%i], "cef%d_"%i):
         args += "   %s {%s} [%s]\n" % arg
   return args



def order():
   return ORDER_PARAMS + ORDER_CONDITIONS 



def sine():
   return SINE_PARAMS
