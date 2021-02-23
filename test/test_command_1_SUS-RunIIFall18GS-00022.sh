#!/bin/bash

# GEN Script begin
rm -f request_fragment_check.py
wget -q https://raw.githubusercontent.com/cms-sw/genproductions/master/bin/utils/request_fragment_check.py
python request_fragment_check.py --bypass_status --prepid SUS-RunIIFall18GS-00022
GEN_ERR=$?
if [ $GEN_ERR -ne 0 ]; then
  echo "GEN Checking Script returned exit code $GEN_ERR which means there are $GEN_ERR errors"
  echo "Validation WILL NOT RUN"
  echo "Please correct errors in the request and run validation again"
  exit $GEN_ERR
fi
echo "Running VALIDATION. GEN Request Checking Script returned no errors"
# GEN Script end

# Dump actual test code to a SUS-RunIIFall18GS-00022_test.sh file that can be run in Singularity
cat <<'EndOfTestFile' > SUS-RunIIFall18GS-00022_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_16_patch2/src ] ; then
  echo release CMSSW_10_2_16_patch2 already exists
else
  scram p CMSSW CMSSW_10_2_16_patch2
fi
cd CMSSW_10_2_16_patch2/src
eval `scram runtime -sh`

# Download fragment from McM
curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/SUS-RunIIFall18GS-00022 --retry 3 --create-dirs -o Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py
[ -s Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py ] || exit $?;

# Check if fragment contais gridpack path ant that it is in cvmfs
if grep -q "gridpacks" Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py; then
  if ! grep -q "/cvmfs/cms.cern.ch/phys_generator/gridpacks" Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py; then
    echo "Gridpack inside fragment is not in cvmfs."
    exit -1
  fi
fi
scram b
cd ../..

# Maximum validation duration: 57600s
# Margin for validation duration: 20%
# Validation duration with margin: 57600 * (1 - 0.20) = 46080s
# Time per event for each sequence: 15.8590s
# Threads for each sequence: 1
# Time per event for single thread for each sequence: 1 * 15.8590s = 15.8590s
# Which adds up to 15.8590s per event
# Single core events that fit in validation duration: 46080s / 15.8590s = 2905
# Produced events limit in McM is 10000
# According to 0.5210 efficiency, up to 10000 / 0.5210 = 19193 events should run
# Clamp (put value) 2905 within 1 and 19193 -> 2905
# It is estimated that this validation will produce: 2905 * 0.5210 = 1513 events
EVENTS=2905


# cmsDriver command
cmsDriver.py Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py --python_filename SUS-RunIIFall18GS-00022_1_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:SUS-RunIIFall18GS-00022.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)"\\nprocess.source.numberEventsInLuminosityBlock="cms.untracked.uint32(191)" --step GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n $EVENTS || exit $? ;

# Run generated config
cmsRun -e -j SUS-RunIIFall18GS-00022_report.xml SUS-RunIIFall18GS-00022_1_cfg.py || exit $? ;

# Report SUS-RunIIFall18GS-00022_report.xml
cat SUS-RunIIFall18GS-00022_report.xml

# Parse values from SUS-RunIIFall18GS-00022_report.xml report
totalEvents=$(grep -Po "(?<=<TotalEvents>)(\d*)(?=</TotalEvents>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
threads=$(grep -Po "(?<=<Metric Name=\"NumberOfThreads\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
peakValueRss=$(grep -Po "(?<=<Metric Name=\"PeakValueRss\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
peakValueVsize=$(grep -Po "(?<=<Metric Name=\"PeakValueVsize\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
totalSize=$(grep -Po "(?<=<Metric Name=\"Timing-tstoragefile-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
totalSizeAlt=$(grep -Po "(?<=<Metric Name=\"Timing-file-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
totalJobTime=$(grep -Po "(?<=<Metric Name=\"TotalJobTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
totalJobCPU=$(grep -Po "(?<=<Metric Name=\"TotalJobCPU\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
eventThroughput=$(grep -Po "(?<=<Metric Name=\"EventThroughput\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
avgEventTime=$(grep -Po "(?<=<Metric Name=\"AvgEventTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIFall18GS-00022_report.xml | tail -n 1)
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
echo "Validation report of SUS-RunIIFall18GS-00022 sequence 1/1"
echo "Total events: $totalEvents"
echo "Threads: $threads"
echo "Peak value RSS: $peakValueRss MB"
echo "Peak value Vsize: $peakValueVsize MB"
echo "Total size: $totalSize MB"
echo "Total job time: $totalJobTime s"
echo "Total CPU time: $totalJobCPU s"
echo "Event throughput: $eventThroughput"
echo "CPU efficiency: "$(bc -l <<< "scale=2; ($totalJobCPU * 100) / ($threads * $totalJobTime)")" %"
echo "Size per event: "$(bc -l <<< "scale=4; ($totalSize * 1024 / $totalEvents)")" kB"
echo "Time per event: "$(bc -l <<< "scale=4; (1 / $eventThroughput)")" s"
echo "Filter efficiency percent: "$(bc -l <<< "scale=8; ($totalEvents * 100) / $EVENTS")" %"
echo "Filter efficiency fraction: "$(bc -l <<< "scale=10; ($totalEvents) / $EVENTS")

# End of SUS-RunIIFall18GS-00022_test.sh file
EndOfTestFile

# Make file executable
chmod +x SUS-RunIIFall18GS-00022_test.sh

# Run in SLC6 container
# Mount afs, eos, cvmfs
# Mount /etc/grid-security for xrootd
export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
singularity run -B /afs -B /eos -B /cvmfs -B /etc/grid-security --home $PWD:$PWD docker://cmssw/slc6:latest $(echo $(pwd)/SUS-RunIIFall18GS-00022_test.sh)
