#!/bin/bash

ENV_PATH=/afs/cern.ch/user/m/myshched/STauGENProduction

ABS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR=${ABS_PATH}/..

source /cvmfs/cms.cern.ch/cmsset_default.sh
export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
export SCRAM_ARCH=slc6_amd64_gcc700

if [ -r ${ENV_PATH}/CMSSW_10_2_16_patch2/src ] ; then
  echo "CMSSW_10_2_16_patch2 exists"
  cd ${ENV_PATH}/CMSSW_10_2_16_patch2/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_2_16_patch2 does not exist"
  exit 1
fi

echo "Creating cmsDrive for RAWSIM"
#cmsDriver.py Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py --python_filename ${OUTDIR}/python/SUS-RunIIFall18GS-00022_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:SUS-RunIIFall18GS-00022.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(191)" --step GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc || exit $? ;

cmsDriver.py Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py --python_filename ${OUTDIR}/python/SUS-RunIIFall18GS-00022_1_cfg.py --eventcontent RAWSIM --outputCommand 'keep *_genParticlePlusGeant_*_*' --customise SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:SUS-RunIIFall18GS-00022.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(191)" --step GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc || exit $? ;

eval `scram runtime -sh`

if [ -r ${ENV_PATH}/CMSSW_10_2_5/src ] ; then
  echo "CMSSW_10_2_5 exists"
  cd ${ENV_PATH}/CMSSW_10_2_5/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_2_5 does not exist"
  exit 1
fi

echo "Creating cmsDrive for PREMIXRAW"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIIAutumn18DRPremix-00225_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:SUS-RunIIAutumn18DRPremix-00225_0.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --geometry DB:Extended --filein file:SUS-RunIIFall18GS-00022.root --datamix PreMix --era Run2_2018 --no_exec --mc || exit $? ;

echo "Creating cmsDrive for AODSIM"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIIAutumn18DRPremix-00225_2_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:SUS-RunIIAutumn18DRPremix-00225.root --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --filein file:SUS-RunIIAutumn18DRPremix-00225_0.root --era Run2_2018 --runUnscheduled --no_exec --mc || exit $? ;

echo "Creating cmsDrive for MINIAODSIM"
cmsDriver.py  --python_filename ${OUTDIR}/python/SUS-RunIIAutumn18MiniAOD-00351_1_cfg.py --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --fileout file:SUS-RunIIAutumn18MiniAOD-00351.root --conditions 102X_upgrade2018_realistic_v15 --step PAT --geometry DB:Extended --filein file:SUS-RunIIAutumn18DRPremix-00225.root --era Run2_2018 --runUnscheduled --no_exec --mc || exit $? ;

eval `scram runtime -sh`
