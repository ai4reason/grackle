import re
from os import path, getenv
from .runner import GrackleRunner
from ..trainer.lash.domain import DEFAULTS

L_BINARY = "lash"
L_STATIC = "-p tstp -m mode0 -M %s" % getenv("LASH_MODE_DIR", "./modes")

L_OK = ['Satisfiable', 'Unsatisfiable', 'Theorem', 'CounterSatisfiable', 'ContradictoryAxioms']
L_FAILED = ['ResourceOut', 'GaveUp']
L_RESULTS = L_OK + L_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

PATS = {
   "STATUS": re.compile(r"^% SZS status (\S*)$", flags=re.MULTILINE),
   "STEPS" : re.compile(r"^% Steps: (\d*)$", flags=re.MULTILINE),
   #"USERTIME": re.compile(r"\buser\s*(\d*)m(\d*\.\d*)s\b")
   "USERTIME": re.compile(r"\buser\s*(\d*\.\d*)\b")
}

VALS = {
   "STATUS": lambda mo: mo.group(1) if mo else "ResourceOut",
   "STEPS": lambda mo: int(mo.group(1)) if mo else -1,
   #"USERTIME": lambda mo: 60*int(mo.group(1))+float(mo.group(2)) if mo else 999999999
   "USERTIME": lambda mo: float(mo.group(1)) if mo else 999999999
}

class LashRunner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      #self.conds = self.conditions(CONDITIONS)

   def args(self, params):
      def one(arg, val):
         return f"-flag {arg} {val}"
      return " ".join([one(x,params[x]) for x in sorted(params)])

   def cmd(self, params, inst):
      params = self.clean(params)
      args = self.args(params)
      problem = path.join(getenv("PYPROVE_BENCHMARKS", "."), inst)
      timeout = (TIMEOUT % self.config["timeout"]) if "timeout" in self.config else ""
      #cmdargs = f"time {timeout}{L_BINARY} {L_STATIC}{args} {problem}"
      cmdargs = f"time -p {timeout}{L_BINARY} {L_STATIC} {args} {problem}"
      return cmdargs

   def process(self, out, inst):
      out = out.decode()
      res = {key:VALS[key](PATS[key].search(out)) for key in PATS}
      result = res["STATUS"]
      if result not in L_RESULTS:
         return None
      ok = self.success(result)
      runtime = res["USERTIME"] if ok else self.config["timeout"]
      quality = 10+int(1000*runtime) if ok else self.config["penalty"]
      resources = res["STEPS"]
      return [quality, runtime, result, resources]

   def success(self, result):
      return result in L_OK

   def clean(self, params):
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      return params

