from ..domain.customdomain import CustomDomain

FLAG="""
reuse_denials
""".strip().split("\n")
#breadth_first
#lightest_first

PARAM="""
max_given
max_weight
para_lit_limit
demod_step_limit
new_constants
max_depth
max_vars
max_literals
""".strip().split("\n")
#demod_increase_limit
#constant_weight
#variable_weight
#not_weight
#or_weight
#prop_atom_weight
#nest_penalty
#depth_penalty
#default_weight
#pick_given_ratio
#age_part
#weight_part
#false_part
#true_part

COUNTER="""
none
given
generated
kept
level
""".strip().split("\n")

ACTIVE=[x for x in COUNTER if x != "none"]

COND=[100,500,1000,2000,5000,10000]

VAL=[0,1,5,10,15,20,50,100,10000]

BIN=["set", "clear"]

class ActionsDomain(CustomDomain):
   
   def __init__(self, flags=1, vals=3, **kwargs):
      kwargs = dict(kwargs, flags=flags, vals=vals)
      self.n_flag = flags
      self.n_val = vals
      CustomDomain.__init__(self, **kwargs)
      self.init()

   def init(self):
      # flag changing actions:
      for n in range(self.n_flag):
         self.add_flag(f"a__flg{n}")
         for m in range(n):
            self.add_dep(f"a__flg{n}_counter", f"a__flg{m}_counter", ACTIVE)
      # value changing actions:
      for n in range(self.n_val):
         self.add_val(f"a__cng{n}")
         for m in range(n):
            self.add_dep(f"a__cng{n}_counter", f"a__cng{m}_counter", ACTIVE)

   def add_flag(self, name): 
      self.add_param(f"{name}_counter", COUNTER, "none")
      self.add_param(f"{name}_cond", COND)
      self.add_param(f"{name}_action", BIN)
      self.add_param(f"{name}_flag", FLAG)
      self.add_dep(f"{name}_cond", f"{name}_counter", ACTIVE)
      self.add_dep(f"{name}_action",f"{name}_counter", ACTIVE)
      self.add_dep(f"{name}_flag", f"{name}_counter", ACTIVE)

   def add_val(self, name):
      self.add_param(f"{name}_counter", COUNTER, "none"),
      self.add_param(f"{name}_cond", COND),
      self.add_param(f"{name}_action", PARAM),
      self.add_param(f"{name}_value", VAL),
      self.add_dep(f"{name}_cond", f"{name}_counter", ACTIVE),
      self.add_dep(f"{name}_action",f"{name}_counter", ACTIVE),
      self.add_dep(f"{name}_flag", f"{name}_counter", ACTIVE),
 
