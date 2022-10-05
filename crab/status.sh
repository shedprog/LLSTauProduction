#!/bin/bash

REG_EXP=$1
CMD=$2
CMSSWSRC=$3
CWD=`pwd`

cd $CMSSWSRC
cmsenv

cd $CWD

#DIRS=(`readlink -f ./*/*/*${REG_EXP}*`)
DIRS=(`readlink -f *${REG_EXP}*`)
for PATH_GLOB in ${DIRS[@]}; do
    echo $PATH_GLOB
    crab ${CMD} -d ${PATH_GLOB}
done
