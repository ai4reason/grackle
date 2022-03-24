from ..smac3 import Smac3Trainer, Smac3TrainerBB, Smac3TrainerHPO, Smac3TrainerROAR
from . import domain
from .tarunner import TARunner

class VampireSmac3Trainer(Smac3Trainer):

   def __init__(self, runner, config={}):
      Smac3Trainer.__init__(self, runner, config)

   def domains(self, params):
      defaults = dict(domain.DEFAULTS)
      defaults.update(params)
      return (domain.PARAMS % defaults) + domain.CONDITIONS + domain.FORBIDDENS 

   def improve(self, state, conf, insts):
      config = dict(self.runner.config)
      tae = TARunner(config).run
      return Smac3Trainer.improve(self, state, conf, insts, tae=tae)


class VampireSmac3TrainerAC(VampireSmac3Trainer):
   pass
   
class VampireSmac3TrainerBB(VampireSmac3Trainer):
   
   def __init__(self, runner, config={}):
      Smac3TrainerBB.__init__(self, runner, config)

class VampireSmac3TrainerHPO(VampireSmac3Trainer):
   
   def __init__(self, runner, config={}):
      Smac3TrainerHPO.__init__(self, runner, config)

class VampireSmac3TrainerROAR(VampireSmac3Trainer):

   def __init__(self, runner, config={}):
      Smac3TrainerROAR.__init__(self, runner, config)


