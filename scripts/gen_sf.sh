#!/bin/bash


CCTBX_ENV=$1
WORK_DIR=$2

source $CCTBX_ENV
cd $WORK_DIR

cctbx.python gen_sf.py $3 $4 $5 $6 $7 $8 $9 ${10} ${11}
