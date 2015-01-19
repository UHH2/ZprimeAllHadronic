#include "UHH2/Zp2TopVLQAllHad/include/Zp2TopVLQAllHadHists.h"
#include "UHH2/core/include/Event.h"

#include "TH1F.h"
#include "TH2F.h"
#include "TH3F.h"
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
  book<TH1F>("Nevts", "Nevts", 1, 0, 1);
  //njet ntopjet
  book<TH1F>("N_jets", "N_{jets}", 20, 0, 20);
  book<TH1F>("N_topjets", "N_{topjets}", 10, 0, 10);
  //mass1 mass2 mass1+2 AK8 CA8 CA15 CMS HEP
  book<TH1F>("m1AK8", "m_{1,AK8}", 200, 0, 2000);
  book<TH1F>("m2AK8", "m_{2,AK8}", 200, 0, 2000);
  book<TH1F>("m12AK8", "m_{1,AK8}+m_{2,AK8}", 200, 0, 6000);
  
  book<TH1F>("m1CA8", "m_{1,CA8}", 200, 0, 2000);
  book<TH1F>("m2CA8", "m_{2,CA8}", 200, 0, 2000);
  book<TH1F>("m12CA8", "m_{1,CA8}+m_{2,CA8}", 200, 0, 6000);
  
  book<TH1F>("m1CA15", "m_{1,CA15}", 200, 0, 2000);
  book<TH1F>("m2CA15", "m_{2,CA15}", 200, 0, 2000);
  book<TH1F>("m12CA15", "m_{1,CA15}+m_{2,CA15}", 200, 0, 6000);
  
  book<TH1F>("m1CMS", "m_{1,CMS}", 200, 0, 2000);
  book<TH1F>("m2CMS", "m_{2,CMS}", 200, 0, 2000);
  book<TH1F>("m12CMS", "m_{1,CMS}+m_{2,CMS}", 200, 0, 6000);
  
  book<TH1F>("m1HEP", "m_{1,HEP}", 200, 0, 2000);
  book<TH1F>("m2HEP", "m_{2,HEP}", 200, 0, 2000);
  book<TH1F>("m12HEP", "m_{1,HEP}+m_{2,HEP}", 200, 0, 6000);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  book<TH1F>("pT1AK8", "pT_{1,AK8}", 200, 0, 2000);
  book<TH1F>("pT2AK8", "pT_{2,AK8}", 200, 0, 2000);
  book<TH1F>("pT12AK8", "pT_{1,AK8}+pT_{2,AK8}", 200, 0, 6000);
  
  book<TH1F>("pT1CA8", "pT_{1,CA8}", 200, 0, 2000);
  book<TH1F>("pT2CA8", "pT_{2,CA8}", 200, 0, 2000);
  book<TH1F>("pT12CA8", "pT_{1,CA8}+pT_{2,CA8}", 200, 0, 6000);
  
  book<TH1F>("pT1CA15", "pT_{1,CA15}", 200, 0, 2000);
  book<TH1F>("pT2CA15", "pT_{2,CA15}", 200, 0, 2000);
  book<TH1F>("pT12CA15", "pT_{1,CA15}+pT_{2,CA15}", 200, 0, 6000);
  
  book<TH1F>("pT1CMS", "pT_{1,CMS}", 200, 0, 2000);
  book<TH1F>("pT2CMS", "pT_{2,CMS}", 200, 0, 2000);
  book<TH1F>("pT12CMS", "pT_{1,CMS}+pT_{2,CMS}", 200, 0, 6000);
  
  book<TH1F>("pT1HEP", "pT_{1,HEP}", 200, 0, 2000);
  book<TH1F>("pT2HEP", "pT_{2,HEP}", 200, 0, 2000);
  book<TH1F>("pT12HEP", "pT_{1,HEP}+pT_{2,HEP}", 200, 0, 6000);
  
  //HT50
  book<TH1F>("HT", "HT_{50}", 200, 0, 10000);
  //deltaPhi(1,2) deltaY(1,2) eta1 eta2
  book<TH1F>("deltaPhi", "#Delta(#phi)", 100, -4, 4);
  book<TH1F>("deltaY", "#Delta(y)", 100, -4, 4);
  book<TH1F>("eta_1", "#eta_{1}", 100, -4, 4);
  book<TH1F>("eta_2", "#eta_{2}", 100, -4, 4);
  //nsub1 nsub2
  book<TH1F>("nsub_1", "#tau_{3}/#tau_{2} 1", 100, 0, 1.1);
  book<TH1F>("nsub_2", "#tau_{3}/#tau_{2} 2", 100, 0, 1.1);
  //maxcsv1 maxcsv2
  book<TH1F>("csv_1", "CSV_{1}", 100, 0, 1.1);
  book<TH1F>("csv_2", "CSV_{2}", 100, 0, 1.1);
  //mistag matrix 2d 3d
  double csv_bins[] = {-100.0,0.0,0.244,0.679,10.0};
  double mistag_pt_bins[] = {150.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0,360.0,380.0,400.0,450.0,500.0,600.0,800.0,2000.0};
  double nsub_bins[] = {0.0,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2};
  book<TH2F>( "mistag2D", ";pT;CSV", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins);
  book<TH3F>( "mistag3D", ";pT;CSV;nsub", sizeof(mistag_pt_bins)/sizeof(double)-1,mistag_pt_bins, sizeof(csv_bins)/sizeof(double)-1, csv_bins,sizeof(nsub_bins)/sizeof(double)-1, nsub_bins);
  //mmin ndau
  book<TH1F>("mmin1", "Minimum pairwise mass 1", 200, 0, 100);
  book<TH1F>("ndau1", "Number of daughters 1", 6, 0, 6);
  book<TH1F>("mmin2", "Minimum pairwise mass 2", 200, 0, 100);
  book<TH1F>("ndau2", "Number of daughters 2", 6, 0, 6);
  
  // leptons
//   book<TH1F>("N_mu", "N^{#mu}", 10, 0, 10);
//   book<TH1F>("pt_mu", "p_{T}^{#mu} [GeV/c]", 40, 0, 200);
//   book<TH1F>("eta_mu", "#eta^{#mu}", 40, -2.1, 2.1);
//   book<TH1F>("reliso_mu", "#mu rel. Iso", 40, 0, 0.5);

  // primary vertices
  book<TH1F>("N_pv", "N^{PV}", 50, 0, 50);
}


void Zp2TopVLQAllHadHists::fill(const Event & event){
  // fill the histograms. Please note the comments in the header file:
  // 'hist' is used here a lot for simplicity, but it will be rather
  // slow when you have many histograms; therefore, better
  // use histogram pointers as members as in 'UHH2/common/include/ElectronHists.h'
  
  // Don't forget to always use the weight when filling.
  double weight = event.weight;
  
  
  
  
  
    //n
  hist("Nevts")->Fill(0.5,weight);
  //njet ntopjet
  hist("N_jets")->Fill(event.jets->size(),weight);
  hist("N_topjets")->Fill(event.topjets->size(),weight);
  //mass1 mass2 mass1+2 AK8 CA8 CA15 CMS HEP
  if (event.jetsAK8->size()>0) if (event.jetsAK8->at(0).v4().isTimelike()) hist("m1AK8")->Fill(event.jetsAK8->at(0).v4().M(),weight);
  if (event.jetsAK8->size()>1) if (event.jetsAK8->at(1).v4().isTimelike()) hist("m2AK8")->Fill(event.jetsAK8->at(1).v4().M(),weight);
  if (event.jetsAK8->size()>1) if ((event.jetsAK8->at(0).v4()+event.jetsAK8->at(1).v4()).isTimelike()) hist("m12AK8")->Fill((event.jetsAK8->at(0).v4()+event.jetsAK8->at(1).v4()).M(),weight);
  
  if (event.topjetsCA8->size()>0) hist("m1CA8")->Fill(TopJetMass(event.topjetsCA8->at(0)),weight);
  if (event.topjetsCA8->size()>1) hist("m2CA8")->Fill(TopJetMass(event.topjetsCA8->at(1)),weight);
  if (event.topjetsCA8->size()>1) hist("m12CA8")->Fill(ZprimeMass(event.topjetsCA8->at(0),event.topjetsCA8->at(1)),weight);
  
  if (event.topjetsCA15->size()>0) hist("m1CA15")->Fill(TopJetMass(event.topjetsCA15->at(0)),weight);
  if (event.topjetsCA15->size()>1) hist("m2CA15")->Fill(TopJetMass(event.topjetsCA15->at(1)),weight);
  if (event.topjetsCA15->size()>1) hist("m12CA15")->Fill(ZprimeMass(event.topjetsCA15->at(0),event.topjetsCA15->at(1)),weight);
  
  if (event.topjets->size()>0) hist("m1CMS")->Fill(TopJetMass(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("m2CMS")->Fill(TopJetMass(event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("m12CMS")->Fill(ZprimeMass(event.topjets->at(0),event.topjets->at(1)),weight);
  
  if (event.topjetsHEP->size()>0) hist("m1HEP")->Fill(TopJetMass(event.topjetsHEP->at(0)),weight);
  if (event.topjetsHEP->size()>1) hist("m2HEP")->Fill(TopJetMass(event.topjetsHEP->at(1)),weight);
  if (event.topjetsHEP->size()>1) hist("m12HEP")->Fill(ZprimeMass(event.topjetsHEP->at(0),event.topjetsHEP->at(1)),weight);
  
  //pt1 pt2 pt1+2 AK8 CA8 CA15 CMS HEP
  if (event.jetsAK8->size()>0) hist("pT1AK8")->Fill(event.jetsAK8->at(0).pt(),weight);
  if (event.jetsAK8->size()>1) hist("pT2AK8")->Fill(event.jetsAK8->at(1).pt(),weight);
  if (event.jetsAK8->size()>1) hist("pT12AK8")->Fill(event.jetsAK8->at(0).pt()+event.jetsAK8->at(1).pt(),weight);
  
  if (event.topjetsCA8->size()>0) hist("pT1CA8")->Fill(TopJetPt(event.topjetsCA8->at(0)),weight);
  if (event.topjetsCA8->size()>1) hist("pT2CA8")->Fill(TopJetPt(event.topjetsCA8->at(1)),weight);
  if (event.topjetsCA8->size()>1) hist("pT12CA8")->Fill(TopJetPt(event.topjetsCA8->at(0))+TopJetPt(event.topjetsCA8->at(1)),weight);
  
  if (event.topjetsCA15->size()>0) hist("pT1CA15")->Fill(TopJetPt(event.topjetsCA15->at(0)),weight);
  if (event.topjetsCA15->size()>1) hist("pT2CA15")->Fill(TopJetPt(event.topjetsCA15->at(1)),weight);
  if (event.topjetsCA15->size()>1) hist("pT12CA15")->Fill(TopJetPt(event.topjetsCA15->at(0))+TopJetPt(event.topjetsCA15->at(1)),weight);
  
  if (event.topjets->size()>0) hist("pT1CMS")->Fill(TopJetPt(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("pT2CMS")->Fill(TopJetPt(event.topjets->at(1)),weight);
  if (event.topjets->size()>1) hist("pT12CMS")->Fill(TopJetPt(event.topjets->at(0))+TopJetPt(event.topjets->at(1)),weight);
  
  if (event.topjetsHEP->size()>0) hist("pT1HEP")->Fill(TopJetPt(event.topjetsHEP->at(0)),weight);
  if (event.topjetsHEP->size()>1) hist("pT2HEP")->Fill(TopJetPt(event.topjetsHEP->at(1)),weight);
  if (event.topjetsHEP->size()>1) hist("pT12HEP")->Fill(TopJetPt(event.topjetsHEP->at(0))+TopJetPt(event.topjetsHEP->at(1)),weight);
  
  //HT50
  hist("HT")->Fill(getHT50(event),weight);
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
  //mistag matrix 2d 3d
  //hist( "mistag2D")->Fill(,weight);
  //hist( "mistag3D")->Fill(,weight);
  //mmin ndau
  if (event.topjets->size()>0) hist("mmin1")->Fill(getMmin(event.topjets->at(0)),weight);
  if (event.topjets->size()>0) hist("ndau1")->Fill(event.topjets->at(0).numberOfDaughters(),weight);
  if (event.topjets->size()>1) hist("mmin2")->Fill(getMmin(event.topjets->at(0)),weight);
  if (event.topjets->size()>1) hist("ndau2")->Fill(event.topjets->at(1).numberOfDaughters(),weight);
  
  
  
  
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
  
  int Npvs = event.pvs->size();
  hist("N_pv")->Fill(Npvs, weight);
}

Zp2TopVLQAllHadHists::~Zp2TopVLQAllHadHists(){}
