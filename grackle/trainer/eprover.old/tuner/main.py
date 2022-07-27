from grackle.runner.eprover import convert, SINE_DEFAULTS
from . import tuner, sine, order


def main():
   return order.PARAMS + sine.PARAMS + \
          order.CONDITIONS + sine.CONDITIONS


class MainTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-main"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.MainTuner")

   def split(self, params):
      params = convert(params)
      fluents = [x for x in params if x.startswith("sine") or x.startswith("tord")]
      main = dict(SINE_DEFAULTS)
      main.update({x:params[x] for x in params if x in fluents})
      extra = {x:params[x] for x in params if x not in fluents}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return main()


