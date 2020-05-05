from grackle.runner.eprover import cef2block
from .. import cefs
from . import base, order, tuner

def glob(config, init=None):
   cefs = cefs.load(config["cefs_db"])
   cefs = map(cef2block, cefs.domain(config["cefs_count"], cefs))
   if init:
      for x in init:
         if x.startswith("cef") and init[x] not in cefs:
            cefs.append(init[x])

   return base.PARAMS     + order.PARAMS     + base.params(config, cefs) + \
          base.CONDITIONS + order.CONDITIONS + base.conditions(config) + \
          base.FORBIDDENS + base.forbiddens(config, cefs)

class GlobalTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.GlobalTuner")

   def split(self, params):
      main = {x:params[x] for x in params if not x.startswith("sine")}
      extra = {x:params[x] for x in params if x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return glob(config, init=init)


