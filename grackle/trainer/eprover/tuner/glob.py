from grackle.runner.eprover import cef2block
from .. import cefs
from . import base, order, tuner

def glob(config, init=None):
   cefs0 = cefs.load(config["cefs_db"])
   cefs0 = list(map(cef2block, cefs.domain(config["cefs_count"], cefs0)))
   if init:
      for x in init:
         if x.startswith("cef") and init[x] not in cefs0:
            cefs0.append(init[x])

   return base.PARAMS     + order.PARAMS     + base.params(config, cefs0) + \
          base.CONDITIONS + order.CONDITIONS + base.conditions(config) + \
          base.FORBIDDENS + base.forbiddens(config, cefs0)

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


