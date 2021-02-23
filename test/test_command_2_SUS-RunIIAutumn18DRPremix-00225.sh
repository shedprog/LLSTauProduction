#!/bin/bash

# Dump actual test code to a SUS-RunIIAutumn18DRPremix-00225_test.sh file that can be run in Singularity
cat <<'EndOfTestFile' > SUS-RunIIAutumn18DRPremix-00225_test.sh
#!/bin/bash

export SCRAM_ARCH=slc6_amd64_gcc700

source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_5/src ] ; then
  echo release CMSSW_10_2_5 already exists
else
  scram p CMSSW CMSSW_10_2_5
fi
cd CMSSW_10_2_5/src
eval `scram runtime -sh`

scram b
cd ../..

# Maximum validation duration: 28800s
# Margin for validation duration: 20%
# Validation duration with margin: 28800 * (1 - 0.20) = 23040s
# Time per event for each sequence: 0.9940s, 1.1987s
# Threads for each sequence: 8, 8
# Time per event for single thread for each sequence: 8 * 0.9940s = 7.9520s, 8 * 1.1987s = 9.5896s
# Which adds up to 17.5416s per event
# Single core events that fit in validation duration: 23040s / 17.5416s = 1313
# Produced events limit in McM is 10000
# According to 1.0000 efficiency, up to 10000 / 1.0000 = 10000 events should run
# Clamp (put value) 1313 within 1 and 10000 -> 1313
# It is estimated that this validation will produce: 1313 * 1.0000 = 1313 events
EVENTS=1313


# cmsDriver command
cmsDriver.py  --python_filename SUS-RunIIAutumn18DRPremix-00225_1_cfg.py --eventcontent PREMIXRAW --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --fileout file:SUS-RunIIAutumn18DRPremix-00225_0.root --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW" --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --geometry DB:Extended --filein file:SUS-RunIIFall18GS-00022.root --datamix PreMix --era Run2_2018 --no_exec --mc -n $EVENTS || exit $? ;

# Run generated config
cmsRun -e -j SUS-RunIIAutumn18DRPremix-00225_0_report.xml SUS-RunIIAutumn18DRPremix-00225_1_cfg.py || exit $? ;

# Report SUS-RunIIAutumn18DRPremix-00225_0_report.xml
cat SUS-RunIIAutumn18DRPremix-00225_0_report.xml

# Parse values from SUS-RunIIAutumn18DRPremix-00225_0_report.xml report
totalEvents=$(grep -Po "(?<=<TotalEvents>)(\d*)(?=</TotalEvents>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
threads=$(grep -Po "(?<=<Metric Name=\"NumberOfThreads\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
peakValueRss=$(grep -Po "(?<=<Metric Name=\"PeakValueRss\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
peakValueVsize=$(grep -Po "(?<=<Metric Name=\"PeakValueVsize\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
totalSize=$(grep -Po "(?<=<Metric Name=\"Timing-tstoragefile-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
totalSizeAlt=$(grep -Po "(?<=<Metric Name=\"Timing-file-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
totalJobTime=$(grep -Po "(?<=<Metric Name=\"TotalJobTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
totalJobCPU=$(grep -Po "(?<=<Metric Name=\"TotalJobCPU\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
eventThroughput=$(grep -Po "(?<=<Metric Name=\"EventThroughput\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
avgEventTime=$(grep -Po "(?<=<Metric Name=\"AvgEventTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_0_report.xml | tail -n 1)
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
echo "Validation report of SUS-RunIIAutumn18DRPremix-00225 sequence 1/2"
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

# cmsDriver command
cmsDriver.py  --python_filename SUS-RunIIAutumn18DRPremix-00225_2_cfg.py --eventcontent AODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --fileout file:SUS-RunIIAutumn18DRPremix-00225.root --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --procModifiers premix_stage2 --filein file:SUS-RunIIAutumn18DRPremix-00225_0.root --era Run2_2018 --runUnscheduled --no_exec --mc -n $EVENTS || exit $? ;

# Run generated config
cmsRun -e -j SUS-RunIIAutumn18DRPremix-00225_report.xml SUS-RunIIAutumn18DRPremix-00225_2_cfg.py || exit $? ;

# Report SUS-RunIIAutumn18DRPremix-00225_report.xml
cat SUS-RunIIAutumn18DRPremix-00225_report.xml

# Parse values from SUS-RunIIAutumn18DRPremix-00225_report.xml report
totalEvents=$(grep -Po "(?<=<TotalEvents>)(\d*)(?=</TotalEvents>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
threads=$(grep -Po "(?<=<Metric Name=\"NumberOfThreads\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
peakValueRss=$(grep -Po "(?<=<Metric Name=\"PeakValueRss\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
peakValueVsize=$(grep -Po "(?<=<Metric Name=\"PeakValueVsize\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
totalSize=$(grep -Po "(?<=<Metric Name=\"Timing-tstoragefile-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
totalSizeAlt=$(grep -Po "(?<=<Metric Name=\"Timing-file-write-totalMegabytes\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
totalJobTime=$(grep -Po "(?<=<Metric Name=\"TotalJobTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
totalJobCPU=$(grep -Po "(?<=<Metric Name=\"TotalJobCPU\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
eventThroughput=$(grep -Po "(?<=<Metric Name=\"EventThroughput\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
avgEventTime=$(grep -Po "(?<=<Metric Name=\"AvgEventTime\" Value=\")(.*)(?=\"/>)" SUS-RunIIAutumn18DRPremix-00225_report.xml | tail -n 1)
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
echo "Validation report of SUS-RunIIAutumn18DRPremix-00225 sequence 2/2"
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

# End of SUS-RunIIAutumn18DRPremix-00225_test.sh file
EndOfTestFile

# Make file executable
chmod +x SUS-RunIIAutumn18DRPremix-00225_test.sh

# Run in SLC6 container
# Mount afs, eos, cvmfs
# Mount /etc/grid-security for xrootd
export SINGULARITY_CACHEDIR="/tmp/$(whoami)/singularity"
singularity run -B /afs -B /eos -B /cvmfs -B /etc/grid-security --home $PWD:$PWD docker://cmssw/slc6:latest $(echo $(pwd)/SUS-RunIIAutumn18DRPremix-00225_test.sh)
