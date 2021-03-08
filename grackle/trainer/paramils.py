import json
from os import path

from grackle.trainer.trainer import Trainer
from grackle.paramils import reparamils

SCENARIO = """
algo = %s
execdir = .
deterministic = 1
run_obj = runlength
overall_obj = mean
cutoff_time = %s
cutoff_length = max
tunerTimeout = %s
paramfile = params.txt
outdir = paramils-out
instance_file = instances.txt
test_instance_file = empty.tst
"""

class ParamilsTrainer(Trainer):
   
   def __init__(self, runner, config={}):
      Trainer.__init__(self, runner, config)

   def domains(self, params):
      pass
   
   def improve(self, state, conf, insts):
      cwd = path.join("training", "iter-%03d-%s"%(state.it,conf))
      cwd = path.join(cwd, self.runner.config["nick"]) if "nick" in self.runner.config else cwd
      params = self.runner.recall(conf)
      algo = "grackle-wrapper.py %s" % repr(json.dumps(self.runner.config))
      scenario = SCENARIO % (algo, state.trainer.runner.config["cutoff"], state.trainer.config["timeout"])
      params = reparamils.launch(
         scenario, 
         domains=self.domains(params), 
         init=params, 
         insts=insts, 
         cwd=cwd, 
         timeout=self.config["timeout"], 
         cores=state.cores)
      params = self.runner.clean(params)
      return self.runner.name(params) 

