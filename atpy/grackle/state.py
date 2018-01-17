import json
from os import path
from . import _load_class, log

class DB:
   def __init__(self, name):
      self.name = name
      self.insts = []      # all instances
      self.results = {}    # { conf : {inst:[quality,runtime,..]} }
      self.bests = {}      # { inst : conf }
      self.runner = None
      self.load("cache")

   def load(self, prefix):
      f_results = "db-%s-%s.json" % (self.name,prefix)
      if path.isfile(f_results):
         self.results = json.load(file(f_results))

   def save(self, prefix):
      f_results = "db-%s-%s.json" % (self.name,prefix)
      json.dump(self.results, file(f_results,"w"))

   def update(self, confs):
      dead = [i for i in self.bests if self.bests[i] not in confs]
      for i in dead:
         del self.bests[i]
   
      # collect (conf,inst) pairs to evaluate
      cis = []
      for conf in confs:
         if conf not in self.results:
            self.results[conf] = {}
         for inst in self.insts:
            if inst not in self.results[conf]:
               cis.append((conf,inst))
  
      # evaluate them
      if cis:
         outs = self.runner.runs(cis)
         for ((conf,inst),result) in outs:
            self.results[conf][inst] = result
  
      # udpate best configs for each instance
      self.update_bests(confs)

   def update_bests(self, confs):
      for conf in confs:
         for inst in self.insts:
            if inst not in self.bests:
               self.bests[inst] = conf
            else:
               result = self.results[conf][inst]
               current_best = self.results[self.bests[inst]][inst]
               if result[0] < current_best[0]:
                  self.bests[inst] = conf

   def eaten(self, conf):
      return [i for i in self.bests if self.bests[i]==conf]

class State:
   def __init__(self, f_run):
      ini = file(f_run).read().strip().split("\n")
      ini = [l.split("=") for l in ini]
      ini = {x.strip():y.strip() for (x,y) in ini}
      log.scenario(ini)

      self.it = 0          # int
      self.done = {}       # { conf : set(frozenset(train)) }
      self.active = []     # [conf]

      self.cores = int(ini["cores"]) if "cores" in ini else 4
      self.tops = int(ini["tops"]) if "tops" in ini else 10
      self.best = int(ini["best"]) if "best" in ini else 4

      runner = _load_class(ini["runner"])(False, self.cores)
      self.evals = DB("evals")
      self.evals.runner = runner
      self.evals.insts = file(ini["evals"]).read().strip().split("\n")
      self.evals.insts = [x.strip() for x in self.evals.insts]
      self.trains = DB("trains")
      self.trains.runner = runner
      self.trains.insts = file(ini["trains"]).read().strip().split("\n")
      self.trains.insts = [x.strip() for x in self.trains.insts]
      self.attention = {i:0.0 for i in self.trains.insts}
      log.instances(self)

      self.alls = []
      inits = file(ini["inits"]).read().strip().split("\n")
      for f_init in inits:
         params = runner.params(file(f_init).read().strip().split())
         params = runner.clean(params)
         init = runner.name(params)
         self.alls.append(init)
         log.init(self, f_init, init)

      self.trainer = _load_class(ini["trainer"])(runner, ini["runner"])

   def did(self, conf, insts):
      for i in insts:
         self.attention[i] += (1.0/len(insts))
      if conf not in self.done:
         self.done[conf] = set()
      self.done[conf].add(frozenset(insts))

   def improved(self, conf, insts):
      if conf not in self.done:
         return False
      return frozenset(insts) in self.done[conf]

