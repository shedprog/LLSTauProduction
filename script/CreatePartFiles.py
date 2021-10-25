import os
from itertools import product

root_dir = os.path.dirname(os.path.abspath(__file__))
directory_out = root_dir+'/../Configuration/ParticleFiles'

try:
    os.stat(directory_out)
except:
    os.mkdir(directory_out)

baseParticleFile="""
BLOCK MASS
#  PDG code   mass   particle
   1000015    %MSTAU%  # ~tau_1
   1000022    %MLSP%  # ~chi_10
Block
# DECAY TABLE
DECAY    1000015  %CTAU% # tau + ~chi_10
#          BR          NDA       ID1     ID2
           1.0         2          15    1000022
"""

hBarCinGeVmm = 1.973269788e-13

mstau_list = [100,250,400]
mlsp_list  = [1, 20]
ctau0_list  = [1000]

grid = list(product(*[mstau_list, mlsp_list, ctau0_list]))
print "create:",len(grid),"files"

for mstau, mlsp, ctau0 in grid:
    print "mstau:",mstau,"mlsp:",mlsp,"ctau:",ctau0
    ctau = hBarCinGeVmm/ctau0
    ParticleFile = baseParticleFile.replace('%MSTAU%','%e' % mstau)
    ParticleFile = ParticleFile.replace('%MLSP%','%e' % mlsp)
    ParticleFile = ParticleFile.replace('%CTAU%','%e' % ctau)
    f = open(directory_out + ("/particles_stau_mstau{}GeV_mlsp{}GeV_ctau{}mm.txt"
        .format(mstau,mlsp, ctau0)), "w")
    f.write(ParticleFile)
    f.close()

print "done"