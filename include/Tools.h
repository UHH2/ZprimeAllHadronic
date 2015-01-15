#pragma once
#include "UHH2/core/include/Event.h"
#include "TLorentzVector.h"
using namespace uhh2;
float getHT50(Event & event);
float getHTAK8(Event & event);
float getMaxTopJetPt(Event & event);
float getMaxTopJetMass(Event & event);
float TopJetMass(TopJet topjet);
float TopJetPt(TopJet topjet);
float ZprimeMass(Topjet t1, Topjet t2);


//int subJetBTag(TopJet topjet, E_BtagType type, TString mode="default",TString filename="");
float getMaxCSV(TopJet t);
