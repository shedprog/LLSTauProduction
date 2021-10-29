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
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700
if [ -r ${ENV_PATH}/CMSSW_10_6_27/src ] ; then
  echo release CMSSW_10_6_27 already exists
else
  cd ${ENV_PATH}
  scram p CMSSW CMSSW_10_6_27

  cd ${ENV_PATH}/CMSSW_10_6_27/src
  eval `scramv1 runtime -sh`
  git cms-addpkg SimG4Core/CustomPhysics/
  git cms-addpkg Configuration/Generator/
fi


# Step 1: Copy test particle files
mkdir -p ${ENV_PATH}/CMSSW_10_6_27/src/data
cp ${OUTDIR}/Configuration/ParticleFiles/*.txt ${ENV_PATH}/CMSSW_10_6_27/src/data

cd ${ENV_PATH}/CMSSW_10_6_27/src

# Step 2: Copy genParticlePlusGeant
cp -f ${OUTDIR}/Configuration/genParticlePlusGeant.py ${ENV_PATH}/CMSSW_10_6_27/src/SimG4Core/CustomPhysics/python/genParticlePlusGeant.py

# Step 3: Copy HSCP file
cp -f ${OUTDIR}/Configuration/Exotica_HSCP_SIM_cfi.py ${ENV_PATH}/CMSSW_10_6_27/src/SimG4Core/CustomPhysics/python/Exotica_HSCP_SIM_cfi.py

# Step 3: Copy fragment-file
mkdir -p ${ENV_PATH}/CMSSW_10_6_27/src/Configuration/GenProduction/python
cp -f ${OUTDIR}/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-LLStau.py ${ENV_PATH}/CMSSW_10_6_27/src/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-LLStau.py
[ -s ${ENV_PATH}/CMSSW_10_6_27/src/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-LLStau.py ] || exit $?;
eval `scram runtime -sh`
scram b


if [ -r ${ENV_PATH}/CMSSW_10_2_16_UL/src ] ; then
  echo release CMSSW_10_2_16_UL already exists
else
  cd ${ENV_PATH}
  scram p CMSSW CMSSW_10_2_16_UL

  cd ${ENV_PATH}/CMSSW_10_2_16_UL/src
  eval `scramv1 runtime -sh`
  git cms-addpkg SimG4Core/CustomPhysics/
  git cms-addpkg Configuration/Generator/
fi
cd ${ENV_PATH}/CMSSW_10_2_16_UL/src

# Step 2: Copy genParticlePlusGeant
cp -f ${OUTDIR}/Configuration/genParticlePlusGeant.py ${ENV_PATH}/CMSSW_10_2_16_UL/src/SimG4Core/CustomPhysics/python/genParticlePlusGeant.py

# Step 3: Copy HSCP file
cp -f ${OUTDIR}/Configuration/Exotica_HSCP_SIM_cfi.py ${ENV_PATH}/CMSSW_10_2_16_UL/src/SimG4Core/CustomPhysics/python/Exotica_HSCP_SIM_cfi.py

eval `scram runtime -sh`
scram b
