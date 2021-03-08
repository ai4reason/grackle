#import grackle

from grackle.runner.cvc4 import Cvc4Runner

rnr = Cvc4Runner({"direct":True, "cutoff":100000, "timeout": 1})

params = open("inits/cvc01").read().strip().split(" ")
params = rnr.parse(params)
inst = "UFNIA/2019-Preiner/combined/t3_rw413.smt2"

for inst in open("ufnia-devel").read().strip().split("\n"):
   #print(inst, rnr.cmd(params, inst))
   print(inst, rnr.run(params, inst))


#params = ["inits/tptp%02d"%n for n in range(10)]
#params = [file(f).read().strip().split() for f in params]
#params = map(rnr.parse, params)
#
##print rnr.repr(params[0]).replace(" ","\n")
#
#inst = "test/tptp/agatha.p"
#
#for p in params:
#   print rnr.run(p, inst)
#
#print rnr.cmd(params[0], inst)

