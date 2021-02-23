
# Production of MC for Long-Lived STau 2018

The following setups are taken from:
https://cms-pdmv.cern.ch/mcm/requests?prepid=SUS-RunIIFall18GS-00022&page=0&shown=127
Thanks https://github.com/lucaswiens for the help.

The following soft is supposed to be run at lxplus.cern.ch. To setup environment and generate config files:
```sh
> cmssw-cc6
> cd script
> ./CreateEnv.sh
> export X509_USER_PROXY=~/public/x509_voms
> voms-proxy-init --valid 192:00:00 --voms cms --rf
> ./CreateDrivers.sh
```

To submit PREMIX
```sh
crab submit -c
```
