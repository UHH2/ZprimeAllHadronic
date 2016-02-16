#pragma once

#include "UHH2/core/include/Hists.h"
#include "UHH2/ZprimeAllHadronic/include/Tools.h"

/**  \brief Example class for booking and filling histograms
 * 
 * NOTE: This class uses the 'hist' method to retrieve histograms.
 * This requires a string lookup and is therefore slow if you have
 * many histograms. Therefore, it is recommended to use histogram
 * pointers as member data instead, like in 'common/include/ElectronHists.h'.
 */
class Zp2TopVLQAllHadHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    Zp2TopVLQAllHadHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~Zp2TopVLQAllHadHists();
private:
    //uhh2::Event::Handle<std::vector<Jet> > h_jetsAK8;
    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsAK8;
    uhh2::Event::Handle<std::vector<TopJet> > h_topjetsCA15;
    // uhh2::Event::Handle<std::vector<TopJet> > h_topjetsHEP;
    // std::vector<uhh2::Event::Handle<std::vector<TopJet> > > topjet_handles;
    // std::vector<uhh2::Event::Handle<std::vector<Jet> > > jet_handles;
    // std::vector<std::string> jet_collection_names;
    // std::vector<std::string> topjet_collection_names;
};

class PreselectionHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    PreselectionHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~PreselectionHists();
private:
    // uhh2::Event::Handle<std::vector<TopJet> > h_topjetsAK8;
    // uhh2::Event::Handle<std::vector<TopJet> > h_topjetsCA15;
};

class SelectionHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    SelectionHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~SelectionHists();
private:
    int top_sys;
    int w_sys;
    //int pu_sys;
    int ttbar_sys;
};

class MistagAndShapeHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    MistagAndShapeHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~MistagAndShapeHists();
};

class BackgroundHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    BackgroundHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~BackgroundHists();
private:
    std::unique_ptr<TFile> f;
    std::unique_ptr<TH2F> mistag;
    std::unique_ptr<TH1F> mass_shape;
    // TFile * f;
    // TH2F * mistag;
    // TH1F * mass_shape;
};

class TriggerHists: public uhh2::Hists {
public:
    // use the same constructor arguments as Hists for forwarding:
    TriggerHists(uhh2::Context & ctx, const std::string & dirname);

    virtual void fill(const uhh2::Event & ev) override;
    virtual ~TriggerHists();
private:
    Event::Handle<float> h_ht;
    Event::Handle<float> h_htca8;
    Event::Handle<float> h_pt1ca8;
    Event::Handle<float> h_pt2ca8;
};
