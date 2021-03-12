#!/bin/sh

export SMTLIB_BENCHMARKS=/home/cbboyan/repos/cbboyan/data/smtlib
fly-grackle.py grackle.fly 2>&1 | tee grackle.flee

