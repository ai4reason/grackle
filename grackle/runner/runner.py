import os
import re
import sys
import sha
import time
import subprocess
import multiprocessing

from .. import log

def wrapper(args):
   (runner, (x, inst)) = args
   limit = runner.config["cutoff"] if "cutoff" in runner.config else None
   return runner.run(x, inst, limit=limit)
         
class Runner(object):
   PERF = "perf stat -e task-clock:up,page-faults:up,instructions:up"
   CLOCK = re.compile(r"(\d*\.\d*)\s*task-clock:up")
   RESULT = re.compile(r"Auc: ([01]\.[0-9]*)")

   def __init__(self, direct, cores=4):
      self.direct = direct
      self.cores = cores
      self.config = {}

   def cmd(self, params, inst, limit=None, extra=None):
      pass

   def process(self, out, inst):
      pass

   def args(self, params):
      return " ".join(["-%s %s"%(p,params[p]) for p in sorted(params)])

   def repr(self, params):
      return " ".join(["%s=%s"%(p,params[p]) for p in sorted(params)])
  
   def name(self, params):
      return params

   def recall(self, conf):
      return conf

   def clean(self, params):
      return params
   
   def params(self, lst):
      ps = {}
      while lst:
         key = lst.pop(0).lstrip("-").strip()
         val = lst.pop(0).strip()
         ps[key] = val
      return ps
   
   def run(self, c, inst, limit=None, extra=None):
      if not self.direct:
         params = self.recall(c)
      else:
         # when self.direct, then pass params directly (not by name)!
         params = c
      cmd = self.cmd(params, inst, limit=limit, extra=extra)
      
      start = time.time()
      try:
         out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
      except subprocess.CalledProcessError as err:
         out = err.output
      except BaseException as err:
         log.fatal("ERROR(Grackle): Runner failed: %s" % (err.message or err.__class__.__name__))
         sys.exit(-1)

      end = time.time()
      
      res = self.process(out, inst, limit)
      if not res:
         msg = "\nERROR(Grackle): Error while evaluating %s on instance %s!\ncommand: %s\noutput: \n%s\n"%(c,inst,cmd,out)
         log.fatal(msg)
         return None

      return res

   def runs(self, cis):
      pool = multiprocessing.Pool(self.cores)
      try:
         results = pool.map_async(wrapper, zip([self]*len(cis),cis)).get(10000000)
      except BaseException as err:
         pool.terminate()
         log.fatal("ERROR(Grackle): Evaluation failed: %s" % (err.message or err.__class__.__name__))
         sys.exit(-1)
      else:
         pool.close()
      if None in results:
         log.fatal("ERROR(Grackle): Evaluation failed, see above for more info.")
         sys.exit(-1)
      return zip(cis, results)

