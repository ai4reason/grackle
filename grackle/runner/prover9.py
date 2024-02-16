import re
import tempfile
import os 
from os import path, getenv
from .runner import GrackleRunner
#from grackle.trainer.prover9.domain import DEFAULTS
from grackle.trainer.prover9.default import DefaultDomain

P_BINARY = "prover9"
P_STATIC = "-f "     # is Prover9's flag for input files (strategies and problems)
P_LIMIT = " -t %ss"  # is Prover9's flag for time limit

# Prover9 has two possible states for End of Search: 
P_OK = ['THEOREM PROVED']
P_FAILED = ['SEARCH FAILED']
P_RESULTS = P_OK + P_FAILED

TIMEOUT = "timeout --kill-after=1 --foreground %s " # note the space at the end

KEYS = [
   #"SZS status",
   "User_CPU=",
   #"Active clauses:",
   #"Termination reason:",
]

PAT = re.compile(r"^%% (%s) (\S*)" % "|".join(KEYS), flags=re.MULTILINE)
pattern_wall_clock = r'User_CPU=(\d+\.\d+)' # We can take User_CPU, System_CPU, Wall_clock
pattern_kept = r'Kept=(\d+)'                # kept Clauses

INTS=frozenset("""
weight
literals
variables
depth
level
""".strip().split("\n"))

IGNORED = ["Fatal error:  renum_vars_recurse: too many variables"]

def make_action_flag(cur, selector=None):
   return "%(counter)s=%(cond)s -> %(action)s(%(flag)s).\n" % cur

def make_action_change(cur, selector=None):
   return "%(counter)s=%(cond)s -> assign(%(action)s, %(value)s).\n" % cur

def make_cond(cur, selector=None):
   cont = "" if "connect" not in cur else (" & " if cur['connect'] == "and" else " | ")
   if "cond" not in cur:
      return ""
   if cur['cond'] in INTS:
      sign = "<" if cur['neg'] == "no" else ">="
      return f"{cur['cond']}{sign}{cur['val']}{cont}"
   else:
      sign = "" if cur['neg'] == "no" else "-"
      return f"{sign}{cur['cond']}{cont}"

def make_given_low(cur, selector=None):
   prop = make_lines(cur, "prp", make_cond, "cond", "none").rstrip(" |&")
   return f"part({selector}, low, {cur['order']}, {prop}) = {cur['ratio']}.\n"

def make_given_high(cur, selector=None):
   prop = make_lines(cur, "prp", make_cond, "cond", "none").rstrip(" |&")
   return f"part({selector}, high, {cur['order']}, {prop}) = {cur['ratio']}.\n"

def make_lines(params, selector, builder, master="counter", deactive="none"):
   def move(val=None):
      nonlocal n, key, cur
      n = val if val is not None else (n+1)
      key = f"{n}_{master}"
      cur = {x[2:]:y for (x,y) in params.items() if  x.startswith(str(n))}

   lines = ""
   params = {x[len(selector):]:y for (x,y) in params.items() if x.startswith(f"{selector}")}
   n = None
   key = None
   cur = None
   move(0)
   while key in params and params[key] != deactive:
      lines += builder(cur, selector+key[0])
      move()
   return lines

def make_actions(params):
   lines = ""
   lines += make_lines(params, "flg", make_action_flag, "counter", "none")
   lines += make_lines(params, "cng", make_action_change, "counter", "none")
   return f"\nlist(actions).\n{lines}end_of_list.\n" if lines.strip() else ""

def make_given(params):
   lines = ""
   lines += make_lines(params, "hgh", make_given_high, "ratio", "0")
   lines += make_lines(params, "low", make_given_low, "ratio", "0")
   return f"\nlist(given_selection).\n{lines}end_of_list.\n" if lines.strip() else ""

def make_strategy(params, defaults):
   for x in defaults:
      if x.startswith("a__") and x not in params:
         params[x] = defaults[x]
   params = {x[3:]:y for (x,y) in params.items() if x.startswith(f"a__")}
   return make_actions(params) + make_given(params)

class Prover9Runner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      penalty = self.config["penalty"]
      self.default("penalty.error", penalty*1000)
      self.default_domain(DefaultDomain)
      #self.conds = self.conditions(CONDITIONS)
      self.temp_file_to_delete = ''  # for the temp files

   # Create a temporary strategy file in memory
   # Explanation: Prover9 doesn' take strategies like Vampire directly, 
   # Prover9 needs an input file with strategies, so we create one. 
   def create_temp_strategy_file(self, params):
      with tempfile.NamedTemporaryFile(mode='w+', delete=False, prefix="prover9-strat-") as temp_file:
         for key in params:
            if key == "max_megs" or key.startswith("a__"): # advanced features
               continue
            value = params[key]
            if value in ["set", "clear"]:
               converted_parameter = f"{value}({key}).\n"
            else:
               converted_parameter = f"assign({key}, {value}).\n"
            temp_file.write(converted_parameter)
         advanced = make_strategy(params, self.domain.defaults)
         temp_file.write(advanced+"\n")
         temp_file.write("assign(max_megs, 2048).\nclear(print_given).\n")
      return temp_file.name
   

   def cmd(self, params, inst):
      params = self.clean(params)
      temp_strategy_file = self.create_temp_strategy_file(params)
      self.temp_file_to_delete = temp_strategy_file
      problem = path.join(getenv("PYPROVE_BENCHMARKS", "."), inst)
      vlimit = P_LIMIT % self.config["timeout"] if "timeout" in self.config else ""
      timeout = TIMEOUT % (self.config["timeout"]+1) if "timeout" in self.config else ""

      cmdargs = f"{timeout} {P_BINARY} {vlimit} {P_STATIC} {temp_strategy_file} {problem}"
      return cmdargs

   def process(self, out, inst):
      out = out.decode()
 
      if "THEOREM PROVED" in out:
        result = "THEOREM PROVED"
      else:
         if ("SEARCH FAILED" not in out) and ("Fatal error" in out):
            for ignored in IGNORED:
               if ignored in out:
                  return [self.config["penalty.error"], self.config["timeout"], "IGNORED", -1]
            return None # report error
         result = "SEARCH FAILED"  
      ok = self.success(result)

      # Search for the pattern in the output
      match_time = re.search(pattern_wall_clock, out)
      runtime = 0.0
      # If a match is found, extract the Wall_clock value
      if match_time:
         runtime = float(match_time.group(1))
      # set to default 0.001 if the Wall_clock is null       
      else:
         runtime = 0.0001

      quality = 10+int(1000*runtime) if ok else self.config["penalty"]   

      match_resources = re.search(pattern_kept, out)
      if match_resources:
         resources = int(match_resources.group(1))
      else:
         resources = 99999999

      if self.temp_file_to_delete:
         os.unlink(self.temp_file_to_delete)  # Deleting temp File

      return [quality, runtime, result, resources]
     

   def success(self, result):
      return result in P_OK

   def clean(self, params):
      params = {x:params[x] for x in params if params[x] != self.domain.defaults[x]}
      return params

