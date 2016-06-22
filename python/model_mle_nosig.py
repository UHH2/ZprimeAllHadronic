def get_model_nosig():
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/theta_66_1p0_0p0_0p0.root', 
    include_mc_uncertainties = False, histogram_filter=lambda x: ('signal' not in x) 
    and ('_jer_' not in x)
    and ('_toptag_' not in x)
    and ('_btag_' not in x)
    and ('_subjetbtag_' not in x)
    and ('_mu_' not in x)
    and ('_jec_' not in x)
    and ('_wtag_' not in x)
    and ('_bkgcorr_' not in x)
    and ('_pu_' not in x) )#mc uncertainties=true
    model.fill_histogram_zerobins()
    model.add_lognormal_uncertainty('qcdnorm', math.log(1.10), 'qcd')
    model.add_lognormal_uncertainty('ttbarnorm', math.log(1.10), 'ttbar')
    #model.set_signal_processes('signal*')
    #model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    #model.add_lognormal_uncertainty('qcd_rate', math.log(1.15), 'qcd')
    # for p in model.processes:
    #     if p == 'qcd': continue
    #     model.add_lognormal_uncertainty('lumi', math.log(1.027), p)
    #     model.add_lognormal_uncertainty('trigger', math.log(1.03), p)
    #     #if 'signal' in p:
    #     #    model.add_lognormal_uncertainty(p+'_rate', math.log(1.15), p)
    return model

model_nosig = get_model_nosig()
model_summary(model_nosig)
options = Options()
options.set('main', 'n_threads', '20')
options.set('global', 'check_cache', 'False')
#plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'
postfit=mle(model_nosig, input='data', n=1, signal_process_groups = {'': []}, with_covariance=True)
print postfit
f=open('anosig.txt','w')
for i in postfit['']:
   if i!='__nll':
       f.write(str(postfit[''][i][0][0])+' '+str(postfit[''][i][0][1])+' '+i+'\n')
f.close()

#postfit.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta2/limits_exp_66_1p0_0p0_0p0.txt')
# plot_exp, plot_obs = bayesian_limits(model,what='all')#bayesian_limits ,what='expected'
# plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp_66_1p0_0p0_0p0.txt')
# plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs_66_1p0_0p0_0p0.txt')
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta2/htmlout_66_1p0_0p0_0p0nosig')
#~/xxl-af-cms/code/theta/theta/utils2/theta-auto.py theta/model_66_1p0_0p0_0p0.py 