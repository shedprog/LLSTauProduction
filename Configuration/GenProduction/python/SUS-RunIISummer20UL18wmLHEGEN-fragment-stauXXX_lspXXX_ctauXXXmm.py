FLAVOR = 'stau'
COM_ENERGY = 13000. # GeV
MASS_POINT = STAU_MASS_XXX   # GeV
MASS_LSP = LSP_MASS_XXX  # GeV
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep#NLO_NLL_any_single_generation_su
CROSS_SECTION = XSEC_XXX # pb
CTAU0_POINT = CTAU_XXX # mm
PROCESS_FILE = 'SimG4Core/CustomPhysics/data/RhadronProcessList.txt'
PARTICLE_FILE = ("data/particles_stau_mstau{}GeV_mlsp{}GeV_ctau{}mm.txt".format(MASS_POINT, MASS_LSP, CTAU0_POINT))
USE_REGGE = False
GRIDPACK =  '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/SMS-TStauStau/v1/SMS-TStauStau_mStau-%s_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % (MASS_POINT)
SLHA_TABLE="""
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000001     1.00000000E+05   # ~d_L
   2000001     1.00000000E+05   # ~d_R
   1000002     1.00000000E+05   # ~u_L
   2000002     1.00000000E+05   # ~u_R
   1000003     1.00000000E+05   # ~s_L
   2000003     1.00000000E+05   # ~s_R
   1000004     1.00000000E+05   # ~c_L
   2000004     1.00000000E+05   # ~c_R
   1000005     1.00000000E+05   # ~b_1
   2000005     1.00000000E+05   # ~b_2
   1000006     1.00000000E+05   # ~t_1
   2000006     1.00000000E+05   # ~t_2
   1000011     1.00000000E+05   # ~e_L
   2000011     1.00000000E+05   # ~e_R
   1000012     1.00000000E+05   # ~nu_eL
   1000013     1.00000000E+05   # ~mu_L
   2000013     1.00000000E+05   # ~mu_R
   1000014     1.00000000E+05   # ~nu_muL
   1000015     %MSTAU%          # ~tau_1
   2000015     1.00000000E+05   # ~tau_2
   1000016     1.00000000E+05   # ~nu_tauL
   1000021     1.00000000E+05   # ~g
   1000022     %MLSP%           # ~chi_10
   1000023     1.00000000E+05   # ~chi_20
   1000025     1.00000000E+05   # ~chi_30
   1000035     1.00000000E+05   # ~chi_40
   1000024     1.00000000E+05   # ~chi_1+
   1000037     1.00000000E+05   # ~chi_2+

# DECAY TABLE
#         PDG            Width
DECAY   1000001     0.00000000E+00   # sdown_L decays
DECAY   2000001     0.00000000E+00   # sdown_R decays
DECAY   1000002     0.00000000E+00   # sup_L decays
DECAY   2000002     0.00000000E+00   # sup_R decays
DECAY   1000003     0.00000000E+00   # sstrange_L decays
DECAY   2000003     0.00000000E+00   # sstrange_R decays
DECAY   1000004     0.00000000E+00   # scharm_L decays
DECAY   2000004     0.00000000E+00   # scharm_R decays
DECAY   1000005     0.00000000E+00   # sbottom1 decays
DECAY   2000005     0.00000000E+00   # sbottom2 decays
DECAY   1000006     0.00000000E+00   # stop1 decays
DECAY   2000006     0.00000000E+00   # stop2 decays
DECAY   1000011     0.00000000E+00   # selectron_L decays
DECAY   2000011     0.00000000E+00   # selectron_R decays
DECAY   1000012     0.0000000E+00    # snu_elL decays
DECAY   1000013     0.00000000E+00   # smuon_L decays
DECAY   2000013     0.00000000E+00   # smuon_R decays
DECAY   1000014     0.00000000E+00   # snu_muL decays
DECAY   1000015     %CTAU%           # stau_1 decays
    1.00000000E+00    2    1000022    15
DECAY   2000015     0.00000000E+00   # stau_2 decays
DECAY   1000016     0.00000000E+00   # snu_tauL decays
DECAY   1000021     0.00000000E+00   # gluino decays
DECAY   1000022     0.00000000E+00   # neutralino1 decays
DECAY   1000023     0.00000000E+00   # neutralino2 decays
DECAY   1000024     0.00000000E+00   # chargino1+ decays
DECAY   1000025     0.00000000E+00   # neutralino3 decays
DECAY   1000035     0.00000000E+00   # neutralino4 decays
DECAY   1000037     0.00000000E+00   # chargino2+ decays
"""

import FWCore.ParameterSet.Config as cms

# externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
#     args = cms.vstring(GRIDPACK),
#     nEvents = cms.untracked.uint32(5000),
#     numberOfParameters = cms.uint32(1),
#     outputFile = cms.string('cmsgrid_final.lhe'),
#     scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
# )

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

model = "TStauStauLL"
hBarCinGeVmm = 1.973269788e-13

ctau = hBarCinGeVmm / CTAU0_POINT
qcut = 80

slhatable = SLHA_TABLE.replace('%MSTAU%','%e' % MASS_POINT)
slhatable = slhatable.replace('%MLSP%','%e' % MASS_LSP)
slhatable = slhatable.replace('%CTAU%','%e' % ctau)

basePythiaParameters = cms.PSet(
     pythia8CommonSettingsBlock,
     pythia8CP5SettingsBlock,
     JetMatchingParameters = cms.vstring(
          'JetMatching:setMad = off',
          'JetMatching:scheme = 1',
          'JetMatching:merge = on',
          'JetMatching:jetAlgorithm = 2',
          'JetMatching:etaJetMax = 5.',
          'JetMatching:coneRadius = 1.',
          'JetMatching:slowJetPower = 1',
          'JetMatching:qCut = %.0f' % qcut, #this is the actual merging scale
          'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
          'JetMatching:nJetMax = 2', #number of partons in born matrix element for highest multiplicity
          'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
          '6:m0 = 172.5',
          'Check:abortIfVeto = on',
     ),
     parameterSets = cms.vstring('pythia8CommonSettings',
                                   'pythia8CP5Settings',
                                   'JetMatchingParameters'
     )
)

basePythiaParameters.pythia8CommonSettings.extend(['1000015:tau0 = %e' % CTAU0_POINT])
basePythiaParameters.pythia8CommonSettings.extend(['ParticleDecays:tau0Max = 4000.1'])
basePythiaParameters.pythia8CommonSettings.extend(['LesHouches:setLifetime = 2'])

generator = cms.EDFilter("Pythia8GeneratorFilter",
     maxEventsToPrint = cms.untracked.int32(1),
     pythiaPylistVerbosity = cms.untracked.int32(1),
     filterEfficiency = cms.untracked.double(1.0),
     pythiaHepMCVerbosity = cms.untracked.bool(False),
     crossSection = cms.untracked.double(CROSS_SECTION),
     comEnergy = cms.double(COM_ENERGY),
     GridpackPath =  cms.string(GRIDPACK),
     ConfigDescription = cms.string('%s_%i_%i_%f' % (model, MASS_POINT, MASS_LSP, CTAU0_POINT)),
     SLHATableForPythia8 = cms.string('%s' % slhatable),
     PythiaParameters = basePythiaParameters,
)

generator.hscpFlavor = cms.untracked.string(FLAVOR)
generator.massPoint = cms.untracked.int32(MASS_POINT)
generator.particleFile = cms.untracked.string(PARTICLE_FILE)
generator.processFile = cms.untracked.string(PROCESS_FILE)
# generator.SLHAFileForPythia8 = cms.untracked.string(SLHA_FILE)
generator.useregge = cms.bool(USE_REGGE)

#need the pythia hadronizer, not the generator, as the generation was already done in the madgraph gridpacks
# generator = cms.EDFilter("Pythia8HadronizerFilter",
#     pythiaPylistVerbosity = cms.untracked.int32(0),
#     filterEfficiency = cms.untracked.double(1),
#     pythiaHepMCVerbosity = cms.untracked.bool(False),
#     comEnergy = cms.double(COM_ENERGY),
#     crossSection = cms.untracked.double(CROSS_SECTION),
#     maxEventsToPrint = cms.untracked.int32(0),
#     SLHATableForPythia8 = cms.string('%s' % slhatable),
#     PythiaParameters = cms.PSet(
#         pythia8CommonSettingsBlock,
#         pythia8CP5SettingsBlock,
#         pythia8PSweightsSettingsBlock,
#         processParameters = cms.vstring(
#             'SUSY:all = off',
#             'SUSY:qqbar2sleptonantislepton= on',
#             '1000015:mayDecay = false', #left-handed stau
#             '-1000015:mayDecay = false',
#             '1000022:mayDecay = false', #LSP
#             '-1000022:mayDecay = false', 
#         ),
#         parameterSets = cms.vstring(
#             'pythia8CommonSettings',
#             'pythia8CP5Settings',
#             'pythia8PSweightsSettings',
#             'processParameters'
#         )
#     )
# )

# generator.hscpFlavor = cms.untracked.string(FLAVOR)
# generator.massPoint = cms.untracked.int32(MASS_POINT)
# generator.particleFile = cms.untracked.string(PARTICLE_FILE)
# generator.processFile = cms.untracked.string(PROCESS_FILE)
# # generator.SLHAFileForPythia8 = cms.untracked.string(SLHA_FILE)
# generator.useregge = cms.bool(USE_REGGE)

# ProductionFilterSequence = cms.Sequence(externalLHEProducer*generator)

# leptonicTauDecayGenFilter = cms.EDFilter("LeptonicTauDecayGenFilter",
#                                              inputTag = cms.InputTag("genParticlePlusGeant")
#                                         )