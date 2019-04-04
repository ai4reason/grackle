import json
import time
from os import path
from . import _load_class, log
from atpy import expres

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

      unused = set(ini)
      def require(key, default):
         if key not in ini:
            return default
         unused.remove(key)
         return ini[key] 

      self.cores = require("cores", 4)
      self.tops = require("tops", 10)
      self.best = require("best", 4)
      self.rank = require("rank", 1)
      self.timeout = require("timeout", 0)

      def copy(to, prefix):
         for x in ini:
            if x.startswith(prefix):
               ix = ini[x]
               to[x[len(prefix):]] = int(ix) if ix.isdigit() else ix
               if x in unused:
                  unused.remove(x)

      def runner(name):
         conf = {"direct":False, "cores":self.cores}
         conf["cls"] = ini["%s.runner"%name]
         copy(conf, "%s.runner."%name)
         copy(conf, "runner.")
         return _load_class(conf["cls"])(conf)

      def data(name):
         did = ini["%s.data"%name]
         if did.startswith("atpy:"):
            bid = did[5:]
            insts = expres.benchmarks.problems(bid)
            insts = [path.join(bid,x) for x in insts]
         else:
            insts = file(did).read().strip().split("\n")
            insts = [x.strip() for x in insts]
         return insts

      def setup(db):
         db.runner = runner(db.name)
         db.insts = data(db.name)

      self.trains = DB("trains", self.rank)
      setup(self.trains)
      if "evals.data" in ini:
         self.evals = DB("evals", self.rank)
         setup(self.evals)
      else:
         self.evals = self.trains
      
      self.trainer = _load_class(ini["trainer"])(t_runner, ini["runner"])
      copy(self.trainer.config, "trainer.")
      
      log.scenario(self, ini, unused)

      self.attention = {i:0.0 for i in self.trains.insts}
      self.alls = []
      inits = file(ini["inits"]).read().strip().split("\n")
      runner = self.trains.runner
      for f_init in inits:
         params = runner.parse(file(f_init).read().strip().split())
         params = runner.clean(params)
         init = runner.name(params)
         self.alls.append(init)
         log.init(self, f_init, init)
      log.inits(self)


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


