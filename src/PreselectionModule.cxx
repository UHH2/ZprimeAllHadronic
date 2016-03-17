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
class PreselectionModule: public AnalysisModule {
public:
    
    explicit PreselectionModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    

    std::unique_ptr<TopJetCorrector> topjetcorrector;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
    std::unique_ptr<JetCorrector> jetcorrector;
   
    unique_ptr<AnalysisModule> common_modules_with_lumi_sel;

    uhh2::Event::Handle<std::vector<TopJet> > h_fatjets;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_nocuts, h_allhad, h_nocutssub, h_allhadsub, h_pre, h_preallhad;//h_nocorr, h_nocorr_gen, h_nocuts, h_nocuts_gen, h_preselection,h_trigger,h_alttrigger,h_trieffden,h_HTtrieffnum,h_AK8trieffnum,h_selection0,h_selection1,h_selection2,h_selection,h_selection_gen,h_preselection_gen,h_ww,h_tv,h_tev;
};


PreselectionModule::PreselectionModule(Context & ctx){
    

    CommonModules* commonObjectCleaning = new CommonModules();
    commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
    //commonObjectCleaning->set_electron_id(AndId<Electron>(ElectronID_Spring15_25ns_medium_noIso,PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->set_muon_id(AndId<Muon>(MuonIDTight(),PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->switch_jetlepcleaner(true);
    //commonObjectCleaning->switch_jetPtSorter(true);
    commonObjectCleaning->disable_jersmear();
    commonObjectCleaning->init(ctx);
    common_modules_with_lumi_sel.reset(commonObjectCleaning);

    bool is_mc = ctx.get("dataset_type") == "MC";
    if (is_mc)
    {
        jetcorrector.reset(new JetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK4PFchs_MC));
        topjetcorrector.reset(new TopJetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK8PFchs_MC));
        subjetcorrector.reset(new SubJetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK4PFchs_MC));
    }
    else
    {
        jetcorrector.reset(new JetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK4PFchs_DATA));
        topjetcorrector.reset(new TopJetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK8PFchs_DATA));
        subjetcorrector.reset(new SubJetCorrector(ctx,JERFiles::Fall15_25ns_L123_AK4PFchs_DATA));
    }

    

    h_nocuts.reset(new PreselectionHists(ctx, "NoCuts"));
    h_allhad.reset(new PreselectionHists(ctx, "AllHad"));
    h_nocutssub.reset(new Zp2TopVLQAllHadHists(ctx, "NoCutsSub"));
    h_allhadsub.reset(new Zp2TopVLQAllHadHists(ctx, "AllHadSub"));
    h_pre.reset(new PreselectionHists(ctx, "Preselection"));
    h_preallhad.reset(new PreselectionHists(ctx, "PreselectionAllHad"));

    h_fatjets = ctx.get_handle<std::vector<TopJet> > ("patJetsCa15CHSJetsSoftDropPacked_daughters");
    

}


bool PreselectionModule::process(Event & event) {

if (!common_modules_with_lumi_sel->process(event)) {
    return false;
}

uhh2::Event::TriggerIndex ti_HT;
//if (event.isRealData)
ti_HT=event.get_trigger_index("HLT_PFHT800_v*");
//else
//    ti_HT=event.get_trigger_index("HLT_PFHT800Emu_v*");
bool HT_trigger = event.passes_trigger(ti_HT);

// uhh2::Event::TriggerIndex ti_subht=event.get_trigger_index("HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v*");
// bool Trim_trigger = event.passes_trigger(ti_subht);


float HT=getHT50(event);
bool HT_cut= HT>850.0;
// bool Trim_cut= HT>750.0;
//if (!(HT_trigger && HT>850.0)) return false;

std::vector<TopJet>* fatjets(0);
if(event.is_valid(h_fatjets)) fatjets = &event.get(h_fatjets);

bool condR8=false;
bool condR15=false;

// if (event.topjets->size()>1)
// {
//   cond1 = TopJetPt(event.topjets->at(0))>200.0/*400.0*/ && TopJetPt(event.topjets->at(1))>200.0 && TopJetMass(event.topjets->at(0))>60.0 && TopJetMass(event.topjets->at(1))>60.0;    
// }
// if (event.topjets->size()>0 && fatjets->size()>0)
// {
//   cond2
// }
int NgoodAK8=0;
for(auto topjet : *event.topjets)
{
  if (TopJetPt(topjet)>200.0 && TopJetMass(topjet)>60.0) NgoodAK8++;
}
condR8=NgoodAK8>1;

for(auto fatjet : *fatjets)
{
  if (TopJetPt(fatjet)>200.0 && TopJetMass(fatjet)>130.0)
  {
    for(auto topjet : *event.topjets)
    {
      if (TopJetPt(topjet)>200.0 && TopJetMass(topjet)>60.0 && deltaR(topjet,fatjet)>0.8) {condR15=true; break;}
    }
  }
  if (condR15) break;
}

//if (cond1 /*&& cond2*/) Nfatjets=true;
//cout<<HT_trigger<<Nfatjets;
bool preselection = HT_trigger && HT_cut && (condR8 || condR15); //( (HT_trigger && HT_cut) /*|| (Trim_trigger && Trim_cut) */) ;


bool is_allhad=false;
if (!event.isRealData)
{
  GenParticle the_gen_top,the_gen_tprime,the_gen_w,the_gen_b,the_gen_tw,the_gen_tb;
  bool has_gen_top=false,has_gen_tprime=false,has_gen_w=false,has_gen_b=false,has_gen_tw=false,has_gen_tb=false;
  for (auto genp : *event.genparticles)
  {
    if (abs(genp.pdgId()) == 6)
    {
      has_gen_top=true;
      auto pthe_gen_tw = genp.daughter(event.genparticles, 1);
      auto pthe_gen_tb = genp.daughter(event.genparticles, 2);
      if (pthe_gen_tw && pthe_gen_tb)
      {
        the_gen_tw=*pthe_gen_tw;
        the_gen_tb=*pthe_gen_tb;
        if(abs(the_gen_tw.pdgId()) != 24)
        {
          std::swap(the_gen_tw, the_gen_tb);
        }
        if(abs(the_gen_tw.pdgId()) == 24)
        {
          has_gen_tw=true;
        }
        if(abs(the_gen_tb.pdgId()) == 5)
        {
          has_gen_tb=true;
        }
      } 
    }
    if (abs(genp.pdgId()) == 8000001)
    {
      has_gen_tprime=true;
      auto pthe_gen_w = genp.daughter(event.genparticles, 1);
      auto pthe_gen_b = genp.daughter(event.genparticles, 2);
      if (pthe_gen_w && pthe_gen_b)
      {
        the_gen_w=*pthe_gen_w;
        the_gen_b=*pthe_gen_b;
        if(abs(the_gen_w.pdgId()) != 24)
        {
          std::swap(the_gen_w, the_gen_b);
        }
        if(abs(the_gen_w.pdgId()) == 24)
        {
          has_gen_w=true;
        }
        if(abs(the_gen_b.pdgId()) == 5)
        {
          has_gen_b=true;
        }
      } 
    }
  }
  if (has_gen_top && has_gen_tprime && has_gen_w && has_gen_b && has_gen_tw && has_gen_tb)
  {
    auto wd1 = the_gen_w.daughter(event.genparticles, 1);
    auto wd2 = the_gen_w.daughter(event.genparticles, 2);
    auto wd3 = the_gen_tw.daughter(event.genparticles, 1);
    auto wd4 = the_gen_tw.daughter(event.genparticles, 2);
    if(wd1 && wd2 && wd3 && wd4)
    {
        int lept=0;
        for(const auto & wd : {*wd1 , *wd2 , *wd3 , *wd4})
        {
            int id = abs(wd.pdgId());
            if(id == 11 || id == 13 || id == 15) ++lept;
        }
        if (lept==0) is_allhad=true;
    }
  }

}


    topjetcorrector->process(event);
    subjetcorrector->process(event);
    jetcorrector->process(event);




    h_nocuts->fill(event);
    h_nocutssub->fill(event);
    if (preselection) h_pre->fill(event);
    if (is_allhad)
    {
    h_allhad->fill(event);
    h_allhadsub->fill(event);
    if (preselection) h_preallhad->fill(event);
    }



    return preselection;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the PreselectionModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(PreselectionModule)

