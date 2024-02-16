
def dotjoin(lst):
   if isinstance(lst, str):
      lst = lst.strip()
      if lst.startswith("{") and lst.endswith("}"):
         return lst
      return "{%s}" % lst 
   return "{%s}" % ",".join(str(x) for x in lst)

class GrackleDomain:
   
   def __init__(self, **kwargs):
      self._kwargs = dict(kwargs)
   
   def __repr__(self):
      args = [f"{x}={y}" for (x,y) in self._kwargs.items()]
      return f"{type(self).__name__}({','.join(args)})"
   
   @property
   def params(self):
      return {}

   @property
   def defaults(self):
      return {}

   @property 
   def conditions(self):
      return []

   @property
   def forbiddens(self):
      return []

   def dump_param(self, key, defaults=None):
      def default(key):
         return defaults[key] if (defaults and (key in defaults)) else self.defaults[key]
      dom = dotjoin(self.params[key])
      return f"{key} {dom} [{default(key)}]"

   def dump_condition(self, cond):
     if not isinstance(cond, str):
        (slave, master, values) = cond
        values = dotjoin(values)
        cond = f"{slave} | {master} in {values}"
     return cond

   def dump_forbidden(self, forbidden):
     return dotjoin(forbidden)

   def dump(self, defaults=None):
      lines = []
      # parameter domain (","-separated string or list of values)
      for key in sorted(self.params):
         lines.append(self.dump_param(key, defaults=defaults))
      lines.append("")
      # conditions (either string or 3-tuples)
      for cond in self.conditions:
         if not cond:
            continue
         lines.append(self.dump_condition(cond))
      lines.append("")
      # forbiddens (strings or string-lists)
      for f in self.forbiddens:
         lines.append(self.dump_forbidden(f))
      return "\n".join(lines)

