# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py --python_filename /afs/cern.ch/user/m/myshched/STauGENProduction/LLSTauProduction/script/../python/SUS-RunIIFall18GS-00022_1_cfg.py --eventcontent RAWSIM --outputCommand keep *_genParticlePlusGeant_*_* --customise SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeProduce,SimG4Core/CustomPhysics/GenPlusSimParticles_cfi.customizeKeep,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --fileout file:SUS-RunIIFall18GS-00022.root --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)\nprocess.source.numberEventsInLuminosityBlock=cms.untracked.uint32(191) --step GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIIFall18GS-00022-fragment.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:SUS-RunIIFall18GS-00022.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v11', '')
process.RAWSIMoutput.outputCommands.append('keep *_genParticlePlusGeant_*_*')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    RandomizedParameters = cms.VPSet(cms.PSet(
        ConfigDescription = cms.string('TStauStauLL_100_1_1000.000000'),
        ConfigWeight = cms.double(80.6451612903),
        GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/SMS-TStauStau/v1/SMS-TStauStau_mStau-100_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
        PythiaParameters = cms.PSet(
            JetMatchingParameters = cms.vstring(
                'JetMatching:setMad = off', 
                'JetMatching:scheme = 1', 
                'JetMatching:merge = on', 
                'JetMatching:jetAlgorithm = 2', 
                'JetMatching:etaJetMax = 5.', 
                'JetMatching:coneRadius = 1.', 
                'JetMatching:slowJetPower = 1', 
                'JetMatching:qCut = 80', 
                'JetMatching:nQmatch = 5', 
                'JetMatching:nJetMax = 2', 
                'JetMatching:doShowerKt = off', 
                '6:m0 = 172.5', 
                'Check:abortIfVeto = on'
            ),
            parameterSets = cms.vstring(
                'pythia8CommonSettings', 
                'pythia8CP5Settings', 
                'JetMatchingParameters'
            ),
            pythia8CP5Settings = cms.vstring(
                'Tune:pp 14', 
                'Tune:ee 7', 
                'MultipartonInteractions:ecmPow=0.03344', 
                'PDF:pSet=20', 
                'MultipartonInteractions:bProfile=2', 
                'MultipartonInteractions:pT0Ref=1.41', 
                'MultipartonInteractions:coreRadius=0.7634', 
                'MultipartonInteractions:coreFraction=0.63', 
                'ColourReconnection:range=5.176', 
                'SigmaTotal:zeroAXB=off', 
                'SpaceShower:alphaSorder=2', 
                'SpaceShower:alphaSvalue=0.118', 
                'SigmaProcess:alphaSvalue=0.118', 
                'SigmaProcess:alphaSorder=2', 
                'MultipartonInteractions:alphaSvalue=0.118', 
                'MultipartonInteractions:alphaSorder=2', 
                'TimeShower:alphaSorder=2', 
                'TimeShower:alphaSvalue=0.118'
            ),
            pythia8CommonSettings = cms.vstring(
                'Tune:preferLHAPDF = 2', 
                'Main:timesAllowErrors = 10000', 
                'Check:epTolErr = 0.01', 
                'Beams:setProductionScalesFromLHEF = off', 
                'SLHA:keepSM = on', 
                'SLHA:minMassSM = 1000.', 
                'ParticleDecays:limitTau0 = on', 
                'ParticleDecays:tau0Max = 10', 
                'ParticleDecays:allowPhotonRadiation = on', 
                '1000015:tau0 = 1.000000e+03', 
                'ParticleDecays:tau0Max = 3000.1', 
                'LesHouches:setLifetime = 2'
            )
        ),
        SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.000000e+02          # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.00000000E+05   # ~g\n   1000022     1.000000e+00           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.0000000E+00    # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     1.973270e-16           # stau_1 decays\n    1.00000000E+00    2    1000022    15\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\nDECAY   1000021     0.00000000E+00   # gluino decays\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n')
    )),
    SLHAFileForPythia8 = cms.untracked.string('dummy.slha'),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(100),
    maxEventsToPrint = cms.untracked.int32(1),
    particleFile = cms.untracked.string('data/particles_stau_mstau100GeV_mlsp1GeV_ctau1000mm.txt'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    useregge = cms.bool(False)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.GenPlusSimParticles_cfi
from SimG4Core.CustomPhysics.GenPlusSimParticles_cfi import customizeProduce,customizeKeep 

#call to customisation function customizeProduce imported from SimG4Core.CustomPhysics.GenPlusSimParticles_cfi
process = customizeProduce(process)

#call to customisation function customizeKeep imported from SimG4Core.CustomPhysics.GenPlusSimParticles_cfi
process = customizeKeep(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise 

#call to customisation function customise imported from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
process = customise(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(191)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
