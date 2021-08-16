import numpy
from scipy import spatial
from . import log

def init(state):
   f_in = state.unsolved["features"]
   insts = frozenset(state.trains.insts)
   
   features = {}
   maxs = None
   length = None
   found = set()
   for line in open(f_in):
      parts = line.strip().split("\t")
      name = parts[0]
      if name not in insts:
         continue
      vector = list(map(float, parts[1:]))
      if not length:
         length = len(vector)
      else:
         if length != len(vector):
            raise Exception("Different feature vector lengths.")
      if not maxs:
         maxs = list(vector)
      else:
         maxs = [max(maxs[i], vector[i]) for i in range(len(vector))]
      found.add(name)
      features[name] = numpy.array(vector)

   missing = insts - found
   if missing:
      log.missing(missing)
      raise Exception("Missing features for some training instances.")

   maxs = numpy.array(maxs)
   state.features = {i:scale(features[i],maxs) for i in features}
   state.scale = maxs
   state.kdtree = None
   state.kdindices = None

def scale(data, maxs):
   return 1000 * (data / maxs)

def update(state, conf):
   mode = state.unsolved["mode"]
   if mode == "inits" and state.kdtree:
      return
   if mode in ["inits", "all"]:
      confs = state.alls
   elif mode == "actives":
      confs = state.active
   else: # mode == "current"
      confs = [conf]
   db = state.trains
   confs = [c for c in confs if c in db.results]
   solved = lambda c, i: db.runner.success(db.results[c][i][2])
   oks = [i for c in confs for i in db.results[c] if solved(c,i)]
   uns = sorted(frozenset(db.insts) - frozenset(oks))
   data = numpy.array([state.features[i] for i in uns])
   log.kdtree(data)
   state.kdtree = spatial.KDTree(data)
   state.kdindices = dict(enumerate(uns))

def select(state, conf, insts):
   update(state, conf)
   insts = sorted(insts)
   query = numpy.array([state.features[i] for i in insts])
   (_, idxs) = state.kdtree.query(query)
   uniq = [idx for idx in set(idxs) if state.kdindices[idx] not in insts]
   count = int(len(insts) * state.unsolved["ratio"])
   if len(uniq) > count:
      uniq = uniq[:count]
   log.kdselect(state, conf, idxs, uniq, insts)
   return [state.kdindices[idx] for idx in uniq]

