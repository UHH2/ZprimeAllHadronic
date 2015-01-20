from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/phys14/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.MC.'
signal_names=['Z1000W10','Z1000W100','Z2000W20','Z2000W200','Z3000W30','Z3000W300']
qcd_names=['QCDHT1000ToInf','QCDHT1000ToInfExt','QCDHT500To1000','QCDHT500To1000Ext']
ttbar_name='TTbar'
ttbar50ns_name='TTbar50ns'

#merge qcd
qcd_filename=hadd(path,filename_base,qcd_names,'qcd_added')
#open files
qcd_file=TFile(qcd_filename,'READ')
ttbar_file=TFile(path+filename_base+ttbar_name+root,'READ')
ttbar50ns_file=TFile(path+filename_base+ttbar50ns_name+root,'READ')
signal_files=[]
for i in signal_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))


#'NoCuts/' 'Preselection/	'
#pileup
for i in ['N_pv','m1CA8','m2CA8','m12CA8','m1CMS','m2CMS','m12CMS','pT1CMS','pT2CMS','HT']:
	maxx=0
	if 'm12' in i:
		maxx=3000
	if 'HT' in i:
		maxx=3000
	if 'm1C' in i or 'm2C' in i:
		maxx=600
	if 'pT' in i:
		maxx=1400
	compare(i+'_NoCut_25vs50ns',[ttbar_file,ttbar50ns_file],['NoCuts/'+i,'NoCuts/'+i],['PU=20 BX=25ns','PU=4 BX=50ns'],True,'hE',i,maxx)
	compare(i+'_Pre_25vs50ns',[ttbar_file,ttbar50ns_file],['Preselection/'+i,'Preselection/'+i],['PU=20 BX=25ns','PU=4 BX=50ns'],True,'hE',i,maxx)
#btagging
for i in ['csv_1','csv_2']:
	compare(i+'_NoCut_btag',[ttbar_file,qcd_file],['NoCuts/'+i,'NoCuts/'+i],['t#bar{t}','QCD'],True,'hE',i,maxx)
	compare(i+'_Pre_btag',[ttbar_file,qcd_file],['Preselection/'+i,'Preselection/'+i],['t#bar{t}','QCD'],True,'hE',i,maxx)
	compare(i+'_NoCut_Zbtag',[signal_files[0],signal_files[2],signal_files[4]],['NoCuts/'+i,'NoCuts/'+i,'NoCuts/'+i],["Z' 1TeV","Z' 2TeV","Z' 3TeV"],True,'hE',i,maxx)
	compare(i+'_Pre_Zbtag',[signal_files[0],signal_files[2],signal_files[4]],['Preselection/'+i,'Preselection/'+i,'Preselection/'+i],["Z' 1TeV","Z' 2TeV","Z' 3TeV"],True,'hE',i,maxx)
#jet
for i in ['m1','m2','m12','pT1','pT2']:
	maxx=0
	if 'm1' in i or 'm2' in i:
		maxx=600
	if 'm12' in i:
		maxx=3000
	if 'pT' in i:
		maxx=1400
	compare(i+'_NoCut_jet',[signal_files[2],signal_files[2],signal_files[2],signal_files[2]],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
	compare(i+'_Pre_jet',[signal_files[2],signal_files[2],signal_files[2],signal_files[2]],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
	compare(i+'_NoCut_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
	compare(i+'_Pre_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)