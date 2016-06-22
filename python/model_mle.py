def get_model():
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/theta_66_1p0_0p0_0p0.root', include_mc_uncertainties = True)#mc uncertainties=true
    model.fill_histogram_zerobins()
    model.set_signal_processes('signal*')
    #model.add_lognormal_uncertainty('ttbar_rate', math.log(1.15), 'ttbar')
    #model.add_lognormal_uncertainty('qcd_rate', math.log(1.15), 'qcd')
    for p in model.processes:
        if p == 'qcd': continue
        model.add_lognormal_uncertainty('lumi', math.log(1.027), p)
        model.add_lognormal_uncertainty('trigger', math.log(1.03), p)
        #if 'signal' in p:
        #    model.add_lognormal_uncertainty(p+'_rate', math.log(1.15), p)
    return model

model = get_model()
model_summary(model)
options = Options()
options.set('main', 'n_threads', '20')
#plot_exp, plot_obs = asymptotic_cls_limits(model,use_data=False,options=options)#bayesian_limits ,what='expected'
postfit=mle(model, input='data', n=1, with_covariance=True)
f=open('a.txt','w')
for i in postfit['signal_525_2_1p2_1p0_0p0_0p0']:
    if i!='__nll':
        f.write(str(postfit['signal_525_2_1p2_1p0_0p0_0p0'][i][0][0])+' '+str(postfit['signal_525_2_1p2_1p0_0p0_0p0'][i][0][1])+' '+i+'\n')
f.close()
#postfit.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta2/limits_exp_66_1p0_0p0_0p0.txt')
# plot_exp, plot_obs = bayesian_limits(model,what='all')#bayesian_limits ,what='expected'
# plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_exp_66_1p0_0p0_0p0.txt')
# plot_obs.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta/limits_obs_66_1p0_0p0_0p0.txt')
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/theta2/htmlout_66_1p0_0p0_0p0')