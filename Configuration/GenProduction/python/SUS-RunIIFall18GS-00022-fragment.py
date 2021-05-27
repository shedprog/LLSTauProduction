import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

import math

baseSLHATable="""
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


generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    RandomizedParameters = cms.VPSet(),
)

model = "TStauStauLL"


hBarCinGeVmm = 1.973269788e-13

# gevWidth = [0.01, 0.05, 0.1, 0.5, 1, 2.5, 5, 7.5, 10]
# mstaus = [90, 100, 125, 150, 175, 200, 250, 300, 350, 400, 450, 500]
# mlsps = [50,100]

# gevWidth = [0.01, 50, 100, 250, 500, 750, 1000]
gevWidth = [1000]
mstaus = [100]
mlsps = [1]

def matchParams(mass):
    if mass < 99: return 80,0.63
    elif mass < 149: return 80,0.62
    elif mass < 199: return 80,0.56
    elif mass < 249 : return 80,0.53
    elif mass < 299 : return 80,0.51
    elif mass < 349 : return 80,0.49
    elif mass < 399 : return 80,0.47
    elif mass < 499 : return 80,0.46
    elif mass < 549 : return 80,0.45
    else: return 80,0.45

# Number of events in thousands per mass point
nevt = 50


# -------------------------------
#    Constructing grid

mpoints = []

for mx in mstaus:
    for my in mlsps:
        if my<mx:
            mpoints.append([mx,my,nevt])


for ctau0 in gevWidth:
  for point in mpoints:
    mstau, mlsp = point[0], point[1]
    qcut, tru_eff = matchParams(mstau)
    wgt = point[2]/tru_eff
    ctau = hBarCinGeVmm / ctau0

    if mlsp==0: mlsp = 1
    slhatable = baseSLHATable.replace('%MSTAU%','%e' % mstau)
    slhatable = slhatable.replace('%MLSP%','%e' % mlsp)
    slhatable = slhatable.replace('%CTAU%','%e' % ctau)

    FLAVOR = 'stau'
    COM_ENERGY = 13000. 
    MASS_POINT = mstau  # GeV
    PROCESS_FILE = 'SimG4Core/CustomPhysics/data/RhadronProcessList.txt'
    PARTICLE_FILE = ("particles_stau_mstau{}GeV_mlsp{}GeV_ctau{}mm.txt".format(mstau, mlsp, ctau0))
    SLHA_FILE = 'dummy.slha'
    USE_REGGE = False

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


    basePythiaParameters.pythia8CommonSettings.extend(['1000015:tau0 = %e' % ctau0])
    basePythiaParameters.pythia8CommonSettings.extend(['ParticleDecays:tau0Max = 3000.1'])
    basePythiaParameters.pythia8CommonSettings.extend(['LesHouches:setLifetime = 2'])

    generator.RandomizedParameters.append(
        cms.PSet(
            ConfigWeight = cms.double(wgt),
            GridpackPath =  cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/SMS-TStauStau/v1/SMS-TStauStau_mStau-%i_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % mstau),
            ConfigDescription = cms.string('%s_%i_%i_%f' % (model, mstau, mlsp, ctau0)),
            SLHATableForPythia8 = cms.string('%s' % slhatable),
            PythiaParameters = basePythiaParameters,
        ),
    )

    generator.hscpFlavor = cms.untracked.string(FLAVOR)
    generator.massPoint = cms.untracked.int32(MASS_POINT)
    generator.SLHAFileForPythia8 = cms.untracked.string(SLHA_FILE)
    generator.processFile = cms.untracked.string(PROCESS_FILE)
    generator.particleFile = cms.untracked.string(PARTICLE_FILE)
    generator.useregge = cms.bool(USE_REGGE)
    