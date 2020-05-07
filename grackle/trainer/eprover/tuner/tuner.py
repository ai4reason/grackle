from os import system, path
from grackle import paramils
from grackle.runner.eprover import EproverRunner 


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
   
   open(f_scenario,"w").write(scenario)
   open(f_params,"w").write(domains)
   open(f_instances,"w").write("\n".join(insts))
   open(f_empty,"w").write("")
   open(f_init,"w").write(" ".join(["%s %s"%(x,init[x]) for x in sorted(init)]))

   params = paramils.reparamils.reparamils(
      "scenario.txt",
      path.join(cwd,"paramils-out"),
      cwd,
      count=cores,
      N=len(insts),
      validN=str(len(insts)),
      init="init_00",
      #out=None,
      out=open(path.join(cwd,"paramils.out"),"w"),
      time_limit=timeout)

   return params

class Tuner(EproverRunner):
   def __init__(self, direct, cores, nick, cls):
      conf = {"direct":direct, "cores":cores}
      EproverRunner.__init__(self, conf)
      self.nick = nick
      self.cls = cls

   def split(self, params):
      pass

   def join(self, main, extra):
      pass

   def domains(self, config, init=None):
      pass
   
   def cmd(self, params, inst):
      if "extra" in self.config:
         params = self.join(params, self.config["extra"])
      return EproverRunner.cmd(self, params, inst)


