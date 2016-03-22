from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors,kGreen,kOrange,kSpring,kAzure
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array

from utils import compare,hadd,doeff,make_plot,make_ratioplot,make_ratioplot2,make_comp,envelope
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
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrowbW",
"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
"Z'(2TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrowbW 1pb",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
]

signal_Zp_masses=[
"1p5",
"1p5",
"1p5",
"2",
"2",
#"2",
#"2",
"2",
#"2",
"2p5",
"2p5",
]

signal_Tp_masses=[
"0p7",
"0p9",
"1p2",
"0p9",
"1p2",
#1p2",
#1p2",
"1p5",
#"1p2",
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
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrowbW",
#"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
#"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
"Z'(2TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrowbW 1pb",
#"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrowbW 1pb",
#"Z'(2TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW",
#"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW",
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
          'subjetbtag':'_BAK8SF',
#          'ttbar':'_TTBAR',
          'toptag':'_TSF',
          'wtag':'_WSF',
          #'pdf':'_PDF',
          #'mean':''
          }



#signal_names=signalWB_names+signalHT_names+signalZT_names
qcd_names=['MC.QCD_HT500to700','MC.QCD_HT700to1000','MC.QCD_HT1000to1500','MC.QCD_HT1500to2000','MC.QCD_HT2000toInf']
ttbar_names=['MC.TTbar']
ttbarhigh_names=['MC.TT_Mtt0700to1000','MC.TT_Mtt1000toINFT']
data_names=['DATA.JetHT_Run2015D_05Oct2015_v1','DATA.JetHT_Run2015D_PromptReco_v4']
# ttbar50ns_name='TTbar50ns'
outfile=TFile('outfile.root','RECREATE')


#merge
force=True
merge=True
qcd_filename=hadd(path,filename_base,qcd_names,'qcd_added',force,merge)
ttbar_filename=hadd(path,filename_base,ttbar_names,'ttbar_added',force,merge)
data_filename=hadd(path,filename_base,data_names,'data_added',force,merge)
#open files
qcd_file=TFile(qcd_filename,'READ')
ttbar_file=TFile(ttbar_filename,'READ')
data_file=TFile(data_filename,'READ')
signal_files=[]
signal_files_pre=[]
signal_files_short=[]
for i in signalWB_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))
for i in signalWB_names_short:
	signal_files_short.append(TFile(path+filename_base+i+root,'READ'))
for i in signalWB_names:
	signal_files_pre.append(TFile(prepath+filename_base+i+root,'READ'))
signalTT_files=[]
signal_files_pre2=[]
for i in signalTT_names:
	signalTT_files.append(TFile(prepath2+filename_base+i+root,'READ'))
for i in signalWB_names:
	signal_files_pre2.append(TFile(prepath2+filename_base+i+root,'READ'))
signalTTreco_files=[]
for i in signalTT_names:
	signalTTreco_files.append(TFile(path+filename_base+i+root,'READ'))

for i in ["N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR",
  "bmass",  "bpt",  "bcsv","csv_pthighest","csv_csvhighest",
  "wmass",  "wpt",  "wnsub",
  "toppt",  "topmass",  "topnsub",  "topcsv",
  "dRbt",  "dRbW",  "dRtW",  "dRtTp",
  "ht",  "htca8",  "ht_twb",  "npv",  "nevt",
  "toppt_wpt",  "toppt_wbpt","ht_twbSR","ht_twbSRbtag","ht_twbSRnobtag",
  "tprimemass",  "tprimept","Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub",
  "zprimemass",  "zprimept",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  "ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag","ttbarCR_zprimemass_low",  "ttbarCR_zprimemassbtag_low",
  "lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag","lowmassCR_zprimemass_low",  "lowmassCR_zprimemassbtag_low",
  #"antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",
    "antibcsvCR_zprimemass",
  #    "antibptCR_zprimemass",  "antibmassCR_zprimemass",
#"antitopmassCRmass_zprimemass",  "antitopnsubCRmass_zprimemass",  "antiwmassCRmass_zprimemass",  "antiwnsubCRmass_zprimemass",  
"antibcsvCRmass_zprimemass",
#  "antibptCRmass_zprimemass",  "antibmassCRmass_zprimemass",
#"antitopmassCRbtag_zprimemass",  "antitopnsubCRbtag_zprimemass",  "antiwmassCRbtag_zprimemass",  "antiwnsubCRbtag_zprimemass",  
"antibcsvCRbtag_zprimemass",
#  "antibptCRbtag_zprimemass",  "antibmassCRbtag_zprimemass",
#"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass",
  "antibcsvCRnobtag_zprimemass",
  #  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
"bkg1","bkg2","bkg12","bkg1up","bkg2up","bkg12up","bkg1down","bkg2down","bkg12down","tprimemass_res", "zprimemassbtag_res", "zprimemassnobtag_res",
'topmass_res','topmass2_res',

"tprimemassbtag","tprimemassnobtag","tprimemassbtagmass","tprimemassnobtagmass","antibcsvCRbtag_tprimemass","antibcsvCRnobtag_tprimemass",
"antibcsvCRbtagmass_tprimemass","antibcsvCRnobtagmass_tprimemass","antibcsvCRbtag_ht_twb","antibcsvCRnobtag_ht_twb",

"ttbarCR_zprimemassnobtag","lowmassCR_zprimemassnobtag","ttbarCR_zprimemassnobtag_low","lowmassCR_zprimemassnobtag_low",
"CA15_zprimemassbtag","CA15_ht_twbSRbtag","CA15_tprimemassbtag",

"CA15_zprimemassnobtag","CA15_ht_twbSRnobtag","CA15_tprimemassnobtag",

"CA15_ttbarCR_zprimemassnobtag","CA15_ttbarCR_zprimemassbtag",
"CA15_lowmassCR_zprimemassnobtag","CA15_lowmassCR_zprimemassbtag",

"CA15_zprimemassbtag_low","CA15_ht_twbSRbtag_low","CA15_tprimemassbtag_low",

"CA15_zprimemassnobtag_low","CA15_ht_twbSRnobtag_low","CA15_tprimemassnobtag_low",

"CA15_ttbarCR_zprimemassnobtag_low","CA15_ttbarCR_zprimemassbtag_low",
"CA15_lowmassCR_zprimemassnobtag_low","CA15_lowmassCR_zprimemassbtag_low",
"index_toptag","index_wtag","index_wtag1","index_wtag2",
]:
  rebinna=10
  uselog=True
  signalzoom=1
  minx=0
  maxx=0
  if 'topmass' in i and '_' not in i:
    minx=60
    maxx=300
  if 'wmass' in i and '_' not in i:
    minx=60
    maxx=300
  if i in ["index_toptag","index_wtag","index_wtag1","index_wtag2","N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR","bcsv","csv_pthighest","csv_csvhighest", "topcsv",]:
    rebinna=1
  if i in ["Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub",]:
    rebinna =2
  if i in ["N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR",
  "bmass",  "bpt",  "bcsv","csv_pthighest","csv_csvhighest",
  "wmass",  "wpt",  "wnsub",
  "toppt",  "topmass",  "topnsub",  "topcsv",
  "dRbt",  "dRbW",  "dRtW",  "dRtTp",
  "ht",  "htca8",  "ht_twb",  "npv",  "nevt",]:
    signalzoom=100
  if i in ["Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub"]:
    signalzoom=20
  if i in ["tprimemass"]:
    signalzoom=20
  if i in ['topmass_res','topmass2_res']:
    signalzoom=30
    rebinna=1
    uselog=False
    minx=60
    maxx=300
  # make_ratioplot(
  #   name=i+'NOSF',
  #   ttbar_file=ttbar_file,
  #   qcd_file=qcd_file,
  #   data_file=data_file,
  #   signal_files=signal_files_short,
  #   histo='Selection/'+i, 
  #   histo_qcd='Selection/'+i,
  #   histo_signal='Selection/'+i,
  #   rebin=rebinna,
  #   minx=minx,
  #   maxx=maxx,
  #   miny=0,
  #   maxy=0,
  #   minratio=0,
  #   maxratio=0,
  #   logy=uselog,
  #       xtitle='',
  #       ytitle='Events',
  #       textsizefactor=1,
  #       signal_legend=signalWB_legendnames_short,
  #       separate_legend=True,
  #       signal_zoom=signalzoom,
  #       fixratio=True,
  #       signal_colors=[kOrange+10,kAzure+1,kSpring-6])

  make_ratioplot(
		name=i,
		ttbar_file=ttbar_file,
		qcd_file=qcd_file,
		data_file=data_file,
		signal_files=signal_files_short,
		histo='Selection/'+i, 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=uselog,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        #dosys=True,
        sysdict=systypes)

  make_ratioplot(
    name=i+'_NOLOG',
    ttbar_file=ttbar_file,
    qcd_file=qcd_file,
    data_file=data_file,
    signal_files=signal_files_short,
    histo='Selection/'+i, 
    histo_qcd='Selection/'+i,
    histo_signal='Selection/'+i,
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        #dosys=True,
        sysdict=systypes)

  make_ratioplot(
    name=i+'_ALL',
    ttbar_file=ttbar_file,
    qcd_file=qcd_file,
    data_file=data_file,
    signal_files=signal_files,
    histo='Selection/'+i, 
    histo_qcd='Selection/'+i,
    histo_signal='Selection/'+i,
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=uselog,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        #dosys=True,
        sysdict=systypes)
  make_ratioplot(
    name=i+'_TT',
    ttbar_file=ttbar_file,
    qcd_file=qcd_file,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo='Selection/'+i, 
    histo_qcd='Selection/'+i,
    histo_signal='Selection/'+i,
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=uselog,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        #dosys=True,
        sysdict=systypes)
  make_ratioplot(
    name=i+'_TTNOLOG',
    ttbar_file=ttbar_file,
    qcd_file=qcd_file,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo='Selection/'+i, 
    histo_qcd='Selection/'+i,
    histo_signal='Selection/'+i,
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        #dosys=True,
        sysdict=systypes)





for i in ["N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR",
  "bmass",  "bpt",  "bcsv","csv_pthighest","csv_csvhighest",
  "wmass",  "wpt",  "wnsub",
  "toppt",  "topmass",  "topnsub",  "topcsv",
  "dRbt",  "dRbW",  "dRtW",  "dRtTp",
  "ht",  "htca8",  "ht_twb",  "npv",  "nevt",
  "toppt_wpt",  "toppt_wbpt","ht_twbSR","ht_twbSRbtag","ht_twbSRnobtag",
  "tprimemass",  "tprimept","Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub",
  "zprimemass",  "zprimept",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass","tprimemass_res", "zprimemassbtag_res", "zprimemassnobtag_res",
  "tprimemassbtag","tprimemassnobtag","tprimemassbtagmass","tprimemassnobtagmass","antibcsvCRbtag_tprimemass","antibcsvCRnobtag_tprimemass",
  "antibcsvCRbtagmass_tprimemass","antibcsvCRnobtagmass_tprimemass","antibcsvCRbtag_ht_twb","antibcsvCRnobtag_ht_twb",
  "TT1btag_tprimemass",  "TT1btag_tprimemass1",  "TT1btag_tprimemass2",  "TT1btag_tprimept",  "TT1btag_tprimept1",  "TT1btag_tprimept2",  "TT1btag_mass",  "TT1btag_dmass",  "TT1btag_dmassomass",  "TT1btag_htak8",  "TT1btag_htak8ak4",  "TT1btag_smass",  "TT1btag_pt",
  "TT2btag_tprimemass",  "TT2btag_tprimemass1",  "TT2btag_tprimemass2",  "TT2btag_tprimept",  "TT2btag_tprimept1",  "TT2btag_tprimept2",  "TT2btag_mass",  "TT2btag_dmass",  "TT2btag_dmassomass",  "TT2btag_htak8",  "TT2btag_htak8ak4",  "TT2btag_smass",  "TT2btag_pt",
  #"TT1btag1Tp_tprimemass",  "TT1btag1Tp_tprimemass1",  "TT1btag1Tp_tprimemass2",  "TT1btag1Tp_tprimept",  "TT1btag1Tp_tprimept1",  "TT1btag1Tp_tprimept2",  "TT1btag1Tp_mass",  "TT1btag1Tp_dmass",  "TT1btag1Tp_dmassomass",  "TT1btag1Tp_htak8",  "TT1btag1Tp_htak8ak4",  "TT1btag1Tp_smass",  "TT1btag1Tp_pt",
  #"TT2btag1Tp_tprimemass",  "TT2btag1Tp_tprimemass1",  "TT2btag1Tp_tprimemass2",  "TT2btag1Tp_tprimept",  "TT2btag1Tp_tprimept1",  "TT2btag1Tp_tprimept2",  "TT2btag1Tp_mass",  "TT2btag1Tp_dmass",  "TT2btag1Tp_dmassomass",  "TT2btag1Tp_htak8",  "TT2btag1Tp_htak8ak4",  "TT2btag1Tp_smass",  "TT2btag1Tp_pt",
  #"TTbar1btag_tprimemass",  "TTbar1btag_tprimemass1",  "TTbar1btag_tprimemass2",  "TTbar1btag_tprimept",  "TTbar1btag_tprimept1",  "TTbar1btag_tprimept2",  "TTbar1btag_mass",  "TTbar1btag_dmass",  "TTbar1btag_dmassomass",  "TTbar1btag_htak8",  "TTbar1btag_htak8ak4",  "TTbar1btag_smass",  "TTbar1btag_pt",
  #"TTbar2btag_tprimemass",  "TTbar2btag_tprimemass1",  "TTbar2btag_tprimemass2",  "TTbar2btag_tprimept",  "TTbar2btag_tprimept1",  "TTbar2btag_tprimept2",  "TTbar2btag_mass",  "TTbar2btag_dmass",  "TTbar2btag_dmassomass",  "TTbar2btag_htak8",  "TTbar2btag_htak8ak4",  "TTbar2btag_smass",  "TTbar2btag_pt",
  #"TTbar1btag1Tp_tprimemass",  "TTbar1btag1Tp_tprimemass1",  "TTbar1btag1Tp_tprimemass2",  "TTbar1btag1Tp_tprimept",  "TTbar1btag1Tp_tprimept1",  "TTbar1btag1Tp_tprimept2",  "TTbar1btag1Tp_mass",  "TTbar1btag1Tp_dmass",  "TTbar1btag1Tp_dmassomass",  "TTbar1btag1Tp_htak8",  "TTbar1btag1Tp_htak8ak4",  "TTbar1btag1Tp_smass",  "TTbar1btag1Tp_pt",
  #"TTbar2btag1Tp_tprimemass",  "TTbar2btag1Tp_tprimemass1",  "TTbar2btag1Tp_tprimemass2",  "TTbar2btag1Tp_tprimept",  "TTbar2btag1Tp_tprimept1",  "TTbar2btag1Tp_tprimept2",  "TTbar2btag1Tp_mass",  "TTbar2btag1Tp_dmass",  "TTbar2btag1Tp_dmassomass",  "TTbar2btag1Tp_htak8",  "TTbar2btag1Tp_htak8ak4",  "TTbar2btag1Tp_smass",  "TTbar2btag1Tp_pt"
  ]:
#i=''
	rebinna=10
	signalzoom=1
	minx=0
	maxx=0
	if 'topmass' in i and '_' not in i:
		minx=60
		maxx=300
	if 'wmass' in i and '_' not in i:
		minx=60
		maxx=300
	if i in ["N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR","bcsv","csv_pthighest","csv_csvhighest", "topcsv",]:
		rebinna=1
	if i in ["Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub",]:
		rebinna =2
	if i in ["N_toptags",  "N_wtags", "Pos_toptags",  "Pos_wtags",  "N_btags", "N_btags_good",  "N_subjetbtags", "N_btags_ttbarCR", "N_btags_good_ttbarCR",
  "bmass",  "bpt",  "bcsv","csv_pthighest","csv_csvhighest",
  "wmass",  "wpt",  "wnsub",
  "toppt",  "topmass",  "topnsub",  "topcsv",
  "dRbt",  "dRbW",  "dRtW",  "dRtTp",
  "ht",  "htca8",  "ht_twb",  "npv",  "nevt",]:
  		signalzoom=100
  	if i in ["Nm1wmass","Nm1wnsub","Nm1topmass","Nm1topnsub"]:
  		signalzoom=20
  	#if i in ["tprimemass"]:
  	#	signalzoom=20
	make_ratioplot(
		name='TT_'+i,
		ttbar_file=ttbar_file,
		qcd_file=qcd_file,
		data_file=data_file,
		signal_files=signalTTreco_files,
		histo='Selection/'+i, 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6]
        )





for i in [
  #"zprimemass",#,  "zprimemassbtag",  "zprimemassnobtag"#,  "zprimemassbmass",  "zprimemassnobmass",
  #"ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  #"lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  #"antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass", 
   #"antibcsvCR_zprimemass",
   #  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
#"ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 #"antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 "antibcsvCRmass_zprimemass",
 # "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 #"antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 #"antibcsvCRbtag_zprimemass", 
 #"antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
#"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass",
 # "antibcsvCRnobtag_zprimemass",
  #  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
  #"bkg1","bkg2",
  "bkg12",
  #"bkg1up","bkg2up",
  "bkg12up",
  #"bkg1down","bkg2down",
  "bkg12down",]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot2(
		name='SR_vs_'+i,
		ttbar_file=0,
		qcd_file=qcd_file,
		data_file=qcd_file,
		signal_files=[],
		histo='Selection/zprimemass', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Control region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )
	gStyle.SetOptFit(1111)
	ratio_to_fit=qcd_file.Get('Selection/zprimemass').Clone('ratio_SR_vs_'+i)
	denominator_CR=qcd_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SR_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SR_vs_'+i+'_c.pdf')

	make_ratioplot2(
		name='SRdata_vs_'+i,
		ttbar_file=0,
		qcd_file=data_file,
		data_file=data_file,
		signal_files=[],
		histo='Selection/zprimemass', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Control region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )
	gStyle.SetOptFit(1111)
	ratio_to_fit=data_file.Get('Selection/zprimemass').Clone('ratio_SRdata_vs_'+i)
	denominator_CR=data_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Add(ttbar_file.Get('Selection/zprimemass'),-1.0)
	denominator_CR.Add(ttbar_file.Get('Selection/'+i),-1.0)
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SRdata_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SRdata_vs_'+i+'_c.pdf')

for i in [
  #"zprimemass",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  #"ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  #"lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  #"antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",
   # "antibcsvCR_zprimemass",#  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
  #"ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 #"antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 #"antibcsvCRmass_zprimemass",# "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 #"antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 "antibcsvCRbtag_zprimemass","antibcsvlooseCRbtag_zprimemass",# "antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
#"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass", 
 #"antibcsvCRnobtag_zprimemass",#  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
 #"bkg1",
 "bkg2",
 #"bkg12","bkg1up",
 "bkg2up",
 #"bkg12up","bkg1down",
 "bkg2down"#,"bkg12down",
 ]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot2(
		name='SRbtag_vs_'+i,
		ttbar_file=0,
		qcd_file=qcd_file,
		data_file=qcd_file,
		signal_files=[],
		histo='Selection/zprimemassbtag', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Control region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

	gStyle.SetOptFit(1111)
	ratio_to_fit=qcd_file.Get('Selection/zprimemassbtag').Clone('ratio_SRbtag_vs_'+i)
	denominator_CR=qcd_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SRbtag_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SRbtag_vs_'+i+'_c.pdf')

	make_ratioplot2(
		name='SRbtagdata_vs_'+i,
		ttbar_file=0,
		qcd_file=data_file,
		data_file=data_file,
		signal_files=[],
		histo='Selection/zprimemassbtag', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Control region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

	gStyle.SetOptFit(1111)
	ratio_to_fit=data_file.Get('Selection/zprimemassbtag').Clone('ratio_SRbtagdata_vs_'+i)
	denominator_CR=data_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Add(ttbar_file.Get('Selection/zprimemassbtag'),-1.0)
	denominator_CR.Add(ttbar_file.Get('Selection/'+i),-1.0)
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SRbtagdata_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SRbtagdata_vs_'+i+'_c.pdf')


for i in [
  #"zprimemass",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  #"ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  #"lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  #"antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",
   # "antibcsvCR_zprimemass",  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
  #"ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 #"antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 #"antibcsvCRmass_zprimemass",# "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 #"antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 #"antibcsvCRbtag_zprimemass",# "antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
#"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass", 
 "antibcsvCRnobtag_zprimemass", "antibcsvlooseCRnobtag_zprimemass",# "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
 "bkg1",#"bkg2","bkg12",
 "bkg1up",#"bkg2up","bkg12up",
 "bkg1down",#"bkg2down","bkg12down",
 ]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot2(
		name='SRnobtag_vs_'+i,
		ttbar_file=0,
		qcd_file=qcd_file,
		data_file=qcd_file,
		signal_files=[],
		histo='Selection/zprimemassnobtag', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Corrected sideband region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

	gStyle.SetOptFit(1111)
	ratio_to_fit=qcd_file.Get('Selection/zprimemassnobtag').Clone('ratio_SRnobtag_vs_'+i)
	denominator_CR=qcd_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SRnobtag_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SRnobtag_vs_'+i+'_c.pdf')

	make_ratioplot2(
		name='SRnobtagdata_vs_'+i,
		ttbar_file=0,
		qcd_file=data_file,
		data_file=data_file,
		signal_files=[],
		histo='Selection/zprimemassnobtag', 
		histo_qcd='Selection/'+i,
		histo_signal='Selection/'+i,
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=2,
        fixratio=True,
        normalize=True,
        qcd_legend='Control region (QCD MC)',
        data_legend='Signal region (QCD MC)'
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

	gStyle.SetOptFit(1111)
	ratio_to_fit=data_file.Get('Selection/zprimemassnobtag').Clone('ratio_SRnobtagdata_vs_'+i)
	denominator_CR=data_file.Get('Selection/'+i).Clone()
	outfile.cd()
	ratio_to_fit.Add(ttbar_file.Get('Selection/zprimemassnobtag'),-1.0)
	denominator_CR.Add(ttbar_file.Get('Selection/'+i),-1.0)
	ratio_to_fit.Rebin(30)
	denominator_CR.Rebin(30)
	ratio_to_fit.Scale(1.0/(ratio_to_fit.Integral()+0.000001))
	denominator_CR.Scale(1.0/(denominator_CR.Integral()+0.000001))
	ratio_to_fit.Divide(denominator_CR)
	ratioc=TCanvas('ratio_SRnobtagdata_vs_'+i+'_c')
	ratio_to_fit.Draw()
	ratio_to_fit.Fit('pol1','','',900,3000)
	ratio_to_fit.GetXaxis().SetRangeUser(900,3000)
	ratio_to_fit.Draw()
	ratio_to_fit.Write()
	ratioc.Write()
	ratioc.SaveAs('pdf/ratio_SRnobtagdata_vs_'+i+'_c.pdf')


for i in ["pTtop",  "pTtprime",  "pTb",  "pTw",  "pTtb",  "pTtw",  "pTzprime",
  "ptop",  "ptprime",  "pb",  "pw",  "ptb",  "ptw",  "pzprime",
  "mtop",  "mtprime",  "mb",  "mw",  "mtb",  "mtw",  "mzprime",
  "dRbW",  "dRtT",  "dRbt",  "dRtW",  "dR_tb_tW",  "dR_tb_W",  "dR_tb_b",  "dR_b_tW",  "dR_W_tW",
  "dR_W1_b1",  "dR_W2_b2",  "dR_W1_W2",  "dR_b1_b2",  "dR_W1_b2",  "dR_W2_b1",
  "pT_closest_topjet_to_top",  "mass_closest_topjet_to_top",  "nsub_closest_topjet_to_top",
  "pT_closest_topjet_to_tprime",  "mass_closest_topjet_to_tprime",  "nsub_closest_topjet_to_tprime",
  "pT_closest_wjet_to_w",  "mass_closest_wjet_to_w",  "nsub_closest_wjet_to_w",
  "pT_closest_bjet_to_b",  "csv_closest_bjet_to_b",

  "pT_closest_wjet_to_tw",  "mass_closest_wjet_to_tw",  "nsub_closest_wjet_to_tw",
  "pT_closest_bjet_to_tb",  "csv_closest_bjet_to_tb",

  "pT_closest_wjet_to_w1",  "mass_closest_wjet_to_w1",  "nsub_closest_wjet_to_w1",
  "pT_closest_bjet_to_b1",  "csv_closest_bjet_to_b1",
  "pT_closest_wjet_to_w2",  "mass_closest_wjet_to_w2",  "nsub_closest_wjet_to_w2",
  "pT_closest_bjet_to_b2",  "csv_closest_bjet_to_b2",
  "matched_top_mass",
  "matched_top_res_mass",
  "matched_tprime_mass",
  "matched_zprime_mass",
  "matched_zprime_res_mass",
  "matched_tprime1_mass",
  "matched_tprime2_mass",
  ]:
  rebinna=1
  minx=0
  maxx=0
  if 'top_mass' in i or 'mass_closest_wjet' in i or 'mass_closest_topjet' in i or 'top_res_mass' in i:
     minx=0
     maxx=300
  compare(name='GEN_'+i,#signalWB_names[i]+'dRbW',
		file_list=signal_files_pre2,#[signal_files[i],signal_files_pre[i]],
		name_list=['NoCuts/'+i]*len(signal_files_pre2),
		legend_list=signalWB_legendnames,
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=minx,maxx=maxx,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)
  compare(name='GENTT_'+i,#signalWB_names[i]+'dRbW',
		file_list=signalTT_files,#[signal_files[i],signal_files_pre[i]],
		name_list=['NoCuts/'+i]*len(signal_files),
		legend_list=signalTT_legendnames,
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=minx,maxx=maxx,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

for i in range(len(signalWB_names)):
	rebinna=10
	compare(name=signalWB_names[i]+'dRbW',
		file_list=[signal_files[i],signal_files_pre[i]],
		name_list=['Selection/dRbW','NoCuts/dRbW'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRtT',
		file_list=[signal_files[i],signal_files_pre[i]],
		name_list=['Selection/dRtTp','NoCuts/dRtT'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRbt',
		file_list=[signal_files[i],signal_files_pre[i]],
		name_list=['Selection/dRbt','NoCuts/dRbt'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRtW',
		file_list=[signal_files[i],signal_files_pre[i]],
		name_list=['Selection/dRtW','NoCuts/dRtW'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)




	compare(name=signalWB_names[i]+'dRbWSAME',
		file_list=[signal_files[i],signal_files[i]],
		name_list=['Selection/dRbW','Selection/dRbWGEN'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRtTSAME',
		file_list=[signal_files[i],signal_files[i]],
		name_list=['Selection/dRtTp','Selection/dRtTpGEN'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRbtSAME',
		file_list=[signal_files[i],signal_files[i]],
		name_list=['Selection/dRbt','Selection/dRbtGEN'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

	compare(name=signalWB_names[i]+'dRtWSAME',
		file_list=[signal_files[i],signal_files[i]],
		name_list=['Selection/dRtW','Selection/dRtWGEN'],
		legend_list=['RECO','GEN'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=rebinna,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)





# for i in ['step1_wmass','step1_wnsub','step1_tcsv','step1_tpt','step2_bcsv','step2_wpt','step3_tprimemass','step3_tprimept','step4_zprimemass','step4_zprimemassbtag','step4_zprimemassbtagnsub']:
# 	make_plot(i, ttbar_file, qcd_file, data_file, signal_files, 'Preselection/'+i,'Preselection/'+i,'PreselectionAllHad/'+i,rebin=rebinna,minx=500,maxx=4000    ,logy=True)#,miny=0.1,maxy=10000
# 	make_plot(i+'_nolog', ttbar_file, qcd_file, data_file, signal_files, 'Preselection/'+i,'Preselection/'+i,'PreselectionAllHad/'+i,rebin=rebinna,minx=500,maxx=4000     ,logy=False)#,miny=0.1,maxy=50

# 	make_ratioplot(
# 		name=i,
# 		ttbar_file=ttbar_file,
# 		qcd_file=qcd_file,
# 		data_file=data_file,
# 		signal_files=signal_files,
# 		histo='Preselection/'+i, 
# 		histo_qcd='Preselection/'+i,
# 		histo_signal='Preselection/'+i,
# 		rebin=rebinna,
# 		minx=0,
# 		maxx=0,
# 		miny=0,
# 		maxy=0,
# 		minratio=0,
# 		maxratio=0,
# 		logy=False,
#         xtitle='',
#         ytitle='Events',
#         textsizefactor=1,
#         signal_legend=signalWB_legendnames
#         )

# 	make_ratioplot(
# 		name=i+'2',
# 		ttbar_file=ttbar_file,
# 		qcd_file=qcd_file,
# 		data_file=data_file,
# 		signal_files=signal_files,
# 		histo='Preselection/'+i, 
# 		histo_qcd='Preselection/'+i,
# 		histo_signal='Preselection/'+i,
# 		rebin=rebinna,
# 		minx=0,
# 		maxx=0,
# 		miny=0,
# 		maxy=0,
# 		minratio=0,
# 		maxratio=0,
# 		logy=False,
#         xtitle='',
#         ytitle='Events',
#         textsizefactor=1,
#         signal_legend=signalWB_legendnames,
#         separate_legend=True
#         )

qcdbkgbtag=data_file.Get("Selection/bkg2").Clone('qcdbkgbtag')
qcdbkgbtag_up=data_file.Get("Selection/bkg2up").Clone('qcdbkgbtag_up')
qcdbkgbtag_down=data_file.Get("Selection/bkg2down").Clone('qcdbkgbtag_down')
qcdbkgnobtag=data_file.Get("Selection/bkg1").Clone('qcdbkgnobtag')
qcdbkgnobtag_up=data_file.Get("Selection/bkg1up").Clone('qcdbkgnobtag_up')
qcdbkgnobtag_down=data_file.Get("Selection/bkg1down").Clone('qcdbkgnobtag_down')
blow=qcdbkgbtag.GetXaxis().FindFixBin(900.0)
bhigh=qcdbkgbtag.GetXaxis().FindFixBin(3000.0)
qcdsfbtag=qcd_file.Get("Selection/zprimemassbtag").Integral(blow,bhigh)/qcd_file.Get("Selection/antibcsvCRbtag_zprimemass").Integral(blow,bhigh)
qcdsfnobtag=qcd_file.Get("Selection/zprimemassnobtag").Integral(blow,bhigh)/qcd_file.Get("Selection/antibcsvCRnobtag_zprimemass").Integral(blow,bhigh)
print 'btag',qcdsfbtag
print 'nobtag',qcdsfnobtag
dratiobtag=data_file.Get("Selection/zprimemassbtag").Clone()
dratiobtag.Add(ttbar_file.Get("Selection/zprimemassbtag"),-1.0)
qcdsfbtag2=dratiobtag.Integral(blow,bhigh)/qcdbkgbtag.Integral(blow,bhigh)
drationobtag=data_file.Get("Selection/zprimemassnobtag").Clone()
drationobtag.Add(ttbar_file.Get("Selection/zprimemassnobtag"),-1.0)
qcdsfnobtag2=drationobtag.Integral(blow,bhigh)/qcdbkgnobtag.Integral(blow,bhigh)
print 'btag2',qcdsfbtag2
print 'nobtag2',qcdsfnobtag2



qcdbkgbtag.Add(ttbar_file.Get("Selection/bkg2").Clone(),-1.0)
qcdbkgbtag.Scale(qcdsfbtag2)
qcdbkgbtag_up.Add(ttbar_file.Get("Selection/bkg2up").Clone(),-1.0)
qcdbkgbtag_up.Scale(qcdsfbtag2)
qcdbkgbtag_down.Add(ttbar_file.Get("Selection/bkg2down").Clone(),-1.0)
qcdbkgbtag_down.Scale(qcdsfbtag2)

qcdbkgnobtag.Add(ttbar_file.Get("Selection/bkg1").Clone(),-1.0)
qcdbkgnobtag.Scale(qcdsfnobtag2)
qcdbkgnobtag_up.Add(ttbar_file.Get("Selection/bkg1up").Clone(),-1.0)
qcdbkgnobtag_up.Scale(qcdsfnobtag2)
qcdbkgnobtag_down.Add(ttbar_file.Get("Selection/bkg1down").Clone(),-1.0)
qcdbkgnobtag_down.Scale(qcdsfnobtag2)

outfile.cd()
qcdbkgbtag.Write()
qcdbkgbtag_up.Write()
qcdbkgbtag_down.Write()
qcdbkgnobtag.Write()
qcdbkgnobtag_up.Write()
qcdbkgnobtag_down.Write()
rebinna=10
signalzoom=1
minx=0
maxx=0
make_ratioplot(
		name='2_btag',
		ttbar_file=ttbar_file,
		qcd_file=outfile,
		data_file=data_file,
		signal_files=signal_files_short,
		histo="Selection/zprimemassbtag", 
		histo_qcd='qcdbkgbtag',
		histo_signal="Selection/zprimemassbtag",
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgbtag_up',bkgdown='qcdbkgbtag_down'
        )
make_ratioplot(
		name='1_btag',
		ttbar_file=ttbar_file,
		qcd_file=outfile,
		data_file=data_file,
		signal_files=signal_files_short,
		histo="Selection/zprimemassnobtag", 
		histo_qcd='qcdbkgnobtag',
		histo_signal="Selection/zprimemassnobtag",
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgnobtag_up',bkgdown='qcdbkgnobtag_down'
        )


make_ratioplot(
    name='2_btagTT',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo="Selection/zprimemassbtag", 
    histo_qcd='qcdbkgbtag',
    histo_signal="Selection/zprimemassbtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgbtag_up',bkgdown='qcdbkgbtag_down'
        )
make_ratioplot(
    name='1_btagTT',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo="Selection/zprimemassnobtag", 
    histo_qcd='qcdbkgnobtag',
    histo_signal="Selection/zprimemassnobtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgnobtag_up',bkgdown='qcdbkgnobtag_down'
        )

make_ratioplot(
    name='2_btagTTNOLOG',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo="Selection/zprimemassbtag", 
    histo_qcd='qcdbkgbtag',
    histo_signal="Selection/zprimemassbtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgbtag_up',bkgdown='qcdbkgbtag_down'
        )
make_ratioplot(
    name='1_btagTTNOLOG',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signalTTreco_files,
    histo="Selection/zprimemassnobtag", 
    histo_qcd='qcdbkgnobtag',
    histo_signal="Selection/zprimemassnobtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalTT_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgnobtag_up',bkgdown='qcdbkgnobtag_down'
        )



make_ratioplot(
    name='2_btagALL',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signal_files,
    histo="Selection/zprimemassbtag", 
    histo_qcd='qcdbkgbtag',
    histo_signal="Selection/zprimemassbtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgbtag_up',bkgdown='qcdbkgbtag_down'
        )
make_ratioplot(
    name='1_btagALL',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signal_files,
    histo="Selection/zprimemassnobtag", 
    histo_qcd='qcdbkgnobtag',
    histo_signal="Selection/zprimemassnobtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=True,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        #signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgnobtag_up',bkgdown='qcdbkgnobtag_down'
        )





make_ratioplot(
    name='2_btagNOLOG',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signal_files_short,
    histo="Selection/zprimemassbtag", 
    histo_qcd='qcdbkgbtag',
    histo_signal="Selection/zprimemassbtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgbtag_up',bkgdown='qcdbkgbtag_down'
        )
make_ratioplot(
    name='1_btagNOLOG',
    ttbar_file=ttbar_file,
    qcd_file=outfile,
    data_file=data_file,
    signal_files=signal_files_short,
    histo="Selection/zprimemassnobtag", 
    histo_qcd='qcdbkgnobtag',
    histo_signal="Selection/zprimemassnobtag",
    rebin=rebinna,
    minx=minx,
    maxx=maxx,
    miny=0,
    maxy=0,
    minratio=0,
    maxratio=0,
    logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames_short,
        separate_legend=True,
        signal_zoom=signalzoom,
        qcd_legend='QCD from sideband',
        fixratio=True,
        signal_colors=[kOrange+10,kAzure+1,kSpring-6],
        dosys=False,
        sysdict=systypes,
        bkgup='qcdbkgnobtag_up',bkgdown='qcdbkgnobtag_down'
        )








compare(name='qcdcorrsystbtag',
		file_list=[qcd_file,qcd_file,qcd_file],
		name_list=['Selection/bkg2','Selection/bkg2up','Selection/bkg2down'],
		legend_list=['nominal','up - weight applied twice','down - no weight applied'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=10,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)

compare(name='qcdcorrsystnobtag',
		file_list=[qcd_file,qcd_file,qcd_file],
		name_list=['Selection/bkg1','Selection/bkg1up','Selection/bkg1down'],
		legend_list=['nominal','up - weight applied twice','down - no weight applied'],
		normalize=True,drawoption='hE',
		xtitle='',ytitle='',
		minx=0,maxx=0,
		rebin=10,
		miny=0,maxy=0,
		textsizefactor=1,logy=False)





signal_filesWB=[]
signal_filesZT=[]
signal_filesHT=[]
for i in signalWB_names:
  signal_filesWB.append(TFile(path+filename_base+i+root,'READ'))
for i in signalZT_names:
  signal_filesZT.append(TFile(path+filename_base+i+root,'READ'))
for i in signalHT_names:
  signal_filesHT.append(TFile(path+filename_base+i+root,'READ'))

dotheta=False
if dotheta:
  rebinna=10
  runList=[0,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000,4000]
  runLen=len(runList)-1
  runArray = array('d',runList)
  u='_'
  uu='__'
  nscan=10
  counter=1
  filecounter=1
  onebtag='Selection/zprimemassnobtag'
  twobtags='Selection/zprimemassbtag'
  sides={'UP':'plus','DOWN':'minus'}
  cats={onebtag:'1btag',twobtags:'2btag'}



  def dosys(file_path='',the_file=0,cats={},sys_to_do={},sample_name='',out_file=0,infile=0):
    if the_file
    the_file=TFile(file_path+'UP'+root,"READ")
    for cat in cats:
      allhad=the_file.Get(cat).Clone()
      allhad.Rebin(rebinna)
      allhad.Rebin(runLen,'',runArray)
      outfile.cd()
      allhad.Write('allhad'+cats[cat]+uu+sample_name)
    for sys in sys_to_do:
        if not (sys in ['mur','muf','murmuf']):
          for side in sides:
            sys_file=TFile(file_path+sys_to_do[sys]+side+root,'READ')
            for cat in cats:
              allhad=sys_file.Get(cat).Clone()
              allhad.Rebin(rebinna)
              allhad=allhad.Rebin(runLen,'',runArray)
              out_file.cd()
              allhad.Write('allhad'+cats[cat]+uu+sample_name+uu+sys+uu+sides[side])
            sys_file.Close()
    if ('mur' in sys_to_do) and ('muf' in sys_to_do) and ('murmuf' in sys_to_do):
      sysfile_MURUP=TFile(file_path+sys_to_do['mur']+'UP.root','READ')
      sysfile_MURDOWN=TFile(file_path+sys_to_do['mur']+'DOWN.root','READ')
      sysfile_MUFUP=TFile(file_path+sys_to_do['muf']+'UP.root','READ')
      sysfile_MUFDOWN=TFile(file_path+sys_to_do['muf']+'DOWN.root','READ')
      sysfile_MURMUFUP=TFile(file_path+sys_to_do['murmuf']+'UP.root','READ')
      sysfile_MURMUFDOWN=TFile(file_path+sys_to_do['murmuf']+'DOWN.root','READ')
      for cat in cats:
        allhad_env=envelope([sysfilettbar_MURUP.Get(cat),sysfilettbar_MURDOWN.Get(cat),sysfilettbar_MUFUP.Get(cat),sysfilettbar_MUFDOWN.Get(cat),sysfilettbar_MURMUFUP.Get(cat),sysfilettbar_MURMUFDOWN.Get(cat)])
        allhad_up=sysfilettbar_MURUP.Get(cat).Clone()
        allhad_down=sysfilettbar_MURUP.Get(cat).Clone()
        for imtt in range(1,allhad_up.GetNbinsX()+1):
          allhad_up.SetBinContent(imtt,allhad_env[imtt-1][1])
          allhad_down.SetBinContent(imtt,allhad_env[imtt-1][0])
        allhad_up.Rebin(rebinna)
        allhad_down.Rebin(rebinna)
        allhad_up=allhad_up.Rebin(runLen,'',runArray)
        allhad_down=allhad_down.Rebin(runLen,'',runArray)
        out_file.cd()
        allhad_up.Write('allhad'+cats[cat]+uu+sample_name+uu+'mu'+uu+'plus')
        allhad_down.Write('allhad'+cats[cat]+uu+sample_name+uu+'mu'+uu+'minus')
      sysfilettbar_MURUP.Close()
      sysfilettbar_MURDOWN.Close()
      sysfilettbar_MUFUP.Close()
      sysfilettbar_MUFDOWN.Close()
      sysfilettbar_MURMUFUP.Close()
      sysfilettbar_MURMUFDOWN.Close()
    the_file.Close()

  thetafileTT=TFile('thetaTT.root','RECREATE')
  dosys(file_path=syspath+filename_base+'MC.TTbar',cats=cats,sys_to_do=systypes,sample_name='ttbar',out_file=thetafileTT)
  dosys(file_path=syspath+filename_base+'MC.TTbar',cats=cats,sys_to_do=systypes,sample_name='DATA',out_file=thetafileTT)
  allhad2btag__DATA=data_file.Get(twobtags).Clone()
  allhad1btag__DATA=data_file.Get(onebtag).Clone()
  allhad2btag__DATA.Rebin(rebinna)
  allhad1btag__DATA.Rebin(rebinna)
  allhad2btag__DATA=allhad2btag__DATA.Rebin(runLen,'',runArray)
  allhad1btag__DATA=allhad1btag__DATA.Rebin(runLen,'',runArray)
  allhad2btag__DATA.Write('allhad2btag__DATA')
  allhad1btag__DATA.Write('allhad1btag__DATA')

  for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:#+[[0,0,0]]:
    filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
    thetafile=TFile('theta/theta'+filename_postfix+'.root','RECREATE')
    thetafile.cd()
    # allhad2btag__qcd=qcd_file.Get(twobtags).Clone()
    # allhad1btag__qcd=qcd_file.Get(onebtag).Clone()
    allhad2btag__qcd=data_file.Get('Selection/bkg2').Clone()
    allhad1btag__qcd=data_file.Get('Selection/bkg1').Clone()
    allhad2btag__ttbar=ttbar_file.Get(twobtags).Clone()
    allhad1btag__ttbar=ttbar_file.Get(onebtag).Clone()
    allhad2btag__DATA=data_file.Get(twobtags).Clone()
    allhad1btag__DATA=data_file.Get(onebtag).Clone()
    allhad2btag__qcd.Scale(qcdsfbtag2)
    allhad1btag__qcd.Scale(qcdsfnobtag2)
    allhad2btag__qcd.Rebin(rebinna)
    allhad1btag__qcd.Rebin(rebinna)
    allhad2btag__ttbar.Rebin(rebinna)
    allhad1btag__ttbar.Rebin(rebinna)
    allhad2btag__DATA.Rebin(rebinna)
    allhad1btag__DATA.Rebin(rebinna)

    allhad2btag__qcd=allhad2btag__qcd.Rebin(runLen,'',runArray)
    allhad1btag__qcd=allhad1btag__qcd.Rebin(runLen,'',runArray)
    allhad2btag__ttbar=allhad2btag__ttbar.Rebin(runLen,'',runArray)
    allhad1btag__ttbar=allhad1btag__ttbar.Rebin(runLen,'',runArray)
    allhad2btag__DATA=allhad2btag__DATA.Rebin(runLen,'',runArray)
    allhad1btag__DATA=allhad1btag__DATA.Rebin(runLen,'',runArray)

    allhad2btag__qcd.Write('allhad2btag__qcd')
    allhad1btag__qcd.Write('allhad1btag__qcd')
    allhad2btag__ttbar.Write('allhad2btag__ttbar')
    allhad1btag__ttbar.Write('allhad1btag__ttbar')
    allhad2btag__DATA.Write('allhad2btag__DATA')
    allhad1btag__DATA.Write('allhad1btag__DATA')
    allhad2btag__qcd__bkgcorr__plus=data_file.Get('Selection/bkg2up').Clone()
    allhad1btag__qcd__bkgcorr__plus=data_file.Get('Selection/bkg1up').Clone()
    allhad2btag__qcd__bkgcorr__minus=data_file.Get('Selection/bkg2down').Clone()
    allhad1btag__qcd__bkgcorr__minus=data_file.Get('Selection/bkg1down').Clone()
    allhad2btag__qcd__bkgcorr__plus.Scale(qcdsfbtag2)
    allhad1btag__qcd__bkgcorr__plus.Scale(qcdsfnobtag2)
    allhad2btag__qcd__bkgcorr__minus.Scale(qcdsfbtag2)
    allhad1btag__qcd__bkgcorr__minus.Scale(qcdsfnobtag2)
    allhad2btag__qcd__bkgcorr__plus.Rebin(rebinna)
    allhad1btag__qcd__bkgcorr__plus.Rebin(rebinna)
    allhad2btag__qcd__bkgcorr__minus.Rebin(rebinna)
    allhad1btag__qcd__bkgcorr__minus.Rebin(rebinna)

    allhad2btag__qcd__bkgcorr__plus=allhad2btag__qcd__bkgcorr__plus.Rebin(runLen,'',runArray)
    allhad1btag__qcd__bkgcorr__plus=allhad1btag__qcd__bkgcorr__plus.Rebin(runLen,'',runArray)
    allhad2btag__qcd__bkgcorr__minus=allhad2btag__qcd__bkgcorr__minus.Rebin(runLen,'',runArray)
    allhad1btag__qcd__bkgcorr__minus=allhad1btag__qcd__bkgcorr__minus.Rebin(runLen,'',runArray)
    allhad2btag__qcd__bkgcorr__plus.Write('allhad2btag__qcd__bkgcorr__plus')
    allhad1btag__qcd__bkgcorr__plus.Write('allhad1btag__qcd__bkgcorr__plus')
    allhad2btag__qcd__bkgcorr__minus.Write('allhad2btag__qcd__bkgcorr__minus')
    allhad1btag__qcd__bkgcorr__minus.Write('allhad1btag__qcd__bkgcorr__minus')
  
    for sys in systypes:
        if not (sys in ['mur','muf','murmuf']):
          for side in sides:
            sys_file=TFile(syspath+filename_base+'MC.TTbar'+systypes[sys]+side+root,'READ')
            for cat in cats:
              allhad=sys_file.Get(cat).Clone()
              allhad.Rebin(rebinna)
              allhad=allhad.Rebin(runLen,'',runArray)
              thetafile.cd()
              allhad.Write('allhad'+cats[cat]+uu+'ttbar'+uu+sys+uu+sides[side])
            sys_file.Close()

    if ('mur' in systypes) and ('muf' in systypes) and ('murmuf' in systypes):
      sysfilettbar_MURUP=TFile(syspath+filename_base+'MC.TTbar'+systypes['mur']+'UP.root','READ')
      sysfilettbar_MURDOWN=TFile(syspath+filename_base+'MC.TTbar'+systypes['mur']+'DOWN.root','READ')
      sysfilettbar_MUFUP=TFile(syspath+filename_base+'MC.TTbar'+systypes['muf']+'UP.root','READ')
      sysfilettbar_MUFDOWN=TFile(syspath+filename_base+'MC.TTbar'+systypes['muf']+'DOWN.root','READ')
      sysfilettbar_MURMUFUP=TFile(syspath+filename_base+'MC.TTbar'+systypes['murmuf']+'UP.root','READ')
      sysfilettbar_MURMUFDOWN=TFile(syspath+filename_base+'MC.TTbar'+systypes['murmuf']+'DOWN.root','READ')
      for cat in cats:
        allhad_env=envelope([sysfilettbar_MURUP.Get(cat),sysfilettbar_MURDOWN.Get(cat),sysfilettbar_MUFUP.Get(cat),sysfilettbar_MUFDOWN.Get(cat),sysfilettbar_MURMUFUP.Get(cat),sysfilettbar_MURMUFDOWN.Get(cat)])
        allhad_up=sysfilettbar_MURUP.Get(cat).Clone()
        allhad_down=sysfilettbar_MURUP.Get(cat).Clone()
        for imtt in range(1,allhad_up.GetNbinsX()+1):
          allhad_up.SetBinContent(imtt,allhad_env[imtt-1][1])
          allhad_down.SetBinContent(imtt,allhad_env[imtt-1][0])
        allhad_up.Rebin(rebinna)
        allhad_down.Rebin(rebinna)
        allhad_up=allhad_up.Rebin(runLen,'',runArray)
        allhad_down=allhad_down.Rebin(runLen,'',runArray)
        thetafile.cd()
        allhad_up.Write('allhad'+cats[cat]+uu+'ttbar'+uu+'mu'+uu+'plus')
        allhad_down.Write('allhad'+cats[cat]+uu+'ttbar'+uu+'mu'+uu+'minus')

      sysfilettbar_MURUP.Close()
      sysfilettbar_MURDOWN.Close()
      sysfilettbar_MUFUP.Close()
      sysfilettbar_MUFDOWN.Close()
      sysfilettbar_MURMUFUP.Close()
      sysfilettbar_MURMUFDOWN.Close()

    #if triplet==[0,0,0]:
    #	for masspoint in range(len(signalTT_names)):

    for masspoint in range(len(signalWB_names)):
      allhad2btag__signalWB=signal_filesWB[masspoint].Get(twobtags).Clone()
      allhad2btag__signalZT=signal_filesZT[masspoint].Get(twobtags).Clone()
      allhad2btag__signalHT=signal_filesHT[masspoint].Get(twobtags).Clone()
      #allhad2btag__signalWB.Sumw2()
      #allhad2btag__signalZT.Sumw2()
      #allhad2btag__signalHT.Sumw2()
      addscale=1.0
      #if '2000' in signalWB_names[masspoint] and '1500' in signalWB_names[masspoint]:
      #  addscale=0.163649053
      allhad2btag__signalWB.Scale(triplet[0]*addscale)
      allhad2btag__signalHT.Scale(triplet[1])
      allhad2btag__signalZT.Scale(triplet[2])
      allhad2btag__signal=allhad2btag__signalWB
      allhad2btag__signal.Add(allhad2btag__signalHT)
      allhad2btag__signal.Add(allhad2btag__signalZT)
      allhad2btag__signal.Rebin(rebinna)
      allhad2btag__signal=allhad2btag__signal.Rebin(runLen,'',runArray)

      allhad1btag__signalWB=signal_filesWB[masspoint].Get(onebtag).Clone()
      allhad1btag__signalZT=signal_filesZT[masspoint].Get(onebtag).Clone()
      allhad1btag__signalHT=signal_filesHT[masspoint].Get(onebtag).Clone()
      #allhad1btag__signalWB.Sumw2()
      #allhad1btag__signalZT.Sumw2()
      #allhad1btag__signalHT.Sumw2()
      allhad1btag__signalWB.Scale(triplet[0]*addscale)
      allhad1btag__signalHT.Scale(triplet[1])
      allhad1btag__signalZT.Scale(triplet[2])
      allhad1btag__signal=allhad1btag__signalWB
      allhad1btag__signal.Add(allhad1btag__signalHT)
      allhad1btag__signal.Add(allhad1btag__signalZT)
      allhad1btag__signal.Rebin(rebinna)
      allhad1btag__signal=allhad1btag__signal.Rebin(runLen,'',runArray)

      thetafile.cd()
      allhad2btag__signal.Write('allhad2btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
        str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))
      allhad1btag__signal.Write('allhad1btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
        str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))

      for sys in systypes:
        if not (sys in ['mur','muf','murmuf']):
          for side in sides:
            sys_fileWB=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes[sys]+side+root,'READ')
            sys_fileHT=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes[sys]+side+root,'READ')
            sys_fileZT=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes[sys]+side+root,'READ')
            for cat in cats:
              allhadWB=sys_fileWB.Get(cat).Clone()
              allhadHT=sys_fileHT.Get(cat).Clone()
              allhadZT=sys_fileZT.Get(cat).Clone()
              allhadWB.Scale(triplet[0]*addscale)
              allhadHT.Scale(triplet[1])
              allhadZT.Scale(triplet[2])
              allhad=allhadWB
              allhad.Add(allhadHT)
              allhad.Add(allhadZT)
              allhad.Rebin(rebinna)
              allhad=allhad.Rebin(runLen,'',runArray)
              thetafile.cd()
              allhad.Write('allhad'+cats[cat]+uu+'signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
        str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')+uu+sys+uu+sides[side])
            sys_fileWB.Close()
            sys_fileHT.Close()
            sys_fileZT.Close()
      if ('mur' in systypes) and ('muf' in systypes) and ('murmuf' in systypes):
        sysfileWB_MURUP=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['mur']+'UP.root','READ')
        sysfileWB_MURDOWN=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['mur']+'DOWN.root','READ')
        sysfileWB_MUFUP=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['muf']+'UP.root','READ')
        sysfileWB_MUFDOWN=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['muf']+'DOWN.root','READ')
        sysfileWB_MURMUFUP=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['murmuf']+'UP.root','READ')
        sysfileWB_MURMUFDOWN=TFile(syspath+filename_base+signalWB_names[masspoint]+systypes['murmuf']+'DOWN.root','READ')
        sysfileHT_MURUP=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['mur']+'UP.root','READ')
        sysfileHT_MURDOWN=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['mur']+'DOWN.root','READ')
        sysfileHT_MUFUP=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['muf']+'UP.root','READ')
        sysfileHT_MUFDOWN=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['muf']+'DOWN.root','READ')
        sysfileHT_MURMUFUP=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['murmuf']+'UP.root','READ')
        sysfileHT_MURMUFDOWN=TFile(syspath+filename_base+signalHT_names[masspoint]+systypes['murmuf']+'DOWN.root','READ')
        sysfileZT_MURUP=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['mur']+'UP.root','READ')
        sysfileZT_MURDOWN=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['mur']+'DOWN.root','READ')
        sysfileZT_MUFUP=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['muf']+'UP.root','READ')
        sysfileZT_MUFDOWN=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['muf']+'DOWN.root','READ')
        sysfileZT_MURMUFUP=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['murmuf']+'UP.root','READ')
        sysfileZT_MURMUFDOWN=TFile(syspath+filename_base+signalZT_names[masspoint]+systypes['murmuf']+'DOWN.root','READ')
        for cat in cats:
          allhadWB_env=envelope([sysfileWB_MURUP.Get(cat),sysfileWB_MURDOWN.Get(cat),sysfileWB_MUFUP.Get(cat),sysfileWB_MUFDOWN.Get(cat),sysfileWB_MURMUFUP.Get(cat),sysfileWB_MURMUFDOWN.Get(cat)])
          allhadHT_env=envelope([sysfileHT_MURUP.Get(cat),sysfileHT_MURDOWN.Get(cat),sysfileHT_MUFUP.Get(cat),sysfileHT_MUFDOWN.Get(cat),sysfileHT_MURMUFUP.Get(cat),sysfileHT_MURMUFDOWN.Get(cat)])
          allhadZT_env=envelope([sysfileZT_MURUP.Get(cat),sysfileZT_MURDOWN.Get(cat),sysfileZT_MUFUP.Get(cat),sysfileZT_MUFDOWN.Get(cat),sysfileZT_MURMUFUP.Get(cat),sysfileZT_MURMUFDOWN.Get(cat)])
          allhadWB_up=sysfileWB_MURUP.Get(cat).Clone()
          allhadHT_up=sysfileHT_MURUP.Get(cat).Clone()
          allhadZT_up=sysfileZT_MURUP.Get(cat).Clone()
          allhadWB_down=sysfileWB_MURUP.Get(cat).Clone()
          allhadHT_down=sysfileHT_MURUP.Get(cat).Clone()
          allhadZT_down=sysfileZT_MURUP.Get(cat).Clone()
          for imtt in range(1,allhadWB_up.GetNbinsX()+1):
            allhadWB_up.SetBinContent(imtt,allhadWB_env[imtt-1][1])
            allhadHT_up.SetBinContent(imtt,allhadHT_env[imtt-1][1])
            allhadZT_up.SetBinContent(imtt,allhadZT_env[imtt-1][1])
            allhadWB_down.SetBinContent(imtt,allhadWB_env[imtt-1][0])
            allhadHT_down.SetBinContent(imtt,allhadHT_env[imtt-1][0])
            allhadZT_down.SetBinContent(imtt,allhadZT_env[imtt-1][0])
          allhadWB_up.Scale(triplet[0]*addscale)
          allhadHT_up.Scale(triplet[1])
          allhadZT_up.Scale(triplet[2])
          allhadWB_down.Scale(triplet[0]*addscale)
          allhadHT_down.Scale(triplet[1])
          allhadZT_down.Scale(triplet[2])
          allhad_up=allhadWB_up
          allhad_up.Add(allhadHT_up)
          allhad_up.Add(allhadZT_up)
          allhad_down=allhadWB_down
          allhad_down.Add(allhadHT_down)
          allhad_down.Add(allhadZT_down)
          allhad_up.Rebin(rebinna)
          allhad_down.Rebin(rebinna)
          allhad_up=allhad_up.Rebin(runLen,'',runArray)
          allhad_down=allhad_down.Rebin(runLen,'',runArray)
          thetafile.cd()
          allhad_up.Write('allhad'+cats[cat]+uu+'signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
        str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')+uu+'mu'+uu+'plus')
          allhad_down.Write('allhad'+cats[cat]+uu+'signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
        str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')+uu+'mu'+uu+'minus')
        sysfileWB_MURUP.Close()
        sysfileWB_MURDOWN.Close()
        sysfileWB_MUFUP.Close()
        sysfileWB_MUFDOWN.Close()
        sysfileWB_MURMUFUP.Close()
        sysfileWB_MURMUFDOWN.Close()
        sysfileHT_MURUP.Close()
        sysfileHT_MURDOWN.Close()
        sysfileHT_MUFUP.Close()
        sysfileHT_MUFDOWN.Close()
        sysfileHT_MURMUFUP.Close()
        sysfileHT_MURMUFDOWN.Close()
        sysfileZT_MURUP.Close()
        sysfileZT_MURDOWN.Close()
        sysfileZT_MUFUP.Close()
        sysfileZT_MUFDOWN.Close()
        sysfileZT_MURMUFUP.Close()
        sysfileZT_MURMUFDOWN.Close()
        
      
      counter+=1
    thetafile.Close()

    theta_config = open('theta/model'+filename_postfix+'.py','w')
    theta_config.write("def get_model():\n\
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/theta"+filename_postfix+".root', include_mc_uncertainties = True)#mc uncertainties=true\n\
    model.fill_histogram_zerobins()\n\
    model.set_signal_processes('signal*')\n\
    #model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')\n\
    #model.add_lognormal_uncertainty('qcd_rate', math.log(1.15), 'qcd')\n\
    for p in model.processes:\n\
        if p == 'qcd': continue\n\
        model.add_lognormal_uncertainty('lumi', math.log(1.027), p)\n\
        model.add_lognormal_uncertainty('trigger', math.log(1.03), p)\n\
        #if 'signal' in p:\n\
        #    model.add_lognormal_uncertainty(p+'_rate', math.log(1.15), p)\n\
    return model\n\
model = get_model()\n\
model_summary(model)\n\
options = Options()\n\
options.set('main', 'n_threads', '20')\n\
#plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'\n\
plot_exp, plot_obs = bayesian_limits(model,what='expected')#bayesian_limits ,what='expected'\n\
plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp"+filename_postfix+".txt')\n\
#plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs"+filename_postfix+".txt')\n\
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/htmlout"+filename_postfix+"')")
    filecounter+=1









#signal contamination
qcd1=qcd_file.Get("Selection/zprimemassnobtag").Clone()
ttbar1=ttbar_file.Get("Selection/zprimemassnobtag").Clone()
qcd2=qcd_file.Get("Selection/zprimemassbtag").Clone()
ttbar2=ttbar_file.Get("Selection/zprimemassbtag").Clone()

qcd1b=qcd_file.Get("Selection/antibcsvCRnobtag_zprimemass").Clone()
ttbar1b=ttbar_file.Get("Selection/antibcsvCRnobtag_zprimemass").Clone()
qcd2b=qcd_file.Get("Selection/antibcsvCRbtag_zprimemass").Clone()
ttbar2b=ttbar_file.Get("Selection/antibcsvCRbtag_zprimemass").Clone()

qcd1bk=qcd_file.Get("Selection/bkg1").Clone()
ttbar1bk=ttbar_file.Get("Selection/bkg1").Clone()
qcd2bk=qcd_file.Get("Selection/bkg2").Clone()
ttbar2bk=ttbar_file.Get("Selection/bkg2").Clone()

den1=qcd1.Integral(blow,bhigh)+ttbar1.Integral(blow,bhigh)
den2=qcd2.Integral(blow,bhigh)+ttbar2.Integral(blow,bhigh)
den1b=qcd1b.Integral(blow,bhigh)+ttbar1b.Integral(blow,bhigh)
den2b=qcd2b.Integral(blow,bhigh)+ttbar2b.Integral(blow,bhigh)
den1bk=qcd1bk.Integral(blow,bhigh)+ttbar1bk.Integral(blow,bhigh)
den2bk=qcd2bk.Integral(blow,bhigh)+ttbar2bk.Integral(blow,bhigh)
for masspoint in range(len(signalWB_names)):
	signal1=signal_filesWB[masspoint].Get("Selection/zprimemassnobtag").Clone()
	signal2=signal_filesWB[masspoint].Get("Selection/zprimemassbtag").Clone()
	signal1b=signal_filesWB[masspoint].Get("Selection/antibcsvCRnobtag_zprimemass").Clone()
	signal2b=signal_filesWB[masspoint].Get("Selection/antibcsvCRbtag_zprimemass").Clone()
	signal1bk=signal_filesWB[masspoint].Get("Selection/bkg1").Clone()
	signal2bk=signal_filesWB[masspoint].Get("Selection/bkg2").Clone()
	num1=signal1.Integral(blow,bhigh)
	num2=signal2.Integral(blow,bhigh)
	num1b=signal1b.Integral(blow,bhigh)
	num2b=signal2b.Integral(blow,bhigh)
	num1bk=signal1bk.Integral(blow,bhigh)
	num2bk=signal2bk.Integral(blow,bhigh)
#	if masspoint in [0,3,6]:


	print signalWB_names[masspoint], num1/den1, num2/den2, num1b/den1b, num2b/den2b, num1bk/den1bk, num2bk/den2bk

# resized_bkg1=qcd_file.Get("Selection/bkg1").Clone('resized_bkg1')
# resized_bkg2=qcd_file.Get("Selection/bkg2").Clone('resized_bkg2')
#resize
for masspoint in [0,3,6]:
	# resized_sgn1=signal_filesWB[masspoint].Get("Selection/bkg1").Clone('resized_sgn1_'+str(masspoint))
	# resized_sgn2=signal_filesWB[masspoint].Get("Selection/bkg2").Clone('resized_sgn2_'+str(masspoint))
	# signal1b=signal_filesWB[masspoint].Get("Selection/antibcsvCRnobtag_zprimemass").Clone()
	# signal2b=signal_filesWB[masspoint].Get("Selection/antibcsvCRbtag_zprimemass").Clone()

	make_ratioplot(
		name='signal_injection2_'+str(masspoint),
		ttbar_file=signal_files[masspoint],
		qcd_file=qcd_file,
		data_file=qcd_file,
		signal_files=[signal_files[masspoint]],
		histo="Selection/zprimemassbtag", 
		histo_qcd='Selection/bkg2',
		histo_ttbar='Selection/bkg2',
		histo_signal="Selection/zprimemassbtag",
		rebin=rebinna,
		minx=minx,
		maxx=maxx,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=[signalWB_legendnames[masspoint]],
        separate_legend=False,
        signal_zoom=1,
        ttbar_zoom=den2/den2bk,
        qcd_zoom=den2/den2bk,
        fixratio=True,
        ttbar_legend='signal in bkg estimate (MC)',qcd_legend='background estimate (MC)', data_legend='observed background (MC)',
        normalize=False
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

	make_ratioplot(
		name='signal_injection1_'+str(masspoint),ttbar_file=signal_files[masspoint],
		qcd_file=qcd_file,data_file=qcd_file,signal_files=[signal_files[masspoint]],
		histo="Selection/zprimemassnobtag",histo_qcd='Selection/bkg1',
		histo_ttbar='Selection/bkg1',histo_signal="Selection/zprimemassnobtag",
		rebin=rebinna,minx=minx,maxx=maxx,miny=0,maxy=0,minratio=0,maxratio=0,logy=False,xtitle='',ytitle='Events',textsizefactor=1,signal_legend=[signalWB_legendnames[masspoint]],separate_legend=False,signal_zoom=1,ttbar_zoom=den1/den1bk,qcd_zoom=den1/den1bk,fixratio=True,ttbar_legend='signal in bkg estimate (MC)',qcd_legend='background estimate (MC)',data_legend="observed background (MC)",normalize=False)
		
		#)


######systematics compare
make_comp(data_file.Get("Selection/bkg1"),data_file.Get("Selection/bkg1up"),data_file.Get("Selection/bkg1down"),'SYS_bkg1',10)
make_comp(data_file.Get("Selection/bkg2"),data_file.Get("Selection/bkg2up"),data_file.Get("Selection/bkg2down"),'SYS_bkg2',10)

ttbar_string='MC.TTbar'
up='UP'
down='DOWN'
# ttbar_MURUP=TFile(syspath+filename_base+ttbar_string+systypes['mur']+up+root)
# ttbar_MURDOWN=TFile(syspath+filename_base+ttbar_string+systypes['mur']+down+root)
# ttbar_MUFUP=TFile(syspath+filename_base+ttbar_string+systypes['muf']+up+root)
# ttbar_MUFDOWN=TFile(syspath+filename_base+ttbar_string+systypes['muf']+down+root)
ttbar_mean=TFile(syspath+filename_base+ttbar_string+up+root)
# ttbar_JECUP=TFile(syspath+filename_base+ttbar_string+systypes['jec']+up+root)
# ttbar_JECDOWN=TFile(syspath+filename_base+ttbar_string+systypes['jec']+down+root)
# ttbar_JERUP=TFile(syspath+filename_base+ttbar_string+systypes['jer']+up+root)
# ttbar_JERDOWN=TFile(syspath+filename_base+ttbar_string+systypes['jer']+down+root)
# ttbar_PUUP=TFile(syspath+filename_base+ttbar_string+systypes['pu']+up+root)
# ttbar_PUDOWN=TFile(syspath+filename_base+ttbar_string+systypes['pu']+down+root)

sr1name="Selection/zprimemassnobtag"
sr2name="Selection/zprimemassbtag"
# make_comp(ttbar_mean.Get(sr1name),ttbar_MURUP.Get(sr1name),ttbar_MURDOWN.Get(sr1name),'SYS_mur1',10)
# make_comp(ttbar_mean.Get(sr2name),ttbar_MURUP.Get(sr2name),ttbar_MURDOWN.Get(sr2name),'SYS_mur2',10)
# make_comp(ttbar_mean.Get(sr1name),ttbar_MUFUP.Get(sr1name),ttbar_MUFDOWN.Get(sr1name),'SYS_muf1',10)
# make_comp(ttbar_mean.Get(sr2name),ttbar_MUFUP.Get(sr2name),ttbar_MUFDOWN.Get(sr2name),'SYS_muf2',10)
# make_comp(ttbar_mean.Get(sr1name),ttbar_JECUP.Get(sr1name),ttbar_JECDOWN.Get(sr1name),'SYS_jec1',10)
# make_comp(ttbar_mean.Get(sr2name),ttbar_JECUP.Get(sr2name),ttbar_JECDOWN.Get(sr2name),'SYS_jec2',10)
# make_comp(ttbar_mean.Get(sr1name),ttbar_JERUP.Get(sr1name),ttbar_JERDOWN.Get(sr1name),'SYS_jer1',10)
# make_comp(ttbar_mean.Get(sr2name),ttbar_JERUP.Get(sr2name),ttbar_JERDOWN.Get(sr2name),'SYS_jer2',10)
# make_comp(ttbar_mean.Get(sr1name),ttbar_PUUP.Get(sr1name),ttbar_PUDOWN.Get(sr1name),'SYS_pu1',10)
# make_comp(ttbar_mean.Get(sr2name),ttbar_PUUP.Get(sr2name),ttbar_PUDOWN.Get(sr2name),'SYS_pu2',10)

for sys in systypes:
	ttbar_SYSUP=TFile(syspath+filename_base+ttbar_string+systypes[sys]+up+root)
	ttbar_SYSDOWN=TFile(syspath+filename_base+ttbar_string+systypes[sys]+down+root)
	make_comp(ttbar_mean.Get(sr1name),ttbar_SYSUP.Get(sr1name),ttbar_SYSDOWN.Get(sr1name),'SYS_'+sys+'1',10)
	make_comp(ttbar_mean.Get(sr2name),ttbar_SYSUP.Get(sr2name),ttbar_SYSDOWN.Get(sr2name),'SYS_'+sys+'2',10)

ttbar_MURUP=TFile(syspath+filename_base+ttbar_string+systypes['mur']+up+root)
ttbar_MURDOWN=TFile(syspath+filename_base+ttbar_string+systypes['mur']+down+root)
ttbar_MUFUP=TFile(syspath+filename_base+ttbar_string+systypes['muf']+up+root)
ttbar_MUFDOWN=TFile(syspath+filename_base+ttbar_string+systypes['muf']+down+root)
ttbar_MURMUFUP=TFile(syspath+filename_base+ttbar_string+systypes['murmuf']+up+root)
ttbar_MURMUFDOWN=TFile(syspath+filename_base+ttbar_string+systypes['murmuf']+down+root)
envelopesr1=envelope([ttbar_MURUP.Get(sr1name),ttbar_MURDOWN.Get(sr1name),ttbar_MUFUP.Get(sr1name),ttbar_MUFDOWN.Get(sr1name),ttbar_MURMUFUP.Get(sr1name),ttbar_MURMUFDOWN.Get(sr1name)])
envelopesr2=envelope([ttbar_MURUP.Get(sr2name),ttbar_MURDOWN.Get(sr2name),ttbar_MUFUP.Get(sr2name),ttbar_MUFDOWN.Get(sr2name),ttbar_MURMUFUP.Get(sr2name),ttbar_MURMUFDOWN.Get(sr2name)])
ttbarsr1_MUDOWN=ttbar_mean.Get(sr1name).Clone()
ttbarsr1_MUUP=ttbar_mean.Get(sr1name).Clone()
ttbarsr2_MUDOWN=ttbar_mean.Get(sr2name).Clone()
ttbarsr2_MUUP=ttbar_mean.Get(sr2name).Clone()
for imtt in range(1,ttbarsr1_MUDOWN.GetNbinsX()+1):
  ttbarsr1_MUDOWN.SetBinContent(imtt,envelopesr1[imtt-1][0])
  ttbarsr1_MUUP.SetBinContent(imtt,envelopesr1[imtt-1][1])
  ttbarsr2_MUDOWN.SetBinContent(imtt,envelopesr2[imtt-1][0])
  ttbarsr2_MUUP.SetBinContent(imtt,envelopesr2[imtt-1][1])
make_comp(ttbar_mean.Get(sr1name),ttbarsr1_MUDOWN,ttbarsr1_MUUP,'SYS_MU1',10)
make_comp(ttbar_mean.Get(sr2name),ttbarsr2_MUDOWN,ttbarsr2_MUUP,'SYS_MU2',10)
outfile.Close()
