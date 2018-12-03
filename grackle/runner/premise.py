import re
import sha
from os import path, system

from .runner import Runner

class PremiseRunner(Runner):
   RESULT = re.compile(r"Auc: ([01]\.[0-9]*)")

   def __init__(self, direct=True, cores=4):
      Runner.__init__(self, direct, cores)
      self.conf_prefix = "conf_premise_"
      self.conf_dir = "confs"
      system("mkdir -p %s" % self.conf_dir)

   def cmd(self, params, inst, limit=None):
      args = self.args(params)
      return "%s premise-eval.sh %s %s" % (Runner.PERF, inst, args)
   
   def quality(self, out):
      q = Runner.quality(self, out)
      return int(10000*(1.0-float(q))) if q else None

   def clock(self, out):
      c = Runner.clock(self, out)
      return int((float(c)/1000.0)*1000)/1000.0 if c else None

   def name(self, params):
      args = self.repr(params).replace("="," ")
      conf = self.conf_prefix+sha.sha(args).hexdigest()
      file(path.join(self.conf_dir,conf),"w").write(args)
      return conf

   def recall(self, conf):
      args = file(path.join(self.conf_dir,conf)).read().strip()
      return self.params(args.split())
  
   def clean(self, params):
      if params["p"] == "knn":
         delete = ["m","l","o"]
      elif params["p"] == "nbayes":
         delete = ["c","d"]
      else:
         raise Exception("Uknown value for param 'p':"%params[p])

      for x in delete:
         if x in params:
            del params[x]

      return params
