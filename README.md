
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

Before running crab source CMSSW env:
```sh
> cd CMSSW_10_2_16_patch2/src
> cmsenv
```

To submit RAWSIM step (setup crab_cfg_step_1.py):
```sh
> crab submit -c crab_cfg_step_1.py
```

To submit PREMIXRAW step (setup crab_cfg_step_2.py):
```sh
> crab submit -c crab_cfg_step_2.py
```

To submit AODSIM step (setup crab_cfg_step_3.py):
```sh
> crab submit -c crab_cfg_step_3.py
```

To submit MINIAODSIM step (setup crab_cfg_step_4.py):
```sh
> crab submit -c crab_cfg_step_4.py
```

Full commands available at LLSTauProduction/test
