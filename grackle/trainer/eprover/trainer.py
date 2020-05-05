from .stage import StageTrainer
from . import tuner



class BaseTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.BASE("00-base")])

class GlobalTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.GLOBAL("00-global")])

class BaseFineTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         #tuner.SINE("00-sine"), 
         #tuner.GLOBAL("01-global"),
         tuner.BASE("00-base"),
         tuner.ORDER("01-order"),
         tuner.FINE("02-fine")])

class GlobalSineFineTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.GLOBAL("00-global"),
         tuner.SINE("01-sine"), 
         tuner.FINE("02-fine")])

class GlobalFineTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.GLOBAL("00-global"),
         tuner.FINE("01-fine")])



      
class WpoTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.BASE("00-base"),
         tuner.WPO_ORDER("01-order"),
         tuner.FINE("02-fine")])

class WpoFakeTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.BASE("00-base"),
         tuner.WPO_FAKE_ORDER("01-order"),
         tuner.FINE("02-fine")])

class WpoOnlyTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.WPO_ONLY("01-wpo-global")])

class WpoFakeOnlyTrainer(StageTrainer):
   def __init__(self, runner, cls):
      StageTrainer.__init__(self, runner, cls, [
         tuner.WPO_FAKE_ONLY("01-wpo-global")])

