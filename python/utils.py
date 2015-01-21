from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors,THStack,kRed,kYellow,kGray
from os import system
from sys import argv
from os import mkdir
from os.path import exists

def compare(name,file_list,name_list,legend_list,normalize=False,drawoption='hE',xtitle='',maxx=0):
  c=TCanvas(name,'',600,600)
  c.SetLeftMargin(0.15)#
  c.SetRightMargin(0.05)#
  # c.SetTopMargin(0.05)#
  c.SetBottomMargin(0.10)
  # if not useOutfile:
  # legend=TLegend(0.7,0.7,0.95,0.95)
  # else:
  c.SetTopMargin(0.15)
  legend=TLegend(0.0,0.85,0.99,0.99)
  #legend=TLegend(0.35,0.2,0.85,0.5)
  legend.SetHeader('')
  #legend.SetTextSize(0.03)
  legend.SetBorderSize(0)
  legend.SetTextFont(42)
  legend.SetLineColor(1)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  histo_list=[]
  # tfile_list=[]
  maxy=0.0
  for i in range(len(name_list)):
    # tfile_list.append(TFile(file_list[i],'READ'))
    histo_list.append(file_list[i].Get(name_list[i]))
    if normalize:
      histo_list[-1].Scale(1.0/(histo_list[-1].Integral()+0.00000001))
    if not histo_list[-1].ClassName()=='TGraphAsymmErrors':
      histo_list[-1].SetStats(0)
    histo_list[-1].SetLineWidth(3)
    histo_list[-1].SetLineColor(i+1)
    histo_list[-1].SetTitle('')
    legend.AddEntry(histo_list[-1],legend_list[i],'l')
    maxy=max(maxy,histo_list[-1].GetMaximum()*1.05)
  for i in range(len(name_list)):
    if i==0:
      if not histo_list[-1].ClassName()=='TGraphAsymmErrors':
        histo_list[i].SetMaximum(maxy)
      else:
        histo_list[i].SetMaximum(1.05)
        histo_list[i].SetMinimum(0.0)
      histo_list[i].Draw(drawoption)
      # if useOutfile:
      histo_list[i].GetXaxis().SetTitle(xtitle)
      if not maxx==0:
        histo_list[i].GetXaxis().SetRangeUser(0,maxx)
      #   histo_list[i].GetYaxis().SetTitle('Efficiency')
    else:
      histo_list[i].Draw(drawoption+'SAME')
  legend.Draw()
  # outfile.cd()
  # c.Write(name)
  c.SaveAs('pdf/'+name+'.pdf')
  #c.SaveAs(folder+name+'.png')

def hadd(path_base,name_base,inputlist,outputname):
  command_list='hadd -f '+path_base+outputname+'.root'#-v 0
  for i in inputlist:
    command_list+=' '+path_base+name_base+i+'.root'
  system(command_list)
  return path_base+outputname+'.root'

def doeff(filename, histoname_den, histoname_num, triggername, outfile,rebin=1):
  numerator=filename.Get(histoname_num)
  denominator=filename.Get(histoname_den)
  if not rebin==1:
    numerator.Rebin(rebin)
    denominator.Rebin(rebin)
  n_num=numerator.Integral()
  n_den=denominator.Integral()
  error_bars=TGraphAsymmErrors()
  error_bars.Divide(numerator,denominator,"cl=0.683 b(1,1) mode")
  outfile.cd()
  error_bars.Write(triggername)
  return n_num/n_den

def make_plot(name, ttbar_file, qcd_file, signal_files, histo):
  c=TCanvas(name,'',600,600)
  c.SetLeftMargin(0.15)#
  c.SetRightMargin(0.05)#
  c.SetBottomMargin(0.10)
  c.SetTopMargin(0.15)
  legend=TLegend(0.0,0.85,0.99,0.99)
  legend.SetHeader('')
  #legend.SetTextSize(0.03)
  legend.SetBorderSize(0)
  legend.SetTextFont(42)
  legend.SetLineColor(1)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  stack=THStack(name+'_stack','')
  ttbar_histo=ttbar_file.Get(histo)
  qcd_histo=qcd_file.Get(histo)
  signal_histos=[]
  colors=[28,9,8]
  for i in range(len(signal_files)):
    signal_histos.append(signal_files[i].Get(histo))
    signal_histos[i].SetLineWidth(3)
    signal_histos[i].SetLineStyle(1)
    signal_histos[i].SetLineColor(colors[i])
  ttbar_histo.SetFillColor(kRed)
  qcd_histo.SetFillColor(kYellow)
  ttbar_histo.SetLineColor(kRed)
  qcd_histo.SetLineColor(kYellow)
  ttbar_histo.SetMarkerColor(kRed)
  qcd_histo.SetMarkerColor(kYellow)
  legend.AddEntry(ttbar_histo,'t#bar{t}','f')
  legend.AddEntry(qcd_histo,'QCD MC','f')
  legend.AddEntry(signal_histos[0],"Z' 1 TeV 1pb",'l')
  legend.AddEntry(signal_histos[1],"Z' 2 TeV 1pb",'l')
  legend.AddEntry(signal_histos[2] ,"Z' 3 TeV 1pb",'l')
  stack.Add(ttbar_histo)
  stack.Add(qcd_histo)
  errors=ttbar_histo.Clone(histo+'tmp')
  errors.Add(qcd_histo)
  err=TGraphAsymmErrors(errors)
  stack.Draw('hist')
  stack.GetXaxis().SetRangeUser(0,4000)
  err.SetFillStyle(3145)
  err.SetFillColor(kGray)
  err.Draw('2')
  #summc.Draw('samehist')
  #stack.SetMinimum(0.1)
  stack.SetMaximum(stack.GetMaximum()*1.2)
  stack.GetXaxis().SetTitle("m_{t#bar{t}}")
  stack.GetYaxis().SetTitle('Events')
  signal_histos[0].Draw('samehist')
  signal_histos[1].Draw('samehist')
  signal_histos[2].Draw('samehist')
  legend.Draw()
  c.SaveAs('pdf/'+name+'.pdf')
