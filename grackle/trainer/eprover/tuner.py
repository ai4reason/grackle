from os import system, path
from grackle import paramils
from grackle.runner.eprover import EproverRunner, convert, SINE_DEFAULTS
from . import domain


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

def launch(scenario, domains, init, insts, cwd, timeout, cores):
   system("rm -fr %s" % cwd)
   system("mkdir -p %s" % cwd)

   f_scenario = path.join(cwd, "scenario.txt")
   f_params = path.join(cwd, "params.txt")
   f_instances = path.join(cwd, "instances.txt")
   f_empty = path.join(cwd, "empty.tst")
   f_init = path.join(cwd, "init_00")
   
   file(f_scenario,"w").write(scenario)
   file(f_params,"w").write(domains)
   file(f_instances,"w").write("\n".join(insts))
   file(f_empty,"w").write("")
   file(f_init,"w").write(" ".join(["%s %s"%(x,init[x]) for x in sorted(init)]))

   params = paramils.reparamils.run_reparamils(
      "scenario.txt",
      path.join(cwd,"paramils-out"),
      cwd,
      count=cores,
      N=len(insts),
      validN=str(len(insts)),
      init="init_00",
      out=None,
      #out=file(path.join(cwd,"paramils.out"),"w"),
      time_limit=timeout)

   return params

class Tuner(EproverRunner):
   def __init__(self, direct, cores, nick, cls):
      EproverRunner.__init__(self, direct, cores=cores)
      self.nick = nick
      self.cls = cls

   def split(self, params):
      pass

   def join(self, main, extra):
      pass

   def domains(self, config, init=None):
      pass
   
   def cmd(self, params, inst, limit=None, extra=None):
      params = self.join(params, extra)
      return EproverRunner.cmd(self, params, inst, limit=limit)

class BaseTuner(Tuner):
   def __init__(self, direct, cores=4, nick="0-base"):
      Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.BaseTuner")

   def split(self, params):
      params = convert(params)
      main = {x:params[x] for x in params if not (x.startswith("tord") or x.startswith("sine"))}
      extra = {x:params[x] for x in params if x.startswith("tord") or x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return domain.base(config, init=init)

class GlobalTuner(Tuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.GlobalTuner")

   def split(self, params):
      main = {x:params[x] for x in params if not x.startswith("sine")}
      extra = {x:params[x] for x in params if x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return domain.glob(config, init=init)

class SineTuner(Tuner):
   def __init__(self, direct, cores=4, nick="0-sine"):
      Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.SineTuner")

   def split(self, params):
      params = convert(params)
      main = dict(SINE_DEFAULTS)
      main.update({x:params[x] for x in params if x.startswith("sine")})
      del main["sine"]
      extra = {x:params[x] for x in params if not x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      params["sine"] = "1"
      return params

   def domains(self, config, init=None):
      return domain.sine()

class OrderTuner(Tuner):
   def __init__(self, direct, cores=4, nick="1-order"):
      Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.OrderTuner")

   def split(self, params):
      params = convert(params)
      main = {x:params[x] for x in params if x.startswith("tord")}
      extra = {x:params[x] for x in params if not x.startswith("tord")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return domain.order()

class FineTuner(Tuner):
   def __init__(self, direct, cores=4, nick="2-fine"):
      Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.FineTuner")

   def split(self, params):
      main = domain.fine_main(params)
      extra = {x:params[x] for x in params if not x.startswith("cef")}
      weights = {x:params[x].split("__")[0] for  x in params if x.startswith("cef")}
      extra.update(weights)
      return (main, extra)

   def join(self, main, extra):
      cefs = domain.fine_cefs(main, extra)
      params = dict(extra)
      params.update(cefs)
      return params

   def domains(self, config, init=None):
      return domain.fine(init)

GLOBAL = lambda nick: GlobalTuner(True, 1, nick)
BASE  = lambda nick: BaseTuner(True, 1, nick)
FINE  = lambda nick: FineTuner(True, 1, nick)
SINE = lambda nick: SineTuner(True, 1, nick)
ORDER = lambda nick: OrderTuner(True, 1, nick)

