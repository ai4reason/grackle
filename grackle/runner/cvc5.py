from os import path, getenv
from .runner import GrackleRunner
from grackle.trainer.cvc5.domain import DEFAULTS, CONDITIONS

CVC5_BINARY = "cvc5"
CVC5_STATIC = "-L smt2.6 --no-incremental --no-type-checking --no-interactive --stats --stats-internal"
CVC5_LIMIT = " --rlimit=%s"

CVC5_OK = ["sat", "unsat"]
CVC5_FAILED = ["unknown", "timeout"]
CVC5_RESULTS = CVC5_OK + CVC5_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

class Cvc5Runner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      penalty = self.config["penalty"]
      self.default("penalty.unknown", penalty)
      self.default("penalty.timeout", penalty)
      self.default("penalty.sat", False)
      self.default("log_solved", False)
      self.conds = self.conditions(CONDITIONS)
      self._args = None

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
      self._args = args
      problem = path.join(getenv("PYPROVE_BENCHMARKS", "."), inst)
      rlimit = CVC5_LIMIT % self.config["rlimit"] if "rlimit" in self.config else ""
      timeout = TIMEOUT % self.config["timeout"] if "timeout" in self.config else ""
      cmdargs = f"{timeout}{CVC5_BINARY} {CVC5_STATIC}{rlimit} {args} {problem}"
      return cmdargs

   def process(self, out, inst):
      out = out.decode().split("\n")
      while len(out)>1 and out[0].startswith("Warning"):
         out = out[1:]
      result = out[0]
      if ("interrupted" in result):
         result = "timeout"
      if result not in CVC5_RESULTS:
         return None
         #result = "unknown"
      (runtime, resources) = self.output(out[1:])
      #failed = [100*self.config["penalty.unknown"], self.config["timeout"], "failed", -1]
      failed = None
      if (runtime is None):
         return failed
      quality = resources if "rlimit" in self.config else 1000*runtime # use ms as quality
      if result == "timeout": #or quality > self.config["cutoff"]:  
         quality = self.config["penalty.timeout"]
      elif result == "unknown":
         quality = self.config["penalty.unknown"]
      elif result == "sat" and self.config["penalty.sat"]:
         quality = self.config["penalty.sat"]
      elif self.config["log_solved"]:
         with open("solved.log","a",buffering=1) as f:
            f.write(f"{inst} {result} {quality} {self._args}\n")

      if (runtime is None) or (quality is None):
         return failed
      return [quality, runtime, result, resources]

   def output(self, lines):
      (runtime, resources) = (None, None)
      for line in lines:
         if line.startswith("resource::resourceUnitsUsed"):
            resources = int(line.split("=")[1])
         elif line.startswith("driver::totalTime"):
            runtime = float(line.split("=")[1])
         elif line.startswith("global::totalTime"):
            runtime = float(line.split("=")[1].rstrip("ms")) / 1000
      return (runtime, resources)

   def success(self, result):
      return result in CVC5_OK

   def clean(self, params):
      # clean default values
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      # clean conditioned arguments
      delme = set()
      idle = False
      while not idle:
         idle = True
         for x in params:
            if x not in self.conds:
               continue
            for y in self.conds[x]:
               val = params[y] if y in params else DEFAULTS[y]
               if val not in self.conds[x][y]:
                  delme.add(x)
                  break
         for x in delme:
            del params[x]
            idle = False
         delme.clear()
      return params

def wrapper(conf, instance, config={}):
   runner = Cvc5Runner(config)
   result = runner.run(conf, instance)
   return (result[0], result[1:]) 

