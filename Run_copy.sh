#!/bin/bash
set -e #this stops the execution of a script if a command or pipeline has an error.

if [ $# -lt 1 ]; then
    echo "  "
    echo "USAGE $0 <Dataset> <block>"
    echo "  "
    echo "INFO Argument <block> is facoltative. default:20"
    echo "  "
    echo "INFO e.g.: < ./Run.sh Abt-Buy 20 > or < ./Run.sh Abt-Buy >"
    echo "  "
    exit 1
fi

DATASET=$1
BLOCK=${2:-20}
DATASET_DIR=$PWD/data/$DATASET
DATA_BLOCK_DIR=$PWD/data_block/$DATASET/$BLOCK
FILES_DIR=$PWD/src/training


#1
cd $FILES_DIR
python3 $FILES_DIR/opencsv.py -dataset $DATASET

#1.a
cd ../..
mkdir -p $PWD/data_block/$DATASET
mkdir -p $PWD/data_block/$DATASET/$BLOCK

#1.b
cd $FILES_DIR
python3 $FILES_DIR/create_match.py -dataset $DATASET -block $BLOCK

#2
python3 $FILES_DIR/blocking.py -dataset $DATASET -block $BLOCK

#3
python3 $FILES_DIR/main.py -dataset $DATASET -block $BLOCK

#4
python3 $FILES_DIR/training.py -dataset $DATASET -block $BLOCK

#5
python3 $FILES_DIR/transformation.py -dataset $DATASET -block $BLOCK

#6
python3 $FILES_DIR/remove_touple_from_train.py -dataset $DATASET -block $BLOCK

#7
python3 $FILES_DIR/add_0_train.py -dataset $DATASET -block $BLOCK

echo "  "
echo "All completed!! :)"
echo "  "