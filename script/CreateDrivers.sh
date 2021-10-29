#!/bin/bash

# ENV_PATH=/afs/cern.ch/user/m/myshched/STauGENProduction

ABS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR=${ABS_PATH}/..

ENV_PATH=${ABS_PATH}/../envs

echo "OUTDIR: ${OUTDIR}"
echo "ENV_PATH: ${ENV_PATH}"

source /cvmfs/cms.cern.ch/cmsset_default.sh
export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
export SCRAM_ARCH=slc7_amd64_gcc700

if [ -r ${ENV_PATH}/CMSSW_10_6_27/src ] ; then
  echo "CMSSW_10_6_27 exists"
  cd ${ENV_PATH}/CMSSW_10_6_27/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_27 does not exist"
  exit 1
fi

echo "Creating cmsDrive for GEN-SIM"
cmsDriver.py Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-LLStau.py \
  --python_filename ${OUTDIR}/python/SUS-RunIISummer20UL18wmLHEGEN_cfg.py \
  --eventcontent RAWSIM,LHE \
  --outputCommand 'keep *_genParticlePlusGeant_*_*' \
  --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce \
  --datatier GEN-SIM,LHE \
  --fileout file:SUS-RunIISummer20UL18wmLHEGEN-LLStau.root \
  --conditions 106X_upgrade2018_realistic_v11_L1v1 \
  --beamspot Realistic25ns13TeVEarly2018Collision \
  --customise_commands "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1)\nprocess.source.numberEventsInLuminosityBlock=cms.untracked.uint32(100)" \
  --step LHE,GEN,SIM \
  --geometry DB:Extended \
  --era Run2_2018 \
  --no_exec --mc -n 20 || exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_6_27/src ] ; then
  echo "CMSSW_10_6_27 exists"
  cd ${ENV_PATH}/CMSSW_10_6_27/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_27 does not exist"
  exit 1
fi

echo "Creating cmsDrive for PREMIXRAW"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIISummer20UL18DIGIPremix_cfg.py \
  --eventcontent PREMIXRAW \
  --outputCommand 'keep *_genParticlePlusGeant_*_*' \
  --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce \
  --datatier GEN-SIM-RAW \
  --fileout file:SUS-RunIIAutumn18DRPremix-LLStau.root \
  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL18_106X_upgrade2018_realistic_v11_L1v1-v2/PREMIX" \
  --conditions 106X_upgrade2018_realistic_v11_L1v1 \
  --step DIGI,DATAMIX,L1,DIGI2RAW \
  --procModifiers premix_stage2 \
  --geometry DB:Extended \
  --filein file:SUS-RunIISummer20UL18wmLHEGEN-LLStau.root \
  --datamix PreMix --era Run2_2018 \
  --no_exec --mc  -n 20 || exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_2_16_UL/src ] ; then
  echo "CMSSW_10_2_16_UL exists"
  cd ${ENV_PATH}/CMSSW_10_2_16_UL/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_2_16_UL does not exist"
  exit 1
fi

echo "Creating cmsDrive for HLT"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIISummer20UL18HLT_cfg.py \
  --eventcontent RAWSIM \
  --outputCommand 'keep *_genParticlePlusGeant_*_*' \
  --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce \
  --datatier GEN-SIM-RAW \
  --fileout file:SUS-RunIISummer20UL18HLT-LLStau.root \
  --conditions 102X_upgrade2018_realistic_v15 \
  --customise_commands 'process.source.bypassVersionCheck = cms.untracked.bool(True)' \
  --step HLT:2018v32 \
  --geometry DB:Extended \
  --filein file:SUS-RunIIAutumn18DRPremix-LLStau.root \
  --era Run2_2018 --no_exec --mc -n 20|| exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_6_27/src ] ; then
  echo "CMSSW_10_6_27 exists"
  cd ${ENV_PATH}/CMSSW_10_6_27/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_27 does not exist"
  exit 1
fi


echo "Creating cmsDrive for AOD"
# cmsDriver command
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIISummer20UL18RECO_cfg.py\
  --eventcontent AODSIM \
  --outputCommand 'keep *_genParticlePlusGeant_*_*' \
  --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce \
  --datatier AODSIM \
  --fileout file:SUS-RunIISummer20UL18RECO-LLStau.root \
  --conditions 106X_upgrade2018_realistic_v11_L1v1 \
  --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI \
  --geometry DB:Extended \
  --filein file:SUS-RunIISummer20UL18HLT-LLStau.root \
  --era Run2_2018 --runUnscheduled \
  --no_exec --mc -n 20 || exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_6_27/src ] ; then
  echo "CMSSW_10_6_27 exists"
  cd ${ENV_PATH}/CMSSW_10_6_27/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_27 does not exist"
  exit 1
fi

echo "Creating cmsDrive for MiniAOD"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIISummer20UL18MiniAODv2_cfg.py \
--eventcontent MINIAODSIM \
--outputCommand 'keep *_genParticlePlusGeant_*_*' \
--customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce \
--datatier MINIAODSIM \
--fileout file:SUS-RunIISummer20UL18MiniAODv2-LLStau.root \
--conditions 106X_upgrade2018_realistic_v16_L1v1 \
--step PAT --procModifiers run2_miniAOD_UL \
--geometry DB:Extended \
--filein file:SUS-RunIISummer20UL18RECO-LLStau.root\
 --era Run2_2018 --runUnscheduled \
 --no_exec --mc -n 20 || exit $? ;
