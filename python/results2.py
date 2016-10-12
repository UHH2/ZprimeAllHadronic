from ROOT import TFile,TCanvas,gROOT,gStyle,TGraph2D,TH2F,TPolyLine,TPolyLine3D,TLine,TGraph,TPad,TColor,TPaletteAxis,gPad,TBox,TLatex
from time import sleep
from os import system
from sys import argv
from os import mkdir
from os.path import exists
from array import array
import CMS_lumi

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

theory_dictionary={'2': 0.667, '2p5': 0.186, '1p5': 2.83}


doresults=True
values_exp = [[[] for i in range(3)] for i in range(len(signalWB_names))]
values_obs = [[[] for i in range(3)] for i in range(len(signalWB_names))]

if doresults:
	u='_'
	uu='__'
	nscan=40
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
		#theta_exp_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
		theta_obs_result = open('theta3/limits_obs'+filename_postfix+'.txt','r')
		#theta_exp_lines=theta_exp_result.readlines()
		theta_obs_lines=theta_obs_result.readlines()
		for masspoint in range(len(signalWB_names)):
			#values_exp[masspoint][0].append(triplet[0])
			#values_exp[masspoint][1].append(triplet[1])
			values_obs[masspoint][0].append(triplet[0])
			values_obs[masspoint][1].append(triplet[1])
			#this_line_exp=filter(None, theta_exp_lines[masspoint+1].split(' '))
			this_line_obs=filter(None, theta_obs_lines[masspoint+1].split(' '))
			#assert(int(this_line_exp[0])==counter)
			assert(int(this_line_obs[0])==counter)
			#values_exp[masspoint][2].append(float(this_line_exp[1]))
			values_obs[masspoint][2].append(float(this_line_obs[1]))
			counter+=1
		#theta_exp_result.close()
		theta_obs_result.close()
		filecounter+=1

if doresults:
	u='_'
	uu='__'
	nscan=10
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
		#theta_obs_result = open('theta/limits_obs'+filename_postfix+'.txt','r')
		theta_exp_lines=theta_exp_result.readlines()
		#theta_obs_lines=theta_obs_result.readlines()
		for masspoint in range(len(signalWB_names)):
			values_exp[masspoint][0].append(triplet[0])
			values_exp[masspoint][1].append(triplet[1])
			#values_obs[masspoint][0].append(triplet[0])
			#values_obs[masspoint][1].append(triplet[1])
			this_line_exp=filter(None, theta_exp_lines[masspoint+1].split(' '))
			#this_line_obs=filter(None, theta_obs_lines[masspoint+1].split(' '))
			assert(int(this_line_exp[0])==counter)
			#assert(int(this_line_obs[0])==counter)
			values_exp[masspoint][2].append(float(this_line_exp[1]))
			#values_obs[masspoint][2].append(float(this_line_obs[1]))
			counter+=1
		theta_exp_result.close()
		#theta_obs_result.close()
		filecounter+=1

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

for tipo in values:
	for masspoint in range(len(signalWB_names)):
		name=signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+'_v2'
		if tipo=='obs':
			name='o'+name
		p=0
		exclusion=0
		#p2=TH2F(name+'2','',10,0,1,10,0,1)
		# p=TH2F(name,'',11,-0.05,1.05,11,-0.05,1.05)
		# exclusion=TH2F(name+'excl','',11,-0.05,1.05,11,-0.05,1.05)
		if tipo=='exp':
			p=TH2F(name,'',11,-0.05,1.05,11,-0.05,1.05)
			exclusion=TH2F(name+'excl','',11,-0.05,1.05,11,-0.05,1.05)
			#p=TH2F(name,'',10,0,1,10,0,1)
			#exclusion=TH2F(name+'excl','',10,0,1,10,0,1)
		else:
			p=TH2F(name,'',41,-0.0125,1.0125,41,-0.0125,1.0125)
			exclusion=TH2F(name+'excl','',41,-0.0125,1.0125,41,-0.0125,1.0125)
		c=TCanvas(name+u+'c','',1300,1000)
		margine=0.15
		c.SetRightMargin(0.20)
		c.SetLeftMargin(margine)
		c.SetTopMargin(0.10)
		c.SetBottomMargin(margine)
		p.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
		p.GetXaxis().SetRangeUser(0,1)
		p.GetYaxis().SetRangeUser(0,1)
		p.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
		p.GetZaxis().SetTitle("Upper cross section limit (pb)")
		sizefactor=1.6
		p.GetXaxis().SetTitleSize(sizefactor*p.GetXaxis().GetTitleSize())
		p.GetYaxis().SetTitleSize(sizefactor*p.GetYaxis().GetTitleSize())
		p.GetZaxis().SetTitleSize(sizefactor*p.GetZaxis().GetTitleSize())
		p.GetXaxis().SetLabelSize(sizefactor*p.GetXaxis().GetLabelSize())
		p.GetYaxis().SetLabelSize(sizefactor*p.GetYaxis().GetLabelSize())
		p.GetZaxis().SetLabelSize(sizefactor*p.GetZaxis().GetLabelSize())
		p.GetZaxis().SetNoExponent(1)
		p.GetZaxis().SetMoreLogLabels(1)
		offset=1.2
		p.GetXaxis().SetTitleOffset(offset*p.GetXaxis().GetTitleOffset())
		p.GetYaxis().SetTitleOffset(offset*p.GetYaxis().GetTitleOffset())
		p.GetZaxis().SetTitleOffset(1.4*p.GetZaxis().GetTitleOffset())
		print 'masspoint',name
		for i in range(len(values[tipo][masspoint][0])):
			p.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],values[tipo][masspoint][2][i])
			if theory_dictionary[signal_Zp_masses[masspoint]]>values[tipo][masspoint][2][i]:
				exclusion.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],20)
			#else:
			# 	exclusion.Fill(values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],0.0)
			#print values[tipo][masspoint][0][i],values[tipo][masspoint][1][i],values[tipo][masspoint][2][i]
		p.SetMinimum(the_minimum)
		p.SetMaximum(the_maximum)
		#p.SetMinimum(min(values_obs[masspoint][2]+values_exp[masspoint][2]))
		#p.SetMaximum(max(values_obs[masspoint][2]+values_exp[masspoint][2]))
		p.GetZaxis().SetMoreLogLabels(1)
		p.SetStats(0)
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
		xx=array('d',[-0.05,1.05,1.05])
		yy=array('d',[1.05,1.05,-0.05])
	

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
		exclusion.GetXaxis().SetRangeUser(0,1)
		exclusion.GetYaxis().SetRangeUser(0,1)
		exclusion.GetXaxis().SetLabelOffset(100)
		exclusion.GetYaxis().SetLabelOffset(100)
		if tipo=='obs':
   			exclusion.Draw('')

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
		#p.Draw('atext')
		tri.Draw('f')
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
		c.SaveAs('pdf/'+name+'.pdf')
	
#outfile.Close()
