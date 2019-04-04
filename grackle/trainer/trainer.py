
class Trainer:
   
   def __init__(self, runner, config={}):
      self.runner = runner
      self.config = dict(config)

   def improve(self, state, conf, insts):
      pass

