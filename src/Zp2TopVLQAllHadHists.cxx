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
  book<TH1F>("m1AK8", ";m_{1,AK8};Events", 200, 0, 2000);
  book<TH1F>("m2AK8", ";m_{2,AK8};Events", 200, 0, 2000);
  book<TH1F>("m12AK8", ";m_{12,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("m1CA8", ";m_{1,CA8};Events", 200, 0, 2000);
  book<TH1F>("m2CA8", ";m_{2,CA8};Events", 200, 0, 2000);
  book<TH1F>("m12CA8", ";m_{12,CA8};Events", 240, 0, 6000);
  
  book<TH1F>("m1CA15", ";m_{1,CA15};Events", 200, 0, 2000);
  book<TH1F>("m2CA15", ";m_{2,CA15};Events", 200, 0, 2000);
  book<TH1F>("m12CA15", ";m_{12,CA15};Events", 240, 0, 6000);
  
  book<TH1F>("m1CMS", ";m_{1,CMS};Events", 200, 0, 2000);
  book<TH1F>("m2CMS", ";m_{2,CMS};Events", 200, 0, 2000);
  book<TH1F>("m12CMS", ";m_{12,CMS};Events", 240, 0, 6000);

  book<TH1F>("m1CMSfat", ";m_{1,CMS};Events", 200, 0, 2000);
  book<TH1F>("m2CMSfat", ";m_{2,CMS};Events", 200, 0, 2000);
  book<TH1F>("m12CMSfat", ";m_{12,CMS};Events", 240, 0, 6000);

  book<TH1F>("m1gen", ";m_{1,gen};Events", 200, 0, 2000);
  book<TH1F>("m2gen", ";m_{2,gen};Events", 200, 0, 2000);
  book<TH1F>("m12gen", ";m_{12,gen};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x3R8", ";m_{1,AK4x3R8};Events", 200, 0, 2000);
  book<TH1F>("m2AK4x3R8", ";m_{2,AK4x3R8};Events", 200, 0, 2000);
  book<TH1F>("m12AK4x3R8", ";m_{12,AK4x3R8};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x4R8", ";m_{1,4x4R8};Events", 200, 0, 2000);
  book<TH1F>("m2AK4x4R8", ";m_{2,4x4R8};Events", 200, 0, 2000);
  book<TH1F>("m12AK4x4R8", ";m_{12,AK4x4R8};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x3R15", ";m_{1,AK4x3R15};Events", 200, 0, 2000);
  book<TH1F>("m2AK4x3R15", ";m_{2,AK4x3R15};Events", 200, 0, 2000);
  book<TH1F>("m12AK4x3R15", ";m_{12,AK4x3R15};Events", 240, 0, 6000);

  book<TH1F>("m1AK4x4R15", ";m_{1,AK4x4R15};Events", 200, 0, 2000);
  book<TH1F>("m2AK4x4R15", ";m_{2,AK4x4R15};Events", 200, 0, 2000);
  book<TH1F>("m12AK4x4R15", ";m_{12,AK4x4R15};Events", 240, 0, 6000);
  
  book<TH1F>("m1HEP", ";m_{1,HEP};Events", 200, 0, 2000);
  book<TH1F>("m2HEP", ";m_{2,HEP};Events", 200, 0, 2000);
  book<TH1F>("m12HEP", ";m_{12,HEP};Events", 240, 0, 6000);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  book<TH1F>("pT1AK8", ";pT_{1,AK8};Events", 200, 0, 2000);
  book<TH1F>("pT2AK8", ";pT_{2,AK8};Events", 200, 0, 2000);
  book<TH1F>("pT12AK8", ";pT_{1,AK8}+pT_{2,AK8};Events", 240, 0, 6000);
  
  book<TH1F>("pT1CA8", ";pT_{1,CA8};Events", 200, 0, 2000);
  book<TH1F>("pT2CA8", ";pT_{2,CA8};Events", 200, 0, 2000);
  book<TH1F>("pT12CA8", ";pT_{1,CA8}+pT_{2,CA8};Events", 240, 0, 6000);
  
  book<TH1F>("pT1CA15", ";pT_{1,CA15};Events", 200, 0, 2000);
  book<TH1F>("pT2CA15", ";pT_{2,CA15};Events", 200, 0, 2000);
  book<TH1F>("pT12CA15", ";pT_{1,CA15}+pT_{2,CA15};Events", 240, 0, 6000);
  
  book<TH1F>("pT1CMS", ";pT_{1,CMS};Events", 200, 0, 2000);
  book<TH1F>("pT2CMS", ";pT_{2,CMS};Events", 200, 0, 2000);
  book<TH1F>("pT12CMS", ";pT_{1,CMS}+pT_{2,CMS};Events", 240, 0, 6000);
  
  book<TH1F>("pT1HEP", ";pT_{1,HEP};Events", 200, 0, 2000);
  book<TH1F>("pT2HEP", ";pT_{2,HEP};Events", 200, 0, 2000);
  book<TH1F>("pT12HEP", ";pT_{1,HEP}+pT_{2,HEP};Events", 240, 0, 6000);
  
  //HT50
  book<TH1F>("HT", ";HT_{50};Events", 200, 0, 10000);
  book<TH2F>("HT50vsNjet50", ";HT;N_{jets};Events", 20,0,5000,20, 0, 20);
  //deltaPhi(1,2) deltaY(1,2) eta1 eta2
  book<TH1F>("deltaPhi", ";#Delta(#phi);Events", 100, -4, 4);
  book<TH1F>("deltaY", ";#Delta(y);Events", 100, -4, 4);
  book<TH1F>("eta_1", ";#eta_{1};Events", 100, -4, 4);
  book<TH1F>("eta_2", ";#eta_{2};Events", 100, -4, 4);
  //nsub1 nsub2
  book<TH1F>("nsub_1", ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
  book<TH1F>("nsub_2", ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
  //maxcsv1 maxcsv2
  book<TH1F>("csv_1", ";CSV_{1};Events", 100, 0, 1.1);
  book<TH1F>("csv_2", ";CSV_{2};Events", 100, 0, 1.1);
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
  h_jetsAK8 = ctx.get_handle<std::vector<Jet> >("patJetsCa8CHSJets");//, "slimmedJetsAK8");
  h_topjetsCA8 = ctx.get_handle<std::vector<TopJet> >("patJetsCa8CHSJetsPrunedPacked");//, "patJetsCA8CHSprunedPacked");
  h_topjetsCA15 = ctx.get_handle<std::vector<TopJet> >("patJetsCa15CHSJetsFilteredPacked");//, "patJetsCA15CHSFilteredPacked");
  h_topjetsHEP = ctx.get_handle<std::vector<TopJet> >("patJetsHepTopTagCHSPacked");//, "patJetsHEPTopTagCHSPacked");

  topjet_collection_names = {"patJetsHepTopTagCHSPacked", "patJetsCa8CHSJetsPrunedPacked", "patJetsCa15CHSJetsFilteredPacked", "patJetsHepTopTagPuppiPacked", "patJetsCmsTopTagPuppiPacked", "patJetsCa8PuppiJetsPrunedPacked", "patJetsCa15PuppiJetsFilteredPacked", "patJetsCa8CHSJetsSoftDropPacked", "patJetsCa8PuppiJetsSoftDropPacked"};//"patJetsCmsTopTagCHSPacked",
  jet_collection_names = {"patJetsCa15CHSJets", "patJetsCa8CHSJets", "patJetsCa15PuppiJets", "patJetsCa8PuppiJets"};
  for(auto collection_name : jet_collection_names)
  {
    jet_handles.push_back(ctx.get_handle<std::vector<Jet> >(collection_name));
  }
  for(auto collection_name : topjet_collection_names)
  {
    topjet_handles.push_back(ctx.get_handle<std::vector<TopJet> >(collection_name));
  }

  for(auto collection_name : jet_collection_names)
  {
    book<TH1F>("N_"+collection_name, ";N_{topjets};Events", 10, 0, 10);
    book<TH1F>("m1_"+collection_name, ";m_{1};Events", 200, 0, 2000);
    book<TH1F>("m2_"+collection_name, ";m_{2};Events", 200, 0, 2000);
    book<TH1F>("m12_"+collection_name, ";m_{12};Events", 240, 0, 6000);
    book<TH1F>("pT1_"+collection_name, ";pT_{1};Events", 200, 0, 2000);
    book<TH1F>("pT2_"+collection_name, ";pT_{2};Events", 200, 0, 2000);
    book<TH1F>("nsub1_"+collection_name, ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
    book<TH1F>("nsub2_"+collection_name, ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
    book<TH1F>("csv1_"+collection_name, ";CSV_{1};Events", 100, 0, 1.1);
    book<TH1F>("csv2_"+collection_name, ";CSV_{2};Events", 100, 0, 1.1);
  }

  for(auto collection_name : topjet_collection_names)
  {
    book<TH1F>("N_"+collection_name, ";N_{topjets};Events", 10, 0, 10);
    book<TH1F>("m1_"+collection_name, ";m_{1};Events", 200, 0, 2000);
    book<TH1F>("m2_"+collection_name, ";m_{2};Events", 200, 0, 2000);
    book<TH1F>("m12_"+collection_name, ";m_{12};Events", 240, 0, 6000);
    book<TH1F>("pT1_"+collection_name, ";pT_{1};Events", 200, 0, 2000);
    book<TH1F>("pT2_"+collection_name, ";pT_{2};Events", 200, 0, 2000);
    book<TH1F>("nsub1_"+collection_name, ";#tau_{3}/#tau_{2} 1;Events", 100, 0, 1.1);
    book<TH1F>("nsub2_"+collection_name, ";#tau_{3}/#tau_{2} 2;Events", 100, 0, 1.1);
    book<TH1F>("csv1_"+collection_name, ";CSV_{1};Events", 100, 0, 1.1);
    book<TH1F>("csv2_"+collection_name, ";CSV_{2};Events", 100, 0, 1.1);
  }

}


void Zp2TopVLQAllHadHists::fill(const Event & event){
  // fill the histograms. Please note the comments in the header file:
  // 'hist' is used here a lot for simplicity, but it will be rather
  // slow when you have many histograms; therefore, better
  // use histogram pointers as members as in 'UHH2/common/include/ElectronHists.h'
  
  // Don't forget to always use the weight when filling.
  double weight = event.weight;
  
  //get extra jet collections
  const auto jetsAK8 = &event.get(h_jetsAK8);
  const auto topjetsCA8 = &event.get(h_topjetsCA8);
  const auto topjetsCA15 = &event.get(h_topjetsCA15);
  const auto topjetsHEP = &event.get(h_topjetsHEP);

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
  if (jetsAK8->size()>0) if (jetsAK8->at(0).v4().isTimelike()) hist("m1AK8")->Fill(jetsAK8->at(0).v4().M(),weight);
  if (jetsAK8->size()>1) if (jetsAK8->at(1).v4().isTimelike()) hist("m2AK8")->Fill(jetsAK8->at(1).v4().M(),weight);
  if (jetsAK8->size()>1) if ((jetsAK8->at(0).v4()+jetsAK8->at(1).v4()).isTimelike()) hist("m12AK8")->Fill((jetsAK8->at(0).v4()+jetsAK8->at(1).v4()).M(),weight);
  
  if (topjetsCA8->size()>0) hist("m1CA8")->Fill(TopJetMass(topjetsCA8->at(0)),weight);
  if (topjetsCA8->size()>1) hist("m2CA8")->Fill(TopJetMass(topjetsCA8->at(1)),weight);
  if (topjetsCA8->size()>1) hist("m12CA8")->Fill(ZprimeMass(topjetsCA8->at(0),topjetsCA8->at(1)),weight);
  
  if (topjetsCA15->size()>0) hist("m1CA15")->Fill(TopJetMass(topjetsCA15->at(0)),weight);
  if (topjetsCA15->size()>1) hist("m2CA15")->Fill(TopJetMass(topjetsCA15->at(1)),weight);
  if (topjetsCA15->size()>1) hist("m12CA15")->Fill(ZprimeMass(topjetsCA15->at(0),topjetsCA15->at(1)),weight);
  
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

  if (topjetsHEP->size()>0) hist("m1HEP")->Fill(TopJetMass(topjetsHEP->at(0)),weight);
  if (topjetsHEP->size()>1) hist("m2HEP")->Fill(TopJetMass(topjetsHEP->at(1)),weight);
  if (topjetsHEP->size()>1) hist("m12HEP")->Fill(ZprimeMass(topjetsHEP->at(0),topjetsHEP->at(1)),weight);
  //if (event.topjets->size()>1) hist("m12HEP")->Fill(ZprimeMass22(event.topjets->at(0),event.topjets->at(1)),weight);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  if (jetsAK8->size()>0) hist("pT1AK8")->Fill(jetsAK8->at(0).pt(),weight);
  if (jetsAK8->size()>1) hist("pT2AK8")->Fill(jetsAK8->at(1).pt(),weight);
  if (jetsAK8->size()>1) hist("pT12AK8")->Fill(jetsAK8->at(0).pt()+jetsAK8->at(1).pt(),weight);
  
  if (topjetsCA8->size()>0) hist("pT1CA8")->Fill(TopJetPt(topjetsCA8->at(0)),weight);
  if (topjetsCA8->size()>1) hist("pT2CA8")->Fill(TopJetPt(topjetsCA8->at(1)),weight);
  if (topjetsCA8->size()>1) hist("pT12CA8")->Fill(TopJetPt(topjetsCA8->at(0))+TopJetPt(topjetsCA8->at(1)),weight);
  
  if (topjetsCA15->size()>0) hist("pT1CA15")->Fill(TopJetPt(topjetsCA15->at(0)),weight);
  if (topjetsCA15->size()>1) hist("pT2CA15")->Fill(TopJetPt(topjetsCA15->at(1)),weight);
  if (topjetsCA15->size()>1) hist("pT12CA15")->Fill(TopJetPt(topjetsCA15->at(0))+TopJetPt(topjetsCA15->at(1)),weight);
  
  if (event.topjets->size()>0) hist("pT1CMS")->Fill(TopJetPt(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("pT2CMS")->Fill(TopJetPt(event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("pT12CMS")->Fill(TopJetPt(event.topjets->at(0))+TopJetPt(event.topjets->at(1)),weight);
  
  if (topjetsHEP->size()>0) hist("pT1HEP")->Fill(TopJetPt(topjetsHEP->at(0)),weight);
  if (topjetsHEP->size()>1) hist("pT2HEP")->Fill(TopJetPt(topjetsHEP->at(1)),weight);
  if (topjetsHEP->size()>1) hist("pT12HEP")->Fill(TopJetPt(topjetsHEP->at(0))+TopJetPt(topjetsHEP->at(1)),weight);
  
  //HT50
  double HT50=getHT50(event);
  hist("HT")->Fill(HT50,weight);
  ((TH2F*)hist("HT50vsNjet50"))->Fill(HT50,njet50,weight);
  //deltaPhi(1,2)->Fill(,weight); deltaY(1,2)->Fill(,weight); eta1 eta2
  if (event.topjets->size()>1) hist("deltaPhi")->Fill(deltaPhi(event.topjets->at(0),event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("deltaY")->Fill(deltaY(event.topjets->at(0),event.topjets->at(1)),weight);
  if (event.topjets->size()>0) hist("eta_1")->Fill(event.topjets->at(0).eta(),weight);
  if (event.topjets->size()>1) hist("eta_2")->Fill(event.topjets->at(1).eta(),weight);
  //nsub1 nsub2
  if (event.topjets->size()>0) hist("nsub_1")->Fill(TopJetNsub(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("nsub_2")->Fill(TopJetNsub(event.topjets->at(1)),weight);
  //maxcsv1 maxcsv2
  if (event.topjets->size()>0) hist("csv_1")->Fill(getMaxCSV(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("csv_2")->Fill(getMaxCSV(event.topjets->at(1)),weight);
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
  
  
for(unsigned int i=0; i<jet_collection_names.size(); i++)
  {
    auto jets = &event.get(jet_handles[i]);
    hist(("N_"+jet_collection_names[i]).c_str())->Fill(jets->size(),weight);
    if (jets->size()>0) if (jets->at(0).v4().isTimelike()) hist(("m1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0).v4().M(),weight);
    if (jets->size()>1) if (jets->at(1).v4().isTimelike()) hist(("m2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1).v4().M(),weight);
    if (jets->size()>1) if ((jets->at(1).v4()+jets->at(0).v4()).isTimelike()) hist(("m12_"+jet_collection_names[i]).c_str())->Fill((jets->at(0).v4()+jets->at(1).v4()).M(),weight);
    if (jets->size()>0) hist(("pT1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0).pt(),weight);
    if (jets->size()>1) hist(("pT2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1).pt(),weight);
    // if (jets->size()>0) hist(("nsub1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0),weight);
    // if (jets->size()>1) hist(("nsub2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1),weight);
    // if (jets->size()>0) hist(("csv1_"+jet_collection_names[i]).c_str())->Fill(jets->at(0),weight);
    // if (jets->size()>1) hist(("csv2_"+jet_collection_names[i]).c_str())->Fill(jets->at(1),weight);
  }

for(unsigned int i=0; i<topjet_collection_names.size(); i++)
  {
    auto jets = &event.get(topjet_handles[i]);
    hist(("N_"+topjet_collection_names[i]).c_str())->Fill(jets->size(),weight);
    if (jets->size()>0) hist(("m1_"+topjet_collection_names[i]).c_str())->Fill(TopJetMass(jets->at(0)),weight);
    if (jets->size()>1) hist(("m2_"+topjet_collection_names[i]).c_str())->Fill(TopJetMass(jets->at(1)),weight);
    if (jets->size()>1) hist(("m12_"+topjet_collection_names[i]).c_str())->Fill(ZprimeMass(jets->at(0),jets->at(1)),weight);
    if (jets->size()>0) hist(("pT1_"+topjet_collection_names[i]).c_str())->Fill(TopJetPt(jets->at(0)),weight);
    if (jets->size()>1) hist(("pT2_"+topjet_collection_names[i]).c_str())->Fill(TopJetPt(jets->at(1)),weight);
    if (jets->size()>0) hist(("nsub1_"+topjet_collection_names[i]).c_str())->Fill(TopJetNsub(jets->at(0)),weight);
    if (jets->size()>1) hist(("nsub2_"+topjet_collection_names[i]).c_str())->Fill(TopJetNsub(jets->at(1)),weight);
    if (jets->size()>0) hist(("csv1_"+topjet_collection_names[i]).c_str())->Fill(getMaxCSV(jets->at(0)),weight);
    if (jets->size()>1) hist(("csv2_"+topjet_collection_names[i]).c_str())->Fill(getMaxCSV(jets->at(1)),weight);
  }

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
