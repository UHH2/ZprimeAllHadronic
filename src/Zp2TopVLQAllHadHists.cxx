#include "UHH2/ZprimeAllHadronic/include/Zp2TopVLQAllHadHists.h"
#include "UHH2/core/include/Event.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TRandom3.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include <iostream>

using namespace std;
using namespace uhh2;

Zp2TopVLQAllHadHists::Zp2TopVLQAllHadHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  // book all histograms here
  // jets
//   book<TH1F>("N_jets", "N_{jets}", 20, 0, 20);  
//   book<TH1F>("eta_jet1", "#eta^{jet 1}", 40, -2.5, 2.5);
//   book<TH1F>("eta_jet2", "#eta^{jet 2}", 40, -2.5, 2.5);
//   book<TH1F>("eta_jet3", "#eta^{jet 3}", 40, -2.5, 2.5);
//   book<TH1F>("eta_jet4", "#eta^{jet 4}", 40, -2.5, 2.5);

  //n
  book<TH1F>("Nevts", ";Nevts;Events", 1, 0, 1);
  //njet ntopjet
  book<TH1F>("N_jets", ";N_{jets};Events", 20, 0, 20);
  book<TH1F>("N_jets50", ";N_{jets};Events", 20, 0, 20);
  book<TH1F>("N_topjets", ";N_{topjets};Events", 10, 0, 10);
  //mass1 mass2 mass1+2 AK8 CA8 CA15 CMS HEP
  // book<TH1F>("m1AK8", ";m_{1,AK8};Events", 2000, 0, 2000);
  // book<TH1F>("m2AK8", ";m_{2,AK8};Events", 2000, 0, 2000);
  // book<TH1F>("m12AK8", ";m_{12,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("m1AK8", ";m_{1,AK8};Events", 2000, 0, 2000);
  book<TH1F>("m2AK8", ";m_{2,AK8};Events", 2000, 0, 2000);
  book<TH1F>("m12AK8", ";m_{12,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("m1CA15", ";m_{1,CA15};Events", 2000, 0, 2000);
  book<TH1F>("m2CA15", ";m_{2,CA15};Events", 2000, 0, 2000);
  book<TH1F>("m12CA15", ";m_{12,CA15};Events", 240, 0, 6000);
  
  book<TH1F>("m1CMS", ";m_{1,CMS};Events", 2000, 0, 2000);
  book<TH1F>("m2CMS", ";m_{2,CMS};Events", 2000, 0, 2000);
  book<TH1F>("m12CMS", ";m_{12,CMS};Events", 240, 0, 6000);

  book<TH1F>("m1CMSfat", ";m_{1,CMS};Events", 2000, 0, 2000);
  book<TH1F>("m2CMSfat", ";m_{2,CMS};Events", 2000, 0, 2000);
  book<TH1F>("m12CMSfat", ";m_{12,CMS};Events", 240, 0, 6000);

  book<TH1F>("m1gen", ";m_{1,gen};Events", 2000, 0, 2000);
  book<TH1F>("m2gen", ";m_{2,gen};Events", 2000, 0, 2000);
  book<TH1F>("m12gen", ";m_{12,gen};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x3R8", ";m_{1,AK4x3R8};Events", 2000, 0, 2000);
  book<TH1F>("m2AK4x3R8", ";m_{2,AK4x3R8};Events", 2000, 0, 2000);
  book<TH1F>("m12AK4x3R8", ";m_{12,AK4x3R8};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x4R8", ";m_{1,4x4R8};Events", 2000, 0, 2000);
  book<TH1F>("m2AK4x4R8", ";m_{2,4x4R8};Events", 2000, 0, 2000);
  book<TH1F>("m12AK4x4R8", ";m_{12,AK4x4R8};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x3R15", ";m_{1,AK4x3R15};Events", 2000, 0, 2000);
  book<TH1F>("m2AK4x3R15", ";m_{2,AK4x3R15};Events", 2000, 0, 2000);
  book<TH1F>("m12AK4x3R15", ";m_{12,AK4x3R15};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x4R15", ";m_{1,AK4x4R15};Events", 2000, 0, 2000);
  book<TH1F>("m2AK4x4R15", ";m_{2,AK4x4R15};Events", 2000, 0, 2000);
  book<TH1F>("m12AK4x4R15", ";m_{12,AK4x4R15};Events", 240, 0, 6000);

  book<TH1F>("m12CMSAK8", ";m_{12,CMSAK8};Events", 240, 0, 6000);
  book<TH1F>("m12AK8CMS", ";m_{12,AK8CMS};Events", 240, 0, 6000);
  
  // book<TH1F>("m1HEP", ";m_{1,HEP};Events", 2000, 0, 2000);
  // book<TH1F>("m2HEP", ";m_{2,HEP};Events", 2000, 0, 2000);
  // book<TH1F>("m12HEP", ";m_{12,HEP};Events", 240, 0, 6000);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  // book<TH1F>("pT1AK8", ";pT_{1,AK8};Events", 2000, 0, 2000);
  // book<TH1F>("pT2AK8", ";pT_{2,AK8};Events", 2000, 0, 2000);
  // book<TH1F>("pT12AK8", ";pT_{1,AK8}+pT_{2,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("pT1AK8", ";pT_{1,AK8};Events", 2000, 0, 2000);
  book<TH1F>("pT2AK8", ";pT_{2,AK8};Events", 2000, 0, 2000);
  book<TH1F>("pT12AK8", ";pT_{1,AK8}+pT_{2,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("pT1CA15", ";pT_{1,CA15};Events", 2000, 0, 2000);
  book<TH1F>("pT2CA15", ";pT_{2,CA15};Events", 2000, 0, 2000);
  book<TH1F>("pT12CA15", ";pT_{1,CA15}+pT_{2,CA15};Events", 240, 0, 6000);
  
  book<TH1F>("pT1CMS", ";pT_{1,CMS};Events", 2000, 0, 2000);
  book<TH1F>("pT2CMS", ";pT_{2,CMS};Events", 2000, 0, 2000);
  book<TH1F>("pT12CMS", ";pT_{1,CMS}+pT_{2,CMS};Events", 240, 0, 6000);
  
  // book<TH1F>("pT1HEP", ";pT_{1,HEP};Events", 2000, 0, 2000);
  // book<TH1F>("pT2HEP", ";pT_{2,HEP};Events", 2000, 0, 2000);
  // book<TH1F>("pT12HEP", ";pT_{1,HEP}+pT_{2,HEP};Events", 240, 0, 6000);
  
  //HT50
  book<TH1F>("HT", ";HT_{50};Events", 200, 0, 10000);
  book<TH2F>("HT50vsNjet50", ";HT;N_{jets};Events", 20,0,5000,20, 0, 20);
  //deltaPhi(1,2) deltaY(1,2) eta1 eta2
  book<TH1F>("deltaPhi", ";#Delta(#phi);Events", 100, -4, 4);
  book<TH1F>("deltaY", ";#Delta(y);Events", 100, -4, 4);
  book<TH1F>("eta_1", ";#eta_{1};Events", 100, -4, 4);
  book<TH1F>("eta_2", ";#eta_{2};Events", 100, -4, 4);

  //nsub1 nsub2 CMS
  book<TH1F>("nsub_1CMS", ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  book<TH1F>("nsub_2CMS", ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //maxcsv1 maxcsv2 CMS
  book<TH1F>("csv_1CMS", ";CSV_{1};Events", 100, 0, 1.1);
  book<TH1F>("csv_2CMS", ";CSV_{2};Events", 100, 0, 1.1);

  //nsub1 nsub2 AK8
  book<TH1F>("nsub_1AK8", ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  book<TH1F>("nsub_2AK8", ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //maxcsv1 maxcsv2 AK8
  book<TH1F>("csv_1AK8", ";CSV_{1};Events", 100, 0, 1.1);
  book<TH1F>("csv_2AK8", ";CSV_{2};Events", 100, 0, 1.1);

  //nsub1 nsub2 CA15
  book<TH1F>("nsub_1CA15", ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  book<TH1F>("nsub_2CA15", ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //maxcsv1 maxcsv2 CA15
  book<TH1F>("csv_1CA15", ";CSV_{1};Events", 100, 0, 1.1);
  book<TH1F>("csv_2CA15", ";CSV_{2};Events", 100, 0, 1.1);

  //mistag matrix 2d 3d
  // double csv_bins[] = {-100.0,0.0,0.244,0.679,10.0};
  // double mistag_pt_bins[] = {150.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,360.0,380.0,400.0,450.0,500.0,600.0,800.0,2000.0};
  // double nsub_bins[] = {0.0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2};
  // book<TH2F>( "mistag2D", ";pT;CSV", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins);
  // book<TH3F>( "mistag3D", ";pT;CSV;nsub", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins,sizeof(nsub_bins)/sizeof(double)-1, nsub_bins);
  //mmin ndau
  book<TH1F>("mmin1", ";Minimum pairwise mass 1;Events", 200, 0, 100);
  book<TH1F>("ndau1", ";Number of daughters 1;Events", 6, 0, 6);
  book<TH1F>("mmin2", ";Minimum pairwise mass 2;Events", 200, 0, 100);
  book<TH1F>("ndau2", ";Number of daughters 2;Events", 6, 0, 6);
  
  //pt/pt vs pt
  book<TProfile>("ptratioVSpt", ";p_{T,gen};p_{T,reco}/p_{T,gen}", 150, 0, 1500);
  //pt/pt vs eta
  book<TProfile>("ptratioVSeta", ";#eta_{gen};p_{T,reco}/p_{T,gen}", 150, -4, 4);
  book<TProfile>("ptratioVSnpv", ";n_{pv};p_{T,reco}/p_{T,gen}", 50, 0, 50);
  //pt/pt vs pt,eta
  book<TProfile2D>("ptratioVSpteta", ";p_{T,gen};#eta_{gen};p_{T,reco}/p_{T,gen}", 15, 0, 1500, 15, -4, 4);
  //m/m vs pt
  book<TProfile>("mratioVSpt", ";p_{T,gen};m_{reco}/m_{gen}", 150, 0, 1500);
  //m/m vs eta
  book<TProfile>("mratioVSeta", ";#eta_{gen};m_{reco}/m_{gen}", 150, -4, 4);
  //m/m vs pt,eta
  book<TProfile2D>("mratioVSpteta", ";p_{T,gen};#eta_{gen};m_{reco}/m_{gen}", 15, 0, 1500, 15, -4, 4);
  //mz/mz vs pt
  book<TProfile>("mZratioVSpt", ";p_{T,gen};m_{Z',reco}/m_{Z',gen}", 150, 0, 1500);
  //mz/mz vs eta
  book<TProfile>("mZratioVSeta", ";#eta_{gen};m_{Z',reco}/m_{Z',gen}", 150, -4, 4);
  //mz/mz vs pt,eta
  book<TProfile2D>("mZratioVSpteta", ";p_{T,gen};#eta_{gen};m_{Z',reco}/m_{Z',gen}", 15, 0, 1500, 15, -4, 4);
  //mz/mz vs pt,pt
  book<TProfile2D>("mZratioVSptpt", ";p_{T1,gen};p_{T2,gen};m_{Z',reco}/m_{Z',gen}", 15, 0, 1500, 15, 0, 1500);
  book<TProfile2D>("mZratioVSetaeta", ";#eta_{1,gen};#eta_{2,gen};m_{Z',reco}/m_{Z',gen}",  15, -4, 4, 15, -4, 4);
  //eta/eta vs pt
  book<TProfile>("etaratioVSpt", ";p_{T,gen};#eta_{reco}/#eta_{gen}", 150, 0, 1500);
  //eta/eta vs eta
  book<TProfile>("etaratioVSeta", ";#eta_{gen};#eta_{reco}/#eta_{gen}", 150, -4, 4);
  //eta/eta vs pt,eta
  book<TProfile2D>("etaratioVSpteta", ";p_{T,gen};#eta_{gen};#eta_{reco}/#eta_{gen}", 15, 0, 1500, 15, -4, 4);
  //ak4
  book<TH1F>("pTAK4", ";pT;Events", 200, 0, 1000);
  book<TH1F>("etaAK4", ";eta;Events", 200, -4, 4);
  book<TProfile>("ptratioVSptAK4", ";p_{T,gen};p_{T,reco}/p_{T,gen}", 200, 0, 1000);
  book<TProfile>("ptratioVSetaAK4", ";#eta_{gen};p_{T,reco}/p_{T,gen}", 200, -4, 4);
  book<TProfile>("ptratioVSeta30AK4", ";#eta_{gen};p_{T,reco}/p_{T,gen}", 50, -4, 4);
  book<TProfile>("ptratioVSnpvAK4", ";n_{pv};p_{T,reco}/p_{T,gen}", 50, 0, 50);
  //<(eta,reco-eta,gen)*sign(eta,gen)> vs eta,gen for e.g. 30<pTgen<40 GeV
  book<TProfile>("etadiffVSeta30AK4", ";#eta_{gen};(#eta_{reco}-#eta_{gen})*sign(#eta_{gen})", 50, -4, 4);

  // leptons
//   book<TH1F>("N_mu", "N^{#mu}", 10, 0, 10);
//   book<TH1F>("pt_mu", "p_{T}^{#mu} [GeV/c]", 40, 0, 200);
//   book<TH1F>("eta_mu", "#eta^{#mu}", 40, -2.1, 2.1);
//   book<TH1F>("reliso_mu", "#mu rel. Iso", 40, 0, 0.5);

  // primary vertices
  book<TH1F>("N_pv", ";N^{PV};Events", 50, 0, 50);


  //get handles ctx.get_handle<double>("HT");
  //h_jetsAK8 = ctx.get_handle<std::vector<Jet> >("patJetsCa8CHSJets");//, "slimmedJetsAK8");
  //h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");//, "patJetsCA8CHSprunedPacked");
  //h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");//, "patJetsCA15CHSFilteredPacked");
  //h_topjetsHEP = ctx.get_handle<std::vector<TopJet> >("patJetsHepTopTagCHSPacked");//, "patJetsHEPTopTagCHSPacked");

  //topjet_collection_names = {"patJetsHepTopTagCHSPacked", "patJetsCa8CHSJetsPrunedPacked", "patJetsCa15CHSJetsFilteredPacked", "patJetsHepTopTagPuppiPacked", "patJetsCmsTopTagPuppiPacked", "patJetsCa8PuppiJetsPrunedPacked", "patJetsCa15PuppiJetsFilteredPacked", "patJetsCa8CHSJetsSoftDropPacked", "patJetsCa8PuppiJetsSoftDropPacked"};//"patJetsCmsTopTagCHSPacked",
  // //jet_collection_names = {"patJetsCa15CHSJets", "patJetsCa8CHSJets", "patJetsCa15PuppiJets", "patJetsCa8PuppiJets"};
  // for(auto collection_name : jet_collection_names)
  // {
  //   jet_handles.push_back(ctx.get_handle<std::vector<Jet> >(collection_name));
  // }
  // for(auto collection_name : topjet_collection_names)
  // {
  //   topjet_handles.push_back(ctx.get_handle<std::vector<TopJet> >(collection_name));
  // }

  // for(auto collection_name : jet_collection_names)
  // {
  //   book<TH1F>("N_"+collection_name, ";N_{topjets};Events", 10, 0, 10);
  //   book<TH1F>("m1_"+collection_name, ";m_{1};Events", 2000, 0, 2000);
  //   book<TH1F>("m2_"+collection_name, ";m_{2};Events", 2000, 0, 2000);
  //   book<TH1F>("m12_"+collection_name, ";m_{12};Events", 240, 0, 6000);
  //   book<TH1F>("pT1_"+collection_name, ";pT_{1};Events", 2000, 0, 2000);
  //   book<TH1F>("pT2_"+collection_name, ";pT_{2};Events", 2000, 0, 2000);
  //   // book<TH1F>("nsub1_"+collection_name, ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  //   // book<TH1F>("nsub2_"+collection_name, ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //   book<TH1F>("csv1_"+collection_name, ";CSV_{1};Events", 100, 0, 1.1);
  //   book<TH1F>("csv2_"+collection_name, ";CSV_{2};Events", 100, 0, 1.1);
  // }

  // for(auto collection_name : topjet_collection_names)
  // {
  //   book<TH1F>("N_"+collection_name, ";N_{topjets};Events", 10, 0, 10);
  //   book<TH1F>("m1_"+collection_name, ";m_{1};Events", 2000, 0, 2000);
  //   book<TH1F>("m2_"+collection_name, ";m_{2};Events", 2000, 0, 2000);
  //   book<TH1F>("m12_"+collection_name, ";m_{12};Events", 240, 0, 6000);
  //   book<TH1F>("pT1_"+collection_name, ";pT_{1};Events", 2000, 0, 2000);
  //   book<TH1F>("pT2_"+collection_name, ";pT_{2};Events", 2000, 0, 2000);
  //   book<TH1F>("nsub1_"+collection_name, ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  //   book<TH1F>("nsub2_"+collection_name, ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //   book<TH1F>("csv1_"+collection_name, ";CSV_{1};Events", 100, 0, 1.1);
  //   book<TH1F>("csv2_"+collection_name, ";CSV_{2};Events", 100, 0, 1.1);
  // }

}


void Zp2TopVLQAllHadHists::fill(const Event & event){
  // fill the histograms. Please note the comments in the header file:
  // 'hist' is used here a lot for simplicity, but it will be rather
  // slow when you have many histograms; therefore, better
  // use histogram pointers as members as in 'UHH2/common/include/ElectronHists.h'
  
  // Don't forget to always use the weight when filling.
  double weight = event.weight;
  
  //get extra jet collections
  //const auto jetsAK8 = &event.get(h_jetsAK8);
  // const auto topjetsAK8 = &event.get(h_topjetsAK8);
  // const auto topjetsCA15 = &event.get(h_topjetsCA15);
  //const auto topjetsHEP = &event.get(h_topjetsHEP);

  int Npvs = event.pvs->size();
    
  //n
  hist("Nevts")->Fill(0.5,weight);
  //njet ntopjet
  hist("N_jets")->Fill(event.jets->size(),weight);
  int njet50=0;
  for (auto jet : *event.jets) if (jet.pt()>40.0) njet50++;
  hist("N_jets50")->Fill(njet50,weight);
  hist("N_topjets")->Fill(event.topjets->size(),weight);
  //mass1 mass2 mass1+2 AK8 CA8 CA15 CMS HEP
  // if (jetsAK8->size()>0) if (jetsAK8->at(0).v4().isTimelike()) hist("m1AK8")->Fill(jetsAK8->at(0).v4().M(),weight);
  // if (jetsAK8->size()>1) if (jetsAK8->at(1).v4().isTimelike()) hist("m2AK8")->Fill(jetsAK8->at(1).v4().M(),weight);
  // if (jetsAK8->size()>1) if ((jetsAK8->at(0).v4()+jetsAK8->at(1).v4()).isTimelike()) hist("m12AK8")->Fill((jetsAK8->at(0).v4()+jetsAK8->at(1).v4()).M(),weight);
  
  // if (topjetsAK8->size()>0) hist("m1AK8")->Fill(TopJetMass(topjetsAK8->at(0)),weight);
  // if (topjetsAK8->size()>1) hist("m2AK8")->Fill(TopJetMass(topjetsAK8->at(1)),weight);
  // if (topjetsAK8->size()>1) hist("m12AK8")->Fill(ZprimeMass(topjetsAK8->at(0),topjetsAK8->at(1)),weight);
  
  // if (topjetsCA15->size()>0) hist("m1CA15")->Fill(TopJetMass(topjetsCA15->at(0)),weight);
  // if (topjetsCA15->size()>1) hist("m2CA15")->Fill(TopJetMass(topjetsCA15->at(1)),weight);
  // if (topjetsCA15->size()>1) hist("m12CA15")->Fill(ZprimeMass(topjetsCA15->at(0),topjetsCA15->at(1)),weight);
  
  if (event.topjets->size()>0)
  {
    hist("m1CMS")->Fill(TopJetMass(event.topjets->at(0)),weight);
    hist("m1CMSfat")->Fill(TopJetMass2(event.topjets->at(0)),weight);
    hist("m1AK4x3R8")->Fill(TopJetMassAK4(event,event.topjets->at(0),3,0.8),weight);
    hist("m1AK4x4R8")->Fill(TopJetMassAK4(event,event.topjets->at(0),4,0.8),weight);
    hist("m1AK4x3R15")->Fill(TopJetMassAK4(event,event.topjets->at(0),3,1.5),weight);
    hist("m1AK4x4R15")->Fill(TopJetMassAK4(event,event.topjets->at(0),4,1.5),weight);
  }
  if (event.topjets->size()>1)
  {
    hist("m2CMS")->Fill(TopJetMass(event.topjets->at(1)),weight);
    hist("m2CMSfat")->Fill(TopJetMass2(event.topjets->at(1)),weight);
    hist("m2AK4x3R8")->Fill(TopJetMassAK4(event,event.topjets->at(1),3,0.8),weight);
    hist("m2AK4x4R8")->Fill(TopJetMassAK4(event,event.topjets->at(1),4,0.8),weight);
    hist("m2AK4x3R15")->Fill(TopJetMassAK4(event,event.topjets->at(1),3,1.5),weight);
    hist("m2AK4x4R15")->Fill(TopJetMassAK4(event,event.topjets->at(1),4,1.5),weight);
  }
  if (event.topjets->size()>1)
  {
    hist("m12CMS")->Fill(ZprimeMass(event.topjets->at(0),event.topjets->at(1)),weight);
    hist("m12CMSfat")->Fill(ZprimeMass2(event.topjets->at(0),event.topjets->at(1)),weight);
    hist("m12AK4x3R8")->Fill(ZprimeMassAK4(event,event.topjets->at(0),event.topjets->at(1),3,0.8),weight);
    hist("m12AK4x4R8")->Fill(ZprimeMassAK4(event,event.topjets->at(0),event.topjets->at(1),4,0.8),weight);
    hist("m12AK4x3R15")->Fill(ZprimeMassAK4(event,event.topjets->at(0),event.topjets->at(1),3,1.5),weight);
    hist("m12AK4x4R15")->Fill(ZprimeMassAK4(event,event.topjets->at(0),event.topjets->at(1),4,1.5),weight);
  }
if(event.gentopjets){
  if (event.gentopjets->size()>0) hist("m1gen")->Fill(TopJetMass2(event.gentopjets->at(0)),weight);
  if (event.gentopjets->size()>1) hist("m2gen")->Fill(TopJetMass2(event.gentopjets->at(1)),weight);
  if (event.gentopjets->size()>1) hist("m12gen")->Fill(ZprimeMass2(event.gentopjets->at(0),event.gentopjets->at(1)),weight);}

// if(event.topjets->size()>1 && topjetsAK8->size()>1)
// {
//   hist("m12CMSAK8")->Fill(ZprimeMass(event.topjets->at(0),topjetsAK8->at(1)),weight);
//   hist("m12AK8CMS")->Fill(ZprimeMass(event.topjets->at(1),topjetsAK8->at(0)),weight);
// }
  // if (topjetsHEP->size()>0) hist("m1HEP")->Fill(TopJetMass(topjetsHEP->at(0)),weight);
  // if (topjetsHEP->size()>1) hist("m2HEP")->Fill(TopJetMass(topjetsHEP->at(1)),weight);
  // if (topjetsHEP->size()>1) hist("m12HEP")->Fill(ZprimeMass(topjetsHEP->at(0),topjetsHEP->at(1)),weight);
  // //if (event.topjets->size()>1) hist("m12HEP")->Fill(ZprimeMass22(event.topjets->at(0),event.topjets->at(1)),weight);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  // if (jetsAK8->size()>0) hist("pT1AK8")->Fill(jetsAK8->at(0).pt(),weight);
  // if (jetsAK8->size()>1) hist("pT2AK8")->Fill(jetsAK8->at(1).pt(),weight);
  // if (jetsAK8->size()>1) hist("pT12AK8")->Fill(jetsAK8->at(0).pt()+jetsAK8->at(1).pt(),weight);
  
  // if (topjetsAK8->size()>0) hist("pT1AK8")->Fill(TopJetPt(topjetsAK8->at(0)),weight);
  // if (topjetsAK8->size()>1) hist("pT2AK8")->Fill(TopJetPt(topjetsAK8->at(1)),weight);
  // if (topjetsAK8->size()>1) hist("pT12AK8")->Fill(TopJetPt(topjetsAK8->at(0))+TopJetPt(topjetsAK8->at(1)),weight);
  
  // if (topjetsCA15->size()>0) hist("pT1CA15")->Fill(TopJetPt(topjetsCA15->at(0)),weight);
  // if (topjetsCA15->size()>1) hist("pT2CA15")->Fill(TopJetPt(topjetsCA15->at(1)),weight);
  // if (topjetsCA15->size()>1) hist("pT12CA15")->Fill(TopJetPt(topjetsCA15->at(0))+TopJetPt(topjetsCA15->at(1)),weight);
  
  if (event.topjets->size()>0) hist("pT1CMS")->Fill(TopJetPt(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("pT2CMS")->Fill(TopJetPt(event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("pT12CMS")->Fill(TopJetPt(event.topjets->at(0))+TopJetPt(event.topjets->at(1)),weight);
  
  // if (topjetsHEP->size()>0) hist("pT1HEP")->Fill(TopJetPt(topjetsHEP->at(0)),weight);
  // if (topjetsHEP->size()>1) hist("pT2HEP")->Fill(TopJetPt(topjetsHEP->at(1)),weight);
  // if (topjetsHEP->size()>1) hist("pT12HEP")->Fill(TopJetPt(topjetsHEP->at(0))+TopJetPt(topjetsHEP->at(1)),weight);
  
  //HT50
  double HT50=getHT50(event);
  hist("HT")->Fill(HT50,weight);
  ((TH2F*)hist("HT50vsNjet50"))->Fill(HT50,njet50,weight);
  //deltaPhi(1,2)->Fill(,weight); deltaY(1,2)->Fill(,weight); eta1 eta2
  if (event.topjets->size()>1) hist("deltaPhi")->Fill(deltaPhi(event.topjets->at(0),event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("deltaY")->Fill(deltaY(event.topjets->at(0),event.topjets->at(1)),weight);
  if (event.topjets->size()>0) hist("eta_1")->Fill(event.topjets->at(0).eta(),weight);
  if (event.topjets->size()>1) hist("eta_2")->Fill(event.topjets->at(1).eta(),weight);

  //nsub1 nsub2 CMS
  if (event.topjets->size()>0) hist("nsub_1CMS")->Fill(TopJetNsub(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("nsub_2CMS")->Fill(TopJetNsub(event.topjets->at(1)),weight);
  //maxcsv1 maxcsv2 CMS
  if (event.topjets->size()>0) hist("csv_1CMS")->Fill(getMaxCSV(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("csv_2CMS")->Fill(getMaxCSV(event.topjets->at(1)),weight);

  // //nsub1 nsub2 AK8
  // if (topjetsAK8->size()>0) hist("nsub_1AK8")->Fill(TopJetNsub(topjetsAK8->at(0)),weight);
  // if (topjetsAK8->size()>1) hist("nsub_2AK8")->Fill(TopJetNsub(topjetsAK8->at(1)),weight);
  // //maxcsv1 maxcsv2 AK8
  // if (topjetsAK8->size()>0) hist("csv_1AK8")->Fill(getMaxCSV(topjetsAK8->at(0)),weight);
  // if (topjetsAK8->size()>1) hist("csv_2AK8")->Fill(getMaxCSV(topjetsAK8->at(1)),weight);

  // //nsub1 nsub2 CA15
  // if (topjetsCA15->size()>0) hist("nsub_1CA15")->Fill(TopJetNsub(topjetsCA15->at(0)),weight);
  // if (topjetsCA15->size()>1) hist("nsub_2CA15")->Fill(TopJetNsub(topjetsCA15->at(1)),weight);
  // //maxcsv1 maxcsv2 CA15
  // if (topjetsCA15->size()>0) hist("csv_1CA15")->Fill(getMaxCSV(topjetsCA15->at(0)),weight);
  // if (topjetsCA15->size()>1) hist("csv_2CA15")->Fill(getMaxCSV(topjetsCA15->at(1)),weight);
  
  //mmin ndau
  if (event.topjets->size()>0) hist("mmin1")->Fill(getMmin(event.topjets->at(0)),weight);
  if (event.topjets->size()>0) hist("ndau1")->Fill(event.topjets->at(0).numberOfDaughters(),weight);
  if (event.topjets->size()>1) hist("mmin2")->Fill(getMmin(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("ndau2")->Fill(event.topjets->at(1).numberOfDaughters(),weight);
  
if (event.gentopjets){
  std::vector<GenTopJet> arr;
  if (event.gentopjets->size()>0) arr.push_back(event.gentopjets->at(0));
  if (event.gentopjets->size()>1) arr.push_back(event.gentopjets->at(1));
  //for(auto gen : *event.gentopjets)
  for(auto gen : arr)
  {
    //cout<<gen.pt()<<endl;
  int index=match2GenTopJet(gen,event);
  if (index>-1)
  {
    TopJet reco=event.topjets->at(index);
    float ptgen=TopJetPt(gen) ;
    float ptreco=TopJetPt(reco) ;
    float ptratio=ptreco/ptgen ;
    float mgen=TopJetMass(gen) ;
    float mreco=TopJetMass(reco) ;
    float mratio=mreco/mgen ;
    float etagen=TopJetEta(gen) ;
    float etareco=TopJetEta(reco) ;
    float etaratio=etareco/etagen ;
    //pt/pt vs pt
    ((TProfile*)hist("ptratioVSpt"))->Fill(ptgen,ptratio,weight);
    ((TProfile*)hist("ptratioVSnpv"))->Fill(Npvs,ptratio,weight);
    //pt/pt vs eta
    ((TProfile*)hist("ptratioVSeta"))->Fill(etagen,ptratio,weight);
    //pt/pt vs pt,eta
    ((TProfile2D*)hist("ptratioVSpteta"))->Fill(ptgen,etagen,ptratio,weight);
    if (mgen>0.1)
    {
      //m/m vs pt
      ((TProfile*)hist("mratioVSpt"))->Fill(ptgen,mratio,weight);
      //m/m vs eta
      ((TProfile*)hist("mratioVSeta"))->Fill(etagen,mratio,weight);
      //m/m vs pt,eta
      ((TProfile2D*)hist("mratioVSpteta"))->Fill(ptgen,etagen,mratio,weight);
  }
    //eta/eta vs pt
    ((TProfile*)hist("etaratioVSpt"))->Fill(ptgen,etaratio,weight);
    //eta/eta vs eta
    ((TProfile*)hist("etaratioVSeta"))->Fill(etagen,etaratio,weight);
    //eta/eta vs pt,eta
    ((TProfile2D*)hist("etaratioVSpteta"))->Fill(ptgen,etagen,etaratio,weight);
  }
  }
  //cout<<endl<<endl;

  for(auto gen : *event.genjets)
  {
    int index=match2GenJet(gen,event);
    if (index>-1)
    {
      Jet reco=event.jets->at(index);
      float ptgen=gen.pt() ;
      float ptreco=reco.pt() ;
      float ptratio=ptreco/ptgen ;
      float etagen=gen.eta() ;
      float etareco=reco.eta() ;
      ((TProfile*)hist("ptratioVSptAK4"))->Fill(ptgen,ptratio,weight);
      hist("pTAK4")->Fill(ptreco,weight);
      hist("etaAK4")->Fill(etareco,weight);
      ((TProfile*)hist("ptratioVSptAK4"))->Fill(ptgen,ptratio,weight);
      ((TProfile*)hist("ptratioVSetaAK4"))->Fill(etagen,ptratio,weight);
      if (ptgen>=30 && ptgen<=40) {((TProfile*)hist("ptratioVSeta30AK4"))->Fill(etagen,ptratio,weight);}
      ((TProfile*)hist("ptratioVSnpvAK4"))->Fill(Npvs,ptratio,weight);
      //<(eta,reco-eta,gen)*sign(eta,gen)> vs eta,gen for e.g. 30<pTgen<40 GeV
      float sign = 1.0; if (etagen<0.0) {sign=-1.0;}
      if (ptgen>=30 && ptgen<=40) {((TProfile*)hist("etadiffVSeta30AK4"))->Fill(etagen,(etareco-etagen)*sign,weight);}



    }
  }
 


  int gen1=-1, gen2=-1;
  if (event.gentopjets->size()>0) gen1=match2GenTopJet(event.gentopjets->at(0),event);
  if (event.gentopjets->size()>1) gen2=match2GenTopJet(event.gentopjets->at(1),event);
  
  if (gen1>-1&&gen2>-1)
  {
    float pt1gen= TopJetPt(event.gentopjets->at(0));
    float pt2gen= TopJetPt(event.gentopjets->at(1));
    float eta1gen= TopJetEta(event.gentopjets->at(0));
    float eta2gen= TopJetEta(event.gentopjets->at(1));
    float mzgen= ZprimeMass(event.gentopjets->at(0),event.gentopjets->at(1));
    float mzreco= ZprimeMass(event.topjets->at(gen1),event.topjets->at(gen2));
    float mzratio= mzreco/mzgen;
  //mz/mz vs pt
    ((TProfile*)hist("mZratioVSpt"))->Fill(pt1gen,mzratio,weight);
  //mz/mz vs eta
    ((TProfile*)hist("mZratioVSeta"))->Fill(eta1gen,mzratio,weight);
  //mz/mz vs pt,eta
    ((TProfile2D*)hist("mZratioVSpteta"))->Fill(pt1gen,eta1gen,mzratio,weight);
  //mz/mz vs pt,pt
    ((TProfile2D*)hist("mZratioVSptpt"))->Fill(pt1gen,pt2gen,mzratio,weight);
    ((TProfile2D*)hist("mZratioVSetaeta"))->Fill(eta1gen,eta2gen,mzratio,weight);
  }
}
  
  
// for(unsigned int i=0; i<jet_collection_names.size(); i++)
//   {
//     auto jets = &event.get(jet_handles[i]);
//     hist(("N_"+jet_collection_names[i]).c_str())->Fill(jets->size(),weight);
//     if (jets->size()>0) if (jets->at(0).v4().isTimelike()) hist(("m1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0).v4().M(),weight);
//     if (jets->size()>1) if (jets->at(1).v4().isTimelike()) hist(("m2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1).v4().M(),weight);
//     if (jets->size()>1) if ((jets->at(1).v4()+jets->at(0).v4()).isTimelike()) hist(("m12_"+jet_collection_names[i]).c_str())->Fill((jets->at(0).v4()+jets->at(1).v4()).M(),weight);
//     if (jets->size()>0) hist(("pT1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0).pt(),weight);
//     if (jets->size()>1) hist(("pT2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1).pt(),weight);
//     // if (jets->size()>0) hist(("nsub1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0),weight);
//     // if (jets->size()>1) hist(("nsub2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1),weight);
//     if (jets->size()>0) hist(("csv1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0).btag_combinedSecondaryVertex(),weight);
//     if (jets->size()>1) hist(("csv2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1).btag_combinedSecondaryVertex(),weight);
//   }

// for(unsigned int i=0; i<topjet_collection_names.size(); i++)
//   {
//     auto jets = &event.get(topjet_handles[i]);
//     hist(("N_"+topjet_collection_names[i]).c_str())->Fill(jets->size(),weight);
//     if (jets->size()>0) hist(("m1_"+topjet_collection_names[i]).c_str())->Fill(TopJetMass(jets->at(0)),weight);
//     if (jets->size()>1) hist(("m2_"+topjet_collection_names[i]).c_str())->Fill(TopJetMass(jets->at(1)),weight);
//     if (jets->size()>1) hist(("m12_"+topjet_collection_names[i]).c_str())->Fill(ZprimeMass(jets->at(0),jets->at(1)),weight);
//     if (jets->size()>0) hist(("pT1_"+topjet_collection_names[i]).c_str())->Fill(TopJetPt(jets->at(0)),weight);
//     if (jets->size()>1) hist(("pT2_"+topjet_collection_names[i]).c_str())->Fill(TopJetPt(jets->at(1)),weight);
//     if (jets->size()>0) hist(("nsub1_"+topjet_collection_names[i]).c_str())->Fill(TopJetNsub(jets->at(0)),weight);
//     if (jets->size()>1) hist(("nsub2_"+topjet_collection_names[i]).c_str())->Fill(TopJetNsub(jets->at(1)),weight);
//     if (jets->size()>0) hist(("csv1_"+topjet_collection_names[i]).c_str())->Fill(getMaxCSV(jets->at(0)),weight);
//     if (jets->size()>1) hist(("csv2_"+topjet_collection_names[i]).c_str())->Fill(getMaxCSV(jets->at(1)),weight);
//   }

//   std::vector<Jet>* jets = event.jets;
//   int Njets = jets->size();
//   hist("N_jets")->Fill(Njets, weight);
//   
//   if(Njets>=1){
//     hist("eta_jet1")->Fill(jets->at(0).eta(), weight);
//   }
//   if(Njets>=2){
//     hist("eta_jet2")->Fill(jets->at(1).eta(), weight);
//   }
//   if(Njets>=3){
//     hist("eta_jet3")->Fill(jets->at(2).eta(), weight);
//   }
//   if(Njets>=4){
//     hist("eta_jet4")->Fill(jets->at(3).eta(), weight);
//   }

//   int Nmuons = event.muons->size();
//   hist("N_mu")->Fill(Nmuons, weight);
//   for (const Muon & thismu : *event.muons){
//       hist("pt_mu")->Fill(thismu.pt(), weight);
//       hist("eta_mu")->Fill(thismu.eta(), weight);
//       hist("reliso_mu")->Fill(thismu.relIso(), weight);
//   }
  
  
  hist("N_pv")->Fill(Npvs, weight);
}

Zp2TopVLQAllHadHists::~Zp2TopVLQAllHadHists(){}

MistagAndShapeHists::MistagAndShapeHists(Context & ctx, const string & dirname): Hists(ctx, dirname){

  //mass shape
  book<TH1F>("mass_shape",";m;Events",200,0.0,400.0);
  //mistag matrix 2d 3d
  //double csv_bins[] = {-100.0,0.0,0.244,0.679,10.0};
  double csv_bins[] = {-11.0,0.0,0.423,0.814,1.1};//0.941
  //double mistag_pt_bins[] = {150.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,360.0,380.0,400.0,450.0,500.0,600.0,800.0,2000.0};
  double mistag_pt_bins[] = {400.0,450.0,500.0,600.0,800.0,1000.0,2000.0};
  // double nsub_bins[] = {0.0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2};
  book<TH2F>( "mistag2D_num", ";pT;CSV", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins);
  book<TH2F>( "mistag2D_den", ";pT;CSV", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins);
  // book<TH3F>( "mistag3D", ";pT;CSV;nsub", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins,sizeof(nsub_bins)/sizeof(double)-1, nsub_bins);

}

void MistagAndShapeHists::fill(const Event & event){

  double weight = event.weight;
  
  if (event.topjets->size()<2) return;

  //mass shape
  unsigned int tag_index=0,probe_index=0;
  TRandom3 rand(abs(static_cast<int>(sin(event.topjets->at(1).subjets().at(0).eta()*1000000)*100000)));
  if (rand.Uniform(1.)<=0.5) probe_index=1;
  else tag_index=1;  
  if ( TopTag(event.topjets->at(tag_index)) && TopTag(event.topjets->at(probe_index)) && (deltaY(event.topjets->at(tag_index),event.topjets->at(probe_index))<1.0))// or use full z' candidate???
    hist("mass_shape")->Fill(TopJetMass(event.topjets->at(probe_index)));

  //mistag matrix 2d 3d
  unsigned int antitag_index=0; probe_index=0;
  rand.SetSeed(abs(static_cast<int>(sin(event.topjets->at(1).subjets().at(0).eta()*1000000)*100000)));
  if (rand.Uniform(1.)<=0.5) probe_index=1;
  else antitag_index=1;
  auto probeJet=event.topjets->at(probe_index);
  auto antitagJet=event.topjets->at(antitag_index);
  auto maxcsv = getMaxCSV(probeJet);
  auto pt = TopJetPt(probeJet);
  if (AntiTopTag(antitagJet) && (deltaY(antitagJet,probeJet)<1.0))
  {
    ((TH2F*)hist("mistag2D_den"))->Fill(pt,maxcsv,weight);
    if (TopTag(probeJet)) ((TH2F*)hist("mistag2D_num"))->Fill(pt,maxcsv,weight);
  }
}

MistagAndShapeHists::~MistagAndShapeHists(){}

BackgroundHists::BackgroundHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  f.reset(new TFile("/afs/desy.de/user/u/usaiem/xxl-af-cms/code/cmssw/CMSSW_7_2_1_patch4/src/UHH2/Zp2TopVLQAllHad/python/mistag.root"));
  // mass_shape.reset(std::move((TH1F*)f->Get("mass_shape")));
  // mistag.reset(std::move((TH2F*)f->Get("Mistag_CMSTT")));
  mass_shape.reset((TH1F*)f->Get("mass_shape"));
  mistag.reset((TH2F*)f->Get("Mistag_CMSTT"));

  book<TH1F>("m12CMS", ";m_{12,CMS};Events", 240, 0, 6000);
}

void BackgroundHists::fill(const Event & event){

  double weight = event.weight;
  unsigned int tag_index=0,mistag_index=0;
  TRandom3 rand(abs(static_cast<int>(sin(event.topjets->at(1).subjets().at(0).eta()*1000000)*100000)));
  if (rand.Uniform(1.)<=0.5) mistag_index=1;
  else tag_index=1;
  auto tagJet=event.topjets->at(tag_index);
  auto mistagJet=event.topjets->at(mistag_index);
  if(TopTag(tagJet))
  {
    auto maxcsv=getMaxCSV(mistagJet);
    auto mistag_bin = mistag->FindFixBin(mistagJet.pt(),maxcsv);
    auto mistag_value = mistag->GetBinContent(mistag_bin);
    gRandom->SetSeed(abs(static_cast<int>(sin(event.topjets->at(1).subjets().at(0).eta()*1000000)*100000)));
    auto RandomMass = mass_shape->GetRandom();
    TLorentzVector TagVector(0,0,0,0), MistagVector(0,0,0,0);
    LorentzVector TagSumOfSubjets(0,0,0,0), MistagSumOfSubjets(0,0,0,0);
    for(auto subjet : tagJet.subjets()) TagSumOfSubjets+=subjet.v4();
    for(auto subjet : mistagJet.subjets()) MistagSumOfSubjets+=subjet.v4();
    TagVector.SetPtEtaPhiE(TagSumOfSubjets.Pt(),TagSumOfSubjets.Eta(),TagSumOfSubjets.Phi(),TagSumOfSubjets.E());
    MistagVector.SetPtEtaPhiM(MistagSumOfSubjets.Pt(),MistagSumOfSubjets.Eta(),MistagSumOfSubjets.Phi(),RandomMass);
    auto mtt = ( TagVector + MistagVector ).M();
    if (deltaY(tagJet,mistagJet)<1.0)
    hist("m12CMS")->Fill(mtt,weight*mistag_value);
  }
}

BackgroundHists::~BackgroundHists(){
  //f->Close();
  //delete mistag;delete mass_shape;
}


PreselectionHists::PreselectionHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  //h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");
  //h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");

  book<TH1F>("N_toptags", ";N_{toptags};Events", 10, 0, 10);
  book<TH1F>("N_wtags", ";N_{wtags};Events", 10, 0, 10);
  book<TH1F>("N_btags", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_subjetbtags", ";N_{subjetbtags};Events", 10, 0, 10);

  book<TH1F>("pTtop", ";p_{T} top gen;Events", 300, 0, 3000);
  book<TH1F>("pTtprime", ";p_{T} T' gen;Events", 300, 0, 3000);
  book<TH1F>("pTb", ";p_{T} b gen;Events", 300, 0, 3000);
  book<TH1F>("pTw", ";p_{T} W gen;Events", 300, 0, 3000);
  book<TH1F>("pTtb", ";p_{T} b from t gen;Events", 300, 0, 3000);
  book<TH1F>("pTtw", ";p_{T} W from t gen;Events", 300, 0, 3000);
  book<TH1F>("pTzprime", ";p_{T} Z' gen;Events", 300, 0, 3000);

  book<TH1F>("ptop", ";p top gen;Events", 300, 0, 3000);
  book<TH1F>("ptprime", ";p T' gen;Events", 300, 0, 3000);
  book<TH1F>("pb", ";p b gen;Events", 300, 0, 3000);
  book<TH1F>("pw", ";p W gen;Events", 300, 0, 3000);
  book<TH1F>("ptb", ";p b from t gen;Events", 300, 0, 3000);
  book<TH1F>("ptw", ";p W from t gen;Events", 300, 0, 3000);
  book<TH1F>("pzprime", ";p Z' gen;Events", 300, 0, 3000);

  book<TH1F>("mtop", ";M top gen;Events", 300, 0, 3000);
  book<TH1F>("mtprime", ";M T' gen;Events", 300, 0, 3000);
  book<TH1F>("mb", ";M b gen;Events", 300, 0, 3000);
  book<TH1F>("mw", ";M W gen;Events", 300, 0, 3000);
  book<TH1F>("mtb", ";M b from t gen;Events", 300, 0, 3000);
  book<TH1F>("mtw", ";M W from t gen;Events", 300, 0, 3000);
  book<TH1F>("mzprime", ";M Z' gen;Events", 300, 0, 3000);

  book<TH1F>("dRbW", ";#Delta R(b,W);Events", 500, 0, 5);
  book<TH1F>("dRtT", ";#Delta R(t,T');Events", 500, 0, 5);
  book<TH1F>("dRbt", ";#Delta R(b,t);Events", 500, 0, 5);
  book<TH1F>("dRtW", ";#Delta R(t,W);Events", 500, 0, 5);
  book<TH1F>("dR_tb_tW", ";#Delta R(b from t, W from t);Events", 500, 0, 5);
  book<TH1F>("dR_tb_W", ";#Delta R(b from t, W from t);Events", 500, 0, 5);
  book<TH1F>("dR_tb_b", ";#Delta R(b from t, W from t);Events", 500, 0, 5);
  book<TH1F>("dR_b_tW", ";#Delta R(b from t, W from t);Events", 500, 0, 5);
  book<TH1F>("dR_W_tW", ";#Delta R(b from t, W from t);Events", 500, 0, 5);

  book<TH1F>("dR_W1_b1", ";#Delta R(b1, W1);Events", 500, 0, 5);
  book<TH1F>("dR_W2_b2", ";#Delta R(b2, W2);Events", 500, 0, 5);
  book<TH1F>("dR_W1_W2", ";#Delta R(W1, W2);Events", 500, 0, 5);
  book<TH1F>("dR_b1_b2", ";#Delta R(b1, b2);Events", 500, 0, 5);
  book<TH1F>("dR_W1_b2", ";#Delta R(b2, W1);Events", 500, 0, 5);
  book<TH1F>("dR_W2_b1", ";#Delta R(W2, b1);Events", 500, 0, 5);

  book<TH1F>("pT_closest_topjet_to_top", ";pT closest topjet to top;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_topjet_to_top", ";mass closest topjet to top;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_topjet_to_top", ";tau32 closest topjet to top;Events", 100, 0, 1);

  book<TH1F>("pT_closest_topjet_to_tprime", ";pT closest topjet to tprime;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_topjet_to_tprime", ";mass closest topjet to tprime;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_topjet_to_tprime", ";tau32 closest topjet to tprime;Events", 100, 0, 1);

  book<TH1F>("pT_closest_wjet_to_w", ";pT closest wjet to w;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_wjet_to_w", ";mass closest wjet to w;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_wjet_to_w", ";tau32 closest wjet to w;Events", 100, 0, 1);

  book<TH1F>("pT_closest_bjet_to_b", ";pT closest bjet to b;Events", 300, 0, 3000);
  book<TH1F>("csv_closest_bjet_to_b", ";csv closest bjet to b;Events", 100, 0, 1);


  book<TH1F>("pT_closest_wjet_to_tw", ";pT closest wjet to w from t;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_wjet_to_tw", ";mass closest wjet to w from t;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_wjet_to_tw", ";tau32 closest wjet to w from t;Events", 100, 0, 1);

  book<TH1F>("pT_closest_bjet_to_tb", ";pT closest bjet to b from t;Events", 300, 0, 3000);
  book<TH1F>("csv_closest_bjet_to_tb", ";csv closest bjet to b from t;Events", 100, 0, 1);



  book<TH1F>("pT_closest_wjet_to_w1", ";pT closest wjet to w;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_wjet_to_w1", ";mass closest wjet to w;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_wjet_to_w1", ";tau32 closest wjet to w;Events", 100, 0, 1);

  book<TH1F>("pT_closest_bjet_to_b1", ";pT closest bjet to b;Events", 300, 0, 3000);
  book<TH1F>("csv_closest_bjet_to_b1", ";csv closest bjet to b;Events", 100, 0, 1);

  book<TH1F>("pT_closest_wjet_to_w2", ";pT closest wjet to w;Events", 300, 0, 3000);
  book<TH1F>("mass_closest_wjet_to_w2", ";mass closest wjet to w;Events", 100, 0, 1000);
  book<TH1F>("nsub_closest_wjet_to_w2", ";tau32 closest wjet to w;Events", 100, 0, 1);

  book<TH1F>("pT_closest_bjet_to_b2", ";pT closest bjet to b;Events", 300, 0, 3000);
  book<TH1F>("csv_closest_bjet_to_b2", ";csv closest bjet to b;Events", 100, 0, 1);


  book<TH1F>("step1_wmass", ";step1: mass w candidate;Events", 100, 0, 1000);
  book<TH1F>("step1_wnsub", ";step1: nsub w candidate;Events", 100, 0, 1);
  book<TH1F>("step1_tcsv", ";step1: csv t candidate;Events", 100, 0, 1);
  book<TH1F>("step1_tpt", ";step1: pt t candidate;Events", 300, 0, 3000);
  book<TH1F>("step2_bcsv", ";step2: csv b candidate;Events", 100, 0, 1);
  book<TH1F>("step2_wpt", ";step2: pt w candidate;Events", 300, 0, 3000);
  book<TH1F>("step2_drbw", ";#Delta R(b,W);Events", 500, 0, 5);
  book<TH1F>("step3_tprimemass", ";step3: mass tprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step3_tprimept", ";step3: pt tprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemass", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemassbtag", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemassbtagnsub", ";step4: mass zprime candidate;Events", 300, 0, 3000);

  book<TH1F>("ttbarSR_zprimemass", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("ttbarSR_zprimemassbtag", ";step4: mass zprime candidate;Events", 300, 0, 3000);

  book<TH1F>("lowmassSR_zprimemass", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("lowmassSR_zprimemassbtag", ";step4: mass zprime candidate;Events", 300, 0, 3000);



}

void PreselectionHists::fill(const Event & event){
    double weight = event.weight;
  
  //get extra jet collections
  //const auto jetsAK8 = &event.get(h_jetsAK8);
  //const auto topjetsAK8 = &event.get(h_topjetsAK8);
  //const auto topjetsCA15 = &event.get(h_topjetsCA15);

  int N_toptags=0;
  for(auto topjet : *event.topjets)
    {
        if (TopTag(topjet))
        {
            N_toptags++;
        }
    }
  hist("N_toptags")->Fill(N_toptags,weight);

  int N_wtags=0;
  for(auto topjet : *event.topjets)
    {
        if (WTag(topjet))
        {
            N_wtags++;
        }
    }
  hist("N_wtags")->Fill(N_wtags,weight);

  int N_bjets=0;
  for(auto jet : *event.jets)
    {
      if (jet.btag_combinedSecondaryVertex()>0.890)
      {
          N_bjets++;
      }
    }
  hist("N_btags")->Fill(N_bjets,weight);


  int N_subjetbtags=0;
  for(auto topjet : *event.topjets)
    {
      if (getMaxCSV(topjet)>0.890)
      {
        N_subjetbtags++;
      }
    }
  hist("N_subjetbtags")->Fill(N_subjetbtags,weight);

if (!event.isRealData)
{

  GenParticle the_gen_top,the_gen_tprime,the_gen_w,the_gen_b,the_gen_tw,the_gen_tb,the_gen_w1,the_gen_b1,the_gen_w2,the_gen_b2;
  bool has_gen_top=false,has_gen_tprime=false,has_gen_w=false,has_gen_b=false,has_gen_tw=false,has_gen_tb=false,has_gen_w1=false,has_gen_b1=false,has_gen_w2=false,has_gen_b2=false;
  for (auto genp : *event.genparticles)
  {

    if (abs(genp.pdgId()) == 9900113)
    {
      hist("pTzprime")->Fill(genp.pt(),weight);
      hist("pzprime")->Fill(genp.v4().P(),weight);
      hist("mzprime")->Fill(genp.v4().M(),weight);
    }

    if (abs(genp.pdgId()) == 6)
    {
      hist("pTtop")->Fill(genp.pt(),weight);
      hist("ptop")->Fill(genp.v4().P(),weight);
      hist("mtop")->Fill(genp.v4().M(),weight);
      has_gen_top=true;
      the_gen_top=genp;

      auto pthe_gen_w = genp.daughter(event.genparticles, 1);
      auto pthe_gen_b = genp.daughter(event.genparticles, 2);
      if (pthe_gen_w && pthe_gen_b)
      {
        the_gen_tw=*pthe_gen_w;
        the_gen_tb=*pthe_gen_b;
        if(abs(the_gen_tw.pdgId()) != 24)
        {
          std::swap(the_gen_tw, the_gen_tb);
        }
        if(abs(the_gen_tw.pdgId()) == 24)
        {
          hist("pTtw")->Fill(the_gen_tw.pt(),weight);
          hist("ptw")->Fill(the_gen_tw.v4().P(),weight);
          hist("mtw")->Fill(the_gen_tw.v4().M(),weight);
          has_gen_tw=true;
        }
        if(abs(the_gen_tb.pdgId()) == 5)
        {
          hist("pTtb")->Fill(the_gen_tb.pt(),weight);
          hist("ptb")->Fill(the_gen_tb.v4().P(),weight);
          hist("mtb")->Fill(the_gen_tb.v4().M(),weight);
          has_gen_tb=true;
        }
      }
    }
    if (abs(genp.pdgId()) == 8000001)
    {
      hist("pTtprime")->Fill(genp.pt(),weight);
      hist("ptprime")->Fill(genp.v4().P(),weight);
      hist("mtprime")->Fill(genp.v4().M(),weight);
      has_gen_tprime=true;
      the_gen_tprime=genp;
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
          hist("pTw")->Fill(the_gen_w.pt(),weight);
          hist("pw")->Fill(the_gen_w.v4().P(),weight);
          hist("mw")->Fill(the_gen_w.v4().M(),weight);
          has_gen_w=true;
          if(genp.pdgId()>0)
          {
            the_gen_w1=the_gen_w;
            has_gen_w1=true;
          }
          else
          {
            the_gen_w2=the_gen_w;
            has_gen_w2=true;
          }
        }
        if(abs(the_gen_b.pdgId()) == 5)
        {
          hist("pTb")->Fill(the_gen_b.pt(),weight);
          hist("pb")->Fill(the_gen_b.v4().P(),weight);
          hist("mb")->Fill(the_gen_b.v4().M(),weight);
          has_gen_b=true;
          if(genp.pdgId()>0)
          {
            the_gen_b1=the_gen_b;
            has_gen_b1=true;
          }
          else
          {
            the_gen_b2=the_gen_b;
            has_gen_b2=true;
          }
        }
      } 
    }
  }


  if (has_gen_b && has_gen_w)
  {
    hist("dRbW")->Fill(deltaR(the_gen_b,the_gen_w),weight);
  }

  if (has_gen_top && has_gen_tprime)
  {
    hist("dRtT")->Fill(deltaR(the_gen_top,the_gen_tprime),weight);
  }

  if (has_gen_b && has_gen_top)
  {
    hist("dRbt")->Fill(deltaR(the_gen_b,the_gen_top),weight);
  }

  if (has_gen_top && has_gen_w)
  {
    hist("dRtW")->Fill(deltaR(the_gen_top,the_gen_w),weight);
  }


  if (has_gen_tb && has_gen_tw)
  {
    hist("dR_tb_tW")->Fill(deltaR(the_gen_tb,the_gen_tw),weight);
  }
  if (has_gen_tb && has_gen_w)
  {
    hist("dR_tb_W")->Fill(deltaR(the_gen_tb,the_gen_w),weight);
  }
  if (has_gen_tb && has_gen_b)
  {
    hist("dR_tb_b")->Fill(deltaR(the_gen_tb,the_gen_b),weight);
  }
  if (has_gen_b && has_gen_tw)
  {
    hist("dR_b_tW")->Fill(deltaR(the_gen_b,the_gen_tw),weight);
  }
  if (has_gen_w && has_gen_tw)
  {
    hist("dR_W_tW")->Fill(deltaR(the_gen_w,the_gen_tw),weight);
  }

  
  if (has_gen_w1 && has_gen_b1)
  {
    hist("dR_W1_b1")->Fill(deltaR(the_gen_w1,the_gen_b1),weight);
  }

  if (has_gen_w2 && has_gen_b2)
  {
    hist("dR_W2_b2")->Fill(deltaR(the_gen_w2,the_gen_b2),weight);
  }

  if (has_gen_w1 && has_gen_w2)
  {
    hist("dR_W1_W2")->Fill(deltaR(the_gen_w1,the_gen_w2),weight);
  }

  if (has_gen_b1 && has_gen_b2)
  {
    hist("dR_b1_b2")->Fill(deltaR(the_gen_b1,the_gen_b2),weight);
  }

  if (has_gen_w1 && has_gen_b2)
  {
    hist("dR_W1_b2")->Fill(deltaR(the_gen_w1,the_gen_b2),weight);
  }

  if (has_gen_w2 && has_gen_b1)
  {
    hist("dR_W2_b1")->Fill(deltaR(the_gen_w2,the_gen_b1),weight);
  }

  TopJet the_closest_top,the_closest_w,the_closest_w1,the_closest_w2,the_closest_tw,the_closest_tprime; Jet the_closest_b,the_closest_b1,the_closest_b2,the_closest_tb;
  //bool has_closest_top=false,has_closest_w=false,has_closest_b=false,has_closest_tprime=false;
  if (has_gen_top)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_top,topjet)<0.8)
      {
        hist("pT_closest_topjet_to_top")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_topjet_to_top")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_topjet_to_top")->Fill(TopJetNsub(topjet),weight);
        //has_closest_top=true;
        the_closest_top=topjet;
      }
    }
  }

  if (has_gen_tprime)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_tprime,topjet)<0.8)
      {
        hist("pT_closest_topjet_to_tprime")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_topjet_to_tprime")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_topjet_to_tprime")->Fill(TopJetNsub(topjet),weight);
        //has_closest_tprime=true;
        the_closest_tprime=topjet;
      }
    }
  }

  if (has_gen_w)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_w,topjet)<0.8)
      {
        hist("pT_closest_wjet_to_w")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_wjet_to_w")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_wjet_to_w")->Fill(TopJetNsub2(topjet),weight);
        //has_closest_w=true;
        the_closest_w=topjet;
      }
    }
  }

    if (has_gen_b)
  {
    for(auto jet : *event.jets)
    {
      if (deltaR(the_gen_b,jet)<0.4)
      {
        hist("pT_closest_bjet_to_b")->Fill(jet.pt(),weight);
        hist("csv_closest_bjet_to_b")->Fill(jet.btag_combinedSecondaryVertex(),weight);
        //has_closest_b=true;
        the_closest_b=jet;
      }
    }
  }




  if (has_gen_tw)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_tw,topjet)<0.8)
      {
        hist("pT_closest_wjet_to_tw")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_wjet_to_tw")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_wjet_to_tw")->Fill(TopJetNsub2(topjet),weight);
        //has_closest_w=true;
        the_closest_tw=topjet;
      }
    }
  }

    if (has_gen_tb)
  {
    for(auto jet : *event.jets)
    {
      if (deltaR(the_gen_tb,jet)<0.4)
      {
        hist("pT_closest_bjet_to_tb")->Fill(jet.pt(),weight);
        hist("csv_closest_bjet_to_tb")->Fill(jet.btag_combinedSecondaryVertex(),weight);
        //has_closest_b=true;
        the_closest_tb=jet;
      }
    }
  }



if (has_gen_w1)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_w1,topjet)<0.8)
      {
        hist("pT_closest_wjet_to_w1")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_wjet_to_w1")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_wjet_to_w1")->Fill(TopJetNsub2(topjet),weight);
        //has_closest_w=true;
        the_closest_w1=topjet;
      }
    }
  }

    if (has_gen_b1)
  {
    for(auto jet : *event.jets)
    {
      if (deltaR(the_gen_b1,jet)<0.4)
      {
        hist("pT_closest_bjet_to_b1")->Fill(jet.pt(),weight);
        hist("csv_closest_bjet_to_b1")->Fill(jet.btag_combinedSecondaryVertex(),weight);
        //has_closest_b=true;
        the_closest_b1=jet;
      }
    }
  }

  if (has_gen_w2)
  {
    for(auto topjet : *event.topjets)
    {
      if (deltaR(the_gen_w2,topjet)<0.8)
      {
        hist("pT_closest_wjet_to_w2")->Fill(TopJetPt(topjet),weight);
        hist("mass_closest_wjet_to_w2")->Fill(TopJetMass(topjet),weight);
        hist("nsub_closest_wjet_to_w2")->Fill(TopJetNsub2(topjet),weight);
        //has_closest_w=true;
        the_closest_w2=topjet;
      }
    }
  }

  if (has_gen_b2)
  {
    for(auto jet : *event.jets)
    {
      if (deltaR(the_gen_b2,jet)<0.4)
      {
        hist("pT_closest_bjet_to_b2")->Fill(jet.pt(),weight);
        hist("csv_closest_bjet_to_b2")->Fill(jet.btag_combinedSecondaryVertex(),weight);
        //has_closest_b=true;
        the_closest_b2=jet;
      }
    }
  }

}










//selection



    TopJet the_top;
    bool has_the_top=false;
    for(auto topjet : *event.topjets)
    {
        if (TopTag(topjet))
        {
            the_top=topjet;
            has_the_top=true;
            hist("step1_tcsv")->Fill(getMaxCSV(topjet),weight);
            hist("step1_tpt")->Fill(TopJetPt(topjet),weight);
            break;
        }
    }
    bool has_the_w=false;
    TopJet the_w;
    if (has_the_top)
    {
        bool found=false;
        for(auto topjet : *event.topjets)
        {
            if(deltaR(topjet,the_top)>0.1 && !found)
            {
              hist("step1_wmass")->Fill(TopJetMass(topjet),weight);
              hist("step1_wnsub")->Fill(TopJetNsub2(topjet),weight);
              found=true;
            }
            if (WTag(topjet)&&deltaR(topjet,the_top)>0.1)
            {
                the_w=topjet;
                has_the_w=true;
                hist("step2_wpt")->Fill(TopJetPt(topjet),weight);
                break;
            }
        }
    }
    bool has_the_b=false;
    Jet the_b;
    if (has_the_top && has_the_w)
    {
        bool found=false;
        for(auto jet : *event.jets)
        {
            if(deltaR(jet,the_top)>0.8 && !found)
            {
              hist("step2_bcsv")->Fill(jet.btag_combinedSecondaryVertex(),weight);
              found=true;
            }
            if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8 && jet.pt()>100.0)
            {
                the_b=jet;
                has_the_b=true;
                hist("step2_drbw")->Fill(deltaR(the_b,the_w),weight);
                hist("step3_tprimemass")->Fill(TprimeMass(the_w,the_b),weight);
                hist("step3_tprimept")->Fill(TprimePt(the_w,the_b),weight);
                break;
            }
        }
    }
    
    if (has_the_b && has_the_w && has_the_top)
    {
      float tprimemass=TprimeMass(the_w,the_b);
    float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b);
    float topmaxcsv=getMaxCSV(the_top);
      if (tprimemass>500.0)
      {
        hist("step4_zprimemass")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("step4_zprimemassbtag")->Fill(zprimemass,weight);
        //if (topmaxcsv>0.890 && TopJetNsub(the_top)<0.7) hist("step4_zprimemassbtagnsub")->Fill(zprimemass,weight);
      }
      if (tprimemass>140.0 && tprimemass<250.0)
      {
        hist("step4_zprimemass")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("ttbarSR_zprimemassbtag")->Fill(zprimemass,weight);
        //if (topmaxcsv>0.890 && TopJetNsub(the_top)<0.7) hist("ttbarSR_zprimemassbtagnsub")->Fill(zprimemass,weight);
      }
      if (tprimemass>250.0 && tprimemass<500.0)
      {
        hist("step4_zprimemass")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("lowmassSR_zprimemassbtag")->Fill(zprimemass,weight);
        //if (topmaxcsv>0.890 && TopJetNsub(the_top)<0.7) hist("lowmassSR_zprimemassbtagnsub")->Fill(zprimemass,weight);
      }

    }


}

PreselectionHists::~PreselectionHists(){}


TriggerHists::TriggerHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  book<TH1F>("HT", ";HT_{50};Events", 200, 0, 10000);
  book<TH1F>("HTCA8", ";HT_{CA8};Events", 200, 0, 10000);
  book<TH1F>("pt1", ";leading topjet p_{T};Events", 200, 0, 4000);
  book<TH1F>("pt2", ";subleading topjet p_{T};Events", 200, 0, 4000);
  h_ht=ctx.get_handle<float>("ht");
  h_htca8=ctx.get_handle<float>("htca8");
  h_pt1ca8=ctx.get_handle<float>("pt1ca8");
  h_pt2ca8=ctx.get_handle<float>("pt2ca8");

}
void TriggerHists::fill(const Event & event){
  double weight = event.weight;
  hist("HT")->Fill(event.get(h_ht),weight);
  hist("HTCA8")->Fill(event.get(h_htca8),weight);
  hist("pt1")->Fill(event.get(h_pt1ca8),weight);
  hist("pt2")->Fill(event.get(h_pt2ca8),weight);
}
TriggerHists::~TriggerHists(){

}





SelectionHists::SelectionHists(Context & ctx, const string & dirname): Hists(ctx, dirname){

  book<TH1F>("N_toptags", ";N_{toptags};Events", 10, 0, 10);
  book<TH1F>("N_wtags", ";N_{wtags};Events", 10, 0, 10);
  book<TH1F>("Pos_toptags", ";Pos_{toptags};Events", 10, 0, 10);
  book<TH1F>("Pos_wtags", ";Pos_{wtags};Events", 10, 0, 10);

  book<TH1F>("N_btags", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_btags_good", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_btags_ttbarCR", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_btags_good_ttbarCR", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_subjetbtags", ";N_{subjetbtags};Events", 10, 0, 10);

  book<TH1F>("bmass", ";m_{b};Events", 200, 0, 100);
  book<TH1F>("bpt", ";p_{T,b};Events", 200, 0, 1000);
  book<TH1F>("bcsv", ";CSV_{b};Events", 101, 0, 1.01);
  book<TH1F>("csv_pthighest", ";CSV_{b};Events", 101, 0, 1.01);
  book<TH1F>("csv_csvhighest", ";CSV_{b};Events", 101, 0, 1.01);

  book<TH1F>("wmass", ";m_{W};Events", 200, 0, 1000);
  book<TH1F>("wpt", ";p_{t,W};Events", 400, 0, 2000);
  book<TH1F>("wnsub", ";#tau_{2}/#tau_{1}(W);Events", 101, 0, 1.01);

  book<TH1F>("toppt", ";p_{T,top};Events", 400, 0, 2000);
  book<TH1F>("topmass", ";m_{top};Events", 400, 0, 2000);
  book<TH1F>("topnsub", ";#tau_{3}/#tau_{2}(top);Events", 101, 0, 1.01);
  book<TH1F>("topcsv", ";CSV_{top};Events", 101, 0, 1.01);

  book<TH1F>("Nm1wmass", ";m_{W};Events", 200, 0, 1000);
  book<TH1F>("Nm1wnsub", ";#tau_{2}/#tau_{1}(W);Events", 101, 0, 1.01);
  book<TH1F>("Nm1topmass", ";m_{top};Events", 400, 0, 2000);
  book<TH1F>("Nm1topnsub", ";#tau_{3}/#tau_{2}(top);Events", 101, 0, 1.01);

  book<TH1F>("dRbt", ";#Delta R(b,top);Events", 500, 0, 5);
  book<TH1F>("dRbW", ";#Delta R(b,W);Events", 500, 0, 5);
  book<TH1F>("dRtW", ";#Delta R(top,W);Events", 500, 0, 5);
  book<TH1F>("dRtTp", ";#Delta R(top,T');Events", 500, 0, 5);
  book<TH1F>("dRbTp", ";#Delta R(b,T');Events", 500, 0, 5);
  book<TH1F>("dRWTp", ";#Delta R(W,T');Events", 500, 0, 5);

  book<TH1F>("dRbtGEN", ";#Delta R(b,top);Events", 500, 0, 5);
  book<TH1F>("dRbWGEN", ";#Delta R(b,W);Events", 500, 0, 5);
  book<TH1F>("dRtWGEN", ";#Delta R(top,W);Events", 500, 0, 5);
  book<TH1F>("dRtTpGEN", ";#Delta R(top,T');Events", 500, 0, 5);
  book<TH1F>("dRbTpGEN", ";#Delta R(b,T');Events", 500, 0, 5);
  book<TH1F>("dRWTpGEN", ";#Delta R(W,T');Events", 500, 0, 5);


  book<TH1F>("ht", ";HT;Events", 300, 0, 3000);
  book<TH1F>("htca8", ";HT_{CA8};Events", 300, 0, 3000);
  book<TH1F>("ht_twb", ";HT_{top+W+b};Events", 300, 0, 3000);
  book<TH1F>("npv", ";N_{PV};Events", 100, 0, 100);
  book<TH1F>("nevt", ";N_{events};Events", 1, 0, 1);

  book<TH1F>("toppt_wpt", ";p_{T,top}-p_{T,W};Events", 400, -1000, 1000);
  book<TH1F>("toppt_wbpt", ";p_{T,top}-p_{T,T'};Events", 400, -1000, 1000);

  book<TH1F>("tprimemass", ";m_{T'};Events", 300, 0, 3000);
  book<TH1F>("tprimept", ";p_{T,T'};Events", 300, 0, 3000);

  book<TH1F>("zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimept", ";p_{T,Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassbtag", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassnobtag", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassbmass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassnobmass", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("tprimemass_res", ";m_{T'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassbtag_res", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("zprimemassnobtag_res", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("ht_twbSR", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("ht_twbSRbtag", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("ht_twbSRnobtag", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("ttbarCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("ttbarCR_zprimemassbtag", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("lowmassCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("lowmassCR_zprimemassbtag", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("ttbarCR_zprimemass_low", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("ttbarCR_zprimemassbtag_low", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("lowmassCR_zprimemass_low", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("lowmassCR_zprimemassbtag_low", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("antitopmassCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antitopnsubCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwmassCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwnsubCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibcsvCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibptCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibmassCR_zprimemass", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("antitopmassCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antitopnsubCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwmassCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwnsubCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibcsvCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibptCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibmassCRmass_zprimemass", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("antitopmassCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antitopnsubCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwmassCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwnsubCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibcsvCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibptCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibmassCRbtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("antitopmassCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antitopnsubCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwmassCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antiwnsubCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibcsvCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibptCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("antibmassCRnobtag_zprimemass", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("bkg1", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg2", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg12", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("bkg1up", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg2up", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg12up", ";m_{Z'};Events", 300, 0, 3000);

  book<TH1F>("bkg1down", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg2down", ";m_{Z'};Events", 300, 0, 3000);
  book<TH1F>("bkg12down", ";m_{Z'};Events", 300, 0, 3000);

  string version=ctx.get("dataset_version", "<not set>");
  top_sys=0;
  w_sys=0;
  //pu_sys=0;
  ttbar_sys=0;

  if (contains(version,"TTBARUP")&&contains(version,"TTbar")) ttbar_sys=1;
  if (contains(version,"TTBARDOWN")&&contains(version,"TTbar")) ttbar_sys=-1;

  if (contains(version,"TSFUP")) top_sys=1;
  if (contains(version,"TSFDOWN")) top_sys=-1;
  if (contains(version,"WSFUP")) w_sys=1;
  if (contains(version,"WSFDOWN")) w_sys=-1;
  //if (contains(version,"PUUP")) pu_sys=1;
  //if (contains(version,"PUDOWN")) pu_sys=-1;

}

void SelectionHists::fill(const Event & event){
    double weight = event.weight;
    //if (pu_sys==1) weight=event.weight_pu_up;
    //else if (pu_sys==-1) weight=event.weight_pu_down;
    weight=weight*TTbarWeight(event,ttbar_sys);
//gen part

bool has_twb_gen=false;
float dRbt=0;
float dRbW=0;
float dRtW=0;
float dRtTp=0;
float dRbTp=0;
float dRWTp=0;
if (!event.isRealData)
{
  GenParticle the_gen_top,the_gen_tprime,the_gen_w,the_gen_b;
  bool has_gen_top=false,has_gen_tprime=false,has_gen_w=false,has_gen_b=false;
  for (auto genp : *event.genparticles)
  {

    if (abs(genp.pdgId()) == 6)
    {
      has_gen_top=true;
      the_gen_top=genp;
    }
    if (abs(genp.pdgId()) == 8000001)
    {
      has_gen_tprime=true;
      the_gen_tprime=genp;
      auto pthe_gen_w = genp.daughter(event.genparticles, 1);
      auto pthe_gen_b = genp.daughter(event.genparticles, 2);
      if (pthe_gen_w && pthe_gen_b)
      {
        the_gen_w=*pthe_gen_w;
        the_gen_b=*pthe_gen_b;
        if(abs(the_gen_w.pdgId()) != 24) std::swap(the_gen_w, the_gen_b);
        if(abs(the_gen_w.pdgId()) == 24) has_gen_w=true;
        if(abs(the_gen_b.pdgId()) == 5) has_gen_b=true;
      } 
    }
  }
  if (has_gen_top && has_gen_b && has_gen_w && has_gen_tprime)
  {
    has_twb_gen=true;
    dRbt=deltaR(the_gen_b,the_gen_top);
    dRbW=deltaR(the_gen_b,the_gen_w);
    dRtW=deltaR(the_gen_top,the_gen_w);
    dRtTp=deltaR(the_gen_top,the_gen_tprime);
    dRbTp=deltaR(the_gen_b,the_gen_tprime);
    dRWTp=deltaR(the_gen_w,the_gen_tprime);
  }
}


  int N_toptags=0;
  for(auto topjet : *event.topjets)
    {
        if (TopTag(topjet))
        {
            N_toptags++;
        }
    }
  hist("N_toptags")->Fill(N_toptags,weight);
  for(unsigned int i=0; i<event.topjets->size(); i++)
  {
        if (TopTag(event.topjets->at(i)))
        {
            hist("Pos_toptags")->Fill(i,weight);
        }
        if (WTag(event.topjets->at(i)))
        {
            hist("Pos_wtags")->Fill(i,weight);
        }
  }

  int N_wtags=0;
  for(auto topjet : *event.topjets)
    {
        if (WTag(topjet))
        {
            N_wtags++;
        }
    }
  hist("N_wtags")->Fill(N_wtags,weight);

  int N_bjets=0;
  for(auto jet : *event.jets)
    {
      if (jet.btag_combinedSecondaryVertex()>0.890)
      {
          N_bjets++;
      }
    }
  hist("N_btags")->Fill(N_bjets,weight);

  int N_bjets_good=0;
  for(auto jet : *event.jets)
    {
      if (jet.btag_combinedSecondaryVertex()>0.890 &&deltaR(jet,event.topjets->at(0))>0.8 &&deltaR(jet,event.topjets->at(1))>0.8)
      {
          N_bjets_good++;
      }
    }
  hist("N_btags_good")->Fill(N_bjets_good,weight);


  int N_subjetbtags=0;
  for(auto topjet : *event.topjets)
    {
      if (getMaxCSV(topjet)>0.890)
      {
        N_subjetbtags++;
      }
    }
  hist("N_subjetbtags")->Fill(N_subjetbtags,weight);

  hist("ht")->Fill(getHT50(event),weight);
  hist("htca8")->Fill(getHTCA8(event),weight);
  hist("npv")->Fill(event.pvs->size(),weight);
  hist("nevt")->Fill(0.5,weight);

//selection

  //toptag+wtag
  TopJet the_top, the_w, the_w2;
  Jet the_b, the_b2;
  Jet the_b_low;

  // if(TopTag(event.topjets->at(0)))
  // {
  //   hist("wmass")->Fill(TopJetMass(event.topjets->at(1)),weight);
  //   hist("wpt")->Fill(TopJetPt(event.topjets->at(1)),weight);
  //   hist("wnsub")->Fill(TopJetNsub2(event.topjets->at(1)),weight);
  // }
  // if(TopTag(event.topjets->at(1)))
  // {
  //   hist("wmass")->Fill(TopJetMass(event.topjets->at(0)),weight);
  //   hist("wpt")->Fill(TopJetPt(event.topjets->at(0)),weight);
  //   hist("wnsub")->Fill(TopJetNsub2(event.topjets->at(0)),weight);
  // }
  // if(WTag(event.topjets->at(0)))
  // {
  //   hist("toppt")->Fill(TopJetPt(event.topjets->at(1)),weight);
  //   hist("topmass")->Fill(TopJetMass(event.topjets->at(1)),weight);
  //   hist("topnsub")->Fill(TopJetNsub(event.topjets->at(1)),weight);
  //   hist("topcsv")->Fill(getMaxCSV(event.topjets->at(1)),weight);
  // }
  // if(WTag(event.topjets->at(1)))
  // {
  //   hist("toppt")->Fill(TopJetPt(event.topjets->at(0)),weight);
  //   hist("topmass")->Fill(TopJetMass(event.topjets->at(0)),weight);
  //   hist("topnsub")->Fill(TopJetNsub(event.topjets->at(0)),weight);
  //   hist("topcsv")->Fill(getMaxCSV(event.topjets->at(0)),weight);
  // }

  bool has_tw=false;
  bool has_twb=false;
  bool has_twb_low=false;
  bool has_ww=false;
  if (TopTag(event.topjets->at(0))&&WTag(event.topjets->at(1)))
  {
    the_top=event.topjets->at(0);
    the_w=event.topjets->at(1);
    has_tw=true;
  }
  else if(TopTag(event.topjets->at(1))&&WTag(event.topjets->at(0)))
  {
    the_top=event.topjets->at(1);
    the_w=event.topjets->at(0);
    has_tw=true;
  }
  else if(WTag(event.topjets->at(1))&&WTag(event.topjets->at(0)))
  {
    the_w=event.topjets->at(0);
    the_w2=event.topjets->at(1);
    has_ww=true;
  }
  ///////////////////RESOLVED ANALYSIS
  if (has_ww)
  {
    float additional_weight=WTagSF(event, the_w, w_sys)*WTagSF(event, the_w2, w_sys);
    bool has_b=false;
    bool has_b2=false;
    bool duebtag=false;
    for(auto jet : *event.jets)
      if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_w)>0.8 &&deltaR(jet,the_w2)>0.8 && jet.pt()>50.0)
      {
        the_b=jet; has_b=true; break;
      }  
    if (has_b) for(auto jet : *event.jets)
      if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_w)>0.8 &&deltaR(jet,the_w2)>0.8 && jet.pt()>50.0 && fabs(jet.eta()-the_b.eta())>0.01)
      {
        
        the_b2=jet; has_b2=true; duebtag=true; break;
      }
    if (has_b && !has_b2) for(auto jet : *event.jets)
      if (deltaR(jet,the_w)>0.8 &&deltaR(jet,the_w2)>0.8 && jet.pt()>50.0 && fabs(jet.eta()-the_b.eta())>0.01)
      {
        
        the_b2=jet; has_b2=true; break;
      }
    if (has_b && has_b2)
    {
      std::vector<TopJet> TopW =    {the_w,  the_w2, the_w,  the_w2};
      std::vector<TopJet> TprimeW = {the_w2, the_w,  the_w2, the_w};
      std::vector<Jet> TopB =       {the_b,  the_b2, the_b2, the_b};
      std::vector<Jet> TprimeB =    {the_b2, the_b,  the_b,  the_b2};
      float biggestTprimeMass=-1;
      bool found=false;
      unsigned int index=0;
      for(unsigned int i=0;i<TopW.size();i++)
      {
        float TopMass=TprimeMass(TopW[i],TopB[i]);
        float TprimeMass2=TprimeMass(TprimeW[i],TprimeB[i]);
        if (TopMass>140.0 && TopMass<250.0 && TprimeMass2>biggestTprimeMass)
        {
          found=true;
          biggestTprimeMass=TprimeMass2;
          index=i;
        }
      }
      if (found)
      {
        float TprimeMass2=TprimeMass(TprimeW[index],TprimeB[index]);
        hist("tprimemass_res")->Fill(TprimeMass2,weight*additional_weight);
        if (TprimeMass2>500.0)
        {
          float ZprimeMass=ZprimeMassResVLQ(TprimeW[index],TopW[index],TprimeB[index],TopB[index]);
          if (duebtag) hist("zprimemassbtag_res")->Fill(ZprimeMass,weight*additional_weight);
          else hist("zprimemassnobtag_res")->Fill(ZprimeMass,weight*additional_weight);
        }

      }
    } 

  }
  //end of resolved analysis

  float additional_weight=1.0;
  if (has_tw)
  {
    additional_weight=WTagSF(event, the_w, w_sys)*TopTagSF(event, the_top, top_sys);
    weight=weight*additional_weight;
  }
  else
  {
    //partial weights
    if (TopTag(event.topjets->at(0))) weight=weight*TopTagSF(event, event.topjets->at(0), top_sys);
    if (TopTag(event.topjets->at(1))) weight=weight*TopTagSF(event, event.topjets->at(1), top_sys);
    if (WTag(event.topjets->at(0))) weight=weight*WTagSF(event, event.topjets->at(0), w_sys);
    if (WTag(event.topjets->at(1))) weight=weight*WTagSF(event, event.topjets->at(1), w_sys);

  }

  if (has_tw) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8 &&deltaR(jet,the_w)>0.8 && jet.pt()>100.0)
  {
        the_b=jet; has_twb=true;
        break;
  }
  if (has_tw) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8 &&deltaR(jet,the_w)>0.8 && jet.pt()>50.0)
  {
        the_b_low=jet; has_twb_low=true;
        break;
  }

  float maxjetpt=-1;
  Jet the_maxjetpt;
  float maxjetcsv=-1;
  Jet the_maxjetcsv;
  if (has_tw) for(auto jet : *event.jets)
  if (deltaR(jet,the_top)>0.8 &&deltaR(jet,the_w)>0.8 && jet.pt()>50.0)
  {
        if (jet.pt()>maxjetpt)
        {
          maxjetpt=jet.pt();
          the_maxjetpt=jet;
        }
        if (jet.btag_combinedSecondaryVertex()>maxjetcsv)
        {
          maxjetcsv=jet.btag_combinedSecondaryVertex();
          the_maxjetcsv=jet;
        }
  }
  if (maxjetpt>-0.5)
  {
      hist("csv_pthighest")->Fill(the_maxjetpt.btag_combinedSecondaryVertex(),weight);
  }
  if (maxjetcsv>-0.5)
  {
      hist("csv_csvhighest")->Fill(the_maxjetcsv.btag_combinedSecondaryVertex(),weight);
  }

  Jet the_unselected_b;
  for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,event.topjets->at(0))>0.8 &&deltaR(jet,event.topjets->at(1))>0.8 && jet.pt()>100.0)
  {
        the_unselected_b=jet;
        break;
  }
  std::pair<TopJet, TopJet> SemiTopTag_mass_Wtag = findTopWpair( SemiTopTag_mass, WTag, event.topjets->at(0), event.topjets->at(1));
  if (!(SemiTopTag_mass_Wtag.first.pt()==SemiTopTag_mass_Wtag.second.pt()))
    if(TprimeMass(SemiTopTag_mass_Wtag.second,the_unselected_b)>500)
      hist("Nm1topnsub")->Fill(TopJetNsub(SemiTopTag_mass_Wtag.first),weight);
  std::pair<TopJet, TopJet> SemiTopTag_nsub_Wtag = findTopWpair( SemiTopTag_nsub, WTag, event.topjets->at(0), event.topjets->at(1));
  if (!(SemiTopTag_nsub_Wtag.first.pt()==SemiTopTag_nsub_Wtag.second.pt()))
    if(TprimeMass(SemiTopTag_nsub_Wtag.second,the_unselected_b)>500)
      hist("Nm1topmass")->Fill(TopJetMass(SemiTopTag_nsub_Wtag.first),weight);
  std::pair<TopJet, TopJet> TopTag_SemiWtag_mass = findTopWpair( TopTag, SemiWTag_mass, event.topjets->at(0), event.topjets->at(1));
  if (!(TopTag_SemiWtag_mass.first.pt()==TopTag_SemiWtag_mass.second.pt()))
    if(TprimeMass(TopTag_SemiWtag_mass.second,the_unselected_b)>500)
      hist("Nm1wnsub")->Fill(TopJetNsub2(TopTag_SemiWtag_mass.second),weight);
  std::pair<TopJet, TopJet> TopTag_SemiWtag_nsub = findTopWpair( TopTag, SemiWTag_nsub, event.topjets->at(0), event.topjets->at(1));
  if (!(TopTag_SemiWtag_nsub.first.pt()==TopTag_SemiWtag_nsub.second.pt()))
    if(TprimeMass(TopTag_SemiWtag_nsub.second,the_unselected_b)>500)
      hist("Nm1wmass")->Fill(TopJetMass(TopTag_SemiWtag_nsub.second),weight);
  // if (has_tw){ hist("dRtW")->Fill(deltaR(the_top,the_w),weight);
  //               hist("toppt_wpt")->Fill(TopJetPt(the_top)-TopJetPt(the_w),weight);}
  
  if (has_twb)
  {

      hist("wmass")->Fill(TopJetMass(the_w),weight);
      hist("wpt")->Fill(TopJetPt(the_w),weight);
      hist("wnsub")->Fill(TopJetNsub2(the_w),weight);
      hist("toppt")->Fill(TopJetPt(the_top),weight);
      hist("topmass")->Fill(TopJetMass(the_top),weight);
      hist("topnsub")->Fill(TopJetNsub(the_top),weight);
      hist("topcsv")->Fill(getMaxCSV(the_top),weight);

      hist("dRtW")->Fill(deltaR(the_top,the_w),weight);
      hist("toppt_wpt")->Fill(TopJetPt(the_top)-TopJetPt(the_w),weight);

      hist("dRbt")->Fill(deltaR(the_b,the_top),weight);
      hist("dRbW")->Fill(deltaR(the_b,the_w),weight);

      hist("toppt_wbpt")->Fill(TopJetPt(the_top)-TprimePt(the_w,the_b),weight);
      LorentzVector tprime_v4(0,0,0,0);
      //for(auto subjet : the_top.subjets()) tprime_v4 += subjet.v4();
      for(auto subjet : the_w.subjets()) tprime_v4 += subjet.v4();
      tprime_v4 += the_b.v4();
      Particle the_tp;
      the_tp.set_v4(tprime_v4);
      hist("dRtTp")->Fill(deltaR(the_top,the_tp),weight);
      float ht_twb = TopJetPt(the_top)+TopJetPt(the_w)+the_b.pt();
      hist("ht_twb")->Fill(ht_twb,weight);

      hist("dRbTp")->Fill(deltaR(the_b,the_tp),weight);
      hist("dRWTp")->Fill(deltaR(the_w,the_tp),weight);
      if (has_twb_gen)
      {
        hist("dRtWGEN")->Fill(dRtW,weight);
        hist("dRbtGEN")->Fill(dRbt,weight);
        hist("dRbWGEN")->Fill(dRbW,weight);
        hist("dRtTpGEN")->Fill(dRtTp,weight);
        hist("dRbTpGEN")->Fill(dRbTp,weight);
        hist("dRWTpGEN")->Fill(dRWTp,weight);
      }
      float tprimemass=TprimeMass(the_w,the_b);
      float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b);
      float topmaxcsv=getMaxCSV(the_top);
      float bmass=JetMass(the_b);
      hist("bmass")->Fill(bmass,weight);
      hist("bpt")->Fill(the_b.pt(),weight);
      hist("bcsv")->Fill(the_b.btag_combinedSecondaryVertex(),weight);
      hist("tprimemass")->Fill(tprimemass,weight);
      hist("tprimept")->Fill(TprimePt(the_w,the_b),weight);
      if (tprimemass>500.0)
      {
        hist("zprimemass")->Fill(zprimemass,weight);
        hist("ht_twbSR")->Fill(ht_twb,weight);
        hist("zprimept")->Fill(ZprimePtVLQ(the_top,the_w,the_b),weight);
        if (topmaxcsv>0.890)
        {
          hist("zprimemassbtag")->Fill(zprimemass,weight);
          hist("ht_twbSRbtag")->Fill(ht_twb,weight);
        }
        else
        {
          hist("zprimemassnobtag")->Fill(zprimemass,weight);
          hist("ht_twbSRnobtag")->Fill(ht_twb,weight);
        }
        if (bmass<10.0) hist("zprimemassbmass")->Fill(zprimemass,weight);
        else hist("zprimemassnobmass")->Fill(zprimemass,weight);
      }
      if (tprimemass>140.0 && tprimemass<250.0)
      {
        hist("ttbarCR_zprimemass")->Fill(zprimemass,weight);
        hist("N_btags_ttbarCR")->Fill(N_bjets,weight);
        hist("N_btags_good_ttbarCR")->Fill(N_bjets_good,weight);
        if (topmaxcsv>0.890) hist("ttbarCR_zprimemassbtag")->Fill(zprimemass,weight);
      }
      if (tprimemass>250.0 && tprimemass<500.0)
      {
        hist("lowmassCR_zprimemass")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("lowmassCR_zprimemassbtag")->Fill(zprimemass,weight);
      }
  }
  if (has_twb_low)
  {
      float topmaxcsv=getMaxCSV(the_top);
      float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b_low);
      float tprimemass=TprimeMass(the_w,the_b_low);
      if (tprimemass>140.0 && tprimemass<250.0)
      {
        hist("ttbarCR_zprimemass_low")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("ttbarCR_zprimemassbtag_low")->Fill(zprimemass,weight);
      }
      if (tprimemass>250.0 && tprimemass<500.0)
      {
        hist("lowmassCR_zprimemass_low")->Fill(zprimemass,weight);
        if (topmaxcsv>0.890) hist("lowmassCR_zprimemassbtag_low")->Fill(zprimemass,weight);
      }
  }

  //antitag CRs
  unsigned int tag_index;
  unsigned int probe_index;
  TRandom3 rand(abs(static_cast<int>(sin(event.topjets->at(1).subjets().at(0).eta()*1000000)*100000)));
  if (rand.Uniform(1.)<=0.5)
  {
    tag_index=0;
    probe_index=1;
  }
  else
  {
    tag_index=1;
    probe_index=0;
  }

  Jet the_b_antitopw;
  bool has_antitopwb=false;
  for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,event.topjets->at(probe_index))>0.8&&deltaR(jet,event.topjets->at(tag_index))>0.8 && jet.pt()>100.0)
  {
        the_b_antitopw=jet; has_antitopwb=true;
        break;
  }

  Jet the_b_topantiw;
  bool has_topantiwb=false;
  for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,event.topjets->at(tag_index))>0.8&&deltaR(jet,event.topjets->at(probe_index))>0.8 && jet.pt()>100.0)
  {
        the_b_topantiw=jet; has_topantiwb=true;
        break;
  }

  if (AntiTopTag_mass(event.topjets->at(probe_index))&&WTag(event.topjets->at(tag_index))&&has_antitopwb )
  {
    float zprimemass=ZprimeMassVLQ(event.topjets->at(probe_index),event.topjets->at(tag_index),the_b_antitopw);
    hist("antitopmassCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(event.topjets->at(tag_index),the_b_antitopw)>500.0)
    {
      hist("antitopmassCRmass_zprimemass")->Fill(zprimemass,weight);
      if (getMaxCSV(event.topjets->at(probe_index))>0.890)
      {
        hist("antitopmassCRbtag_zprimemass")->Fill(zprimemass,weight);
      }
      else
      {
        hist("antitopmassCRnobtag_zprimemass")->Fill(zprimemass,weight);
      }
    }
  }

  if (AntiTopTag_nsub(event.topjets->at(probe_index))&&WTag(event.topjets->at(tag_index))&&has_antitopwb )
  {
    float zprimemass=ZprimeMassVLQ(event.topjets->at(probe_index),event.topjets->at(tag_index),the_b_antitopw);
    hist("antitopnsubCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(event.topjets->at(tag_index),the_b_antitopw)>500.0)
    {
      hist("antitopnsubCRmass_zprimemass")->Fill(zprimemass,weight);
      if (getMaxCSV(event.topjets->at(probe_index))>0.890)
      {
        hist("antitopnsubCRbtag_zprimemass")->Fill(zprimemass,weight);
      }
      else
      {
        hist("antitopnsubCRnobtag_zprimemass")->Fill(zprimemass,weight);
      }
    }
  }

  if (AntiWTag_mass(event.topjets->at(probe_index))&&TopTag(event.topjets->at(tag_index))&&has_topantiwb )
  {
    float zprimemass=ZprimeMassVLQ(event.topjets->at(tag_index),event.topjets->at(probe_index),the_b_topantiw);
    hist("antiwmassCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(event.topjets->at(probe_index),the_b_topantiw)>500.0)
    {
      hist("antiwmassCRmass_zprimemass")->Fill(zprimemass,weight);
      if (getMaxCSV(event.topjets->at(tag_index))>0.890)
      {
        hist("antiwmassCRbtag_zprimemass")->Fill(zprimemass,weight);
      }
      else
      {
        hist("antiwmassCRnobtag_zprimemass")->Fill(zprimemass,weight);
      }
    }
  }

  if (AntiWTag_nsub(event.topjets->at(probe_index))&&TopTag(event.topjets->at(tag_index))&&has_topantiwb )
  {
    float zprimemass=ZprimeMassVLQ(event.topjets->at(tag_index),event.topjets->at(probe_index),the_b_topantiw);
    hist("antiwnsubCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(event.topjets->at(probe_index),the_b_topantiw)>500.0)
    {
      hist("antiwnsubCRmass_zprimemass")->Fill(zprimemass,weight);
      if (getMaxCSV(event.topjets->at(tag_index))>0.890)
      {
        hist("antiwnsubCRbtag_zprimemass")->Fill(zprimemass,weight);
      }
      else
      {
        hist("antiwnsubCRnobtag_zprimemass")->Fill(zprimemass,weight);
      }
    }
  }


  Jet the_b_antibcsv;
  bool has_twantibcsv=false;
  if (has_tw && !has_twb) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()<0.890&&deltaR(jet,the_top)>0.8&&deltaR(jet,the_w)>0.8 && jet.pt()>100.0)
  {
        the_b_antibcsv=jet; has_twantibcsv=true;
        break;
  }
  if (has_twantibcsv)
  {
    float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b_antibcsv);
    hist("antibcsvCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(the_w,the_b_antibcsv)>500.0)
    {
      hist("antibcsvCRmass_zprimemass")->Fill(zprimemass,weight);
      hist("bkg12")->Fill(zprimemass,weight*QCDWeight( zprimemass, "mean", "nominal"));
      hist("bkg12up")->Fill(zprimemass,weight*QCDWeight( zprimemass, "mean", "up"));
      hist("bkg12down")->Fill(zprimemass,weight*QCDWeight( zprimemass, "mean", "down"));
      if (getMaxCSV(the_top)>0.890)
      {
        hist("antibcsvCRbtag_zprimemass")->Fill(zprimemass,weight);
        hist("bkg2")->Fill(zprimemass,weight*QCDWeight( zprimemass, "2", "nominal"));
        hist("bkg2up")->Fill(zprimemass,weight*QCDWeight( zprimemass, "2", "up"));
        hist("bkg2down")->Fill(zprimemass,weight*QCDWeight( zprimemass, "2", "down"));
      }
      else
      {
        hist("antibcsvCRnobtag_zprimemass")->Fill(zprimemass,weight);
        hist("bkg1")->Fill(zprimemass,weight*QCDWeight( zprimemass, "1", "nominal"));
        hist("bkg1up")->Fill(zprimemass,weight*QCDWeight( zprimemass, "1", "up"));
        hist("bkg1down")->Fill(zprimemass,weight*QCDWeight( zprimemass, "1", "down"));
      }
    }
  }




  Jet the_b_antibpt;
  bool has_twantibpt=false;
  if (has_tw) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8&&deltaR(jet,the_w)>0.8 && jet.pt()<100.0)
  {
        the_b_antibpt=jet; has_twantibpt=true;
        break;
  }
  if (has_twantibpt)
  {
    float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b_antibpt);
    hist("antibptCR_zprimemass")->Fill(zprimemass,weight);
    if (TprimeMass(the_w,the_b_antibpt)>500.0)
    {
      hist("antibptCRmass_zprimemass")->Fill(zprimemass,weight);
      if (getMaxCSV(the_top)>0.890)
      {
        hist("antibptCRbtag_zprimemass")->Fill(zprimemass,weight);
      }
      else
      {
        hist("antibptCRnobtag_zprimemass")->Fill(zprimemass,weight);
      }
    }
  }

  Jet the_b_antibmass;
  bool has_twantibmass=false;
  if (has_tw) for(auto jet : *event.jets)
  if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8&&deltaR(jet,the_w)>0.8 && jet.pt()>100.0&&JetMass(jet)>10.0)
  {
        the_b_antibmass=jet; has_twantibmass=true;
        break;
  }
  if (has_twantibmass)
  {
      float zprimemass=ZprimeMassVLQ(the_top,the_w,the_b_antibmass);
      hist("antibmassCR_zprimemass")->Fill(zprimemass,weight);
      if (TprimeMass(the_w,the_b_antibmass)>500.0)
      {
        hist("antibmassCRmass_zprimemass")->Fill(zprimemass,weight);
        if (getMaxCSV(the_top)>0.890)
        {
          hist("antibmassCRbtag_zprimemass")->Fill(zprimemass,weight);
        }
        else
        {
          hist("antibmassCRnobtag_zprimemass")->Fill(zprimemass,weight);
        }
      }
  }

}

SelectionHists::~SelectionHists(){}