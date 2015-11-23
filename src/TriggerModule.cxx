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
    


    unique_ptr<AnalysisModule> common_modules_with_lumi_sel;

    std::unique_ptr<Hists> h_nocuts, 
                           h_sel0, h_sel1, h_sel2,
                           h_den_mu0, h_den_mu1, h_den_mu2,
                           h_den_ht0, h_den_ht1, h_den_ht2,
                           h_num_mu0, h_num_mu1, h_num_mu2,
                           h_num_ht0, h_num_ht1, h_num_ht2;
};


TriggerModule::TriggerModule(Context & ctx){
    
    h_nocuts.reset(new TriggerHists(ctx,"nocuts"));
    h_sel0.reset(new TriggerHists(ctx,"sel0"));
    h_sel1.reset(new TriggerHists(ctx,"sel1"));
    h_sel2.reset(new TriggerHists(ctx,"sel2"));
    h_den_mu0.reset(new TriggerHists(ctx,"den_mu0"));
    h_den_mu1.reset(new TriggerHists(ctx,"den_mu1"));
    h_den_mu2.reset(new TriggerHists(ctx,"den_mu2"));
    h_den_ht0.reset(new TriggerHists(ctx,"den_ht0"));
    h_den_ht1.reset(new TriggerHists(ctx,"den_ht1"));
    h_den_ht2.reset(new TriggerHists(ctx,"den_ht2"));
    h_num_mu0.reset(new TriggerHists(ctx,"num_mu0"));
    h_num_mu1.reset(new TriggerHists(ctx,"num_mu1"));
    h_num_mu2.reset(new TriggerHists(ctx,"num_mu2"));
    h_num_ht0.reset(new TriggerHists(ctx,"num_ht0"));
    h_num_ht1.reset(new TriggerHists(ctx,"num_ht1"));
    h_num_ht2.reset(new TriggerHists(ctx,"num_ht2"));

    CommonModules* commonObjectCleaning = new CommonModules();
    commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
    //commonObjectCleaning->set_electron_id(AndId<Electron>(ElectronID_Spring15_25ns_medium_noIso,PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->set_muon_id(AndId<Muon>(MuonIDTight(),PtEtaCut(20.0, 2.1)));
    commonObjectCleaning->switch_jetlepcleaner(true);
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

uhh2::Event::TriggerIndex ti_HT650=event.get_trigger_index("HLT_PFHT650_v*");
bool HT650_trigger = event.passes_trigger(ti_HT650);

bool sel0=false;
bool sel1=false;
bool sel2=false;

const auto topjets = event.topjets;

const TopJetId topjetID = SDTopTag(SDTopTag::WP::Mis10);
//const TopJetId topjetID = SDTopTag(SDTopTag::WP::Mis1b);

bool toptag_requirement=false;
int nbtag=0;
if (topjets->size()>1)
{
    toptag_requirement = topjetID(topjets->at(0),event)&&topjetID(topjets->at(1),event);
    if (getMaxCSV(topjets->at(0))>0.890) nbtag++;
    if (getMaxCSV(topjets->at(1))>0.890) nbtag++;
}


sel0 = toptag_requirement;
sel1 = toptag_requirement && (nbtag>0);
sel2 = toptag_requirement && (nbtag>1);

h_nocuts->fill(event);

//0
if (sel0)
{
    h_sel0->fill(event);
    if (Mu_trigger)
    {
        h_den_mu0->fill(event);
        if (HT_trigger)
        {
            h_num_mu0->fill(event);
        }
    }
    if (HT650_trigger)
    {
        h_den_ht0->fill(event);
        if (HT_trigger)
        {
            h_num_ht0->fill(event);
        }
    }
}
//1
if (sel1)
{
    h_sel1->fill(event);
    if (Mu_trigger)
    {
        h_den_mu1->fill(event);
        if (HT_trigger)
        {
            h_num_mu1->fill(event);
        }
    }
    if (HT650_trigger)
    {
        h_den_ht1->fill(event);
        if (HT_trigger)
        {
            h_num_ht1->fill(event);
        }
    }
}
//2
if (sel2)
{
    h_sel2->fill(event);
    if (Mu_trigger)
    {
        h_den_mu2->fill(event);
        if (HT_trigger)
        {
            h_num_mu2->fill(event);
        }
    }
    if (HT650_trigger)
    {
        h_den_ht2->fill(event);
        if (HT_trigger)
        {
            h_num_ht2->fill(event);
        }
    }
}

    return false;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the TriggerModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(TriggerModule)
