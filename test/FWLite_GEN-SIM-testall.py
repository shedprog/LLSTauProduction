import argparse
from DataFormats.FWLite import Events, Handle
import ROOT
import numpy as np
from colorama import Fore, Back, Style
import os
import math
ROOT.gROOT.SetBatch(True)

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
                + str(sim_obj.vtx[track.vertIndex()].position().z()) + ")"
    if par.status()==8: 
        print (Fore.YELLOW + indent + \
            "+->pdgId:", par.pdgId(), \
            "E:", par.energy(), \
            "eta:", par.eta(), \
            "vtx rho:", par.vertex().rho(), \
            "vtx z", par.vertex().z(), \
            "status:", par.status(), \
            # Fore.RED + "SimVertex:" + vtx if vtx!='' else '', \
            Style.RESET_ALL 
        )
    else:
        print (indent + \
            "+->pdgId:", par.pdgId(), \
            "E:", par.energy(), \
            "eta:", par.eta(), \
            "vtx rho:", par.vertex().rho(), \
            "vtx z", par.vertex().z(), \
            "status:", par.status(), \
            # Fore.RED + "SimVertex:" + vtx if vtx!='' else '', \
            Style.RESET_ALL
        )

    daughters = par.daughterRefVector()
    size = daughters.size()
    for i, child in enumerate(daughters):
        s = '|' if i<size-1 else ' '
        PrintDecay(child, indent + d_indent + "  ", s, sim_obj)

def get_mother(gen, pdgId_mother):
    if gen.numberOfMothers() >= 1:
        if abs(gen.motherRef().pdgId()) != pdgId_mother:
            return gen
        else:
            return get_mother(gen.motherRef(), pdgId_mother)
    return gen

def isFrom(object_part, pdgId):
    mother = object_part.mother(0)
    if mother:
        if abs(mother.pdgId()) == pdgId: return True
        else: return isFrom(mother, pdgId)
    else: return False

def plot_lifetime(files, dir_out):
    
    print ("Task: plot_lifetime")
    # x: displacement [cm]
    disp_hists = ROOT.TH1D("disp","disp", 100, 0, 100)

    for f_name in files:

        print ("FILE: ", f_name)

        events = Events(f_name)

        # Gen par info
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticlePlusGeant'

        n_ev = 0
        for n_ev, ev in enumerate(events):
            # print ("event", n_ev)
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
                        disp_hists.Fill(disp / gamma)

    try:
        os.stat(dir_out)
    except:
        os.mkdir(dir_out)
    
    c = ROOT.TCanvas("c", "c", 1000, 800)
    disp_hists.GetXaxis().SetTitle("[cm]")
    disp_hists.SetTitle("|s#tau.vtx()-#tau.vtx()| / #gamma")
    disp_hists.Draw()
    disp_hists.GetXaxis().SetTitle("[cm]")
    # disp_hists.GetXaxis().SetRangeUser(0., 100.)
    disp_hists.SetLineColor(2)
    disp_hists.Draw("same")
    c.Print(dir_out + "/lifetime.png")

    c2 = ROOT.TCanvas("c2", "c2", 1000, 800)
    h2 = disp_hists.GetCumulative()
    h2.Scale(1.0 / disp_hists.GetEntries())
    # h2.GetXaxis().SetRangeUser(0., 100.)
    h2.GetXaxis().SetTitle("[cm]")
    h2.SetLineColor(2)
    h2.Draw("same")
    c2.Print(dir_out + "/lifetime_integral.png")

def vertex_diff(files, dir_out):
    '''
    function plots the difference between the vertex of gen particle and simulated vertex
    '''
    print ("Task: vertex_diff")
    
    all_xy = {
        "all" : [[], []],
        "tau_child" : [[], []],
        "tau_gen" : [[], []],
    }
    
    for f_name in files:

        print ("FILE: ", f_name)

        events = Events(f_name)

        # Tracks info part
        handleTracks = Handle('std::vector<SimTrack>')
        labelTracks = 'g4SimHits'
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticles'
        handleVertex = Handle('std::vector<SimVertex>')
        labelVertex = 'g4SimHits'
        
        n_ev = 0
        for n_ev, ev in enumerate(events):
            if n_ev % 100 == 0:
                print (n_ev, "events")
            
            ev.getByLabel(labelGEN, handleGEN)
            gen_particle = handleGEN.product()

            ev.getByLabel(labelTracks, handleTracks)
            tracks = handleTracks.product()

            ev.getByLabel(labelVertex, handleVertex)
            vertex = handleVertex.product()
            
            obj_list = SimObjects(vertex, tracks, gen_particle)
            
            for tr in tracks:
                if (not tr.noVertex()) and (not tr.noGenpart()):
                    # print "tracks:", tr.genpartIndex()-1, tr.vertIndex()
                    # print vertex[tr.vertIndex()].position().x(), vertex[tr.vertIndex()].position().y(), vertex[tr.vertIndex()].position().z()
                    # print gen_particle[tr.genpartIndex()-1].vertex().x(), gen_particle[tr.genpartIndex()-1].vertex().y(), gen_particle[tr.genpartIndex()-1].vertex().z()
                    dist = (vertex[tr.vertIndex()].position().x(
                            )-gen_particle[tr.genpartIndex()-1].vertex().x())**2
                    dist += (vertex[tr.vertIndex()].position().y() -
                                gen_particle[tr.genpartIndex()-1].vertex().y())**2
                    # dist += (vertex[tr.vertIndex()].position().z() -
                    #             gen_particle[tr.genpartIndex()-1].vertex().z())**2
                    dist = np.sqrt(dist)

                    # filter out low energy particles:
                    if abs(gen_particle[tr.genpartIndex()-1].pt()) < 3.0 or gen_particle[tr.genpartIndex()-1].pdgId() == 22:
                        continue
                                         
                    if isFrom(gen_particle[tr.genpartIndex()-1], 15):
                        all_xy["tau_child"][0].append(gen_particle[tr.genpartIndex()-1].vertex().rho())
                        all_xy["tau_child"][1].append(dist)
                        
                    if gen_particle[tr.genpartIndex()-1].pdgId() == 15:
                        all_xy["tau_gen"][0].append(gen_particle[tr.genpartIndex()-1].vertex().rho())
                        all_xy["tau_gen"][1].append(dist)

                    # if(gen_particle[tr.genpartIndex()-1].vertex().rho() > 30):
                    #     PrintDecay(gen_particle[tr.genpartIndex()-1].motherRef(),"","", obj_list)
                    #     input("Press Enter to continue...")
                    
                    all_xy["all"][0].append(gen_particle[tr.genpartIndex()-1].vertex().rho())
                    all_xy["all"][1].append(dist)

    tau_child = ROOT.TGraph(len(all_xy["tau_child"][0]), np.array(all_xy["tau_child"][0]), np.array(all_xy["tau_child"][1]))
    tau_child.SetMarkerStyle(8)
    tau_child.SetMarkerSize(0.5)
    tau_child.SetMarkerColor(3)
    
    tau_gen = ROOT.TGraph(len(all_xy["tau_gen"][0]), np.array(all_xy["tau_gen"][0]), np.array(all_xy["tau_gen"][1]))
    tau_gen.SetMarkerStyle(8)
    tau_gen.SetMarkerSize(0.5)
    tau_gen.SetMarkerColor(2)

    all_tgraph = ROOT.TGraph(len(all_xy["all"][0]), np.array(all_xy["all"][0]), np.array(all_xy["all"][1]))
    all_tgraph.GetXaxis().SetTitle("Transverse Displacment Gen-level [cm]")
    all_tgraph.GetYaxis().SetTitle("|#vec{SimVertex}-#vec{GenVertex}| [cm]")
    all_tgraph.GetXaxis().SetRangeUser(0, 100.0)
    all_tgraph.GetYaxis().SetRangeUser(0, 30.0)
    all_tgraph.SetMarkerStyle(8)
    all_tgraph.SetMarkerSize(0.5)
    all_tgraph.SetMarkerColor(4)

    c = ROOT.TCanvas("c", "c", 1000, 800)
    all_tgraph.Draw("ap")
    tau_child.Draw("p")
    tau_gen.Draw("p")
    
    # Draw bisector
    bisector = ROOT.TF1("bisector", "x", 0, 100)
    bisector.SetLineWidth(1)
    bisector.SetLineColor(1)
    bisector.Draw("same")
    
    legend = ROOT.TLegend(0.6, 0.8, 0.95, 0.95)
    legend.AddEntry(tau_child, "gen-part (from tau chain)", "p")
    legend.AddEntry(tau_gen, "gen-part (tau)", "p")
    legend.AddEntry(all_tgraph, "gen-part (all)", "p")
    legend.Draw("same")

    t = ROOT.TPaveText(.5,.4,.95,.78,"NDC")
    t.AddText("All point should be near the zero over the value in abs(diff) (y-axis).")
    t.AddText("Location of the points on the besector should be suspitious,")
    t.AddText("cooresponding would mean that for any gen-level vertex (x,y,z)")
    t.AddText("the sim-level vertex is (0,0,0).")
    t.Draw("same")
    
    c.Print(dir_out + "/vertex_gen_diff.png")

def vis_tau_mass(files, dir_out):
    '''
    calculate the mass of the tau decay products
    '''
    def calculate_visible(gen_particle):
        
        if gen_particle.status() == 8: return (0,0,0,0)
        
        daughters = gen_particle.daughterRefVector()
        size = daughters.size()
        
        if size==0:
            if abs(gen_particle.pdgId()) in [12, 14, 16]:
                return (0,0,0,0)
            else:
                return (gen_particle.px(), gen_particle.py(), gen_particle.pz(), gen_particle.energy())
        else:
            x,y,z,E = 0,0,0,0
            for i, child in enumerate(daughters):
                x_,y_,z_,E_ = calculate_visible(child)
                x += x_
                y += y_
                z += z_
                E += E_
            return (x,y,z,E)
    
    print ("Task: calculated_vis_mass")
    # x: displacement [cm]
    mass_hist = ROOT.TH1D("mass","mass", 60, 0, 2)

    for f_name in files:

        print ("FILE: ", f_name)

        events = Events(f_name)

        # Gen par info
       # Tracks info part
        handleTracks = Handle('std::vector<SimTrack>')
        labelTracks = 'g4SimHits'
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticlePlusGeant'
        handleVertex = Handle('std::vector<SimVertex>')
        labelVertex = 'g4SimHits'
        
        n_ev = 0
        for n_ev, ev in enumerate(events):
            
            ev.getByLabel(labelGEN, handleGEN)
            gen_particle = handleGEN.product()
            ev.getByLabel(labelTracks, handleTracks)
            tracks = handleTracks.product()
            ev.getByLabel(labelVertex, handleVertex)
            vertex = handleVertex.product()
            
            obj_list = SimObjects(vertex, tracks, gen_particle)
            for gen in gen_particle:
                if abs(gen.pdgId())==15 and gen.statusFlags().isLastCopy():
                    x,y,z,E = calculate_visible(gen)
                    delta = E**2 - x**2 - y**2 - z**2
                    if delta<0: continue #floating point issues
                    mass = math.sqrt(delta)
                    mass_hist.Fill(mass)
                    # if mass>1.75:
                    #     print ("mass: ", mass)
                    #     PrintDecay(gen.motherRef(),"","", obj_list)
                    #     input("Press Enter to continue...")
                    
    try:
        os.stat(dir_out)
    except:
        os.mkdir(dir_out)

    c = ROOT.TCanvas("c", "c", 1000, 800)
    c.SetLogy()
    mass_hist.GetXaxis().SetTitle("[cm]")
    mass_hist.SetTitle("vissible components of the tau decay products")
    mass_hist.GetXaxis().SetTitle("[GeV]")
    mass_hist.SetLineColor(2)
    mass_hist.Draw()
    c.Print(dir_out + "/tau_mass.png")

def energy_sharing(files, dir_out):

    print ("Task: energy sharing")
    # x: displacement [cm]
    energy_sharing = ROOT.TH2D("energy_delta","energy_delta", 100, 0, 300, 100, -2, 2)

    for f_name in files:

        print ("FILE: ", f_name)

        events = Events(f_name)

        # Gen par info
        handleTracks = Handle('std::vector<SimTrack>')
        labelTracks = 'g4SimHits'
        handleGEN = Handle('std::vector<reco::GenParticle>')
        labelGEN = 'genParticlePlusGeant'
        # labelGEN = 'genParticles'
        handleVertex = Handle('std::vector<SimVertex>')
        labelVertex = 'g4SimHits'
        n_ev = 0
        for n_ev, ev in enumerate(events):           
            ev.getByLabel(labelGEN, handleGEN)
            gen_particle = handleGEN.product()
            ev.getByLabel(labelTracks, handleTracks)
            tracks = handleTracks.product()
            ev.getByLabel(labelVertex, handleVertex)
            vertex = handleVertex.product()
            obj_list = SimObjects(vertex, tracks, gen_particle)
            for gen in gen_particle:
                if abs(gen.pdgId()) == 15:
                    daughters = gen.daughterRefVector()
                    E_childs = 0.0
                    is_fusion_process = False
                    has_daughters = False
                    for i, child in enumerate(daughters):
                        has_daughters = True
                        if child.numberOfMothers() > 1:
                            is_fusion_process = True
                        E_childs += child.energy()
                    if not is_fusion_process and has_daughters:
                        energy_sharing.Fill(gen.energy(), (gen.energy()-E_childs)/gen.energy())
                        # if (gen.energy()-E_childs)/gen.energy() < -0.9:
                        #     PrintDecay(daughters[0].motherRef(),"","", obj_list)
                        #     input("Press Enter to continue...")
                
                    
    try:
        os.stat(dir_out)
    except:
        os.mkdir(dir_out)

    c = ROOT.TCanvas("c", "c", 1000, 800)
    energy_sharing.GetXaxis().SetTitle("[cm]")
    energy_sharing.SetTitle("(mother_energy - children_energy)/mother_energy")
    energy_sharing.GetXaxis().SetTitle("mother_energy [GeV]")
    energy_sharing.GetYaxis().SetTitle("(mother_energy - children_energy)/mother_energy [GeV]")
    energy_sharing.Draw("colz")
    c.Print(dir_out + "/energy_sharing.png")

def main():
    '''
    Main function reads from the input arguments:
    1) the input file
    2) the output foler path
    3) list of functions to test
    4) number of events to process
    example of use:
    > python3 ./FWLite_GEN-SIM-testall.py SUS-RunIISummer20UL16GEN-000XX.root mc_tests_output
              --function_list plot_lifetime,vertex_diff
    
    List of tests:
    
    1.G4 + pythia decay duplication:
    2. Reseting the vertex to 0,0,0:
    python3 ./FWLite_GEN-SIM-testall.py ~/GEN-SIM-TESTs/SUS-RunIIFall18GS-00022_removeLine.root
            ./mc_tests_output_duplication --function_list energy_sharing,vis_tau_mass,vertex_diff,plot_lifetime 
    '''
    
    parser = argparse.ArgumentParser(description='Process some inputs.')
    parser.add_argument('input_file', type=str, help='path to input file')
    parser.add_argument('output_folder', type=str, help='path to output folder')
    parser.add_argument('--function_list', type=str, help='comma-separated list of functions to test', required=True)
    args = parser.parse_args()

    # Perform the specified actions with the input arguments
    print("Input file:", args.input_file)
    print("Output folder:", args.output_folder)
    print("Function list:", args.function_list.split(','))
    
    if "plot_lifetime" in args.function_list.split(','):
        plot_lifetime([args.input_file], args.output_folder)
        
    if "vertex_diff" in args.function_list.split(','):
        vertex_diff([args.input_file], args.output_folder)
        
    if "vis_tau_mass" in args.function_list.split(','):
        vis_tau_mass([args.input_file], args.output_folder)
    
    if "energy_sharing" in args.function_list.split(','):
        energy_sharing([args.input_file], args.output_folder)
    

if __name__ == '__main__':
    main()
