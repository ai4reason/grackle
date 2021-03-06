import json
import time
from os import path
from . import _load_class, log
from pyprove import expres

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
         self.results = json.load(open(f_results))

   def save(self, prefix):
      f_results = "db-%s-%s.json" % (self.name,prefix)
      json.dump(self.results, open(f_results,"w"), indent=3, sort_keys=True)

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
         oks = [c for c in confs if self.results[c][inst] and self.results[c][inst][0] != failed]
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
            result = result if result else (1000*failed, 0)
            qsum += result[0]
            tsum += result[1]
            total += 1
            if result[0] != failed:
               success.add(inst)
      return (self.name, len(success), qsum/total, tsum/total)

def convert(string):
   if string == "True":
      return True
   elif string == "False":
      return False
   elif string.isdigit():
      return int(string)
   else:
      return string

class State:
   def __init__(self, f_run):
      self.start_time = time.time()

      ini = open(f_run).read().strip().split("\n")
      ini = [l.split("=") for l in ini if l]
      ini = {x.strip():y.strip() for (x,y) in ini}

      self.it = 0          # int
      self.done = {}       # { conf : set(frozenset(train)) }
      self.active = []     # [conf]

      unused = set(ini)
      def require(key, default):
         if key not in ini:
            log.msg("Warning: Setting configuration key '%s' to the default value '%s'" % (key, default))
            return default
         unused.remove(key)
         ix = ini[key] 
         return convert(ix)

      def check(key):
         if key not in ini:
            raise Exception("Required configuration key '%s' not specified" % key)
         unused.remove(key)

      self.cores = require("cores", 4)
      self.tops = require("tops", 10)
      self.best = require("best", 4)
      self.rank = require("rank", 1)
      self.timeout = require("timeout", 0)

      def copy(to, prefix):
         for x in ini:
            if x.startswith(prefix):
               ix = ini[x]
               to[x[len(prefix):]] = convert(ix)
               if x in unused:
                  unused.remove(x)

      def runner(name):
         conf = {"direct":False, "cores":self.cores}
         conf["cls"] = ini["%s.runner"%name]
         copy(conf, "runner.")
         copy(conf, "%s.runner."%name)
         return _load_class(conf["cls"])(conf)

      def data(name):
         did = ini["%s.data"%name]
         if did.startswith("pyprove:"):
            bid = did[8:]
            insts = expres.benchmarks.problems(bid)
            insts = [path.join(bid,x) for x in insts]
         else:
            insts = open(did).read().strip().split("\n")
            insts = [x.strip() for x in insts]
         return insts

      def setup(db):
         db.runner = runner(db.name)
         db.insts = data(db.name)

      self.trains = DB("trains", self.rank)
      check("trains.data")
      check("trains.runner")
      setup(self.trains)
      if "evals.data" in ini:
         check("evals.data")
         check("evals.runner")
         self.evals = DB("evals", self.rank)
         setup(self.evals)
      else:
         self.evals = self.trains
      
      check("trainer")
      t_runner = runner("trainer")
      self.trainer = _load_class(ini["trainer"])(t_runner, ini["trainer.runner"])
      copy(self.trainer.config, "trainer.")
      copy(self.trainer.runner.config, "trainer.runner.")
      
      check("inits")
      log.scenario(self, ini, unused)

      self.attention = {i:0.0 for i in self.trains.insts}
      self.alls = []
      inits = open(ini["inits"]).read().strip().split("\n")
      runner = self.trains.runner
      for f_init in inits:
         params = runner.parse(open(f_init).read().strip().split())
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


