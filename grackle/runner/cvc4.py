from os import path, getenv
from .runner import GrackleRunner
from grackle.trainer.cvc4.domain import DEFAULTS

CVC4_BINARY = "cvc4"
CVC4_STATIC = "-L smt2.6 --no-incremental --no-type-checking --no-interactive --stats"
CVC4_LIMIT = " --rlimit=%s"

CVC4_OK = ["sat", "unsat"]
CVC4_FAILED = ["unknown", "timeout"]
CVC4_RESULTS = CVC4_OK + CVC4_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

class Cvc4Runner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
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
      problem = path.join(getenv("SMTLIB_BENCHMARKS", "."), inst)
      rlimit = CVC4_LIMIT % self.config["rlimit"] if "rlimit" in self.config else ""
      timeout = TIMEOUT % self.config["timeout"] if "timeout" in self.config else ""
      cmdargs = f"{timeout}{CVC4_BINARY} {CVC4_STATIC}{rlimit} {args} {problem}"
      return cmdargs

   def process(self, out, inst):
      out = out.decode().split("\n")
      result = out[0]
      if "interrupted" in result:
         result = "timeout"
      if result not in CVC4_RESULTS:
         return None
      (runtime, resources) = self.output(out[1:])
      quality = resources if "rlimit" in self.config else 1000*runtime # use ms as quality
      if result == "timeout": #or quality > self.config["cutoff"]:  
         quality = self.config["penalty.timeout"]
      elif result == "unknown":
         quality = self.config["penalty.unknown"]
      if (runtime is None) or (quality is None):
         return None
      return [quality, runtime, result, resources]

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

def wrapper(conf, instance, config={}):
   runner = Cvc4Runner(config)
   result = runner.run(conf, instance)
   return (result[0], result[1:]) if result else None

