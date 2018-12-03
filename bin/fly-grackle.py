#!/usr/bin/python

import sys
import grackle

if len(sys.argv) != 2:
   print "usage: %s grackle.fly" % sys.argv[0]

init = grackle.state.State(sys.argv[1])
grackle.main.loop(init)

