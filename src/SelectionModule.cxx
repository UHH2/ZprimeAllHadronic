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
#include "UHH2/common/include/JetHists.h"
#include "UHH2/common/include/MCWeight.h"

using namespace std;
using namespace uhh2;

/** \brief Basic analysis example of an AnalysisModule (formerly 'cycle') in UHH2
 * 
 * This is the central class which calls other AnalysisModules, Hists or Selection classes.
 * This AnalysisModule, in turn, is called (via AnalysisModuleRunner) by SFrame.
 */
class SelectionModule: public AnalysisModule {
public:
    
    explicit SelectionModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    

    std::unique_ptr<TopJetCorrector> topjetcorrector;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
    std::unique_ptr<JetCorrector> jetcorrector;
   
    unique_ptr<AnalysisModule> common_modules_with_lumi_sel, btagwAK4, btagwAK8;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_selection, h_selectionallhad,h_btageffAK4,h_btageffAK8;
};


SelectionModule::SelectionModule(Context & ctx){
  
    CommonModules* commonObjectCleaning = new CommonModules();
    //commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
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
        jetcorrector.reset(new JetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK4PFchs_MC));
        topjetcorrector.reset(new TopJetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK8PFchs_MC));
        subjetcorrector.reset(new SubJetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK4PFchs_MC));
    }
    else
    {
        jetcorrector.reset(new JetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK4PFchs_DATA));
        topjetcorrector.reset(new TopJetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK8PFchs_DATA));
        subjetcorrector.reset(new SubJetCorrector(ctx,JERFiles::Summer15_25ns_L123_AK4PFchs_DATA));
    }

    h_selection.reset(new SelectionHists(ctx, "Selection"));
    h_selectionallhad.reset(new SelectionHists(ctx, "SelectionAllHad"));
    h_btageffAK4.reset(new BTagMCEfficiencyHists(ctx, "BTagMCEfficiencyHistsAK4",CSVBTag::WP_MEDIUM,"jets"));
    h_btageffAK8.reset(new BTagMCEfficiencyHists(ctx, "BTagMCEfficiencyHistsAK8",CSVBTag::WP_MEDIUM,"topjets"));
    //btagwAK4.reset(new MCBTagScaleFactor(ctx, CSVBTag::WP_MEDIUM, "jets"));
    //btagwAK8.reset(new MCBTagScaleFactor(ctx, CSVBTag::WP_MEDIUM, "topjets"));
}


bool SelectionModule::process(Event & event) {

if (!common_modules_with_lumi_sel->process(event)) {
    return false;
}

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

    h_selection->fill(event);
    h_btageffAK4->fill(event);
    h_btageffAK8->fill(event);

    //btagwAK4->process(event);
    //btagwAK8->process(event);

    if (is_allhad)
    {
    h_selectionallhad->fill(event);
    }

    return false;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the SelectionModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(SelectionModule)
