import json
from os import path
from . import _load_class, log

class DB:
   def __init__(self, name, rank):
      self.name = name
      self.insts = []      # all instances
      self.results = {}    # { conf : {inst:[quality,runtime,..]} }
      self.ranking = {}    # { inst : [conf] }
      self.runner = None
      self.rank = rank
      self.load("cache")

   def load(self, prefix):
      f_results = "db-%s-%s.json" % (self.name,prefix)
      if path.isfile(f_results):
         self.results = json.load(file(f_results))

   def save(self, prefix):
      f_results = "db-%s-%s.json" % (self.name,prefix)
      json.dump(self.results, file(f_results,"w"))

   def update(self, confs):
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
  
      # udpate ranking for each instance
      self.update_ranking(confs)

   def update_ranking(self, confs):
      self.ranking = {}
      for inst in self.insts:
         key = lambda conf: self.results[conf][inst][0]
         self.ranking[inst] = sorted(confs, key=key)

   def mastered(self, conf):
      return [i for i in self.insts if conf in self.ranking[i][:self.rank]]

class State:
   def __init__(self, f_run):
      ini = file(f_run).read().strip().split("\n")
      ini = [l.split("=") for l in ini]
      ini = {x.strip():y.strip() for (x,y) in ini}

      self.it = 0          # int
      self.done = {}       # { conf : set(frozenset(train)) }
      self.active = []     # [conf]

      self.cores = int(ini["cores"]) if "cores" in ini else 4
      self.tops = int(ini["tops"]) if "tops" in ini else 10
      self.best = int(ini["best"]) if "best" in ini else 4
      self.rank = int(ini["rank"]) if "rank" in ini else 1
      self.train_limit = int(ini["train_time"]) if "train_time" in ini else None
      if self.train_limit < 0:
         self.train_limit = None

      runner = _load_class(ini["runner"])(False, self.cores)
      self.evals = DB("evals", self.rank)
      self.evals.runner = runner
      self.evals.insts = file(ini["evals"]).read().strip().split("\n")
      self.evals.insts = [x.strip() for x in self.evals.insts]
      self.trains = DB("trains", self.rank)
      self.trains.runner = runner
      self.trains.insts = file(ini["trains"]).read().strip().split("\n")
      self.trains.insts = [x.strip() for x in self.trains.insts]
      self.attention = {i:0.0 for i in self.trains.insts}
      log.scenario(self, ini)

      self.alls = []
      inits = file(ini["inits"]).read().strip().split("\n")
      for f_init in inits:
         params = runner.params(file(f_init).read().strip().split())
         params = runner.clean(params)
         init = runner.name(params)
         self.alls.append(init)
         log.init(self, f_init, init)
      log.inits(self)

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

