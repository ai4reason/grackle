from os import path, system
import sys
import logging
from joblib import Parallel, delayed
from .. import log

from grackle.trainer.trainer import Trainer
from ConfigSpace.read_and_write import pcs
from smac.scenario.scenario import Scenario
from smac.facade.smac_ac_facade import SMAC4AC 
#from smac.intensification.successive_halving import SuccessiveHalving
from .smac3wrapper import Wrapper

def optimize(SMAC, scenario, tae, n, logs):
   if logs:
      logging.basicConfig(filename=path.join(scenario.output_dir, "log_%d" % n))
      logging.getLogger().setLevel(logging.DEBUG)
   smac = SMAC(scenario=scenario, tae_runner=tae, run_id=n, rng=n)
   inc = smac.optimize()
   try:
      cost = smac.runhistory.get_cost(inc)
   except:
      cost = sys.maxint
   return (inc, cost)

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
      timeout = self.trainlimit(len(insts))
      scenario = Scenario({
         "deterministic": True,
         "execdir": cwd,
         "run_obj": "quality", #"runtime"
         "wallclock-limit": timeout,
         "train_inst_fn": f_insts,
         "limit_resources": False,
         "cs": pcs.read(self.domains(params).split("\n")),
         "output_dir": cwd,
         "shared_model": True,
         "input_psmac_dirs": path.join(cwd, "run_*"),
      })

      tae = tae if tae else Wrapper(self.runner).run

      try:
         res = Parallel(n_jobs=state.cores)(
            delayed(optimize)(self.SMAC, scenario, tae, n, self.config["log"]) 
               for n in range(state.cores)
         )
         inc = min(res, key=lambda x: x[1])[0]
      except Exception as err:
         log.msg("ERROR: SMAC failed: %s" % str(err))
         inc = params

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

