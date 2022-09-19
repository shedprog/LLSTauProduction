# TEMPLATE used for automatic script submission of multiple datasets

import commands
username = commands.getoutput("whoami")

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIISummer20UL18DIGIPremix-stau250_lsp1_ctau100mm_v6'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../python/SUS-RunIISummer20UL18DIGIPremix_cfg.py'

config.JobType.maxJobRuntimeMin = 20*60
config.JobType.maxMemoryMB = 4000

config.section_("Data")

config.Data.inputDataset = ''
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1 #number of events per jobs
# config.Data.totalUnits = 500 #number of event

config.Data.outLFNDirBase = '/store/user/%s/mc/UL2018-pythia-v6' %(username)
config.Data.publication = True
config.Data.outputDatasetTag = 'PREMIXRAW'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
