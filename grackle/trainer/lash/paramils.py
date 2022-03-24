from ..paramils import ParamilsTrainer
from . import domain

class LashParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (domain.PARAMS % domain.DEFAULTS) + domain.CONDITIONS + domain.FORBIDDENS 
   
