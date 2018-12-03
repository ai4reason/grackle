from os import path, system

from .trainer import Trainer
from .. import paramils


SCENARIO = """
algo = grackle-wrapper.py %s
execdir = .
deterministic = 1
run_obj = runlength
overall_obj = mean
cutoff_time = 60
cutoff_length = max
tunerTimeout = 360000
paramfile = params.txt
outdir = paramils-out
instance_file = instances.txt
test_instance_file = empty.tst
"""

PARAMS = """
p {knn,nbayes} [knn]

c {1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5,17.0,17.5,18.0,18.5,19.0,19.5,20.0,21,22,23,24,25,26,27,28,29,30,35,40,50,60,70,80,90,100} [6.0]
d {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000} [3]

l {0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0} [0.2]
m {0.05,0.1,0.15,0.2,0.25,0.5,0.75,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.0,3.25,3.5,3.75,4.0,4.25,4.5,4.75,5.0} [5.0]
o {5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175,180,185,190,195,200} [20]

c | p in {knn}
d | p in {knn}
m | p in {nbayes}
l | p in {nbayes}
o | p in {nbayes}
"""

class PremiseTrainer(Trainer):
   def __init__(self, runner, cls):
      Trainer.__init__(self, runner)
      self.cls = cls

   def improve(self, state, conf, insts):
      cwd = path.join("training","iter-%03d-%s"%(state.it,conf))
      system("rm -fr %s" % cwd)
      system("mkdir -p %s" % cwd)
      init = self.runner.recall(conf)
      init = " ".join(["%s %s"%(x,init[x]) for x in sorted(init)])
      
      f_scenario = path.join(cwd, "scenario.txt")
      f_params = path.join(cwd, "params.txt")
      f_instances = path.join(cwd, "instances.txt")
      f_empty = path.join(cwd, "empty.tst")
      f_init = path.join(cwd, "init_00")
      
      file(f_scenario,"w").write(SCENARIO % self.cls)
      file(f_params,"w").write(PARAMS)
      file(f_instances,"w").write("\n".join(insts))
      file(f_empty,"w").write("")
      file(f_init,"w").write(init)

      params = paramils.reparamils.run_reparamils(
         "scenario.txt",
         path.join(cwd,"paramils-out"),
         cwd,
         count=state.cores,
         N=len(insts),
         validN=str(len(insts)),
         init="init_00",
         #out=None,
         out=file(path.join(cwd,"paramils.out"),"w"),
         time_limit=state.train_limit)

      params = self.runner.clean(params)
      return self.runner.name(params) 

