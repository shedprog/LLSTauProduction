from DataFormats.FWLite import Events, Handle
import ROOT
import numpy as np

if __name__ == '__main__':
    
    files = ['/afs/cern.ch/user/m/myshched/STauGENProduction/LLSTauProduction20UL18_test/script/SUS-RunIIFall18GS-00022.root']

    for f_name in files:
        
        print "FILE: ",f_name

        events = Events(f_name)

        # Gen par info
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticlePlusGeant'

        n_ev = 0
        for n_ev, ev in enumerate(events):
            print "event: ", n_ev
            if n_ev % 1000 == 0:
                print n_ev, "events"

            ev.getByLabel(labelGEN, handleGEN)
            gen_particle = handleGEN.product()

            for gen in gen_particle:

                if abs(gen.pdgId())==1000015:

                    print gen.pdgId(), \
                        "status:", gen.status()

                if abs(gen.pdgId())==15:

                    print gen.pdgId(), \
                        "pt:", gen.pt(), \
                        "vtx rho:", gen.vertex().rho(), \
                        "vtx abs:", gen.vertex().r(), \
                        "status:", gen.status()

                    for doughter in gen.daughterRefVector():
                        print "-----> pdgId:", doughter.pdgId(), \
                            "pt:", doughter.pt(), \
                            "vtx rho:", doughter.vertex().rho(), \
                            "vtx abs:", doughter.vertex().r(), \
                            "status:", doughter.status()
                        for dd in doughter.daughterRefVector():
                            print "----------> pdgId:", dd.pdgId(), \
                                "pt:", dd.pt(), \
                                "vtx rho:", dd.vertex().rho(), \
                                "vtx abs:", dd.vertex().r(), \
                                "status:", doughter.status()

            raw_input("stop")
