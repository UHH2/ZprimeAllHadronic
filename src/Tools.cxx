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

float JetMass(Jet jet)
{
  LorentzVector v4=jet.v4();
  if(!v4.isTimelike()) return 0.0;
  else return v4.M();
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

float ZprimeMassResVLQ(TopJet t1, TopJet t2, Jet t3, Jet t4)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  allsubjets += t3.v4();
  allsubjets += t4.v4();
  if(!allsubjets.isTimelike()) return 0.0;
  else return allsubjets.M();
}

float ZprimePtResVLQ(TopJet t1, TopJet t2, Jet t3, Jet t4)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : t1.subjets()) allsubjets += subjet.v4();
  for(auto subjet : t2.subjets()) allsubjets += subjet.v4();
  allsubjets += t3.v4();
  allsubjets += t4.v4();
  return allsubjets.Pt();
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

float TopJetPt2(TopJet topjet)
{
  LorentzVector allsubjets(0,0,0,0);
  for(auto subjet : topjet.subjets()) allsubjets += subjet.v4();
  return allsubjets.Pt();
}

float TopJetPt(Particle topjet)
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

  // //pt requirement
  // if(TopJetPt(topjet)<400.0) return false;
  // //mass requirement
  // auto mjet = TopJetMass(topjet);
  // if(mjet<110 || mjet>210) return false;
  // //nsubjettiness requirement
  // if (TopJetNsub(topjet)>0.86) return false;
  // return true;

bool TopTag(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>400.0 && mjet>110.0 && mjet<210.0 && TopJetNsub(topjet)<0.86;
}

bool TopTag15(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>200.0 && mjet>140.0 && mjet<250.0 && TopJetNsub(topjet)<0.88;
}

bool AntiTopTag_mass(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>400.0 && (mjet<110.0 || mjet>210.0) && TopJetNsub(topjet)<0.86;
}
bool AntiTopTag_nsub(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>400.0 && mjet>110.0 && mjet<210.0 && TopJetNsub(topjet)>0.86;
}

bool WTag(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return mjet>70.0 && mjet<100.0 && TopJetNsub2(topjet)<0.6 && TopJetPt(topjet)>200.0;//65 105
}

bool AntiWTag_mass(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return (mjet<70.0 || mjet>100.0) && TopJetNsub2(topjet)<0.6 && TopJetPt(topjet)>200.0;
}

bool AntiWTag_nsub(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return mjet>70.0 && mjet<100.0 && TopJetNsub2(topjet)>0.6 && TopJetPt(topjet)>200.0;
}

bool TopTag_nopt(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return mjet>110.0 && mjet<210.0 && TopJetNsub(topjet)<0.86;
}

bool WTag_nopt(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return mjet>70.0 && mjet<100.0 && TopJetNsub2(topjet)<0.6;//65 105
}

bool SemiTopTag_mass(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>400.0 && mjet>110.0 && mjet<210.0;
}
bool SemiTopTag_nsub(TopJet topjet)
{
  //auto mjet = TopJetMass(topjet);
  return TopJetPt(topjet)>400.0 && TopJetNsub(topjet)<0.86;
}
bool SemiWTag_mass(TopJet topjet)
{
  auto mjet = TopJetMass(topjet);
  return mjet>70.0 && mjet<100.0 && TopJetPt(topjet)>200.0;
}
bool SemiWTag_nsub(TopJet topjet)
{
  //auto mjet = TopJetMass(topjet);
  return TopJetNsub2(topjet)<0.6 && TopJetPt(topjet)>200.0;
}

std::pair<TopJet, TopJet> findTopWpair( bool (*ttag)(TopJet), bool (*wtag)(TopJet), TopJet first, TopJet second)
{

if (ttag(first) && wtag(second)) return std::make_pair( first, second );
else if (ttag(second) && wtag(first)) return std::make_pair( second, first );
return std::make_pair( first, first );

}










float QCDWeight(float mzp, string mode, string syst)
{
 float weight = 1.0;
 if (mode=="mean")
 {
  weight = 1.414 - 0.0002473 *mzp;
 }
 if (mode=="1")
 {
  weight = 1.31511055109 + mzp * ( -0.000180944645427 );
 }
 if (mode=="2")
 {
  weight = 1.27068031541 + mzp * ( -0.000188252028031 );
 }
 if (mode=="1par")
 {
  weight = 1.95859445486 + mzp * ( -0.000831431907595 ) + mzp * mzp * ( 1.53312771869e-07 );
 }
 if (mode=="2par")
 {
  weight = 2.32313235808 + mzp * ( -0.0012089203851 ) + mzp * mzp * ( 2.30655337018e-07 );
 }
 if (syst=="nominal")
  {
    return weight;
  }
  if (syst=="up")
  {
    return weight*weight;
  }
  if (syst=="down")
  {
    return 1.0;
  }
  if (syst=="up_fit")
  {
    if (contains(mode,"par"))
    {
      if (contains(mode,"1"))
      {
        //parabola up 1btag
        return QCDWeight(mzp,mode,"nominal") + sqrt( 0.0851352974342 + mzp * mzp * ( 8.13557680355e-08 ) +  2 * mzp * ( -8.21702286312e-05 ) + 2 * mzp * mzp * ( 1.85752118875e-08 ) + 2 * mzp * mzp * mzp * ( -1.87773199501e-11 ) + mzp * mzp * mzp * mzp * ( 4.42559720473e-15 ) );
      }
      else
      {
        //parabola up 2btag
        return QCDWeight(mzp,mode,"nominal") + sqrt( 0.532269629238 + mzp * mzp * ( 4.73725413458e-07 ) +  2 * mzp * ( -0.00049705700664 ) + 2 * mzp * mzp * ( 1.08331539344e-07 ) + 2 * mzp * mzp * mzp * ( -1.05059965354e-10 ) + mzp * mzp * mzp * mzp * ( 2.37419352069e-14 ) );
      }
    }
    else
    {
      if (contains(mode,"1"))
      {
        //retta up 1btag
        return QCDWeight(mzp,mode,"nominal") + sqrt( 0.00717099381301 + mzp * mzp * ( 1.68566805877e-09 ) +  2 * mzp * ( -3.3576447591e-06 ) );
      }
      else
      {
        //retta up 2btag
        return QCDWeight(mzp,mode,"nominal") + sqrt( 0.0379661070487 + mzp * mzp * ( 8.82665212869e-09 ) +  2 * mzp * ( -1.76812706191e-05 ) );
      }
    }
  }
  if (syst=="down_fit")
  {
    if (contains(mode,"par"))
    {
      if (contains(mode,"1"))
      {
        //parabola down 1btag
        return QCDWeight(mzp,mode,"nominal") - sqrt( 0.0851352974342 + mzp * mzp * ( 8.13557680355e-08 ) +  2 * mzp * ( -8.21702286312e-05 ) + 2 * mzp * mzp * ( 1.85752118875e-08 ) + 2 * mzp * mzp * mzp * ( -1.87773199501e-11 ) + mzp * mzp * mzp * mzp * ( 4.42559720473e-15 ) );
      }
      else
      {
        //parabola down 2btag
        return QCDWeight(mzp,mode,"nominal") - sqrt( 0.532269629238 + mzp * mzp * ( 4.73725413458e-07 ) +  2 * mzp * ( -0.00049705700664 ) + 2 * mzp * mzp * ( 1.08331539344e-07 ) + 2 * mzp * mzp * mzp * ( -1.05059965354e-10 ) + mzp * mzp * mzp * mzp * ( 2.37419352069e-14 ) );
      }
    }
    else
    {
      if (contains(mode,"1"))
      {
        //retta down 1btag
        return QCDWeight(mzp,mode,"nominal") - sqrt( 0.00717099381301 + mzp * mzp * ( 1.68566805877e-09 ) +  2 * mzp * ( -3.3576447591e-06 ) );
      }
      else
      {
        //retta down 2btag
        return QCDWeight(mzp,mode,"nominal") - sqrt( 0.0379661070487 + mzp * mzp * ( 8.82665212869e-09 ) +  2 * mzp * ( -1.76812706191e-05 ) );
      }
    }
  }
  return 1.0;
}
float QCDWeightFat(float mzp, string mode, string syst)
{
 float weight = 1.0;
 if (mode=="1")
 {
  weight = 1.32130072233 + mzp * ( -0.000198404914716 );
 }
 if (mode=="2")
 {
  weight = 1.30773562166 + mzp * ( -0.000204175716166 );
 }
 if (mode=="1par")
 {
  weight = 1.85203876597 + mzp * ( -0.000776802891645 ) + mzp * mzp * ( 1.43786864781e-07 );
 }
 if (mode=="2par")
 {
  weight = 1.16136650728 + mzp * ( -4.00092857569e-05 ) + mzp * mzp * ( -4.16348684288e-08 );
 }
 if (syst=="nominal")
  {
    //event.weight *= weight;
    return weight;
  }
  if (syst=="up")
  {
    //event.weight *= weight*weight;
    return weight*weight;
  }
  if (syst=="down")
  {
    return 1.0;
  }
  if (syst=="up_fit")
  {
    if (contains(mode,"par"))
    {
      if (contains(mode,"1"))
      {
        //parabola up 1btag
        return QCDWeightFat(mzp,mode,"nominal") + sqrt( 0.0359913003279 + mzp * mzp * ( 3.93258954589e-08 ) +  2 * mzp * ( -3.7020107814e-05 ) + 2 * mzp * mzp * ( 8.73218168984e-09 ) + 2 * mzp * mzp * mzp * ( -9.51629863789e-12 ) + mzp * mzp * mzp * mzp * ( 2.36569757444e-15 ) );
      }
      else
      {
        //parabola up 2btag
        return QCDWeightFat(mzp,mode,"nominal") + sqrt( 0.204174512393 + mzp * mzp * ( 2.37846449579e-07 ) +  2 * mzp * ( -0.000217087665565 ) + 2 * mzp * mzp * ( 5.24404784647e-08 ) + 2 * mzp * mzp * mzp * ( -5.8816757527e-11 ) + mzp * mzp * mzp * mzp * ( 1.49167233514e-14 ) );
      }
    }
    else
    {
      if (contains(mode,"1"))
      {
        //retta up 1btag
        return QCDWeightFat(mzp,mode,"nominal") + sqrt( 0.00375935948195 + mzp * mzp * ( 1.04545372171e-09 ) +  2 * mzp * ( -1.89386651423e-06 ) );
      }
      else
      {
        //retta up 2btag
        return QCDWeightFat(mzp,mode,"nominal") + sqrt( 0.0198173908369 + mzp * mzp * ( 5.93150377106e-09 ) +  2 * mzp * ( -1.03144316693e-05 ) );
      }
    }
  }
  if (syst=="down_fit")
  {
    if (contains(mode,"par"))
    {
      if (contains(mode,"1"))
      {
        //parabola down 1btag
        return QCDWeightFat(mzp,mode,"nominal") - sqrt( 0.0359913003279 + mzp * mzp * ( 3.93258954589e-08 ) +  2 * mzp * ( -3.7020107814e-05 ) + 2 * mzp * mzp * ( 8.73218168984e-09 ) + 2 * mzp * mzp * mzp * ( -9.51629863789e-12 ) + mzp * mzp * mzp * mzp * ( 2.36569757444e-15 ) );
      }
      else
      {
        //parabola down 2btag
        return QCDWeightFat(mzp,mode,"nominal") - sqrt( 0.204174512393 + mzp * mzp * ( 2.37846449579e-07 ) +  2 * mzp * ( -0.000217087665565 ) + 2 * mzp * mzp * ( 5.24404784647e-08 ) + 2 * mzp * mzp * mzp * ( -5.8816757527e-11 ) + mzp * mzp * mzp * mzp * ( 1.49167233514e-14 ) );
      }
    }
    else
    {
      if (contains(mode,"1"))
      {
        //retta down 1btag
        return QCDWeightFat(mzp,mode,"nominal") - sqrt( 0.00375935948195 + mzp * mzp * ( 1.04545372171e-09 ) +  2 * mzp * ( -1.89386651423e-06 ) );
      }
      else
      {
        //retta down 2btag
        return QCDWeightFat(mzp,mode,"nominal") - sqrt( 0.0198173908369 + mzp * mzp * ( 5.93150377106e-09 ) +  2 * mzp * ( -1.03144316693e-05 ) );
      }
    }
  }
  return 1.0;
}













float TTbarWeight(const Event & event, int syst)
{
  if (event.isRealData) return 1.0;
  TTbarGen ttbargen(*event.genparticles, false);
  if (ttbargen.DecayChannel()==TTbarGen::e_notfound)
  {
    /*cout<<"ttbargen not found";*/ return 1.0;
  }
  // float N=0.92;
  // float alpha=-0.00096;
  // float sigmaN=0.17;
  // float sigmaAlpha=0.00020;
  float weight= 0.93*exp(-0.00088*0.5*(ttbargen.Top().pt()+ttbargen.Antitop().pt()));
  if (syst==0)
  {
    //event.weight *= weight;
    return weight;
  }
  if (syst==1)
  {
    //event.weight *= weight*weight;
    return weight*weight;
  }
  if (syst==-1)
  {
    return 1.0;
  }
  return 1.0;
}

float TopTagSF(const Event & event, TopJet jet, int sys)
{
  float sf=0.85;
  float error=0.08;
  //https://twiki.cern.ch/twiki/bin/view/CMS/JetTopTagging
  if (jet.pt()>550.0)
  {
    sf=1.08;
    error=0.16;
  }
  if(!event.isRealData)
  {
    // if (contains(procname,"TSFUP")) return sf+error;
    // if (contains(procname,"TSFDOWN")) return sf-error;
    if (sys==1) return sf+error;
    if (sys==-1) return sf-error;
    return sf;
  }
  else return 1.0;
}
float WTagSF(const Event & event, TopJet jet, int sys)
{
  float sf=0.98;
  float error=0.03;
  float errorbig=0.048;

  //https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
  //http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2015_196_v8.pdf
  if(!event.isRealData)
  {
    bool is_matched=false;
    for (auto genp : *event.genparticles)
    {
      if (abs(genp.pdgId()) == 24)
      {
        if(deltaR(jet,genp)<0.8)
        {
          is_matched=true;
          break;
        }
      }
    }
    // if (contains(procname,"WSFUP")) return sf+error;
    // if (contains(procname,"WSFDOWN")) return sf-error;
    if (is_matched)
    {
      if (sys==1)
      {
        if(jet.pt()>300.0)
        {
          return sf+errorbig;
        }
        else
        {
          return sf+error;
        }
      }
      if (sys==-1)
      {
        if(jet.pt()>300.0)
        {
          return sf-errorbig;
        }
        else
        {
          return sf-error;
        }
      }
      return sf;
    }
  }
  return 1.0;
}

bool contains(string s, string substring)
{
 return s.find(substring)!=string::npos; 
}

bool SDTopTag::operator()(const TopJet & topjet, const uhh2::Event &) const {
    
    float mjet = TopJetMass(topjet);

    if(mjet < 110) return false;
    if(mjet > 210) return false;
    //if (topjet.pt()<400) return false;

    float nsub = TopJetNsub(topjet);
    float csv  = getMaxCSV(topjet);

    //bool istagged=false;

// e(B) = 0.1% SD WP1 0.1%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.44
// e(B) = 0.1% SD WP2 0.1%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.54, max SD subjet b-discriminant > 0.79

// e(B) = 0.3% SD WP1 0.3%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.50
// e(B) = 0.3% SD WP2 0.3%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.61, max SD subjet b-discriminant > 0.76

// e(B) = 1% SD WP1 1%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.59
// e(B) = 1% SD WP2 1%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.69, max SD subjet b-discriminant > 0.66

// e(B) = 3% SD WP1 3%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.69
// e(B) = 3% SD WP2 3%    SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.75, max SD subjet b-discriminant > 0.39

// e(B) = 10% SD WP1  10%   SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.86
// e(B) = 10% SD WP2  10%   SD(β=0,z=0.1, R=0.8) [110,210]  tau32 < 0.87, max SD subjet b-discriminant > 0.089

    switch(m_WP)
    {
      case WP::Mis0p1 : if(nsub<0.44) return true; break;
      case WP::Mis0p1b : if(nsub<0.54 && csv>0.79) return true; break;
      case WP::Mis0p3 : if(nsub<0.50) return true; break;
      case WP::Mis0p3b : if(nsub<0.61 && csv>0.76) return true; break;
      case WP::Mis1 : if(nsub<0.59) return true; break;
      case WP::Mis1b : if(nsub<0.69 && csv>0.66) return true; break;
      case WP::Mis3 : if(nsub<0.69) return true; break;
      case WP::Mis3b : if(nsub<0.75 && csv>0.39) return true; break;
      case WP::Mis10 : if(nsub<0.86) return true; break;
      case WP::Mis10b : if(nsub<0.87 && csv>0.089) return true; break;
      default: std::cout<<"SDTopTag working point not valid"<<std::endl;
    }
    

    return false;
}

SDTopTag::SDTopTag(WP WorkingPoint): m_WP(WorkingPoint){}