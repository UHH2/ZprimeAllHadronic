from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors,kGreen,kOrange,kSpring,TF1,kAzure
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array
import math

from utils import compare,hadd,doeff,make_plot,make_ratioplot,make_ratioplot2,make_comp,envelope,make_fitplot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/selection/'
prepath='/nfs/dust/cms/user/usaiem/preselection2/'
prepath2='/nfs/dust/cms/user/usaiem/preselection2/'
syspath='/nfs/dust/cms/user/usaiem/sys/'
# path2='/nfs/dust/cms/user/usaiem/phys14-2/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.'
signalHT_names=[
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1500Nar_LH']
signalZT_names=[
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1500Nar_LH']
signalWB_names=[
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1500Nar_LH']

signalWB_thetanames=[
'MZp1507',
'MZp1509',
'MZp1512',
'MZp2009',
'MZp2012',
#'MZp2011',#'MZp2012R',
#'MZp2013',#'MZp2012W',
'MZp2015',
#'MZp2014',#'MZp20W12',
'MZp2512',
'MZp2515']

signalTT_names=[
'MC.MC_TpTp_M-1000',
'MC.MC_TpTp_M-1100',
'MC.MC_TpTp_M-1200',
'MC.MC_TpTp_M-1300',
'MC.MC_TpTp_M-1400',
'MC.MC_TpTp_M-1500',
'MC.MC_TpTp_M-1600',
'MC.MC_TpTp_M-1700',
'MC.MC_TpTp_M-1800',
'MC.MC_TpTp_M-700',
'MC.MC_TpTp_M-800',
'MC.MC_TpTp_M-900'
]
signalTT_thetanames=[
'TpTp1000',
'TpTp1100',
'TpTp1200',
'TpTp1300',
'TpTp1400',
'TpTp1500',
'TpTp1600',
'TpTp1700',
'TpTp1800',
'TpTp700',
'TpTp800',
'TpTp900'
]
signalTT_legendnames=[
"T'T' 1000 GeV",
"T'T' 1100 GeV",
"T'T' 1200 GeV",
"T'T' 1300 GeV",
"T'T' 1400 GeV",
"T'T' 1500 GeV",
"T'T' 1600 GeV",
"T'T' 1700 GeV",
"T'T' 1800 GeV",
"T'T' 700 GeV",
"T'T' 800 GeV",
"T'T' 900 GeV"
]
signalTT_masses=[
'1',
'1p1',
'1p2',
'1p3',
'1p4',
'1p5',
'1p6',
'1p7',
'1p8',
'0p7',
'0p8',
'0p9'
]

signalWB_legendnames=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR(bW)=1",
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrowbW",
"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2.0TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
"Z'(2.0TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrowbW",
"Z'(2.0TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
]

signalHT_legendnames=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR( tH)=1",
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrow tH",
"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrow tH",
"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tH",
"Z'(2.0TeV)#rightarrowT't, T'(0.9TeV)#rightarrow tH",
"Z'(2.0TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tH",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrow tH",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrow tH",
"Z'(2.0TeV)#rightarrowT't, T'(1.5TeV)#rightarrow tH",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrow tH",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tH",
"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrow tH",
]

signalZT_legendnames=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR( tZ)=1",
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrow tZ",
"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrow tZ",
"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tZ",
"Z'(2.0TeV)#rightarrowT't, T'(0.9TeV)#rightarrow tZ",
"Z'(2.0TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tZ",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrow tZ",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrow tZ",
"Z'(2.0TeV)#rightarrowT't, T'(1.5TeV)#rightarrow tZ",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrow tZ",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrow tZ",
"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrow tZ",
]

signal_Zp_masses=[
"1p5",
"1p5",
"1p5",
"2",
"2",
# "2",
# "2",
"2",
# "2W",
"2p5",
"2p5",
]

signal_Tp_masses=[
"0p7",
"0p9",
"1p2",
"0p9",
"1p2",
# "1p2R",
# "1p2W",
"1p5",
# "1p2",
"1p2",
"1p5",
]




signalHT_names_short=[
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp700Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Wid_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1500Nar_LH'
]
signalZT_names_short=[
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp700Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Wid_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1500Nar_LH'
]
signalWB_names_short=[
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp700Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp900Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_RH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Wid_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1500Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1200Nar_LH',
#'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1500Nar_LH'
]
signalWB_legendnames_short=[
"m_{Z'}=1.5 TeV, m_{T'}=0.7 TeV",
#"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrowbW",
#"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
#"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"m_{Z'}=2.0 TeV, m_{T'}=0.9 TeV",
#"Z'(2.0TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrowbW 1pb",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrowbW 1pb",
#"Z'(2TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"m_{Z'}=2.5 TeV, m_{T'}=1.2 TeV",
#"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
#"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
]

signal_Zp_masses_short=[
"1p5",
#"1p5",
#"1p5",
"2",
#"2",
#"2",
#"2",
#"2",
#"2",
"2p5",
#"2p5",
]

signal_Tp_masses_short=[
"0p7",
#"0p9",
#"1p2",
"0p9",
#"1p2",
#1p2",
#1p2",
#"1p5",
#"1p2",
"1p2",
#"1p5",
]

systypes={'mur':'_MUR',
          'muf':'_MUF',
          'murmuf':'_MURMUF',
          'jec':'_JEC',
          'jer':'_JER',
          'pu':'_PU',
          'btag':'_BAK4SF',
#          'subjetbtag':'_BAK8SF',
#          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
          'pdf':'_PDF',
          #'mean':''
          }
systypes2={'mur':'_MUR',
          'muf':'_MUF',
          'murmuf':'_MURMUF',
          'jec':'_JEC',
          'jer':'_JER',
          'pu':'_PU',
          'btag':'_BAK4SF',
#          'subjetbtag':'_BAK8SF',
#          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
          'pdf':'_PDF',
          'mean':''
          }





dotheta=True
if dotheta:
  rebinna=10
  runList=[0,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3500,4000]
  runLen=len(runList)-1
  runArray = array('d',runList)
  u='_'
  uu='__'
  nscan=40
  counter=1
  filecounter=1

 

  for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]+[[0.5,0.25,0.25]]:#+[[0,0,0]]:
    print counter
    filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
    

    theta_config = open('theta3/model'+filename_postfix+'.py','w')
    theta_config.write("def get_model():\n\
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta3/theta"+filename_postfix+".root', include_mc_uncertainties = True)#mc uncertainties=true\n\
    model.fill_histogram_zerobins()\n\
    model.set_signal_processes('signal*')\n\
    #model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')\n\
    #model.add_lognormal_uncertainty('qcd_rate', math.log(1.15), 'qcd')\n\
    for p in model.processes:\n\
        if p == 'qcd':\n\
          model.add_lognormal_uncertainty('qcd_rate', math.log(1.50), p)\n\
        if p == 'qcd': continue\n\
        model.add_lognormal_uncertainty('lumi', math.log(1.027), p)\n\
        model.add_lognormal_uncertainty('trigger', math.log(1.03), p)\n\
        if p == 'ttbar':\n\
          model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), p)\n\
        if p == 'singletop':\n\
          model.add_lognormal_uncertainty('singletop_rate', math.log(1.15), p)\n\
        #if 'signal' in p:\n\
        #    model.add_lognormal_uncertainty(p+'_rate', math.log(1.15), p)\n\
    return model\n\
model = get_model()\n\
model_summary(model)\n\
options = Options()\n\
options.set('main', 'n_threads', '20')\n\
#plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'\n\
plot_exp, plot_obs = bayesian_limits(model,what='observed')#bayesian_limits ,what='expected'\n\
#plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp"+filename_postfix+".txt')\n\
plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs"+filename_postfix+".txt')\n\
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/htmlout"+filename_postfix+"')")
    filecounter+=1



