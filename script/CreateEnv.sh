#!/bin/bash

# ENV_PATH=/afs/cern.ch/user/m/myshched/STauGENProduction

ABS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR=${ABS_PATH}/..

ENV_PATH=${ABS_PATH}/../envs
mkdir -p ${ENV_PATH}

echo "ENV_PATH: " $ENV_PATH
echo "OUTDIR: " $OUTDIR

echo "Creating environment for RAWSIM"
cd $ENV_PATH
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r ${ENV_PATH}/CMSSW_10_2_16_patch2/src ] ; then
  echo release CMSSW_10_2_16_patch2 already exists
else
  cd ${ENV_PATH}
  scram p CMSSW CMSSW_10_2_16_patch2
fi

# Copy test particle files
mkdir -p ${ENV_PATH}/CMSSW_10_2_16_patch2/src/data
cp ${OUTDIR}/Configuration/ParticleFiles/*.txt ${ENV_PATH}/CMSSW_10_2_16_patch2/src/data

cd ${ENV_PATH}/CMSSW_10_2_16_patch2/src
mkdir -p ${ENV_PATH}/CMSSW_10_2_16_patch2/src/Configuration/GenProduction/python
cp -f ${OUTDIR}/Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py ${ENV_PATH}/CMSSW_10_2_16_patch2/src/Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py
[ -s ${ENV_PATH}/CMSSW_10_2_16_patch2/src/Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py ] || exit $?;
eval `scram runtime -sh`
scram b

# echo "Creating environment for PREMIXRAW, AODSIM, MINIAODSIM"
# cd $ENV_PATH
# export SCRAM_ARCH=slc6_amd64_gcc700
# source /cvmfs/cms.cern.ch/cmsset_default.sh
# if [ -r ${ENV_PATH}/CMSSW_10_2_5/src ] ; then
#   echo release CMSSW_10_2_5 already exists
# else
#   cd ${ENV_PATH}
#   scram p CMSSW CMSSW_10_2_5
# fi

# cd ${ENV_PATH}/CMSSW_10_2_5/src
# eval `scram runtime -sh`
# scram b
