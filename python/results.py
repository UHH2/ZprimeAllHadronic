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

doresults=True
if doresults:
	u='_'
	uu='__'
	nscan=10
	counter=1
	filecounter=1
	outfile=TFile('results.root','RECREATE')
	outfile.cd()

	values = [[[] for i in range(3)] for i in range(len(signalWB_names))]

	for triplet in [[i/float(nscan),j/float(nscan),(nscan-i-j)/float(nscan)] for i in range(nscan+1) for j in range(nscan+1-i)]:
		filename_postfix=u+str(filecounter)+u+str(triplet[0]).replace('.','p')+u+str(triplet[1]).replace('.','p')+u+str(triplet[2]).replace('.','p')
		theta_exp_result = open('theta/limits_exp'+filename_postfix+'.txt','r')
		theta_exp_lines=theta_exp_result.readlines()
		for masspoint in range(len(signalWB_names)):
			values[masspoint][0].append(triplet[0])
			values[masspoint][1].append(triplet[1])
			this_line=filter(None, theta_exp_lines[masspoint+1].split(' '))
			assert(int(this_line[0])==counter)
			values[masspoint][2].append(float(this_line[1]))
			counter+=1
		theta_exp_result.close()
		

		filecounter+=1

plots=[]
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

for masspoint in range(len(signalWB_names)):
	name=signal_Zp_masses[masspoint]+u+signal_Tp_masses[masspoint]+'_v2'
	p=TH2F(name,'',11,-0.05,1.05,11,-0.05,1.05)
	c=TCanvas(name+u+'c')#,'',600,600)
	c.SetRightMargin(0.15)
	p.GetXaxis().SetTitle("T' #rightarrow bW branching fraction")
	p.GetXaxis().SetRangeUser(0,1)
	p.GetYaxis().SetTitle("T' #rightarrow tH branching fraction")
	p.GetZaxis().SetTitle("Cross section limit (pb)")
	for i in range(len(values[masspoint][0])):
		p.Fill(values[masspoint][0][i],values[masspoint][1][i],values[masspoint][2][i])
	p.SetMinimum(0.2)
	p.SetMaximum(5.5)
	p.GetZaxis().SetMoreLogLabels(1)
	p.SetStats(0)

	p.Draw('cont4z')
	p.Write()
	plots.append(p)
	xx=array('d',[-0.05,1.04,1.04])
	yy=array('d',[1.04,1.04,-0.05])
	
	null = TPad("null","",0,0,1,1)
   	null.SetFillStyle(0)
   	null.SetFrameFillStyle(0)
   	null.Draw()
   	null.cd()

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
   	null.Range(x1-LM,yf-BM,x2+RM,y2+TM)
	tri=TPolyLine(3,xx,yy)
	tri.SetFillColor(0)
	tri.Draw('f')
	c.SetLogz(1)
	c.SaveAs('pdf/'+name+'.pdf')
outfile.Close()
