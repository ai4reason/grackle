#!/bin/bash

export PYPROVE_BENCHMARKS=$PWD/benchmarks

rm -fr training

cp db-trains-init.json db-trains-cache.json

fly-grackle.py grackle.fly 2>&1 | tee grackle.flee

