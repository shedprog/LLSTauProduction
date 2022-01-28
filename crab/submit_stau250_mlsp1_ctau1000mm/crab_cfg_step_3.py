# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18HLT-stau250_lsp1_ctau1000mm_v4'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18HLT_cfg.py'

config.JobType.maxJobRuntimeMin = 10*60
config.JobType.maxMemoryMB = 4000

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIISummer20UL18GEN-stau250_lsp1_ctau1000mm_v4/myshched-PREMIXRAW-2ba8a5596d4fba7b13e51f381fcee32a/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/myshched/mc/UL2018-pythia-v4'
config.Data.publication = True
config.Data.outputDatasetTag = 'HLT'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
