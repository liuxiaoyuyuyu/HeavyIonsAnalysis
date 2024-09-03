from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException

# We want to put all the CRAB project directories from the tasks we submit here into one common directory.
# That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_('JobType')
config.JobType.pluginName = 'Analysis'

config.section_('Data')
config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.splitting = 'FileBased'
#config.Data.totalUnits = 300
config.Data.unitsPerJob = 3
#config.Data.publication = False
config.JobType.Memory = 3000
#config.JobType.RunTime = 1400
config.JobType.psetName = 'pset_mc.py'
config.JobType.allowUndistributedCMSSW = True
config.Data.allowNonValidInputDataset = True

config.section_('Site')
#config.Data.ignoreLocality = True
#config.Site.whitelist = ['T1_US_*','T2_US_*','T1_FR_*','T2_FR_*','T2_CH_CERN','T2_BE_IIHE']
#config.Site.storageSite = 'T3_US_Rice'
config.Site.storageSite = 'T2_CH_CERN'

def submit(config):
    try:
        crabCommand('submit', config = config, dryrun=False)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

#############################################################################################
## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
#############################################################################################

dataMap = {
#            "MG5-pythia8_HT1500to2000_Run2018": { "PD":  '/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "MG5-pythia8_HT1000to1500_Run2018": { "PD":  '/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Herwig7_Pt15to7000Flat_Run2017": { "PD":  '/QCD_Pt-15to7000_TuneCH3_Flat_13TeV_herwig7/RunIISummer19UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Herwig7_Pt15to7000Flat_Run2018": { "PD":  '/QCD_Pt-15to7000_TuneCH3_Flat_13TeV_herwig7/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
            "Herwig7_Pt150to3000FlatPower7_Run2018": { "PD":  '/QCD_Pt-150to3000_TuneCH3_FlatPower7_13TeV-herwig7/RunIISummer19UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2018": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2018": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2018": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2018": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2018": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2018": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2018": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2017": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2017": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2017": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2017": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2017": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2017": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2017": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2016": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2016": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2016": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2016": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2016": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2016": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2016": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2016APV": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2016APV": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2016APV": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2016APV": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2016APV": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2016APV": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2016APV": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM' },

#            "Pythia8_Pt150to7000_Run2016APV": { "PD":  '/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'},
#            "Pythia8_Pt150to7000_Run2016": { "PD":  '/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM' },
#            "Pythia8_Pt150to7000_Run2017": { "PD":  '/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM' },
#            "Pythia8_Pt150to7000_Run2018": { "PD":  '/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2018": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2018": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2018": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2018": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2018": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2018": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2018": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },
#            "Pythia8_Pt3200toInf_Run2018": { "PD":  '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2017": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2017": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2017": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2017": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2017": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2017": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2017": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },
#            "Pythia8_Pt3200toInf_Run2017": { "PD":  '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL17MiniAOD-106X_mc2017_realistic_v6-v2/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2016": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2016": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2016": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2016": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2016": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2016": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2016": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },
#            "Pythia8_Pt3200toInf_Run2016": { "PD":  '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM' },

#            "Pythia8_Pt470to600_Run2016APV": { "PD":  '/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt600to800_Run2016APV": { "PD":  '/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt800to1000_Run2016APV": { "PD":  '/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt1000to1400_Run2016APV": { "PD":  '/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt1400to1800_Run2016APV": { "PD":  '/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt1800to2400_Run2016APV": { "PD":  '/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt2400to3200_Run2016APV": { "PD":  '/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },
#            "Pythia8_Pt3200toInf_Run2016APV": { "PD":  '/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPV-106X_mcRun2_asymptotic_preVFP_v8-v2/MINIAODSIM' },

          }

## Submit the JeHT PDs
for key, val in dataMap.items():
    config.General.requestName = 'JetTrees_PFJetsAK8_'+key+'_MiniAODv2_20220529_v1'
#    config.General.requestName = 'JetTrees_PFJetsAK8_'+key+'_MiniAODv1_20220529_v1'
    config.Data.inputDataset = val["PD"]
    config.Data.outputDatasetTag = config.General.requestName
#    config.Data.outLFNDirBase = '/store/user/davidlw/'
    config.Data.outLFNDirBase = '/store/group/phys_heavyions/flowcorr/'

    print("Submitting CRAB job for: "+val["PD"])
    submit(config)
