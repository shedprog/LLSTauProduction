from DataFormats.FWLite import Events, Handle
import ROOT
import numpy as np
import os
import math

# This script plots the exponential distribution for the different lifetimes
# the calculation includes accounting of the momentum of the particle

def get_mother(gen, pdgId_mother):
    if gen.numberOfMothers() >= 1:
        if abs(gen.motherRef().pdgId()) != pdgId_mother:
            return gen
        else:
            return get_mother(gen.motherRef(), pdgId_mother)

    return gen

if __name__ == '__main__':

    files = [
            ['/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v4/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau1000mm_v4/GENSIM/220125_122410/0000/SUS-RunIISummer20UL18wmLHEGEN-LLStau_10.root',
            '/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v4/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau1000mm_v4/GENSIM/220125_122410/0000/SUS-RunIISummer20UL18wmLHEGEN-LLStau_408.root',
            '/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v4/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau1000mm_v4/GENSIM/220125_122410/0000/SUS-RunIISummer20UL18wmLHEGEN-LLStau_401.root',
            ],
            [
            '/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v5-100cm/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau100mm_v5/GENSIM/220520_091940/0001/SUS-RunIISummer20UL18wmLHEGEN-LLStau_1339.root',
            '/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v5-100cm/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau100mm_v5/GENSIM/220520_091940/0001/SUS-RunIISummer20UL18wmLHEGEN-LLStau_1336.root',
            '/pnfs/desy.de/cms/tier2/store/user/myshched/mc/UL2018-pythia-v5-100cm/SUS-RunIISummer20UL18GEN-stau100_lsp1_ctau100mm_v5/GENSIM/220520_091940/0001/SUS-RunIISummer20UL18wmLHEGEN-LLStau_1692.root'
            ]]

    # x: displacement [cm]
    disp_hists = []
    for i, file in enumerate(files):
        disp_hists.append( ROOT.TH1D("disp"+str(i),"disp", 1000, 0, 2000) )


    for i, f_names in enumerate(files):

        for f_name in f_names:

            print "FILE: ", f_name

            events = Events(f_name)

            # Gen par info
            handleGEN = Handle('std::vector<reco::GenParticle>')
            labelGEN = 'genParticlePlusGeant'

            n_ev = 0
            for n_ev, ev in enumerate(events):
                print "event", n_ev
        
                ev.getByLabel(labelGEN, handleGEN)
                gen_particle = handleGEN.product()

                for gen in gen_particle:
                    if abs(gen.pdgId())==15:
                        if abs(gen.motherRef().pdgId())==1000015:
                            mother = get_mother(gen.motherRef(), 1000015)
                            x, y, z = mother.vertex().x(), mother.vertex().y(), mother.vertex().z()
                            gamma = mother.energy() / mother.mass()
                            disp = math.sqrt( \
                                    (gen.vertex().x()-x)**2 + \
                                    (gen.vertex().y()-y)**2 + \
                                    (gen.vertex().z()-z)**2 )
                            disp_hists[i].Fill(disp / gamma)

    pref = "compare_"
    dir_out = "./output_displacment/"
    try:
        os.stat(dir_out)
    except:
        os.mkdir(dir_out)
    
    c = ROOT.TCanvas("c", "c", 1000, 800)
    disp_hists[1].GetXaxis().SetTitle("[cm]")
    disp_hists[1].SetTitle("|s#tau.vtx()-#tau.vtx()| / #gamma")
    disp_hists[1].Draw()
    disp_hists[0].GetXaxis().SetTitle("[cm]")
    disp_hists[0].SetLineColor(2)
    disp_hists[0].Draw("same")
    c.Print(dir_out + pref + "lifetime.pdf")

    c2 = ROOT.TCanvas("c2", "c2", 1000, 800)
    h1 = disp_hists[1].GetCumulative()
    h1.SetTitle("integral |s#tau.vtx()-#tau.vtx()| / #gamma ( 63% at t_{0} )")
    h1.Scale(1.0 / disp_hists[1].GetEntries())
    h1.GetYaxis().SetRangeUser(0., 1.)
    h1.GetXaxis().SetRangeUser(0., 120.)
    h2 = disp_hists[0].GetCumulative()
    h2.Scale(1.0 / disp_hists[0].GetEntries())
    h2.GetXaxis().SetRangeUser(0., 120.)
    h1.GetXaxis().SetTitle("[cm]")
    h1.Draw()
    h2.GetXaxis().SetTitle("[cm]")
    h2.SetLineColor(2)
    h2.Draw("same")
    c2.Print(dir_out + pref + "lifetime_integral.pdf")


