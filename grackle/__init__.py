
def _load_class(cls):
   i = cls.rindex(".")
   pkg = cls[:i]
   cls = cls[i+1:]
   mod = __import__(pkg, fromlist=[cls])
   return getattr(mod, cls)

from . import log
from . import state
from . import main
from . import runner
from . import trainer

