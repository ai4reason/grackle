
class Trainer:
   
   def __init__(self, runner, config={}):
      self.runner = runner
      self.config = dict(config)
      if "instance_budget" not in self.config:
         self.config["instance_budget"] = None

   def improve(self, state, conf, insts):
      pass

