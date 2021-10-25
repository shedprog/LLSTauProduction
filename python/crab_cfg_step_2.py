# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIIFall18GS_ctau1000mm_mstau100_250_400_mlsp1_20-PREMIXRAW'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIIAutumn18DRPremix-00225_1_cfg.py'

config.JobType.maxJobRuntimeMin = 20*60
config.JobType.maxMemoryMB = 4000

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIIFall18GS_ctau1000mm_mstau100_250_400_mlsp1_20-RAWSIM/myshched-SUS-RunIIFall18GS_ctau1000mm_mstau100_250_400_mlsp1_20-RAWSIM-47668c1fec598f2e7574fc0c3a6a0522/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1 #number of events per jobs
# config.Data.totalUnits = 500 #number of event

config.Data.outLFNDirBase = '/store/user/myshched/SUS-RunIIFall18GS-production-new/SUS-RunIIFall18GS_ctau1000mm_mstau100_250_400_mlsp1_20-PREMIXRAW'
config.Data.publication = True
config.Data.outputDatasetTag = 'SUS-RunIIFall18GS_ctau1000mm_mstau100_250_400_mlsp1_20-PREMIXRAW'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
