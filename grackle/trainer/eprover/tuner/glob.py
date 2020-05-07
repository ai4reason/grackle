from grackle.runner.eprover import cef2block
from .. import cefs
from . import tuner, base, order, given

def free(key):
   return base.free(key) or order.free(key) or given.free(key)

def glob(config, init=None):
   cefs0 = given.evals(config, init=init)
   return base.PARAMS     + order.PARAMS     + given.params(config, cefs0) + \
          base.CONDITIONS + order.CONDITIONS + given.conditions(config) + \
          base.FORBIDDENS + given.forbiddens(config, cefs0)

class GlobalTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.GlobalTuner")

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
      return glob(config, init=init)


