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
    
    Event::Handle<float> h_ht;
    Event::Handle<float> h_htca8;
    Event::Handle<float> h_pt1ca8;
    Event::Handle<float> h_pt2ca8;

    std::unique_ptr<TopJetCorrector> topjetcorrector;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
    std::unique_ptr<JetCorrector> jetcorrector;

    unique_ptr<AnalysisModule> common_modules_with_lumi_sel;

    std::unique_ptr<Hists> h_nocuts, 
                           h_sel0, h_sel1, h_sel2,
                           h_den_mu0, h_den_mu1, h_den_mu2,
                           h_den_ht0, h_den_ht1, h_den_ht2,
                           h_num_mu0, h_num_mu1, h_num_mu2,
                           h_num_ht0, h_num_ht1, h_num_ht2,

                           h_sel0pt, h_sel1pt, h_sel2pt,
                           h_den_mu0pt, h_den_mu1pt, h_den_mu2pt,
                           h_den_ht0pt, h_den_ht1pt, h_den_ht2pt,
                           h_num_mu0pt, h_num_mu1pt, h_num_mu2pt,
                           h_num_ht0pt, h_num_ht1pt, h_num_ht2pt,

                           h_num_mu0_subht, h_num_mu1_subht, h_num_mu2_subht,
                           h_num_ht0_subht, h_num_ht1_subht, h_num_ht2_subht,
                           h_num_mu0pt_subht, h_num_mu1pt_subht, h_num_mu2pt_subht,
                           h_num_ht0pt_subht, h_num_ht1pt_subht, h_num_ht2pt_subht,

                           h_num_mu0_subpt, h_num_mu1_subpt, h_num_mu2_subpt,
                           h_num_ht0_subpt, h_num_ht1_subpt, h_num_ht2_subpt,
                           h_num_mu0pt_subpt, h_num_mu1pt_subpt, h_num_mu2pt_subpt,
                           h_num_ht0pt_subpt, h_num_ht1pt_subpt, h_num_ht2pt_subpt;
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

    h_sel0pt.reset(new TriggerHists(ctx,"sel0pt"));
    h_sel1pt.reset(new TriggerHists(ctx,"sel1pt"));
    h_sel2pt.reset(new TriggerHists(ctx,"sel2pt"));
    h_den_mu0pt.reset(new TriggerHists(ctx,"den_mu0pt"));
    h_den_mu1pt.reset(new TriggerHists(ctx,"den_mu1pt"));
    h_den_mu2pt.reset(new TriggerHists(ctx,"den_mu2pt"));
    h_den_ht0pt.reset(new TriggerHists(ctx,"den_ht0pt"));
    h_den_ht1pt.reset(new TriggerHists(ctx,"den_ht1pt"));
    h_den_ht2pt.reset(new TriggerHists(ctx,"den_ht2pt"));
    h_num_mu0pt.reset(new TriggerHists(ctx,"num_mu0pt"));
    h_num_mu1pt.reset(new TriggerHists(ctx,"num_mu1pt"));
    h_num_mu2pt.reset(new TriggerHists(ctx,"num_mu2pt"));
    h_num_ht0pt.reset(new TriggerHists(ctx,"num_ht0pt"));
    h_num_ht1pt.reset(new TriggerHists(ctx,"num_ht1pt"));
    h_num_ht2pt.reset(new TriggerHists(ctx,"num_ht2pt"));

    h_num_mu0_subht.reset(new TriggerHists(ctx,"num_mu0_subht"));
    h_num_mu1_subht.reset(new TriggerHists(ctx,"num_mu1_subht"));
    h_num_mu2_subht.reset(new TriggerHists(ctx,"num_mu2_subht"));
    h_num_ht0_subht.reset(new TriggerHists(ctx,"num_ht0_subht"));
    h_num_ht1_subht.reset(new TriggerHists(ctx,"num_ht1_subht"));
    h_num_ht2_subht.reset(new TriggerHists(ctx,"num_ht2_subht"));
    h_num_mu0pt_subht.reset(new TriggerHists(ctx,"num_mu0pt_subht"));
    h_num_mu1pt_subht.reset(new TriggerHists(ctx,"num_mu1pt_subht"));
    h_num_mu2pt_subht.reset(new TriggerHists(ctx,"num_mu2pt_subht"));
    h_num_ht0pt_subht.reset(new TriggerHists(ctx,"num_ht0pt_subht"));
    h_num_ht1pt_subht.reset(new TriggerHists(ctx,"num_ht1pt_subht"));
    h_num_ht2pt_subht.reset(new TriggerHists(ctx,"num_ht2pt_subht"));

    h_num_mu0_subpt.reset(new TriggerHists(ctx,"num_mu0_subpt"));
    h_num_mu1_subpt.reset(new TriggerHists(ctx,"num_mu1_subpt"));
    h_num_mu2_subpt.reset(new TriggerHists(ctx,"num_mu2_subpt"));
    h_num_ht0_subpt.reset(new TriggerHists(ctx,"num_ht0_subpt"));
    h_num_ht1_subpt.reset(new TriggerHists(ctx,"num_ht1_subpt"));
    h_num_ht2_subpt.reset(new TriggerHists(ctx,"num_ht2_subpt"));
    h_num_mu0pt_subpt.reset(new TriggerHists(ctx,"num_mu0pt_subpt"));
    h_num_mu1pt_subpt.reset(new TriggerHists(ctx,"num_mu1pt_subpt"));
    h_num_mu2pt_subpt.reset(new TriggerHists(ctx,"num_mu2pt_subpt"));
    h_num_ht0pt_subpt.reset(new TriggerHists(ctx,"num_ht0pt_subpt"));
    h_num_ht1pt_subpt.reset(new TriggerHists(ctx,"num_ht1pt_subpt"));
    h_num_ht2pt_subpt.reset(new TriggerHists(ctx,"num_ht2pt_subpt"));

    CommonModules* commonObjectCleaning = new CommonModules();
    commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
    //commonObjectCleaning->set_electron_id(AndId<Electron>(ElectronID_Spring15_25ns_medium_noIso,PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->set_muon_id(AndId<Muon>(MuonIDTight(),PtEtaCut(20.0, 2.1)));
    commonObjectCleaning->switch_jetlepcleaner(true);
    commonObjectCleaning->switch_jetPtSorter(true);
    commonObjectCleaning->init(ctx);
    common_modules_with_lumi_sel.reset(commonObjectCleaning);


    bool is_mc = ctx.get("dataset_type") == "MC";
    if (is_mc)
    {
        jetcorrector.reset(new JetCorrector(JERFiles::Summer15_25ns_L123_AK4PFchs_MC));
        topjetcorrector.reset(new TopJetCorrector(JERFiles::Summer15_25ns_L123_AK8PFchs_MC));
        subjetcorrector.reset(new SubJetCorrector(JERFiles::Summer15_25ns_L123_AK4PFchs_MC));
    }
    else
    {
        jetcorrector.reset(new JetCorrector(JERFiles::Summer15_25ns_L123_AK4PFchs_DATA));
        topjetcorrector.reset(new TopJetCorrector(JERFiles::Summer15_25ns_L123_AK8PFchs_DATA));
        subjetcorrector.reset(new SubJetCorrector(JERFiles::Summer15_25ns_L123_AK4PFchs_DATA));
    }

    h_ht=ctx.get_handle<float>("ht");
    h_htca8=ctx.get_handle<float>("htca8");
    h_pt1ca8=ctx.get_handle<float>("pt1ca8");
    h_pt2ca8=ctx.get_handle<float>("pt2ca8");

}


bool TriggerModule::process(Event & event) {

const auto topjets = event.topjets;

if (!common_modules_with_lumi_sel->process(event)) {
        return false;
    }

topjetcorrector->process(event);
subjetcorrector->process(event);
jetcorrector->process(event);

event.set(h_ht, getHT50(event));
event.set(h_htca8, getHTCA8(event));
if (topjets->size()>0)
    event.set(h_pt1ca8, TopJetPt(topjets->at(0)));
else
    event.set(h_pt1ca8, 0);
if (topjets->size()>1)
    event.set(h_pt2ca8, TopJetPt(topjets->at(1)));
else
    event.set(h_pt2ca8, 0);


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


uhh2::Event::TriggerIndex ti_subht=event.get_trigger_index("HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v*");
bool subht_trigger = event.passes_trigger(ti_subht);

uhh2::Event::TriggerIndex ti_subpt=event.get_trigger_index("HLT_AK8PFJet360_TrimMass30_v*");
bool subpt_trigger = event.passes_trigger(ti_subpt);

// //HLT_AK8DiPFJet250_200_TrimMass30_BTagCSV0p45_v2
// //HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v3
// //HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV0p45_v2
// HLT_AK8PFHT650_TrimR0p1PT0p03Mass50_v2
// //HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v3
// HLT_AK8PFJet360_TrimMass30_v3


bool sel0=false;
bool sel1=false;
bool sel2=false;
bool sel0pt=false;
bool sel1pt=false;
bool sel2pt=false;



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

bool ptcond = false;
if (topjets->size()>1)
{
    ptcond = TopJetPt(topjets->at(0))>400 && TopJetPt(topjets->at(1))>400;
}

sel0 = toptag_requirement;
sel1 = toptag_requirement && (nbtag>0);
sel2 = toptag_requirement && (nbtag>1);
sel0pt = sel0 && ptcond;
sel1pt = sel1 && ptcond;
sel2pt = sel2 && ptcond;

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
        if (subht_trigger)
        {
            h_num_mu0_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu0_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht0->fill(event);
        if (HT_trigger)
        {
            h_num_ht0->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht0_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht0_subpt->fill(event);
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
        if (subht_trigger)
        {
            h_num_mu1_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu1_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht1->fill(event);
        if (HT_trigger)
        {
            h_num_ht1->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht1_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht1_subpt->fill(event);
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
        if (subht_trigger)
        {
            h_num_mu2_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu2_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht2->fill(event);
        if (HT_trigger)
        {
            h_num_ht2->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht2_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht2_subpt->fill(event);
        }

    }
}



//ptcut
//0
if (sel0pt)
{
    h_sel0pt->fill(event);
    if (Mu_trigger)
    {
        h_den_mu0pt->fill(event);
        if (HT_trigger)
        {
            h_num_mu0pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_mu0pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu0pt_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht0pt->fill(event);
        if (HT_trigger)
        {
            h_num_ht0pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht0pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht0pt_subpt->fill(event);
        }

    }
}
//1
if (sel1pt)
{
    h_sel1pt->fill(event);
    if (Mu_trigger)
    {
        h_den_mu1pt->fill(event);
        if (HT_trigger)
        {
            h_num_mu1pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_mu1pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu1pt_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht1pt->fill(event);
        if (HT_trigger)
        {
            h_num_ht1pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht1pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht1pt_subpt->fill(event);
        }

    }
}
//2
if (sel2pt)
{
    h_sel2pt->fill(event);
    if (Mu_trigger)
    {
        h_den_mu2pt->fill(event);
        if (HT_trigger)
        {
            h_num_mu2pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_mu2pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_mu2pt_subpt->fill(event);
        }

    }
    if (HT650_trigger)
    {
        h_den_ht2pt->fill(event);
        if (HT_trigger)
        {
            h_num_ht2pt->fill(event);
        }
        if (subht_trigger)
        {
            h_num_ht2pt_subht->fill(event);
        }
        if (subpt_trigger)
        {
            h_num_ht2pt_subpt->fill(event);
        }

    }
}





    return false;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the TriggerModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(TriggerModule)
