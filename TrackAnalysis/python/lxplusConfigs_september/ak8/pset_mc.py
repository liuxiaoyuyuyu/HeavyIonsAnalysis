import FWCore.ParameterSet.Config as cms
import HLTrigger.HLTfilters.hltHighLevel_cfi
process = cms.Process('Analysis')

# Limit the output messages
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

# input files
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    fileNames = cms.untracked.vstring(
        "/store/mc/RunIISummer20UL18MiniAODv2/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/100000/021E9C3E-CEB9-4343-9B3A-12790E92E8D9.root"
        ),
    )

# number of events to process, set to -1 to process all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# load Global Tag, geometry, etc.
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# root output
process.TFileService = cms.Service("TFileService",
    fileName = cms.string("output_UL_ak8.root"))

process.hlt = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone()
process.hlt.HLTPaths = ['HLT_AK8PFJet500_v*'] # for allphysics
process.hlt.andOr = cms.bool(True)
process.hlt.throw = cms.bool(False)
process.eventFilterHLT = cms.Sequence(process.hlt)

process.analyzer = cms.EDAnalyzer('TrackAnalyzer',
    doTrack = cms.untracked.bool(False),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    lostTracksSrc = cms.InputTag("lostTracks"),
    beamSpotSrc = cms.untracked.InputTag('offlineBeamSpot'),
    #jets2 = cms.InputTag("slimmedJets"),
    #jets2 = cms.InputTag('slimmedJetsPuppi'),
    jets2 = cms.InputTag('slimmedJetsAK8'),
    #jets2 = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked"),

    doGen = cms.untracked.bool(True),
    genEvtInfo = cms.InputTag("generator"),
    packedGen = cms.InputTag("packedGenParticles"),
    genJets = cms.InputTag("slimmedGenJetsAK8"),
    puSummaryInfo = cms.InputTag("slimmedAddPileupInfo")
)

# main forest sequence
process.runAnalyzer = cms.Path(
#    process.eventFilterHLT*
    process.analyzer
    )
