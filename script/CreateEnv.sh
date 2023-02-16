#!/bin/bash

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
if [ -r ${ENV_PATH}/CMSSW_10_6_31_patch1/src ] ; then
  echo release CMSSW_10_6_31_patch1 already exists
else
  cd ${ENV_PATH}
  scram p CMSSW CMSSW_10_6_31_patch1

  cd ${ENV_PATH}/CMSSW_10_6_31_patch1/src
  eval `scramv1 runtime -sh`

  #git cms-addpkg SimG4Core/Generators
  #git remote add REMOTE_WITH_FIX https://github.com/shedprog/cmssw.git
  #git fetch REMOTE_WITH_FIX from-CMSSW_10_6_31_patch1-hard-stau-fix
  #git checkout -b FIXED_BR REMOTE_WITH_FIX/from-CMSSW_10_6_31_patch1-hard-stau-fix

  # Check if fix was applied:
  #LINE_FIX=`sed -n 380p SimG4Core/Generators/src/Generator.cc`
  #if [[ $LINE_FIX == *"1000015"* ]]; then
  #  echo ">>> FIX is applied!"
  #else
  #  echo "Error: FIX is not applied! git checkout should be fixed"
  #  exit 1
  #fi

fi


# Step 1: Copy test particle files
mkdir -p ${ENV_PATH}/CMSSW_10_6_31_patch1/src/data
cp ${OUTDIR}/Configuration/ParticleFiles/*.txt ${ENV_PATH}/CMSSW_10_6_31_patch1/src/data

cd ${ENV_PATH}/CMSSW_10_6_31_patch1/src

# Step 2: Copy genParticlePlusGeant
#cp -f ${OUTDIR}/Configuration/genParticlePlusGeant.py ${ENV_PATH}/CMSSW_10_6_31_patch1/src/SimG4Core/CustomPhysics/python/genParticlePlusGeant.py

# Step 3: Copy HSCP file
#cp -f ${OUTDIR}/Configuration/Exotica_HSCP_SIM_cfi.py ${ENV_PATH}/CMSSW_10_6_31_patch1/src/SimG4Core/CustomPhysics/python/Exotica_HSCP_SIM_cfi.py

# Step 3: Copy fragment-file
source ${ABS_PATH}/CrossSection.sh
mkdir -p ${ENV_PATH}/CMSSW_10_6_31_patch1/src/Configuration/GenProduction/python
#STAU_MASS_POINTS=(100 250 400) #GeV
STAU_MASS_POINTS=(250) #GeV
LSP_MASS_POINTS=(1) #GeV
CTAU_POINTS=(0.01) #mm
for MASS in ${STAU_MASS_POINTS[@]}; do
for LSP in ${LSP_MASS_POINTS[@]}; do
for CTAU in ${CTAU_POINTS[@]}; do
  CTAU_FMT=$(sed "s/\./p/g" <<< $CTAU)
  #set -e; XSEC=$(GET_XSEC $MASS); set +e
  #echo "Create fragment mstau:${MASS}, mlsp:${LSP}, ctau:${CTAU}mm, XSEC: ${XSEC}"
  echo "Create fragment mstau:${MASS}, mlsp:${LSP}, ctau:${CTAU}mm"
  #sed "s/STAU_MASS_XXX/$MASS/" ${OUTDIR}/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stauXXX_lspXXX_ctauXXXmm.py | sed "s/LSP_MASS_XXX/$LSP/" | sed "s/XSEC_XXX/$XSEC/" | sed "s/CTAU_XXX/$CTAU/" > ${ENV_PATH}/CMSSW_10_6_31_patch1/src/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stau${MASS}_lsp${LSP}_ctau${CTAU}mm.py
  sed "s/STAU_MASS_XXX/$MASS/" ${OUTDIR}/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stauXXX_lspXXX_ctauXXXmm.py | sed "s/LSP_MASS_XXX/$LSP/" | sed "s/CTAU_XXX/$CTAU/" | sed "s/CTAU_FMT_XXX/$CTAU_FMT/" > ${ENV_PATH}/CMSSW_10_6_31_patch1/src/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stau${MASS}_lsp${LSP}_ctau${CTAU_FMT}mm.py
  [ -s ${ENV_PATH}/CMSSW_10_6_31_patch1/src/Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stau${MASS}_lsp${LSP}_ctau${CTAU_FMT}mm.py ] || exit $?;
done
done
done

eval `scram runtime -sh`
scram b

if [ -r ${ENV_PATH}/CMSSW_10_2_16_UL/src ] ; then
  echo release CMSSW_10_2_16_UL already exists
else
  cd ${ENV_PATH}
  scram p CMSSW CMSSW_10_2_16_UL

  cd ${ENV_PATH}/CMSSW_10_2_16_UL/src
  eval `scramv1 runtime -sh`
  #git cms-addpkg SimG4Core/CustomPhysics
fi
cd ${ENV_PATH}/CMSSW_10_2_16_UL/src

# Step 2: Copy genParticlePlusGeant
#cp -f ${OUTDIR}/Configuration/genParticlePlusGeant.py ${ENV_PATH}/CMSSW_10_2_16_UL/src/SimG4Core/CustomPhysics/python/genParticlePlusGeant.py

# Step 3: Copy HSCP file
#cp -f ${OUTDIR}/Configuration/Exotica_HSCP_SIM_cfi.py ${ENV_PATH}/CMSSW_10_2_16_UL/src/SimG4Core/CustomPhysics/python/Exotica_HSCP_SIM_cfi.py

eval `scram runtime -sh`
scram b
