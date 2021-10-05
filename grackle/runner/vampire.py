import re
from os import path, getenv
from .runner import GrackleRunner
from grackle.trainer.vampire.domain import DEFAULTS, REPLACE, CONDITIONS

V_BINARY = "vampire"
V_STATIC = "--proof off -stat full --input_syntax tptp"
V_LIMIT = " --time_limit %ss"

V_OK = ['Satisfiable', 'Unsatisfiable', 'Theorem', 'CounterSatisfiable', 'ContradictoryAxioms']
V_FAILED = ['ResourceOut', 'GaveUp']
V_RESULTS = V_OK + V_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

KEYS = [
   "SZS status",
   "Time elapsed:",
   "Active clauses:",
   "Termination reason:",
]

PAT = re.compile(r"^%% (%s) (\S*)" % "|".join(KEYS), flags=re.MULTILINE)

class VampireRunner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      self.conds = self.conditions(CONDITIONS)

   def args(self, params):
      def one(arg, val):
         if val.startswith("__"):
            val = val[2:]
         if arg in REPLACE:
            val = val.replace("_", REPLACE[arg])
         return f"--{arg} {val}"
      return " ".join([one(x,params[x]) for x in sorted(params)])

   def cmd(self, params, inst):
      params = self.clean(params)
      args = self.args(params)
      problem = path.join(getenv("PYPROVE_BENCHMARKS", "."), inst)
      vlimit = V_LIMIT % self.config["timeout"] if "timeout" in self.config else ""
      timeout = TIMEOUT % (self.config["timeout"]+1) if "timeout" in self.config else ""
      cmdargs = f"{timeout}{V_BINARY} {V_STATIC}{vlimit} {args} {problem}"
      return cmdargs

   def process(self, out, inst):
      def get(key):
         return res[key] if key in res else None
      out = out.decode()
      res = dict(PAT.findall(out))
      runtime = get("Time elapsed:")
      result = get("SZS status")
      if result not in V_RESULTS:
         reason = get("Termination reason:")
         if not reason:
            return None
         if reason == "Time":
            result = "ResourceOut"
         elif reason == "Refutation":
            result = "GaveUp"
         else:
            return None
      resources = get("Active clauses:")
      if (runtime is None) or (result is None):
         return [100*self.config["penalty"], self.config["timeout"], "failed", -1]
      resources = int(resources) if resources else -1
      runtime = float(runtime)
      quality = int(1000*runtime)
      return [quality, runtime, result, resources]

   def success(self, result):
      return result in V_OK

   def clean(self, params):
      # clean default values
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      # clean conditioned arguments
      delme = []
      for x in params:
         if x not in self.conds:
            continue
         for y in self.conds[x]:
            if y in params and params[y] not in self.conds[x][y]:
               delme.append(x)
      for x in delme:
         del params[x]
      return params

   def conditions(self, s_conds):
      conds = {}
      for line in s_conds.strip().split("\n"):
         (name, cond) = line.strip().split("|")
         name = name.strip()
         (cname, vals) = cond.split(" in ")
         cname = cname.strip()
         vals = vals.strip().strip("{}").split(",")
         vals = frozenset([x.strip() for x in vals])
         if name not in conds:
            conds[name] = {}
         conds[name][cname] = vals
      return conds
            
