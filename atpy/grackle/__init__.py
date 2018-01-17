
def _load_class(cls):
   i = cls.rindex(".")
   pkg = cls[:i]
   cls = cls[i+1:]
   mod = __import__(pkg, fromlist=[cls])
   return getattr(mod, cls)

import log
import state
import main
import runner
import trainer

