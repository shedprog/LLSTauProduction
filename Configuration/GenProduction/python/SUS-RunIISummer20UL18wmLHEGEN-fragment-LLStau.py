FLAVOR = 'stau'
COM_ENERGY = 13000. # GeV
MASS_POINT = 100   # GeV
MASS_LSP = 1 # GeV
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep#NLO_NLL_any_single_generation_su
CROSS_SECTION = 0.3657 # pb
CTAU_POINT = 1000 # mm
PROCESS_FILE = 'SimG4Core/CustomPhysics/data/RhadronProcessList.txt'
PARTICLE_FILE = ("data/particles_stau_mstau{}GeV_mlsp{}GeV_ctau{}mm.txt".format(MASS_POINT, MASS_LSP, CTAU_POINT))
USE_REGGE = False
# GRIDPACK = '/srv/staus_%s_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz' % (MASS_POINT)
GRIDPACK =  '/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/SMS-TStauStau/v1/SMS-TStauStau_mStau-%s_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz' % (MASS_POINT)
# SLHA_FILE = 'dummy.slha'
SLHA_TABLE="""
##******************************************************************
##                      MadGraph/MadEvent                          *
##******************************************************************
## Les Houches friendly file for the (MS)SM parameters of MadGraph *
##      SM parameter set and decay widths produced by MSSMCalc     *
##******************************************************************
##*Please note the following IMPORTANT issues:                     *
##                                                                 *
##0. REFRAIN from editing this file by hand! Some of the parame-   *
##   ters are not independent. Always use a calculator.            *
##                                                                 *
##1. alpha_S(MZ) has been used in the calculation of the parameters*
##   This value is KEPT by madgraph when no pdf are used lpp(i)=0, *
##   but, for consistency, it will be reset by madgraph to the     *
##   value expected IF the pdfs for collisions with hadrons are    *
##   used.                                                         *
##                                                                 *
##2. Values of the charm and bottom kinematic (pole) masses are    *
##   those used in the matrix elements and phase space UNLESS they *
##   are set to ZERO from the start in the model (particles.dat)   *
##   This happens, for example,  when using 5-flavor QCD where     *
##   charm and bottom are treated as partons in the initial state  *
##   and a zero mass might be hardwired in the model definition.   *
##                                                                 *
##       The SUSY decays have calculated using SDECAY 1.1a         *
##                                                                 *
##******************************************************************
#
BLOCK DCINFO  # Decay Program information
     1   SDECAY      # decay calculator
     2   1.1a        # version number
#
BLOCK SPINFO  # Spectrum calculator information
     1   ISASUGRA
     2   7.81
#
BLOCK MODSEL  # Model selection
     1     1   #
#
BLOCK SMINPUTS  # Standard Model inputs
     1     1.25778332E+02   # alpha_em^-1(M_Z)^MSbar
     2     1.16570000E-05   # G_F [GeV^-2]
     3     1.17200002E-01   # alpha_S(M_Z)^MSbar
     4     9.11876000E+01   # M_Z pole mass
     5     4.25000000E+00   # mb(mb)^MSbar
     6     1.72500000E+02   # mt pole mass (extracted)
     7     1.77682000E+00   # mtau pole mass (extracted)
#
BLOCK MINPAR  # Input parameters - minimal models
     1     6.00000000E+02   #  m_0
     2     3.00000000E+02   #  m_{1/2}
     3     1.00000000E+01   #  tan(beta)
     4     1.00000000E+00   #  sign(mu)
#
BLOCK EXTPAR  # Input parameters - non-minimal models
     0     2.21278347E+16   #  Input scale
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
         5     4.80000000E+00   # b-quark pole mass (extracted)
         6     1.72500000E+02   # t-quark pole mass (not read by ME)
        15     1.77682000E+00   # tau pole mass (not read by ME)
        23     9.11876000E+01   # Z pole mass (not read by ME)
        24     8.03990000E+01   # W+
        25     1.25000000E+02   # h
        35     7.49062561E+05   # H
        36     7.43967712E+05   # A
        37     7.53755432E+05   # H+
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
#
BLOCK NMIX  # Neutralino Mixing Matrix
  1  1     1.00000000E+00   # N_11
  1  2     0.00000000E+00   # N_12
  1  3     0.00000000E+00   # N_13
  1  4     0.00000000E+00   # N_14
  2  1     0.00000000E+00   # N_21
  2  2     1.00000000E+00   # N_22
  2  3     0.00000000E+00   # N_23
  2  4     0.00000000E+00   # N_24
  3  1     0.00000000E+00   # N_31
  3  2     0.00000000E+00   # N_32
  3  3     1.00000000E+00   # N_33
  3  4     0.00000000E+00   # N_34
  4  1     0.00000000E+00   # N_41
  4  2     0.00000000E+00   # N_42
  4  3     0.00000000E+00   # N_43
  4  4     1.00000000E+00   # N_44
#
BLOCK UMIX  # Chargino Mixing Matrix U
  1  1     1.00000000E+00   # U_11
  1  2     0.00000000E+00   # U_12
  2  1     0.00000000E+00   # U_21
  2  2     1.00000000E+00   # U_22
#
BLOCK VMIX  # Chargino Mixing Matrix V
  1  1     1.00000000E+00   # V_11
  1  2     0.00000000E+00   # V_12
  2  1     0.00000000E+00   # V_21
  2  2     1.00000000E+00   # V_22
#
BLOCK STOPMIX  # Stop Mixing Matrix
  1  1     1.00000000E+00   # O_{11}
  1  2     0.00000000E+00   # O_{12}
  2  1     0.00000000E+00   # O_{21}
  2  2     1.00000000E+00   # O_{22}
#
BLOCK SBOTMIX  # Sbottom Mixing Matrix
  1  1     1.00000000E+00   # O_{11}
  1  2     0.00000000E+00   # O_{12}
  2  1     0.00000000E+00   # O_{21}
  2  2     1.00000000E+00   # O_{22}
#
Block SELMIX
    1   1 1.000000e+00 # RRl11
    2   2 1.000000e+00 # RRl22
    3   3 2.8248721e-01 # RRl33
    3   6 9.5927111e-01 # RRl36
    4   4 1.000000e+00 # RRl44
    5   5 1.000000e+00 # RRl55
    6   3 9.592711e-01 # RRl63
    6   6 -2.824872e-01 # RRl66
#
BLOCK ALPHA  # Higgs mixing
          -1.02914833E-01   # Mixing angle in the neutral Higgs boson sector
#
BLOCK HMIX Q=  6.61219971E+02  # DRbar Higgs Parameters
     1     4.12454407E+02   #  mu(Q)
     2     9.36003455E+00   # tanb (extracted)
     3     2.50607727E+02   #  Higgs vev at Q
     4     5.53487938E+05   #  m_A^2(Q)
#
BLOCK GAUGE Q=  6.61219971E+02  # The gauge couplings
     3     1.07381373E+00   # g3(Q) MSbar
#
BLOCK AU Q=  6.61219971E+02  # The trilinear couplings
  3  3    -5.32061523E+02   # A_t(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK AD Q=  6.61219971E+02  # The trilinear couplings
  3  3    -8.07902039E+02   # A_b(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK AE Q=  6.61219971E+02  # The trilinear couplings
  3  3    -1.81115051E+02   # A_tau(Q) DRbar
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YU Q=  6.61219971E+02  # The Yukawa couplings
  3  3     8.85841429E-01   # y_t(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YD Q=  6.61219971E+02  # The Yukawa couplings
  3  3     1.36232540E-01   # y_b(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK YE Q=  6.61219971E+02  # The Yukawa couplings
  3  3     1.01981103E-01   # y_tau(Q) (extracted)
  1  1     0.000000e+00 # dummy
  2  2     0.000000e+00 # dummy
#
BLOCK MSOFT Q=  6.61219971E+02  # The soft SUSY breaking masses at the scale Q
     1     1.24019547E+02   #  M_1(Q)
     2     2.32185043E+02   #  M_2(Q)
     3     6.86750671E+02   #  M_3(Q)
    21     3.23374943E+04   # mH1^2(Q)
    22    -1.28800134E+05   # mH2^2(Q)
    31     6.29402649E+02   #  MeL(Q)
    32     6.29402649E+02   #  MmuL(Q)
    33     6.26662476E+02   #  MtauL(Q)
    34     6.08800842E+02   #  MeR(Q)
    35     6.08800842E+02   #  MmuR(Q)
    36     6.03154236E+02   #  MtauR(Q)
    41     8.48326294E+02   #  MqL1(Q)
    42     8.48326294E+02   #  MqL2(Q)
    43     7.40788147E+02   #  MqL3(Q)
    44     8.34092896E+02   #  MuR(Q)
    45     8.34092896E+02   #  McR(Q)
    46     5.90198242E+02   #  MtR(Q)
    47     8.32408752E+02   #  MdR(Q)
    48     8.32408752E+02   #  MsR(Q)
    49     8.31454102E+02   #  MbR(Q)
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
# - The multi-body decays for the inos, stops and sbottoms are included.
#
# - The SUSY decays of the top quark are included.
#
#
#         PDG            Width
DECAY        23     2.49520000E+00   # Z width (SM calculation)
DECAY        24     2.08500000E+00   # W width (SM calculation)
#
#         PDG            Width
DECAY         6     1.02218095E+00   # top decays
#          BR         NDA      ID1       ID2
     1.00000000E+00    2           5        24   # BR(t ->  b    W+)
     0.00000000E+00    2           5        37   # BR(t ->  b    H+)
     0.00000000E+00    2     1000006   1000022   # BR(t -> ~t_1 ~chi_10)
     0.00000000E+00    2     1000006   1000023   # BR(t -> ~t_1 ~chi_20)
     0.00000000E+00    2     1000006   1000025   # BR(t -> ~t_1 ~chi_30)
     0.00000000E+00    2     1000006   1000035   # BR(t -> ~t_1 ~chi_40)
     0.00000000E+00    2     2000006   1000022   # BR(t -> ~t_2 ~chi_10)
     0.00000000E+00    2     2000006   1000023   # BR(t -> ~t_2 ~chi_20)
     0.00000000E+00    2     2000006   1000025   # BR(t -> ~t_2 ~chi_30)
     0.00000000E+00    2     2000006   1000035   # BR(t -> ~t_2 ~chi_40)
#
#         PDG            Width
DECAY        25     1.65461618E-03   # h decays
#          BR         NDA      ID1       ID2
     1.47339152E-01    2          15       -15   # BR(H1 -> tau- tau+)
     7.81441418E-01    2           5        -5   # BR(H1 -> b bb)
     6.76395564E-02    2          24       -24   # BR(H1 -> W+ W-)
     3.57987415E-03    2          23        23   # BR(H1 -> Z Z)
#
#         PDG            Width
DECAY        35     1.26118245E+00   # H decays
#          BR         NDA      ID1       ID2
     1.21586159E-01    2          15       -15   # BR(H -> tau- tau+)
     2.21890882E-01    2           6        -6   # BR(H -> t tb)
     6.50784860E-01    2           5        -5   # BR(H -> b bb)
     1.26971777E-03    2          24       -24   # BR(H -> W+ W-)
     6.21230085E-04    2          23        23   # BR(H -> Z Z)
     0.00000000E+00    2          24       -37   # BR(H -> W+ H-)
     0.00000000E+00    2         -24        37   # BR(H -> W- H+)
     0.00000000E+00    2          37       -37   # BR(H -> H+ H-)
     3.84715147E-03    2          25        25   # BR(H -> h h)
     0.00000000E+00    2          36        36   # BR(H -> A A)
#
#         PDG            Width
DECAY        36     1.32606570E+00   # A decays
#          BR         NDA      ID1       ID2
     1.14768736E-01    2          15       -15   # BR(A -> tau- tau+)
     2.69728288E-01    2           6        -6   # BR(A -> t tb)
     6.14379413E-01    2           5        -5   # BR(A -> b bb)
     1.12356280E-03    2          23        25   # BR(A -> Z h)
     0.00000000E+00    2          23        35   # BR(A -> Z H)
     0.00000000E+00    2          24       -37   # BR(A -> W+ H-)
     0.00000000E+00    2         -24        37   # BR(A -> W- H+)
#
#         PDG            Width
DECAY        37     1.27808456E+00   # H+ decays
#          BR         NDA      ID1       ID2
     1.20644761E-01    2         -15        16   # BR(H+ -> tau+ nu_tau)
     8.78124903E-01    2           6        -5   # BR(H+ -> t bb)
     1.23033590E-03    2          24        25   # BR(H+ -> W+ h)
     0.00000000E+00    2          24        35   # BR(H+ -> W+ H)
     0.00000000E+00    2          24        36   # BR(H+ -> W+ A)
#
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

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(GRIDPACK),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

#need the pythia hadronizer, not the generator, as the generation was already done in the madgraph gridpacks
generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(
            'SUSY:all = off',
            'SUSY:qqbar2sleptonantislepton= on',
            '1000015:mayDecay = false', #left-handed stau
            '-1000015:mayDecay = false',
            '1000022:mayDecay = false', #LSP
            '-1000022:mayDecay = false', #gravitino
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'pythia8PSweightsSettings',
            'processParameters'
        )
    )
)

generator.hscpFlavor = cms.untracked.string(FLAVOR)
generator.massPoint = cms.untracked.int32(MASS_POINT)
generator.particleFile = cms.untracked.string(PARTICLE_FILE)
generator.processFile = cms.untracked.string(PROCESS_FILE)
# generator.SLHAFileForPythia8 = cms.untracked.string(SLHA_FILE)
generator.useregge = cms.bool(USE_REGGE)

ProductionFilterSequence = cms.Sequence(externalLHEProducer*generator)

# leptonicTauDecayGenFilter = cms.EDFilter("LeptonicTauDecayGenFilter",
#                                              inputTag = cms.InputTag("genParticlePlusGeant")
#                                         )