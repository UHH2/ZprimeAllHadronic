from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor,TGraphAsymmErrors,TGraph,kYellow,kRed,kGreen,kOrange,TLegend,kAzure
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array
import CMS_lumi
from ROOT.Math import Interpolator
from ROOT.Math import Interpolation


gROOT.SetBatch()

def set_palette(name='', ncontours=999):
    """Set a color palette from a given RGB list
    stops, red, green and blue should all be lists of the same length
    see set_decent_colors for an example"""

    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
        # (define more palettes)
    else:
        # default palette, looks cool
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

    s = array('d', stops)
    r = array('d', red)
    g = array('d', green)
    b = array('d', blue)

    npoints = len(s)
    TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    gStyle.SetNumberContours(ncontours)

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
"0p7",#0
"0p9",#1
"1p2",#2
"0p9",#3
"1p2",#4
#1p2",#
#1p2",#
"1p5",#5
#"1p2",#
"1p2",#6
"1p5",#7
]

signal_Zp_masses2=[
"1.5",
"1.5",
"1.5",
"2.0",
"2.0",
#"2",
#"2",
"2.0",
#"2",
"2.5",
"2.5",
]

signal_Tp_masses2=[
"0.7",
"0.9",
"1.2",
"0.9",
"1.2",
#1p2",
#1p2",
"1.5",
#"1p2",
"1.2",
"1.5",
]

theory_files=['ZPRIME_CS_lhc13tev_NNPDF30_nnlo_as_0118_q=0.5m.txt',
'ZPRIME_CS_lhc13tev_NNPDF30_nnlo_as_0118_q=1.0m.txt',
'ZPRIME_CS_lhc13tev_NNPDF30_nnlo_as_0118_q=2.0m.txt']

#theory1110=[1.4,0.38,0.021]
theory1110_pre=[1.4,1.87,1.57,1.28,1.01,0.38,0.34,0.258,0.18,0.132,0.106,0.042,0.021]
width1110_pre=[47,60.3,73.9,87.6,101,170,237,286,355,408,452,872,1050]
x1110_pre=[1.5,1.6,1.7,1.8,1.9,2.0,2.05,2.1,2.2,2.3,2.4,2.45,2.5]
#theory1410=[0.12*0.0494,0.03*0.2199,0.0087*0.1014]

# theory1410_zp=[0.1096, 0.0941941, 0.0812049, 0.0702895, 
#  0.0610887, 0.0531233, 0.0462985, 
#  0.040349, 0.035255, 0.0309674, 0.0272837,
#   0.0239634, 0.0210468, 0.018506, 
#  0.0162989, 0.0143873, 0.0127257, 
#  0.0112562, 0.00997291, 0.00885648, 
#  0.00788735]
# width1410=[50.5522, 55.6905, 61.152, 67.0003, 
#  73.239, 79.8582, 86.8438, 94.1805, 
#  101.853, 109.845, 118.143, 126.731, 
#  135.594, 144.72, 154.095, 163.705, 
#  173.537, 183.58, 193.822, 453.186, 
#  564.14]
# theory1410_br=[4.94822, 7.86529, 10.3043, 12.4474, 
#  14.3494, 16.0392, 17.5389, 18.8675, 
#  20.0425, 21.0798, 21.9938, 22.7977, 
#  23.5031, 24.1204, 24.6588, 25.1265, 
#  25.5309, 25.8783, 26.1744, 11.9094, 
#  10.1431]
from theory_data import theory1410_zp,width1410,theory1410_br
theory1410=[theory1410_zp[i]*theory1410_br[i]/100 for i in range(len(theory1410_zp))]
x1410=range(1500,2501,1)
width1410_rel=[100.0*width1410[i]/x1410[i] for i in range(len(x1410))]
x1410=[i/1000.0 for i in x1410]
nwa1410=0
for i in range(len(width1410_rel)):
	if width1410_rel[i]>10:
		nwa1410=i
		break
x_1410=array('d',x1410[:nwa1410+1])
x_1410_2=array('d',x1410[nwa1410:])
y_theory1410=array('d',theory1410[:nwa1410+1])
y_theory1410_2=array('d',theory1410[nwa1410:])
theory_curve_1410=TGraph(len(theory1410[:nwa1410+1]),x_1410,y_theory1410)
theory_curve_1410_2=TGraph(len(theory1410[nwa1410:]),x_1410_2,y_theory1410_2)

#print width1410_rel
#print x1410[nwa1410],width1410[nwa1410],width1410_rel[nwa1410]

theory_values=[]
for i in theory_files:
	pairs=[]
	the_file=open(i,'r')
	lines=the_file.readlines()
	for line in lines:
		splitted=filter(None, line.split(' '))
		#if float(splitted[0])>=1500 and float(splitted[0])<=2500:
		pairs.append([float(splitted[0])/1000,0.7*float(splitted[2])])
	theory_values.append(pairs)
	the_file.close()

def find_limit(theory,limit):
	return 0

x_theory=array('d',[theory_values[1][i][0] for i in range(len(theory_values[1]))])
y_theory=array('d',[theory_values[1][i][1] for i in range(len(theory_values[1]))])
y_theory_up=array('d',[abs(max(theory_values[0][i][1]-theory_values[1][i][1],theory_values[2][i][1]-theory_values[1][i][1])) for i in range(len(theory_values[1]))])
y_theory_down=array('d',[abs(min(theory_values[0][i][1]-theory_values[1][i][1],theory_values[2][i][1]-theory_values[1][i][1])) for i in range(len(theory_values[1]))])
theory_curve=TGraph(len(theory_values[1]),x_theory,y_theory)

x=array('d',[1.5,2.0,2.5])
# x_1110=array('d',x1110[:7])
# x_1110_2=array('d',x1110[6:])
# y_theory1110=array('d',theory1110[:7])
# y_theory1110_2=array('d',theory1110[6:])
# x_1110=array('d',x1110)
# x_1110_2=array('d',x1110[6:])
# y_theory1110=array('d',theory1110)
# y_theory1110_2=array('d',theory1110[6:])

# x_1410=array('d',x1410)
# y_theory1410=array('d',theory1410)
x1110=range(1500,2501,1)
x1110=[i/1000.0 for i in x1110]
x1110_pre_a=array('d',x1110_pre)
theory1110_pre_a=array('d',theory1110_pre)
width1110_pre_a=array('d',width1110_pre)
inter1110=Interpolator(len(x1110_pre), Interpolation.kAKIMA)
inter1110_w=Interpolator(len(x1110_pre), Interpolation.kAKIMA)
inter1110.SetData(len(x1110_pre), x1110_pre_a, theory1110_pre_a)
inter1110_w.SetData(len(x1110_pre), x1110_pre_a, width1110_pre_a)
width1110=[]
theory1110=[]
theory1110_rel=[]
nwa1110=0
for i in range(len(x1110)):
	theory1110.append(inter1110.Eval(x1110[i]))
	width1110.append(inter1110_w.Eval(x1110[i]))
	theory1110_rel.append(0.1*width1110[-1]/x1110[i])
	if theory1110_rel[-1]>10.0 and nwa1110==0:
		nwa1110=i

x_1110=array('d',x1110[:nwa1110+1])
x_1110_2=array('d',x1110[nwa1110:])
y_theory1110=array('d',theory1110[:nwa1110+1])
y_theory1110_2=array('d',theory1110[nwa1110:])
theory_curve_1110=TGraph(len(theory1110[:nwa1110+1]),x_1110,y_theory1110)
theory_curve_1110_2=TGraph(len(theory1110[nwa1110:]),x_1110_2,y_theory1110_2)
#theory_curve_1410=TGraph(len(theory1410),x_1410,y_theory1410)

theory_curve_1110.SetLineWidth(3)
theory_curve_1110.SetLineColor(kAzure)
theory_curve_1110.SetMarkerColor(kAzure)
theory_curve_1110_2.SetLineWidth(3)
theory_curve_1110_2.SetLineColor(kAzure)
theory_curve_1110_2.SetMarkerColor(kAzure)
theory_curve_1110_2.SetLineStyle(7)
theory_curve_1110_33=theory_curve_1110_2.Clone()
theory_curve_1110_33.SetLineColor(1)
theory_curve_1110_33.SetMarkerColor(1)

theory_curve_1410.SetLineWidth(3)
theory_curve_1410.SetLineColor(kGreen+3)
theory_curve_1410.SetMarkerColor(kGreen+3)
theory_curve_1410_2.SetLineWidth(3)
theory_curve_1410_2.SetLineColor(kGreen+3)
theory_curve_1410_2.SetMarkerColor(kGreen+3)
theory_curve_1410_2.SetLineStyle(7)

zeros_theory=array('d',[0 for i in range(len(theory_values[1]))])
theory_sigma=TGraphAsymmErrors(len(theory_values[1]),x_theory,y_theory,zeros_theory,zeros_theory,y_theory_down,y_theory_up)
#print theory_values
theory_curve.SetLineWidth(3)
theory_curve.SetLineColor(kRed)
theory_curve.SetMarkerColor(kRed)
#theory_sigma
b=TCanvas('theory_curve','',1200,1000)
b.SetLogy()
theory_sigma.Draw('a3')
#theory_curve.Draw('alp')
b.SaveAs('pdf/theory_curve.pdf')

doresults=True
if doresults:
	u='_'
	uu='__'
	nscan=10
	counter=1
	filecounter=1

	plotcounter=0
	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]+[[0.5,0.25,0.25]]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		theta_obs_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
		theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
		theta_exp_lines=theta_exp_result.readlines()
		theta_obs_lines=theta_obs_result.readlines()
		if triplet in [[0.5,0.25,0.25],[0.0,0.5,0.5]]:
			plotcounter=plotcounter+1
			c=TCanvas('unodlimit'+str(plotcounter),'',1200,1000)
			c.SetLogy()
			margine=0.15
			c.SetRightMargin(0.10)
			c.SetLeftMargin(margine)
			c.SetTopMargin(0.10)
			c.SetBottomMargin(margine)
			
			lines_exp=[filter(None, theta_exp_lines[2+1].split(' ')),filter(None, theta_exp_lines[4+1].split(' ')),filter(None, theta_exp_lines[6+1].split(' '))]
			lines_obs=[filter(None, theta_obs_lines[2+1].split(' ')),filter(None, theta_obs_lines[4+1].split(' ')),filter(None, theta_obs_lines[6+1].split(' '))]
			y_obs=array('d',[float(lines_obs[0][1]),
				         float(lines_obs[1][1]),
				         float(lines_obs[2][1])])
			y_exp=array('d',[float(lines_exp[0][1]),
				         float(lines_exp[1][1]),
				         float(lines_exp[2][1])])
			y_err2down=array('d',[
				float(lines_exp[0][1])-float(lines_exp[0][2]),
				float(lines_exp[1][1])-float(lines_exp[1][2]),
				float(lines_exp[2][1])-float(lines_exp[2][2])
				])
			y_err1down=array('d',[
				float(lines_exp[0][1])-float(lines_exp[0][4]),
				float(lines_exp[1][1])-float(lines_exp[1][4]),
				float(lines_exp[2][1])-float(lines_exp[2][4])
				])
			y_err1up=array('d',[
				float(lines_exp[0][5])-float(lines_exp[0][1]),
				float(lines_exp[1][5])-float(lines_exp[1][1]),
				float(lines_exp[2][5])-float(lines_exp[2][1])
				])
			y_err2up=array('d',[
				float(lines_exp[0][3])-float(lines_exp[0][1]),
				float(lines_exp[1][3])-float(lines_exp[1][1]),
				float(lines_exp[2][3])-float(lines_exp[2][1])
				])
			zeros=array('d',[0,0,0])
			exp1sigma=TGraphAsymmErrors(3,x,y_exp,zeros,zeros,y_err1down,y_err1up)
			exp2sigma=TGraphAsymmErrors(3,x,y_exp,zeros,zeros,y_err2down,y_err2up)
			explim=TGraph(3,x,y_exp)
			obslim=TGraph(3,x,y_obs)
			obslim.SetLineWidth(2)
			explim.SetLineWidth(2)
			explim.SetLineStyle(2)
			explim.SetTitle('')
			obslim.SetTitle('')
			exp2sigma.SetTitle('')
			exp1sigma.SetTitle('')
			#obslim.SetMinimum(0.001);
			#duesigma=TGraphAsymmErrors(3,)
			exp1sigma.SetFillColor(kGreen+1)
			exp2sigma.SetFillColor(kOrange)
			# exp2sigma.SetMaximum(150)
			# exp2sigma.SetMinimum(0.07)
			exp2sigma.SetMaximum(10000)
			if triplet[0]==0.0:
				exp2sigma.SetMinimum(0.0007)
			else:
				exp2sigma.SetMinimum(0.007)
			exp2sigma.Draw('a3lp')
			if triplet[0]==0.0:
				exp2sigma.GetXaxis().SetTitle("#rho^{0}_{L} mass [TeV]")
			else:
				exp2sigma.GetXaxis().SetTitle("G* mass [TeV]")
			exp2sigma.GetXaxis().SetRangeUser(1.4,2.6)
			exp2sigma.GetYaxis().SetTitle("Upper cross section limit [pb]")

			sizefactor=1.6
			exp2sigma.GetXaxis().SetTitleSize(sizefactor*exp2sigma.GetXaxis().GetTitleSize())
			exp2sigma.GetYaxis().SetTitleSize(sizefactor*exp2sigma.GetYaxis().GetTitleSize())
			exp2sigma.GetXaxis().SetLabelSize(sizefactor*exp2sigma.GetXaxis().GetLabelSize())
			exp2sigma.GetYaxis().SetLabelSize(sizefactor*exp2sigma.GetYaxis().GetLabelSize())
			#exp2sigma.GetYaxis().SetMoreLogLabels(1)
			offset=1.2
			exp2sigma.GetXaxis().SetTitleOffset(offset*exp2sigma.GetXaxis().GetTitleOffset())
			exp2sigma.GetYaxis().SetTitleOffset(offset*exp2sigma.GetYaxis().GetTitleOffset())

			exp1sigma.Draw('3')
			explim.Draw('lp')
			obslim.Draw('lp')
			#theory_curve.Draw('lp')

			if triplet[0]==0.0:
				theory_curve_1410.Draw('l')
				theory_curve_1410_2.Draw('l')
			else:
				theory_curve_1110.Draw('l')
				theory_curve_1110_2.Draw('l')

				#theory_curve_1110_3=theory_curve_1110.Clone()
				#theory_curve_1110_4=theory_curve_1110_2.Clone()

				#theory_curve_1110_3.Draw('c')
				#theory_curve_1110_4.Draw('c')
			

			legend=TLegend(0.335,0.55,0.9,0.9)
 			legend.SetTextSize(0.030)
  			legend.SetBorderSize(0)
  			legend.SetTextFont(42)
  			legend.SetLineColor(1)
  			legend.SetLineStyle(1)
  			legend.SetLineWidth(1)
  			legend.SetFillColor(0)
  			legend.SetFillStyle(0)
  			legend.SetHeader('#bf{#it{#Beta}}(T#rightarrow bW, tH, tZ) = 50%, 25%, 25%')
  			if triplet[0]==0.0:
  				legend.SetHeader('#bf{#it{#Beta}}(T#rightarrow tH, tZ) = 50%, 50%')
  			legend.AddEntry(obslim,'Observed','l')
  			legend.AddEntry(explim,'Expected','l')
  			legend.AddEntry(exp1sigma,'#pm 1 std. deviation','f')
  			legend.AddEntry(exp2sigma,'#pm 2 std. deviation','f')
  			#legend.AddEntry(theory_curve,"SSM Z'#rightarrow Tt, B(Z'#rightarrow Tt) = 70%",'l')
  			#legend.AddEntry(theory_curve_1110,"G*#rightarrow Tt (arXiv:1110.6058)",'l')
  			if not triplet[0]==0.0:
  				legend.AddEntry(theory_curve_1110,"G*#rightarrow Tt, tan #theta_{3} = 0.44, sin #phi_{tR} = 0.6, Y_{*} = 3",'l')
  			#legend.AddEntry(theory_curve_1410,"#rho_{0}#rightarrow Tt (arXiv:1410.2883)",'l')
  			if triplet[0]==0.0:
  				legend.AddEntry(theory_curve_1410,"#rho^{0}_{L}#rightarrow Tt, y_{L} = c_{2} = c_{3} = 1, g_{#rho_{L}} = 3",'l')
  			if triplet[0]==0.0:
  				#theory_curve_1110_33.SetLineColor(kGreen+3)
  				legend.AddEntry(theory_curve_1110_33,"#Gamma_{#rho^{0}_{L}}/m_{#rho^{0}_{L}} > 10 %",'l')
  			else:
  				#theory_curve_1110_33.SetLineColor(kAzure)
  				legend.AddEntry(theory_curve_1110_33,"#Gamma_{G*}/m_{G*} > 10 %",'l')

  			legend.Draw()
			CMS_lumi.CMS_lumi(c, 4, 11)
			c.SaveAs('pdf/unodlimit'+str(plotcounter)+'.pdf')

		if triplet in [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]:
			print 'bW',triplet[0],'tH',triplet[1],'tZ',triplet[2]
		for masspoint in range(len(signalWB_names)):
			#values[masspoint][0].append(triplet[0])
			#values[masspoint][1].append(triplet[1])
			this_line_exp=filter(None, theta_exp_lines[masspoint+1].split(' '))
			this_line_obs=filter(None, theta_obs_lines[masspoint+1].split(' '))
			assert(int(this_line_exp[0])==counter and int(this_line_obs[0])==counter)
			if triplet in [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]:
				print int(float(signal_Zp_masses2[masspoint])*1000),'&',int(float(signal_Tp_masses2[masspoint])*1000),'&',\
			'%s' % float('%.2g' % float(this_line_obs[1])),'&',\
			'%s' % float('%.2g' % float(this_line_exp[2])),'&',\
			'%s' % float('%.2g' % float(this_line_exp[4])),'&',\
			'%s' % float('%.2g' % float(this_line_exp[1])),'&',\
			'%s' % float('%.2g' % float(this_line_exp[5])),'&',\
			'%s' % float('%.2g' % float(this_line_exp[3])),'\\\\'
			#values[masspoint][2].append(float(this_line[1]))
			counter+=1
		theta_exp_result.close()
		theta_obs_result.close()
		filecounter+=1



