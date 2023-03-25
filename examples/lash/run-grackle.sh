#!/bin/sh

export PYPROVE_BENCHMARKS=$PWD/benchmarks
export TPTP=$PYPROVE_BENCHMARKS
export LASH_MODE_DIR=$PWD/modes

rm -fr training

cp db-trains-init.json db-trains-cache.json

fly-grackle.py grackle.fly.test 2>&1 | tee grackle.flee

