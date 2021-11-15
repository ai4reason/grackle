import time
from os import path
from . import log, unsolved
from .tools import load_class, convert, parse_ini
from .db import DB
from pyprove import expres

class State:
   def __init__(self, f_run):
      self.start_time = time.time()

      ini = parse_ini(f_run)

      self.it = 0          # int
      self.done = {}       # { conf : set(frozenset(train)) }
      self.active = []     # [conf]
      self.unsolved = {}

      unused = set(ini)
      def require(key, default, warn=True):
         if key not in ini:
            if warn:
               log.msg("Warning: Setting configuration key '%s' to the default value '%s'" % (key, default))
            return default
         unused.remove(key)
         ix = ini[key] 
         return convert(ix)

      def check(key):
         if key not in ini:
            raise Exception("Required configuration key '%s' not specified" % key)
         if key in unused:
            unused.remove(key)

      self.cores = require("cores", 4)
      self.tops = require("tops", 10)
      self.best = require("best", 4)
      self.rank = require("rank", 1)
      self.timeout = require("timeout", 0)
      self.atavistic = require("atavistic", True, warn=False)

      def copy(to, prefix, use=True):
         for x in ini:
            if x.startswith(prefix):
               ix = ini[x]
               to[x[len(prefix):]] = convert(ix)
               if use and (x in unused):
                  unused.remove(x)

      def runner(name, direct=False):
         conf = {"direct":direct, "cores":self.cores}
         conf["cls"] = ini["%s.runner"%name]
         copy(conf, "runner.")
         copy(conf, "%s.runner."%name)
         return load_class(conf["cls"])(conf)

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
      t_runner = runner("trainer", direct=True)
      self.trainer = load_class(ini["trainer"])(t_runner)
      self.trainer.config["cls"] = ini["trainer"]
      copy(self.trainer.config, "trainer.")
      copy(self.trainer.runner.config, "trainer.runner.")

      copy(self.unsolved, "unsolved.", use=False)
      if self.unsolved:
         check("unsolved.features")
         self.unsolved["ratio"] = require("unsolved.ratio", 1.0)
         self.unsolved["mode"] = require("unsolved.mode", "inits")
         self.unsolved["maxrank"] = require("unsolved.maxrank", 1)
         modes = ["inits", "all", "actives", "current"]
         if self.unsolved["mode"] not in modes:
            raise Exception("Unknown config value for 'unsolved.mode' (%s). Allowed values are: %s." % (self.unsolved["mode"], ", ".join(modes)))
         unsolved.init(self)
      
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

      if not self.atavistic:
         self.active = list(self.alls)

   def genofond(self):
      return self.alls if self.atavistic else self.active

   def newborn(self, conf):
      self.alls.append(conf)
      if not self.atavistic:
         self.active.append(conf)

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

   def timeouted(self, trainlimit):
      if (not self.timeout) or (not trainlimit):
         return False

      t_train = trainlimit
      t_elapsed = time.time() - self.start_time 
      t_remains = self.timeout - t_elapsed

      return t_remains < t_train


