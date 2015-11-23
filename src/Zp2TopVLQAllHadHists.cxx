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


SelectionHists::SelectionHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  h_topjetsAK8 = ctx.get_handle<std::vector<TopJet> >("patJetsAk8CHSJetsSoftDropPacked_daughters");
  h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked_daughters");

  book<TH1F>("N_toptags", ";N_{toptags};Events", 10, 0, 10);
  book<TH1F>("N_wtags", ";N_{wtags};Events", 10, 0, 10);
  book<TH1F>("N_btags", ";N_{btags};Events", 10, 0, 10);
  book<TH1F>("N_subjetbtags", ";N_{subjetbtags};Events", 10, 0, 10);

  book<TH1F>("pTtop", ";p_{T} top gen;Events", 300, 0, 3000);
  book<TH1F>("pTtprime", ";p_{T} T' gen;Events", 300, 0, 3000);
  book<TH1F>("pTb", ";p_{T} b gen;Events", 300, 0, 3000);
  book<TH1F>("pTw", ";p_{T} W gen;Events", 300, 0, 3000);
  book<TH1F>("pTzprime", ";p_{T} Z' gen;Events", 300, 0, 3000);

  book<TH1F>("ptop", ";p top gen;Events", 300, 0, 3000);
  book<TH1F>("ptprime", ";p T' gen;Events", 300, 0, 3000);
  book<TH1F>("pb", ";p b gen;Events", 300, 0, 3000);
  book<TH1F>("pw", ";p W gen;Events", 300, 0, 3000);
  book<TH1F>("pzprime", ";p Z' gen;Events", 300, 0, 3000);

  book<TH1F>("mtop", ";M top gen;Events", 300, 0, 3000);
  book<TH1F>("mtprime", ";M T' gen;Events", 300, 0, 3000);
  book<TH1F>("mb", ";M b gen;Events", 300, 0, 3000);
  book<TH1F>("mw", ";M W gen;Events", 300, 0, 3000);
  book<TH1F>("mzprime", ";M Z' gen;Events", 300, 0, 3000);

  book<TH1F>("dRbW", ";#Delta R(b,W);Events", 500, 0, 5);
  book<TH1F>("dRtT", ";#Delta R(t,T');Events", 500, 0, 5);
  book<TH1F>("dRbt", ";#Delta R(b,t);Events", 500, 0, 5);
  book<TH1F>("dRtW", ";#Delta R(t,W);Events", 500, 0, 5);

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

  book<TH1F>("step1_wmass", ";step1: mass w candidate;Events", 100, 0, 1000);
  book<TH1F>("step1_wnsub", ";step1: nsub w candidate;Events", 100, 0, 1);
  book<TH1F>("step1_tcsv", ";step1: csv t candidate;Events", 100, 0, 1);
  book<TH1F>("step1_tpt", ";step1: pt t candidate;Events", 300, 0, 3000);
  book<TH1F>("step2_bcsv", ";step2: csv b candidate;Events", 100, 0, 1);
  book<TH1F>("step2_wpt", ";step2: pt w candidate;Events", 300, 0, 3000);
  book<TH1F>("step3_tprimemass", ";step3: mass tprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step3_tprimept", ";step3: pt tprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemass", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemassbtag", ";step4: mass zprime candidate;Events", 300, 0, 3000);
  book<TH1F>("step4_zprimemassbtagnsub", ";step4: mass zprime candidate;Events", 300, 0, 3000);

}

void SelectionHists::fill(const Event & event){
    double weight = event.weight;
  
  //get extra jet collections
  //const auto jetsAK8 = &event.get(h_jetsAK8);
  const auto topjetsAK8 = &event.get(h_topjetsAK8);
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
  for(auto topjet : *topjetsAK8)
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

  GenParticle the_gen_top,the_gen_tprime,the_gen_w,the_gen_b;
  bool has_gen_top=false,has_gen_tprime=false,has_gen_w=false,has_gen_b=false;
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
        }
        if(abs(the_gen_b.pdgId()) == 5)
        {
          hist("pTb")->Fill(the_gen_b.pt(),weight);
          hist("pb")->Fill(the_gen_b.v4().P(),weight);
          hist("mb")->Fill(the_gen_b.v4().M(),weight);
          has_gen_b=true;
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

  TopJet the_closest_top,the_closest_w,the_closest_tprime; Jet the_closest_b;
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
    for(auto topjet : *topjetsAK8)
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
        for(auto topjet : *topjetsAK8)
        {
            if(deltaR(topjet,the_top)>0.8 && !found)
            {
              hist("step1_wmass")->Fill(TopJetMass(topjet),weight);
              hist("step1_wnsub")->Fill(TopJetNsub2(topjet),weight);
              found=true;
            }
            if (WTag(topjet)&&deltaR(topjet,the_top)>0.8)
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
            if (jet.btag_combinedSecondaryVertex()>0.890&&deltaR(jet,the_top)>0.8 && jet.pt()>200.0)
            {
                the_b=jet;
                has_the_b=true;
                hist("step3_tprimemass")->Fill(TprimeMass(the_w,the_b),weight);
                hist("step3_tprimept")->Fill(TprimePt(the_w,the_b),weight);
                break;
            }
        }
    }
    if (has_the_b && has_the_w && has_the_top && TprimeMass(the_w,the_b)>700.0)
    {
      hist("step4_zprimemass")->Fill(ZprimeMassVLQ(the_top,the_w,the_b),weight);
      if (getMaxCSV(the_top)>0.890) hist("step4_zprimemassbtag")->Fill(ZprimeMassVLQ(the_top,the_w,the_b),weight);
      if (getMaxCSV(the_top)>0.890 && TopJetNsub(the_top)<0.7) hist("step4_zprimemassbtagnsub")->Fill(ZprimeMassVLQ(the_top,the_w,the_b),weight);
    }

}

SelectionHists::~SelectionHists(){}


TriggerHists::TriggerHists(Context & ctx, const string & dirname): Hists(ctx, dirname){
  book<TH1F>("HT", ";HT_{50};Events", 200, 0, 10000);
  book<TH1F>("HTCA8", ";HT_{CA8};Events", 200, 0, 10000);
}
void TriggerHists::fill(const Event & event){
  double weight = event.weight;
  double HT50=getHT50(event);
  double HTCA8=getHTCA8(event);
  hist("HT")->Fill(HT50,weight);
  hist("HTCA8")->Fill(HTCA8,weight);
}
TriggerHists::~TriggerHists(){

}
