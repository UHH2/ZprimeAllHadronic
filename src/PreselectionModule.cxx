#include <iostream>
#include <memory>

#include "UHH2/core/include/AnalysisModule.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/common/include/CleaningModules.h"
#include "UHH2/common/include/JetCorrections.h"
#include "UHH2/common/include/ElectronHists.h"
#include "UHH2/Zp2TopVLQAllHad/include/Zp2TopVLQAllHadSelections.h"
#include "UHH2/Zp2TopVLQAllHad/include/Zp2TopVLQAllHadHists.h"
#include "UHH2/Zp2TopVLQAllHad/include/Tools.h"

using namespace std;
using namespace uhh2;

/** \brief Basic analysis example of an AnalysisModule (formerly 'cycle') in UHH2
 * 
 * This is the central class which calls other AnalysisModules, Hists or Selection classes.
 * This AnalysisModule, in turn, is called (via AnalysisModuleRunner) by SFrame.
 */
class PreselectionModule: public AnalysisModule {
public:
    
    explicit PreselectionModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    
    std::unique_ptr<JetCleaner> jetcleaner;
    std::unique_ptr<JetCorrector> jetcorrector;
   
    // declare the Selections to use. Use unique_ptr to ensure automatic call of delete in the destructor,
    // to avoid memory leaks.
    // std::unique_ptr<Selection> njet_sel, bsel;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_nocuts, h_preselection,h_trigger,h_alttrigger,h_trieffden,h_HTtrieffnum,h_AK8trieffnum,h_selection;
};


PreselectionModule::PreselectionModule(Context & ctx){
    // In the constructor, the typical tasks are to create
    // other modules like cleaners (1), selections (2) and Hist classes (3).
    // But you can do more and e.g. access the configuration, as shown below.
    
    // cout << "Hello World from PreselectionModule!" << endl;
    
    // If needed, access the configuration of the module here, e.g.:
    // string testvalue = ctx.get("TestKey", "<not set>");
    // cout << "TestKey in the configuration was: " << testvalue << endl;
    
    // If running in SFrame, the keys "dataset_version", "dataset_type" and "dataset_lumi"
    // are set to the according values in the xml file. For CMSSW, these are
    // not set automatically, but can be set in the python config file.
    for(auto & kv : ctx.get_all()){
        cout << " " << kv.first << " = " << kv.second << endl;
    }
    
    // 1. setup other modules. Here, only the jet cleaner
    jetcleaner.reset(new JetCleaner(30.0, 2.4));
    jetcorrector.reset(new JetCorrector(JERFiles::PHYS14_L123_MC));
    
    // 2. set up selections:
    // njet_sel.reset(new NJetSelection(2));
    // bsel.reset(new NBTagSelection(1));

    // 3. Set up Hists classes:
    h_nocuts.reset(new Zp2TopVLQAllHadHists(ctx, "NoCuts"));
    h_preselection.reset(new Zp2TopVLQAllHadHists(ctx, "Preselection"));
    h_trigger.reset(new Zp2TopVLQAllHadHists(ctx, "Trigger"));
    h_alttrigger.reset(new Zp2TopVLQAllHadHists(ctx, "altTrigger"));
    h_HTtrieffnum.reset(new Zp2TopVLQAllHadHists(ctx, "HTtrieffnum"));
    h_AK8trieffnum.reset(new Zp2TopVLQAllHadHists(ctx, "AK8trieffnum"));
    h_trieffden.reset(new Zp2TopVLQAllHadHists(ctx, "trieffden"));
    h_selection.reset(new Zp2TopVLQAllHadHists(ctx, "Selection"));

    // h_njet.reset(new Zp2TopVLQAllHadHists(ctx, "Njet"));
    // h_bsel.reset(new Zp2TopVLQAllHadHists(ctx, "Bsel"));
    // h_ele.reset(new ElectronHists(ctx, "ele_nocuts"));
}


bool PreselectionModule::process(Event & event) {
    // This is the main procedure, called for each event. Typically,
    // do some pre-processing by calling the modules' process method
    // of the modules constructed in the constructor (1).
    // Then, test whether the event passes some selection and -- if yes --
    // use it to fill the histograms (2).
    // Finally, decide whether or not to keep the event in the output (3);
    // this is controlled by the return value of this method: If it
    // returns true, the event is kept; if it returns false, the event
    // is thrown away.
    
    //cout << "PreselectionModule: Starting to process event (runid, eventid) = (" << event.run << ", " << event.event << "); weight = " << event.weight << endl;

    //print all trigger names    
    //for (unsigned int i=0; i<event.get_current_triggernames().size();i++)
    //cout<< event.get_current_triggernames()[i]<<"\n";
    //cout<<"\n\n\n";


    // 1. run all modules; here: only jet cleaning.
    jetcleaner->process(event);
    jetcorrector->process(event);
    
    uhh2::Event::TriggerIndex ti_HT=event.get_trigger_index("HLT_PFHT900*");
    uhh2::Event::TriggerIndex ti_AK8=event.get_trigger_index("HLT_AK8PFJet360TrimMod_Mass30*");
    bool HT_trigger = event.passes_trigger(ti_HT);
    bool AK8_trigger = event.passes_trigger(ti_AK8);
    bool HT_cut = getHT50(event)>950.0;
    bool AK8_cut = getMaxTopJetPt(event)>400.0 && getMaxTopJetMass(event)>35.0;
    bool DiTopjet_condition = false;
    if (event.topjets->size()>1)
    {
        if ((TopJetPt(event.topjets->at(0))>400) && (TopJetPt(event.topjets->at(1))>400))
        {
            DiTopjet_condition=true;
        }
    }
    bool preselection = (((HT_trigger && HT_cut) || (AK8_trigger && AK8_cut)) && (DiTopjet_condition));
    bool trigger_selection = ((HT_trigger && HT_cut) || (AK8_trigger && AK8_cut));
    bool alt_trigger_selection = ((AK8_trigger && AK8_cut) && (!(HT_trigger && HT_cut)));
    bool selection = TopTag()
    int nbtag = 0;
    bool eff_selection =

    // bool CMScut = ;
    // bool HEPcut = ;
    // 2. test selections and fill histograms
    
    h_nocuts->fill(event);
    if (preselection)
    {
        h_preselection->fill(event);
    }
    
    // bool njet_selection = njet_sel->passes(event);
    // if(njet_selection){
    //     h_njet->fill(event);
    // }
    // bool bjet_selection = bsel->passes(event);
    // if(bjet_selection){
    //     h_bsel->fill(event);
    // }
    // h_ele->fill(event);
    
    // 3. decide whether or not to keep the current event in the output:
    return preselection;//njet_selection && bjet_selection;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the PreselectionModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(PreselectionModule)
