import json

SOLVED = ['Satisfiable', 'Unsatisfiable', 'Theorem', 'CounterSatisfiable', 'ContradictoryAxioms']

def transcript(fin):
   try:
      lines = [line.split() for line in open(fin).read().strip().split("\n")]
   except OSError:
      return None
   lines = {line[4]: line[-1] for line in lines}
   return lines

def load(f, f_trans=None):
   res = json.load(open(f))
   if f_trans:
      renames = transcript(f_trans)
      if renames:
         res = {(renames[s] if s in renames else s):res[s] for s in res}
   return res

def solved1(result):
   return set(p for p in result if p and result[p][2] in SOLVED)

def solved(results, apply=solved1):
   return {s:apply(results[s]) for s in results}

def counts(results):
   return solved(results, apply=lambda r: len(solved1(r)))

# printing
#
#

def perf(counts):
   data = [(counts[s], s) for s in sorted(counts, key=lambda x: counts[x])]
   print("\n".join("%s\t%s" % x for x in data))

def greedy(results):
   total = 0
   n = 0
   while results:
      best = max(results, key=lambda s: len(results[s]))
      eaten = frozenset(results[best])
      total += len(eaten)
      n += 1
      print("%s: %s" % (best, len(eaten)))
      for s in results:
         results[s].difference_update(eaten)
      results = {s:results[s] for s in results if results[s]}
   print("# TOTAL = %s (by %d)" % (total, n))
   
