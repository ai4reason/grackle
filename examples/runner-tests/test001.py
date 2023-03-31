#!/usr/bin/env python3

from grackle.runner.vampire import VampireRunner

rnr = VampireRunner({"direct":True, "cutoff":1})

instance = "agatha.p"
strategy = {"avatar": "off"}

print(rnr.cmd(strategy, instance))
print(rnr.run(strategy, instance))

