from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array

from utils import compare,hadd,doeff,make_plot,make_ratioplot
gROOT.SetBatch()

#setup
path='/nfs/dust/cms/user/usaiem/selection/'
prepath='/nfs/dust/cms/user/usaiem/preselection2/'
prepath2='/nfs/dust/cms/user/usaiem/preselection2/'
syspath='/nfs/dust/cms/user/usaiem/sys/'
# path2='/nfs/dust/cms/user/usaiem/phys14-2/'
root='.root'
filename_base='uhh2.AnalysisModuleRunner.'
signal_names=[
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
'MC.ZpToTpT_TpToHT_MZp2500Nar_MTp1500Nar_LH',
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
'MC.ZpToTpT_TpToZT_MZp2500Nar_MTp1500Nar_LH',
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

signal_legends=[
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(700\\GeV)\\rightarrow Wb$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Wb$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Wb$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Wb$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Wb$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Wb$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Wb$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Wb$ & ",

"$Z'(1500\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Ht$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(700\\GeV)\\rightarrow Ht$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Ht$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Ht$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Ht$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Ht$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Ht$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Ht$ & ",

"$Z'(1500\\GeV)\\rightarrow T't$, $T'(700\\GeV)\\rightarrow Zt$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Zt$ & ",
"$Z'(1500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Zt$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(900\\GeV)\\rightarrow Zt$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Zt$ & ",
"$Z'(2000\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Zt$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1200\\GeV)\\rightarrow Zt$ & ",
"$Z'(2500\\GeV)\\rightarrow T't$, $T'(1500\\GeV)\\rightarrow Zt$ & ",
]

for i in range(len(signal_names)):
	pre=TFile(prepath+filename_base+signal_names[i]+root,'READ')
	sel=TFile(path+filename_base+signal_names[i]+root,"READ")
	denplot=pre.Get('NoCutsSub/Nevts')
	den=denplot.Integral()
	numplot1=sel.Get('Selection/zprimemassnobtag')
	numplot2=sel.Get('Selection/zprimemassbtag')
	num1=numplot1.Integral()
	num2=numplot2.Integral()
	eff=(num1+num2)*100/den
	eff1=(num1)*100/den
	eff2=(num2)*100/den
	#print signal_legends[i], "%.0f" % den,'&',"%.0f" % num1,'&',"%.0f" % num2,'&', "%.1f" % eff,'\% \\\\'
	#print eff,eff1,eff2
	print signal_legends[i],"%.1f" % eff1,'\% &', "%.1f" % eff2,'\% \\\\'