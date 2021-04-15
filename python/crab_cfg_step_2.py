# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp1-PREMIXRAW'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIIAutumn18DRPremix-00225_1_cfg.py'

config.JobType.maxJobRuntimeMin = 20*60
config.JobType.maxMemoryMB = 4000

config.section_("Data")

config.Data.inputDataset = '/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM/myshched-SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM-fb425d1c5dfc8ad081616fbde3d99149/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1 #number of events per jobs
config.Data.totalUnits = 500 #number of event

config.Data.outLFNDirBase = '/store/user/myshched/SUS-RunIIFall18GS-production/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp1-PREMIXRAW'
config.Data.publication = True
config.Data.outputDatasetTag = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp1-PREMIXRAW'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
