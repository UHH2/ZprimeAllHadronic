from ROOT import TFile,TCanvas,gROOT,gStyle
from os import system
from sys import argv
from os import mkdir
from os.path import exists

from utils import compare,hadd,doeff,make_plot,make_ratioplot
gROOT.SetBatch()

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

doresults=True
if doresults:
	u='_'
	uu='__'
	nscan=10
	counter=1
	filecounter=1
	outfile-TFile('results.root','RECREATE')
	outfile.cd()

	values = [[[] for i in range(3)] for i in range(len(signalWB_names))]

	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		theta_exp_result = open('theta/limits_exp_'+filename_postfix+'.pytxt','r')


		for masspoint in range(len(signalWB_names)):
			values[masspoint][0].append(triplet[0])
			values[masspoint][1].append(triplet[1])
			values[masspoint][2].append()

			allhad2btag__signalWB=signal_filesWB[masspoint].Get(twobtags).Clone()
			allhad2btag__signalZT=signal_filesZT[masspoint].Get(twobtags).Clone()
			allhad2btag__signalHT=signal_filesHT[masspoint].Get(twobtags).Clone()
			#allhad2btag__signalWB.Sumw2()
			#allhad2btag__signalZT.Sumw2()
			#allhad2btag__signalHT.Sumw2()
			allhad2btag__signalWB.Scale(triplet[0])
			allhad2btag__signalHT.Scale(triplet[1])
			allhad2btag__signalZT.Scale(triplet[2])
			allhad2btag__signal=allhad2btag__signalWB
			allhad2btag__signal.Add(allhad2btag__signalHT)
			allhad2btag__signal.Add(allhad2btag__signalZT)
			allhad2btag__signal.Rebin(rebinna)

			allhad1btag__signalWB=signal_filesWB[masspoint].Get(onebtag).Clone()
			allhad1btag__signalZT=signal_filesZT[masspoint].Get(onebtag).Clone()
			allhad1btag__signalHT=signal_filesHT[masspoint].Get(onebtag).Clone()
			#allhad1btag__signalWB.Sumw2()
			#allhad1btag__signalZT.Sumw2()
			#allhad1btag__signalHT.Sumw2()
			allhad1btag__signalWB.Scale(triplet[0])
			allhad1btag__signalHT.Scale(triplet[1])
			allhad1btag__signalZT.Scale(triplet[2])
			allhad1btag__signal=allhad1btag__signalWB
			allhad1btag__signal.Add(allhad1btag__signalHT)
			allhad1btag__signal.Add(allhad1btag__signalZT)
			allhad1btag__signal.Rebin(rebinna)

			allhad2btag__signal.Write('allhad2btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
				str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))
			allhad1btag__signal.Write('allhad1btag__signal_'+str(counter)+u+signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+u+
				str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p'))
			counter+=1
		theta_exp_result.Close()
		

		filecounter+=1

plots=[]
for masspoint in range(len(signalWB_names)):
	plots.append(TGraph2D())


limits_exp_10_0p0_0p9_0p1.txt
limits_exp_11_0p0_1p0_0p0.txt
limits_exp_12_0p1_0p0_0p9.txt
limits_exp_13_0p1_0p1_0p8.txt
limits_exp_14_0p1_0p2_0p7.txt
limits_exp_15_0p1_0p3_0p6.txt
limits_exp_16_0p1_0p4_0p5.txt
limits_exp_17_0p1_0p5_0p4.txt
limits_exp_18_0p1_0p6_0p3.txt
limits_exp_19_0p1_0p7_0p2.txt
limits_exp_1_0p0_0p0_1p0.txt
limits_exp_20_0p1_0p8_0p1.txt
limits_exp_21_0p1_0p9_0p0.txt
limits_exp_22_0p2_0p0_0p8.txt
limits_exp_23_0p2_0p1_0p7.txt
limits_exp_24_0p2_0p2_0p6.txt
limits_exp_25_0p2_0p3_0p5.txt
limits_exp_26_0p2_0p4_0p4.txt
limits_exp_27_0p2_0p5_0p3.txt
limits_exp_28_0p2_0p6_0p2.txt
limits_exp_29_0p2_0p7_0p1.txt
limits_exp_2_0p0_0p1_0p9.txt
limits_exp_30_0p2_0p8_0p0.txt
limits_exp_31_0p3_0p0_0p7.txt
limits_exp_32_0p3_0p1_0p6.txt
limits_exp_33_0p3_0p2_0p5.txt
limits_exp_34_0p3_0p3_0p4.txt
limits_exp_35_0p3_0p4_0p3.txt
limits_exp_36_0p3_0p5_0p2.txt
limits_exp_37_0p3_0p6_0p1.txt
limits_exp_38_0p3_0p7_0p0.txt
limits_exp_39_0p4_0p0_0p6.txt
limits_exp_3_0p0_0p2_0p8.txt
limits_exp_40_0p4_0p1_0p5.txt
limits_exp_41_0p4_0p2_0p4.txt
limits_exp_42_0p4_0p3_0p3.txt
limits_exp_43_0p4_0p4_0p2.txt
limits_exp_44_0p4_0p5_0p1.txt
limits_exp_45_0p4_0p6_0p0.txt
limits_exp_46_0p5_0p0_0p5.txt
limits_exp_47_0p5_0p1_0p4.txt
limits_exp_48_0p5_0p2_0p3.txt
limits_exp_49_0p5_0p3_0p2.txt
limits_exp_4_0p0_0p3_0p7.txt
limits_exp_50_0p5_0p4_0p1.txt
limits_exp_51_0p5_0p5_0p0.txt
limits_exp_52_0p6_0p0_0p4.txt
limits_exp_53_0p6_0p1_0p3.txt
limits_exp_54_0p6_0p2_0p2.txt
limits_exp_55_0p6_0p3_0p1.txt
limits_exp_56_0p6_0p4_0p0.txt
limits_exp_57_0p7_0p0_0p3.txt
limits_exp_58_0p7_0p1_0p2.txt
limits_exp_59_0p7_0p2_0p1.txt
limits_exp_5_0p0_0p4_0p6.txt
limits_exp_60_0p7_0p3_0p0.txt
limits_exp_61_0p8_0p0_0p2.txt
limits_exp_62_0p8_0p1_0p1.txt
limits_exp_63_0p8_0p2_0p0.txt
limits_exp_64_0p9_0p0_0p1.txt
limits_exp_65_0p9_0p1_0p0.txt
limits_exp_66_1p0_0p0_0p0.txt
limits_exp_6_0p0_0p5_0p5.txt
limits_exp_7_0p0_0p6_0p4.txt
limits_exp_8_0p0_0p7_0p3.txt
limits_exp_9_0p0_0p8_0p2.txt
