#!/bin/bash
set -e #this stops the execution of a script if a command or pipeline has an error.

DATASET=$1

#1
mkdir -p output/$DATASET

#NAME_UN= "${DATASET}_output-unsupervised.csv"

#2
cp data_block/$DATASET/20/"${DATASET}_output-unsupervised.csv" output/$DATASET/
cp data_block/$DATASET/20/train.csv output/$DATASET/

