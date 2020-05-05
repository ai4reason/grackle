from grackle.runner.eprover import cef2block, convert
from .. import cefs as cefs_mod
from . import tuner, fine

PARAMS = """
   sel {SelectMaxLComplexAvoidPosPred,SelectNewComplexAHP,SelectComplexG,SelectCQPrecWNTNp} [SelectMaxLComplexAvoidPosPred]
   simparamod {none,normal,oriented} [normal]
   srd {0,1} [0]
   forwardcntxtsr {0,1} [1]
   splaggr {0,1} [1]
   splcl {0,4,7} [4]
"""

CONDITIONS = ""

FORBIDDENS = ""

def params(config, cefs):
   pars = ""
   slots = ",".join(map(str, range(config["min_slots"], config["max_slots"]+1)))
   pars += "   slots {%s} [%s]\n" % (slots, config["min_slots"])
   for i in range(config["max_slots"]):
      pars += "   freq%d {%s} [%s]\n" % (i, fine.DOMAIN["freq"], 1)
      pars += "   cef%d {%s} [%s]\n" % (i, ",".join(cefs), cefs[i%len(cefs)])
   return pars
   
def conditions(config):
   conds = ""
   for i in range(config["min_slots"], config["max_slots"]):
       dom = ",".join(map(str,range(i+1, config["max_slots"]+1)))
       conds += "   %s | %s in {%s}\n" % ("freq%d"%i, "slots", dom)
       conds += "   %s | %s in {%s}\n" % ("cef%d"%i, "slots", dom)
   return conds

def forbiddens(config, cefs):
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
   cefs = cefs_mod.load(config["cefs_db"])
   cefs = list(map(cef2block, cefs_mod.domain(config["cefs_count"], cefs)))
   if init:
      for x in init:
         if x.startswith("cef") and init[x] not in cefs:
            cefs.append(init[x])

   return PARAMS     + params(config, cefs) + \
          CONDITIONS + conditions(config) + \
          FORBIDDENS + forbiddens(config, cefs)


class BaseTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-base"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.BaseTuner")

   def split(self, params):
      params = convert(params)
      main = {x:params[x] for x in params if not (x.startswith("tord") or x.startswith("sine"))}
      extra = {x:params[x] for x in params if x.startswith("tord") or x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return base(config, init=init)


