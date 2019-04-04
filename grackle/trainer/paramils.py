import json
from os import path

from grackle.trainer.trainer import Trainer
from grackle.paramils import reparamils

class ParamilsTrainer(Trainer):
   
   def __init__(self, runner, config={}):
      Trainer.__init__(self, runner, config)

   def domains(self, params):
      pass
   
   def improve(self, state, conf, insts):
      cwd = path.join("training", "iter-%03d-%s"%(state.it,conf))
      cwd = path.join(cwd, self.runner.config["nick"])
      params = self.runner.recall(conf)
      algo = "grackle-wrapper.py %s" % repr(json.dumps(self.runner.config))
      return reparamils.launch(
         scenario, 
         domains=self.domains(params), 
         init=params, 
         insts, 
         cwd, 
         timeout=self.config["timeout"], 
         cores=state.cores)

