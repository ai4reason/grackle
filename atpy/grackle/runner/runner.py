import re
import sys
import sha
import time
import commands
import multiprocessing

from .. import log

def wrapper(args):
   (runner, (x, inst)) = args
   return runner.run(x, inst)

class Runner(object):
   PERF = "perf stat -e task-clock:up,page-faults:up,instructions:up"
   CLOCK = re.compile(r"(\d*\.\d*)\s*task-clock:up")
   RESULT = re.compile(r"Auc: ([01]\.[0-9]*)")

   def __init__(self, direct, cores=4):
      self.direct = direct
      self.cores = cores

   def cmd(self, params, inst):
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
   
   def quality(self, out):
      mo = Runner.RESULT.search(out)
      return mo.group(1) if mo else None

   def clock(self, out):
      mo = Runner.CLOCK.search(out)
      return mo.group(1) if mo else None

   def params(self, lst):
      ps = {}
      while lst:
         key = lst.pop(0).lstrip("-").strip()
         val = lst.pop(0).strip()
         ps[key] = val
      return ps
   
   def run(self, c, inst, limit=None):
      if not self.direct:
         params = self.recall(c)
      else:
         # when self.direct, then pass params directly (not by name)!
         params = c
      cmd = self.cmd(params, inst)
      start = time.time()
      (status,out) = commands.getstatusoutput(cmd)
      end = time.time()
      if status != 0:
         print "GRACKLE: Error while evaluating %s on instance %s!\ncommand: %s\noutput: \n%s\n"%(c,inst,cmd,out)
         return None
      
      quality = self.quality(out) or 1000000000
      clock = self.clock(out) or (end-start)
      return [quality,clock]

   def runs(self, cis):
      pool = multiprocessing.Pool(self.cores)
      results = pool.map(wrapper, zip([self]*len(cis),cis))
      if None in results:
         log.error("GRACKLE: Error: Evaluation failed, see above for more info.")
         sys.exit(-1)
      return zip(cis, results)
   
