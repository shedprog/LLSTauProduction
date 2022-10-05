# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromCRIC

username = getUsernameFromCRIC()

config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18MiniAOD-stau100_lsp1_ctau100mm_v6'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18MiniAODv2_cfg.py'

config.JobType.maxJobRuntimeMin = 5*60
config.JobType.maxMemoryMB = 2500

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau100mm_v6/sobhatta-RECO-1a2a8efe82f5ce56cfcbf6dbf5abbe49/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/user/%s/mc/UL2018-pythia-v6' %(username)
config.Data.publication = True
config.Data.outputDatasetTag = 'MiniAOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
