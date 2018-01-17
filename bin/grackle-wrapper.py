#!/usr/bin/python

import sys
from atpy import grackle

RESULT="\nResult for ParamILS: %s, %s, %s, 1000000, %s"

def run():
   cls = sys.argv[1]
   runner = grackle._load_class(cls)(direct=True,cores=1)

   inst = sys.argv[2]
   limit = int(float(sys.argv[4]))
   seed = sys.argv[6]
   params = runner.params(sys.argv[7:])

   (quality,clock) = runner.run(params, inst, limit=limit)[:2]

   print RESULT % ("OK", clock, quality, seed)

if len(sys.argv) < 2:
   print "usage: %s runner_cls instance spec time cutoff seed arg1 val1 ..." % sys.argv[0]
else:
   run()

