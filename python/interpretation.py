from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor,TGraphAsymmErrors,TGraph,kYellow,kGreen,kOrange,TLegend
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array
import CMS_lumi

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

theory_values=[]
for i in theory_files:
	pairs=[]
	the_file=open(i,'r')
	lines=the_file.readlines()
	for line in lines:
		splitted=filter(None, line.split(' '))
		pairs.append([float(splitted[0]),float(splitted[2])])
	theory_values.append(pairs)
	the_file.close()

x_theory=array('d',[theory_values[0][i][0] for i in range(len(theory_values[0]))])
y_theory=array('d',[float(lines_obs[0][1]),
				         float(lines_obs[1][1]),
				         float(lines_obs[2][1])])
print theory_values


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
		if triplet in [[0.5,0.25,0.25],[1.0,0.0,0.0]]:
			plotcounter=plotcounter+1
			c=TCanvas('unodlimit'+str(plotcounter),'',1200,1000)
			c.SetLogy()
			margine=0.15
			c.SetRightMargin(0.10)
			c.SetLeftMargin(margine)
			c.SetTopMargin(0.10)
			c.SetBottomMargin(margine)
			x=array('d',[1.5,2.0,2.5])
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
			obslim.SetLineWidth(3)
			explim.SetLineWidth(3)
			explim.SetLineStyle(2)
			explim.SetTitle('')
			obslim.SetTitle('')
			exp2sigma.SetTitle('')
			exp1sigma.SetTitle('')
			#obslim.SetMinimum(0.001);
			#duesigma=TGraphAsymmErrors(3,)
			exp1sigma.SetFillColor(kGreen+1)
			exp2sigma.SetFillColor(kOrange)
			exp2sigma.SetMaximum(150)
			exp2sigma.SetMinimum(0.07)
			exp2sigma.Draw('a3lp')
			exp2sigma.GetXaxis().SetTitle("Z' mass [TeV]")
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

			legend=TLegend(0.45,0.6,0.9,0.9)
 			legend.SetTextSize(0.045)
  			legend.SetBorderSize(0)
  			legend.SetTextFont(42)
  			legend.SetLineColor(1)
  			legend.SetLineStyle(1)
  			legend.SetLineWidth(1)
  			legend.SetFillColor(0)
  			legend.SetFillStyle(0)
  			legend.SetHeader('BR(bW)=1')
  			if triplet[0]==1.0:
  				legend.SetHeader('BR(bW,tH,tZ)=0.5,0.25,0.25')
  			legend.AddEntry(obslim,'Observed','l')
  			legend.AddEntry(explim,'Expected','l')
  			legend.AddEntry(exp1sigma,'#pm 1 std. deviation','f')
  			legend.AddEntry(exp2sigma,'#pm 2 std. deviation','f')
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
				print signal_Zp_masses2[masspoint],'&',signal_Tp_masses2[masspoint],'&',\
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



