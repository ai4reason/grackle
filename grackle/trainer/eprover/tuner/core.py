from grackle.runner.eprover import cef2block, convert
from . import tuner, base, order, sine



def free(key):
   return (key in base.FREE) or order.free(key) or sine.free(key)

def core(config, init=None):
   return base.PARAMS     + order.PARAMS     + sine.PARAMS + \
          base.CONDITIONS + order.CONDITIONS + sine.CONDITIONS + \
          base.FORBIDDENS 



class CoreTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-core"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.CoreTuner")

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
      return core(config, init=init)


