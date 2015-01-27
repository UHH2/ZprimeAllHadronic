import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('/nfs/dust/cms/user/usaiem/gc-output/PHYS14v0/signals3/MC_Zp_TTJets_M2000W20_20x25_40_miniaod.root')
handle_topjets  = Handle ('std::vector<pat::Jet>')
handle_genjets  = Handle ('std::vector<reco::GenJet>')
handle_gensubjets  = Handle ('std::vector<reco::GenJet>')
label = ("patJetsCMSTopTagCHSPacked")
label2 = ("patJetsCA8CHS",'genJets')
ROOT.gROOT.SetBatch()
ROOT.gROOT.SetStyle('Plain') # white background
zmassHist = ROOT.TH1F ("zmass", "Z Candidate Mass", 50, 20, 220)
for event in events:
	event.getByLabel (label, handle)
	event.getByLabel (label2, handle2)
	topjet = handle.product()
	genjet = handle2.product()
	if len(topjet)>0:
		if topjet[0].numberOfDaughters()>1:
			if topjet[0].daughter(1).genJet():
				print 'number of daughters',topjet[0].daughter(0).pt()-topjet[0].daughter(0).genJet().pt()
				#print 'number of daughters - gen jet',genjet[0].numberOfDaughters()