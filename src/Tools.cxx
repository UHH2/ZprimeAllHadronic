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

int subJetBTag(TopJet topjet, E_BtagType type, TString mode, TString filename){

  //Modes:
  //default --> no SF
  //mean --> SF
  //lightup,lightdown,bcup,bcdown --> SF systematics evaluation

  int nBTagsSub=0;

  int isdelta[3];
  isdelta[0]=0;
  isdelta[1]=0;
  isdelta[2]=0;

  TString syst=mode;

  float discriminator_cut;

  double refcsv=0.;

  bool dosf=1;

  if(type==e_CSVL) discriminator_cut = 0.244;
  if(type==e_CSVM) discriminator_cut = 0.679;
  if(type==e_CSVT) discriminator_cut = 0.898;
 
  std::vector<Jet> subjets_top;
  //std::vector<float> btagsub_combinedSecondaryVertex_top;
  //std::vector<int> flavorsub_top;

  subjets_top=topjet.subjets();
  //btagsub_combinedSecondaryVertex_top=topjet.btagsub_combinedSecondaryVertex();
  //flavorsub_top=topjet.flavorsub();

  double dr12=deltaR(subjets_top[0],subjets_top[1]);
  double dr13=deltaR(subjets_top[0],subjets_top[2]);
  double dr23=deltaR(subjets_top[1],subjets_top[2]);
 
  if(mode=="lightupdelta"||mode=="lightdowndelta"||mode=="bcupdelta"||mode=="bcdowndelta"){
    
    if(dr12<0.4||dr13<0.4) isdelta[0]=1;
    if(dr12<0.4||dr23<0.4) isdelta[1]=1;
    if(dr13<0.4||dr23<0.4) isdelta[2]=1;
    
  }

  if(filename==""&&mode!="default"){
    std::cout << "ATTENTION!!! Asked b-tagging SF, but no efficiencies provided! SF will NOT be applied!!!" << std::endl;
  }

  if(filename==""||mode=="default"){
    dosf=0;
  }
  
  if(mode!="default"&&mode!="mean"&&mode!="lightup"&&mode!="lightdown"&&mode!="bcup"&&mode!="bcdown"&&mode!="lightupdelta"&&mode!="lightdowndelta"&&mode!="bcupdelta"&&mode!="bcdowndelta"){
    std::cout << "ATTENTION!!! B-tagging SF mode not known! Will NOT perform any SF re-weighting!" << std::endl;
    dosf=0;
  }

  TFile *file_mc=NULL;

  if(dosf){
    file_mc = new TFile(filename);
    
    file_mc->cd();
  }
  
  for(unsigned int i=0; i < subjets_top.size(); ++i){

    Particle subjet=subjets_top[i];
    int flav = subjets_top[i].flavor();
    float subpt=subjet.pt();
    float subeta=subjet.eta();
    float test=subjets_top[i].btag_combinedSecondaryVertex();

    if(!dosf){
      if(test>discriminator_cut){
	nBTagsSub += 1;
      }     
      continue;
    }

    TF1 *csv=NULL;
    TF1 *csvu=NULL;
    TF1 *csvd=NULL;
    
    TH1F *numpt=NULL;
    TH1F *denpt=NULL;
    TH1F *effipt=NULL;
    TH1F *errbc=NULL;

    TRandom3* rand;

    double bc_bins[] = {
      20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800
    };
    errbc=new TH1F("errbc","shift bc", 16, bc_bins);

    int possible=1;
    
    if(type==e_CSVL){
      if(abs(flav)==4||abs(flav)==5){
	csv = new TF1("csv", "0.997942*((1.+(0.00923753*x))/(1.+(0.0096119*x)))", 20.0, 800.0);
	double SFbc_error[] = {
	 0.033299,
	 0.0146768,
	 0.013803,
	 0.0170145,
	 0.0166976,
	 0.0137879,
	 0.0149072,
	 0.0153068,
	 0.0133077,
	 0.0123737,
	 0.0157152,
	 0.0175161,
	 0.0209241,
	 0.0278605,
	 0.0346928,
	 0.0350099};
	for(Int_t ibc=1;ibc<17;ibc++){
	  errbc->SetBinContent(ibc,SFbc_error[ibc-1]);
	}
      }
      else if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	if(fabs(subeta)>=0&&fabs(subeta)<=0.5)
	  {
	    csv = new TF1("csv", "((1.01177+(0.0023066*x))+(-4.56052e-06*(x*x)))+(2.57917e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((1.04582+(0.00290226*x))+(-5.89124e-06*(x*x)))+(3.37128e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.977761+(0.00170704*x))+(-3.2197e-06*(x*x)))+(1.78139e-09*(x*(x*x)))", 20.0, 1000.0);
	  }
	else if(fabs(subeta)>0.5&&fabs(subeta)<=1.0)
	  {
	    csv = new TF1("csv", "((0.975966+(0.00196354*x))+(-3.83768e-06*(x*x)))+(2.17466e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((1.00683+(0.00246404*x))+(-4.96729e-06*(x*x)))+(2.85697e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.945135+(0.00146006*x))+(-2.70048e-06*(x*x)))+(1.4883e-09*(x*(x*x)))", 20.0, 1000.0);
	  }
	else if(fabs(subeta)>1.0&&fabs(subeta)<=1.5)
	  {
	    csv = new TF1("csv", "((0.93821+(0.00180935*x))+(-3.86937e-06*(x*x)))+(2.43222e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((0.964787+(0.00219574*x))+(-4.85552e-06*(x*x)))+(3.09457e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.911657+(0.00142008*x))+(-2.87569e-06*(x*x)))+(1.76619e-09*(x*(x*x)))", 20.0, 1000.0);
	  }
	else if(fabs(subeta)>1.5&&fabs(subeta)<=2.4)
	  {
	    csv = new TF1("csv", "((1.00022+(0.0010998*x))+(-3.10672e-06*(x*x)))+(2.35006e-09*(x*(x*x)))", 20.0, 850.0);
	    csvu = new TF1("csvu", "((1.03039+(0.0013358*x))+(-3.89284e-06*(x*x)))+(3.01155e-09*(x*(x*x)))", 20.0, 850.0);
	    csvd = new TF1("csvd", "((0.970045+(0.000862284*x))+(-2.31714e-06*(x*x)))+(1.68866e-09*(x*(x*x)))", 20.0, 850.0);
	  }
	else{
	  possible=0;
	}
      }
      else{
	possible=0;
      }
    }
    if(type==e_CSVM){
      if(abs(flav)==4||abs(flav)==5){
	csv = new TF1("csv", "(0.938887+(0.00017124*x))+(-2.76366e-07*(x*x))", 20.0, 800.0);
	double SFbc_error[] = {
	  0.0415707,
	  0.0204209,
	  0.0223227,
	  0.0206655,
	  0.0199325,
	  0.0174121,
	  0.0202332,
	  0.0182446,
	  0.0159777,
	  0.0218531,
	  0.0204688,
	  0.0265191,
	  0.0313175,
	  0.0415417,
	  0.0740446,
	  0.0596716 };
	for(Int_t ibc=1;ibc<17;ibc++){
	  errbc->SetBinContent(ibc,SFbc_error[ibc-1]);
	}
      }
      else if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	if(fabs(subeta)>=0&&fabs(subeta)<=0.8)
	  {
	    csv = new TF1("csv", "((1.07541+(0.00231827*x))+(-4.74249e-06*(x*x)))+(2.70862e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((1.18638+(0.00314148*x))+(-6.68993e-06*(x*x)))+(3.89288e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.964527+(0.00149055*x))+(-2.78338e-06*(x*x)))+(1.51771e-09*(x*(x*x)))", 20.0, 1000.0);
	  }
	else if(fabs(subeta)>0.8&&fabs(subeta)<=1.6)
	  {
	    csv = new TF1("csv", "((1.05613+(0.00114031*x))+(-2.56066e-06*(x*x)))+(1.67792e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((1.16624+(0.00151884*x))+(-3.59041e-06*(x*x)))+(2.38681e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.946051+(0.000759584*x))+(-1.52491e-06*(x*x)))+(9.65822e-10*(x*(x*x)))", 20.0, 1000.0);
	  }
	else if(fabs(subeta)>1.6&&fabs(subeta)<=2.4)
	  {
	    csv = new TF1("csv", "((1.05625+(0.000487231*x))+(-2.22792e-06*(x*x)))+(1.70262e-09*(x*(x*x)))", 20.0, 850.0);
	    csvu = new TF1("csvu", "((1.15575+(0.000693344*x))+(-3.02661e-06*(x*x)))+(2.39752e-09*(x*(x*x)))", 20.0, 850.0);
	    csvd = new TF1("csvd", "((0.956736+(0.000280197*x))+(-1.42739e-06*(x*x)))+(1.0085e-09*(x*(x*x)))", 20.0, 850.0);
	  }
	else{
	  possible=0;
	}
      }
      else{
	possible=0;
      }
    }
    if(type==e_CSVT){
      if(abs(flav)==4||abs(flav)==5){
	csv = new TF1("csv", "(0.927563+(1.55479e-05*x))+(-1.90666e-07*(x*x))", 20.0, 800.0);
	double SFbc_error[] = {
	  0.0515703,
	  0.0264008,
	  0.0272757,
	  0.0275565,
	  0.0248745,
	  0.0218456,
	  0.0253845,
	  0.0239588,
	  0.0271791,
	  0.0273912,
	  0.0379822,
	  0.0411624,
	  0.0786307,
	  0.0866832,
	  0.0942053,
	  0.102403};
	for(Int_t ibc=1;ibc<17;ibc++){
	  errbc->SetBinContent(ibc,SFbc_error[ibc-1]);
	}
      }
      else if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	if(fabs(subeta)>=0&&fabs(subeta)<=2.4)
	  {
	    csv = new TF1("csv", "((1.00462+(0.00325971*x))+(-7.79184e-06*(x*x)))+(5.22506e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvu = new TF1("csvu", "((1.16361+(0.00464695*x))+(-1.09467e-05*(x*x)))+(7.21896e-09*(x*(x*x)))", 20.0, 1000.0);
	    csvd = new TF1("csvd", "((0.845757+(0.00186422*x))+(-4.6133e-06*(x*x)))+(3.21723e-09*(x*(x*x)))", 20.0, 1000.0);
	  }
	else{
	  possible=0;
	}
      }
      else{
	possible=0;
      }
    }
    
    if(!possible){
      if(test>discriminator_cut){
	nBTagsSub += 1;
      }

      delete errbc;
      continue;
    }
    
    double SF=0;
    
    if (csv->GetXmin() > subpt){
      SF=csv->Eval(csv->GetXmin());
    }
    else if (csv->GetXmax() < subpt){ 
      SF=csv->Eval(csv->GetXmax());
    }
    else{
      SF=csv->Eval(subpt);
    } 
    
    refcsv=SF;

    double addSF=0;
    
    int bin;
    
    int doubleunc=0;
    
    if((syst=="bcup"||syst=="bcdown"||syst=="bcupdelta"||syst=="bcdowndelta")&&(abs(flav)==5||abs(flav)==4)){
      if(subpt>=800){
	bin=errbc->GetXaxis()->GetNbins();
	doubleunc=1;
      }
      else if(subpt<20){
	bin=1;
	doubleunc=1;
      }
      else{
	bin=errbc->GetXaxis()->FindBin(subpt);
      }
      addSF=errbc->GetBinContent(bin);
      if(doubleunc){
	addSF=2*addSF;
      }
      if(abs(flav)==4){
	addSF=2*addSF;
      }
      if(syst=="bcdown"||syst=="bcdowndelta"){
	addSF=-addSF;
      }
      if(isdelta[i]){
	addSF=2*addSF;
      }
    }
    
    SF=SF+addSF;
    
    if((syst=="lightup"||syst=="lightupdelta")&&(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21)){
      if (csvu->GetXmin() > subpt){
	SF=csvu->Eval(csvu->GetXmin());
      }
      else if (csvu->GetXmax() < subpt){ 
	SF=csvu->Eval(csvu->GetXmax());
      }
      else{
	SF=csvu->Eval(subpt);
      }
      if(isdelta[i]){
	SF=SF+(SF-refcsv);
      }
    }
    
    if((syst=="lightdown"||syst=="lightdowndelta")&&(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21)){
      if (csvd->GetXmin() > subpt){
	SF=csvd->Eval(csvd->GetXmin());
      }
      else if (csvd->GetXmax() < subpt){ 
	SF=csvd->Eval(csvd->GetXmax());
      }
      else{
	SF=csvd->Eval(subpt);
      }
      if(isdelta[i]){
	SF=SF+(SF-refcsv);
      }
    }
    
    if(type==e_CSVL){
      if(abs(flav)==5){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet_bTagL");
	effipt=new TH1F("effipt","effi pt", 17, jetpt_bins);
      }
      if(abs(flav)==4){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet_bTagL");
	effipt=new TH1F("effipt","effi pt", 14, jetpt_bins);
      }
      if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 1600
	};
	if(fabs(subeta)>=0&&fabs(subeta)<=0.5)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1L");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1_bTagL");
	  }
	if(fabs(subeta)>0.5&&fabs(subeta)<=1.0)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e2L");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e2_bTagL");
	  }
	if(fabs(subeta)>1.0&&fabs(subeta)<=1.5)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3L");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3_bTagL");
	  }
	if(fabs(subeta)>1.5&&fabs(subeta)<=2.4)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3L");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3_bTagL");
	  }
	
	effipt=new TH1F("effipt","effi pt", 16, jetpt_bins);
      } 
    }

    if(type==e_CSVM){
      if(abs(flav)==5){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet_bTagM");
	effipt=new TH1F("effipt","effi pt", 17, jetpt_bins);
      }
      if(abs(flav)==4){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet_bTagM");
	effipt=new TH1F("effipt","effi pt", 14, jetpt_bins);
      }
      if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 1600
	};
	if(fabs(subeta)>=0&&fabs(subeta)<=0.8)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1M");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1_bTagM");
	  }
	if(fabs(subeta)>0.8&&fabs(subeta)<=1.6)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e2M");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e2_bTagM");
	  }
	if(fabs(subeta)>1.6&&fabs(subeta)<=2.4)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3M");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e3_bTagM");
	  }
	effipt=new TH1F("effipt","effi pt", 16, jetpt_bins);
      } 
    }

    if(type==e_CSVT){
      if(abs(flav)==5){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_bJet_bTagT");
	effipt=new TH1F("effipt","effi pt", 17, jetpt_bins);
      }
      if(abs(flav)==4){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 1600
	};
	denpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet");
	numpt=(TH1F*) file_mc->Get("BTagEff/pt_cJet_bTagT");
	effipt=new TH1F("effipt","effi pt", 14, jetpt_bins);
      }
      if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
	double jetpt_bins[] = {
	  20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 1600
	};
	if(fabs(subeta)>=0&&fabs(subeta)<=2.4)
	  {
	    denpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1T");
	    numpt=(TH1F*) file_mc->Get("BTagEff/pt_lJet_e1_bTagT");
	  }
	effipt=new TH1F("effipt","effi pt", 16, jetpt_bins);
      } 
    }

    effipt->Divide(numpt,denpt,1,1,"B");
    
    float effi;
    
    if(subpt>=1600){
      bin=effipt->GetXaxis()->GetNbins();
    }
    else if(subpt<20){
      bin=1;
    }
    else{
      bin=effipt->GetXaxis()->FindBin(subpt);
    }

    if(denpt->GetBinContent(bin)*denpt->GetEntries()/denpt->Integral()<10){
      if(test>discriminator_cut){
	nBTagsSub += 1;
      }
      
      delete csv;
      delete numpt;
      delete denpt;
      delete effipt;
      delete errbc;
      continue;
    }
    
    effi=effipt->GetBinContent(bin);
    
    double etaseed = subeta;
    double sin_eta = sin(etaseed*1000000);
    int seed = abs(static_cast<int>(sin_eta*100000));
    
    rand = new TRandom3(seed);
    
    float coin = rand->Uniform(1.);
    
    bool istagged=false;
    
    if(test>discriminator_cut) istagged=true;
    
    bool newtag = istagged;
    
    if(SF > 1){
      
      if( !istagged ) {
	
	//fraction of jets that needs to be upgraded
	float mistagPercent = (1.0 - SF) / (1.0 - (1.0/effi) );
	
	//upgrade to tagged
	if( coin < mistagPercent ) {newtag = true;}
      }
      
    }else{
      
      //downgrade tagged to untagged
      if( istagged && coin > SF ) {newtag = false;}
      
    }
    
    //if(istagged!=newtag)
      //cout << "Flavor " << flav << " was " << istagged << " is " << newtag << endl;
    

    if(newtag){
      nBTagsSub += 1;
    }

    if(abs(flav)==1||abs(flav)==2||abs(flav)==3||abs(flav)==21){
      if(fabs(subeta)>=0&&fabs(subeta)<=2.4){

	delete csvu;
	delete csvd;

      }
    }

    delete csv;
    delete numpt;
    delete denpt;
    delete effipt;
    delete errbc;
    delete rand;
    
  }
  
  if(dosf){
    file_mc->Close();   
    delete file_mc;
  }

  return nBTagsSub;

}