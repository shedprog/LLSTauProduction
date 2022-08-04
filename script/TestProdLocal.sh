#!/bin/bash

# ENV_PATH=/afs/cern.ch/user/m/myshched/STauGENProduction

ABS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR=${ABS_PATH}/..

ENV_PATH=${ABS_PATH}/../envs

source /cvmfs/cms.cern.ch/cmsset_default.sh
export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
export SCRAM_ARCH=slc7_amd64_gcc700

if [ -r ${ENV_PATH}/CMSSW_10_6_30_patch1/src ] ; then
  echo "CMSSW_10_6_30_patch1 exists"
  cd ${ENV_PATH}/CMSSW_10_6_30_patch1/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_30_patch1 does not exist"
  exit 1
fi

cmsRun -e -j SUS-RunIISummer20UL18wmLHEGEN_report.xml ${ABS_PATH}/../python/SUS-RunIISummer20UL18wmLHEGEN-stau100_lsp1_ctau100mm_cfg.py || exit $? ;

cmsRun -e -j SUS-RunIISummer20UL18DIGIPremix_report.xml ${ABS_PATH}/../python/SUS-RunIISummer20UL18DIGIPremix_cfg.py || exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_2_16_UL/src ] ; then
  echo "CMSSW_10_2_16_UL exists"
  cd ${ENV_PATH}/CMSSW_10_2_16_UL/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_2_16_UL does not exist"
  exit 1
fi

cmsRun -e -j SUS-RunIISummer20UL18HLT_report.xml ${ABS_PATH}/../python/SUS-RunIISummer20UL18HLT_cfg.py || exit $? ;

if [ -r ${ENV_PATH}/CMSSW_10_6_30_patch1/src ] ; then
  echo "CMSSW_10_6_30_patch1 exists"
  cd ${ENV_PATH}/CMSSW_10_6_30_patch1/src
  eval `scramv1 runtime -sh` # the same as cmsenv
  cd -
else
  echo "CMSSW_10_6_30_patch1 does not exist"
  exit 1
fi

cmsRun -e -j SUS-RunIISummer20UL18RECO_report.xml ${ABS_PATH}/../python/SUS-RunIISummer20UL18RECO_cfg.py || exit $? ;

cmsRun -e -j SUS-RunIISummer20UL18MiniAODv2_report.xml ${ABS_PATH}/../python/SUS-RunIISummer20UL18MiniAODv2_cfg.py || exit $? ;
