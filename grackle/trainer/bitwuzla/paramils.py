from ..paramils import ParamilsTrainer
from . import domain

class BitwuzlaParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain.PARAMS % domain.DEFAULTS) + domain.CONDITIONS + domain.FORBIDDENS 
   
