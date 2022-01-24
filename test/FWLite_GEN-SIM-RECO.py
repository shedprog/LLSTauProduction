from DataFormats.FWLite import Events, Handle
import ROOT
import numpy as np
from colorama import Fore, Back, Style

class SimObjects:
    def __init__(self, vtx, tr, gen):
        self.vtx = vtx
        self.tr = tr
        self.gen = gen

def PrintDecay(par, indent, d_indent, sim_obj):

    vtx = ''
    for track in sim_obj.tr:
        if track.genpartIndex()-1 == par.index():
            vtx = vtx + "(" \
                + str(sim_obj.vtx[track.vertIndex()].position().rho()) + "," \
                + str(sim_obj.vtx[track.vertIndex()].position().r()) + ")"

    print indent + \
        "+->pdgId:", par.pdgId(), \
        "pt:", par.pt(), \
        "vtx rho:", par.vertex().rho(), \
        "vtx abs:", par.vertex().r(), \
        "status:", par.status(), \
        Fore.RED + "SimVertex:" + vtx if vtx!='' else '', \
        Style.RESET_ALL 

    daughters = par.daughterRefVector()
    size = daughters.size()
    for i, child in enumerate(daughters):
        s = '|' if i<size-1 else ' '
        PrintDecay(child, indent + d_indent + "  ", s, sim_obj)

if __name__ == '__main__':
    
    files = ['../script/SUS-RunIIFall18GS-00022_fix_final.root']

    for f_name in files:
        
        print "FILE: ",f_name

        events = Events(f_name)

        # Gen par info
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticles'

        # Tracks info part
        handleTracks = Handle('std::vector<SimTrack>')
        labelTracks = 'g4SimHits'

        # Vertex info part
        handleVertex = Handle('std::vector<SimVertex>')
        labelVertex = 'g4SimHits'

        n_ev = 0
        for n_ev, ev in enumerate(events):
            print "event: ", n_ev
            if n_ev % 1000 == 0:
                print n_ev, "events"

            ev.getByLabel(labelGEN, handleGEN)
            gen_particle = handleGEN.product()

            ev.getByLabel(labelTracks, handleTracks)
            tracks = handleTracks.product()

            ev.getByLabel(labelVertex, handleVertex)
            vertex = handleVertex.product()

            obj_list = SimObjects(vertex, tracks, gen_particle)

            for gen in gen_particle:
                
                # if abs(gen.pdgId())==1000015 and gen.statusFlags().isLastCopy():
                #     PrintDecay(gen,"","")

                if abs(gen.pdgId())==15 and abs(gen.motherRef().pdgId())!=15:
                    PrintDecay(gen.motherRef(),"","", obj_list)

            raw_input("stop")
