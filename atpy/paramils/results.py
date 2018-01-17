import os
from os import path

def get_paramils_result(outdir, numRun):
   fs = [f for f in os.listdir(outdir) if "traj_%d"%numRun in f and f.endswith(".txt")]
   f0 = fs[0]
   
   last = file(path.join(outdir,f0)).read().strip().split("\n")[-1]
   last = last.strip().split(",") 
   
   params = [p.split("=") for p in last[5:]]
   params = {p[0].strip():p[1].strip("' ") for p in params}

   return (int(last[2]), float(last[1]), params)

