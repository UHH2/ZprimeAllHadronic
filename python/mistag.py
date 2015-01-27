from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,domistag
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/phys14-3/'
outfile=TFile('mistag.root','RECREATE')
filenames=['uhh2.AnalysisModuleRunner.MC.QCDHT1000ToInf','uhh2.AnalysisModuleRunner.MC.QCDHT1000ToInfExt','uhh2.AnalysisModuleRunner.MC.QCDHT500To1000','uhh2.AnalysisModuleRunner.MC.QCDHT500To1000Ext']
filename=hadd(path,'',filenames,'mistag_added')
qcdfile=TFile(filename,'READ')

domistag(qcdfile,outfile,'Mistag/mistag2D_den','Mistag/mistag2D_num','CMSTT')
compare('mistag',[outfile,outfile,outfile],['Mistag_px2_CMSTT','Mistag_px3_CMSTT','Mistag_px4_CMSTT'],['#beta_{max}#in [0, 0.423]','#beta_{max}#in [0.423, 0.814]','#beta_{max}#in [0.814, 1]'],False,'hE','m_{t#bar{t}} [GeV]','Misidentification rate')

mass_shape=qcdfile.Get('Mistag/mass_shape').Clone('mass_shape')
mass_shape.Rebin(4)
mass_shape.Write()
compare('mass_shape',[outfile],['mass_shape'],['Mass shape'],True,'hE','m_{t#bar{t}} [GeV]','Fraction of events',100,300)

compare('closure',[qcdfile,qcdfile],['Selection/m12CMS','Background/m12CMS'],['Selected MC QCD', 'Predicted MC QCD'],True,'hE','m_{t#bar{t}} [GeV]','Fraction of events',500,4000,5)

