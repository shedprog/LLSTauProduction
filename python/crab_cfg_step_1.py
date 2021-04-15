# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SUS-RunIIFall18GS-00022_1_cfg.py'

config.JobType.maxJobRuntimeMin = 35*60
config.JobType.maxMemoryMB = 2500


config.section_("Data")
config.Data.inputDBS = 'global'
config.Data.outputPrimaryDataset = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM'
config.Data.splitting = 'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 5000 #number of events per jobs
config.Data.totalUnits = 14000000 #number of event
#config.Data.totalUnits = 10#number of event for testing
config.Data.outLFNDirBase = '/store/user/myshched/SUS-RunIIFall18GS-production/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM-RAWSIM'
config.Data.publication = True
config.Data.outputDatasetTag = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau100_mlsp1-RAWSIM'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
