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
        "root://cmsxrootd.fnal.gov//store/data/Run2023C/JetMET0/MINIAOD/PromptReco-v4/000/367/770/00000/47952325-f71b-44d3-979e-b2aa2ff17cbf.root"
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
process.hlt500 = process.hlt.clone()
process.hlt450 = process.hlt.clone()
process.hlt400 = process.hlt.clone()
process.hlt320 = process.hlt.clone()
process.hlt260 = process.hlt.clone()
process.hlt450.HLTPaths = ['HLT_AK8PFJet450_v*']
process.hlt400.HLTPaths = ['HLT_AK8PFJet400_v*']
process.hlt320.HLTPaths = ['HLT_AK8PFJet320_v*']
process.hlt260.HLTPaths = ['HLT_AK8PFJet260_v*']
process.eventFilterHLT500 = cms.Sequence(process.hlt500)
process.eventFilterHLT450 = cms.Sequence(process.hlt450)
process.eventFilterHLT400 = cms.Sequence(process.hlt400)
process.eventFilterHLT320 = cms.Sequence(process.hlt320)
process.eventFilterHLT260 = cms.Sequence(process.hlt260)

process.analyzer = cms.EDAnalyzer('TrackAnalyzer',
    doTrack = cms.untracked.bool(False),
    trackPtMin = cms.untracked.double(0.01),
    vertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    packedCandSrc = cms.InputTag("packedPFCandidates"),
    lostTracksSrc = cms.InputTag("lostTracks"),
    beamSpotSrc = cms.untracked.InputTag('offlineBeamSpot'),
    #jets2 = cms.InputTag("slimmedJets")
    #jets2 = cms.InputTag('slimmedJetsPuppi')
    jets2 = cms.InputTag('slimmedJetsAK8')
    #jets2 = cms.InputTag("slimmedJetsAK8PFPuppiSoftDropPacked")
)
process.analyzer500 = process.analyzer.clone()
process.analyzer450 = process.analyzer.clone()
process.analyzer400 = process.analyzer.clone()
process.analyzer320 = process.analyzer.clone()
process.analyzer260 = process.analyzer.clone()

# main forest sequence
process.runAnalyzer500 = cms.Path(
    process.eventFilterHLT500 *
    process.analyzer500
    )

process.runAnalyzer450 = cms.Path(
    process.eventFilterHLT450 *
    process.analyzer450
    )

process.runAnalyzer400 = cms.Path(
    process.eventFilterHLT400 *
    process.analyzer400
    )

process.runAnalyzer320 = cms.Path(
    process.eventFilterHLT320 *
    process.analyzer320
    )

process.runAnalyzer260 = cms.Path(
    process.eventFilterHLT260 *
    process.analyzer260
    )
