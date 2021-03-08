#!/bin/bash

LIMIT=1
#PROBLEM="UFNIA/2019-Preiner/qf/t3_rw730.smt2"
PROBLEM="UFNIA/vcc-havoc/vccp-union1.c.8.reint4.smt2"
DIR="$HOME/atp/benchmarks/smtlib"
STRAT=`echo $CONF | tr "_" " "`

ulimit -S -t "$LIMIT" 
cvc4 -L smt2.6 --no-incremental --no-type-checking --no-interactive --stats --rlimit 33000 $@ $DIR/$PROBLEM 2>&1 | grep -i resourceUnitsUsed

