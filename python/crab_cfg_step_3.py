# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-AOD'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIIAutumn18DRPremix-00225_2_cfg.py'

config.JobType.maxJobRuntimeMin = 20*60
config.JobType.maxMemoryMB = 4000

config.section_("Data")


#config.Data.inputDBS = 'global'

#config.Data.userInputFiles = open('List_2_2.txt').readlines()

config.Data.inputDataset = '/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-RAWSIM/myshched-SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-PREMIXRAW-5aa1749307f00d6302ec929df355f761/USER'
config.Data.inputDBS = 'phys03'

#config.Data.outputPrimaryDataset = 'SMS-T1tttt_mini'


config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 1#number of files
config.Data.outLFNDirBase = '/store/user/myshched/SUS-RunIIFall18GS-production/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-AOD'
config.Data.publication = True
config.Data.outputDatasetTag = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-AOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
