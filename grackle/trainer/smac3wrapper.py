
class Wrapper:

   def __init__(self, runner):
      self.runner = runner

   def run(self, config, seed, instance):
      result = self.runner.run(config, instance)
      #print("TAE", instance, result)
      return (result[0], result[1:]) 

