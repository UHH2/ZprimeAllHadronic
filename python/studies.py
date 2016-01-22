from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,doeff,make_plot,make_ratioplot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/selection/'
prepath='/nfs/dust/cms/user/usaiem/preselection/'
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
for i in signalWB_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))
for i in signalWB_names:
	signal_files_pre.append(TFile(prepath+filename_base+i+root,'READ'))

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
  "antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",  "antibcsvCR_zprimemass",  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
"antitopmassCRmass_zprimemass",  "antitopnsubCRmass_zprimemass",  "antiwmassCRmass_zprimemass",  "antiwnsubCRmass_zprimemass",  "antibcsvCRmass_zprimemass",  "antibptCRmass_zprimemass",  "antibmassCRmass_zprimemass",
"antitopmassCRbtag_zprimemass",  "antitopnsubCRbtag_zprimemass",  "antiwmassCRbtag_zprimemass",  "antiwnsubCRbtag_zprimemass",  "antibcsvCRbtag_zprimemass",  "antibptCRbtag_zprimemass",  "antibmassCRbtag_zprimemass",
"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass",  "antibcsvCRnobtag_zprimemass",  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
"bkg1","bkg2","bkg12","bkg1up","bkg2up","bkg12up","bkg1down","bkg2down","bkg12down",]:
#i=''
	rebinna=10
	signalzoom=2
	minx=0
	maxx=0
	if 'topmass' in i and '_' not in i:
		minx=50
		maxx=300
	if 'wmass' in i and '_' not in i:
		minx=50
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
	make_ratioplot(
		name=i,
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
		logy=False,
        xtitle='',
        ytitle='Events',
        textsizefactor=1,
        signal_legend=signalWB_legendnames,
        separate_legend=True,
        signal_zoom=signalzoom,
        fixratio=True,
        #signal_colors=[1,2,3,1,2,3,1,2]
        )

for i in [
  "zprimemass",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  "ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  "lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  "antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",  "antibcsvCR_zprimemass",  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
"ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 "antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 "antibcsvCRmass_zprimemass", "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 "antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 "antibcsvCRbtag_zprimemass", "antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass",
  "antibcsvCRnobtag_zprimemass",  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
  "bkg1","bkg2","bkg12","bkg1up","bkg2up","bkg12up","bkg1down","bkg2down","bkg12down",]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot(
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

	make_ratioplot(
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
  "zprimemass",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  "ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  "lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  "antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",  "antibcsvCR_zprimemass",  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
  "ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 "antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 "antibcsvCRmass_zprimemass", "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 "antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 "antibcsvCRbtag_zprimemass", "antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass", 
 "antibcsvCRnobtag_zprimemass",  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
 "bkg1","bkg2","bkg12","bkg1up","bkg2up","bkg12up","bkg1down","bkg2down","bkg12down",]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot(
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

	make_ratioplot(
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
  "zprimemass",  "zprimemassbtag",  "zprimemassnobtag",  "zprimemassbmass",  "zprimemassnobmass",
  "ttbarCR_zprimemass",  "ttbarCR_zprimemassbtag",
  "lowmassCR_zprimemass",  "lowmassCR_zprimemassbtag",
  "antitopmassCR_zprimemass",  "antitopnsubCR_zprimemass",  "antiwmassCR_zprimemass",  "antiwnsubCR_zprimemass",  "antibcsvCR_zprimemass",  "antibptCR_zprimemass",  "antibmassCR_zprimemass",
  "ttbarCR_zprimemass_low", "ttbarCR_zprimemassbtag_low", "lowmassCR_zprimemass_low", "lowmassCR_zprimemassbtag_low", 
 "antitopmassCRmass_zprimemass", "antitopnsubCRmass_zprimemass", "antiwmassCRmass_zprimemass", "antiwnsubCRmass_zprimemass", 
 "antibcsvCRmass_zprimemass", "antibptCRmass_zprimemass", "antibmassCRmass_zprimemass", 
 "antitopmassCRbtag_zprimemass", "antitopnsubCRbtag_zprimemass", "antiwmassCRbtag_zprimemass", "antiwnsubCRbtag_zprimemass", 
 "antibcsvCRbtag_zprimemass", "antibptCRbtag_zprimemass", "antibmassCRbtag_zprimemass",
"antitopmassCRnobtag_zprimemass",  "antitopnsubCRnobtag_zprimemass",  "antiwmassCRnobtag_zprimemass",  "antiwnsubCRnobtag_zprimemass", 
 "antibcsvCRnobtag_zprimemass",  "antibptCRnobtag_zprimemass",  "antibmassCRnobtag_zprimemass",
 "bkg1","bkg2","bkg12","bkg1up","bkg2up","bkg12up","bkg1down","bkg2down","bkg12down",]:
 	rebinna=10
	minx=0
	maxx=0
	# if i=='topmass':
	# 	minx=100
	# 	maxx=300
	make_ratioplot(
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
        qcd_legend='Control region (QCD MC)',
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

	make_ratioplot(
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

outfile.Close()

dotheta=True
if dotheta:
	rebinna=10
	u='_'
	uu='__'
	signal_filesWB=[]
	signal_filesZT=[]
	signal_filesHT=[]
	for i in signalWB_names:
		signal_filesWB.append(TFile(path+filename_base+i+root,'READ'))
	for i in signalZT_names:
		signal_filesZT.append(TFile(path+filename_base+i+root,'READ'))
	for i in signalHT_names:
		signal_filesHT.append(TFile(path+filename_base+i+root,'READ'))
	nscan=10
	counter=1
	filecounter=1
	onebtag='Selection/zprimemassnobtag'
	twobtags='Selection/zprimemassbtag'
	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		thetafile=TFile('theta/theta'+filename_postfix+'.root','RECREATE')
		thetafile.cd()
		allhad2btag__qcd=qcd_file.Get(twobtags).Clone()
		allhad1btag__qcd=qcd_file.Get(onebtag).Clone()
		allhad2btag__ttbar=ttbar_file.Get(twobtags).Clone()
		allhad1btag__ttbar=ttbar_file.Get(onebtag).Clone()
		allhad2btag__DATA=data_file.Get(twobtags).Clone()
		allhad1btag__DATA=data_file.Get(onebtag).Clone()
		allhad2btag__qcd.Rebin(rebinna)
		allhad1btag__qcd.Rebin(rebinna)
		allhad2btag__ttbar.Rebin(rebinna)
		allhad1btag__ttbar.Rebin(rebinna)
		allhad2btag__DATA.Rebin(rebinna)
		allhad1btag__DATA.Rebin(rebinna)
		allhad2btag__qcd.Write('allhad2btag__qcd')
		allhad1btag__qcd.Write('allhad1btag__qcd')
		allhad2btag__ttbar.Write('allhad2btag__ttbar')
		allhad1btag__ttbar.Write('allhad1btag__ttbar')
		allhad2btag__DATA.Write('allhad2btag__DATA')
		allhad1btag__DATA.Write('allhad1btag__DATA')

		for masspoint in range(len(signalWB_names)):
			allhad2btag__signalWB=signal_filesWB[masspoint].Get(twobtags).Clone()
			allhad2btag__signalZT=signal_filesZT[masspoint].Get(twobtags).Clone()
			allhad2btag__signalHT=signal_filesHT[masspoint].Get(twobtags).Clone()
			#allhad2btag__signalWB.Sumw2()
			#allhad2btag__signalZT.Sumw2()
			#allhad2btag__signalHT.Sumw2()
			allhad2btag__signalWB.Scale(triplet[0])
			allhad2btag__signalHT.Scale(triplet[1])
			allhad2btag__signalZT.Scale(triplet[2])
			allhad2btag__signal=allhad2btag__signalWB
			allhad2btag__signal.Add(allhad2btag__signalHT)
			allhad2btag__signal.Add(allhad2btag__signalZT)
			allhad2btag__signal.Rebin(rebinna)

			allhad1btag__signalWB=signal_filesWB[masspoint].Get(onebtag).Clone()
			allhad1btag__signalZT=signal_filesZT[masspoint].Get(onebtag).Clone()
			allhad1btag__signalHT=signal_filesHT[masspoint].Get(onebtag).Clone()
			#allhad1btag__signalWB.Sumw2()
			#allhad1btag__signalZT.Sumw2()
			#allhad1btag__signalHT.Sumw2()
			allhad1btag__signalWB.Scale(triplet[0])
			allhad1btag__signalHT.Scale(triplet[1])
			allhad1btag__signalZT.Scale(triplet[2])
			allhad1btag__signal=allhad1btag__signalWB
			allhad1btag__signal.Add(allhad1btag__signalHT)
			allhad1btag__signal.Add(allhad1btag__signalZT)
			allhad1btag__signal.Rebin(rebinna)

			allhad2btag__signal.Write('allhad2btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
				str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))
			allhad1btag__signal.Write('allhad1btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
				str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))
			counter+=1
		thetafile.Close()
		theta_config = open('theta/model'+filename_postfix+'.py','w')
		theta_config.write("def get_model():\n\
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_15_patch1/src/UHH2/ZprimeAllHadronic/python/theta/theta"+filename_postfix+".root', include_mc_uncertainties = True)#mc uncertainties=true\n\
    model.fill_histogram_zerobins()\n\
    model.set_signal_processes('signal*')\n\
    model.add_lognormal_uncertainty('ttbar_rate', 0.15, 'ttbar')\n\
    model.add_lognormal_uncertainty('qcd_rate', 0.15, 'qcd')\n\
    for p in model.processes:\n\
        if p == 'qcd': continue\n\
        model.add_lognormal_uncertainty('lumi', 0.026, p)\n\
        if 'signal' in p:\n\
            model.add_lognormal_uncertainty(p+'_rate', 0.15, p)\n\
    return model\n\
model = get_model()\n\
model_summary(model)\n\
options = Options()\n\
options.set('main', 'n_threads', '20')\n\
plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'\n\
plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_15_patch1/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp"+filename_postfix+".txt')\n\
#plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_15_patch1/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs"+filename_postfix+".txt')\n\
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_15_patch1/src/UHH2/ZprimeAllHadronic/python/theta/htmlout"+filename_postfix+"')")
		filecounter+=1


			


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

qcdsfbtag=qcd_file.Get("Selection/zprimemassbtag").Integral()/qcd_file.Get("Selection/antibcsvCRbtag_zprimemass").Integral()
qcdsfnobtag=qcd_file.Get("Selection/zprimemassnobtag").Integral()/qcd_file.Get("Selection/antibcsvCRnobtag_zprimemass").Integral()
print 'btag',qcdsfbtag
print 'nobtag',qcdsfnobtag

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
	
