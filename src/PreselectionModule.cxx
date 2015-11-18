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
    std::unique_ptr<TopJetCorrector> topjetcorrector;
    std::unique_ptr<SubJetCorrector> subjetcorrector;
   
    
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_nocuts, h_allhad, h_nocutssub, h_allhadsub;//h_nocorr, h_nocorr_gen, h_nocuts, h_nocuts_gen, h_preselection,h_trigger,h_alttrigger,h_trieffden,h_HTtrieffnum,h_AK8trieffnum,h_selection0,h_selection1,h_selection2,h_selection,h_selection_gen,h_preselection_gen,h_ww,h_tv,h_tev;
};


PreselectionModule::PreselectionModule(Context & ctx){
    
    jetcleaner.reset(new JetCleaner(30.0, 2.4));
    jetcorrector.reset(new JetCorrector(JERFiles::PHYS14_L123_MC));
    topjetcorrector.reset(new TopJetCorrector(JERFiles::PHYS14_L123_AK8PFchs_MC));
    subjetcorrector.reset(new SubJetCorrector(JERFiles::PHYS14_L123_MC));

    

    h_nocuts.reset(new SelectionHists(ctx, "NoCuts"));
    h_allhad.reset(new SelectionHists(ctx, "AllHad"));
    h_nocutssub.reset(new Zp2TopVLQAllHadHists(ctx, "NoCutsSub"));
    h_allhadsub.reset(new Zp2TopVLQAllHadHists(ctx, "AllHadSub"));


    

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
    // for (unsigned int i=0; i<event.get_current_triggernames().size();i++)
    // cout<< event.get_current_triggernames()[i]<<"\n";
    // cout<<"\n\n\n";

//uhh2::Event::TriggerIndex ti_HT=event.get_trigger_index("HLT_PFHT900*");
//bool HT_trigger = event.passes_trigger(ti_HT);
//const auto topjetsAK8 = &event.get(h_topjetsAK8);
//if ((!HT_trigger)||(topjetsAK8->size()<2)) return false;
//if ((!HT_trigger)||(topjetsAK8->size()<2)) return false;
if (getHT50(event)<800.0) return false;

bool is_allhad=false;

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



// if (event.gentopjets){
//     TTbarGen ttbargen(*event.genparticles,false);
//     is_allhad = ttbargen.IsTopHadronicDecay() && ttbargen.IsAntiTopHadronicDecay();
// }

    //if (event.topjets->size()>0) cout<<event.topjets->at(0).pt()<<endl;
    //uncorrect_topjets(event);
    //if (event.topjets->size()>0) cout<<event.topjets->at(0).pt()<<endl<<endl;
    // h_nocorr->fill(event);
    // if (is_allhad) h_nocorr_gen->fill(event);

    jetcleaner->process(event);
    jetcorrector->process(event);
    topjetcorrector->process(event);
    subjetcorrector->process(event);

// jet_correctors[0]->process(event);
    // for (unsigned int i=0;)
    // for(auto & corrector : jet_correctors)
    // {
    //     corrector->process(event);
    // }
    // for(auto & corrector : topjet_correctors)
    // {
    //     corrector->process(event);
    // }
    // for(auto & corrector : subjet_correctors)
    // {
    //     corrector->process(event);
    // }
    // jetAK8corrector->process(event);
    // jetAK8corrector->process(event);
    // jetCA15corrector->process(event);
    // jetHEPcorrector->process(event);

    // subjetAK8corrector->process(event);
    // subjetCA15corrector->process(event);
    // subjetHEPcorrector->process(event);


h_nocuts->fill(event);
h_nocutssub->fill(event);
if (is_allhad)
{
h_allhad->fill(event);
h_allhadsub->fill(event);
}


    // TopJet the_top;
    // bool has_the_top=false;
    // for(auto topjet : *event.topjets)
    // {
    //     if (TopTag(topjet))
    //     {
    //         the_top=topjet;
    //         has_the_top=true;
    //         break;
    //     }
    // }
    // bool has_the_w=false;
    // TopJet the_w;
    // if (has_the_top)
    // {
    //     for(auto topjet : *topjetsAK8)
    //     {
    //         if (WTag(topjet)&&deltaR(topjet,the_top)>0.8)
    //         {
    //             the_w=topjet;
    //             has_the_w=true;
    //             break;
    //         }
    //     }
    // }
    // bool has_the_b=false;
    // Jet the_b;
    // if (has_the_top && has_the_w)
    // {
    //     for(auto jet : *event.jets)
    //     {
    //         if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8)
    //         {
    //             the_b=jet;
    //             has_the_b=true;
    //             break;
    //         }
    //     }
    // }


     //std::cout<<CMSTopTag()<<std::endl;

    
    //uhh2::Event::TriggerIndex ti_AK8=event.get_trigger_index("HLT_AK8PFJet360_TrimMass30*");

    // std::cout<< "Event" <<std::endl;
    // std::cout<< "CMS ungroomed" <<std::endl;
    // std::cout<< toptag_sel->passes(event) <<std::endl;
    // std::cout<< "CMS groomed" <<std::endl;
    // std::cout<< toptaggroom_sel->passes(event) <<std::endl;
    // std::cout<< "HEP" <<std::endl;
    // std::cout<< toptaghep_sel->passes(event) <<std::endl;
    // std::cout<<std::endl;
    //if(event.topjets->size()>0)
    //{
        //std::cout<< event.topjets->at(0).subjets()[0].v4().M()-event.topjets->at(0).subjets()[0].v4().mass() <<std::endl;
        //std::cout<<  <<std::endl;
    //}


    
    // bool AK8_trigger = event.passes_trigger(ti_AK8);
    // bool HT_cut = getHT50(event)>950.0;
    // bool AK8_cut = getMaxTopJetPt(event)>400.0 && getMaxTopJetMass(event)>35.0;
    // bool DiTopjet_condition = isDiTopjetEvent(event);
    // bool preselection = /*(((HT_trigger && HT_cut) || (AK8_trigger && AK8_cut)) &&*/ (DiTopjet_condition)/*)*/;
    // bool trigger_selection = ((HT_trigger && HT_cut) || (AK8_trigger && AK8_cut));
    // bool alt_trigger_selection = ((AK8_trigger && AK8_cut) && (!(HT_trigger && HT_cut)));
    // bool selection = false;
    // if (DiTopjet_condition)
    //     {
    //         if (TopTag(event.topjets->at(0))&&
    //             TopTag(event.topjets->at(1))&&
    //             (fabs(deltaPhi(event.topjets->at(0),event.topjets->at(1)))>2.1)//&&
    //             //(fabs(deltaY(event.topjets->at(0),event.topjets->at(1)))<1.0)
    //                 ) {selection=true;}
    //     }
    // int nbtag = 0;
    // if (event.topjets->size()>0)
    // {
    //     if (getMaxCSV(event.topjets->at(0))>0.814)
    //     {
    //         nbtag++;
    //     }
    // }
    // if (event.topjets->size()>1)
    // {
    //     if (getMaxCSV(event.topjets->at(1))>0.814)
    //     {
    //         nbtag++;
    //     }
    // } 
    // bool eff_selection = selection && (nbtag>1);
    
    // h_nocuts->fill(event);
    // if (is_allhad) h_nocuts_gen->fill(event);
    // if (preselection)
    // {
    //     h_preselection->fill(event);
    //     if (is_allhad) h_preselection_gen->fill(event);
    // }
    
    // if (trigger_selection)
    // {
    //     h_trigger->fill(event);
    // }
    // if (alt_trigger_selection)
    // {
    //     h_alttrigger->fill(event);
    // }
    
    // if (eff_selection)
    // {
    //     h_trieffden->fill(event);
    //     if (HT_trigger)
    //     {
    //         h_HTtrieffnum->fill(event);
    //     }
    //     if (AK8_trigger)
    //     {
    //         h_AK8trieffnum->fill(event);
    //     }
    // }

    // if (preselection && selection)
    // {
    //     h_selection->fill(event);
    //     if (ZprimeMass(event.topjets->at(0),event.topjets->at(1))>2000.0) cout<<"ditopjet "<<event.run<<":"<<event.luminosityBlock<<":"<<event.event<<" "<<TopJetMass(event.topjets->at(0))<<" "<<TopJetPt(event.topjets->at(0))<<" "<<TopJetMass(event.topjets->at(1))<<" "<<TopJetPt(event.topjets->at(1))<<" "<<ZprimeMass(event.topjets->at(0),event.topjets->at(1))<<" "<<nbtag<<" "<<event.topjets->at(0).eta()<<" "<<event.topjets->at(1).eta()<<endl;
    //     if (is_allhad) h_selection_gen->fill(event);
    // }
    // if (preselection && selection && (nbtag==0))
    // {
    //     h_selection0->fill(event);    
    // }
    // if (preselection && selection && (nbtag==1))
    // {
    //     h_selection1->fill(event);    
    // }
    // if (preselection && selection && (nbtag==2))
    // {
    //     h_selection2->fill(event);    
    // }
    // const auto topjetsAK8 = &event.get(h_topjetsAK8);
    // if (topjetsAK8->size()>1)
    // {
    //     if ((TopJetPt(topjetsAK8->at(0))>200)&&
    //     (TopJetMass(topjetsAK8->at(0))>60)&&
    //     (TopJetMass(topjetsAK8->at(0))<100)&&
    //     (TopJetNsub2(topjetsAK8->at(0))<0.5)&&
    //     (TopJetPt(topjetsAK8->at(1))>200)&&
    //     (TopJetMass(topjetsAK8->at(1))>60)&&
    //     (TopJetMass(topjetsAK8->at(1))<100)&&
    //     (TopJetNsub2(topjetsAK8->at(1))<0.5)&&
    //     (fabs(deltaPhi(topjetsAK8->at(0),topjetsAK8->at(1)))>2.1))
    //     {
    //         h_ww->fill(event);
    //         if (ZprimeMass(topjetsAK8->at(0),topjetsAK8->at(1))>2000.0) cout<<"diwjet "<<event.run<<":"<<event.luminosityBlock<<":"<<event.event<<endl;
    //     }

    //     if ((TopJetPt(topjetsAK8->at(0))>200)&&
    //     (TopJetMass(topjetsAK8->at(0))>50)&&
    //     (TopJetMass(topjetsAK8->at(0))<130)&&
    //     (TopJetNsub2(topjetsAK8->at(0))<0.6)&&
    //     (TopJetPt(topjetsAK8->at(1))>200)&&
    //     (TopJetMass(topjetsAK8->at(1))>50)&&
    //     (TopJetMass(topjetsAK8->at(1))<130)&&
    //     (TopJetNsub2(topjetsAK8->at(1))<0.6)&&
    //     (fabs(deltaPhi(topjetsAK8->at(0),topjetsAK8->at(1)))>2.1))
    //     {
    //         h_tev->fill(event);
    //         if (ZprimeMass(topjetsAK8->at(0),topjetsAK8->at(1))>4000.0) cout<<"tev "<<event.run<<":"<<event.luminosityBlock<<":"<<event.event<<" "<<ZprimeMass(topjetsAK8->at(0),topjetsAK8->at(1))<<endl;
    //     }
    // }
    // if ((event.topjets->size()>1)&&(topjetsAK8->size()>1))
    // {
    //     if (((TopTag(event.topjets->at(0)))&&
    //         (TopJetPt(event.topjets->at(0))>400)&&
    //         (TopJetPt(topjetsAK8->at(1))>200)&&
    //         (TopJetMass(topjetsAK8->at(1))>60)&&
    //         (TopJetMass(topjetsAK8->at(1))<130)&&
    //         (TopJetNsub2(topjetsAK8->at(1))<0.5)&&
    //         (fabs(deltaPhi(event.topjets->at(0),topjetsAK8->at(1)))>2.1)) ||
    //         ((TopTag(event.topjets->at(1)))&&
    //         (TopJetPt(event.topjets->at(1))>400)&&
    //         (TopJetPt(topjetsAK8->at(0))>200)&&
    //         (TopJetMass(topjetsAK8->at(0))>60)&&
    //         (TopJetMass(topjetsAK8->at(0))<130)&&
    //         (TopJetNsub2(topjetsAK8->at(0))<0.5)&&
    //         (fabs(deltaPhi(event.topjets->at(1),topjetsAK8->at(0)))>2.1))

    //         )
    //     {
    //         h_tv->fill(event);
    //         if (ZprimeMass(event.topjets->at(0),topjetsAK8->at(1))>3000.0 || ZprimeMass(event.topjets->at(1),topjetsAK8->at(0))>3000.0 ) cout<<"tv "<<event.run<<":"<<event.luminosityBlock<<":"<<event.event<<endl;
    //     }
    // }
    // return preselection;
    return true;
}

// as we want to run the ExampleCycleNew directly with AnalysisModuleRunner,
// make sure the PreselectionModule is found by class name. This is ensured by this macro:
UHH2_REGISTER_ANALYSIS_MODULE(PreselectionModule)
