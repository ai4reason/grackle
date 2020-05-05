from grackle.runner.eprover import convert, SINE_DEFAULTS
from . import tuner

PARAMS = """
   sineG {CountFormulas,CountTerms} [CountFormulas]
   sineh {none,hypos} [hypos]
   sinegf {1.1,1.2,1.4,1.5,2.0,5.0,6.0} [1.2]
   sineD {none,1,3,10,20,40,160} [none]
   sineR {none,01,02,03,04} [none]
   sineL {10,20,40,60,80,100,500,20000} [100]
   sineF {1.0,0.8,0.6} [1.0]
"""

#   sineL {10,20,40,60,80,100,500,20000} [100]
#   sineR {UU,01,02,03,04} [UU]
#   sinegf {1.1,1.2,1.4,1.5,2.0,5.0,6.0} [1.2]
#   sineh  {hypos,none} [hypos]
#   sine {0,1} [0]
#   sineL  | sine in {1}
#   sineR  | sine in {1}
#   sinegf | sine in {1}
#   sineh  | sine in {1}
#"""

def sine():
   return PARAMS



class SineTuner(tuner.Tuner):
   def __init__(self, direct, cores=4, nick="0-sine"):
      tuner.Tuner.__init__(self, direct, cores, nick, 
         "grackle.trainer.eprover.tuner.SineTuner")

   def split(self, params):
      params = convert(params)
      main = dict(SINE_DEFAULTS)
      main.update({x:params[x] for x in params if x.startswith("sine")})
      del main["sine"]
      extra = {x:params[x] for x in params if not x.startswith("sine")}
      return (main, extra)

   def join(self, main, extra):
      params = dict(main)
      params.update(extra)
      params["sine"] = "1"
      return params

   def domains(self, config, init=None):
      return sine()


