from ..smac3 import Smac3Trainer, Smac3TrainerBB, Smac3TrainerHPO, Smac3TrainerROAR
from . import domain
from . import domain_full
from . import domain_casc
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



class VampireSmac3FullTrainerAC(VampireSmac3Trainer):

   def domains(self, params):
      defaults = dict(domain_full.DEFAULTS)
      defaults.update(params)
      return (domain_full.PARAMS % defaults) + domain_full.CONDITIONS + domain_full.FORBIDDENS 

class VampireSmac3FullTrainerROAR(VampireSmac3FullTrainerAC):

   def __init__(self, runner, config={}):
      Smac3TrainerROAR.__init__(self, runner, config)



class VampireSmac3CascTrainerAC(VampireSmac3Trainer):

   def domains(self, params):
      defaults = dict(domain_casc.DEFAULTS)
      defaults.update(params)
      return (domain_casc.PARAMS % defaults) + domain_casc.CONDITIONS + domain_casc.FORBIDDENS 

class VampireSmac3CascTrainerROAR(VampireSmac3CascTrainerAC):

   def __init__(self, runner, config={}):
      Smac3TrainerROAR.__init__(self, runner, config)

