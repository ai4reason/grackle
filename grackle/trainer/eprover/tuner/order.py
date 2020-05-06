from . import tuner
from grackle.runner.eprover import convert

PARAMS = """
   tord {Auto,LPO4,KBO6} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
"""

# prord {arity,invfreq,invfreqconstmin} [invfreqconstmin]
# tord {Auto,LPO4,KBO6} [LPO4]

CONDITIONS = """
   tord_prec   | tord in {LPO4,KBO6}
   tord_weight | tord in {KBO6}
   tord_const  | tord in {KBO6}
"""

def order():
   return PARAMS + CONDITIONS 



class OrderTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="1-order"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.OrderTuner")

   def split(self, params):
      params = convert(params)
      main = {x:params[x] for x in params if x.startswith("tord")}
      extra = {x:params[x] for x in params if not x.startswith("tord")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      return params

   def domains(self, config, init=None):
      return order()


