import json
from itertools import cycle

from grackle.runner.eprover import cef2block


def load(f_cefs):
   return json.load(open(f_cefs))

def save(f_cefs, cefs):
   json.dump(cefs, open(f_cefs,"w"), indent=3, sort_keys=True)

def weight(cef):
   return cef.split("(")[0]

def usage(weight, cefs):
   weight_cefs = [cef for cef in cefs if cef.startswith(weight+"(")]
   usage0 = sum([cefs[cef] for cef in weight_cefs])
   bests = sorted([(cefs[cef],cef) for cef in weight_cefs],reverse=True)
   return (usage0, bests)

def domain(count, cefs):
   ret = []
   weights = set(map(weight,cefs))
   w_bests = sorted([usage(w,cefs) for w in weights],reverse=True)
   count = min(len(cefs), count)

   for (usage0 ,bests) in cycle(w_bests):
      if len(ret) >= count:
         return ret[:count]
      if bests:
         cef = bests.pop(0)[1]
         ret.append(cef)







