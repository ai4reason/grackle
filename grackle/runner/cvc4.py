from os import path, getenv
from .runner import GrackleRunner
from grackle.trainer.cvc4 import DEFAULTS

CVC4_BINARY = "cvc4"
CVC4_STATIC = "-L smt2.6 --no-incremental --no-type-checking --no-interactive --stats"
CVC4_LIMIT = "--rlimit=%s"

CVC4_OK = ["sat", "unsat"]
CVC4_FAILED = ["unknown", "timeout"]
CVC4_RESULTS = CVC4_OK + CVC4_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

class Cvc4Runner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("cutoff", 100000)
      cutoff = self.config["cutoff"]
      self.default("penalty", 1000*cutoff)
      penalty = self.config["penalty"]
      self.default("penalty.unknown", penalty)
      self.default("penalty.timeout", penalty)

   def args(self, params):
      def one(arg, val):
         arg = arg.replace("_", "-")
         val = val.replace("_", "-")
         if val == "yes":
            return f"--{arg}"
         elif val == "no":
            return f"--no-{arg}"
         else:
            return f"--{arg}={val}"
      return " ".join([one(x,params[x]) for x in sorted(params)])

   def cmd(self, params, inst):
      args = self.args(params)
      limit = CVC4_LIMIT % self.config["cutoff"]
      problem = path.join(getenv("SMTLIB_BENCHMARKS", "."), inst)
      timeout = TIMEOUT % self.config["timeout"] if "timeout" in self.config else ""
      return f"{timeout}{CVC4_BINARY} {CVC4_STATIC} {limit} {args} {problem}"

   def process(self, out, inst):
      out = out.decode().split("\n")
      res = out[0]
      if "interrupted" in res:
         res = "timeout"
      if res not in CVC4_RESULTS:
         return None
      (runtime, quality) = self.output(out[1:])
      q = quality
      if res == "timeout": #or quality > self.config["cutoff"]:  
         quality = self.config["penalty.timeout"]
      elif res == "unknown":
         quality = self.config["penalty.unknown"]
      if (runtime is None) or (quality is None):
         return None
      return [quality, runtime, res, q]

   def output(self, lines):
      (runtime, resources) = (None, None)
      for line in lines:
         if line.startswith("resource::resourceUnitsUsed,"):
            resources = int(line.split(" ")[1])
         elif line.startswith("driver::totalTime,"):
            runtime = float(line.split(" ")[1])
      return (runtime, resources)

   def success(self, result):
      return result in CVC4_OK

   def clean(self, params):
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      return params


