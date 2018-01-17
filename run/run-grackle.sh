#!/bin/sh

GRACKLE=`dirname $PWD`

export PATH=$GRACKLE/bin:$PATH
export PYTHONPATH=$GRACKLE
export PREMISE_INSTANCE_DIR=$GRACKLE/premise/data

grackle.py grackle.fly | tee grackle.log

