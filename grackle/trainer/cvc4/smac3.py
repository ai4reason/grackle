from ..smac3 import Smac3Trainer 
from .domain import *
from grackle.runner.cvc4 import wrapper as cvc4wrapper

class Cvc4Smac3Trainer(Smac3Trainer):

   def domains(self, params):
      defaults = dict(DEFAULTS)
      defaults.update(params)
      return (PARAMS % defaults) + CONDITIONS + FORBIDDENS 

   def improve(self, state, conf, insts):
      config = dict(self.runner.config)
      tae = lambda conf, seed, instance: cvc4wrapper(conf, instance, config=config)
      return Smac3Trainer.improve(self, state, conf, insts, tae=tae)

