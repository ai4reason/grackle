from ..paramils import ParamilsTrainer
from . import domain, domain_full, domain_casc

class VampireParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain.PARAMS % domain.DEFAULTS) + domain.CONDITIONS + domain.FORBIDDENS 
   
class VampireParamilsFullTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain_full.PARAMS % domain_full.DEFAULTS) + domain_full.CONDITIONS + domain_full.FORBIDDENS 

class VampireParamilsCascTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain_casc.PARAMS % domain_casc.DEFAULTS) + domain_casc.CONDITIONS + domain_casc.FORBIDDENS 
