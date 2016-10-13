from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor,TPaletteAxis,gPad,TBox,TLatex,TLegend,TH1D
from time import sleep
from os import system
from sys import argv#,settrace
from os import mkdir
from os.path import exists
from array import array
import CMS_lumi
#from time import sleep

from utils import compare,hadd,doeff,make_plot,make_ratioplot
gROOT.SetBatch()

import gc
gc.disable()

#settrace

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

signalWB_legendnames=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR(bW)=1",
"#splitline{Expected}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 0.7 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 0.9 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 1.2 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 0.9 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 1.2 TeV}}",
#"#splitline{Expected}{#splitline{m_{Z'} = 2 TeV),}{{T'} = 1.2 TeVRH)}}",
#"#splitline{Expected}{#splitline{m_{Z'} = 2 TeV),}{{T'} = 1.2 TeVWide)}}",
"#splitline{Expected}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 1.5 TeV}}",
#"#splitline{Expected}{#splitline{m_{Z'} = 2 TeV,W}{), m_{T'} = 1.2 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 2.5 TeV}{m_{T'} = 1.2 TeV}}",
"#splitline{Expected}{#splitline{m_{Z'} = 2.5 TeV}{m_{T'} = 1.5 TeV}}",
]

signalWB_legendnames_obs=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR(bW)=1",
"#splitline{Observed}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 0.7 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 0.9 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 1.5 TeV}{m_{T'} = 1.2 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 0.9 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 1.2 TeV}}",
#"#splitline{Observed}{#splitline{m_{Z'} = 2 TeV),}{{T'} = 1.2 TeVRH)}}",
#"#splitline{Observed}{#splitline{m_{Z'} = 2 TeV),}{{T'} = 1.2 TeVWide)}}",
"#splitline{Observed}{#splitline{m_{Z'} = 2.0 TeV}{m_{T'} = 1.5 TeV}}",
#"#splitline{Observed}{#splitline{m_{Z'} = 2 TeV,W}{), m_{T'} = 1.2 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 2.5 TeV}{m_{T'} = 1.2 TeV}}",
"#splitline{Observed}{#splitline{m_{Z'} = 2.5 TeV}{m_{T'} = 1.5 TeV}}",
]

signalWB_legendnames_obs2=[
#"m_{Z'}=1.5TeV, m_{T'}=0.7TeV, BR(bW)=1",
"m_{Z'}=1.5TeV, m_{T'}=0.7TeV",
"m_{Z'}=1.5TeV, m_{T'}=0.9TeV",
"m_{Z'}=1.5TeV, m_{T'}=1.2TeV",
"m_{Z'}=2.0TeV, m_{T'}=0.9, 1.2TeV",
"m_{Z'}=2.0TeV, m_{T'}=1.2TeV",
#"m_{Z'}=2TeV),, {T'}=1.2TeVRH)",
#"m_{Z'}=2TeV),, {T'}=1.2TeVWide)",
"m_{Z'}=2.0TeV, m_{T'}=1.5TeV",
#"m_{Z'}=2TeV,W, ), m_{T'}=1.2TeV",
"m_{Z'}=2.5TeV, m_{T'}=1.2TeV",
"m_{Z'}=2.5TeV, m_{T'}=1.5TeV",
]

theory_dictionary={'2': 0.667, '2p5': 0.186, '1p5': 2.83}

doresults=True
values_exp = [[[] for i in range(3)] for i in range(len(signalWB_names))]
values_obs = [[[] for i in range(3)] for i in range(len(signalWB_names))]

# if doresults:
# 	u='_'
# 	uu='__'
# 	nscan=40
# 	counter=1
# 	filecounter=1
# 	# outfile=TFile('results.root','RECREATE')
# 	# outfile.cd()
# 	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
# 		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
# 		#theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
# 		########################################################################################################################
# 		########################################################################################################################
# 		########################################################################################################################
# 		########################################################################################################################
# 		########################################################################################################################
# 		########################################################################################################################
# 		#theta_exp_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
# 		theta_obs_result = open('theta3/limits_obs'+filename_postfix+'.txt','r')
# 		#theta_exp_lines=theta_exp_result.readlines()
# 		theta_obs_lines=theta_obs_result.readlines()
# 		for masspoint in range(len(signalWB_names)):
# 			#values_exp[masspoint][0].append(triplet[0])
# 			#values_exp[masspoint][1].append(triplet[1])
# 			values_obs[masspoint][0].append(triplet[0])
# 			values_obs[masspoint][1].append(triplet[1])
# 			#this_line_exp=filter(None, theta_exp_lines[masspoint+1].split(' '))
# 			this_line_obs=filter(None, theta_obs_lines[masspoint+1].split(' '))
# 			#assert(int(this_line_exp[0])==counter)
# 			assert(int(this_line_obs[0])==counter)
# 			#values_exp[masspoint][2].append(float(this_line_exp[1]))
# 			values_obs[masspoint][2].append(float(this_line_obs[1]))
# 			counter+=1
# 		#theta_exp_result.close()
# 		theta_obs_result.close()
# 		filecounter+=1

u='_'
uu='__'
nscan=10
if doresults:
	counter=1
	filecounter=1
	# outfile=TFile('results.root','RECREATE')
	# outfile.cd()
	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		#theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
		########################################################################################################################
		########################################################################################################################
		########################################################################################################################
		########################################################################################################################
		########################################################################################################################
		########################################################################################################################
		theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
		theta_obs_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
		theta_exp_lines=theta_exp_result.readlines()
		theta_obs_lines=theta_obs_result.readlines()
		for masspoint in range(len(signalWB_names)):
			values_exp[masspoint][0].append(triplet[0])
			values_exp[masspoint][1].append(triplet[1])
			values_obs[masspoint][0].append(triplet[0])
			values_obs[masspoint][1].append(triplet[1])
			this_line_exp=filter(None, theta_exp_lines[masspoint+1].split(' '))
			this_line_obs=filter(None, theta_obs_lines[masspoint+1].split(' '))
			assert(int(this_line_exp[0])==counter)
			assert(int(this_line_obs[0])==counter)
			values_exp[masspoint][2].append(float(this_line_exp[1]))
			values_obs[masspoint][2].append(float(this_line_obs[1]))
			counter+=1
		theta_exp_result.close()
		theta_obs_result.close()
		filecounter+=1

# print values_obs

#values_exp=[[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [1.7781, 1.8689, 1.8604, 1.8734, 1.9384, 1.9567, 1.9109, 1.9652, 2.0652, 2.0837, 2.1041, 1.7019, 1.7441, 1.7512, 1.8064, 1.7455, 1.7996, 1.8249, 1.8755, 1.8841, 1.9576, 1.5124, 1.6343, 1.5342, 1.5903, 1.6439, 1.6638, 1.6634, 1.6922, 1.7069, 1.3569, 1.3701, 1.3938, 1.4306, 1.4534, 1.4463, 1.4179, 1.4794, 1.2111, 1.2159, 1.2576, 1.2672, 1.3059, 1.2896, 1.2807, 1.0738, 1.0962, 1.1013, 1.0991, 1.1291, 1.1242, 0.95186, 0.97153, 1.0146, 1.0208, 0.98965, 0.89871, 0.89364, 0.86489, 0.92335, 0.78369, 0.78222, 0.81127, 0.74078, 0.71458, 0.68214]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [1.5187, 1.5112, 1.534, 1.4759, 1.5318, 1.4998, 1.5737, 1.5595, 1.5633, 1.5622, 1.5443, 1.6041, 1.6033, 1.6149, 1.6306, 1.6624, 1.6588, 1.6839, 1.7426, 1.6919, 1.6224, 1.7295, 1.7393, 1.7254, 1.7012, 1.7415, 1.7684, 1.7153, 1.7624, 1.7148, 1.7771, 1.7511, 1.7658, 1.7649, 1.8026, 1.8528, 1.8041, 1.8246, 1.762, 1.7508, 1.7756, 1.867, 1.8152, 1.8594, 1.8695, 1.7606, 1.7709, 1.788, 1.7868, 1.8692, 1.9119, 1.7402, 1.7592, 1.7385, 1.7855, 1.7969, 1.6467, 1.6879, 1.6786, 1.6928, 1.5814, 1.6288, 1.632, 1.5208, 1.5257, 1.3783]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [2.6316, 2.7651, 2.8981, 3.1468, 3.4194, 3.7376, 3.793, 4.1611, 4.4955, 4.9602, 5.4802, 2.879, 3.0465, 3.367, 3.4046, 3.5432, 4.0515, 4.3464, 4.7408, 5.2137, 5.724, 3.0614, 3.2435, 3.5727, 3.7076, 4.1163, 4.5479, 4.7567, 5.5467, 5.9628, 3.2826, 3.5794, 3.9239, 4.265, 4.5704, 5.1201, 5.6128, 6.2657, 3.6576, 3.9788, 4.3029, 4.6061, 5.0299, 5.8509, 6.4524, 4.0145, 4.24, 4.7749, 5.2034, 5.9137, 6.7307, 4.3804, 4.9497, 5.5824, 6.1823, 6.9344, 4.913, 5.5197, 6.4554, 7.4512, 5.474, 6.4995, 7.4409, 6.7762, 8.069, 7.7508]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.6078, 0.6259, 0.64171, 0.65128, 0.67302, 0.66833, 0.70864, 0.73968, 0.759, 0.78863, 0.79851, 0.62545, 0.60856, 0.6564, 0.65989, 0.68274, 0.72007, 0.72778, 0.77473, 0.75394, 0.78121, 0.59058, 0.59404, 0.61398, 0.6458, 0.66179, 0.68046, 0.70051, 0.72989, 0.7644, 0.57896, 0.5804, 0.61134, 0.61803, 0.6435, 0.64678, 0.6809, 0.68422, 0.53805, 0.55432, 0.5809, 0.60055, 0.59968, 0.62375, 0.64132, 0.49913, 0.52715, 0.54083, 0.55204, 0.56648, 0.57423, 0.47942, 0.48876, 0.49712, 0.50854, 0.533, 0.4404, 0.45419, 0.45226, 0.47107, 0.42552, 0.42306, 0.43569, 0.38098, 0.3949, 0.35401]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.46583, 0.51821, 0.52853, 0.54748, 0.56217, 0.61471, 0.6408, 0.64314, 0.69856, 0.70126, 0.77887, 0.50764, 0.54241, 0.56351, 0.59953, 0.6104, 0.64754, 0.65907, 0.72683, 0.76025, 0.82211, 0.55118, 0.57448, 0.5775, 0.62086, 0.6632, 0.67644, 0.70731, 0.75902, 0.79679, 0.57454, 0.59994, 0.60219, 0.63965, 0.6615, 0.71342, 0.72883, 0.77154, 0.5758, 0.59394, 0.6289, 0.66069, 0.67288, 0.72679, 0.76589, 0.59093, 0.58916, 0.63694, 0.6568, 0.69871, 0.70588, 0.57723, 0.61689, 0.6193, 0.65689, 0.69327, 0.57084, 0.59469, 0.60615, 0.63503, 0.55005, 0.57451, 0.56128, 0.52893, 0.53091, 0.48237]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.53597, 0.55974, 0.58807, 0.6276, 0.67954, 0.7075, 0.72862, 0.79617, 0.84822, 0.91532, 1.0278, 0.59293, 0.6374, 0.65497, 0.6749, 0.7212, 0.76255, 0.82341, 0.91051, 0.95723, 1.0604, 0.64024, 0.66745, 0.73443, 0.7569, 0.82288, 0.874, 0.93865, 1.0216, 1.1173, 0.69916, 0.74171, 0.80466, 0.87043, 0.92168, 0.99234, 1.1378, 1.1965, 0.79375, 0.84022, 0.91268, 0.96412, 1.0643, 1.1527, 1.2844, 0.84817, 0.94935, 1.0271, 1.1114, 1.2443, 1.3956, 0.97848, 1.0956, 1.1765, 1.3597, 1.5379, 1.1177, 1.2561, 1.4598, 1.6219, 1.2912, 1.5203, 1.6895, 1.5289, 1.7273, 1.8474]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.30471, 0.31937, 0.33057, 0.34897, 0.35847, 0.38026, 0.39009, 0.41154, 0.43276, 0.47287, 0.49689, 0.3026, 0.32154, 0.33938, 0.35237, 0.37696, 0.37167, 0.39902, 0.41408, 0.44463, 0.49068, 0.29997, 0.32003, 0.34077, 0.34393, 0.35898, 0.36961, 0.41223, 0.42966, 0.45112, 0.30268, 0.30748, 0.33356, 0.33571, 0.36654, 0.38504, 0.39256, 0.42549, 0.29161, 0.31903, 0.30594, 0.32261, 0.34925, 0.35394, 0.38574, 0.28186, 0.30433, 0.31529, 0.31126, 0.33048, 0.34785, 0.28382, 0.28944, 0.29697, 0.31526, 0.32341, 0.26901, 0.28615, 0.29453, 0.29245, 0.25932, 0.26534, 0.27376, 0.25093, 0.25742, 0.23181]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.2625, 0.28751, 0.28941, 0.29923, 0.32334, 0.33818, 0.36221, 0.37888, 0.40616, 0.42362, 0.45372, 0.27138, 0.28629, 0.29583, 0.31407, 0.32891, 0.34263, 0.36272, 0.39292, 0.42241, 0.47033, 0.27564, 0.29516, 0.3055, 0.32537, 0.33788, 0.36058, 0.37834, 0.39622, 0.44111, 0.29182, 0.3033, 0.32121, 0.33706, 0.34053, 0.36242, 0.38619, 0.40112, 0.2791, 0.29787, 0.31555, 0.33205, 0.34211, 0.35763, 0.38365, 0.27659, 0.29271, 0.30491, 0.31815, 0.3294, 0.35042, 0.26967, 0.28048, 0.2821, 0.31059, 0.32393, 0.26301, 0.28001, 0.27742, 0.30183, 0.26119, 0.27707, 0.27325, 0.24666, 0.25353, 0.2357]]]
#sleep(10)
#values_obs=[[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [2.8146, 3.225, 2.884, 3.4112, 3.2197, 3.3509, 3.3307, 3.4112, 4.0426, 3.6172, 4.7965, 2.9669, 2.7578, 3.044, 2.9498, 3.142, 3.4719, 3.2793, 3.416, 3.1671, 3.7911, 2.33, 2.4945, 2.5749, 2.5803, 2.3583, 2.3039, 2.3691, 2.6553, 3.1031, 2.2076, 2.0385, 2.0033, 2.3966, 2.3561, 2.2947, 2.0922, 2.495, 1.6974, 1.6271, 1.7112, 1.8728, 1.8809, 2.1223, 1.816, 1.3737, 1.3598, 1.4363, 1.5103, 1.5173, 1.466, 1.4041, 1.2511, 1.1271, 1.2618, 1.3516, 1.0129, 1.0167, 1.1861, 1.0536, 0.96912, 0.90838, 1.0405, 0.83966, 0.83095, 0.80772]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [2.8909, 2.7882, 3.0129, 2.7272, 3.3791, 3.0545, 2.8912, 3.4045, 2.9898, 3.0187, 3.9476, 2.7014, 2.7924, 3.2662, 3.3966, 3.3818, 3.0255, 3.2382, 2.9263, 3.5379, 3.6244, 2.9369, 3.0925, 3.2551, 3.2753, 3.4002, 3.1033, 2.985, 3.1904, 3.2557, 2.7819, 2.897, 2.9314, 3.2762, 2.6718, 3.1582, 3.4136, 3.3845, 2.5494, 2.624, 2.5527, 3.0284, 2.6968, 3.3562, 3.1497, 2.6082, 2.573, 2.6293, 2.6553, 2.7555, 2.7591, 2.3888, 2.3463, 2.4037, 2.58, 2.2553, 2.2096, 2.0899, 2.2208, 2.1492, 1.7765, 2.1325, 2.1539, 1.6018, 1.7681, 1.5396]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [3.4437, 3.648, 3.8311, 4.3694, 4.907, 5.6752, 5.9566, 6.9538, 7.0091, 8.2311, 9.2208, 3.445, 3.8947, 4.1562, 4.9093, 4.664, 6.3193, 5.8384, 6.9931, 8.4375, 11.393, 3.7296, 4.2061, 4.1396, 4.696, 5.6586, 5.605, 7.1334, 7.3374, 10.935, 4.1687, 4.6401, 4.6569, 5.2169, 5.9847, 6.8398, 8.3433, 9.3754, 4.3903, 5.1046, 5.034, 5.7998, 7.8342, 7.8706, 9.3046, 4.6368, 6.3442, 6.0318, 6.4771, 8.2413, 9.9902, 4.8214, 5.6741, 6.9242, 8.3181, 8.9374, 5.6057, 6.8778, 9.4355, 9.2658, 6.2692, 8.4922, 10.976, 7.3235, 8.7321, 8.9069]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.35838, 0.40583, 0.40285, 0.36819, 0.44149, 0.48393, 0.42875, 0.43847, 0.52357, 0.50211, 0.58514, 0.35307, 0.35493, 0.37995, 0.38332, 0.43702, 0.44193, 0.42015, 0.45528, 0.46313, 0.47157, 0.33994, 0.3518, 0.34873, 0.33617, 0.3969, 0.41381, 0.41574, 0.40949, 0.44494, 0.31152, 0.34032, 0.34061, 0.35129, 0.35311, 0.37271, 0.36696, 0.38389, 0.28656, 0.30468, 0.29456, 0.31472, 0.31297, 0.32486, 0.3619, 0.24968, 0.25699, 0.27495, 0.29008, 0.29448, 0.33079, 0.26076, 0.25083, 0.25602, 0.29749, 0.26379, 0.23457, 0.23302, 0.25613, 0.24829, 0.23451, 0.23519, 0.2365, 0.21514, 0.18631, 0.18712]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.2969, 0.3011, 0.32326, 0.32556, 0.35498, 0.37346, 0.38906, 0.44512, 0.40313, 0.48434, 0.54711, 0.29912, 0.31821, 0.35342, 0.33486, 0.38234, 0.36958, 0.41993, 0.41218, 0.42958, 0.48684, 0.29303, 0.35602, 0.35049, 0.39156, 0.38825, 0.36172, 0.4025, 0.44849, 0.42158, 0.30734, 0.35247, 0.35417, 0.34435, 0.37662, 0.42939, 0.41161, 0.44515, 0.34025, 0.30399, 0.31482, 0.36743, 0.37133, 0.44198, 0.49444, 0.29905, 0.31284, 0.41392, 0.34631, 0.38375, 0.37912, 0.27697, 0.30855, 0.35394, 0.33507, 0.35135, 0.29299, 0.3166, 0.32762, 0.31569, 0.30914, 0.27791, 0.30353, 0.29381, 0.31317, 0.27007]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.31998, 0.3424, 0.33075, 0.35215, 0.34863, 0.42834, 0.46145, 0.39748, 0.49221, 0.52784, 0.62522, 0.33444, 0.3477, 0.36113, 0.41035, 0.43756, 0.43307, 0.55496, 0.52684, 0.54874, 0.59044, 0.37338, 0.38132, 0.38143, 0.4366, 0.45889, 0.51379, 0.59571, 0.59744, 0.66874, 0.39211, 0.42065, 0.46699, 0.42954, 0.59944, 0.61476, 0.64656, 0.7491, 0.42276, 0.55418, 0.47803, 0.53128, 0.58386, 0.68189, 0.83191, 0.49335, 0.5755, 0.62552, 0.5913, 0.68855, 0.84521, 0.53218, 0.61733, 0.63757, 0.76132, 0.7961, 0.5742, 0.69607, 0.80825, 0.84297, 0.68839, 0.80882, 0.83277, 0.77218, 0.86742, 0.95878]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.16699, 0.17903, 0.18588, 0.16488, 0.17861, 0.18288, 0.21036, 0.19411, 0.2381, 0.2277, 0.24974, 0.16262, 0.18689, 0.18075, 0.20066, 0.20055, 0.19391, 0.22187, 0.21032, 0.23009, 0.28562, 0.1859, 0.19553, 0.21401, 0.21347, 0.22306, 0.21614, 0.24009, 0.23889, 0.2735, 0.22653, 0.22173, 0.26423, 0.24419, 0.27719, 0.29277, 0.30551, 0.28197, 0.22463, 0.24905, 0.2469, 0.25502, 0.27458, 0.264, 0.33053, 0.27614, 0.25074, 0.24743, 0.28445, 0.29058, 0.28576, 0.27956, 0.27409, 0.31115, 0.27006, 0.30748, 0.29079, 0.30187, 0.27415, 0.35026, 0.29519, 0.31892, 0.32445, 0.28825, 0.31361, 0.30018]], [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.7, 0.8, 0.8, 0.8, 0.9, 0.9, 1.0], [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.0, 0.1, 0.2, 0.3, 0.4, 0.0, 0.1, 0.2, 0.3, 0.0, 0.1, 0.2, 0.0, 0.1, 0.0], [0.12526, 0.13845, 0.15494, 0.14189, 0.15465, 0.16904, 0.15943, 0.18933, 0.20202, 0.19926, 0.22503, 0.14545, 0.14658, 0.15628, 0.17769, 0.17238, 0.1911, 0.20435, 0.22876, 0.2331, 0.24272, 0.16397, 0.18785, 0.19167, 0.19547, 0.21812, 0.20806, 0.24464, 0.26134, 0.29865, 0.17232, 0.19563, 0.20072, 0.20035, 0.22665, 0.28298, 0.27208, 0.28668, 0.20438, 0.18868, 0.2575, 0.21682, 0.26878, 0.27768, 0.34004, 0.21399, 0.21209, 0.25289, 0.26103, 0.29786, 0.31545, 0.24098, 0.26441, 0.26003, 0.33735, 0.29059, 0.2628, 0.29489, 0.28599, 0.31819, 0.26035, 0.28907, 0.30472, 0.32703, 0.30555, 0.30098]]]

#plots=[]
# for masspoint in range(len(signalWB_names)):
# 	name=signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]
# 	p=TGraph2D(name,";T' #rightarrow bW branching fraction;T' #rightarrow tH branching fraction;Cross section limit (pb)",len(values[masspoint][0]),array('d',values[masspoint][0]),array('d',values[masspoint][1]),array('d',values[masspoint][2]) )
# 	c=TCanvas(name+u+'c')#,'',600,600)
# 	c.SetRightMargin(0.15)
# 	p.SetMargin(0.1)
	
# 	# plots[-1].GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
# 	# plots[-1].GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
# 	#p.GetZaxis().SetRangeUser(0.1,5.5)
# 	p.SetMinimum(0.2)
# 	p.SetMaximum(5.5)
# 	p.GetZaxis().SetMoreLogLabels(1)

# 	p.Draw('colz')
# 	#p.GetZaxis().SetRangeUser(0.1,5.5)
# 	#p.SetMinimum(0.1)
# 	#p.SetMaximum(5.5)
# 	#c.Update()
# 	p.Write()
# 	plots.append(p)

# 	c.SetLogz(1)
# 	c.SaveAs('pdf/'+name+'.pdf')
gStyle.SetPalette(55)
gStyle.SetNumberContours(99)#999
#set_palette('',99)

the_maximum=-100.0
the_minimum=1000000.0
for masspoint in range(len(signalWB_names)):
	the_minimum = min(min(values_obs[masspoint][2]+values_exp[masspoint][2]),the_minimum)
	the_maximum = max(max(values_obs[masspoint][2]+values_exp[masspoint][2]),the_maximum)

print the_minimum, the_maximum

the_minimum=0.12526
the_maximum=11.393

values={'exp':values_exp,'obs':values_obs}

tutti=[]

xx=array('d',[-0.05,1.05,1.05])
yy=array('d',[1.05,1.05,-0.05])


for tipo in values:
	for masspoint in range(len(signalWB_names)):
		name=signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+'_v2'
		if tipo=='obs':
			name='o'+name
		#p=0
		exclusion=0
		contList=0
		contLen=0
		contArray=0
		#p2=TH2F(name+'2','',10,0,1,10,0,1)

		sizefactor=1.6
		margine=0.15
		offset=1.2

		legend=0

		if tipo=='obs':
			th_value=theory_dictionary[signal_Zp_masses[masspoint]]
			contList=[th_value*0.97,th_value,th_value*1.03]
			contLen=len(contList)
			contArray = array('d',contList)
			exclusion=TH2F(name+'excl','',11,-0.05,1.05,11,-0.05,1.05)
			exclusion2=TH2F(name+'excl2','',11,-0.05,1.05,11,-0.05,1.05)
			exclusion.SetContour(contLen,contArray)
			exclusion2.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
			exclusion2.GetXaxis().SetRangeUser(-0.05,1.05)
			exclusion2.GetYaxis().SetRangeUser(-0.05,1.05)
			exclusion2.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
			exclusion2.GetZaxis().SetTitle("Upper cross section limit (pb)")
			#sizefactor=1.6
			exclusion2.GetXaxis().SetTitleSize(sizefactor*exclusion2.GetXaxis().GetTitleSize())
			exclusion2.GetYaxis().SetTitleSize(sizefactor*exclusion2.GetYaxis().GetTitleSize())
			exclusion2.GetZaxis().SetTitleSize(sizefactor*exclusion2.GetZaxis().GetTitleSize())
			exclusion2.GetXaxis().SetLabelSize(sizefactor*exclusion2.GetXaxis().GetLabelSize())
			exclusion2.GetYaxis().SetLabelSize(sizefactor*exclusion2.GetYaxis().GetLabelSize())
			exclusion2.GetZaxis().SetLabelSize(sizefactor*exclusion2.GetZaxis().GetLabelSize())
			exclusion2.GetZaxis().SetNoExponent(1)
			exclusion2.GetZaxis().SetMoreLogLabels(1)
			#offset=1.2
			exclusion2.SetStats(0)
			exclusion2.GetXaxis().SetTitleOffset(offset*exclusion2.GetXaxis().GetTitleOffset())
			exclusion2.GetYaxis().SetTitleOffset(offset*exclusion2.GetYaxis().GetTitleOffset())
			exclusion2.GetZaxis().SetTitleOffset(1.4*exclusion2.GetZaxis().GetTitleOffset())

		p=TH2F(name,'',11,-0.05,1.05,11,-0.05,1.05)
		#p=TH2F(name,'',11,-0.10,1.00,11,-0.10,1.00)
		
		# if tipo=='exp':
		# 	p=TH2F(name,'',11,-0.05,1.05,11,-0.05,1.05)
		# 	exclusion=TH2F(name+'excl','',11,-0.05,1.05,11,-0.05,1.05)
		# 	#p=TH2F(name,'',10,0,1,10,0,1)
		# 	#exclusion=TH2F(name+'excl','',10,0,1,10,0,1)
		# else:
		# 	p=TH2F(name,'',41,-0.0125,1.0125,41,-0.0125,1.0125)
		# 	exclusion=TH2F(name+'excl','',41,-0.0125,1.0125,41,-0.0125,1.0125)
		c=TCanvas(name+u+'c','',1300,1000)
		
		c.SetRightMargin(0.20)
		c.SetLeftMargin(margine)
		c.SetTopMargin(0.10)
		c.SetBottomMargin(margine)
		p.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
		p.GetXaxis().SetRangeUser(0,1)
		p.GetYaxis().SetRangeUser(0,1)
		p.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
		p.GetZaxis().SetTitle("Upper cross section limit (pb)")
		
		p.GetXaxis().SetTitleSize(sizefactor*p.GetXaxis().GetTitleSize())
		p.GetYaxis().SetTitleSize(sizefactor*p.GetYaxis().GetTitleSize())
		p.GetZaxis().SetTitleSize(sizefactor*p.GetZaxis().GetTitleSize())
		p.GetXaxis().SetLabelSize(sizefactor*p.GetXaxis().GetLabelSize())
		p.GetYaxis().SetLabelSize(sizefactor*p.GetYaxis().GetLabelSize())
		p.GetZaxis().SetLabelSize(sizefactor*p.GetZaxis().GetLabelSize())
		p.GetZaxis().SetNoExponent(1)
		p.GetZaxis().SetMoreLogLabels(1)
		
		p.GetXaxis().SetTitleOffset(offset*p.GetXaxis().GetTitleOffset())
		p.GetYaxis().SetTitleOffset(offset*p.GetYaxis().GetTitleOffset())
		p.GetZaxis().SetTitleOffset(1.4*p.GetZaxis().GetTitleOffset())
		print 'masspoint',name
		for i in range(len(values[tipo][masspoint][0])):
			p.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],values[tipo][masspoint][2][i])
			if tipo=='obs':
				exclusion.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],values[tipo][masspoint][2][i])
			#if theory_dictionary[signal_Zp_masses[masspoint]]>values[tipo][masspoint][2][i]:
			#	exclusion.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],20)
			#else:
			# 	exclusion.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],0.0)
			#print values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],values[tipo][masspoint][2][i]
		p.SetMinimum(the_minimum)
		p.SetMaximum(the_maximum)
		#p.SetMinimum(min(values_obs[masspoint][2]+values_exp[masspoint][2]))
		#p.SetMaximum(max(values_obs[masspoint][2]+values_exp[masspoint][2]))
		p.GetZaxis().SetMoreLogLabels(1)
		p.SetStats(0)
		if tipo=='obs':
			exclusion.SetStats(0)

		#p2.Draw('')
		p.Draw('cont4z')

		#p2.GetXaxis().SetRangeUser(0,1)
		# gPad.Update()
		# palette = exclusion.GetListOfFunctions().FindObject("palette")
		# palette.SetX1NDC(1.1)
		# palette.SetX2NDC(1.2)
		# palette.SetY1NDC(1.1)
		# palette.SetY2NDC(1.2)
		#p.Write()
		#plots.append(p)
	

		if tipo=='obs':
			bm = c.GetBottomMargin()
			lm = c.GetLeftMargin()
			rm = c.GetRightMargin()
			to = c.GetTopMargin()
			x1 = p.GetXaxis().GetXmin()
			yf = p.GetYaxis().GetXmin()
			x2 = p.GetXaxis().GetXmax()
			y2 = p.GetYaxis().GetXmax()

			Xa = (x2-x1)/(1-lm-rm)-(x2-x1)
			Ya = (y2-yf)/(1-bm-to)-(y2-yf)
			LM = Xa*(lm/(lm+rm))
			RM = Xa*(rm/(lm+rm))
			BM = Ya*(bm/(bm+to))
			TM = Ya*(to/(bm+to))
			null2 = TPad("null2","",0,0,1,1)
			null2.SetFillStyle(0)
			null2.SetFrameFillStyle(0)
			null2.Draw()
			null2.cd()
			null2.Range(x1-LM,yf-BM,x2+RM,y2+TM)
			null2.SetRightMargin(0.20)
			null2.SetLeftMargin(margine)
			null2.SetTopMargin(0.10)
			null2.SetBottomMargin(margine)
			#exclusion.SetMinimum(the_minimum)
			#exclusion.SetMaximum(the_maximum)
			exclusion.GetXaxis().SetRangeUser(-0.05,1.05)
			exclusion.GetYaxis().SetRangeUser(-0.05,1.05)
			exclusion.GetXaxis().SetLabelOffset(100)
			exclusion.GetYaxis().SetLabelOffset(100)
			#exclusion.Draw('CONT3')
			exclusion2.Draw()
			c2=TCanvas(name+'_c2')
			c2.cd()
			exclusion.Draw('CONT Z LIST')
			c2.Update()
			conts=gROOT.GetListOfSpecials().FindObject("contours")
			c.cd()
			null2.cd()
			codes=[
			[0,0,0],
			[1,0,1],
			[2,0,10],
			[3,0,10],
			[4,0,10],
			[5,0,0],
			[6,2,0],
			[7,2,0],
			]
			print 'total',conts.GetSize()
			for i in range(conts.GetSize()):
				cont=conts.At(i)
				print i,cont.GetSize()
				for j in range(cont.GetSize()):
					contour=cont.At(j)
					contour.SetLineColor(2)
					if [masspoint,i,j] in codes:
						contour.SetLineWidth(1003)
						contour.SetFillStyle(3005)
						contour.SetFillColor(2)
						contour.Draw('c')
						tutti.append(contour.Clone())
			if masspoint in [3,4]:
				xcont=array('d',[0,1])
				ycont=array('d',[1,0])
				allcont=TGraph(2,ycont,xcont)
				allcont.SetLineWidth(1006)
				allcont.SetFillStyle(3005)
				allcont.SetFillColor(2)
				allcont.SetLineColor(2)
				allcont.Draw('c')
				tutti.append(allcont.Clone())
			if masspoint in [2]:
				xcont=array('d',[0])
				ycont=array('d',[0])
				allcont=TGraph(1,ycont,xcont)
				allcont.SetLineWidth(1006)
				allcont.SetFillStyle(3005)
				allcont.SetFillColor(2)
				allcont.SetLineColor(2)
				allcont.Draw('c')
				tutti.append(allcont.Clone())

  						

			#print conts
			#print conts.GetSize()


		bm = c.GetBottomMargin()
		lm = c.GetLeftMargin()
		rm = c.GetRightMargin()
		to = c.GetTopMargin()
		x1 = p.GetXaxis().GetXmin()
		yf = p.GetYaxis().GetXmin()
		x2 = p.GetXaxis().GetXmax()
		y2 = p.GetYaxis().GetXmax()

		Xa = (x2-x1)/(1-lm-rm)-(x2-x1)
		Ya = (y2-yf)/(1-bm-to)-(y2-yf)
		LM = Xa*(lm/(lm+rm))
		RM = Xa*(rm/(lm+rm))
		BM = Ya*(bm/(bm+to))
		TM = Ya*(to/(bm+to))

		null = TPad("null","",0,0,1,1)
		null.SetFillStyle(0)
		null.SetFrameFillStyle(0)
		null.Draw()
		null.cd()
		null.Range(x1-LM,yf-BM,x2+RM,y2+TM)

		tri=TPolyLine(3,xx,yy)
		tri.SetFillColor(0)
		box1=TBox(-0.2,-0.2,1.05,0)
		box2=TBox(-0.2,-0.2,0,1.05)
		box1.SetFillColor(0)
		box2.SetFillColor(0)
		#p.Draw('atext')
		tri.Draw('f')
		box1.Draw('f')
		box2.Draw('f')
		tri.Draw('f')

		if tipo=='obs':
			bm = c.GetBottomMargin()
			lm = c.GetLeftMargin()
			rm = c.GetRightMargin()
			to = c.GetTopMargin()
			x1 = p.GetXaxis().GetXmin()
			yf = p.GetYaxis().GetXmin()
			x2 = p.GetXaxis().GetXmax()
			y2 = p.GetYaxis().GetXmax()

			Xa = (x2-x1)/(1-lm-rm)-(x2-x1)
			Ya = (y2-yf)/(1-bm-to)-(y2-yf)
			LM = Xa*(lm/(lm+rm))
			RM = Xa*(rm/(lm+rm))
			BM = Ya*(bm/(bm+to))
			TM = Ya*(to/(bm+to))

			null3 = TPad("null3","",0,0,1,1)
			null3.SetFillStyle(0)
			null3.SetFrameFillStyle(0)
			null3.Draw()
			null3.cd()
			null3.Range(x1-LM,yf-BM,x2+RM,y2+TM)
			null3.SetRightMargin(0.20)
			null3.SetLeftMargin(margine)
			null3.SetTopMargin(0.10)
			null3.SetBottomMargin(margine)

			# exclusion2.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
			# exclusion2.GetXaxis().SetRangeUser(-0.05,1.05)
			# exclusion2.GetYaxis().SetRangeUser(-0.05,1.05)
			# exclusion2.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
			# exclusion2.GetZaxis().SetTitle("Upper cross section limit (pb)")
			# #sizefactor=1.6
			# exclusion2.GetXaxis().SetTitleSize(sizefactor*exclusion2.GetXaxis().GetTitleSize())
			# exclusion2.GetYaxis().SetTitleSize(sizefactor*exclusion2.GetYaxis().GetTitleSize())
			# exclusion2.GetZaxis().SetTitleSize(sizefactor*exclusion2.GetZaxis().GetTitleSize())
			# exclusion2.GetXaxis().SetLabelSize(sizefactor*exclusion2.GetXaxis().GetLabelSize())
			# exclusion2.GetYaxis().SetLabelSize(sizefactor*exclusion2.GetYaxis().GetLabelSize())
			# exclusion2.GetZaxis().SetLabelSize(sizefactor*exclusion2.GetZaxis().GetLabelSize())
			# exclusion2.GetZaxis().SetNoExponent(1)
			# exclusion2.GetZaxis().SetMoreLogLabels(1)
			# #offset=1.2
			# exclusion2.SetStats(0)
			# exclusion2.GetXaxis().SetTitleOffset(offset*exclusion2.GetXaxis().GetTitleOffset())
			# exclusion2.GetYaxis().SetTitleOffset(offset*exclusion2.GetYaxis().GetTitleOffset())
			# exclusion2.GetZaxis().SetTitleOffset(1.4*exclusion2.GetZaxis().GetTitleOffset())
			exclusion2.Draw()

		gStyle.SetPaintTextFormat('4.2f')
		p.SetMarkerSize(0.4)
		#p.SetMarkerColor(14)
		#p.Draw('atext45 same')
		c.SetLogz(1)
		#p.GetZaxis().SetMoreLogLabels(1)
		CMS_lumi.writeExtraText=False
		if tipo=='exp':
			CMS_lumi.writeExtraText=True
		CMS_lumi.CMS_lumi(c, 4, 33)
		latex=TLatex(0.2 ,0.1,signalWB_legendnames[masspoint])
		if tipo=='obs':
			latex=TLatex(0.2 ,0.1,signalWB_legendnames_obs[masspoint])
		latex.SetTextFont(42)
		#latex.SetTextSize(latex.GetTextSize()*0.85)
		#latex.SetTextAlign(11)
		latex.Draw()
		if tipo=='obs':
			leg_x=0.3
			leg_y=0.8
			legend=TLegend(leg_x,leg_y,leg_x+0.20,leg_y+0.15)
 			legend.SetTextSize(latex.GetTextSize())
  			legend.SetBorderSize(0)
  			legend.SetTextFont(42)
  			legend.SetLineColor(1)
  			legend.SetLineStyle(1)
  			legend.SetLineWidth(1)
  			legend.SetFillColor(0)
  			legend.SetFillStyle(0)
  			legend.SetHeader('')
  			tg=TGraph(3,xx,yy)
  			tg.SetLineColor(2)
			tg.SetLineWidth(503)
			tg.SetFillStyle(3005)
			tg.SetFillColor(2)
  			legend.AddEntry(tg,"SSM Z' excl.",'lf')
			legend.Draw()
		c.SaveAs('pdf/'+name+'.pdf')

#hexcolor=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
#             1.5 0    1.5 1     1.5d 2     2.0 3     2.0d 4
hexcolor=["#1f77b4", "#ff7f0e","#ff7f0e", "#2ca02c", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
intcolor=[TColor.GetColor(i) for i in hexcolor]

ctutti=TCanvas('tuttic','',1000,1000)		
ctutti.SetRightMargin(0.05)
ctutti.SetLeftMargin(margine)
ctutti.SetTopMargin(0.05)
ctutti.SetBottomMargin(margine)
ctutti.cd()
bogus=TH1D('','',1,0,1)
bogus.Draw()
bogus.SetMinimum(0)
bogus.SetMaximum(1)
bogus.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
bogus.GetXaxis().SetRangeUser(0,1)
bogus.GetYaxis().SetRangeUser(0,1)
bogus.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
sizefactor=sizefactor*0.9
bogus.GetXaxis().SetTitleSize(sizefactor*bogus.GetXaxis().GetTitleSize())
bogus.GetYaxis().SetTitleSize(sizefactor*bogus.GetYaxis().GetTitleSize())
bogus.GetXaxis().SetLabelSize(sizefactor*bogus.GetXaxis().GetLabelSize())
bogus.GetYaxis().SetLabelSize(sizefactor*bogus.GetYaxis().GetLabelSize())
bogus.SetStats(0)		
bogus.GetXaxis().SetTitleOffset(offset*bogus.GetXaxis().GetTitleOffset())
bogus.GetYaxis().SetTitleOffset(offset*bogus.GetYaxis().GetTitleOffset())
legend=TLegend(0.55,0.55,0.94,0.94)
#legend.SetTextSize(latex.GetTextSize())
legend.SetBorderSize(0)
legend.SetTextFont(42)
legend.SetLineColor(1)
legend.SetLineStyle(1)
legend.SetLineWidth(1)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetHeader("SSM Z' exclusion")
tutti2=[i.Clone() for i in tutti]
for i in range(len(tutti)):
	tutti[i].SetLineColor(intcolor[i])
	tutti[i].SetFillColor(intcolor[i])
	tutti[i].Draw('c')
	tutti2[i].SetLineColor(intcolor[i])
	tutti2[i].SetFillColor(intcolor[i])
	tutti2[i].SetLineWidth(303)
	if i not in [2,4]:
		tutti[i].Draw('c')
		legend.AddEntry(tutti2[i],signalWB_legendnames_obs2[i],'lf')
	#else:
	#	tutti[i].Draw('c')
	#	tutti[i].GetXaxis().SetRangeUser(0.0,1.0)
	#	ctutti.Update()
xx=array('d',[0.0,1.0,1.0])
yy=array('d',[1.0,1.0,0.0])
tri=TPolyLine(3,xx,yy)
tri.SetFillColor(0)
tri.Draw('f')
xborder=array('d',[0.0,1.0])
yborder=array('d',[1.0,0.0])
bor=TPolyLine(2,xborder,yborder)
bor.SetLineColor(1)
bor.SetLineWidth(1)
bor.Draw('l')
legend.Draw()

ctutti.SaveAs('pdf/observed.pdf')

# if masspoint==0:
# 	ctutti.cd()
# 	p.Draw('cont4z')
# 	xwhite=array('d',[-0.05,-0.05,1.05])
# 	ywhite=array('d',[1.05,-0.05,-0.05])
# 	twhite=TGraph(3,xwhite,ywhite)
# 	twhite.SetFillColor(0)
# 	twhite.Draw()

#outfile.Close()
