from grackle.runner.eprover import EproverRunner

class TARunner:

   def __init__(self, config):
      self.runner = EproverRunner(config)

   def run(self, config, seed, instance):
      result = self.runner.run(config, instance)
      return (result[0], result[1:]) if result else None

