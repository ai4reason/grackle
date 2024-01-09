import re
import tempfile
import os 
from os import path, getenv
from .runner import GrackleRunner
from grackle.trainer.prover9.domain import DEFAULTS

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

class Prover9Runner(GrackleRunner):

   def __init__(self, config={}):
      GrackleRunner.__init__(self, config)
      self.default("penalty", 100000000)
      #self.conds = self.conditions(CONDITIONS)
      self.temp_file_to_delete = ''  # for the temp files

   def args(self, params):
         def one(arg, val):
            return f"-flag {arg} {val}"
         return " ".join([one(x,params[x]) for x in sorted(params)])
   
   # Create a temporary strategy file in memory
   # Explanation: Prover9 doesn' take strategies like Vampire directly, 
   # Prover9 needs an input file with strategies, so we create one. 
   def create_temp_strategy_file(self, params):
      with tempfile.NamedTemporaryFile(mode='w+', delete=False, prefix="prover9-strat-") as temp_file:
         for key in params:
            value = params[key]
            converted_parameter = f"assign({key}, {value}).\n"
            temp_file.write(converted_parameter)
      return temp_file.name
   

   def cmd(self, params, inst):
      #print("CMD")
      params = self.clean(params)
      #args = self.args(params)
      temp_strategy_file = self.create_temp_strategy_file(params)
      self.temp_file_to_delete = temp_strategy_file
      #print(f"Temporary strategy file path: {temp_strategy_file}") 
      #print("This temp file should be deleted later: ",self.temp_file_to_delete) 
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
      params = {x:params[x] for x in params if params[x] != DEFAULTS[x]}
      return params
