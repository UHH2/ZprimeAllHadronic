def get_model():
    model = build_model_from_rootfile('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/CA15combi.root', include_mc_uncertainties = True,
 histogram_filter=lambda x: ('CA15' not in x) )#mc uncertainties=true
    model.fill_histogram_zerobins()
    model.set_signal_processes('MZp*')
    model.add_lognormal_uncertainty('ttbar_rate', math.log(1.30), 'ttbar')
    model.add_lognormal_uncertainty('qcd_rate', math.log(1.30), 'qcd')
    for p in model.processes:
        #if p == 'qcd': continue
        #model.add_lognormal_uncertainty('lumi', math.log(1.027), p)
        #model.add_lognormal_uncertainty('trigger', math.log(1.03), p)
        if 'MZp' in p:
            model.add_lognormal_uncertainty(p+'_rate', math.log(1.30), p)
    return model
model = get_model()
model_summary(model)
options = Options()
options.set('main', 'n_threads', '20')
plot_exp, plot_obs = bayesian_limits(model,what='expected')#bayesian_limits ,what='expected'
# plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/limitsCA15.txt')
# report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/CA15htmlout')
plot_exp.write_txt('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/limitsNOCA15.txt')
report.write_html('/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_6_3/src/UHH2/ZprimeAllHadronic/python/NOCA15htmlout')