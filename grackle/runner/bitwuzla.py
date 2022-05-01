import re
from os import path, getenv
from .runner import GrackleRunner
from ..trainer.bitwuzla.domain import DEFAULTS, CONDITIONS

BWZ_BINARY = "bitwuzla"
BWZ_STATIC = "-v" # -t=1 -l=1 --smt2

BWZ_OK = ['sat', 'unsat']
BWZ_FAILED = ['unknown']
BWZ_RESULTS = BWZ_OK + BWZ_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

PATS = {
   "STATUS"  : re.compile(r"^(sat|unsat|unknown)$", flags=re.MULTILINE),
   "LOGIC"   : re.compile(r"^\[bitwuzla\>parse\] logic (\S*)$", flags=re.MULTILINE),
   "EXPECTED": re.compile(r"^\[bitwuzla\>parse\] status (\S*)$", flags=re.MULTILINE),
   "USERTIME": re.compile(r"\buser\s*(\d*\.\d*)\b")
}

def format1(notfound="error", apply=str):
   def handle(mo):
      return apply(mo.group(1)) if mo else notfound
   return handle

VALS = {
   "STATUS"  : format1(),
   "LOGIC"   : format1(),
   "EXPECTED": format1(),
   "USERTIME": format1(999999999, float),
}

class BitwuzlaRunner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      self.conds = self.conditions(CONDITIONS)

   def args(self, params):
      def one(arg, val):
         arg = arg.replace("_","-")
         return f"--{arg}={val}"
      return " ".join([one(x,params[x]) for x in sorted(params)])

   def cmd(self, params, inst):
      params = self.clean(params)
      args = self.args(params)
      problem = path.join(getenv("PYPROVE_BENCHMARKS", "."), inst)
      if "timeout" in self.config:
         t = self.config["timeout"]
         timeout = TIMEOUT % (t+1)
         limit = f" -t={t}"
      else:
         timeout = ""
         limit = ""
      cmdargs = f"time -p {timeout}{BWZ_BINARY}{limit} {BWZ_STATIC} {args} {problem}"
      return cmdargs

   def process(self, out, inst):
      out = out.decode()
      res = {key:VALS[key](PATS[key].search(out)) for key in PATS}
      result = res["STATUS"]
      if result not in BWZ_RESULTS:
         return None
      ok = self.success(result)
      runtime = res["USERTIME"] if ok else self.config["timeout"]
      quality = 10+int(1000*runtime) if ok else self.config["penalty"]
      return [quality, runtime, result]

   def success(self, result):
      return result in BWZ_OK

   def clean(self, params):
      # clean default values
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      # clean conditioned arguments
      delme = set()
      for x in params:
         if x not in self.conds:
            continue
         for y in self.conds[x]:
            if y in params and params[y] not in self.conds[x][y]:
               delme.add(x)
               break
      for x in delme:
         del params[x]
      return params

