from grackle.runner.eprover import cef2block
from . import tuner

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

def args(cef0, prefix):
   wargs = cef0.replace("_M_","-").replace("_D_",".").split("__")
   weight = wargs.pop(0)
   argtyps = [x.split(":") for x in WEIGHTS[weight].split(" ") if x]
   args = []
   for (arg,typ) in argtyps:
      dom = DOMAIN[typ]
      default = wargs.pop(0)
      args += [(prefix+arg,dom,default)]
   return args

def main(params):
   main = {}
   slots = int(params["slots"])
   for i in range(slots):
      args0 = args(params["cef%d"%i], "cef%d_"%i)
      for (name,dom,default) in args0:
         main[name] = default
   return main

def cef(weight, main, key):
   args0 = [x.split(":")[0] for x in WEIGHTS[weight].split(" ")]
   args0 = [main["%s_%s"%(key,x)] for x in args0]
   return "%s(%s)" % (weight, ",".join(args0))

def cefs(main, extra):
   cefs0 = {}
   slots = int(extra["slots"])
   for i in range(slots):
      key = "cef%d"%i
      cef0 = cef(extra[key], main, key) 
      cefs0[key] = cef2block(cef0)
   return cefs0

def fine(params):
   slots = int(params["slots"])
   args0 = ""
   for i in range(slots):
      args0 += "# %s\n" % params["cef%d"%i] # just a comment
      for arg in args(params["cef%d"%i], "cef%d_"%i):
         args0 += "   %s {%s} [%s]\n" % arg
   return args0



class FineTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="2-fine"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.FineTuner")

   def split(self, params):
      main0 = main(params)
      extra = {x:params[x] for x in params if not x.startswith("cef")}
      weights = {x:params[x].split("__")[0] for  x in params if x.startswith("cef")}
      extra.update(weights)
      return (main0, extra)

   def join(self, main0, extra):
      cefs0 = cefs(main0, extra)
      params = dict(extra)
      params.update(cefs0)
      return params

   def domains(self, config, init=None):
      return fine(init)

