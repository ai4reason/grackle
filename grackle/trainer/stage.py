from .trainer import Trainer
from .. import log

class StageTrainer(Trainer):

   def __init__(self, runner, trainers, config={}):
      Trainer.__init__(self, runner, config)
      self.trainers = trainers

   def improve(self, state, conf, insts):
      for trainer in enumerate(self.trainers):
         log.tuner(trainer.config["nick"], i+1, len(self.trainers))
         conf = trainer.improve(state, conf, insts)
      return conf

