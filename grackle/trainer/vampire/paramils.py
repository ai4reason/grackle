from ..paramils import ParamilsTrainer
from . import domain, domain_full

class VampireParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain.PARAMS % domain.DEFAULTS) + domain.CONDITIONS + domain.FORBIDDENS 
   
class VampireParamilsFullTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain_full.PARAMS % domain_full.DEFAULTS) + domain_full.CONDITIONS + domain_full.FORBIDDENS 

