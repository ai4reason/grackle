from grackle.runner.eprover import EproverRunner 
from .... import log

class EproverTuner(EproverRunner):
   def __init__(self, config={}, nick="nick"):
      EproverRunner.__init__(self, config)
      self.default("nick", nick)
      self.config["cls"] = self.__class__.__module__ + "." + self.__class__.__name__

   def split(self, params):
      raise NotImplementedError("Abstract method not implemented.")

   def join(self, main, extra):
      raise NotImplementedError("Abstract method not implemented.")

   def domains(self, config, init=None):
      raise NotImplementedError("Abstract method not implemented.")

   def run(self, params, inst):
      joint = self.join(params, self.config["extra"]) if "extra" in self.config else params
      res = EproverRunner.run(self, joint, inst)
      if not res:
         log.fatal("ERROR(Grackle): Original params were: %s\n" % params)
      return res

