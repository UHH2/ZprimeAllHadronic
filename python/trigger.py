from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors,kBlack,kWhite
from sys import argv
from os import system

from utils import compare,hadd,doeff,make_plot
gROOT.SetBatch()


path_base='/nfs/dust/cms/user/usaiem/miniaodv2/'
name_base='uhh2.AnalysisModuleRunner.'
datamu_filenames=["DATA.SingleMuon_Run2015D_05Oct2015_v1","DATA.SingleMuon_Run2015D_PromptReco_v4"]
dataht_filenames=["DATA.JetHT_Run2015D_05Oct2015_v1","DATA.JetHT_Run2015D_PromptReco_v4"]
ttbar_filenames=['MC.TTbar']
qcd_filenames=["MC.QCD_HT500to700","MC.QCD_HT700to1000","MC.QCD_HT1000to1500","MC.QCD_HT1500to2000","MC.QCD_HT2000toInf"]
mc_filenames=ttbar_filenames+qcd_filenames

force=True
datamu_filename=hadd(path_base,name_base,datamu_filenames,'datamu_trigger_merge',force)
dataht_filename=hadd(path_base,name_base,dataht_filenames,'dataht_trigger_merge',force)
ttbar_filename=hadd(path_base,name_base,ttbar_filenames,'ttbar_trigger_merge',force)
qcd_filename=hadd(path_base,name_base,qcd_filenames,'qcd_trigger_merge',force)
mc_filename=hadd(path_base,name_base,mc_filenames,'mc_trigger_merge',force)


datamu_file=TFile(datamu_filename)
dataht_file=TFile(dataht_filename)
ttbar_file=TFile(ttbar_filename)
qcd_file=TFile(qcd_filename)
mc_file=TFile(mc_filename)

outfile=TFile('outfile.root','RECREATE')

# colors=[kRed,kBlue,kBlack,kGreen,kOrange,6,9]

# histo_list=['HT']#,'pT4','SumOfTopCandidatesPt','LeadingTopCandidatePt','SubLeadingTopCandidatePt','HT50'
# histo_list2=['HT_{50} [GeV]']#,'p_{T} fourth AK5 jet'


# cut_list=["Trigger1Histos","Trigger2Histos","Trigger3Histos"]#,"Trigger4Histos","Trigger5Histos"
# trigger_names=["HLT_HT750","HLT_QuadJet50","HLT_HT750||HLT_QuadJet50"]
# base_cut="BaseHistos"



def getEff(name,den_input,num_input,rebin=0,xtitle='',ytitle=''):
  c=TCanvas(name+'_Canvas')
  legend=TLegend(0.8,0.1,0.999,0.6)
  legend.SetFillColor(kWhite)
  den=den_input.Clone()
  num=num_input.Clone()
  if rebin!=0:
      den.Rebin(rebin)
      num.Rebin(rebin)
  error_bars=TGraphAsymmErrors()
  error_bars.Divide(num,den,"cl=0.683 b(1,1) mode")
  error_bars.SetLineWidth(3)
  if xtitle=='':
    error_bars.GetXaxis().SetTitle(num.GetXaxis().GetTitle())
  else:
    error_bars.GetXaxis().SetTitle(xtitle)
  if ytitle=='':
    error_bars.GetYaxis().SetTitle(num.GetYaxis().GetTitle())
  else:
    error_bars.GetYaxis().SetTitle(ytitle)
  error_bars.GetXaxis().SetRangeUser(400,2000)
  error_bars.SetLineColor(kBlack)
  error_bars.SetMaximum(1.01)
  error_bars.SetMinimum(0.)
  if ytitle=='':
    error_bars.GetYaxis().SetTitle("Trigger rate")
  else:
    error_bars.GetYaxis().SetTitle(ytitle)
  error_bars.SetTitle('')
  error_bars.Draw('AP')
  #c.SaveAs('pdf/'+name+'.pdf')
  c.Write(name+'_Canvas')
  error_bars.Write(name)

def getSF(name,den_data_input,num_data_input,den_mc_input,num_mc_input,rebin=0,xtitle='',ytitle=''):
  c=TCanvas(name+'_Canvas')
  legend=TLegend(0.8,0.1,0.999,0.6)
  legend.SetFillColor(kWhite)
  den_data=den_data_input.Clone()
  num_data=num_data_input.Clone()
  den_mc=den_mc_input.Clone()
  num_mc=num_mc_input.Clone()
  if rebin!=0:
      den_mc.Rebin(rebin)
      num_mc.Rebin(rebin)
      den_data.Rebin(rebin)
      num_data.Rebin(rebin)
  num_mc.Divide(den_mc)
  num_data.Divide(den_data)
  num_data.Divide(num_mc)
  num_data.SetLineWidth(3)
  if xtitle=='':
    num_data.GetXaxis().SetTitle(num_data.GetXaxis().GetTitle())
  else:
    num_data.GetXaxis().SetTitle(xtitle)
  if ytitle=='':
    num_data.GetYaxis().SetTitle(num_data.GetYaxis().GetTitle())
  else:
    num_data.GetYaxis().SetTitle(ytitle)
  num_data.SetLineColor(kBlack)
  num_data.SetMaximum(1.5)
  num_data.SetMinimum(0.)
  if ytitle=='':
    num_data.GetYaxis().SetTitle("Scale factor")
  else:
    num_data.GetYaxis().SetTitle(ytitle)
  num_data.SetTitle('')
  num_data.GetXaxis().SetRangeUser(0,2500)
  num_data.Draw('HIST')
  #c.SaveAs('pdf/'+name+'.pdf')
  c.Write(name+'_Canvas')
  num_data.Write(name)

def getEffSF(name,data_file,mc_file,folder_postfix,histo_name,den_custom='',num_custom=''):
  den='den_'+folder_postfix+'/'+histo_name
  num='num_'+folder_postfix+'/'+histo_name
  if den_custom!='':
    den=den_custom
  if num_custom!='':
    num=num_custom
  getEff(name+'_eff_data_'+folder_postfix+'_'+histo_name,data_file.Get(den).Clone(),data_file.Get(num),1)
  getEff(name+'_eff_mc_'+folder_postfix+'_'+histo_name,mc_file.Get(den),mc_file.Get(num),1)
  getSF(name+'_sf_'+folder_postfix+'_'+histo_name,data_file.Get(den),
                             data_file.Get(num),
                             mc_file.Get(den),
                             mc_file.Get(num),1)
  # compare(
  #     name=name+'_'+folder_postfix+'_'+histo_name+'_DATAMC',
  #     file_list=[outfile,outfile],
  #     name_list=[name+'_eff_data_'+folder_postfix+'_'+histo_name,name+'_eff_mc_'+folder_postfix+'_'+histo_name],
  #     legend_list=['DATA','MC'],
  #     drawoption='AP',
  #     xtitle='HT [GeV]',
  #     ytitle='Trigger efficiency',
  #     #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
  #     textsizefactor=0.7)

paths=['mu0','mu1','mu2','ht0','ht1','ht2','mu0pt','mu1pt','mu2pt','ht0pt','ht1pt','ht2pt']

for i in paths:
  if 'mu' in i:
    # getEffSF('muqcd',datamu_file,qcd_file,i,'HT')
    # getEffSF('muttbar',datamu_file,ttbar_file,i,'HT')
    # getEffSF('muqcdttbar',datamu_file,mc_file,i,'HT')
    getEffSF('muqcd',datamu_file,qcd_file,i,'HTCA8')
    getEffSF('muttbar',datamu_file,ttbar_file,i,'HTCA8')
    getEffSF('muqcdttbar',datamu_file,mc_file,i,'HTCA8')
    compare(
      name='mu_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['muqcd_eff_data_'+i+'_HTCA8','muqcd_eff_mc_'+i+'_HTCA8','muttbar_eff_mc_'+i+'_HTCA8','muqcdttbar_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=1600,miny=0.3,maxy=1.1,rebin=1,
      textsizefactor=0.7)

    getEffSF('muqcd_subht',datamu_file,qcd_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    getEffSF('muttbar_subht',datamu_file,ttbar_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    getEffSF('muqcdttbar_subht',datamu_file,mc_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    compare(
      name='mu_subht_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['muqcd_subht_eff_data_'+i+'_HTCA8','muqcd_subht_eff_mc_'+i+'_HTCA8','muttbar_subht_eff_mc_'+i+'_HTCA8','muqcdttbar_subht_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
      textsizefactor=0.7)

    getEffSF('muqcd_subpt',datamu_file,qcd_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    getEffSF('muttbar_subpt',datamu_file,ttbar_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    getEffSF('muqcdttbar_subpt',datamu_file,mc_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    compare(
      name='mu_subpt_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['muqcd_subpt_eff_data_'+i+'_HTCA8','muqcd_subpt_eff_mc_'+i+'_HTCA8','muttbar_subpt_eff_mc_'+i+'_HTCA8','muqcdttbar_subpt_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
      textsizefactor=0.7)

  else:
    # getEffSF('htqcd',dataht_file,qcd_file,i,'HT')
    # getEffSF('htttbar',dataht_file,ttbar_file,i,'HT')
    # getEffSF('htqcdttbar',dataht_file,mc_file,i,'HT')
    getEffSF('htqcd',dataht_file,qcd_file,i,'HTCA8')
    getEffSF('htttbar',dataht_file,ttbar_file,i,'HTCA8')
    getEffSF('htqcdttbar',dataht_file,mc_file,i,'HTCA8')
    compare(
      name='ht_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['htqcd_eff_data_'+i+'_HTCA8','htqcd_eff_mc_'+i+'_HTCA8','htttbar_eff_mc_'+i+'_HTCA8','htqcdttbar_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
      textsizefactor=0.7)

    getEffSF('htqcd_subht',dataht_file,qcd_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    getEffSF('htttbar_subht',dataht_file,ttbar_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    getEffSF('htqcdttbar_subht',dataht_file,mc_file,i,'HTCA8','','num_'+i+'_subht'+'/HTCA8')
    compare(
      name='ht_subht_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['htqcd_subht_eff_data_'+i+'_HTCA8','htqcd_subht_eff_mc_'+i+'_HTCA8','htttbar_subht_eff_mc_'+i+'_HTCA8','htqcdttbar_subht_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
      textsizefactor=0.7)

    getEffSF('htqcd_subpt',dataht_file,qcd_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    getEffSF('htttbar_subpt',dataht_file,ttbar_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    getEffSF('htqcdttbar_subpt',dataht_file,mc_file,i,'HTCA8','','num_'+i+'_subpt'+'/HTCA8')
    compare(
      name='ht_subpt_'+i+'_HTCA8_DATAMC',
      file_list=[outfile,outfile,outfile,outfile],
      name_list=['htqcd_subpt_eff_data_'+i+'_HTCA8','htqcd_subpt_eff_mc_'+i+'_HTCA8','htttbar_subpt_eff_mc_'+i+'_HTCA8','htqcdttbar_subpt_eff_mc_'+i+'_HTCA8'],
      legend_list=['DATA','MC QCD','MC TTbar','MC QCD+TTbar'],
      drawoption='AP',
      xtitle='HT_{CA8} [GeV]',
      ytitle='Trigger efficiency',
      #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
      textsizefactor=0.7)

  
# getEff('DATA',data_file.Get('Denom/HT'),data_file.Get('Num/HT'),2)
# getEff('MC',mc_file.Get('Denom/HT'),mc_file.Get('Num/HT'),2)
# getSF('SF',data_file.Get('Denom/HT'),data_file.Get('Num/HT'),mc_file.Get('Denom/HT'),mc_file.Get('Num/HT'))

# compare(
#   name='DATAMC',
#   file_list=[outfile,outfile],
#   name_list=['DATA','MC'],
#   legend_list=['DATA','MC'],
#   drawoption='AP',
#   xtitle='HT [GeV]',
#   ytitle='Trigger efficiency',
#   #minx=0,maxx=0,rebin=1,miny=0,maxy=0,
#   textsizefactor=1)

#drawoption2= drawoption.replace("a", "")

#compare('SF',[outfile,outfile],['DATA','MC'],['DATA','MC'])

outfile.Close()

# def getEff2(histo_index,cut_index,rebin=0):
#   c=TCanvas(cut_list[cut_index]+'_'+histo_list[histo_index]+'_Canvas')
#   legend=TLegend(0.8,0.1,0.999,0.6)
#   legend.SetFillColor(kWhite)
#   eff_histos=[]
#   eff_error_bars=[]
#   sample_files=[]
#   for sample_index in range(len(sample_list)):
#     #print path_base+sample_list[sample_index]+'.root'
#     sample_files.append(TFile(path_base+sample_list[sample_index]+'.root'))
#     #print sample_file
#     base_hist=sample_files[-1].Get(base_cut+"/"+histo_list[histo_index]).Clone('base'+sample_list[sample_index]+'_'+cut_list[cut_index]+'_'+histo_list[histo_index])
#     trigger_hist=sample_files[-1].Get(cut_list[cut_index]+"/"+histo_list[histo_index]).Clone(cut_list[cut_index]+'_'+histo_list[histo_index]+'_'+sample_list[sample_index])
#     if rebin!=0:
#       base_hist.Rebin(rebin)
#       trigger_hist.Rebin(rebin)
#     #eff_histos.append(eff_histo)
#     #print sample_list[sample_index]+'_'+cut_list[cut_index]+'_'+histo_list[histo_index]
#     error_bars=TGraphAsymmErrors()
#     error_bars.Divide(trigger_hist,base_hist,"cl=0.683 b(1,1) mode")
#     eff_error_bars.append(error_bars)
#     eff_histos.append(trigger_hist)
#     eff_histos[-1].Divide(trigger_hist,base_hist,1,1,'B')
#     eff_histos[-1].SetStats(kFALSE)
#     eff_histos[-1].SetLineWidth(3)
#     eff_histos[-1].GetXaxis().SetTitle(histo_list2[histo_index])
#     eff_histos[-1].SetLineColor(colors[sample_index])
#     eff_histos[-1].SetMaximum(1.01)
#     eff_histos[-1].SetMinimum(0.)
#     eff_histos[-1].GetYaxis().SetTitle("Trigger rate")
#     eff_histos[-1].SetTitle(trigger_names[cut_index])
    
#     eff_error_bars[-1].SetLineWidth(3)
#     eff_error_bars[-1].GetXaxis().SetTitle(histo_list2[histo_index])
#     eff_error_bars[-1].SetLineColor(colors[sample_index])
#     eff_error_bars[-1].SetMaximum(1.01)
#     eff_error_bars[-1].SetMinimum(0.)
#     eff_error_bars[-1].GetYaxis().SetTitle("Trigger rate")
#     eff_error_bars[-1].SetTitle(trigger_names[cut_index])
    
#     legend.AddEntry(eff_histos[-1],sample_names[sample_index],'l')
#     if len(eff_histos)==1:
#       c.cd()
#       #eff_histos[-1].Draw('AXIS')
#       eff_error_bars[-1].Draw('AP')
#     else:
#       c.cd()
#       #eff_histos[-1].Draw('SAME')
#       eff_error_bars[-1].Draw('PSAME')
#     c2=TCanvas(cut_list[cut_index]+'_'+histo_list[histo_index]+'_'+sample_list[sample_index]+'_Canvas')
#     #eff_histos[-1].Draw('AXIS')
#     eff_error_bars[-1].Draw('AP')
#     #eff_error_bars[-1].Write()
#     legend2=TLegend(0.8,0.2,0.999,0.93)
#     legend2.AddEntry(eff_histos[-1],sample_list[sample_index],'l')
#     legend2.Draw()
#     c2.SaveAs("pdf/"+cut_list[cut_index]+'_'+histo_list[histo_index]+'_'+sample_list[sample_index]+".pdf")
#     outfile.cd()
#     eff_histos[-1].Write()
#     c2.Write()
  
#   c.cd()
#   legend.Draw()
#   c.SaveAs("pdf/"+cut_list[cut_index]+'_'+histo_list[histo_index]+".pdf")
#   outfile.cd()
#   c.Write()