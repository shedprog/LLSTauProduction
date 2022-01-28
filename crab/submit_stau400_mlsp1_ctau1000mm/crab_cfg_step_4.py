# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18RECO-stau400_lsp1_ctau1000mm_v4'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18RECO_cfg.py'

config.JobType.maxJobRuntimeMin = 5*60
config.JobType.maxMemoryMB = 2500

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIISummer20UL18GEN-stau400_lsp1_ctau1000mm_v4/myshched-HLT-b403a189a2d057e62e59ed092120c7f4/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/myshched/mc/UL2018-pythia-v4'
config.Data.publication = True
config.Data.outputDatasetTag = 'RECO'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
