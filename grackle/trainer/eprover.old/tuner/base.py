from grackle.runner.eprover import cef2block, convert
from .. import cefs as cefs_mod
from . import tuner, given

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

FREE = ["sel", "simparamod", "srd", "forwardcntxtsr", "splaggr", "splcl"]

def free(key):
   return (key in FREE) or given.free(key)

def base(config, init=None):
   cefs = given.evals(config, init=init)
   return PARAMS     + given.params(config, cefs) + \
          CONDITIONS + given.conditions(config) + \
          FORBIDDENS + given.forbiddens(config, cefs)



class BaseTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-base"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.BaseTuner")

   def split(self, params):
      params = convert(params)
      main = {x:params[x] for x in params if free(x)}
      extra = {x:params[x] for x in params if not free(x)}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return base(config, init=init)


