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
   
    // std::unique_ptr<GenericJetCorrector> jetAK8corrector;
    std::unique_ptr<GenericTopJetCorrector> jetAK8corrector;
    std::unique_ptr<GenericTopJetCorrector> jetCA15corrector;
    // std::unique_ptr<GenericTopJetCorrector> jetHEPcorrector;

    std::unique_ptr<GenericSubJetCorrector> subjetAK8corrector;
    std::unique_ptr<GenericSubJetCorrector> subjetCA15corrector;
    // std::unique_ptr<GenericSubJetCorrector> subjetHEPcorrector;

    // uhh2::Event::Handle<std::vector<Jet> > h_jetsAK8;
    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsAK8;
    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsCA15;
    // uhh2::Event::Handle<std::vector<TopJet> > h_topjetsHEP;

    std::vector<std::unique_ptr<GenericJetCorrector> > jet_correctors;
    std::vector<std::unique_ptr<GenericTopJetCorrector> > topjet_correctors;
    std::vector<std::unique_ptr<GenericSubJetCorrector> > subjet_correctors;
    std::vector<std::string> jet_collection_names;
    std::vector<std::string> topjet_collection_names;

    // declare the Selections to use. Use unique_ptr to ensure automatic call of delete in the destructor,
    // to avoid memory leaks.
    // std::unique_ptr<Selection> njet_sel, bsel;
    std::unique_ptr<Selection> toptag_sel;
    std::unique_ptr<Selection> toptaggroom_sel;
    std::unique_ptr<Selection> toptaghep_sel;

    //uhh2::Event::Handle<std::vector<TopJet> > h_topjetsAK8;
    //uhh2::Event::Handle<std::vector<TopJet> > h_topjetsCA15;
    
    // store the Hists collection as member variables. Again, use unique_ptr to avoid memory leaks.
    std::unique_ptr<Hists> h_nocorr, h_nocorr_gen, h_nocuts, h_nocuts_gen, h_preselection,h_trigger,h_alttrigger,h_trieffden,h_HTtrieffnum,h_AK8trieffnum,h_selection0,h_selection1,h_selection2,h_selection,h_selection_gen,h_preselection_gen,h_ww,h_tv,h_tev;
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
    // for(auto & kv : ctx.get_all()){
    //     cout << " " << kv.first << " = " << kv.second << endl;
    // }
    // h_jetsAK8 = ctx.declare_event_input<std::vector<Jet> >("patJetsCa8CHSJets");//, "slimmedJetsAK8");
    // h_topjetsCA8 = ctx.declare_event_input<std::vector<TopJet> >("patJetsCa8CHSJetsPrunedPacked");//, "patJetsCA8CHSprunedPacked");
    // h_topjetsCA15 = ctx.declare_event_input<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked");//, "patJetsCA15CHSFilteredPacked");
    // h_topjetsHEP = ctx.declare_event_input<std::vector<TopJet> >("patJetsHepTopTagCHSPacked");//, "patJetsHEPTopTagCHSPacked");

    // h_jetsAK8 = ctx.declare_event_output<std::vector<Jet> >("patJetsCa8CHSJets");//, "slimmedJetsAK8");
    // h_topjetsCA8 = ctx.declare_event_output<std::vector<TopJet> >("patJetsCa8CHSJetsPrunedPacked");//, "patJetsCA8CHSprunedPacked");
    // h_topjetsCA15 = ctx.declare_event_output<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked");//, "patJetsCA15CHSFilteredPacked");
    // h_topjetsHEP = ctx.declare_event_output<std::vector<TopJet> >("patJetsHepTopTagCHSPacked");//, "patJetsHEPTopTagCHSPacked");
    // 1. setup other modules. Here, only the jet cleaner
    jetcleaner.reset(new JetCleaner(30.0, 2.4));
    jetcorrector.reset(new JetCorrector(JERFiles::PHYS14_L123_MC));
    topjetcorrector.reset(new TopJetCorrector(JERFiles::PHYS14_L123_AK8PFchs_MC));
    subjetcorrector.reset(new SubJetCorrector(JERFiles::PHYS14_L123_MC));

    //jetAK8corrector.reset(new GenericJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,"patJetsCa8CHSJets"));
    jetAK8corrector.reset(new GenericTopJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,"patJetsAk8CHSJetsSoftDropPacked_daughters"));
    jetCA15corrector.reset(new GenericTopJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,"patJetsCa15CHSJetsFilteredPacked_daughters"));
    // jetHEPcorrector.reset(new GenericTopJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,"patJetsHepTopTagCHSPacked"));

    subjetAK8corrector.reset(new GenericSubJetCorrector(ctx,JERFiles::PHYS14_L123_MC,"patJetsAk8CHSJetsSoftDropPacked_daughters"));
    subjetCA15corrector.reset(new GenericSubJetCorrector(ctx,JERFiles::PHYS14_L123_MC,"patJetsCa15CHSJetsFilteredPacked_daughters"));
    // subjetHEPcorrector.reset(new GenericSubJetCorrector(ctx,JERFiles::PHYS14_L123_MC,"patJetsHepTopTagCHSPacked"));
    
    // 2. set up selections:
    // njet_sel.reset(new NJetSelection(2));
    // bsel.reset(new NBTagSelection(1));
    const TopJetId topjetID = CMSTopTag();
    const TopJetId topjetIDgroom = CMSTopTag(CMSTopTag::MassType::groomed);
    const TopJetId topjetIDhep = HEPTopTag();
    toptag_sel.reset(new NTopJetSelection(1,-1,topjetID));
    toptaggroom_sel.reset(new NTopJetSelection(1,-1,topjetIDgroom));
    toptaghep_sel.reset(new NTopJetSelection(1,-1,topjetIDhep));

    // 3. Set up Hists classes:
    h_nocorr.reset(new Zp2TopVLQAllHadHists(ctx, "NoCorr"));
    h_nocorr_gen.reset(new Zp2TopVLQAllHadHists(ctx, "NoCorrGen"));
    h_nocuts.reset(new Zp2TopVLQAllHadHists(ctx, "NoCuts"));
    h_nocuts_gen.reset(new Zp2TopVLQAllHadHists(ctx, "NoCutsGen"));
    h_preselection.reset(new Zp2TopVLQAllHadHists(ctx, "Preselection"));
    h_preselection_gen.reset(new Zp2TopVLQAllHadHists(ctx, "PreselectionGen"));
    h_trigger.reset(new Zp2TopVLQAllHadHists(ctx, "Trigger"));
    h_alttrigger.reset(new Zp2TopVLQAllHadHists(ctx, "altTrigger"));
    h_HTtrieffnum.reset(new Zp2TopVLQAllHadHists(ctx, "HTtrieffnum"));
    h_AK8trieffnum.reset(new Zp2TopVLQAllHadHists(ctx, "AK8trieffnum"));
    h_trieffden.reset(new Zp2TopVLQAllHadHists(ctx, "trieffden"));
    h_selection0.reset(new Zp2TopVLQAllHadHists(ctx, "Selection0"));
    h_selection1.reset(new Zp2TopVLQAllHadHists(ctx, "Selection1"));
    h_selection2.reset(new Zp2TopVLQAllHadHists(ctx, "Selection2"));
    h_selection.reset(new Zp2TopVLQAllHadHists(ctx, "Selection"));
    h_selection_gen.reset(new Zp2TopVLQAllHadHists(ctx, "SelectionGen"));
    h_ww.reset(new Zp2TopVLQAllHadHists(ctx, "ww"));
    h_tev.reset(new Zp2TopVLQAllHadHists(ctx, "tev"));
    h_tv.reset(new Zp2TopVLQAllHadHists(ctx, "tv"));

    h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");//, "patJetsCA8CHSprunedPacked");
    h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");//, "patJetsCA15CHSFilteredPacked");

    // h_njet.reset(new Zp2TopVLQAllHadHists(ctx, "Njet"));
    // h_bsel.reset(new Zp2TopVLQAllHadHists(ctx, "Bsel"));
    // h_ele.reset(new ElectronHists(ctx, "ele_nocuts"));
    // topjet_collection_names = {"patJetsHepTopTagCHSPacked", "patJetsCa8CHSJetsPrunedPacked", "patJetsCa15CHSJetsFilteredPacked", "patJetsHepTopTagPuppiPacked", "patJetsCmsTopTagPuppiPacked", "patJetsCa8PuppiJetsPrunedPacked", "patJetsCa15PuppiJetsFilteredPacked", "patJetsCa8CHSJetsSoftDropPacked", "patJetsCa8PuppiJetsSoftDropPacked"};//"patJetsCmsTopTagCHSPacked",
    // jet_collection_names = {"patJetsCa15CHSJets", "patJetsCa8CHSJets", "patJetsCa15PuppiJets", "patJetsCa8PuppiJets"};
    // for(auto collection_name : jet_collection_names)
    // {
    //     jet_correctors.push_back(std::unique_ptr<GenericJetCorrector>(new GenericJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,collection_name)));
    // }
    // for(auto collection_name : topjet_collection_names)
    // {
    //     topjet_correctors.push_back(std::unique_ptr<GenericTopJetCorrector>(new GenericTopJetCorrector(ctx,JERFiles::PHYS14_L123_AK8PFchs_MC,collection_name)));
    //     subjet_correctors.push_back(std::unique_ptr<GenericSubJetCorrector>(new GenericSubJetCorrector(ctx,JERFiles::PHYS14_L123_MC,collection_name)));
    // }
    

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

uhh2::Event::TriggerIndex ti_HT=event.get_trigger_index("HLT_PFHT800*");
bool HT_trigger = event.passes_trigger(ti_HT);
const auto topjetsAK8 = &event.get(h_topjetsAK8);
if ((!HT_trigger)||(topjetsAK8->size()<2)) return false;


bool is_allhad=false;
if (event.gentopjets){
    TTbarGen ttbargen(*event.genparticles,false);
    is_allhad = ttbargen.IsTopHadronicDecay() && ttbargen.IsAntiTopHadronicDecay();
}

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
     jetAK8corrector->process(event);
     jetCA15corrector->process(event);
    // jetHEPcorrector->process(event);

     subjetAK8corrector->process(event);
     subjetCA15corrector->process(event);
    // subjetHEPcorrector->process(event);

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
    TopJet the_top;
    bool has_the_top=false;
    for(auto topjet : *event.topjets)
    {
        if (TopTag(topjet))
        {
            the_top=topjet;
            has_the_top=true;
            break;
        }
    }
    bool has_the_w=false;
    TopJet the_w;
    if (has_the_top)
    {
        for(auto topjet : *topjetsAK8)
        {
            if (WTag(topjet)&&deltaR(topjet,the_top)>0.8)
            {
                the_w=topjet;
                has_the_w=true;
                break;
            }
        }
    }
    bool has_the_b=false;
    Jet the_b;
    if (has_the_top && has_the_w)
    {
        for(auto jet : *event.jets)
        {
            if (jet.btag_combinedSecondaryVertex()>0.8&&deltaR(jet,the_top)>0.8)
            {
                the_b=jet;
                has_the_b=true;
                break;
            }
        }
    }

    
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
