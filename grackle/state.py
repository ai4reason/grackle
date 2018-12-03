import json
import time
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

   def update_ranking(self, confs, failed=1000000):
      self.ranking = {}
      for inst in self.insts:
         key = lambda conf: (self.results[conf][inst][0], conf)
         oks = [c for c in confs if self.results[c][inst][0] != failed]
         self.ranking[inst] = sorted(oks, key=key)

   def mastered(self, conf):
      return [i for i in self.insts if conf in self.ranking[i][:self.rank]]

   def status(self, failed=1000000):
      total = 0
      qsum = 0.0
      tsum = 0.0
      success = set()
      for conf in self.results:
         for inst in self.insts:
            result = self.results[conf][inst]
            qsum += result[0]
            tsum += result[1]
            total += 1
            if result[0] != failed:
               success.add(inst)
      return (self.name, len(success), qsum/total, tsum/total)

def copy_conf(ini, config, prefix):
   for x in ini:
      if x.startswith(prefix):
         ix = ini[x]
         config[x[len(prefix):]] = int(ix) if ix.isdigit() else ix

class State:
   def __init__(self, f_run):
      self.start_time = time.time()

      ini = file(f_run).read().strip().split("\n")
      ini = [l.split("=") for l in ini if l]
      ini = {x.strip():y.strip() for (x,y) in ini}

      self.it = 0          # int
      self.done = {}       # { conf : set(frozenset(train)) }
      self.active = []     # [conf]

      self.cores = int(ini["cores"]) if "cores" in ini else 4
      self.tops = int(ini["tops"]) if "tops" in ini else 10
      self.best = int(ini["best"]) if "best" in ini else 4
      self.rank = int(ini["rank"]) if "rank" in ini else 1
      self.timeout = int(ini["timeout"]) if "timeout" in ini else 0
      self.train_limit = int(ini["train_time"]) if "train_time" in ini else None
      if self.train_limit < 0:
         self.train_limit = None

      t_runner = _load_class(ini["runner"])(False, self.cores)
      copy_conf(ini, t_runner.config, "runner.trains.")
      self.trains = DB("trains", self.rank)
      self.trains.runner = t_runner
      self.trains.insts = file(ini["trains"]).read().strip().split("\n")
      self.trains.insts = [x.strip() for x in self.trains.insts]

      if "evals" in ini:
         e_runner = _load_class(ini["runner"])(False, self.cores)
         copy_conf(ini, e_runner.config, "runner.evals.")
         self.evals = DB("evals", self.rank)
         self.evals.runner = e_runner
         self.evals.insts = file(ini["evals"]).read().strip().split("\n")
         self.evals.insts = [x.strip() for x in self.evals.insts]
      else:
         self.evals = self.trains

      self.attention = {i:0.0 for i in self.trains.insts}
      log.scenario(self, ini)

      self.alls = []
      inits = file(ini["inits"]).read().strip().split("\n")
      for f_init in inits:
         params = t_runner.params(file(f_init).read().strip().split())
         params = t_runner.clean(params)
         init = t_runner.name(params)
         self.alls.append(init)
         log.init(self, f_init, init)
      log.inits(self)

      self.trainer = _load_class(ini["trainer"])(t_runner, ini["runner"])
      copy_conf(ini, self.trainer.config, "trainer.")

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

   def timeouted(self):
      if not self.timeout:
         return False
      if "timeout" not in self.trainer.config:
         return False

      t_train = 3 * self.trainer.config["timeout"] 
      t_elapsed = time.time() - self.start_time 
      t_remains = self.timeout - t_elapsed

      return t_remains < t_train


