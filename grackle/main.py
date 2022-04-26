#!/usr/bin/python

import json
from os import path

from . import log, unsolved

def evaluate(state, db, confs):
   log.timestamp(state.start_time, "Evaluation started")
   log.update(db, confs)
   db.update(confs)
   log.timestamp(state.start_time, "Evaluation done")
   if state.it == 1:
      db.save("init")

   state.evals.save("cache")
   state.trains.save("cache")
   log.status(state, db)

def reduction(state):
   mastered = {c:state.evals.mastered(c) for c in state.genofond()}
   enough = [c for c in state.genofond() if len(mastered[c])>=state.best]
   active = sorted(enough, key=lambda x: len(mastered[x]), reverse=True)
   state.active = active[:state.tops]
   log.active(state, mastered)

def select(state):
   bps = {c:state.trains.mastered(c) for c in state.active}
   log.training(state, bps)
   bps = {c:bps[c] for c in bps if not state.improved(c, bps[c])}
   avgs = {c:[state.attention[i] for i in bps[c]] for c in bps}
   avgs = {c:avgs[c] for c in avgs if len(avgs[c])>=1}
   avgs = {c:sum(avgs[c])/len(avgs[c]) for c in avgs}
   avgs = {c:(avgs[c],-len(bps[c])) for c in avgs}

   if state.selection == "strong":
      candidates = sorted(avgs, key=lambda c:avgs[c])
   elif state.selection == "weak":
      candidates = sorted(avgs, key=lambda c:avgs[c], reverse=True)
   else:
      raise Exception("Unsupported selection strategy: %s" % state.selection)
   log.candidates(candidates, avgs)
   return candidates

def specialize(state, conf):
   log.timestamp(state.start_time, "Specialization started")
   insts = state.trains.mastered(conf)
   uns = unsolved.select(state, conf, insts) 
   insts.extend(uns)
   if state.timeouted(state.trainer.trainlimit(len(insts))):
      return False

   log.improving(state, conf, insts)
   new = state.trainer.improve(state, conf, insts)
   state.did(conf, insts)
   log.timestamp(state.start_time, "Specialization done")
   return new

def improve(state, candidates):
   for conf in candidates:
      new = specialize(state, conf)
      if new is False:
         log.timeout(state)
         return False
      if new not in state.alls:
         log.improved(state, new)
         state.newborn(new)
         return True
      else:
         log.notnew(state, new)

   log.finished(state)
   state.evals.save("final")
   state.trains.save("final")
   return False

def loop(state):
   while True:
      log.iter(state)
      evaluate(state, state.evals, state.genofond())
      reduction(state)
      evaluate(state, state.trains, state.active)
      candidates = select(state)
      if not improve(state, candidates):
         return state

