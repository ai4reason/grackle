import json

SOLVED = ['Satisfiable', 'Unsatisfiable', 'Theorem', 'CounterSatisfiable', 'ContradictoryAxioms']

def transcript(fin):
   try:
      lines = [line.split() for line in open(fin).read().strip().split("\n")]
   except OSError:
      return None
   lines = {line[4]: line[-1] for line in lines}
   return lines

def load(f, f_trans=None, filter_mode=None): 
   # `filter_mode` is `None`, `True`, or `False`.
   res = json.load(open(f))
   if f_trans:
      renames = transcript(f_trans)
      if renames:
         if filter_mode is not None:
            res = {s:res[s] for s in res if (s in renames) is filter_mode}
         res = {(renames[s] if s in renames else s):res[s] for s in res}
   return res

def update(todb, fromdb):
   news = fromdb.keys() - todb.keys()
   #both = fromdb.keys() & todb.keys()
   for s in news:
      todb[s] = fromdb[s] 

def join(dbs):
   joint = {}
   for db in dbs:
      update(joint, load(db))
   return joint

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

def greedy(results, max_n=None):
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
      if max_n and n >= max_n:
         break
   print("# TOTAL = %s (by %d)" % (total, n))
   
