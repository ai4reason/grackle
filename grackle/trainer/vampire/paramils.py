from ..paramils import ParamilsTrainer
from .domain import PARAMS, DEFAULTS, CONDITIONS, FORBIDDENS

class VampireParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (PARAMS % DEFAULTS) + CONDITIONS + FORBIDDENS 
   
