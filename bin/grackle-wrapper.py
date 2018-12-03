#!/usr/bin/python

import sys
import json
import grackle

RESULT="\nResult for ParamILS: %s, %s, %s, 1000000, %s"

def run():
   cls = sys.argv[1]
   runner = grackle._load_class(cls)(direct=True,cores=1)

   if sys.argv[2] == "EXTRA":
      shift = 2
      extra = json.loads(sys.argv[3])
   else:
      shift = 0
      extra = None

   inst = sys.argv[2+shift]
   limit = int(float(sys.argv[4+shift]))
   seed = sys.argv[6+shift]
   params = runner.params(sys.argv[7+shift:])

   (quality,clock) = runner.run(params, inst, limit=limit, extra=extra)[:2]

   print RESULT % ("OK", clock, quality, seed)

if len(sys.argv) < 2:
   print "usage: %s runner_cls instance spec time cutoff seed arg1 val1 ..." % sys.argv[0]
else:
   run()

