#include <iostream>
#include <memory>

#include "UHH2/core/include/AnalysisModule.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/common/include/CleaningModules.h"
#include "UHH2/common/include/JetCorrections.h"
#include "UHH2/common/include/ElectronHists.h"
#include "UHH2/ZprimeAllHadronic/include/Zp2TopVLQAllHadSelections.h"
#include "UHH2/ZprimeAllHadronic/include/Zp2TopVLQAllHadHists.h"
#include "UHH2/ZprimeAllHadronic/include/Tools.h"
#include "UHH2/common/include/TTbarGen.h"
#include "UHH2/common/include/TopJetIds.h"
#include "UHH2/common/include/NSelections.h"
#include "UHH2/common/include/CommonModules.h"

using namespace std;
using namespace uhh2;

/** \brief Basic analysis example of an AnalysisModule (formerly 'cycle') in UHH2
 * 
 * This is the central class which calls other AnalysisModules, Hists or Selection classes.
 * This AnalysisModule, in turn, is called (via AnalysisModuleRunner) by SFrame.
 */
class TriggerModule: public AnalysisModule {
public:
    
    explicit TriggerModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    

    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsAK8;
    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsCA15;

    std::unique_ptr<CommonModules> common;

    std::unique_ptr<Hists> h_nocuts, h_num, h_denom;
};


TriggerModule::TriggerModule(Context & ctx){
    

    h_nocuts.reset(new TriggerHists(ctx, "NoCuts"));
    h_denom.reset(new TriggerHists(ctx, "Denom"));
    h_num.reset(new TriggerHists(ctx, "Num"));
    // h_allhadsub.reset(new TriggerHists(ctx, "AllHadSub"));

    h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");//, "patJetsCA8CHSprunedPacked");
    h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");//, "patJetsCA15CHSFilteredPacked");

    common.reset(new CommonModules());
    common->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,7.0)));
    common->switch_jetPtSorter(true);
    common->init(ctx);

    

}


bool TriggerModule::process(Event & event) {


// uhh2::Event::TriggerIndex ti_Mu=event.get_trigger_index("HLT_Mu45_eta2p1_*");
// bool Mu_trigger = event.passes_trigger(ti_Mu);

// uhh2::Event::TriggerIndex ti_HT=event.get_trigger_index("HLT_PFHT800*");
// bool HT_trigger = event.passes_trigger(ti_HT);

//bool selection=false;

const TopJetId topjetID = CMSTopTag();
//topjetID(,event)

if (event.topjets->size()>1)
{
cout<<topjetID(event.topjets->at(0),event);
}

h_nocuts->fill(event);
// if (Mu_trigger)
// {

// }
//h_nocutssub->fill(event);
//if (is_allhad)
//{
//h_allhad->fill(event);
//h_allhadsub->fill(event);
//}



    return true;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the TriggerModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(TriggerModule)
