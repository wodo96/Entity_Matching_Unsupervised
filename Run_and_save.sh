#!/bin/bash
set -e #this stops the execution of a script if a command or pipeline has an error.

DATASET=$1

#1
mkdir -p output

#2
sh ./Run.sh $DATASET 2>&1 | tee ./output/$DATASET.txt