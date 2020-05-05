from . import tuner, base, order, glob
from grackle.runner.eprover import cef2block


ORDER_PARAMS = """
   tord {Auto,LPO4,KBO6,WPO} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max} [Sum]
"""

ONLY_PARAMS = """
   tord {WPO} [WPO]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max} [Sum]
"""

FAKE_ORDER_PARAMS = """
   tord {Auto,LPO4,KBO6,WPO} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max,SumVar0,SumVar1,SumVarN,SumVarZ,SumVar0First,SumVar1First,SumVarNFirst,SumVarZFirst,SumVar0Last,SumVar1Last,SumVarNLast,SumVarZLast,SumVar0Odds,SumVar1Odds,SumVarNOdds,SumVarZOdds,SumVar0Evens,SumVar1Evens,SumVarNEvens,SumVarZEvens,MaxVar0,MaxVar1,MaxVarN,MaxVarZ,MaxVar0First,MaxVar1First,MaxVarNFirst,MaxVarZFirst,MaxVar0Last,MaxVar1Last,MaxVarNLast,MaxVarZLast,MaxVar0Odds,MaxVar1Odds,MaxVarNOdds,MaxVarZOdds,MaxVar0Evens,MaxVar1Evens,MaxVarNEvens,MaxVarZEvens} [Sum]
"""

FAKE_ONLY_PARAMS = """
   tord {WPO} [WPO]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max,SumVar0,SumVar1,SumVarN,SumVarZ,SumVar0First,SumVar1First,SumVarNFirst,SumVarZFirst,SumVar0Last,SumVar1Last,SumVarNLast,SumVarZLast,SumVar0Odds,SumVar1Odds,SumVarNOdds,SumVarZOdds,SumVar0Evens,SumVar1Evens,SumVarNEvens,SumVarZEvens,MaxVar0,MaxVar1,MaxVarN,MaxVarZ,MaxVar0First,MaxVar1First,MaxVarNFirst,MaxVarZFirst,MaxVar0Last,MaxVar1Last,MaxVarNLast,MaxVarZLast,MaxVar0Odds,MaxVar1Odds,MaxVarNOdds,MaxVarZOdds,MaxVar0Evens,MaxVar1Evens,MaxVarNEvens,MaxVarZEvens} [Sum]
"""

ORDER_CONDITIONS = """
   tord_prec    | tord in {LPO4,KBO6,WPO}
   tord_weight  | tord in {KBO6,WPO}
   tord_const   | tord in {KBO6,WPO}
   tord_coefs   | tord in {WPO}
   tord_algebra | tord in {WPO}
"""

class WpoOrderTuner(order.OrderTuner):
   def __init__(self, direct, cores=4, nick="1-wpo-order"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.WpoOrderTuner")

   def domains(self, config, init=None):
      return ORDER_PARAMS + ORDER_CONDITIONS

class WpoFakeOrderTuner(order.OrderTuner):
   def __init__(self, direct, cores=4, nick="1-fakewpo-order"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.WpoFakeOrderTuner")

   def domains(self, config, init=None):
      return FAKE_ORDER_PARAMS + ORDER_CONDITIONS

class OnlyWpoTuner(glob.GlobalTuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.OnlyWpoTuner")

   def domains(self, config, init=None):
      cefs = domain.cefs_load(config["cefs_db"])
      cefs = map(cef2block, domain.cefs_domain(config["cefs_count"], cefs))
      if init:
         for x in init:
            if x.startswith("cef") and init[x] not in cefs:
               cefs.append(init[x])
      return base.PARAMS + ONLY_PARAMS + \
             base.params(config, cefs) + \
             base.CONDITIONS + \
             base.conditions(config) + \
             base.FORBIDDENS + base.forbiddens(config, cefs)

class OnlyWpoFakeTuner(glob.GlobalTuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.OnlyWpoFakeTuner")

   def domains(self, config, init=None):
      cefs0 = cefs.load(config["cefs_db"])
      cefs0 = map(cef2block, cefs.domain(config["cefs_count"], cefs0))
      if init:
         for x in init:
            if x.startswith("cef") and init[x] not in cefs0:
               cefs0.append(init[x])
      return base.PARAMS + FAKE_ONLY_PARAMS + \
             base.params(config, cefs) + \
             base.CONDITIONS + \
             base.conditions(config) + \
             base.FORBIDDENS + base.forbiddens(config, cefs)


