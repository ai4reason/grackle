#import grackle

import grackle
from grackle.runner.eprover import EproverRunner

rnr = EproverRunner({"direct":True,"cutoff":1})

params = ["inits/tptp%02d"%n for n in range(10)]
params = [file(f).read().strip().split() for f in params]
params = map(rnr.parse, params)

#print rnr.repr(params[0]).replace(" ","\n")

inst = "test/tptp/agatha.p"

for p in params:
   print rnr.run(p, inst)

print rnr.cmd(params[0], inst)

