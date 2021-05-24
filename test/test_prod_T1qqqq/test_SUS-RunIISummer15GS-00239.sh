#!/bin/bash

# GEN Script begin
rm -f request_fragment_check.py
wget -q https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/utils/request_fragment_check.py
python request_fragment_check.py --bypass_status --prepid SUS-RunIISummer15GS-00239
GEN_ERR=$?
if [ $GEN_ERR -ne 0 ]; then
  echo "GEN Checking Script returned exit code $GEN_ERR which means there are $GEN_ERR errors"
  echo "Validation WILL NOT RUN"
  echo "Please correct errors in the request and run validation again"
  exit $GEN_ERR
fi
echo "Running VALIDATION. GEN Request Checking Script returned no errors"
# GEN Script end

# Dump actual test code to a SUS-RunIISummer15GS-00239_test.sh file that can be run in Singularity
cat <<'EndOfTestFile' > SUS-RunIISummer15GS-00239_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_41/src ] ; then
  echo release CMSSW_7_1_41 already exists
else
  scram p CMSSW CMSSW_7_1_41
fi
cd CMSSW_7_1_41/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SUS-RunIISummer15GS-00239 --retry 3 --create-dirs -o Configuration/GenProduction/python/SUS-RunIISummer15GS-00239-fragment.py
[ -s Configuration/GenProduction/python/SUS-RunIISummer15GS-00239-fragment.py ] || exit $?;

# Check if fragment contais gridpack path ant that it is in cvmfs
if grep -q "gridpacks" Configuration/GenProduction/python/SUS-RunIISummer15GS-00239-fragment.py; then
  if ! grep -q "/cvmfs/cms.cern.ch/phys_generator/gridpacks" Configuration/GenProduction/python/SUS-RunIISummer15GS-00239-fragment.py; then
    echo "Gridpack inside fragment is not in cvmfs."
    exit -1
  fi
fi
scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 19.8793s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 19.8793s = 19.8793s
# Which adds up to 19.8793s per event
# Single core events that fit in validation duration: 23040s / 19.8793s = 1158
# Produced events limit in McM is 10000
# According to 0.2990 efficiency, validation should run 10000 / 0.2990 = 33444 events to reach the limit of 10000
# Take the minimum of 1158 and 33444, but more than 0 -> 1158
# It is estimated that this validation will produce: 1158 * 0.2990 = 346 events
EVENTS=1158


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/SUS-RunIISummer15GS-00239-fragment.py --python_filename SUS-RunIISummer15GS-00239_1_cfg.py --eventcontent RAWSIM --outputCommand 'keep *_genParticlePlusGeant_*_*' --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:SUS-RunIISummer15GS-00239.root --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)" --step GEN,SIM --magField 38T_PostLS1 --no_exec --mc -n $EVENTS || exit $? ;

# Run generated config
REPORT_NAME=SUS-RunIISummer15GS-00239_report.xml
# Run the cmsRun
cmsRun -e -j $REPORT_NAME SUS-RunIISummer15GS-00239_1_cfg.py || exit $? ;

# Parse values from SUS-RunIISummer15GS-00239_report.xml report
processedEvents=$(grep -Po "(?<=<Metric Name=\"NumberEvents\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
producedEvents=$(grep -Po "(?<=<TotalEvents>)(\d*)(?=</TotalEvents>)" $REPORT_NAME | tail -n 1)
threads=$(grep -Po "(?<=<Metric Name=\"NumberOfThreads\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
peakValueRss=$(grep -Po "(?<=<Metric Name=\"PeakValueRss\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
peakValueVsize=$(grep -Po "(?<=<Metric Name=\"PeakValueVsize\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
totalSize=$(grep -Po "(?<=<Metric Name=\"Timing-tstoragefile-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
totalSizeAlt=$(grep -Po "(?<=<Metric Name=\"Timing-file-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
totalJobTime=$(grep -Po "(?<=<Metric Name=\"TotalJobTime\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
totalJobCPU=$(grep -Po "(?<=<Metric Name=\"TotalJobCPU\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
eventThroughput=$(grep -Po "(?<=<Metric Name=\"EventThroughput\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
avgEventTime=$(grep -Po "(?<=<Metric Name=\"AvgEventTime\" Value=\")(.*)(?=\"/>)" $REPORT_NAME | tail -n 1)
if [ -z "$threads" ]; then
  echo "Could not find NumberOfThreads in report, defaulting to 1"
  threads=1
fi
if [ -z "$eventThroughput" ]; then
  eventThroughput=$(bc -l <<< "scale=4; 1 / ($avgEventTime / $threads)")
fi
if [ -z "$totalSize" ]; then
  totalSize=$totalSizeAlt
fi
if [ -z "$processedEvents" ]; then
  processedEvents=$EVENTS
fi
echo "Validation report of SUS-RunIISummer15GS-00239 sequence 1/1"
echo "Processed events: $processedEvents"
echo "Produced events: $producedEvents"
echo "Threads: $threads"
echo "Peak value RSS: $peakValueRss MB"
echo "Peak value Vsize: $peakValueVsize MB"
echo "Total size: $totalSize MB"
echo "Total job time: $totalJobTime s"
echo "Total CPU time: $totalJobCPU s"
echo "Event throughput: $eventThroughput"
echo "CPU efficiency: "$(bc -l <<< "scale=2; ($totalJobCPU * 100) / ($threads * $totalJobTime)")" %"
echo "Size per event: "$(bc -l <<< "scale=4; ($totalSize * 1024 / $producedEvents)")" kB"
echo "Time per event: "$(bc -l <<< "scale=4; (1 / $eventThroughput)")" s"
echo "Filter efficiency percent: "$(bc -l <<< "scale=8; ($producedEvents * 100) / $processedEvents")" %"
echo "Filter efficiency fraction: "$(bc -l <<< "scale=10; ($producedEvents) / $processedEvents")

# End of SUS-RunIISummer15GS-00239_test.sh file
EndOfTestFile

# Make file executable
chmod +x SUS-RunIISummer15GS-00239_test.sh

# Run in SLC6 container
# Mount afs, eos, cvmfs
# Mount /etc/grid-security for xrootd
export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
singularity run -B /afs -B /eos -B /cvmfs -B /etc/grid-security --home $PWD:$PWD /cvmfs/unpacked.cern.ch/registry.hub.docker.com/cmssw/slc6:amd64 $(echo $(pwd)/SUS-RunIISummer15GS-00239_test.sh)
