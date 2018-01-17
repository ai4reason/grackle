
def active(state, mastered):
   print "> ACTIVE CONFIGURATIONS: %d" % len(state.active)
   for conf in sorted(state.active):
      info = "\n".join(["%s%s"%(inst,state.evals.results[conf][inst]) for inst in sorted(mastered[conf])])
      print "> %s: masters %d evals" % (conf, len(mastered[conf]))
      print info
   print

def training(state, bpis):
   print "> TRAINING PERFORMANCE:"
   #(results, bests) = db_trains
   for c in sorted(bpis):
      info = "\n".join(["%s%s"%(i,state.trains.results[c][i]) for i in sorted(bpis[c])])
      print "> %s: masters %d trains" % (c, len(bpis[c]))
      print info
   print

def improving(state, conf, insts):
   print "> Improving %s on %d instances." % (conf, len(insts))

def iter(state):
   state.it += 1
   print
   print "=== ITER %d ===" % state.it
   print

def update(db, confs):
   print "> Evaluating %d configurations on %s." % (len(confs), db.name)

def candidates(candidates, avgs):
   print "TRAINING CANDIDATES:"
   for c in candidates:
      print "%s: %s" % (c, avgs[c])
   print

def finished(state):
   print "> No new strategy. Terminating."

def improved(state, conf):
   params = state.trains.runner.recall(conf)
   rep = state.trains.runner.repr(params)
   print "> IMPROVED CONFIG: %s: %s" % (conf, rep)

def init(state, f_init, conf):
   params = state.trains.runner.recall(conf)
   rep = state.trains.runner.repr(params)
   print "> Loaded initial config: %s (%s)" % (f_init, conf)
   print "INIT CONFIG: %s: %s" % (conf, rep)

def scenario(ini):
   print 
   print "=== GRACKLE RUNNING ==="
   print
   print "> Loading initialization:"
   print "\n".join(["%s = %s" % (x,ini[x]) for x in ini])
   print

def instances(state):
   print "> Loaded %d evals" % len(state.evals.insts)
   print "> Loaded %d trains" % len(state.trains.insts)

def msg(m):
   print m

def error(m):
   print m

