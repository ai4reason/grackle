from . import tuner, trainer, domain
from grackle.runner.eprover import cef2block

WPO_ORDER_PARAMS = """
   tord {Auto,LPO4,KBO6,WPO} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max} [Sum]
"""

WPO_ONLY_PARAMS = """
   tord {WPO} [WPO]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max} [Sum]
"""

WPO_FAKE_ORDER_PARAMS = """
   tord {Auto,LPO4,KBO6,WPO} [LPO4]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max,SumVar0,SumVar1,SumVarN,SumVarZ,SumVar0First,SumVar1First,SumVarNFirst,SumVarZFirst,SumVar0Last,SumVar1Last,SumVarNLast,SumVarZLast,SumVar0Odds,SumVar1Odds,SumVarNOdds,SumVarZOdds,SumVar0Evens,SumVar1Evens,SumVarNEvens,SumVarZEvens,MaxVar0,MaxVar1,MaxVarN,MaxVarZ,MaxVar0First,MaxVar1First,MaxVarNFirst,MaxVarZFirst,MaxVar0Last,MaxVar1Last,MaxVarNLast,MaxVarZLast,MaxVar0Odds,MaxVar1Odds,MaxVarNOdds,MaxVarZOdds,MaxVar0Evens,MaxVar1Evens,MaxVarNEvens,MaxVarZEvens} [Sum]
"""

WPO_FAKE_ONLY_PARAMS = """
   tord {WPO} [WPO]
   tord_prec {unary_first,unary_freq,arity,invarity,const_max,const_min,freq,invfreq,invconjfreq,invfreqconjmax,invfreqconjmin,invfreqconstmin} [arity]
   tord_weight {firstmaximal0,arity,aritymax0,modarity,modaritymax0,aritysquared,aritysquaredmax0,invarity,invaritymax0,invaritysquared,invaritysquaredmax0,precedence,invprecedence,precrank5,precrank10,precrank20,freqcount,invfreqcount,freqrank,invfreqrank,invconjfreqrank,freqranksquare,invfreqranksquare,invmodfreqrank,invmodfreqrankmax0,constant} [arity]
   tord_const {0,1} [0]
   tord_coefs {constant,arity,invarity,firstmax,firstmin,ascend,descend} [constant]
   tord_algebra {Sum,Max,SumVar0,SumVar1,SumVarN,SumVarZ,SumVar0First,SumVar1First,SumVarNFirst,SumVarZFirst,SumVar0Last,SumVar1Last,SumVarNLast,SumVarZLast,SumVar0Odds,SumVar1Odds,SumVarNOdds,SumVarZOdds,SumVar0Evens,SumVar1Evens,SumVarNEvens,SumVarZEvens,MaxVar0,MaxVar1,MaxVarN,MaxVarZ,MaxVar0First,MaxVar1First,MaxVarNFirst,MaxVarZFirst,MaxVar0Last,MaxVar1Last,MaxVarNLast,MaxVarZLast,MaxVar0Odds,MaxVar1Odds,MaxVarNOdds,MaxVarZOdds,MaxVar0Evens,MaxVar1Evens,MaxVarNEvens,MaxVarZEvens} [Sum]
"""

WPO_ORDER_CONDITIONS = """
   tord_prec    | tord in {LPO4,KBO6,WPO}
   tord_weight  | tord in {KBO6,WPO}
   tord_const   | tord in {KBO6,WPO}
   tord_coefs   | tord in {WPO}
   tord_algebra | tord in {WPO}
"""

class WpoOrderTuner(tuner.OrderTuner):
   def __init__(self, direct, cores=4, nick="1-wpo-order"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.wpo.WpoOrderTuner")

   def domains(self, config, init=None):
      return WPO_ORDER_PARAMS + WPO_ORDER_CONDITIONS

class WpoFakeOrderTuner(tuner.OrderTuner):
   def __init__(self, direct, cores=4, nick="1-fakewpo-order"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.wpo.WpoFakeOrderTuner")

   def domains(self, config, init=None):
      return WPO_FAKE_ORDER_PARAMS + WPO_ORDER_CONDITIONS

class OnlyWpoTuner(tuner.GlobalTuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.wpo.OnlyWpoTuner")

   def domains(self, config, init=None):
      cefs = domain.cefs_load(config["cefs_db"])
      cefs = map(cef2block, domain.cefs_domain(config["cefs_count"], cefs))
      if init:
         for x in init:
            if x.startswith("cef") and init[x] not in cefs:
               cefs.append(init[x])
      return domain.BASE_PARAMS + WPO_ONLY_PARAMS + \
             domain.base_params(config, cefs) + \
             domain.BASE_CONDITIONS + \
             domain.base_conditions(config) + \
             domain.BASE_FORBIDDENS + domain.base_forbiddens(config, cefs)

class OnlyWpoFakeTuner(tuner.GlobalTuner):
   def __init__(self, direct, cores=4, nick="0-global"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.wpo.OnlyWpoFakeTuner")

   def domains(self, config, init=None):
      cefs = domain.cefs_load(config["cefs_db"])
      cefs = map(cef2block, domain.cefs_domain(config["cefs_count"], cefs))
      if init:
         for x in init:
            if x.startswith("cef") and init[x] not in cefs:
               cefs.append(init[x])
      return domain.BASE_PARAMS + WPO_FAKE_ONLY_PARAMS + \
             domain.base_params(config, cefs) + \
             domain.BASE_CONDITIONS + \
             domain.base_conditions(config) + \
             domain.BASE_FORBIDDENS + domain.base_forbiddens(config, cefs)

WPO_ORDER = lambda nick: WpoOrderTuner(True, 1, nick)
WPO_FAKE_ORDER = lambda nick: WpoFakeOrderTuner(True, 1, nick)
WPO_ONLY = lambda nick: OnlyWpoTuner(True, 1, nick)
WPO_FAKE_ONLY = lambda nick: OnlyWpoFakeTuner(True, 1, nick)

class WpoTrainer(trainer.StageTrainer):
   def __init__(self, runner, cls):
      trainer.StageTrainer.__init__(self, runner, cls, [
         tuner.BASE("00-base"),
         WPO_ORDER("01-order"),
         tuner.FINE("02-fine")])

class WpoFakeTrainer(trainer.StageTrainer):
   def __init__(self, runner, cls):
      trainer.StageTrainer.__init__(self, runner, cls, [
         tuner.BASE("00-base"),
         WPO_FAKE_ORDER("01-order"),
         tuner.FINE("02-fine")])

class WpoOnlyTrainer(trainer.StageTrainer):
   def __init__(self, runner, cls):
      trainer.StageTrainer.__init__(self, runner, cls, [
         WPO_ONLY("01-wpo-global")])

class WpoFakeOnlyTrainer(trainer.StageTrainer):
   def __init__(self, runner, cls):
      trainer.StageTrainer.__init__(self, runner, cls, [
         WPO_FAKE_ONLY("01-wpo-global")])

