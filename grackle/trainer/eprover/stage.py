import json
from os import path, system
from ..trainer import Trainer
from .tuner.tuner import SCENARIO, launch
from grackle import log

class EproverTrainer(Trainer):
   def __init__(self, runner, cls):
      Trainer.__init__(self, runner)
      self.cls = cls

   def tune(self, tuner_cls, domains, init, insts, cwd, cores, extra=None):
      cutoff = self.config["cutoff"]
      timeout = self.config["timeout"]
      algo = "grackle-wrapper.py %s" % tuner_cls
      if extra:
         algo += " EXTRA %s" % repr(json.dumps(extra))
      scenario = SCENARIO % (algo, cutoff, timeout)
      return launch(scenario, domains, init, insts, cwd, timeout, cores)

   def finish(self, params):
      params = self.runner.clean(params)
      return self.runner.name(params) 

class StageTrainer(EproverTrainer):
   def __init__(self, runner, cls, tuners):
      EproverTrainer.__init__(self, runner, cls)
      self.tuners = tuners

   def improve(self, state, conf, insts):
      params = self.runner.recall(conf)
      i = 1
      for tuner in self.tuners:
         log.tuner(tuner.nick, i, len(self.tuners))
         params = self.stage(state, conf, tuner, params, insts)
         i += 1
      return self.finish(params)

   def stage(self, state, conf, tuner, params, insts):
      cwd = path.join("training", "iter-%03d-%s"%(state.it,conf), tuner.nick)
      domains = tuner.domains(self.config, params)
      (main, extra) = tuner.split(params)
      main = self.tune(tuner.cls, domains, main, insts, cwd, state.cores, extra=extra)
      return tuner.join(main, extra)


