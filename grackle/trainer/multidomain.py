from .domain import GrackleDomain

class MultiDomain(GrackleDomain):
   
   def __init__(self, domains):
      self.reset()
      for domain in domains:
         self.add(domain)
   
   def __repr__(self):
      args = [repr(dom) for dom in self._domains]
      return f"{type(self).__name__}([{','.join(args)}])"

   def reset(self):
      self._params = {}
      self._defaults = {}
      self._conditions = []
      self._forbiddens = []
      self._domains = []

   def add(self, domain):
      self._params.update(domain.params)
      self._defaults.update(domain.defaults)
      self._conditions.extend(domain.conditions)
      self._forbiddens.extend(domain.forbiddens)
      self._domains.append(domain)

   @property
   def params(self):
      return self._params

   @property
   def defaults(self):
      return self._defaults

   @property 
   def conditions(self):
      return self._conditions

   @property
   def forbiddens(self):
      return self._forbiddens

