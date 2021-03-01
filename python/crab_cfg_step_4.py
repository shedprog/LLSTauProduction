# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-MiniAOD'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIIAutumn18MiniAOD-00351_1_cfg.py'

config.JobType.maxJobRuntimeMin = 2*60
config.JobType.maxMemoryMB = 2500

config.section_("Data")


#config.Data.inputDBS = 'global'

#config.Data.userInputFiles = open('List_2_2.txt').readlines()

config.Data.inputDataset = '/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-RAWSIM/myshched-SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-AOD-2fd59cbde119ecab78af65e08efe8aae/USER'
config.Data.inputDBS = 'phys03'

#config.Data.outputPrimaryDataset = 'SMS-T1tttt_mini'


config.Data.splitting = 'FileBased'#'Automatic' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 1#number of files
config.Data.outLFNDirBase = '/store/user/myshched/SUS-RunIIFall18GS-production/SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-MiniAOD'
config.Data.publication = True
config.Data.outputDatasetTag = 'SUS-RunIIFall18GS_ctau0p01-1000mm_mstau90_mlsp50-MiniAOD'

config.section_("Site")
config.Site.whitelist = ['T2_DE_DESY']
config.Site.storageSite = 'T2_DE_DESY'
