import os
import time

FATAL_LOG = os.path.join(os.getenv("HOME"),"grackle-errors.log")

def active(state, mastered):
   print "> ACTIVE CONFIGURATIONS: %d" % len(state.active)
   for conf in sorted(state.active):
      info = "\n".join(["%s%s"%(inst,state.evals.results[conf][inst]) for inst in sorted(mastered[conf])])
      print "> %s: masters %d evals" % (conf, len(mastered[conf]))
      print info
   print ">"

def training(state, bpis):
   print "> TRAINING PERFORMANCE:"
   #(results, bests) = db_trains
   for c in sorted(bpis):
      info = "\n".join(["%s%s"%(i,state.trains.results[c][i]) for i in sorted(bpis[c])])
      print "> %s: masters %d trains" % (c, len(bpis[c]))
      print info
   print ">"

def improving(state, conf, insts):
   print "> Improving %s on %d trains." % (conf, len(insts))

def iter(state):
   state.it += 1
   print ">"
   print "> === ITER %d ===" % state.it
   print ">"

def update(db, confs):
   print "> Evaluating %d configurations on %s." % (len(confs), db.name)

def status(state, db):
   runtime = (time.time() - state.start_time) / 60
   print "> STATUS @ %d (%s): %s, %.2f, %.4f" % ((runtime,)+db.status())

def candidates(candidates, avgs):
   print "TRAINING CANDIDATES:"
   for c in candidates:
      print "%s: %s" % (c, avgs[c])
   print

def finished(state):
   print "> Nothing more to do. Terminating."
   print ">"
   print "> FINAL CONFIGURATIONS: %d" % len(state.active)
   for conf in sorted(state.active):
      params = state.trains.runner.recall(conf)
      rep = state.trains.runner.repr(params)
      print "> %s: %s" % (conf, rep)

def timeout(state):
   print "> Timeout: Not enough time for training. Terminating after %s seconds." % (time.time() - state.start_time)

def timestamp(t_start, msg, prog="GRACKLE"):
   t_elapsed = int(time.time() - t_start)
   t_hour = t_elapsed / 3600
   t_min = (t_elapsed % 3600) / 60
   t_sec = t_elapsed % 60
   print "> [%02d:%02d:%02d] %s: %s" % (t_hour, t_min, t_sec, prog, msg)

def improved(state, conf):
   params = state.trains.runner.recall(conf)
   rep = state.trains.runner.repr(params)
   print "> INVENTED CONFIG: %s: %s" % (conf, rep)
   print ">"

def notnew(state, conf):
   print "> Invented config already known: %s" % conf
   print ">"

def init(state, f_init, conf):
   print "> Loaded initial config %s from %s" % (conf, f_init)

def inits(state):
   print ">"
   print "> INITIAL CONFIGURATIONS: %d" % len(state.alls)
   for conf in sorted(state.alls):
      params = state.trains.runner.recall(conf)
      rep = state.trains.runner.repr(params)
      print "> %s: %s" % (conf, rep)

def scenario(state, ini):
   print ">" 
   print "> === GRACKLE RUNNING ==="
   print ">"
   print "> Loaded parameters:"
   print "> cores = %s" % state.cores
   print "> best = %s" % state.best
   print "> tops = %s" % state.tops
   print "> rank = %s" % state.rank
   print "> timeout = %s" % state.timeout
   print "> trains = %s" % ini["trains"]
   if "evals" in ini:
      print "> evals = %s" % ini["evals"]
   else:
      print "> evals = &trains"
   print "> inits = %s" % ini["inits"]
   print "> runner = %s" % ini["runner"]
   print "> trainer = %s" % ini["trainer"]
   print ">"
   print "> Loaded %d evals" % len(state.evals.insts)
   print "> Loaded %d trains" % len(state.trains.insts)

def tuner(nick, i, n):
   print ">>"
   print ">> === TUNER[%d/%d]: %s ===" % (i,n,nick)

def msg(m):
   print m

def error(m):
   print m

def fatal(m):
   error(m)
   f = file(FATAL_LOG, "a")
   f.write(m)
   f.close()

