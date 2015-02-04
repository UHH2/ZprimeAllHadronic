from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,doeff,make_plot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/phys14-4/'
path2='/nfs/dust/cms/user/usaiem/phys14-3/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.MC.'
signal_names=['Z1000W10','Z1000W100','Z2000W20','Z2000W200','Z3000W30','Z3000W300']
qcd_names=['QCDHT1000ToInf','QCDHT1000ToInfExt','QCDHT500To1000','QCDHT500To1000Ext']
ttbar_name='TTbar'
ttbar50ns_name='TTbar50ns'
outfile=TFile('outfile.root','RECREATE')

#merge qcd
qcd_filename=hadd(path,filename_base,qcd_names,'qcd_added')
#open files
qcd_file=TFile(qcd_filename,'READ')
ttbar_file=TFile(path+filename_base+ttbar_name+root,'READ')
ttbar50ns_file=TFile(path+filename_base+ttbar50ns_name+root,'READ')
signal_files=[]
for i in signal_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))
signal_files.append(TFile(path2+filename_base+signal_names[2]+root,'READ'))
signal_files.append(TFile(path2+filename_base+signal_names[4]+root,'READ'))
# signal_files.append(TFile(path2+filename_base+'newzp'+root,'READ'))
signal_files.append(TFile(path2+filename_base+signal_names[0]+root,'READ'))
signal_files.append(TFile(path+filename_base+'newzp'+root,'READ'))


thetafile=TFile('theta.root','RECREATE')
thetafile.cd()
for i in ['0','1','2']:
	ttbar_file.Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__ttbar')
	qcd_file.Get('Background'+i+'/m12CMS').Write('allhad'+i+'btag__qcd')
	signal_files[1].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp1000')
	signal_files[3].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp2000')
	signal_files[5].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp3000')
thetafile.Close()

outfile.cd()

# #'NoCuts/' 'Preselection/	'
# #pileup
# for i in ['N_pv','m1CA8','m2CA8','m12CA8','m1CMS','m2CMS','m12CMS','pT1CMS','pT2CMS','HT']:
# 	maxx=0
# 	if 'm12' in i:
# 		maxx=3000
# 	if 'HT' in i:
# 		maxx=3000
# 	if 'm1C' in i or 'm2C' in i:
# 		maxx=600
# 	if 'pT' in i:
# 		maxx=1400
# 	compare(i+'_NoCut_25vs50ns',[ttbar_file,ttbar50ns_file],['NoCuts/'+i,'NoCuts/'+i],['PU=20 BX=25ns','PU=4 BX=50ns'],True,'hE',i,maxx)
# 	compare(i+'_Pre_25vs50ns',[ttbar_file,ttbar50ns_file],['Preselection/'+i,'Preselection/'+i],['PU=20 BX=25ns','PU=4 BX=50ns'],True,'hE',i,maxx)
# #btagging
# for i in ['csv_1','csv_2']:
# 	compare(i+'_NoCut_btag',[ttbar_file,qcd_file],['NoCuts/'+i,'NoCuts/'+i],['t#bar{t}','QCD'],True,'hE',i,maxx)
# 	compare(i+'_Pre_btag',[ttbar_file,qcd_file],['Preselection/'+i,'Preselection/'+i],['t#bar{t}','QCD'],True,'hE',i,maxx)
# 	compare(i+'_NoCut_Zbtag',[signal_files[0],signal_files[2],signal_files[4]],['NoCuts/'+i,'NoCuts/'+i,'NoCuts/'+i],["Z' 1TeV","Z' 2TeV","Z' 3TeV"],True,'hE',i,maxx)
# 	compare(i+'_Pre_Zbtag',[signal_files[0],signal_files[2],signal_files[4]],['Preselection/'+i,'Preselection/'+i,'Preselection/'+i],["Z' 1TeV","Z' 2TeV","Z' 3TeV"],True,'hE',i,maxx)
#jet
#for i in ['m1','m2','m12','pT1','pT2']:
for i in ['m12']:
	maxx=0
	if 'm1' in i or 'm2' in i:
		maxx=600
	if 'm12' in i:
		maxx=3000
	if 'pT' in i:
		maxx=1400
	compare(i+'_NoCutGen_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['NoCutsGen/'+i+'AK4x4R15','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
	compare(i+'_SelGen_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['SelectionGen/'+i+'AK4x4R15','SelectionGen/'+i+'CA15','SelectionGen/'+i+'CMS','SelectionGen/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,1)
	compare(i+'_Sel_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['Selection/'+i+'AK4x4R15','Selection/'+i+'CA15','Selection/'+i+'CMS','Selection/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,1)
	compare(i+'_Sel_jetqcd',[qcd_file,qcd_file,qcd_file],['Selection/'+i+'AK4x4R15','Selection/'+i+'CA15','Selection/'+i+'CMS'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',100,2500,4)
	# compare(i+'_Pre_jet',[signal_files[2],signal_files[2],signal_files[2],signal_files[2]],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
	compare(i+'_NoCut_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'histo',i,'Fraction of events',0.001,maxx,1)

	compare(i+'_NoCut_JEC',[signal_files[2],signal_files[6]],['NoCuts/'+i+'CMS','NoCuts/'+i+'CMS'],['CMSTT subjets corrected with AK4 JEC','CMSTT subjets uncorrected'],True,'histo',i,'Fraction of events',0.001,maxx,1)
	maxx=4000
	compare(i+'_NoCut_jet3',[signal_files[4],signal_files[4],signal_files[4],signal_files[4]],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'histo',i,'Fraction of events',1000,maxx,1)
	compare(i+'_NoCut_JEC3',[signal_files[4],signal_files[7]],['NoCuts/'+i+'CMS','NoCuts/'+i+'CMS'],['CMSTT subjets corrected with AK4 JEC','CMSTT subjets uncorrected'],True,'histo',i,'Fraction of events',1000,maxx,1)
	# compare(i+'_Pre_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
# #trigger
doeff(signal_files[-2], 'trieffden/HT','HTtrieffnum/HT', 'HTTrigger_1TeV', outfile)
# doeff(ttbar_file, 'trieffden/HT','HTtrieffnum/HT', 'HTTrigger_ttbar', outfile,2)
compare('HTTrigger_1TeV',[outfile],['HTTrigger_1TeV'],["PFHT900 efficiency (Z' 1 TeV)"],xtitle='HT [GeV]',minx=800,maxx=1800,drawoption='')
# compare('HTTrigger_ttbar',[outfile],['HTTrigger_ttbar'],['HTTrigger_ttbar'],False,'','HT [GeV]',4000)
doeff(signal_files[-2], 'trieffden/pT1CA8','AK8trieffnum/pT1CA8', 'AK8Trigger_1TeV', outfile,2)
# doeff(ttbar_file, 'trieffden/pT1CA8','AK8trieffnum/pT1CA8', 'AK8Trigger_ttbar', outfile,2)
compare('AK8Trigger_1TeV',[outfile],['AK8Trigger_1TeV'],["AK8PFJet360TrimModMass30 eff. (Z' 1 TeV)"],False,'','pT1 [GeV]')
# compare('AK8Trigger_ttbar',[outfile],['AK8Trigger_ttbar'],['AK8Trigger_ttbar'],False,'','pT1 [GeV]',2000)

#jet response
compare('responsevspt',[signal_files[-1]],['NoCutsGen/ptratioVSpt'],['CMS TopJet response'],minx=200,maxx=1200, miny=0.95,maxy=1.05,drawoption='E',xtitle='p_{T,gen} [GeV]',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8)
compare('responsevsnpv',[signal_files[-1]],['NoCutsGen/ptratioVSnpv'],['CMS TopJet response'],minx=8,maxx=34, miny=0.95,maxy=1.05,drawoption='E',xtitle='N_{pv}',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8)
compare('responseak4',[signal_files[-1]],['NoCutsGen/ptratioVSptAK4'],['AK4 response'],minx=50,maxx=1500, miny=0.9,maxy=1.1,drawoption='E',xtitle='p_{T,gen} [GeV]',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8,rebin=5)

#stack
make_plot('Selection0', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection0/m12CMS','Background0/m12CMS',4,500,4000,1,10000,True)
make_plot('Selection1', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection1/m12CMS','Background1/m12CMS',4,500,4000,1,10000,True)
make_plot('Selection2', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection2/m12CMS','Background2/m12CMS',4,500,4000,1,1000,True)


outfile.Close()