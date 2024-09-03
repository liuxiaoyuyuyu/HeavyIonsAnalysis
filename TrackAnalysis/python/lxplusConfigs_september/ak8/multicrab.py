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
config.Data.splitting = 'LumiBased'
#config.Data.totalUnits = 300
config.Data.unitsPerJob = 300
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt'
#config.Data.publication = False
config.JobType.Memory = 3500
#config.JobType.RunTime = 1400
config.JobType.psetName = 'pset.py'
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
#            "Run2016Bv1": { "PD":  '/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016Bv2": { "PD":  '/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016C": { "PD":  '/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016D": { "PD":  '/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016E": { "PD":  '/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016F-HIPM": { "PD":  '/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016F": { "PD":  '/JetHT/Run2016F-UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016G": { "PD":  '/JetHT/Run2016G-UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2016H": { "PD":  '/JetHT/Run2016H-UL2016_MiniAODv2-v2/MINIAOD' },
#            "Run2017B": { "PD":  '/JetHT/Run2017B-UL2017_MiniAODv2-v1/MINIAOD' },
#            "Run2017C": { "PD":  '/JetHT/Run2017C-UL2017_MiniAODv2-v1/MINIAOD' },
#            "Run2017D": { "PD":  '/JetHT/Run2017D-UL2017_MiniAODv2-v1/MINIAOD' },
#            "Run2017E": { "PD":  '/JetHT/Run2017E-UL2017_MiniAODv2-v1/MINIAOD' },
#            "Run2017F": { "PD":  '/JetHT/Run2017F-UL2017_MiniAODv2-v1/MINIAOD' },
#            "Run2018A": { "PD":  '/JetHT/Run2018A-UL2018_MiniAODv2-v1/MINIAOD' },
#            "Run2018B": { "PD":  '/JetHT/Run2018B-UL2018_MiniAODv2-v1/MINIAOD' },
#            "Run2018C": { "PD":  '/JetHT/Run2018C-UL2018_MiniAODv2-v1/MINIAOD' },
#            "Run2018D": { "PD":  '/JetHT/Run2018D-UL2018_MiniAODv2-v2/MINIAOD' }
            "Run2016Bv1": { "PD":  '/JetHT/Run2016B-21Feb2020_ver1_UL2016_HIPM-v1/MINIAOD' },
            "Run2016Bv2": { "PD":  '/JetHT/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/MINIAOD' },
            "Run2016C": { "PD":  '/JetHT/Run2016C-21Feb2020_UL2016_HIPM-v1/MINIAOD' },
            "Run2016D": { "PD":  '/JetHT/Run2016D-21Feb2020_UL2016_HIPM-v1/MINIAOD' },
            "Run2016E": { "PD":  '/JetHT/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD' },
            "Run2016F": { "PD":  '/JetHT/Run2016F-21Feb2020_UL2016-v1/MINIAOD' },
            "Run2016F-HIPM": { "PD":  '/JetHT/Run2016F-21Feb2020_UL2016_HIPM-v1/MINIAOD' },
            "Run2016G": { "PD":  '/JetHT/Run2016G-21Feb2020_UL2016-v1/MINIAOD' },
            "Run2016H": { "PD":  '/JetHT/Run2016H-21Feb2020_UL2016-v1/MINIAOD' },
#            "Run2017B": { "PD":  '/JetHT/Run2017B-09Aug2019_UL2017-v1/MINIAOD' },
#            "Run2017C": { "PD":  '/JetHT/Run2017C-09Aug2019_UL2017-v1/MINIAOD' },
#            "Run2017D": { "PD":  '/JetHT/Run2017D-09Aug2019_UL2017-v1/MINIAOD' },
#            "Run2017E": { "PD":  '/JetHT/Run2017E-09Aug2019_UL2017-v1/MINIAOD' },
#            "Run2017F": { "PD":  '/JetHT/Run2017F-09Aug2019_UL2017-v1/MINIAOD' },
#            "Run2018A": { "PD":  '/JetHT/Run2018A-12Nov2019_UL2018-v2/MINIAOD' },
#            "Run2018B": { "PD":  '/JetHT/Run2018B-12Nov2019_UL2018-v2/MINIAOD' },
#            "Run2018C": { "PD":  '/JetHT/Run2018C-12Nov2019_UL2018_rsb-v1/MINIAOD' },
#            "Run2018D": { "PD":  '/JetHT/Run2018D-12Nov2019_UL2018-v5/MINIAOD' }
            }

## Submit the JeHT PDs
for key, val in dataMap.items():
    config.General.requestName = 'JetTrees_PFJetsAK8_'+key+'_MiniAODv1_20220529_v1'
    config.Data.inputDataset = val["PD"]
    config.Data.outputDatasetTag = config.General.requestName
#    config.Data.outLFNDirBase = '/store/user/davidlw/'
    config.Data.outLFNDirBase = '/store/group/phys_heavyions/flowcorr/'

    print("Submitting CRAB job for: "+val["PD"])
    submit(config)
