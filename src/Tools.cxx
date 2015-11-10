#include "UHH2/ZprimeAllHadronic/include/Tools.h"

float deltaR(Particle p1, Particle p2)
{
  auto deltaeta = p1.eta() - p2.eta();
  auto dphi = deltaPhi(p1,p2);
  return sqrt(deltaeta * deltaeta + dphi * dphi);
}

float getHT50(const Event & event)
{
  float ht=0.0;
  for(auto jet : *event.jets)
    if (jet.pt()>=50.0) ht+=jet.pt();
  return ht;
}

float getHTCA8(const Event & event)
{
 if (event.topjets->size()>1) return event.topjets->at(0).pt() + event.topjets->at(1).pt();
 if (event.topjets->size()>0) return event.topjets->at(0).pt();
 return 0.0;
}

float TopJetMass(TopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float TopJetMass2(Particle topjet)
{
  if (topjet.v4().isTimelike()) return topjet.v4().M();
  else return 0.0;
}

float ZprimeMass(TopJet t1, TopJet t2)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float ZprimePt(TopJet t1, TopJet t2)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  return allsubjets.Pt();
}
float ZprimeMassVLQ(TopJet t1, TopJet t2, Jet t3)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  allsubjets += t3.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}
float ZprimePtVLQ(TopJet t1, TopJet t2, Jet t3)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  allsubjets += t3.v4();
  return allsubjets.Pt();
}

float TprimeMass(TopJet t1, Jet t2)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  allsubjets += t2.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}
float TprimePt(TopJet t1, Jet t2)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  allsubjets += t2.v4();
  return allsubjets.Pt();
}


float ZprimeMass2(Particle t1, Particle t2)
{
  LorentzVector allsubjets(0,0,0,0);
  allsubjets += t1.v4();
  allsubjets += t2.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float TopJetPt(TopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  return allsubjets.Pt();
}

float TopJetPt2(Particle topjet)
{
  return topjet.pt();
}

float getMaxTopJetMass(const Event & event)
{
  if  (event.topjets->size()==0) return 0.0;
  std::vector<float> valuelist;
  for(auto topjet : *event.topjets) valuelist.push_back(TopJetMass(topjet));
  if (valuelist.size()>0)
  return *std::max_element(valuelist.begin(),valuelist.end());
  else return 0;
}

float getMaxTopJetPt(const Event & event)
{
  if  (event.topjets->size()==0) return 0.0;
  std::vector<float> valuelist;
  for(auto topjet : *event.topjets) valuelist.push_back( TopJetPt(topjet) );
  if (valuelist.size()>0)
  return *std::max_element(valuelist.begin(),valuelist.end());
  else return 0;
}

float getMaxCSV(TopJet t)
{
  std::vector<float> csv;
  for (auto subjet : t.subjets()) csv.push_back(subjet.btag_combinedSecondaryVertex());
  if (csv.size()>0)
  return *max_element(std::begin(csv), std::end(csv));
  else return 0;
}

float TopJetNsub(TopJet t)
{
  return t.tau3()/t.tau2();
}

float TopJetNsub2(TopJet t)
{
  return t.tau2()/t.tau1();
}

float getMmin(TopJet topjet)
{
  auto nsubjets=topjet.subjets().size();
  float mmin=0;
  if(nsubjets>=3) {

        std::vector<Jet> subjets = topjet.subjets();
        sort(subjets.begin(), subjets.end(), HigherPt());

        double m01 = 0;
        if( (subjets[0].v4()+subjets[1].v4()).isTimelike())
            m01=(subjets[0].v4()+subjets[1].v4()).M();
        double m02 = 0;
        if( (subjets[0].v4()+subjets[2].v4()).isTimelike() )
            m02=(subjets[0].v4()+subjets[2].v4()).M();
        double m12 = 0;
        if( (subjets[1].v4()+subjets[2].v4()).isTimelike() )
            m12 = (subjets[1].v4()+subjets[2].v4()).M();

        //minimum pairwise mass
        mmin = std::min(m01,std::min(m02,m12));
    }
    return mmin;
}

float deltaY(TopJet j1,TopJet j2)
{
  return fabs(j1.v4().Rapidity()-j2.v4().Rapidity());
}
float deltaPhi(Particle j1,Particle j2)
{
    auto deltaphi = fabs(j1.phi() - j2.phi());
    if(deltaphi > M_PI) deltaphi = 2* M_PI - deltaphi;
    return fabs(deltaphi);
}

bool TopTag(TopJet topjet)
{
  if(TopJetPt(topjet)<400.0) return false;
  //number of subjets requirement
  if(topjet.subjets().size()<3) return false;
  //mass requirement
  auto mjet = TopJetMass(topjet);
  if(mjet<140 || mjet>250) return false;
  //minimum pairwise mass requirement
  if (getMmin(topjet)<50) return false;

  return true;
}

bool AntiTopTag(TopJet topjet)
{
  //number of subjets requirement
  if(topjet.subjets().size()<3) return false;
  //mass requirement
  auto mjet = TopJetMass(topjet);
  if(mjet<140 || mjet>250) return false;
  //minimum pairwise mass requirement
  if (getMmin(topjet)>50) return false;

  return true;
}

bool isGoodZprimeCandidate(TopJet t1, TopJet t2)
{
  return (TopJetPt(t1)>400) && 
  (TopJetPt(t2)>400) &&
  (TopTag(t1))&&
  (TopTag(t1))&&
  (deltaPhi(t1,t2)>2.1)&&
  (deltaY(t1,t2)<1.0);
}

bool isDiTopjetEvent(const Event & event)
{
  if (event.topjets->size()>1)
  {
    if ((TopJetPt(event.topjets->at(0))>300) && (TopJetPt(event.topjets->at(1))>300))
    {
      return true;
    }
  }
  return false;
}

int match2GenTopJet(GenTopJet gen, const Event & event)
{
  float deltar=0.8;
  int index=-1;
  for (unsigned int i=0;i<event.topjets->size();i++)
  {
    float current_deltar=deltaR(gen,event.topjets->at(i));
    if (current_deltar<deltar)
    {
      deltar=current_deltar;
      index=i;
    }
  }
  return index;
}

int match2GenJet(Particle gen, const Event & event)
{
  float deltar=0.4;
  int index=-1;
  for (unsigned int i=0;i<event.jets->size();i++)
  {
    float current_deltar=deltaR(gen,event.jets->at(i));
    if (current_deltar<deltar)
    {
      deltar=current_deltar;
      index=i;
    }
  }
  return index;
}

float TopJetMass(GenTopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float TopJetPt(GenTopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  return allsubjets.Pt();
}

float ZprimeMass(GenTopJet t1, GenTopJet t2)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float TopJetEta(TopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  return allsubjets.Eta();
}
float TopJetEta(GenTopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  return allsubjets.Eta();
}

LorentzVector getAK4FromTopJet(const Event & event, TopJet t, unsigned int njets, float r)
{
  std::vector<int> indices;
  std::vector<float> deltar;
  for (unsigned int i=0;i<njets;i++)
  {
    float mindr=999;
    float minindex=-1;
    float drlimit=-1;
    if (indices.size()>0)
      drlimit=deltar[indices.size()-1];
    for (unsigned int j=0;j<event.jets->size();j++)
    {
      float dr=deltaR(t,event.jets->at(j));
      if ((dr<r) && (dr<mindr) && (dr>(drlimit+0.0001)))
      {
        mindr=dr;
        minindex=j;
      }
    }
    if (minindex>-1)
    {
      indices.push_back(minindex);
      deltar.push_back(mindr);
    }
    else
    {
      break;
    }
  }
  LorentzVector v(0,0,0,0);
  for(auto i : indices)
  {
    v+=event.jets->at(i).v4();
  }
  return v;
}

float TopJetMassAK4(const Event & event, TopJet t, unsigned int njets, float r)
{
  LorentzVector tv4 = getAK4FromTopJet(event,t,njets,r);
  if (tv4.isTimelike()) return tv4.M();
  else return 0;
}

float ZprimeMassAK4(const Event & event, TopJet t1, TopJet t2, unsigned int njets, float r)
{
  LorentzVector zv4 = getAK4FromTopJet(event,t1,njets,r)+getAK4FromTopJet(event,t2,njets,r);
  if (zv4.isTimelike()) return zv4.M();
  else return 0;
}


void uncorrect_topjets(const Event & event){
    for (auto & jet : *event.topjets)
    {
      jet.set_v4(jet.v4() * jet.JEC_factor_raw());
      jet.set_JEC_factor_raw(1.);
    }
}

bool WTag(TopJet topjet)
{
  return TopJetMass(topjet)>60.0 && TopJetMass(topjet)<100.0 && TopJetNsub2(topjet)<0.6 && TopJetPt(topjet)>200.0;
}

bool CMSTopTag::operator()(const TopJet & topjet, const uhh2::Event &) const {
    auto subjets = topjet.subjets();
    if(subjets.size() < 3) return false;
    
    float mjet = 0.0;
    switch(m_typeOfMass)
    {
      case MassType::ungroomed : mjet=topjet.v4().M(); break;
      case MassType::groomed : mjet=m_groomed(topjet); break;
      default: std::cout<<"CMSTopTag Mass type not valid"<<std::endl;
    }
    if(mjet < m_mjetLower) return false;
    if(mjet > m_mjetUpper) return false;

    auto mmin = m_disubjet_min(topjet);
    if(mmin < m_mminLower) return false;

    return true;
}

CMSTopTag::CMSTopTag(double mminLower, double mjetLower, double mjetUpper, MassType typeOfMass): m_mminLower(mminLower),
    m_mjetLower(mjetLower), m_mjetUpper(mjetUpper), m_typeOfMass(typeOfMass){}

CMSTopTag::CMSTopTag(MassType typeOfMass): m_mminLower(50.), m_mjetLower(140.), m_mjetUpper(250.), m_typeOfMass(typeOfMass){}