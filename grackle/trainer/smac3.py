from os import path, system
import sys

from grackle.trainer.trainer import Trainer
from ConfigSpace.read_and_write import pcs
from smac.scenario.scenario import Scenario
from smac.facade.experimental.psmac_facade import PSMAC
from smac.utils.io.output_directory import create_output_directory

SCENARIO = {
   "deterministic": True,
   "execdir": ".",
   "run_obj": "quality", #"runtime"
   "algo_runs_timelimit": 60,
   "train_inst_fn": "ufnia-try",
}

class Smac3Trainer(Trainer):
   
   def __init__(self, runner, config={}):
      Trainer.__init__(self, runner, config)

   def domains(self, params):
      pass
   
   def improve(self, state, conf, insts, tae=None):
      cwd = path.join("training", "iter-%03d-%s"%(state.it,conf))
      cwd = path.join(cwd, self.runner.config["nick"]) if "nick" in self.runner.config else cwd
      system(f'mkdir -p "{cwd}"')
      f_insts = path.join(cwd, "insts")
      open(f_insts, "w").write("\n".join(insts))

      params = self.runner.recall(conf)
      scn = dict(SCENARIO)
      scn["execdir"] = cwd
      scn["train_inst_fn"] = f_insts
      scn["cs"] = pcs.read(self.domains(params).split("\n"))
      scn["algo_runs_timelimit"] = self.config["timeout"]
      scenario = Scenario(scn)

      tae = tae if tae else self.wrapper
      smac = PSMAC(scenario=scenario, tae=tae, n_optimizers=state.cores, validate=False)
      # begin of output dir hack 
      smac.scenario.output_dir = cwd
      smac.output_dir = create_output_directory(smac.scenario, run_id=smac.run_id)
      smac.scenario.shared_model = smac.shared_model
      # end of hack
      inc = smac.optimize()
      params = self.runner.clean(inc[0])
      return self.runner.name(params) 

   def wrapper(self, conf, seed, instance):
      """
      This is a bit unfortunate, as it loads all the above imported modules
      over and over again.  It takes time and it is completely unnecassary.
      Try to provide `tae` argument for `self.improve` which will avoid this to
      speed up things. See `cvc4.smac3.py` for an example.
      """
      result = self.runner.run(conf, instance)
      return result[0]

