from os import path, system
import sys

from grackle.trainer.trainer import Trainer
from ConfigSpace.read_and_write import pcs
from smac.scenario.scenario import Scenario
from smac.facade.smac_ac_facade import SMAC4AC 
from smac.intensification.simple_intensifier import SimpleIntensifier
from smac.intensification.parallel_scheduling import ParallelScheduler
from smac.intensification.successive_halving import SuccessiveHalving
from .smac3wrapper import Wrapper

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
      self.SMAC = SMAC4AC

   def domains(self, params):
      raise NotImplementedError()
   
   def improve(self, state, conf, insts, tae=None):
      cwd = path.join("training", "iter-%03d-%s"%(state.it,conf))
      cwd = path.join(cwd, self.runner.config["nick"]) if "nick" in self.runner.config else cwd
      system(f'mkdir -p "{cwd}"')
      f_insts = path.join(cwd, "insts")
      open(f_insts, "w").write("\n".join(insts))

      params = self.runner.recall(conf)
      if self.config["instance_budget"]:
         timeout = len(insts) * self.config["instance_budget"]
         timeout = min(self.config["timeout"], timeout)
      else:
         timeout = self.config["timeout"]
      scenario = Scenario({
         "deterministic": True,
         "execdir": cwd,
         "run_obj": "quality", #"runtime"
         #"algo_runs_timelimit": 60,
         "wallclock-limit": timeout,
         "train_inst_fn": f_insts,
         "limit_resources": False,
         "cs": pcs.read(self.domains(params).split("\n")),
         "output_dir": cwd
      })

      tae = tae if tae else Wrapper(self.runner).run
      iargs = {
         "instances": insts,
         "min_chall": 1,
         "initial_budget": 1, 
         "max_budget": len(insts), 
         "eta": 3,
         "deterministic": True,
      }
      smac = self.SMAC(
         scenario=scenario, 
         tae_runner=tae, 
         n_jobs=state.cores, 
         intensifier=SuccessiveHalving, 
         intensifier_kwargs=iargs
      )
      inc = smac.optimize()
      params = self.runner.clean(inc)
      return self.runner.name(params) 

class Smac3TrainerAC(Smac3Trainer):
   "SMAC4AC is the default"
   pass
   
class Smac3TrainerBB(Smac3Trainer):
   
   def __init__(self, runner, config={}):
      Smac3Trainer.__init__(self, runner, config)
      from smac.facade.smac_bb_facade import SMAC4BB 
      self.SMAC = SMAC4BB

class Smac3TrainerHPO(Smac3Trainer):
   
   def __init__(self, runner, config={}):
      Smac3Trainer.__init__(self, runner, config)
      from smac.facade.smac_hpo_facade import SMAC4HPO
      self.SMAC = SMAC4HPO

class Smac3TrainerROAR(Smac3Trainer):

   def __init__(self, runner, config={}):
      Smac3Trainer.__init__(self, runner, config)
      from smac.facade.roar_facade import ROAR
      self.SMAC = ROAR

