from .trainer import Trainer
from .domain.multidomain import MultiDomain
from .. import log

class StageTrainer(Trainer):

   def __init__(self, runner, trainer, config={}):
      assert(isinstance(runner.domain, MultiDomain))
      Trainer.__init__(self, runner, config)
      self._trainer = trainer
      self._confname = "unknown"

   def improve(self, state, conf, insts):
      orig = self.runner.domain
      params = self.runner.recall(conf)
      for (i,domain) in enumerate(orig.domains):
         nick = f"{i+1:02d}-{domain.name}"
         self.runner.domain = domain
         self.runner.config["nick"] = nick
         log.tuner(nick, i+1, len(orig.domains))
         (params, fixed) = domain.split(params)
         self.runner.config["fixed"] = fixed
         # TODO: adjust timeout (/ n)
         params = self._trainer.improve(state, conf, insts, params=params)
         params = domain.join(params, fixed)
      self.runner.domain = orig
      del self.runner.config["fixed"]
      params = self.runner.clean(params)
      return self.runner.name(params)

