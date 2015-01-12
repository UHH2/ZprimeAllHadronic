#include "UHH2/Zp2TopVLQAllHad/include/Tools.h"

float getHT50(Event & event)
{
  float ht=0.0;
  for(unsigned int i=0; i<event.jets->size(); ++i)
  {
    if (event.jets->at(i).pt()>=50.0)
    {
      ht+=event.jets->at(i).pt();
    }
  }
  return ht;
}

float getHTAK8(Event & event)
{
 if (event.jets->size()>1) return event.jets->at(0).pt() + event.jets->at(1).pt();
 if (event.jets->size()>0) return event.jets->at(0).pt();
 return 0.0;
}

float getMaxTopJetPt(Event & event)
{
  valuelist std::vector<float>;
    for(unsigned int i=0; i<event.jets->size(); ++i)
    {
      valuelist.push_back(event.jets->at(i).pt());
    }
  return max(valuelist);
}

float getMaxTopJetMass(Event & event)
{
  valuelist std::vector<float>;
    for(unsigned int i=0; i<event.jets->size(); ++i)
    {
      if (event.jets->at(i).v4().isTimelike()) valuelist.push_back(event.jets->at(i).v4().M());
    }
  return max(valuelist);
}
