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
#include "UHH2/ZprimeAllHadronic/include/Tools.h"

using namespace std;
using namespace uhh2;

/** \brief Basic analysis example of an AnalysisModule (formerly 'cycle') in UHH2
 * 
 * This is the central class which calls other AnalysisModules, Hists or Selection classes.
 * This AnalysisModule, in turn, is called (via AnalysisModuleRunner) by SFrame.
 */
class SysSelModule: public AnalysisModule {
public:
    
    explicit SysSelModule(Context & ctx);
    virtual bool process(Event & event) override;

private:
    

    std::unique_ptr<TopJetCorrector> topjetcorrector;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
    std::unique_ptr<JetCorrector> jetcorrector;
   
    unique_ptr<AnalysisModule> common_modules_with_lumi_sel;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
   
};


SysSelModule::SysSelModule(Context & ctx){
    

    CommonModules* commonObjectCleaning = new CommonModules();
    commonObjectCleaning->set_jet_id(AndId<Jet>(JetPFID(JetPFID::WP_LOOSE), PtEtaCut(30.0,2.4)));
    //commonObjectCleaning->set_electron_id(AndId<Electron>(ElectronID_Spring15_25ns_medium_noIso,PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->set_muon_id(AndId<Muon>(MuonIDTight(),PtEtaCut(20.0, 2.1)));
    //commonObjectCleaning->switch_jetlepcleaner(true);
    //commonObjectCleaning->switch_jetPtSorter(true);
    commonObjectCleaning->disable_jersmear();
    commonObjectCleaning->init(ctx,"");
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

      

}


bool SysSelModule::process(Event & event) {

if (!common_modules_with_lumi_sel->process(event)) {
    return false;
}




    topjetcorrector->process(event);
    subjetcorrector->process(event);
    jetcorrector->process(event);



  bool has_tw=false;
  bool has_twb=false;
  bool has_w=false;
  bool has_t=false;
  TopJet the_top, the_w;
  Jet the_b;



  for(auto topjet : *event.topjets)
  {
    if (TopTag(topjet))
    {
      has_t=true;
      the_top=topjet;
      break;
    }
  }
  for(auto topjet : *event.topjets)
  {
    if (WTag(topjet))
    {
      has_w=true;
      the_w=topjet;
      break;
    }
  }
  has_tw = has_t && has_w ;


  if (has_tw) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>medium_btag&&deltaR(jet,the_top)>0.8 &&deltaR(jet,the_w)>0.8 && jet.pt()>100.0)
  {
        the_b=jet; has_twb=true;
        break;
  }

    return has_twb;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the SysSelModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(SysSelModule)
