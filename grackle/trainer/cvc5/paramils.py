from ..paramils import ParamilsTrainer
from .domain import *

class Cvc5ParamilsTrainer(ParamilsTrainer):
   
   def domains(self, params):
      return (PARAMS % DEFAULTS) + CONDITIONS + FORBIDDENS 
   
