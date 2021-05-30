#!/bin/bash

# ENV_PATH=/afs/cern.ch/user/m/myshched/STauGENProduction

ABS_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
OUTDIR=${ABS_PATH}/..

ENV_PATH=${ABS_PATH}/../envs

source /cvmfs/cms.cern.ch/cmsset_default.sh
export CMSSW_GIT_REFERENCE=/cvmfs/cms.cern.ch/cmssw.git.daily
export SCRAM_ARCH=slc6_amd64_gcc700

# if [ -r ${ENV_PATH}/CMSSW_10_2_16_patch2/src ] ; then
#   echo "CMSSW_10_2_16_patch2 exists"
#   cd ${ENV_PATH}/CMSSW_10_2_16_patch2/src
#   eval `scramv1 runtime -sh` # the same as cmsenv
#   cd -
# else
#   echo "CMSSW_10_2_16_patch2 does not exist"
#   exit 1
# fi

# cmsRun -e -j SUS-RunIIFall18GS-00022_report.xml ${ABS_PATH}/../python/SUS-RunIIFall18GS-00022_1_cfg.py || exit $? ;

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

cmsRun -e -j SUS-RunIIAutumn18DRPremix-00225_0_report.xml ${ABS_PATH}/../python/SUS-RunIIAutumn18DRPremix-00225_1_cfg.py || exit $? ;

cmsRun -e -j SUS-RunIIAutumn18DRPremix-00225_report.xml ${ABS_PATH}/../python/SUS-RunIIAutumn18DRPremix-00225_2_cfg.py || exit $? ;

cmsRun -e -j SUS-RunIIAutumn18MiniAOD-00351_report.xml ${ABS_PATH}/../python/SUS-RunIIAutumn18MiniAOD-00351_1_cfg.py || exit $? ;