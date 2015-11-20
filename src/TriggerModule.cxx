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

    unique_ptr<AnalysisModule> common_modules_with_lumi_sel;

    std::unique_ptr<Hists> h_nocuts, h_sel, h_num, h_denom, h_num2, h_denom2, h_sel2;
};


TriggerModule::TriggerModule(Context & ctx){
    

    h_nocuts.reset(new TriggerHists(ctx, "NoCuts"));
    h_sel.reset(new TriggerHists(ctx, "Sel"));
    h_sel2.reset(new TriggerHists(ctx, "Sel2"));
    h_denom.reset(new TriggerHists(ctx, "Denom"));
    h_denom2.reset(new TriggerHists(ctx, "Denom2"));
    h_num.reset(new TriggerHists(ctx, "Num"));
    h_num2.reset(new TriggerHists(ctx, "Num2"));
    // h_allhadsub.reset(new TriggerHists(ctx, "AllHadSub"));

    //h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");//, "patJetsCA8CHSprunedPacked");
    //h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");//, "patJetsCA15CHSFilteredPacked");

    CommonModules* commonObjectCleaning = new CommonModules();
    commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
    //commonObjectCleaning->set_electron_id(AndId<Electron>(ElectronID_Spring15_25ns_medium_noIso,PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->set_muon_id(AndId<Muon>(MuonIDTight(),PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->switch_jetlepcleaner(true);
    commonObjectCleaning->switch_jetPtSorter(true);
    commonObjectCleaning->init(ctx);
    common_modules_with_lumi_sel.reset(commonObjectCleaning);

    

}


bool TriggerModule::process(Event & event) {

if (!common_modules_with_lumi_sel->process(event)) {
        return false;
    }

uhh2::Event::TriggerIndex ti_Mu=event.get_trigger_index("HLT_Mu45_eta2p1_*");
bool Mu_trigger = event.passes_trigger(ti_Mu);

uhh2::Event::TriggerIndex ti_HT;
if (event.isRealData)
    ti_HT=event.get_trigger_index("HLT_PFHT800_v*");
else
    ti_HT=event.get_trigger_index("HLT_PFHT800Emu_v*");

bool HT_trigger = event.passes_trigger(ti_HT);

// uhh2::Event::TriggerIndex ti_HT650=event.get_trigger_index("HLT_PFHT650_v*");
// bool HT650_trigger = event.passes_trigger(ti_HT650);

//bool selection=false;

//const auto topjetsSD = &event.get(h_topjetsAK8);
//const auto topjetsCA15 = &event.get(h_topjetsCA15);
const auto topjets = event.topjets;

const TopJetId topjetID = SDTopTag(SDTopTag::WP::Mis10);
//const TopJetId topjetID = SDTopTag(SDTopTag::WP::Mis1b);

bool selection=false;
bool selection2=false;
if (topjets->size()>1)
    selection = topjetID(topjets->at(0),event)&&topjetID(topjets->at(1),event);
    if (selection && ( getMaxCSV(topjets->at(0))>0.890 || getMaxCSV(topjets->at(1))>0.890 )) selection2=true;

h_nocuts->fill(event);

if (selection)
{
    h_sel->fill(event);
    if (Mu_trigger)
    {
        h_denom->fill(event);
        if (HT_trigger)
        {
            h_num->fill(event);
        }
    }
    // if (HT650_trigger)
    // {
    //     h_denom2->fill(event);
    //     if (HT_trigger)
    //     {
    //         h_num2->fill(event);
    //     }
    // }
}


if (selection2 )
{
    h_sel2->fill(event);
    if (Mu_trigger)
    {
        h_denom2->fill(event);
        if (HT_trigger)
        {
            h_num2->fill(event);
        }
    }
}


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
