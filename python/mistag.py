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

mass_shape=qcdfile.Get('Mistag/mass_shape').Clone('mass_shape')
mass_shape.Rebin(4)
mass_shape.Write()
compare('mass_shape',[outfile],['mass_shape'],'Mass shape',False,'hE','m_{t#bar{t}}')