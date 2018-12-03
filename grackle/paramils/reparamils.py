import sys
import os
from os import path
import subprocess
import time

from .results import get_paramils_result

def run_reparamils(scenariofile, outdir, cwd, binary="param_ils_2_3_run.rb", count=1, N=10, validN="800", init="1", out=None, time_limit=None):
   def run(numRun, currentInit):
      arg = [binary, "-numRun", str(numRun), "-scenariofile", scenariofile, "-N", str(N), "-validN", validN, "-output_level", "0", "-userunlog", "0", "-init", currentInit]
      return subprocess.Popen(arg,stdout=out,close_fds=True,cwd=cwd)

   if not out:
      out = open(os.devnull, 'w')
     
   running = {numRun:run(numRun,init) for numRun in range(count)}
   fresh = count
   elder = (None,None,None)
   it = 1
   log = ""
   print ">> --- TRAIN ITER %d ---" % it
   start = time.time()
   if time_limit:
      end = time.time() + time_limit
   else:
      end = float("inf")
   iter_start = time.time()
   adult = False
   while running:
      time.sleep(2)
      sys.stdout.flush()

      log0 = log
      log = ""
      for numRun in running:
         (n,q,params) = get_paramils_result(outdir, numRun)
         log += "%2s:%3s (%8.1f)\t" % (numRun,n,q) 
         #print numRun, n, q
         if not adult and numRun is not elder[0] and n == N:
            adult = True
            stable_len = max(20, time.time() - iter_start)
            stable_time = time.time() + stable_len
            print "%6s> %s" % (int(time.time()-start),log)
            print ">> first young (%d) reached N (=%d); entering stabilization phase (%s seconds)" % (numRun, N, stable_len)
            sys.stdout.flush()
      if log != log0:
         print "%6s> %s" % (int(time.time()-start),log)
         sys.stdout.flush()
     
      if not adult or time.time() < stable_time:
         if time.time() < end:
            continue
         else:
            print ">> time limit reached. terminating."
            sys.stdout.flush()

      winner = None
      bestq = None
      for numRun in running:
         (n,q,params) = get_paramils_result(outdir, numRun)
         if n == N:
            if (not winner) or q < winner[1]:
               winner = (numRun,q,params)
         if (not bestq) or q < bestq[1]:
               bestq = (numRun,q,params)
      if not winner: # when timeout-ing
         if elder[0] is not None: 
            winner = elder
         else:
            winner = bestq

      print ">> winner: %s with Q = %s" % (winner[0],  winner[1])
      sys.stdout.flush()

      if time.time() > end:
         elder = winner
         break

      if elder[0] is not None and int(1000*winner[1]) >= int(1000*elder[1]):
         print ">> no improvement. terminating."
         sys.stdout.flush()
         elder = winner
         break

      kills = running.keys()
      kills.remove(winner[0])
      #print "> terminating: ", kills
      for kill in kills:
         running[kill].terminate()

      time.sleep(1)
      for kill in kills:
         if not running[kill].poll():
            print ">> killing: ", kill
            try:
               running[kill].kill()
            except:
               pass
      
      keep = running[winner[0]]
      params = winner[2]
      init0 = " ".join(["%s %s"%(x,params[x]) for x in sorted(params)])
      f_init = "init_%02d"%it
      file(path.join(cwd,f_init),"w").write(init0)
      running = {numRun:run(numRun,f_init) for numRun in range(fresh,fresh+count-1)}
      running[winner[0]] = keep

      fresh += (count-1)
      elder = winner
      it += 1
      print ">> --- TRAIN ITER %d ---" % it
      sys.stdout.flush()
      iter_start = time.time()
      adult = False

   #print "> terminating: ", running.keys()
   for kill in running:
      running[kill].terminate()
   time.sleep(1)
   for kill in running:
      if not running[kill].poll():
         print ">> killing: ", kill
         try:
            running[kill].kill()
         except:
            pass

   #print "RES: ", elder[2]
   return elder[2]

