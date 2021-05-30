
# Production of MC for Long-Lived STau 2018

To generate ParticleFiles you need to hardcode requiered mstau, mlsp, ctau parameters inside `script/CreatePartFiles.py` and execute
```sh
> python script/CreatePartFiles.py
```

The following soft is supposed to be run at lxplus.cern.ch. To setup environment and generate config files:
```sh
> cmssw-cc6
> cd script
> ./CreateEnv.sh
> export X509_USER_PROXY=~/public/x509_voms
> voms-proxy-init --valid 192:00:00 --voms cms --rfc
> ./CreateDrivers.sh
```

Before running crab source CMSSW env:
```sh
> cd CMSSW_10_2_16_patch2/src
> cmsenv
```


For the tests it is possible to run production (few events) locally with:
```sh
> cd ./python
> ../script/TestProdLocal.sh
```

To submit production on grid:
```sh
> crab submit -c crab_cfg_step_1.py
> crab submit -c crab_cfg_step_2.py
> crab submit -c crab_cfg_step_3.py
> crab submit -c crab_cfg_step_4.py
```

Full testing commands are available at LLSTauProduction/test

The following setups are inherited from:
- https://cms-pdmv.cern.ch/mcm/requests?prepid=SUS-RunIIFall18GS-00022&page=0&shown=127 
- https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=\*SUS-RunIISummer15GS-00239\*&shown=1572991
- https://github.com/lucaswiens
