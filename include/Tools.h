#pragma once
#include "UHH2/core/include/Event.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include "TF1.h"
#include "TH1F.h"
#include "TRandom3.h"

using namespace uhh2;
bool TopTag(TopJet topjet);
bool AntiTopTag(TopJet topjet);
float getHT50(const Event & event);
float getHTAK8(const Event & event);
float getMaxTopJetPt(const Event & event);
float getMaxTopJetMass(const Event & event);
float TopJetMass(TopJet topjet);
float TopJetPt(TopJet topjet);
float TopJetMass2(TopJet topjet);
float TopJetPt2(TopJet topjet);
float ZprimeMass(TopJet t1, TopJet t2);
float ZprimeMass2(TopJet t1, TopJet t2);
float TopJetNsub(TopJet t);
float getMaxCSV(TopJet t);
float getMmin(TopJet topjet);
float deltaY(TopJet j1,TopJet j2);
float deltaPhi(Particle j1,Particle j2);
float deltaR(Particle p1, Particle p2);
bool isGoodZprimeCandidate(TopJet t1, TopJet t2);
bool isDiTopjetEvent(const Event & event);
int match2GenTopJet(GenTopJet gen, const Event & event);
float TopJetMass(GenTopJet topjet);
float TopJetPt(GenTopJet topjet);
float ZprimeMass(GenTopJet t1, GenTopJet t2);
float TopJetEta(TopJet topjet);
float TopJetEta(GenTopJet topjet);
struct HigherPt {
    bool operator() (const Particle& j1, const Particle& j2) const {
        return j1.pt() > j2.pt();
    };
};
enum E_BtagType {
    e_CSVT, /**< Combined Secondary Vertex tagger, tight working point */
    e_CSVM, /**< Combined Secondary Vertex tagger, medium working point */
    e_CSVL, /**< Combined Secondary Vertex tagger, loose working point */
    e_JPT,  /**< Jet Probability tagger, tight working point */
    e_JPM, /**< Jet Probability tagger, medium working point */
    e_JPL /**< Jet Probability tagger, loose working point */
};
int subJetBTag(TopJet topjet, E_BtagType type, TString mode="default",TString filename="");
