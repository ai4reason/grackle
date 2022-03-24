from ..paramils import ParamilsTrainer
from .tuner.base import BaseTuner

class EproverParamilsTunerTrainer(ParamilsTrainer):
   
   def __init__(self, runner, config, tuner):
      ParamilsTrainer.__init__(self, runner, config)
      self._runner = runner
      self.runner = tuner

   def domains(self, params):
      return self.runner.domains(self.config, params)
   
   def improve(self, state, conf, insts):
      params = self._runner.recall(conf)
      (main, extra) = self.runner.split(params)
      self.runner.config["extra"] = extra
      self.conf = conf
      main = ParamilsTrainer.improve(self, state, main, insts)
      params = self.runner.join(main, extra)
      return self._runner.name(params)
   
   def recall(self, conf):
      return conf

   def name(self, params):
      return params

   def confname(self, conf):
      return self.conf

class EproverParamilsBaseTrainer(EproverParamilsTunerTrainer):

   def __init__(self, runner, config={}):
      EproverParamilsTunerTrainer.__init__(self, runner, config,
         BaseTuner(dict(runner.config), "00-base")
      )

