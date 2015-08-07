from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,doeff,make_plot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/spring15/'
# path2='/nfs/dust/cms/user/usaiem/phys14-2/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.MC.'
signal_names=['ZpTpTbW','ZpTpTtZ']#['newzp1000','newzp2000','newzp3000','newzp4000']#'Z1000W100','Z2000W200','Z3000W300'
qcd_names=['MC_QCD_Pt1000to1400','MC_QCD_Pt120to170','MC_QCD_Pt1400to1800','MC_QCD_Pt15to30','MC_QCD_Pt170to300','MC_QCD_Pt1800to2400','MC_QCD_Pt2400to3200','MC_QCD_Pt300to470','MC_QCD_Pt30to50','MC_QCD_Pt3200toInf','MC_QCD_Pt470to600','MC_QCD_Pt50to80','MC_QCD_Pt600to800','MC_QCD_Pt800to1000','MC_QCD_Pt80to120',]#'QCDHT1000ToInf',,'QCDHT500To1000'
#qcd_names=['QCDHT1000ToInf','QCDHT500To1000']#'QCDHT1000ToInf',,'QCDHT500To1000'
ttbar_name='TTbar'
# ttbar50ns_name='TTbar50ns'
outfile=TFile('outfile.root','RECREATE')


# #merge qcd
qcd_filename=hadd(path,filename_base,qcd_names,'qcd_added',True)
# #open files
qcd_file=TFile(qcd_filename,'READ')
ttbar_file=TFile(path+filename_base+ttbar_name+root,'READ')
# # ttbar50ns_file=TFile(path+filename_base+ttbar50ns_name+root,'READ')
signal_files=[]
for i in signal_names:
	signal_files.append(TFile(path+filename_base+i+root,'READ'))
# signal_files.append(TFile(path2+filename_base+signal_names[2]+root,'READ'))	
# signal_files.append(TFile(path2+filename_base+signal_names[2]+root,'READ'))
# signal_files.append(TFile(path2+filename_base+signal_names[4]+root,'READ'))
# # signal_files.append(TFile(path2+filename_base+'newzp'+root,'READ'))
# signal_files.append(TFile(path2+filename_base+signal_names[0]+root,'READ'))
# signal_files.append(TFile(path+filename_base+'newzp'+root,'READ'))

rebinna=10

for i in ['step1_wmass','step1_wnsub','step1_tcsv','step1_tpt','step2_bcsv','step2_wpt','step3_tprimemass','step3_tprimept','step4_zprimemass','step4_zprimemassbtag','step4_zprimemassbtagnsub']:
	make_plot(i, ttbar_file, qcd_file, signal_files, 'NoCuts/'+i,'NoCuts/'+i,rebin=rebinna,minx=500,maxx=4000,miny=0.1,maxy=10000,logy=True)
	


# thetafile=TFile('theta.root','RECREATE')
# thetafile.cd()
# for i in ['0','1','2']:
# 	ttbar_file.Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__ttbar')
# 	qcd_file.Get('Background'+i+'/m12CMS').Write('allhad'+i+'btag__qcd')
# 	signal_files[1].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp1000')
# 	signal_files[3].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp2000')
# 	signal_files[5].Get('Selection'+i+'/m12CMS').Write('allhad'+i+'btag__zp3000')
# thetafile.Close()

# outfile.cd()

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

# compare('mttbar',[signal_files[0]]*1,['Selection/m12CMS'],['13TeV Data'],False,'hE','mttbar [GeV]','Events',0,5000,rebin=6,textsizefactor=0.75)
# compare('mww',[signal_files[0]]*1,['ww/m12AK8'],['13TeV Data'],False,'hE','mww [GeV]','Events',0,5000,rebin=6,textsizefactor=0.75,logy=True,miny=0.5,maxy=1000)
# compare('mww2',[signal_files[0]]*1,['tev/m12AK8'],['13TeV Data'],False,'hE','mww [GeV]','Events',0,5000,rebin=6,textsizefactor=0.75,logy=True,miny=0.5,maxy=10000)
# compare('mtv',[signal_files[0]]*1,['tev/m12AK8CMS'],['13TeV Data'],False,'hE','mtw [GeV]','Events',400,5000,rebin=6,textsizefactor=0.75,logy=True,miny=0.5,maxy=10000)
# compare('mtv2',[signal_files[0]]*1,['tev/m12CMSAK8'],['13TeV Data'],False,'hE','mtw [GeV]','Events',400,5000,rebin=6,textsizefactor=0.75,logy=True,miny=0.5,maxy=10000)

# for i in ['m1','m2','m12','pT1','pT2','nsub_1CMS','nsub_2CMS','csv_1','csv_2','mmin1','mmin2','ndau1','ndau2']:

# 	#compare(i+'_new',[signal_files[1]]*2,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'_patJetsCmsTopTagPuppiPacked'],['CMS chs','CMS puppi'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
# 	#compare(i+'_new2',[signal_files[1]]*4,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 chs pruned','CA8 puppi pruned','CA8 chs sd','CA8 puppi sd'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
# 	#compare(i+'_new4',[signal_files[1]]*7,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8CHSJets','NoCutsGen/'+i+'_patJetsCa8PuppiJets','NoCutsGen/'+i+'CMS'],['CA8 chs pruned','CA8 puppi pruned','CA8 chs sd','CA8 puppi sd','CA8 CHS','CA8 puppi','CMS'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
# 	#compare(i+'_new3',[signal_files[1]]*2,['NoCutsGen/'+i+'_patJetsCa15CHSJetsFilteredPacked','NoCutsGen/'+i+'_patJetsCa15PuppiJetsFilteredPacked'],['CA15 chs filtered','CA15 puppi filtered'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
	
# 	if i in ['m1','m2','m12']:
# 		lim=400
# 		rb=4
# 		if i=='m12':
# 			lim=4000
# 			rb=1
# 		compare(i+'_1tev',[signal_files[0]]*8,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'CMSfat','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'AK4x3R8','NoCutsGen/'+i+'AK4x4R8','NoCutsGen/'+i+'AK4x3R15','NoCutsGen/'+i+'AK4x4R15'],['CMS','CMSfat','AK8','CA15','AK4x3R8','AK4x4R8','AK4x3R15','AK4x4R15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_2tev',[signal_files[1]]*8,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'CMSfat','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'AK4x3R8','NoCutsGen/'+i+'AK4x4R8','NoCutsGen/'+i+'AK4x3R15','NoCutsGen/'+i+'AK4x4R15'],['CMS','CMSfat','AK8','CA15','AK4x3R8','AK4x4R8','AK4x3R15','AK4x4R15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_3tev',[signal_files[2]]*8,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'CMSfat','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'AK4x3R8','NoCutsGen/'+i+'AK4x4R8','NoCutsGen/'+i+'AK4x3R15','NoCutsGen/'+i+'AK4x4R15'],['CMS','CMSfat','AK8','CA15','AK4x3R8','AK4x4R8','AK4x3R15','AK4x4R15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_4tev',[signal_files[3]]*8,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'CMSfat','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'AK4x3R8','NoCutsGen/'+i+'AK4x4R8','NoCutsGen/'+i+'AK4x3R15','NoCutsGen/'+i+'AK4x4R15'],['CMS','CMSfat','AK8','CA15','AK4x3R8','AK4x4R8','AK4x3R15','AK4x4R15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 	elif i in ['pT1','pT2','csv_1','csv_2']:
# 		lim=2000
# 		rb=1
# 		if 'pT' in i:
# 			rb=8
# 		compare(i+'_1tev',[signal_files[0]]*3,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15'],['CMS','AK8','CA15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_2tev',[signal_files[1]]*3,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15'],['CMS','AK8','CA15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_3tev',[signal_files[2]]*3,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15'],['CMS','AK8','CA15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 		compare(i+'_4tev',[signal_files[3]]*3,['NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'AK8','NoCutsGen/'+i+'CA15'],['CMS','AK8','CA15'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=rb)
# 	elif i in ['nsub_1CMS','nsub_2CMS','mmin1','mmin2','ndau1','ndau2']:
# 		compare(i+'_1tev',[signal_files[0]]*1,['NoCutsGen/'+i],['CMS'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=1)
# 		compare(i+'_2tev',[signal_files[1]]*1,['NoCutsGen/'+i],['CMS'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=1)
# 		compare(i+'_3tev',[signal_files[2]]*1,['NoCutsGen/'+i],['CMS'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=1)
# 		compare(i+'_4tev',[signal_files[3]]*1,['NoCutsGen/'+i],['CMS'],True,'histo',i+' [GeV]','Fraction of events',0,lim,rebin=1)
	#compare(i+'_new3tev',[signal_files[2]]*7,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8CHSJets','NoCutsGen/'+i+'_patJetsCa8PuppiJets','NoCutsGen/'+i+'CMS'],['CA8 chs pruned','CA8 puppi pruned','CA8 chs sd','CA8 puppi sd','CA8 CHS','CA8 puppi','CMS'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',2000,4000,rebin=1)
	#compare(i+'_newqcd',[qcd_file]*7,['NoCuts/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCuts/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCuts/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCuts/'+i+'_patJetsCa8PuppiJetsSoftDropPacked','NoCuts/'+i+'_patJetsCa8CHSJets','NoCuts/'+i+'_patJetsCa8PuppiJets','NoCuts/'+i+'CMS'],['CA8 chs pruned','CA8 puppi pruned','CA8 chs sd','CA8 puppi sd','CA8 CHS','CA8 puppi','CMS'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,2500,rebin=1)

# compare(i+'_dpg2tev',[signal_files[1]]*4,['SelectionGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',500,2500,rebin=1,textsizefactor=0.75)
# compare(i+'_dpg1tev',[signal_files[0]]*4,['SelectionGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,2000,rebin=1)
# compare(i+'_dpg3tev',[signal_files[2]]*4,['SelectionGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','SelectionGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','SelectionGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,4000,rebin=2)
# compare(i+'_dpgqcd',[qcd_file]*4,['Selection/'+i+'_patJetsCa8CHSJetsPrunedPacked','Selection/'+i+'_patJetsCa8PuppiJetsPrunedPacked','Selection/'+i+'_patJetsCa8CHSJetsSoftDropPacked','Selection/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,2500,rebin=3)

# i='m1'
# compare(i+'_dpg2tev',[signal_files[1]]*4,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,300,rebin=1,textsizefactor=0.75)
# compare(i+'_dpg1tev',[signal_files[0]]*4,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,300,rebin=1)
# compare(i+'_dpg3tev',[signal_files[2]]*4,['NoCutsGen/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCutsGen/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCutsGen/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,300,rebin=1)
# compare(i+'_dpgqcd',[qcd_file]*4,['NoCuts/'+i+'_patJetsCa8CHSJetsPrunedPacked','NoCuts/'+i+'_patJetsCa8PuppiJetsPrunedPacked','NoCuts/'+i+'_patJetsCa8CHSJetsSoftDropPacked','NoCuts/'+i+'_patJetsCa8PuppiJetsSoftDropPacked'],['CA8 CHS pruned','CA8 PUPPI pruned','CA8 CHS soft drop','CA8 PUPPI soft drop'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',0,300,rebin=1)

# for i in ['m12']:
# 	maxx=0
# 	if 'm1' in i or 'm2' in i:
# 		maxx=600
# 	if 'm12' in i:
# 		maxx=3000
# 	if 'pT' in i:
# 		maxx=1400
	# compare(i+'_NoCutGen_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['NoCutsGen/'+i+'AK4x4R15','NoCutsGen/'+i+'CA15','NoCutsGen/'+i+'CMS','NoCutsGen/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,rebin=1)
	# compare(i+'_SelGen_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['SelectionGen/'+i+'AK4x4R15','SelectionGen/'+i+'CA15','SelectionGen/'+i+'CMS','SelectionGen/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,1)
	# compare(i+'_Sel_jet',[signal_files[-1],signal_files[-1],signal_files[-1],signal_files[-1]],['Selection/'+i+'AK4x4R15','Selection/'+i+'CA15','Selection/'+i+'CMS','Selection/'+i+'gen'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet','CMS gen. Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',1000,2500,1)
	# compare(i+'_Sel_jetqcd',[qcd_file,qcd_file,qcd_file],['Selection/'+i+'AK4x4R15','Selection/'+i+'CA15','Selection/'+i+'CMS'],['up to 4 closest AK4 to CMSJet within R=1.5','CA15 filtered','CMSTT Jet'],True,'histo','m_{t#bar{t}} [GeV]','Fraction of events',100,2500,4)
	# # compare(i+'_Pre_jet',[signal_files[2],signal_files[2],signal_files[2],signal_files[2]],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
	# compare(i+'_NoCut_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'histo',i,'Fraction of events',0.001,maxx,1)

	# compare(i+'_NoCut_JEC',[signal_files[2],signal_files[6]],['NoCuts/'+i+'CMS','NoCuts/'+i+'CMS'],['CMSTT subjets corrected with AK4 JEC','CMSTT subjets uncorrected'],True,'histo',i,'Fraction of events',0.001,maxx,1)
	# maxx=4000
	# compare(i+'_NoCut_jet3',[signal_files[4],signal_files[4],signal_files[4],signal_files[4]],['NoCuts/'+i+'CA8','NoCuts/'+i+'CA15','NoCuts/'+i+'CMS','NoCuts/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'histo',i,'Fraction of events',1000,maxx,1)
	# compare(i+'_NoCut_JEC3',[signal_files[4],signal_files[7]],['NoCuts/'+i+'CMS','NoCuts/'+i+'CMS'],['CMSTT subjets corrected with AK4 JEC','CMSTT subjets uncorrected'],True,'histo',i,'Fraction of events',1000,maxx,1)
	# compare(i+'_Pre_jetqcd',[qcd_file,qcd_file,qcd_file,qcd_file],['Preselection/'+i+'CA8','Preselection/'+i+'CA15','Preselection/'+i+'CMS','Preselection/'+i+'HEP'],['CA8 pruned','CA15 filtered','CMSTT','HEPTT'],True,'hE',i,maxx)
# #trigger
# doeff(signal_files[-2], 'trieffden/HT','HTtrieffnum/HT', 'HTTrigger_1TeV', outfile)
# doeff(ttbar_file, 'trieffden/HT','HTtrieffnum/HT', 'HTTrigger_ttbar', outfile,2)
# compare('HTTrigger_1TeV',[outfile],['HTTrigger_1TeV'],["PFHT900 efficiency (Z' 1 TeV)"],xtitle='HT [GeV]',minx=800,maxx=1800,drawoption='')
# compare('HTTrigger_ttbar',[outfile],['HTTrigger_ttbar'],['HTTrigger_ttbar'],False,'','HT [GeV]',4000)
# doeff(signal_files[-2], 'trieffden/pT1CA8','AK8trieffnum/pT1CA8', 'AK8Trigger_1TeV', outfile,2)
# doeff(ttbar_file, 'trieffden/pT1CA8','AK8trieffnum/pT1CA8', 'AK8Trigger_ttbar', outfile,2)
# compare('AK8Trigger_1TeV',[outfile],['AK8Trigger_1TeV'],["AK8PFJet360TrimModMass30 eff. (Z' 1 TeV)"],False,'','pT1 [GeV]')
# compare('AK8Trigger_ttbar',[outfile],['AK8Trigger_ttbar'],['AK8Trigger_ttbar'],False,'','pT1 [GeV]',2000)

#jet response
# compare('responsevspt',[signal_files[-1]],['NoCutsGen/ptratioVSpt'],['CMS TopJet response'],minx=200,maxx=1200, miny=0.95,maxy=1.05,drawoption='E',xtitle='p_{T,gen} [GeV]',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8)
# compare('responsevsnpv',[signal_files[-1]],['NoCutsGen/ptratioVSnpv'],['CMS TopJet response'],minx=8,maxx=34, miny=0.95,maxy=1.05,drawoption='E',xtitle='N_{pv}',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8)
# compare('responseak4',[signal_files[-1]],['NoCutsGen/ptratioVSptAK4'],['AK4 response'],minx=50,maxx=1500, miny=0.9,maxy=1.1,drawoption='E',xtitle='p_{T,gen} [GeV]',ytitle='p_{T,reco}/p_{T,gen}',textsizefactor=0.8,rebin=5)

#stack
# make_plot('Selection0', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection0/m12CMS','Background0/m12CMS',4,500,4000,1,10000,True)
# make_plot('Selection1', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection1/m12CMS','Background1/m12CMS',4,500,4000,1,10000,True)
# make_plot('Selection2', ttbar_file, qcd_file, [signal_files[0],signal_files[2],signal_files[4]], 'Selection2/m12CMS','Background2/m12CMS',4,500,4000,1,1000,True)


outfile.Close()