# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stau400_lsp1_ctau1000mm.py --python_filename /afs/cern.ch/user/m/myshched/STauGENProduction/LLSTauProduction20UL18/script/../python/SUS-RunIISummer20UL18wmLHEGEN-stau400_lsp1_ctau1000mm_cfg.py --eventcontent RAWSIM --outputCommand keep *_genParticlePlusGeant_*_* --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi.customise,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeKeep,SimG4Core/CustomPhysics/genParticlePlusGeant.customizeProduce --datatier GEN-SIM --fileout file:SUS-RunIISummer20UL18wmLHEGEN-LLStau.root --conditions 106X_upgrade2018_realistic_v11_L1v1 --beamspot Realistic25ns13TeVEarly2018Collision --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1)\nprocess.source.numberEventsInLuminosityBlock=cms.untracked.uint32(100) --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2018 --no_exec --mc -n 20
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('SIM',Run2_2018)

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
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-fragment-stau400_lsp1_ctau1000mm.py nevts:20'),
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
    fileName = cms.untracked.string('file:SUS-RunIISummer20UL18wmLHEGEN-LLStau.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v11_L1v1', '')
process.RAWSIMoutput.outputCommands.append('keep *_genParticlePlusGeant_*_*')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'pythia8PSweightsSettings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SUSY:all = off', 
            'SUSY:qqbar2sleptonantislepton= on', 
            '1000015:mayDecay = false', 
            '-1000015:mayDecay = false', 
            '1000022:mayDecay = false', 
            '-1000022:mayDecay = false'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
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
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
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
            'ParticleDecays:allowPhotonRadiation = on'
        ),
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on', 
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,isr_G2GG_muR_up isr:G2GG:muRfac=2.0,isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,isr_X2XG_muR_up isr:X2XG:muRfac=2.0,isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,isr_G2GG_cNS_up isr:G2GG:cNS=2.0,isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,isr_X2XG_cNS_up isr:X2XG:cNS=2.0}', 
            'UncertaintyBands:nFlavQ = 4', 
            'UncertaintyBands:MPIshowers = on', 
            'UncertaintyBands:overSampleFSR = 10.0', 
            'UncertaintyBands:overSampleISR = 10.0', 
            'UncertaintyBands:FSRpTmin2Fac = 20', 
            'UncertaintyBands:ISRpTmin2Fac = 1'
        )
    ),
    SLHATableForPythia8 = cms.string('\n##******************************************************************\n##                      MadGraph/MadEvent                          *\n##******************************************************************\n## Les Houches friendly file for the (MS)SM parameters of MadGraph *\n##      SM parameter set and decay widths produced by MSSMCalc     *\n##******************************************************************\n##*Please note the following IMPORTANT issues:                     *\n##                                                                 *\n##0. REFRAIN from editing this file by hand! Some of the parame-   *\n##   ters are not independent. Always use a calculator.            *\n##                                                                 *\n##1. alpha_S(MZ) has been used in the calculation of the parameters*\n##   This value is KEPT by madgraph when no pdf are used lpp(i)=0, *\n##   but, for consistency, it will be reset by madgraph to the     *\n##   value expected IF the pdfs for collisions with hadrons are    *\n##   used.                                                         *\n##                                                                 *\n##2. Values of the charm and bottom kinematic (pole) masses are    *\n##   those used in the matrix elements and phase space UNLESS they *\n##   are set to ZERO from the start in the model (particles.dat)   *\n##   This happens, for example,  when using 5-flavor QCD where     *\n##   charm and bottom are treated as partons in the initial state  *\n##   and a zero mass might be hardwired in the model definition.   *\n##                                                                 *\n##       The SUSY decays have calculated using SDECAY 1.1a         *\n##                                                                 *\n##******************************************************************\n#\nBLOCK DCINFO  # Decay Program information\n     1   SDECAY      # decay calculator\n     2   1.1a        # version number\n#\nBLOCK SPINFO  # Spectrum calculator information\n     1   ISASUGRA\n     2   7.81\n#\nBLOCK MODSEL  # Model selection\n     1     1   #\n#\nBLOCK SMINPUTS  # Standard Model inputs\n     1     1.25778332E+02   # alpha_em^-1(M_Z)^MSbar\n     2     1.16570000E-05   # G_F [GeV^-2]\n     3     1.17200002E-01   # alpha_S(M_Z)^MSbar\n     4     9.11876000E+01   # M_Z pole mass\n     5     4.25000000E+00   # mb(mb)^MSbar\n     6     1.72500000E+02   # mt pole mass (extracted)\n     7     1.77682000E+00   # mtau pole mass (extracted)\n#\nBLOCK MINPAR  # Input parameters - minimal models\n     1     6.00000000E+02   #  m_0\n     2     3.00000000E+02   #  m_{1/2}\n     3     1.00000000E+01   #  tan(beta)\n     4     1.00000000E+00   #  sign(mu)\n#\nBLOCK EXTPAR  # Input parameters - non-minimal models\n     0     2.21278347E+16   #  Input scale\n#\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n         5     4.80000000E+00   # b-quark pole mass (extracted)\n         6     1.72500000E+02   # t-quark pole mass (not read by ME)\n        15     1.77682000E+00   # tau pole mass (not read by ME)\n        23     9.11876000E+01   # Z pole mass (not read by ME)\n        24     8.03990000E+01   # W+\n        25     1.25000000E+02   # h\n        35     7.49062561E+05   # H\n        36     7.43967712E+05   # A\n        37     7.53755432E+05   # H+\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     4.000000e+02          # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.00000000E+05   # ~g\n   1000022     1.000000e+00           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n#\nBLOCK NMIX  # Neutralino Mixing Matrix\n  1  1     1.00000000E+00   # N_11\n  1  2     0.00000000E+00   # N_12\n  1  3     0.00000000E+00   # N_13\n  1  4     0.00000000E+00   # N_14\n  2  1     0.00000000E+00   # N_21\n  2  2     1.00000000E+00   # N_22\n  2  3     0.00000000E+00   # N_23\n  2  4     0.00000000E+00   # N_24\n  3  1     0.00000000E+00   # N_31\n  3  2     0.00000000E+00   # N_32\n  3  3     1.00000000E+00   # N_33\n  3  4     0.00000000E+00   # N_34\n  4  1     0.00000000E+00   # N_41\n  4  2     0.00000000E+00   # N_42\n  4  3     0.00000000E+00   # N_43\n  4  4     1.00000000E+00   # N_44\n#\nBLOCK UMIX  # Chargino Mixing Matrix U\n  1  1     1.00000000E+00   # U_11\n  1  2     0.00000000E+00   # U_12\n  2  1     0.00000000E+00   # U_21\n  2  2     1.00000000E+00   # U_22\n#\nBLOCK VMIX  # Chargino Mixing Matrix V\n  1  1     1.00000000E+00   # V_11\n  1  2     0.00000000E+00   # V_12\n  2  1     0.00000000E+00   # V_21\n  2  2     1.00000000E+00   # V_22\n#\nBLOCK STOPMIX  # Stop Mixing Matrix\n  1  1     1.00000000E+00   # O_{11}\n  1  2     0.00000000E+00   # O_{12}\n  2  1     0.00000000E+00   # O_{21}\n  2  2     1.00000000E+00   # O_{22}\n#\nBLOCK SBOTMIX  # Sbottom Mixing Matrix\n  1  1     1.00000000E+00   # O_{11}\n  1  2     0.00000000E+00   # O_{12}\n  2  1     0.00000000E+00   # O_{21}\n  2  2     1.00000000E+00   # O_{22}\n#\nBlock SELMIX\n    1   1 1.000000e+00 # RRl11\n    2   2 1.000000e+00 # RRl22\n    3   3 2.8248721e-01 # RRl33\n    3   6 9.5927111e-01 # RRl36\n    4   4 1.000000e+00 # RRl44\n    5   5 1.000000e+00 # RRl55\n    6   3 9.592711e-01 # RRl63\n    6   6 -2.824872e-01 # RRl66\n#\nBLOCK ALPHA  # Higgs mixing\n          -1.02914833E-01   # Mixing angle in the neutral Higgs boson sector\n#\nBLOCK HMIX Q=  6.61219971E+02  # DRbar Higgs Parameters\n     1     4.12454407E+02   #  mu(Q)\n     2     9.36003455E+00   # tanb (extracted)\n     3     2.50607727E+02   #  Higgs vev at Q\n     4     5.53487938E+05   #  m_A^2(Q)\n#\nBLOCK GAUGE Q=  6.61219971E+02  # The gauge couplings\n     3     1.07381373E+00   # g3(Q) MSbar\n#\nBLOCK AU Q=  6.61219971E+02  # The trilinear couplings\n  3  3    -5.32061523E+02   # A_t(Q) DRbar\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK AD Q=  6.61219971E+02  # The trilinear couplings\n  3  3    -8.07902039E+02   # A_b(Q) DRbar\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK AE Q=  6.61219971E+02  # The trilinear couplings\n  3  3    -1.81115051E+02   # A_tau(Q) DRbar\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK YU Q=  6.61219971E+02  # The Yukawa couplings\n  3  3     8.85841429E-01   # y_t(Q) (extracted)\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK YD Q=  6.61219971E+02  # The Yukawa couplings\n  3  3     1.36232540E-01   # y_b(Q) (extracted)\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK YE Q=  6.61219971E+02  # The Yukawa couplings\n  3  3     1.01981103E-01   # y_tau(Q) (extracted)\n  1  1     0.000000e+00 # dummy\n  2  2     0.000000e+00 # dummy\n#\nBLOCK MSOFT Q=  6.61219971E+02  # The soft SUSY breaking masses at the scale Q\n     1     1.24019547E+02   #  M_1(Q)\n     2     2.32185043E+02   #  M_2(Q)\n     3     6.86750671E+02   #  M_3(Q)\n    21     3.23374943E+04   # mH1^2(Q)\n    22    -1.28800134E+05   # mH2^2(Q)\n    31     6.29402649E+02   #  MeL(Q)\n    32     6.29402649E+02   #  MmuL(Q)\n    33     6.26662476E+02   #  MtauL(Q)\n    34     6.08800842E+02   #  MeR(Q)\n    35     6.08800842E+02   #  MmuR(Q)\n    36     6.03154236E+02   #  MtauR(Q)\n    41     8.48326294E+02   #  MqL1(Q)\n    42     8.48326294E+02   #  MqL2(Q)\n    43     7.40788147E+02   #  MqL3(Q)\n    44     8.34092896E+02   #  MuR(Q)\n    45     8.34092896E+02   #  McR(Q)\n    46     5.90198242E+02   #  MtR(Q)\n    47     8.32408752E+02   #  MdR(Q)\n    48     8.32408752E+02   #  MsR(Q)\n    49     8.31454102E+02   #  MbR(Q)\n#\n#\n#\n#                             =================\n#                             |The decay table|\n#                             =================\n#\n# - The multi-body decays for the inos, stops and sbottoms are included.\n#\n# - The SUSY decays of the top quark are included.\n#\n#\n#         PDG            Width\nDECAY        23     2.49520000E+00   # Z width (SM calculation)\nDECAY        24     2.08500000E+00   # W width (SM calculation)\n#\n#         PDG            Width\nDECAY         6     1.02218095E+00   # top decays\n#          BR         NDA      ID1       ID2\n     1.00000000E+00    2           5        24   # BR(t ->  b    W+)\n     0.00000000E+00    2           5        37   # BR(t ->  b    H+)\n     0.00000000E+00    2     1000006   1000022   # BR(t -> ~t_1 ~chi_10)\n     0.00000000E+00    2     1000006   1000023   # BR(t -> ~t_1 ~chi_20)\n     0.00000000E+00    2     1000006   1000025   # BR(t -> ~t_1 ~chi_30)\n     0.00000000E+00    2     1000006   1000035   # BR(t -> ~t_1 ~chi_40)\n     0.00000000E+00    2     2000006   1000022   # BR(t -> ~t_2 ~chi_10)\n     0.00000000E+00    2     2000006   1000023   # BR(t -> ~t_2 ~chi_20)\n     0.00000000E+00    2     2000006   1000025   # BR(t -> ~t_2 ~chi_30)\n     0.00000000E+00    2     2000006   1000035   # BR(t -> ~t_2 ~chi_40)\n#\n#         PDG            Width\nDECAY        25     1.65461618E-03   # h decays\n#          BR         NDA      ID1       ID2\n     1.47339152E-01    2          15       -15   # BR(H1 -> tau- tau+)\n     7.81441418E-01    2           5        -5   # BR(H1 -> b bb)\n     6.76395564E-02    2          24       -24   # BR(H1 -> W+ W-)\n     3.57987415E-03    2          23        23   # BR(H1 -> Z Z)\n#\n#         PDG            Width\nDECAY        35     1.26118245E+00   # H decays\n#          BR         NDA      ID1       ID2\n     1.21586159E-01    2          15       -15   # BR(H -> tau- tau+)\n     2.21890882E-01    2           6        -6   # BR(H -> t tb)\n     6.50784860E-01    2           5        -5   # BR(H -> b bb)\n     1.26971777E-03    2          24       -24   # BR(H -> W+ W-)\n     6.21230085E-04    2          23        23   # BR(H -> Z Z)\n     0.00000000E+00    2          24       -37   # BR(H -> W+ H-)\n     0.00000000E+00    2         -24        37   # BR(H -> W- H+)\n     0.00000000E+00    2          37       -37   # BR(H -> H+ H-)\n     3.84715147E-03    2          25        25   # BR(H -> h h)\n     0.00000000E+00    2          36        36   # BR(H -> A A)\n#\n#         PDG            Width\nDECAY        36     1.32606570E+00   # A decays\n#          BR         NDA      ID1       ID2\n     1.14768736E-01    2          15       -15   # BR(A -> tau- tau+)\n     2.69728288E-01    2           6        -6   # BR(A -> t tb)\n     6.14379413E-01    2           5        -5   # BR(A -> b bb)\n     1.12356280E-03    2          23        25   # BR(A -> Z h)\n     0.00000000E+00    2          23        35   # BR(A -> Z H)\n     0.00000000E+00    2          24       -37   # BR(A -> W+ H-)\n     0.00000000E+00    2         -24        37   # BR(A -> W- H+)\n#\n#         PDG            Width\nDECAY        37     1.27808456E+00   # H+ decays\n#          BR         NDA      ID1       ID2\n     1.20644761E-01    2         -15        16   # BR(H+ -> tau+ nu_tau)\n     8.78124903E-01    2           6        -5   # BR(H+ -> t bb)\n     1.23033590E-03    2          24        25   # BR(H+ -> W+ h)\n     0.00000000E+00    2          24        35   # BR(H+ -> W+ H)\n     0.00000000E+00    2          24        36   # BR(H+ -> W+ A)\n#\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.0000000E+00    # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     1.973270e-16           # stau_1 decays\n    1.00000000E+00    2    1000022    15\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\nDECAY   1000021     0.00000000E+00   # gluino decays\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n'),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(0.001859),
    filterEfficiency = cms.untracked.double(1),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(400),
    maxEventsToPrint = cms.untracked.int32(0),
    particleFile = cms.untracked.string('data/particles_stau_mstau400GeV_mlsp1GeV_ctau1000mm.txt'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    useregge = cms.bool(False)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.4.2/sus_sms/SMS-TStauStau/v1/SMS-TStauStau_mStau-400_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(20),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


process.ProductionFilterSequence = cms.Sequence(process.externalLHEProducer+process.generator)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise 

#call to customisation function customise imported from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
process = customise(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.genParticlePlusGeant
from SimG4Core.CustomPhysics.genParticlePlusGeant import customizeKeep,customizeProduce 

#call to customisation function customizeKeep imported from SimG4Core.CustomPhysics.genParticlePlusGeant
process = customizeKeep(process)

#call to customisation function customizeProduce imported from SimG4Core.CustomPhysics.genParticlePlusGeant
process = customizeProduce(process)

# End of customisation functions

# Customisation from command line

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=int(1)
process.source.numberEventsInLuminosityBlock=cms.untracked.uint32(100)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
