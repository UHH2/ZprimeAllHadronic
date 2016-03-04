#pragma once
#include "UHH2/core/include/Event.h"
#include "TLorentzVector.h"
#include "TFile.h"
#include "TF1.h"
#include "TH1F.h"
#include "TRandom3.h"
#include "UHH2/core/include/AnalysisModule.h"
#include "UHH2/common/include/JetCorrections.h"
#include "UHH2/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "UHH2/common/include/TopJetIds.h"
#include "UHH2/common/include/TTbarGen.h"
#include <string>

using namespace uhh2;
using namespace std;
bool TopTag(TopJet topjet);
bool WTag(TopJet topjet);
bool AntiTopTag(TopJet topjet);
bool AntiTopTag_mass(TopJet topjet);
bool AntiTopTag_nsub(TopJet topjet);
bool AntiWTag_mass(TopJet topjet);
bool AntiWTag_nsub(TopJet topjet);
bool SemiTopTag_mass(TopJet topjet);
bool SemiTopTag_nsub(TopJet topjet);
bool SemiWTag_mass(TopJet topjet);
bool SemiWTag_nsub(TopJet topjet);
bool TopTag_nopt(TopJet topjet);
bool WTag_nopt(TopJet topjet);
float getHT50(const Event & event);
float getHTCA8(const Event & event);
float getMaxTopJetPt(const Event & event);
float getMaxTopJetMass(const Event & event);
float TopJetMass(TopJet topjet);
float JetMass(Jet jet);
float TopJetPt(TopJet topjet);
float TopJetMass2(Particle topjet);
float TopJetPt2(Particle topjet);
float ZprimeMass(TopJet t1, TopJet t2);
float ZprimePt(TopJet t1, TopJet t2);
float TprimeMass(TopJet t1, Jet t2);
float TprimePt(TopJet t1, Jet t2);
float ZprimeMassVLQ(TopJet t1, TopJet t2, Jet t3);
float ZprimeMassResVLQ(TopJet t1, TopJet t2, Jet t3, Jet t4);
float ZprimePtVLQ(TopJet t1, TopJet t2, Jet t3);
float ZprimePtResVLQ(TopJet t1, TopJet t2, Jet t3, Jet t4);
float ZprimeMass2(Particle t1, Particle t2);
float TopJetNsub(TopJet t);
float TopJetNsub2(TopJet t);
float getMaxCSV(TopJet t);
float getMmin(TopJet topjet);
float deltaY(TopJet j1,TopJet j2);
float deltaPhi(Particle j1,Particle j2);
float deltaR(Particle p1, Particle p2);
bool isGoodZprimeCandidate(TopJet t1, TopJet t2);
bool isDiTopjetEvent(const Event & event);
int match2GenTopJet(GenTopJet gen, const Event & event);
int match2GenJet(Particle gen, const Event & event);
float TopJetMass(GenTopJet topjet);
float TopJetPt(GenTopJet topjet);
float ZprimeMass(GenTopJet t1, GenTopJet t2);
float TopJetEta(TopJet topjet);
float TopJetEta(GenTopJet topjet);
LorentzVector getAK4FromTopJet(const Event & event, TopJet t, unsigned int njets, float r);
float TopJetMassAK4(const Event & event, TopJet t, unsigned int njets, float r);
float ZprimeMassAK4(const Event & event, TopJet t1, TopJet t2, unsigned int njets, float r);
void uncorrect_topjets(const Event & event);
std::pair<TopJet, TopJet> findTopWpair(	bool (*ttag)(TopJet), bool (*wtag)(TopJet), TopJet first, TopJet second);

float TopTagSF(const Event & event, TopJet jet, int sys);
float WTagSF(const Event & event, TopJet jet, int sys);
bool contains(string s, string substring);

struct HigherPt {
    bool operator() (const Particle& j1, const Particle& j2) const {
        return j1.pt() > j2.pt();
    };
};

float QCDWeight(float mzp, string mode = "mean", string syst = "nominal");
float TTbarWeight(const Event & event, int syst = 0);
//enum E_BtagType {
//    e_CSVT, /**< Combined Secondary Vertex tagger, tight working point */
//    e_CSVM, /**< Combined Secondary Vertex tagger, medium working point */
//    e_CSVL, /**< Combined Secondary Vertex tagger, loose working point */
//    e_JPT,  /**< Jet Probability tagger, tight working point */
//    e_JPM, /**< Jet Probability tagger, medium working point */
//    e_JPL /**< Jet Probability tagger, loose working point */
//};



// e(B) = 0.1% SD WP1	0.1%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.44
// e(B) = 0.1% SD WP2	0.1%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.54, max SD subjet b-discriminant > 0.79

// e(B) = 0.3% SD WP1	0.3%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.50
// e(B) = 0.3% SD WP2	0.3%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.61, max SD subjet b-discriminant > 0.76

// e(B) = 1% SD WP1	1%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.59
// e(B) = 1% SD WP2	1%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.69, max SD subjet b-discriminant > 0.66

// e(B) = 3% SD WP1	3%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.69
// e(B) = 3% SD WP2	3%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.75, max SD subjet b-discriminant > 0.39

// e(B) = 10% SD WP1	10%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.86
// e(B) = 10% SD WP2	10%	 	SD(β=0,z=0.1, R=0.8) [110,210]	tau32 < 0.87, max SD subjet b-discriminant > 0.089



class SDTopTag {
public:
  
  enum class WP {
	Mis0p1,
	Mis0p1b,
	Mis0p3,
	Mis0p3b,
	Mis1,
	Mis1b,
	Mis3,
	Mis3b,
	Mis10,
	Mis10b
};

  explicit SDTopTag(WP WorkingPoint = WP::Mis0p1);
  
  bool operator()(const TopJet & topjet, const uhh2::Event & event) const;
 

 private:
  WP m_WP;
};



