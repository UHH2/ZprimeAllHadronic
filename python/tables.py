from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array

from utils import compare,hadd,doeff,make_plot,make_ratioplot
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

doresults=True
if doresults:
	u='_'
	uu='__'
	nscan=10
	counter=1
	filecounter=1
	outfile=open('tables.txt','w')

	#values = [[[] for i in range(3)] for i in range(len(signalWB_names))]

	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		theta_obs_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
		theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
		theta_exp_lines=theta_exp_result.readlines()
		theta_obs_lines=theta_obs_result.readlines()
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


	outfile.close()
