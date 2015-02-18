def get_model():
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_0_pre6/src/UHH2/ZprimeAllHadronic/python/theta.root', include_mc_uncertainties = True)#mc uncertainties=true
    model.fill_histogram_zerobins()
    model.set_signal_processes('zp*')
    model.add_lognormal_uncertainty('ttbar_rate', 0.15, 'ttbar')
    model.add_lognormal_uncertainty('qcd_rate', 0.15, 'qcd')
    model.add_lognormal_uncertainty('signal1000_rate', 0.15, 'zp1000')
    model.add_lognormal_uncertainty('signal2000_rate', 0.15, 'zp2000')
    model.add_lognormal_uncertainty('signal3000_rate', 0.15, 'zp3000')
    for p in model.processes:
        if p == 'qcd': continue
        model.add_lognormal_uncertainty('lumi', 0.026, p)
    return model
model = get_model()
model_summary(model)
plot_exp, plot_obs = bayesian_limits(model,what='expected')#bayesian
plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_0_pre6/src/UHH2/ZprimeAllHadronic/python/limits.txt')
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_4_0_pre6/src/UHH2/ZprimeAllHadronic/python/htmlout_limit2')