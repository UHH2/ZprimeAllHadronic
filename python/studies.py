from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,doeff,make_plot,make_ratioplot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/preselection/'
# path2='/nfs/dust/cms/user/usaiem/phys14-2/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.'
signalHT_names=[
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToHT_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1500Nar_LH']
signalZT_names=[
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToZT_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1500Nar_LH']
signalWB_names=[
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp700Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp1500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp900Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Nar_RH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1200Wid_LH',
'MC.ZpToTpT_TpToWB_MZp2000Nar_MTp1500Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2000Wid_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1200Nar_LH',
'MC.ZpToTpT_TpToWB_MZp2500Nar_MTp1500Nar_LH']
signalWB_legendnames=[
"Z'(1.5TeV)#rightarrowT't, T'(0.7TeV)#rightarrowbW 1pb",
"Z'(1.5TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW 1pb",
"Z'(1.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(0.9TeV)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(1.2TeV,RH)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(1.2TeV,Wide)#rightarrowbW 1pb",
"Z'(2TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW 1pb",
"Z'(2TeV,Wide)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2.5TeV)#rightarrowT't, T'(1.2TeV)#rightarrowbW 1pb",
"Z'(2.5TeV)#rightarrowT't, T'(1.5TeV)#rightarrowbW 1pb",
]
signal_names=signalWB_names+signalHT_names+signalZT_names
qcd_names=['MC.QCD_HT500to700','MC.QCD_HT700to1000','MC.QCD_HT1000to1500','MC.QCD_HT1500to2000','MC.QCD_HT2000toInf']
ttbar_names=['MC.TTbar']
ttbarhigh_names=['MC.TT_Mtt0700to1000','MC.TT_Mtt1000toINFT']
data_names=['DATA.JetHT_Run2015D_05Oct2015_v1','DATA.JetHT_Run2015D_PromptReco_v4']
# ttbar50ns_name='TTbar50ns'
outfile=TFile('outfile.root','RECREATE')


#merge
force=False
merge=False
qcd_filename=hadd(path,filename_base,qcd_names,'qcd_added',force,merge)
ttbar_filename=hadd(path,filename_base,ttbar_names,'ttbar_added',force,merge)
data_filename=hadd(path,filename_base,data_names,'data_added',force,merge)
#open files
qcd_file=TFile(qcd_filename,'READ')
ttbar_file=TFile(ttbar_filename,'READ')
data_file=TFile(data_filename,'READ')
signal_files=[]
for i in signalWB_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))

rebinna=20

for i in ['step1_wmass','step1_wnsub','step1_tcsv','step1_tpt','step2_bcsv','step2_wpt','step3_tprimemass','step3_tprimept','step4_zprimemass','step4_zprimemassbtag','step4_zprimemassbtagnsub']:
	make_plot(i, ttbar_file, qcd_file, data_file, signal_files, 'Preselection/'+i,'Preselection/'+i,'PreselectionAllHad/'+i,rebin=rebinna,minx=500,maxx=4000    ,logy=True)#,miny=0.1,maxy=10000
	make_plot(i+'_nolog', ttbar_file, qcd_file, data_file, signal_files, 'Preselection/'+i,'Preselection/'+i,'PreselectionAllHad/'+i,rebin=rebinna,minx=500,maxx=4000     ,logy=False)#,miny=0.1,maxy=50

	make_ratioplot(
		name=i,
		ttbar_file=ttbar_file,
		qcd_file=qcd_file,
		data_file=data_file,
		signal_files=signal_files,
		histo='Preselection/'+i, 
		histo_qcd='Preselection/'+i,
		histo_signal='Preselection/'+i,
		rebin=rebinna,
		minx=0,
		maxx=0,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames
        )

	make_ratioplot(
		name=i+'2',
		ttbar_file=ttbar_file,
		qcd_file=qcd_file,
		data_file=data_file,
		signal_files=signal_files,
		histo='Preselection/'+i, 
		histo_qcd='Preselection/'+i,
		histo_signal='Preselection/'+i,
		rebin=rebinna,
		minx=0,
		maxx=0,
		miny=0,
		maxy=0,
		minratio=0,
		maxratio=0,
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True
        )
	
outfile.Close()