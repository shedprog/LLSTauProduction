# TEMPLATE used for automatic script submission of multiple datasets

import commands
username = commands.getoutput("whoami")

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18GEN-stau400_lsp1_ctau100mm_v4'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18wmLHEGEN-stau400_lsp1_ctau100mm_cfg.py'

config.JobType.maxJobRuntimeMin = 20*60
config.JobType.maxMemoryMB = 2000

config.section_("Data")
config.Data.inputDBS = 'global'
config.Data.outputPrimaryDataset = 'SUS-RunIISummer20UL18GEN-stau400_lsp1_ctau1000mm_v4'
config.Data.splitting = 'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1000 #number of events per jobs
config.Data.totalUnits = 2000000 #number of event
# config.Data.totalUnits = 10#number of event for testing
config.Data.outLFNDirBase = '/store/user/%s/mc/UL2018-pythia-v4' %(username)
config.Data.publication = True
config.Data.outputDatasetTag = 'GENSIM'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
