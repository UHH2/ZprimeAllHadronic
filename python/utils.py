from ROOT import TFile,TCanvas,gROOT,gStyle,TLegend,TGraphAsymmErrors
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
    histo_list[-1].SetStats(0)
    histo_list[-1].SetLineWidth(3)
    histo_list[-1].SetLineColor(i+1)
    histo_list[-1].SetTitle('')
    legend.AddEntry(histo_list[-1],legend_list[i],'l')
    maxy=max(maxy,histo_list[-1].GetMaximum()*1.05)
  for i in range(len(name_list)):
    if i==0:
      histo_list[i].SetMaximum(maxy)
      # else:
      #   histo_list[i].SetMaximum(1.05)
      #   histo_list[i].SetMinimum(0.0)
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
  command_list='hadd '+path_base+outputname+'.root'#-v 0
  for i in inputlist:
    command_list+=' '+path_base+name_base+i+'.root'
  system(command_list)
  return path_base+outputname+'.root'

def doeff(filename, histoname, triggername):
  tmp_file=TFile(filename,'READ')
  numerator=tmp_file.Get(triggername+'/'+histoname+'Passing')
  denominator=tmp_file.Get(triggername+'/'+histoname+'Denom')
  n_num=numerator.Integral()
  n_den=denominator.Integral()
  error_bars=TGraphAsymmErrors()
  error_bars.Divide(numerator,denominator,"cl=0.683 b(1,1) mode")
  outfile.cd()
  error_bars.Write(filename.split('.')[0]+'_'+histoname+'_'+triggername)
  return n_num/n_den

def make_plot(histo_name,folder=htfolder,override=False,ttbar1=0,ttbar2=0,bkg1=0,bkg2=0,data1=0,data2=0,err1=0,err2=0): 
    zf=1
    legendstring="HEPTopTagger HT>800 GeV"
    if folder==mjfolder:
      legendstring="HEPTopTagger HT<800 GeV"
    if override:
      legendstring="HEPTopTagger"
    larghezza=0.7
    if histo_name in ['Mtt0','Mtt1','Mtt2','Mtt012']:
      larghezza=0.5
    legend=TLegend(larghezza,0.5,0.945,0.895,legendstring)
    legend.SetFillColor(kWhite)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    if histo_name in ['Mtt0','Mtt1','Mtt2','Mtt012']:
      legend.SetTextSize(0.05)
    stack=THStack(histo_name+us+'stack','')
    #ttbar_histo=ttbar_file.Get(cut_name+'/'+histo_name).Clone('ttbar'+us+histo_name+us+cut_name)
    #qcd_histo=qcd_file.Get(cut_name+'/'+histo_name).Clone('qcd'+us+histo_name+us+cut_name)
    #data_histo=data_file.Get(cut_name+'/'+histo_name).Clone('data'+us+histo_name+us+cut_name)
    bkg_histo_name=histo_name
    measured_histo_name='Measured'+histo_name
    #if '_0btag_' in cut_name:
      #bkg_histo_name='Mtt0'
      #measured_histo_name='MeasuredMtt0'
    #elif '_1btag_' in cut_name:
      #bkg_histo_name='Mtt1'
      #measured_histo_name='MeasuredMtt1'
    #elif '_2btag_' in cut_name:
      #bkg_histo_name='Mtt2'
      #measured_histo_name='MeasuredMtt2'
    #elif '_012btag_' in cut_name:
      #bkg_histo_name='Mtt012'
      #measured_histo_name='MeasuredMtt012'
    if folder==mjfolder:
      data_file=mjdata_file
    else:
      data_file=htdata_file
    data_histo=data_file.Get(folder+measured_histo_name).Clone('data'+us+histo_name)
    bkg_histo=data_file.Get(folder+bkg_histo_name).Clone('bkg'+us+histo_name)#background_file.Get(folder+bkg_histo_name).Clone('bkg'+us+histo_name+us+cut_name)
    bkg_histo_up=bkg_histo.Clone('bkg'+us+histo_name+'_up')
    bkg_histo_down=bkg_histo.Clone('bkg'+us+histo_name+'_down')
    ttbar_histo=ttbar_file.Get(folder+measured_histo_name).Clone('ttbar'+us+histo_name)
    ttbkg_histo=ttbar_file.Get(folder+bkg_histo_name)
    qcd_histo=bkg_histo.Clone("aa")#qcd_file.Get(folder+measured_histo_name).Clone('qcd'+us+histo_name)
    ###mistag error propagation
    sys_diff=[]
    for imtt in range(1,ttbar_histo.GetNbinsX()+1):
      sys_diff.append([])
    for isys in range(1,len(systematics)):
      ttf=TFile(path_base+cyclename+'TTbar'+systematics[isys]+'.root','READ')
      outfile.cd()
      ttbar_tmp=ttf.Get(folder+measured_histo_name).Clone('ttbar'+theta_sys[isys])
      ttbar_tmp.Add(ttbar_histo,-1)
      for imtt in range(1,ttbar_histo.GetNbinsX()+1):
        sys_diff[imtt-1].append(ttbar_tmp.GetBinContent(imtt))
    
    doaverageq2=True
    ttbar_q2up=ttbar_histo.Clone('ttbar_q2up')
    ttbar_q2down=ttbar_histo.Clone('ttbar_q2down')
    if doaverageq2:
      ttf_up=TFile(path_base+cyclename+'TTbar'+'_scaleup'+'.root','READ')
      ttf_down=TFile(path_base+cyclename+'TTbar'+'_scaledown'+'.root','READ')
      tt_up=ttf_up.Get(folder+measured_histo_name).Clone('ttbar_q2up')
      tt_down=ttf_down.Get(folder+measured_histo_name).Clone('ttbar_q2down')
      tt_updiff=ttbar_histo.Clone('tt_updiff')
      tt_downdiff=ttbar_histo.Clone('tt_downdiff')
      tt_updiff.Add(tt_up,-1)
      tt_downdiff.Add(tt_down,-1)
      for imtt in range(1,ttbar_histo.GetNbinsX()+1):
        diff=max(abs(tt_updiff.GetBinContent(imtt)),abs(tt_downdiff.GetBinContent(imtt)))
        sys_diff[imtt-1].append(diff)
        sys_diff[imtt-1].append(-diff)
        ttbar_q2up.SetBinContent(imtt,ttbar_q2up.GetBinContent(imtt)+diff)
        ttbar_q2down.SetBinContent(imtt,ttbar_q2down.GetBinContent(imtt)-diff)

    if histo_name=='Mtt0' or histo_name=='Mtt1' or histo_name=='Mtt2':
      #for imtt in range(1,ttbar_histo.GetNbinsX()+1):
      #  sys_diff.append([])
      #for isys in range(1,len(systematics)):
      #  ttf=TFile(path_base+cyclename+'TTbar'+systematics[isys]+'.root','READ')
      #  outfile.cd()
      #  ttbar_tmp=ttf.Get(folder+measured_histo_name).Clone('ttbar'+theta_sys[isys])
      #  ttbar_tmp.Add(ttbar_histo,-1)
      #  for imtt in range(1,ttbar_histo.GetNbinsX()+1):
      #    sys_diff[imtt-1].append(ttbar_tmp.GetBinContent(imtt))
      
      the_pdfsysfilename='thetapdf.root'
      if folder==mjfolder:
        the_pdfsysfilename='mjthetapdf.root'
      pdffile=TFile(the_pdfsysfilename,"READ")
      the_namebase='httbtag'
      if folder==mjfolder:
        the_namebase='mjhttbtag'
      uu='__'
      pdfttbarup=pdffile.Get(the_namebase+histo_name[3]+uu+'ttbar'+uu+'pdf__plus').Clone('pdfup'+the_namebase+histo_name[3])
      pdfttbardown=pdffile.Get(the_namebase+histo_name[3]+uu+'ttbar'+uu+'pdf__minus').Clone('pdfdown'+the_namebase+histo_name[3])
      pdfttbarup.Add(ttbar_histo,-1)
      pdfttbardown.Add(ttbar_histo,-1)
      for imtt in range(1,ttbar_histo.GetNbinsX()+1):
        sys_diff[imtt-1].append(pdfttbarup.GetBinContent(imtt))
        sys_diff[imtt-1].append(pdfttbardown.GetBinContent(imtt))
      #print sys_diff
      mistag_matrix=bkg_file.Get(folder+"Mistag/data_htt/Mistag_data_htt")
      errmtt=data_file.Get(folder+'Err'+histo_name)
      for mtt_bin in range(1,errmtt.GetNbinsX()+1):
        a1 = 0.0
        a2 = 0.0
        den = 0.0
        for pt_bin in range(1,errmtt.GetNbinsY()+1):
          for csv_bin in range(1,errmtt.GetNbinsZ()+1):
            #print errmtt.GetBinContent(mtt_bin,pt_bin,csv_bin)
            a1 += mistag_matrix.GetBinContent(pt_bin,csv_bin) * sqrt(errmtt.GetBinContent(mtt_bin,pt_bin,csv_bin))
            a2 += mistag_matrix.GetBinError(pt_bin,csv_bin) * errmtt.GetBinContent(mtt_bin,pt_bin,csv_bin)
            den += mistag_matrix.GetBinContent(pt_bin,csv_bin) * errmtt.GetBinContent(mtt_bin,pt_bin,csv_bin)
            dx=0.0
            if  den>0.0:
              dx = sqrt(a1*a1+a2*a2)/ den
                #print mtt_bin,dx
        bkg_histo.SetBinError(mtt_bin, dx * bkg_histo.GetBinContent(mtt_bin))
        bkg_histo_up.SetBinContent(mtt_bin, bkg_histo.GetBinContent(mtt_bin) + dx * bkg_histo.GetBinContent(mtt_bin))
        bkg_histo_down.SetBinContent(mtt_bin, bkg_histo.GetBinContent(mtt_bin) - dx * bkg_histo.GetBinContent(mtt_bin))
    ###
    
    #ttbkg_histo.Scale(0.92*0.95*0.95*0.92)
    bkg_histo.Add(ttbkg_histo,-1.0)######################################## ttbar subtraction
    bkg_histo_up.Add(ttbkg_histo,-1.0)########################################
    bkg_histo_down.Add(ttbkg_histo,-1.0)########################################
    sum_mc=ttbar_histo.Clone('sum_mc'+us+histo_name)
    sum_mc.Add(bkg_histo)
    err=TGraphAsymmErrors(sum_mc)
    sysup=[]
    relsysup=[]
    sysdown=[]
    if True:#histo_name=='Mtt0' or histo_name=='Mtt1' or histo_name=='Mtt2':
      for ierr in range(1,err.GetN()+1):
        eup=0.
        edown=0.
        for i in sys_diff[ierr-1]:
          #print i
          if i<0:
            edown=edown+i*i
          else:
            eup=eup+i*i
        sysup.append(sqrt(eup))
        relsysup.append(sqrt(eup)/(ttbar_histo.GetBinContent(ierr)+0.00000001))
        sysdown.append(sqrt(edown))
        #print eup,err.GetErrorYhigh(ierr)
        lumierr=0.0263*ttbar_histo.GetBinContent(ierr)
        trigerr=0#0.0202*ttbar_histo.GetBinContent(ierr)
        xserr=0.1618*ttbar_histo.GetBinContent(ierr)
        err.SetPointEYhigh(ierr-1,sqrt(lumierr*lumierr+trigerr*trigerr+xserr*xserr+err.GetErrorYhigh(ierr-1)*err.GetErrorYhigh(ierr-1)+eup))
        err.SetPointEYlow(ierr-1,sqrt(lumierr*lumierr+trigerr*trigerr+xserr*xserr+err.GetErrorYlow(ierr-1)*err.GetErrorYlow(ierr-1)+edown))
    #print relsysup
    if override:
      ttbarm=ttbar1.Clone()
      ttbarm.Add(ttbar2)
      bkgm=bkg1.Clone()
      bkgm.Add(bkg2)
      datam=data1.Clone()
      datam.Add(data2)
      errm=err1.Clone()
      sum_mcm=ttbarm.Clone()
      sum_mcm.Add(bkgm)
      errm=TGraphAsymmErrors(sum_mcm)
      for ierr in range(1,err1.GetN()+1):
        errm.SetPointEYhigh(ierr-1,sqrt(err1.GetErrorYhigh(ierr-1)*err1.GetErrorYhigh(ierr-1)+err2.GetErrorYhigh(ierr-1)*err2.GetErrorYhigh(ierr-1)))
        errm.SetPointEYlow(ierr-1,sqrt(err1.GetErrorYlow(ierr-1)*err1.GetErrorYlow(ierr-1)+err2.GetErrorYlow(ierr-1)*err2.GetErrorYlow(ierr-1)))
      sum_mc=sum_mcm
      data_histo=datam
      ttbar_histo=ttbarm
      bkg_histo=bkgm
      err=errm

    sum_mc_noerr=sum_mc.Clone('sum_mc_noerr'+us+histo_name)
    for i in range(1,sum_mc_noerr.GetNbinsX()+1):
      sum_mc_noerr.SetBinError(i,0)
    
    data_histo_noerr=data_histo.Clone('data_noerr'+us+histo_name)
    for i in range(1,data_histo_noerr.GetNbinsX()+1):
      data_histo_noerr.SetBinError(i,0)
    ratio_histo_nodataerr=data_histo_noerr.Clone('ratio_nodataerr'+us+histo_name)
    ratio_histo_nodataerr.Divide(sum_mc)
    ratio_histo_nodataerr2=ratio_histo_nodataerr.Clone('ratio_nodataerr2'+us+histo_name)
    for i in range(1,ratio_histo_nodataerr.GetNbinsX()+1):
      ratio_histo_nodataerr.SetBinContent(i,1)
      #if ratio_histo_nodataerr.GetBinError(i)==0:
  #ratio_histo_nodataerr.SetBinError(i,1.25)
    err_ratio=TGraphAsymmErrors(ratio_histo_nodataerr)
    if True:#histo_name=='Mtt0' or histo_name=='Mtt1' or histo_name=='Mtt2':
      for ierr in range(1,err.GetN()+1):
        if sum_mc.GetBinContent(ierr)>0:
          val=sum_mc.GetBinContent(ierr)
          staterr=sum_mc.GetBinError(ierr)
          #err_ratio.SetPointEYhigh(ierr,sqrt(staterr*staterr/(val*val)+sysup[ierr-1]*sysup[ierr-1]/(val*val)))
          #err_ratio.SetPointEYlow(ierr,sqrt(staterr*staterr/(val*val)+sysdown[ierr-1]*sysdown[ierr-1]/(val*val)))
          #print err.GetErrorYhigh(ierr-1),sqrt(staterr*staterr+sysup[ierr-1]*sysup[ierr-1])
          if data_histo.GetBinContent(ierr)>0:
            err_ratio.SetPointEYhigh(ierr-1,err.GetErrorYhigh(ierr-1)/val)
            err_ratio.SetPointEYlow(ierr-1,err.GetErrorYlow(ierr-1)/val)
          else:
            err_ratio.SetPointEYhigh(ierr-1,0)
            err_ratio.SetPointEYlow(ierr-1,0)

    
    summc=sum_mc.Clone('summc')
    summc.SetLineColor(kBlack)
    ratio_histo=data_histo.Clone('ratio'+us+histo_name)
    ratio_histo.Divide(sum_mc_noerr)
    ratio_histo.SetLineColor(1)
    ratio_histo.SetLineStyle(1)
    ratio_histo.SetLineWidth(1)
    ratio_histo.SetMarkerColor(1)
    ratio_histo.SetMarkerStyle(8)
    ratio_histo.SetMarkerSize(1)
    ratio_histo.SetStats(0)
    ratio_histo.SetTitle('') 
    ratio_histo.GetYaxis().SetLabelSize(0.16333)
    ratio_histo.GetYaxis().SetTitleSize(0.16333)
    ratio_histo.GetYaxis().SetTitleOffset(0.4928)
    ratio_histo.GetXaxis().SetLabelSize(0.16333)
    ratio_histo.GetXaxis().SetTitleSize(0.16333)
    ratio_histo.GetXaxis().SetTitleOffset(1.3)
    ratio_histo.GetYaxis().SetTitle('Data/Bkg')
    #ratio_histo.GetXaxis().SetTitle('m_{t#bar{t}} [GeV]')
    ratio_histo.GetYaxis().SetRangeUser(-0.25,2.25)
    ratio_histo.GetYaxis().SetNdivisions(3,2,0)
    #ratio_histo.GetXaxis().SetRangeUser(ratio_histo.GetXaxis().GetXmin(),ratio_histo.GetXaxis().GetXmax()*zf)
    line1=TLine(ratio_histo.GetXaxis().GetXmin(),1.0,ratio_histo.GetXaxis().GetXmax(),1.0)#*zf
    line1.SetLineStyle(2)
    ttbar_histo.SetFillColor(kRed)
    qcd_histo.SetFillColor(kYellow)
    bkg_histo.SetFillColor(kYellow)
    ttbar_histo.SetLineColor(kRed)
    qcd_histo.SetLineColor(kYellow)
    bkg_histo.SetLineColor(kYellow)
    ttbar_histo.SetMarkerColor(kRed)
    qcd_histo.SetMarkerColor(kYellow)
    bkg_histo.SetMarkerColor(kYellow)
    data_histo.SetLineColor(1)
    data_histo.SetLineStyle(1)
    data_histo.SetLineWidth(1)
    data_histo.SetMarkerColor(1)
    data_histo.SetMarkerStyle(8)
    data_histo.SetMarkerSize(1)
    #data_histo.GetXaxis().SetRangeUser(data_histo.GetXaxis().GetXmin(),data_histo.GetXaxis().GetXmax()*zf)
    legend.AddEntry(data_histo,'Data','pEX0')
    legend.AddEntry(ttbar_histo,'t#bar{t}','f')
    #legend.AddEntry(qcd_histo,'QCD MC','f')
    legend.AddEntry(bkg_histo,'NTMJ','f')
    stack.Add(ttbar_histo)
    #stack.Add(qcd_histo)
    stack.Add(bkg_histo)
    cmslabelstring="CMS Preliminary #sqrt{s} = 8TeV  19.7 fb^{-1}"
    if folder==mjfolder:
      cmslabelstring="CMS Preliminary #sqrt{s} = 8TeV  18.3 fb^{-1}"
    if override:
      cmslabelstring="CMS Preliminary #sqrt{s} = 8TeV  18.3-19.7 fb^{-1}"
    cmslabel=TLatex(0.15,0.925,cmslabelstring)
    #cmslabel=TLatex(0.15,0.925,"Private work")
    cmslabel.SetTextSize(0.07)
    cmslabel.SetNDC()
    cmslabel.SetTextFont(42)
    #cmslabel.SetLineWidth(5)
    
    signal1000=signal_files[process_names_signal_narrow.index('750')].Get(folder+measured_histo_name).Clone('ZP1000'+us+histo_name)
    signal2000=signal_files[process_names_signal_narrow.index('1000')].Get(folder+measured_histo_name).Clone('ZP2000'+us+histo_name)
    signal3000=signal_files[process_names_signal_narrow.index('1250')].Get(folder+measured_histo_name).Clone('ZP3000'+us+histo_name)
    if override:
      signal1000.Add(signal_files[process_names_signal_narrow.index('750')].Get(mjfolder+measured_histo_name).Clone('ZP1000'+us+histo_name))
      signal2000.Add(signal_files[process_names_signal_narrow.index('1000')].Get(mjfolder+measured_histo_name).Clone('ZP2000'+us+histo_name))
      signal3000.Add(signal_files[process_names_signal_narrow.index('1250')].Get(mjfolder+measured_histo_name).Clone('ZP3000'+us+histo_name))
    signal1000.SetLineWidth(3)
    signal1000.SetLineStyle(1)
    signal2000.SetLineWidth(3)
    signal2000.SetLineStyle(1)
    signal3000.SetLineWidth(3)
    signal3000.SetLineStyle(1)
    signal1000.SetLineColor(28)
    signal2000.SetLineColor(9)
    signal3000.SetLineColor(8)
    signal1000.Scale(3.0)
    signal2000.Scale(3.0)
    signal3000.Scale(3.0)
    legend.AddEntry(signal1000,"Z' 750 GeV 3pb",'l')
    legend.AddEntry(signal2000,"Z' 1.0 TeV 3pb",'l')
    legend.AddEntry(signal3000,"Z' 1.25 TeV 3pb",'l')
    
    mjpostfix=''
    if folder==mjfolder:
      mjpostfix='mj'
    canvas=TCanvas(histo_name+mjpostfix+us+'canvas','',0,0,600,600)#,'',100,100)
    canvas.Divide(1,2)
    top_pad=canvas.GetPad(1)
    bottom_pad=canvas.GetPad(2)
    top_pad.SetPad( 0.0, 0.30, 1.0, 1.0 )
    bottom_pad.SetPad( 0.0, 0.0, 1.0, 0.30 )
    #top_pad.SetLeftMargin(0.18)#0.15
    #top_pad.SetRightMargin(0.05)#0.01
    #top_pad.SetTopMargin(0.13)#0.10
    #top_pad.SetBottomMargin(0.15)#0.0
    top_pad.SetLeftMargin(0.15)#
    top_pad.SetRightMargin(0.05)#
    top_pad.SetTopMargin(0.10)#
    top_pad.SetBottomMargin(0.0)#
    bottom_pad.SetLeftMargin(0.15)
    bottom_pad.SetRightMargin(0.05)
    bottom_pad.SetTopMargin(0.0)
    bottom_pad.SetBottomMargin(0.45)
    top_pad.cd()
    stack.Draw('hist')
    err.SetFillStyle(3145)
    err.SetFillColor(kGray)
    err.Draw('2')
    data_histo.Draw("sameEX0")
    #if histo_name not in ['Mtt0','Mtt1','Mtt2','Mtt012']:
    summc.Draw('samehist')
    stack.SetMinimum(0.1)
    stack.SetMaximum(stack.GetMaximum()*1.2)
    stack.GetXaxis().SetTitle("a")#ttbar_histo.GetXaxis().GetTitle())
    stack.GetYaxis().SetTitle('Events')
    stack.GetYaxis().SetLabelSize(0.07)
    stack.GetYaxis().SetTitleSize(0.07)
    stack.GetYaxis().SetTitleOffset(1.15)
    stack.GetXaxis().SetLabelSize(0.07)
    stack.GetXaxis().SetTitleSize(0.07)
    stack.GetXaxis().SetTitleOffset(1.0)
#stack.GetYaxis().SetRangeUser(stack.GetYaxis().GetXmin(),stack.GetYaxis().GetXmax()*1.5)
    
    #stack.GetYaxis().SetLabelSize(0.045)
    #stack.GetYaxis().SetTitleSize(0.045)
    #stack.GetYaxis().SetTitleOffset(1.9)
    #stack.GetXaxis().SetLabelSize(0.045)
    #stack.GetXaxis().SetTitleSize(0.045)
    #stack.GetXaxis().SetTitleOffset(1.5)
    
    #stack.GetXaxis().SetRangeUser(stack.GetXaxis().GetXmin(),stack.GetXaxis().GetXmax()*zf)
    signal1000.Draw('samehist')
    signal2000.Draw('samehist')
    signal3000.Draw('samehist')
    legend.Draw()
    cmslabel.Draw()
    bottom_pad.cd()
    err_ratio.SetFillStyle(1001)
    err_ratio.SetFillColor(kGray)
    ratio_histo.Draw('EX0')
    err_ratio.Draw('same2')
    ratio_histo.Draw('sameEX0')
    line1.Draw()
    #outfile.cd(cut_name)
    outfile.cd()
    canvas.Write()
    overridepostfix=''
    if override:
      overridepostfix='merge'
    canvas.SaveAs('pdf/'+folder+canvas.GetName()+overridepostfix+'.pdf')
    if histo_name in ['Mtt0','Mtt1','Mtt2','Mtt012']:
      canvas.SaveAs('pdf/'+folder+canvas.GetName()+overridepostfix+'.png')
    bkg_histo.Write()
    bkg_histo_up.Write()
    bkg_histo_down.Write()
    return [bkg_histo,bkg_histo_up,bkg_histo_down,ttbar_q2up,ttbar_q2down,ttbar_histo,data_histo,err]