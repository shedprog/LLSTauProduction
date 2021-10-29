
# Production of MC for Long-Lived STau 20UL18 (updated GEN-SIM recipe)

For the UL production follows: https://cms-pdmv.cern.ch/mcm/chained_requests?prepid=SUS-chain_RunIISummer20UL18wmLHEGEN_flowRunIISummer20UL18SIM_flowRunIISummer20UL18DIGIPremix_flowRunIISummer20UL18HLT_flowRunIISummer20UL18RECO_flowRunIISummer20UL18MiniAODv2-00012&page=0&shown=15

To generate ParticleFiles you need to hardcode requiered mstau, mlsp, ctau parameters inside `script/CreatePartFiles.py` and execute
```sh
> python script/CreatePartFiles.py
```

The following soft is supposed to be run at lxplus.cern.ch. To setup environment and generate config files:
```sh
> cd script
> ./CreateEnv.sh
> export X509_USER_PROXY=~/public/x509_voms
> voms-proxy-init --valid 192:00:00 --voms cms --rfc
> ./CreateDrivers.sh
```


For the tests it is possible to run production (few events) locally with:
```sh
> cd ./python
> ../script/TestProdLocal.sh
```