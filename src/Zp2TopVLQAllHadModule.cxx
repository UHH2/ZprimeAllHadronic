#include <iostream>
#include <memory>

#include "UHH2/core/include/AnalysisModule.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/common/include/CleaningModules.h"
#include "UHH2/common/include/ElectronHists.h"
#include "UHH2/ZprimeAllHadronic/include/Zp2TopVLQAllHadSelections.h"
#include "UHH2/ZprimeAllHadronic/include/Zp2TopVLQAllHadHists.h"
#include "UHH2/common/include/JetCorrections.h"

using namespace std;
using namespace uhh2;

/** \brief Basic analysis example of an AnalysisModule (formerly 'cycle') in UHH2
 * 
 * This is the central class which calls other AnalysisModules, Hists or Selection classes.
 * This AnalysisModule, in turn, is called (via AnalysisModuleRunner) by SFrame.
 */
class Zp2TopVLQAllHadModule: public AnalysisModule {
public:
    
    explicit Zp2TopVLQAllHadModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    
    //std::unique_ptr<JetCleaner> jetcleaner;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
    // declare the Selections to use. Use unique_ptr to ensure automatic call of delete in the destructor,
    // to avoid memory leaks.
    //std::unique_ptr<Selection> njet_sel, bsel;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_nocuts, h_mistag, h_background,h_selection,h_selection0,h_selection1,h_selection2,h_background0,h_background1,h_background2;//, h_njet, h_bsel, h_ele;
};


Zp2TopVLQAllHadModule::Zp2TopVLQAllHadModule(Context & ctx){
    // In the constructor, the typical tasks are to create
    // other modules like cleaners (1), selections (2) and Hist classes (3).
    // But you can do more and e.g. access the configuration, as shown below.
    
    //cout << "Hello World from Zp2TopVLQAllHadModule!" << endl;
    
    // If needed, access the configuration of the module here, e.g.:
    //string testvalue = ctx.get("TestKey", "<not set>");
    //cout << "TestKey in the configuration was: " << testvalue << endl;
    
    // If running in SFrame, the keys "dataset_version", "dataset_type" and "dataset_lumi"
    // are set to the according values in the xml file. For CMSSW, these are
    // not set automatically, but can be set in the python config file.
    //for(auto & kv : ctx.get_all()){
    //    cout << " " << kv.first << " = " << kv.second << endl;
    //}
    
    // 1. setup other modules. Here, only the jet cleaner
    //jetcleaner.reset(new JetCleaner(30.0, 2.4));
    subjetcorrector.reset(new SubJetCorrector(JERFiles::PHYS14_L123_MC));
    // 2. set up selections:
    //njet_sel.reset(new NJetSelection(2));
    //bsel.reset(new NBTagSelection(1));

    // 3. Set up Hists classes:
    h_nocuts.reset(new Zp2TopVLQAllHadHists(ctx, "NoCuts"));
    h_selection.reset(new Zp2TopVLQAllHadHists(ctx, "Selection"));
    h_selection0.reset(new Zp2TopVLQAllHadHists(ctx, "Selection0"));
    h_selection1.reset(new Zp2TopVLQAllHadHists(ctx, "Selection1"));
    h_selection2.reset(new Zp2TopVLQAllHadHists(ctx, "Selection2"));
    h_mistag.reset(new MistagAndShapeHists(ctx, "Mistag"));
    h_background.reset(new BackgroundHists(ctx, "Background"));
    h_background0.reset(new BackgroundHists(ctx, "Background0"));
    h_background1.reset(new BackgroundHists(ctx, "Background1"));
    h_background2.reset(new BackgroundHists(ctx, "Background2"));
    //h_njet.reset(new Zp2TopVLQAllHadHists(ctx, "Njet"));
    //h_bsel.reset(new Zp2TopVLQAllHadHists(ctx, "Bsel"));
    //h_ele.reset(new ElectronHists(ctx, "ele_nocuts"));
}


bool Zp2TopVLQAllHadModule::process(Event & event) {
    // This is the main procedure, called for each event. Typically,
    // do some pre-processing by calling the modules' process method
    // of the modules constructed in the constructor (1).
    // Then, test whether the event passes some selection and -- if yes --
    // use it to fill the histograms (2).
    // Finally, decide whether or not to keep the event in the output (3);
    // this is controlled by the return value of this method: If it
    // returns true, the event is kept; if it returns false, the event
    // is thrown away.
    
    //cout << "Zp2TopVLQAllHadModule: Starting to process event (runid, eventid) = (" << event.run << ", " << event.event << "); weight = " << event.weight << endl;
    
    // 1. run all modules; here: only jet cleaning.
    //jetcleaner->process(event);
    subjetcorrector->process(event);
    // 2. test selections and fill histograms
    
    int nbtag = 0;
    if (event.topjets->size()>0)
    {
        if (getMaxCSV(event.topjets->at(0))>0.814)
        {
            nbtag++;
        }
    }
    if (event.topjets->size()>1)
    {
        if (getMaxCSV(event.topjets->at(1))>0.814)
        {
            nbtag++;
        }
    } 

    h_nocuts->fill(event);
    if (TopTag(event.topjets->at(0))&&TopTag(event.topjets->at(1)) && (deltaY(event.topjets->at(0),event.topjets->at(1))<1.0))
    {
        h_selection->fill(event);
        if (nbtag==0) h_selection0->fill(event);
        if (nbtag==1) h_selection1->fill(event);
        if (nbtag==2) h_selection2->fill(event);
    }
    h_mistag->fill(event);
    h_background->fill(event);
    if (nbtag==0) h_background0->fill(event);
    if (nbtag==1) h_background1->fill(event);
    if (nbtag==2) h_background2->fill(event);
    
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
    return true;//njet_selection && bjet_selection;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the Zp2TopVLQAllHadModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(Zp2TopVLQAllHadModule)
