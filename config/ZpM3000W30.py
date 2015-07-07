from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'ZpM3000W30_test'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_3/src/UHH2/core/python/ntuplewriter.py'
config.JobType.outputFiles = ["Ntuple.root"]

config.Data.inputDataset = '/ZprimeToTT_M-3000_W-30_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/eusai/' # % (getUsernameFromSiteDB())
config.Data.publication = False
#config.Data.publishDataName = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = 'T2_DE_DESY'
